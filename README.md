# HA wiki

Statický český průvodce Home Assistant pro běžné domácnosti.

## Sestavení

```sh
python3 -m pip install --target .vendor -r requirements.txt
python3 build.py
python3 -m http.server 8000 --directory dist
```

Otevřete http://localhost:8000. Výstup v `dist/` lze hostovat jako běžný statický web v kořeni domény. Obsah se nepřipravuje za běhu na serveru.

## Úpravy obsahu

Články jsou v `obsah/`. Adresář a název Markdown souboru určují adresu článku. Každý článek začíná YAML metadaty: title, description, cas, obtiznost, kontrola_zdroju a stav. Nepoužívejte označení „otestováno“, pokud postup nebyl skutečně ověřen na zařízení.

Šablonu článku najdete v `sablony/navod.md`. Vzhled a vyhledávání jsou v `assets/`. Zdrojové HTML šablony společného rozložení, článků, karet a rozcestníků jsou v `sablony/`; nejde o vygenerované stránky. Jejich naplnění obsahem zajišťuje `build.py`. Po úpravě znovu spusťte sestavení. Hlavní stránka používá zvolený seznam článků; nové články se automaticky objeví v příslušné sekci a vyhledávání.

Vyhledávání používá malý JavaScript a neodesílá dotazy na server. Bez JavaScriptu zůstává navigace a čtení článků funkční.

## Obsahová omezení první verze

Deset úvodních článků vychází z odkazované dokumentace. Postupy nebyly vyzkoušeny na fyzickém zařízení. Produktová srovnání, ceny pro ČR/SR, fotografie kroků a další praktické scénáře vyžadují doplnění a ověření. Web je česky; samostatná slovenská verze zatím není součástí.

## Doména a barvy

Cílová adresa je https://www.hawiki.cz a je nastavena v `site.json`. Generátor ji používá v kanonických adresách jednotlivých stránek. DNS a hosting musí být připojeny samostatně. Produkční hosting zajišťuje Cloudflare Worker `hawiki-cz` se statickými aktivy. Konfigurace Workeru je v `wrangler.jsonc`.

Hlavní barva je Home Assistant modrá `#18BCF2`; textové odkazy používají tmavší `#0879A6` pro lepší čitelnost. Zdroj palety: https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/core.globals.ts

## Zdrojový repozitář

https://github.com/erikni/HAwiki.cz obsahuje pouze zdroje, Markdown články a podklady. `dist/` s hotovým HTML, stažené knihovny `.vendor/` a lokální hostingové nastavení se do něj nenahrávají.

## Cloudflare Workers

Produkční Worker se jmenuje `hawiki-cz`. Soubor `wrangler.jsonc` určuje název Workeru a adresář `dist/` se statickými aktivy. Produkční workflow `.github/workflows/deploy-cloudflare-workers.yml` sestaví a zkontroluje web a pouze z větve `main` spustí `wrangler deploy`.

Workflow `.github/workflows/preview-cloudflare-workers.yml` se spouští pro pull requesty ze stejného repozitáře. Příkaz `wrangler preview --name pr-<číslo-PR>` vytvoří oddělené Workers Preview bez změny produkčního provozu. Skutečnou URL zveřejní Cloudflare Wrangler Action v GitHub Deployment a souhrnu běhu. Očekávaný vzor je `*-hawiki-cz.gemini77.workers.dev`; před schválením mergu je nutné ověřit konkrétní adresu.

V GitHub repozitáři nastavte secret `CLOUDFLARE_API_TOKEN`. Token musí mít oprávnění upravovat Workers Scripts v účtu, ve kterém je Worker `hawiki-cz`. Veřejné ID účtu je uvedeno ve workflow; API token se nesmí zapisovat do repozitáře.

Sestavení zajišťuje `sh build-cloudflare.sh`: nainstaluje knihovny, převede Markdown do HTML a spustí místní kontroly. Při chybě workflow skončí s nenulovým návratovým kódem. Vygenerovaný adresář `dist/` zůstává mimo Git.

Domény `www.hawiki.cz` a `hawiki.cz` se spravují v nastavení produkčního Workeru. Samotná hodnota v `site.json` nenastavuje DNS ani route.

Dokumentace: https://developers.cloudflare.com/workers/static-assets/ a https://developers.cloudflare.com/workers/previews/

## Kontrola Python skriptů

Funkce v `build.py` a `check.py` mají dokumentaci a standardní formátování. Oba skripty lze bezpečně importovat; sestavení a kontrola se spustí pouze při jejich přímém spuštění.

```sh
python3 -m pip install pylint
python3 -m pylint build.py check.py
```

## Strukturovaná metadata a sdílení

Generátor vytváří JSON-LD typu Article pro články a Open Graph pro všechny stránky. Volitelné pole `temata` je seznam textů; propíše se do keywords a article:tag. Citace se přebírají z Markdown odkazů v závěrečné sekci Zdroj nebo Zdroje.

Volitelná pole `autor` (jméno osoby), `publikovano` a `aktualizovano` se zobrazí v článku a strukturovaných datech. Data zapisujte jako uvozovaný řetězec ISO 8601 a doplňujte pouze doložené údaje. Kontrola zdrojů je samostatný údaj. Open Graph article:author vyžaduje profilovou URL, proto se ze samotného jména negeneruje.

Společný náhled pro sdílení je v assets/social-card.png (1200 × 630 px). Open Graph se řídí https://ogp.me/ a JSON-LD https://schema.org/Article.

## SEO a tematické rozcestníky

`seo.json` uchovává SEO názvy kategorií, cestu začátečníka, tematické skupiny a odkazy na domácí scénáře. Úvodní texty HUBů jsou v `obsah/<téma>/index.md` s metadaty `type: hub`, `title`, `seoTitle` (volitelné), `description` a případně `kontrola_zdroju`. Adresář určuje URL HUBu; `index.md` nepřidává do URL další část. Nová témata přidejte do `topics` a doplňte odpovídající Markdown; prázdné archivy se nevytvářejí. Nové integrační průvodce lze přidat pod `obsah/integrace/` a tematické rozcestníky pod `obsah/integrace/<výrobce>/index.md`. Stávající články zůstávají na svých URL.

Články mohou mít vlastní `seoTitle` a seznam `related` existujících slugů bez lomítka na začátku nebo konci. `autor` může být jméno nebo seznam jmen. Údaje o autorovi a vydání se nevytvářejí automaticky. Volitelný `sourceType` přijímá `official-docs`, `tested`, `editorial` a `mixed`; `testedOn` je popis skutečně použitého testovacího prostředí. `kontrola_zdroju` zůstává datem kontroly dokumentace.

Generátor vytváří `sitemap.xml` z registru právě vytvořených veřejných stránek; statické ověřovací soubory ani zbylé HTML z předchozího sestavení se do ní nepropíší. `robots.txt` odkazuje na sitemap. Hostname redirect vyžaduje nastavení Cloudflare podle `docs/cloudflare-canonical.md`.
