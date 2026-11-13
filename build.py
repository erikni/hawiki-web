"""Generate the static HAwiki.cz website from Markdown articles.

Run ``python3 build.py`` from any working directory. Source content lives in
``obsah/``, HTML source templates in ``sablony/`` and shared assets in ``assets/``.
Generated pages and the search index are written to ``dist/``.
"""

import html
import importlib
import json
import re
from pathlib import Path
import shutil
from string import Template
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / ".vendor"))
from responsive_images import render_hero
OUTPUT_DIRECTORY = ROOT / "dist"
SECTIONS = {
    "zaciname": ("Začínáme", "Váš první krok k pohodlnější domácnosti."),
    "co-chci-usnadnit": ("Co chci usnadnit", "Vyberte si podle běžného života."),
    "co-koupit": ("Co koupit", "Nejdřív potřeba, potom nákup."),
    "navody": ("Návody", "Malé kroky s konkrétním výsledkem."),
    "pomoc": ("Pomoc", "Když něco nefunguje, začněte tady."),
    "novinky": ("Novinky", "Týdenní přehled dění kolem Home Assistant a chytré domácnosti."),
    "ai": ("AI", "Modely, hlas a agenti pro chytrou domácnost."),
    "dalsi-moznosti": ("Další možnosti", "Rozšíření pro váš další krok."),
}
SEO = json.loads((ROOT / "seo.json").read_text(encoding="utf-8"))
GENERATED_ROUTES = set()

REQUIRED_METADATA = (
    "title", "description", "cas", "obtiznost", "kontrola_zdroju", "stav",
)
PRACTICAL_ARTICLES = {
    "co-chci-usnadnit/svetla",
    "navody/lampa-vecer",
    "pomoc/zalohovani",
}
HOMEPAGE_INTEGRATIONS = [
    ("Google Kalendář", "integrace/google-calendar-home-assistant"),
    ("MQTT", "integrace/mqtt-home-assistant"),
    ("SmartThings", "integrace/smartthings-home-assistant"),
    ("Sonos", "integrace/sonos-home-assistant"),
]


def render_template(name: str, **values: str) -> str:
    """Substitute values into an HTML source template.

    Callers escape plain text before passing it here. Rendered Markdown and
    other HTML fragments are intentionally inserted unchanged.
    """
    path = ROOT / "sablony" / f"{name}.html"
    return Template(path.read_text(encoding="utf-8")).substitute(values)


def load_pages() -> list[dict[str, str]]:
    """Read YAML metadata and render each Markdown article with its contents.

    Dependencies can be installed locally in ``.vendor`` or in the active Python
    environment. Missing metadata produces an error identifying the source file.
    """
    sys.path.insert(0, str(ROOT / ".vendor"))
    markdown = importlib.import_module("markdown")
    yaml = importlib.import_module("yaml")
    pages = []

    for path in sorted((ROOT / "obsah").rglob("*.md")):
        _, front_matter, body = path.read_text(encoding="utf-8").split("---", 2)
        metadata = yaml.safe_load(front_matter)
        if not isinstance(metadata, dict):
            raise ValueError(f"{path}: metadata must be a YAML mapping")
        if metadata.get("type") == "hub":
            continue
        missing = [key for key in REQUIRED_METADATA if key not in metadata]
        if missing:
            raise ValueError(f"{path}: missing metadata: {', '.join(missing)}")

        slug = path.relative_to(ROOT / "obsah").with_suffix("").as_posix()
        converter = markdown.Markdown(
            extensions=["toc", "tables", "fenced_code", "codehilite", "admonition"]
        )
        pages.append({
            **metadata,
            "slug": slug,
            "body": converter.convert(body),
            "toc": converter.toc,
            "citations": re.findall(r"\]\((https?://[^\s)]+)\)",
                re.split(r"(?m)^## Zdroje?\s*$", body)[-1])
                if re.search(r"(?m)^## Zdroje?\s*$", body) else [],
        })

    return pages


