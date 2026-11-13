"""Check canonical metadata, schema and sitemap consistency after a build."""
import json
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "https://www.hawiki.cz"


class MetadataParser(HTMLParser):
    """Collect headings, canonical links and JSON-LD from generated HTML."""

    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.canonicals = []
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


def main():
    """Assert every generated route has consistent metadata and sitemap membership."""
    output = ROOT / "dist"
    urls = [node.text for node in ET.parse(output / "sitemap.xml").iter()
            if node.tag.endswith("}loc")]
    assert len(urls) == len(set(urls)), "Duplicate sitemap URL"
    generated = set()
    for path in sorted(output.rglob("index.html")):
        route = path.parent.relative_to(output).as_posix()
        expected = ORIGIN + "/" + (route + "/" if route != "." else "")
        parsed = MetadataParser()
        parsed.feed(path.read_text(encoding="utf-8"))
        assert parsed.h1_count == 1, path
        assert parsed.canonicals == [expected], path
        assert parsed.meta.get("description"), path
        assert parsed.meta.get("og:url") == expected, path
        for field in ("og:title", "og:description", "og:type", "og:image"):
            assert parsed.meta.get(field), (path, field)
        if route != ".":
            assert any(item["@type"] == "BreadcrumbList" for item in parsed.schemas), path
        else:
            assert {item["@type"] for item in parsed.schemas} == {"WebSite", "Organization"}
            assert 140 <= len(parsed.meta["description"]) <= 160
        for schema in parsed.schemas:
            if schema["@type"] == "Article":
                assert schema["mainEntityOfPage"] == expected, path
        generated.add(expected)
    assert generated == set(urls), "Sitemap does not match generated routes"
    robots = (output / "robots.txt").read_text(encoding="utf-8")
    assert "Sitemap: " + ORIGIN + "/sitemap.xml" in robots
    assert "Disallow: /" not in robots
    print(f"Ověřeno SEO, JSON-LD a sitemap všech {len(generated)} stránek.")


if __name__ == "__main__":
    main()
