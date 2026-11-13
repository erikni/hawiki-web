# SEO návrh HAwiki.cz k revizi

Návrh je připraven lokálně v odděleném checkoutu aktuálního GitHub main `3ae2a3e`. Původní rozpracovaný adresář `web` nebyl přepsán. Není vytvořen nový commit ani provedeno nasazení.

## Obsah k přečtení

- [Zigbee: tematický rozcestník](../content/zigbee/index.md)
- [Integrace: tematický rozcestník](../content/integrace/index.md)
- [Automatizace: tematický rozcestník](../content/automatizace/index.md)
- [Jak nainstalovat Home Assistant](../content/zaciname/instalace-home-assistant.md)
- [ZHA vs Zigbee2MQTT](../content/zigbee/zha-vs-zigbee2mqtt.md)
- [O projektu a ověřování obsahu](../content/o-projektu/index.md)

## Technické změny a výsledky

- [Přehled změn, odchylek a kontrol](seo-changes.md)
- [Výchozí audit](seo-audit.md)
- [Přesný návrh Cloudflare redirectu](cloudflare-canonical.md)
- [Výsledky 52 HTTP a mobilních kontrol](seo-validation.json)
- [Návrhy LinkedIn, YouTube a Instagram](seo-socialni-site.md)
- [Použité prompty a ilustrace](seo-images.md)

Změny zachovávají základní navigaci, barvy, claim a adresy stávajících článků. Přidávají metadata, sitemap, tematické odkazy, cestu začátečníka, úplné breadcrumbs a společné Co dál.

Build a interní odkazy procházejí, metadata/JSON-LD/sitemap jsou ověřeny pro 59 stránek. Mobilní kontrola běží v Chrome na 360, 390, 768 a 1440 px. Autorství ani data vydání se nevymýšlejí. Nové technické texty vycházejí z citované dokumentace a nedeklarují fyzické testování.

K publikaci je nutné výslovné schválení tohoto konkrétního návrhu podle AGENTS.md a redakčního postupu. Doménové redirecty mají připravenou konfiguraci, ale jejich produkční stav nebyl kvůli chybě síťové proxy ověřen.