def render_cards(pages: list[dict[str, str]]) -> str:
    """Render linked article cards from their display metadata."""
    cards = [
        render_template(
            "card",
            slug=html.escape(page["slug"]),
            difficulty=html.escape(page["obtiznost"]),
            duration=html.escape(page["cas"]),
            title=html.escape(page["title"]),
            description=html.escape(page["description"]),
        )
        for page in pages
    ]
    return '<div class="cards">' + "".join(cards) + "</div>"


def article_metadata(article: dict, canonical_url: str, config: dict, properties: dict) -> dict:
    """Build article schema and extend Open Graph from known source metadata."""
    section_title = section_label(article["slug"].split("/")[0])
    properties["article:section"] = section_title
    topics = article.get("temata", [])
    if not isinstance(topics, list) or not all(isinstance(t, str) for t in topics):
        raise ValueError(f"{article["slug"]}: temata must be a list of strings")
    data = {
        "@context": "https://schema.org", "@type": "Article",
        "@id": canonical_url + "#article", "url": canonical_url,
        "mainEntityOfPage": canonical_url, "headline": article["title"],
        "description": article["description"], "inLanguage": config["language"],
        "articleSection": section_title,
        "publisher": {"@type": "Organization", "name": config["name"],
                      "url": config["url"] + "/"},
        "about": {"@type": "SoftwareApplication", "name": "Home Assistant",
                  "url": "https://www.home-assistant.io/"},
    }
    if topics:
        data["keywords"] = topics
    if article["citations"]:
        data["citation"] = article["citations"]
    for field, schema_key, og_key in (
        ("publikovano", "datePublished", "article:published_time"),
        ("aktualizovano", "dateModified", "article:modified_time"),
    ):
        if article.get(field):
            data[schema_key] = str(article[field])
            properties[og_key] = str(article[field])
    if article.get("autor"):
        data["author"] = [{"@type": "Person", "name": name}
                          for name in author_names(article)]
    # Escape HTML-sensitive characters so content cannot close the script.
    return data


def page_metadata(route: str, title: str, description: str,
                  article: dict | None = None, breadcrumb_title: str | None = None) -> tuple:
    """Render Open Graph and schema using the common canonical origin."""
    config = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
    canonical_url = config["url"] + "/" + (route + "/" if route else "")
    image_url = config["url"].rstrip("/") + "/assets/social-card.png"
    properties = {
        "og:title": title, "og:description": description,
        "og:type": "article" if article else "website",
        "og:url": canonical_url, "og:site_name": config["name"],
        "og:locale": "cs_CZ", "og:image": image_url,
        "og:image:type": "image/png", "og:image:width": "1200",
        "og:image:height": "630",
        "og:image:alt": "HAwiki.cz – Home Assistant srozumitelně",
    }
    schemas = []
    structured_data = ""
    if not route:
        schemas.extend([
            {"@context": "https://schema.org", "@type": "WebSite",
             "@id": canonical_url + "#website", "url": canonical_url,
             "name": config["name"], "inLanguage": config["language"]},
            {"@context": "https://schema.org", "@type": "Organization",
             "@id": canonical_url + "#organization", "url": canonical_url,
             "name": config["name"]},
        ])
    if route:
        crumbs = breadcrumb_items(
            route, article["title"] if article else (breadcrumb_title or title))
        schemas.append({"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": position,
                "name": label, "item": config["url"] + "/" + (path + "/" if path else "")}
                for position, (label, path) in enumerate(crumbs, 1)]})
    tags = []
    if article:
        schemas.append(article_metadata(article, canonical_url, config, properties))
        tags = article.get("temata", [])
    if schemas:
        encoded = json.dumps(schemas, ensure_ascii=False).replace("<", "\\u003c")
        structured_data = '<script type="application/ld+json">' + encoded + '</script>'
    open_graph = "\n".join(
        f'<meta property="{key}" content="{html.escape(value, quote=True)}">'
        for key, value in [*properties.items(), *(("article:tag", t) for t in tags)]
    )
    return open_graph, structured_data


