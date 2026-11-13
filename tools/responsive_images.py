"""Generate responsive encodings of article illustrations during the build."""
import html
import warnings
from pathlib import Path
from PIL import Image, ImageOps


def render_hero(page, root: Path, output: Path) -> str:
    url = page.get('obrazek')
    if not url:
        return ''
    # Only repository assets are accepted; never fetch arbitrary metadata URLs.
    relative = Path(url.lstrip('/'))
    source = (root / relative).resolve()
    if not url.startswith('/assets/') or not source.is_relative_to((root / 'assets').resolve()):
        raise ValueError(f'Unsupported article image: {url}')
    with Image.open(source) as original:
        width, height = original.size
        try:
            image = ImageOps.exif_transpose(original).convert('RGB')
        except OSError as error:
            warnings.warn(f'Image not optimized; keeping original {url}: {error}')
            return (
                '<figure class="article-hero"><img src="' + html.escape(url, quote=True)
                + '" alt="' + html.escape(page.get('obrazek_alt', ''), quote=True)
                + f'" width="{width}" height="{height}"'
                + ' style="width:100%;height:auto;display:block;border-radius:16px" decoding="async"></figure>'
            )
        width, height = image.size
        widths = sorted({min(width, size) for size in (480, 800, 1200)})
        variants = []
        for size in widths:
            target = relative.with_name(f'{relative.stem}-{size}w.webp')
            destination = output / target
            destination.parent.mkdir(parents=True, exist_ok=True)
            image.resize((size, round(height * size / width)), Image.Resampling.LANCZOS).save(
                destination, 'WEBP', quality=82, method=6)
            variants.append(f'/{target.as_posix()} {size}w')
    escape = lambda value: html.escape(str(value), quote=True)
    return (
        '<figure class="article-hero"><picture>'
        '<source type="image/webp" srcset="' + escape(', '.join(variants))
        + '" sizes="(max-width:650px) calc(100vw - 120px), (max-width:940px) calc(100vw - 160px), 780px">'
        '<img src="' + escape(url) + '" alt="' + escape(page.get('obrazek_alt', ''))
        + '" width="' + str(width) + '" height="' + str(height)
        + '" style="width:100%;height:auto;display:block;border-radius:16px" decoding="async">'
        '</picture></figure>'
    )
