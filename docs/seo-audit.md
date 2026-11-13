# SEO audit – 8. 10. 2026

- Základ návrhu: aktuální GitHub main `3ae2a3e`; oddělený checkout `seo-preview`, aktualizovaný pomocí pull --ff-only. Původní web má rozdílnou historii a rozpracované změny; zůstává zachován.
- Stack: vlastní Python generátor, Markdown 3.8.2, PyYAML, Pygments; statický výstup `dist/`, Cloudflare Pages přes GitHub Actions.
- Routing: cesta Markdownu v `content/` určuje URL s koncovým lomítkem. Kategorie v SECTIONS, další stránky generuje `tools/build.py`.
- Metadata: společná šablona title + suffix, description, canonical HTTPS/www ze site.json, Open Graph včetně obrázku.
- Structured data: Article, citace, témata a volitelný autor/publikace/aktualizace. Chybí WebSite, Organization a BreadcrumbList.
- Breadcrumbs: viditelně Domů / kategorie, bez aktuální stránky a JSON-LD.
- Obsah: české YAML frontmatter; autor a data pouze doložená. Tagy `temata` jsou viditelné štítky, bez odkazů a tagových archivů.
- Sitemap ani RSS nejsou generovány. robots.txt dovoluje indexaci, neodkazuje na sitemap.
- Homepage má jako H1 pouze marketingový claim. Kategorie používají krátké názvy i v H1/title.
- Related content ani learning path nejsou společné komponenty. V některých článcích existuje vlastní sekce Co dál.
- Lze rozšířit existující generátor, šablony a konfigurační soubory; není potřeba nový framework ani klientská knihovna.
- Doplnit sitemap z registru skutečně vytvořených indexovatelných stránek, SEO konfiguraci kategorií, kurátorované HUBy, learning path, related content a breadcrumbs/schema.
- Redirecty host/scheme jsou infrastruktura Cloudflare, nikoli nastavení canonical v site.json. Pokus o živou HTTP kontrolu skončil chybou proxy CONNECT 500, nikoli ověřenou odpovědí webu. Skutečný stav redirectů zůstává neověřený.
- Existuje jeden specializovaný článek Shelly: samostatný HUB odložit do doby rozšíření obsahu.