def write_page(route: str, title: str, description: str, body: str,
               article: dict | None = None, **options) -> None:
    """Wrap page content in the common layout and save its UTF-8 index file.

    Routes are relative to the output root. An empty route writes the homepage.
    The canonical origin is taken from ``site.json``.
    """
    config = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
    canonical_url = config["url"].rstrip("/") + "/"
    if route:
        canonical_url += route + "/"
    navigation = "".join(
        f'<a href="/{key}/">{html.escape(section[0])}</a>'
        for key, section in SECTIONS.items() if key not in {"dalsi-moznosti", "co-chci-usnadnit"}
    )
    open_graph, structured_data = page_metadata(
        route, title, description, article, options.get("breadcrumb_title"))
    document = render_template(
        "layout",
        title=html.escape(title + " | " + config["name"]),
        description=html.escape(description),
        canonical_url=html.escape(canonical_url),
        navigation=navigation,
        open_graph=open_graph,
        structured_data=structured_data,
        body=body,
    )
    GENERATED_ROUTES.add(route)
    path = OUTPUT_DIRECTORY / route / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding="utf-8")


def write_articles(pages: list[dict[str, str]]) -> None:
    """Generate an article page with breadcrumbs and a table of contents."""
    for page in pages:
        section = page["slug"].split("/")[0]
        body = render_template(
            "article",
            section=html.escape(section),
            section_title=html.escape(section_label(section)),
            breadcrumbs=render_breadcrumbs(page["slug"], page["title"]),
            next_steps=render_next_steps(page, pages),
            difficulty=html.escape(page["obtiznost"]),
            duration=html.escape(page["cas"]),
            title=html.escape(page["title"]),
            description=html.escape(page["description"]),
            hero_image=render_hero(page, ROOT, OUTPUT_DIRECTORY),
            review_date=html.escape(page["kontrola_zdroju"]),
            topic_labels=(
                '<ul class="topic-labels" aria-label="Témata článku">'
                + "".join(
                    render_topic_label(topic)
                    for topic in page.get("temata", [])
                )
                + '</ul>'
            ) if page.get("temata") else "",
            review_status=html.escape(page["stav"]),
            editorial_metadata=render_editorial_metadata(page),
            content=page["body"],
            table_of_contents=page["toc"],
        )
        write_page(page["slug"], page.get("seoTitle", page["title"]),
                   page["description"], body, article=page)


def write_sections(pages: list[dict[str, str]]) -> None:
    """Generate a listing page for every configured content section."""
    for key, (title, description) in SECTIONS.items():
        settings = SEO["sections"].get(key, {})
        title = settings.get("heading", title)
        description = settings.get("description", description)
        section_pages = [page for page in pages if page["slug"].startswith(key + "/")]
        section_extra = ""
        if key == "navody":
            section_extra = (
                '<section class="directory-callout" aria-labelledby="navody-integrace">'
                '<div><span class="eyebrow">PROPOJENÍ ZAŘÍZENÍ A SLUŽEB</span>'
                '<h2 id="navody-integrace">Hledáte konkrétní integraci?</h2>'
                '<p>Vyberte zařízení nebo službu a zjistěte, jak je propojit s Home Assistantem.</p>'
                '</div><a class="button" href="/integrace/">Prohlédnout integrace →</a>'
                '</section>'
            )
        body = render_template(
            "section",
            title=html.escape(title),
            description=html.escape(description),
            cards=render_cards(section_pages),
            breadcrumbs=render_breadcrumbs(key, title),
            learning_path=render_learning_path(pages) if key == "zaciname" else "",
            section_extra=section_extra,
        )
        write_page(key, settings.get("title", title), description, body,
                   breadcrumb_title=title)


