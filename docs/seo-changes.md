# SEO changes

## Implemented

- Lokální návrh v odděleném checkoutu `seo-preview`, založený na GitHub main `3ae2a3e`. Původní rozpracovaný adresář `web` zůstává zachován.
- Jednotný HTTPS/www canonical, přesné homepage title/H1 a přirozený popis (156 znaků); marketingový claim i základní menu zachovány.
- SEO H1, title a popisy šesti hlavních kategorií v `seo.json`.
- Kurátorované HUBy `/zigbee/`, `/integrace/`, `/automatizace/`: úvod, podtémata, start, existující návody, problémy a související témata. Markdown zůstává v `content/`, `type: hub` využívá společný generátor a šablonu.
- Rozhodovací průvodce `/zaciname/instalace-home-assistant/` a srovnání `/zigbee/zha-vs-zigbee2mqtt/`, zdroje a datum jejich kontroly, hlavní ilustrace.
- Osm skutečných kroků začátečníka; místo chybějícího univerzálního návodu přidání prvního zařízení odkaz na vysvětlení zařízení a integrací. První spuštění Green je prolinkováno z instalace a souvisejících článků.
- Homepage: Nejčastější témata a Co chcete doma vyřešit, odkazy na dostupný obsah.
- Sdílená komponenta Co dál: předchozí/další krok, tematické odkazy, nejvýše tři související články. Podpora explicitního `related`; chybné reference zastaví build.
- Klíčové štítky témat odkazují na dostupné HUBy. Nejsou vytvářeny tagové archivy.
- Úplné breadcrumbs včetně aktuální stránky a BreadcrumbList; WebSite a Organization na homepage; zachován Article s doloženými metadaty a odlišným seoTitle.
- Autor může být jedna osoba či seznam osob. Volitelné sourceType/testedOn se zobrazují jen při vyplnění. Žádný autor, publikace, aktualizace ani testovací prostředí nebyly automaticky doplněny.
- `/o-projektu/` včetně metodiky ověřování a odkazu z patičky.
- Sitemap obsahuje pouze právě vygenerované veřejné stránky a canonical URL; robots.txt na ni odkazuje. Doplněno ignorování dist/ v Gitu.
- `tools/check_seo.py` ověřuje SEO/schema/sitemap a je zapojený do build-cloudflare.sh.

## Existing functionality reused

- Python/Markdown generátor, společné HTML šablony, CSS, karty, štítky, vyhledávání a statický hosting.
- site.json jako zdroj canonical originu; Open Graph včetně společné karty 1200 × 630.
- Stávající URL článků, články a doložené citace/datum kontroly.
- Existující kontrola interních odkazů a současné vykreslení YAML s Pygments.

## Requires external infrastructure change

- Přesměrování host/scheme na HTTPS/www vyžaduje ověřit a případně nastavit Cloudflare zónu. Přesné pravidlo, zachování path/query a testovací matice jsou v [cloudflare-canonical.md](cloudflare-canonical.md).
- Přístup k živému hostname z prostředí skončil chybou proxy CONNECT 500. Stav produkčních redirectů není potvrzen. Tento návrh nebyl nasazen.

## Recommended future content

- Detailní přidání prvního zařízení, samostatné návody pro ZHA, Zigbee2MQTT, síť mesh a koordinátory.
- Po rozšíření obsahu Shelly HUB a průvodce jeho konkrétními způsoby připojení.
- Další výrobci pod `/integrace/<výrobce>/`, podtémata automatizací a rozcestníky ESPHome, Matter, Energie a Hlas. Architektura podporuje vnořené Markdowny a kurátorované skupiny; nevytváří prázdné stránky.
- Ověřené praktické zkušenosti a autorství doplnit až na základě doložených údajů.

## Not implemented and why

- Samostatný Shelly HUB: pouze jeden specializovaný existující článek, nestačí pro další přínosný rozcestník. Článek je přístupný z Integrací.
- Žaluzie jako homepage scénář: chybí samostatný relevantní návod. Žádné placeholder odkazy.
- Stovky tagových stránek, plošný noindex, URL migrace ani nový framework: nejsou potřeba a chybí důvod.
- Samostatná metodika: je součástí O projektu.
- RSS: projekt jej neměl, zadání vyžaduje zjistit stav, nikoli vytvořit feed.
- Autor Erik Brožek ani data vydání: nejsou automaticky odvozována z identity zadavatele či dne sestavení.
- Commit, push, nasazení a zveřejnění na sociálních sítích: návrh zatím nebyl výslovně schválen podle AGENTS.md a redakčního postupu.

## Validation

- Build: 59 stránek. `tools/check.py`: všechny interní odkazy a soubory procházejí.
- `tools/check_seo.py`: všech 59 stránek má jeden H1, vlastní canonical, Open Graph, parsovatelné JSON-LD a shodu se sitemap; robots neblokuje obsah.
- Python pylint skriptů v `tools/`: 10.00/10, bez hlášení. Syntaxe ověřena py_compile.
- Chrome/Playwright: 13 klíčových URL × 4 šířky (360, 390, 768, 1440 px), celkem 52 úspěšných kontrol HTTP 200, H1, title, description, canonical, JSON-LD, načtení obrázků a vodorovného přetékání. Výsledky v seo-validation.json. Screenshoty homepage, Zigbee, cesty začátečníka a článku byly vytvořeny pro vizuální kontrolu.
- Rozsah hlavního Markdown textu bez metadat a zdrojů: instalace 2894 znaků, ZHA vs Zigbee2MQTT 2718, Zigbee 2214, Integrace 2336, Automatizace 2272. Převzatá technická tvrzení podle dokumentace, nikoli fyzický test zařízení.
- Nové hlavní ilustrace vizuálně zkontrolovány a přítomny v sestaveném webu; neobsahují přesný screenshot ani fotografii testovaného výrobku.
- Návrhy LinkedIn/YouTube/Instagram jsou v seo-socialni-site.md, plánované URL nejsou vydávány za publikované.
