"""Check canonical, hreflang, schema and sitemap consistency for every site."""

import json
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent


class MetadataParser(HTMLParser):
    """Collect headings, link metadata, Open Graph and JSON-LD."""

    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.canonicals = []
        self.alternates = {}
        self.meta = {}
        self.schemas = []
        self.in_schema = False
        self.schema_text = ""

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonicals.append(attributes.get("href"))
        if tag == "link" and attributes.get("rel") == "alternate":
            self.alternates[attributes.get("hreflang")] = attributes.get("href")
        if tag == "meta":
            key = attributes.get("name", attributes.get("property"))
            self.meta[key] = attributes.get("content")
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self.in_schema = True
            self.schema_text = ""

    def handle_data(self, data):
        if self.in_schema:
            self.schema_text += data

    def handle_endtag(self, tag):
        if tag == "script" and self.in_schema:
            self.schemas.extend(json.loads(self.schema_text))
            self.in_schema = False


def sitemap_urls(output: Path) -> list[str]:
    """Read all locations from one generated sitemap."""
    return [node.text for node in ET.parse(output / "sitemap.xml").iter()
            if node.tag.endswith("}loc")]


def check_site(language: str, settings: dict) -> dict[str, MetadataParser]:
    """Validate every generated page for one language."""
    output = ROOT / settings["outputDirectory"]
    origin = settings["url"].rstrip("/")
    urls = sitemap_urls(output)
    assert len(urls) == len(set(urls)), f"{language}: duplicate sitemap URL"
    generated = set()
    parsed_pages = {}
    for path in sorted(output.rglob("index.html")):
        route = path.parent.relative_to(output).as_posix()
        route = "" if route == "." else route
        expected = origin + "/" + (route + "/" if route else "")
        parsed = MetadataParser()
        parsed.feed(path.read_text(encoding="utf-8"))
        assert parsed.h1_count == 1, path
        assert parsed.canonicals == [expected], path
        assert parsed.meta.get("description"), path
        assert parsed.meta.get("og:url") == expected, path
        assert parsed.meta.get("og:locale") == settings["ogLocale"], path
        for field in ("og:title", "og:description", "og:type", "og:image"):
            assert parsed.meta.get(field), (path, field)
        if route:
            assert any(item["@type"] == "BreadcrumbList" for item in parsed.schemas), path
        else:
            assert {item["@type"] for item in parsed.schemas} == {"WebSite", "Organization"}
        for schema in parsed.schemas:
            if schema["@type"] == "Article":
                assert schema["mainEntityOfPage"] == expected, path
                assert schema["inLanguage"] == settings["language"], path
        generated.add(expected)
        parsed_pages[expected] = parsed
    assert generated == set(urls), f"{language}: sitemap does not match generated routes"
    robots = (output / "robots.txt").read_text(encoding="utf-8")
    assert "Sitemap: " + origin + "/sitemap.xml" in robots
    assert "Disallow: /" not in robots
    return parsed_pages


def main():
    """Validate both site trees and reciprocal localized alternatives."""
    sites = json.loads((ROOT / "sites.json").read_text(encoding="utf-8"))
    all_pages = {}
    total = 0
    for language, settings in sites.items():
        pages = check_site(language, settings)
        all_pages.update(pages)
        total += len(pages)
    for url, parsed in all_pages.items():
        for language, alternate in parsed.alternates.items():
            if language == "x-default":
                continue
            assert alternate in all_pages, (url, language, alternate)
            target = all_pages[alternate]
            source_language = next(
                key for key, settings in sites.items()
                if url.startswith(settings["url"].rstrip("/") + "/")
            )
            assert target.alternates.get(source_language) == url, (url, alternate)
    print(f"Ověřeno SEO, JSON-LD, hreflang a sitemap všech {total} stránek.")


if __name__ == "__main__":
    main()