def write_homepage(pages: list[dict[str, str]]) -> None:
    """Generate the homepage with beginner guides and selected practical articles."""
    page_slugs = {page["slug"] for page in pages}
    missing_integrations = [
        slug for _, slug in HOMEPAGE_INTEGRATIONS if slug not in page_slugs
    ]
    if missing_integrations:
        raise ValueError(
            "Homepage integration links reference missing articles: "
            + ", ".join(missing_integrations)
        )
    body = render_template(
        "home",
        topic_links=render_topic_links(),
        integration_links=render_link_list(HOMEPAGE_INTEGRATIONS),
        use_cases=render_link_list(SEO["useCases"]),
        starter_cards=render_cards(
            [page for page in pages if page["slug"].startswith("zaciname/")]
        ),
        news_cards=render_cards(sorted(
            [page for page in pages if page["slug"].startswith("novinky/")],
            key=lambda page: page["slug"], reverse=True,
        )[:3]),
        practical_cards=render_cards(
            [page for page in pages if page["slug"] in PRACTICAL_ARTICLES]
        ),
    )
    write_page(
        "",
        "Home Assistant česky: návody pro chytrou domácnost",
        "Home Assistant česky: návody, výběr zařízení a automatizace krok za krokem. "
        "Zjistěte, jak může chytrá domácnost usnadnit každý den, a začněte jednou změnou.",
        body,
    )


def write_search(pages: list[dict[str, str]]) -> None:
    """Generate the search page and the article metadata consumed by its script."""
    write_page(
        "hledani", "Hledání", "Najděte návod podle toho, co potřebujete.",
        render_template("search"),
    )
    index = [
        {key: page[key] for key in ("title", "description", "slug")}
        for page in pages
    ]
    (OUTPUT_DIRECTORY / "search.json").write_text(
        json.dumps(index, ensure_ascii=False), encoding="utf-8"
    )




def author_names(page: dict) -> list:
    """Support one author name or several names without inventing attribution."""
    authors = page.get("autor", [])
    if isinstance(authors, str):
        authors = [authors]
    if not isinstance(authors, list) or not all(isinstance(name, str) for name in authors):
        raise ValueError(f'{page["slug"]}: autor must be a name or list of names')
    return authors


def render_editorial_metadata(page: dict) -> str:
    """Display only known authors, editorial dates and declared verification."""
    entries = []
    if page.get("autor"):
        entries.append("Autor: " + ", ".join(author_names(page)))
    for key, label in (("publikovano", "Publikováno: "), ("aktualizovano", "Aktualizováno: ")):
        if page.get(key):
            entries.append(label + str(page[key]))
    source_labels = {
        "official-docs": "Podle oficiální dokumentace", "tested": "Prakticky testováno",
        "editorial": "Redakční doporučení", "mixed": "Dokumentace a praktická zkušenost"}
    if page.get("sourceType"):
        if page["sourceType"] not in source_labels:
            raise ValueError(f'{page["slug"]}: unsupported sourceType')
        entries.append("Typ: " + source_labels[page["sourceType"]])
    if page.get("testedOn"):
        entries.append("Testováno na: " + str(page["testedOn"]))
    if not entries:
        return ""
    return '<p class="review">' + " · ".join(html.escape(entry) for entry in entries) + '</p>'


def section_label(section: str) -> str:
    """Return the existing menu label or a configured topic label."""
    if section in SECTIONS:
        return SECTIONS[section][0]
    return SEO["topics"].get(section, {}).get("label", section.replace("-", " ").capitalize())


def breadcrumb_items(route: str, title: str) -> list:
    """Use the same complete breadcrumb path for visible HTML and JSON-LD."""
    items = [("HAwiki", "")]
    parts = route.split("/")
    for index in range(1, len(parts)):
        parent = "/".join(parts[:index])
        items.append((section_label(parent), parent))
    items.append((title, route))
    return items


