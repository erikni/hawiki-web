"""Check that generated HTML links resolve to local files.

Run after ``tools/build.py``. External URLs and fragment-only links are skipped;
relative links and root-relative links are checked against the ``dist`` tree.
A missing file raises an error and causes a nonzero exit code for Pages builds.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

OUTPUT_DIRECTORY = Path(__file__).resolve().parent.parent / "dist"


class LocalLinkChecker(HTMLParser):
    """Validate href and src attributes in one generated HTML document."""

    def __init__(self, page: Path, output_directory: Path) -> None:
        """Remember the document and output root used to resolve local paths."""
        super().__init__()
        self.page = page
        self.output_directory = output_directory

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        """Check local link targets on an opening tag.

        The tag name is unused: any element with href or src can reference a
        local file. Directory URLs resolve to their generated ``index.html``.
        """
        for attribute, value in attrs:
            if attribute not in ("href", "src") or not value:
                continue
            self.check_link(value)

    def check_link(self, value: str) -> None:
        """Resolve one local URL and report a missing target with its source page."""
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return

        decoded_path = unquote(parsed.path)
        if parsed.path.startswith("/"):
            target = self.output_directory / decoded_path.lstrip("/")
        else:
            target = self.page.parent / decoded_path
        if parsed.path.endswith("/"):
            target /= "index.html"
        if not target.is_file():
            raise FileNotFoundError(f"{self.page}: {value}")


def main() -> None:
    """Validate every generated HTML page, failing if no build output exists."""
    pages = sorted(OUTPUT_DIRECTORY.rglob("*.html"))
    if not pages:
        raise FileNotFoundError("No generated HTML found; run tools/build.py first.")

    for page in pages:
        checker = LocalLinkChecker(page, OUTPUT_DIRECTORY)
        checker.feed(page.read_text(encoding="utf-8"))
        checker.close()
    print("Ověřeny odkazy a lokální soubory všech HTML stránek.")


if __name__ == "__main__":
    main()