def render_breadcrumbs(route: str, title: str) -> str:
    """Render navigation with an accessible current-page label."""
    items = breadcrumb_items(route, title)
    return '<nav class="crumb" aria-label="Drobečková navigace"><ol>' + "".join(
        '<li>' + ('<span aria-current="page">' + html.escape(label) + '</span>'
        if index == len(items) - 1 else
        f'<a href="/{path + "/" if path else ""}">{html.escape(label)}</a>') + '</li>'
        for index, (label, path) in enumerate(items)
    ) + '</ol></nav>'


def render_link_list(items: list) -> str:
    """Render small navigational cards without a client-side dependency."""
    return '<ul class="link-grid">' + "".join(
        f'<li><a href="/{html.escape(path)}/">{html.escape(label)}</a></li>'
        for label, path in items
    ) + '</ul>'


def render_topic_links() -> str:
    """Link established topics and existing hardware, energy and voice guides."""
    return render_link_list([(topic["label"], route)
        for route, topic in SEO["topics"].items()] + [
        ("Shelly", "co-koupit/shelly-zarizeni-prehled"), ("Hardware", "co-koupit"),
        ("Energie", "navody/prehled-spotreby-elektriny"), ("Hlas a AI", "ai")])


def render_topic_label(topic: str) -> str:
    """Link curated topic labels; other labels remain ordinary text."""
    for route, settings in SEO["topics"].items():
        if topic.casefold() in [tag.casefold() for tag in settings["tags"]]:
            return f'<li class="topic-label"><a href="/{route}/">{html.escape(topic)}</a></li>'
    return f'<li class="topic-label">{html.escape(topic)}</li>'


def learning_steps(pages: list) -> list:
    """Use only steps whose actual source article exists."""
    slugs = {page["slug"] for page in pages}
    return [(label, slug) for label, slug in SEO["learningPath"] if slug in slugs]


def render_learning_path(pages: list) -> str:
    """Render the ordered beginner path above the existing article listing."""
    return '<section class="learning-path"><h2>Vaše cesta krok za krokem</h2><ol>' + "".join(
        f'<li><a href="/{slug}/">{html.escape(label)}</a></li>'
        for label, slug in learning_steps(pages)
    ) + '</ol></section>'


def page_topics(page: dict) -> list:
    """Match actual article tags and curated article membership to topic hubs."""
    tags = {tag.casefold() for tag in page.get("temata", [])}
    return [route for route, topic in SEO["topics"].items()
        if tags.intersection(tag.casefold() for tag in topic["tags"])
        or page["slug"] in topic["articles"] or page["slug"].startswith(route + "/")]


def related_articles(page: dict, pages: list, topics: list) -> list:
    """Prioritize declared links and shared topics over broad category matches."""
    by_slug = {item["slug"]: item for item in pages}
    explicit = page.get("related", [])
    if not isinstance(explicit, list) or any(slug not in by_slug for slug in explicit):
        raise ValueError(f'{page["slug"]}: related must reference existing article slugs')
    related = [by_slug[slug] for slug in explicit if slug != page["slug"]]
    tags = set(page.get("temata", []))
    candidates = [item for item in pages if item["slug"] != page["slug"]
        and item not in related and set(topics).intersection(page_topics(item))]
    related += sorted(candidates, key=lambda item:
        2 * len(tags.intersection(item.get("temata", [])))
        + len(set(topics).intersection(page_topics(item))), reverse=True)
    if not related:
        related = [item for item in pages if item["slug"] != page["slug"]
            and item["slug"].split("/")[0] == page["slug"].split("/")[0]]
    return related


def render_next_steps(page: dict, pages: list) -> str:
    """Share previous/next steps and bounded, deterministic related guides."""
    links = []
    path = learning_steps(pages)
    positions = [index for index, (_, slug) in enumerate(path) if slug == page["slug"]]
    if positions:
        index = positions[0]
        for position, label in ((index - 1, "← Předchozí krok: "), (index + 1, "Další krok → ")):
            if 0 <= position < len(path):
                name, slug = path[position]
                links.append((label + name, slug))
    topics = page_topics(page)
    for route in topics:
        links.append(("Téma: " + SEO["topics"][route]["label"], route))
    related = related_articles(page, pages, topics)
    return '<section class="next-steps"><h2>Co dál</h2>' + render_link_list(links) + (
        '<h3>Související návody</h3>' + render_link_list([
            (item["title"], item["slug"]) for item in related[:3]]) if related else ""
    ) + '</section>'


def write_hubs(pages: list) -> None:
    """Render editorial Markdown introductions and configured article groups."""
    yaml = importlib.import_module("yaml")
    markdown = importlib.import_module("markdown")
    for path in sorted((ROOT / "obsah").rglob("index.md")):
        _, front_matter, source = path.read_text(encoding="utf-8").split("---", 2)
        metadata = yaml.safe_load(front_matter)
        if metadata.get("type") != "hub":
            continue
        route = path.parent.relative_to(ROOT / "obsah").as_posix()
        content = markdown.markdown(source, extensions=["tables"])
        topic = SEO["topics"].get(route)
        if topic:
            by_slug = {page["slug"]: page for page in pages}
            for slug in [topic["start"], *topic["articles"], *topic["help"]]:
                if slug not in by_slug:
                    raise ValueError(f"{route}: missing curated article {slug}")
            content += '<h2>Doporučený start</h2>' + render_cards([by_slug[topic["start"]]])
            content += '<h2>Články a návody</h2>' + render_cards([
                page for page in pages
                if route in page_topics(page) and page["slug"] != topic["start"]])
            content += '<h2>Řešení problémů</h2>' + render_cards(
                [by_slug[slug] for slug in topic["help"]])
            content += '<h2>Související témata</h2>' + render_link_list([
                (SEO["topics"][key]["label"], key) for key in topic["related"]])
        body = render_template("hub", title=html.escape(metadata["title"]),
            description=html.escape(metadata["description"]), content=content,
            breadcrumbs=render_breadcrumbs(route, metadata["title"]),
            review_metadata=(
                '<p class="review">Kontrola zdrojů: <time datetime="'
                + html.escape(metadata["kontrola_zdroju"]) + '">'
                + html.escape(metadata["kontrola_zdroju"]) + '</time></p>'
            ) if metadata.get("kontrola_zdroju") else "")
        write_page(route, metadata.get("seoTitle", metadata["title"]),
                   metadata["description"], body, breadcrumb_title=metadata["title"])


def write_sitemap() -> None:
    """Include only indexable routes generated in this build, never stale files."""
    origin = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))["url"]
    if origin != "https://www.hawiki.cz":
        raise ValueError("Canonical hostname must be https://www.hawiki.cz")
    ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    sitemap = ET.Element(namespace + "urlset")
    for route in sorted(GENERATED_ROUTES):
        entry = ET.SubElement(sitemap, namespace + "url")
        ET.SubElement(entry, namespace + "loc").text = origin + "/" + (route + "/" if route else "")
    ET.ElementTree(sitemap).write(
        OUTPUT_DIRECTORY / "sitemap.xml", encoding="utf-8", xml_declaration=True)


def main() -> None:
    """Build articles, section listings, homepage, search index and shared assets."""
    OUTPUT_DIRECTORY.mkdir(exist_ok=True)
    GENERATED_ROUTES.clear()
    pages = load_pages()
    write_articles(pages)
    write_sections(pages)
    write_homepage(pages)
    write_search(pages)
    write_hubs(pages)
    shutil.copytree(ROOT / "assets", OUTPUT_DIRECTORY / "assets", dirs_exist_ok=True)
    shutil.copytree(ROOT / "static", OUTPUT_DIRECTORY, dirs_exist_ok=True)
    write_sitemap()
    print(f"Vytvořeno {len(GENERATED_ROUTES)} HTML stránek.")


if __name__ == "__main__":
    main()
