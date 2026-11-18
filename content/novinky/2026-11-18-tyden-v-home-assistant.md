---
title: "Týden v Home Assistant: AUX-2 oživuje starší techniku"
description: "Přehled za 11.–17. listopadu 2026: Home Assistant Connect AUX-2, opravy Core 2026.11.2, firmware Shelly 2.2.1 a kontrola UniFi, AI i ESPHome."
cas: "4 minuty"
obtiznost: "Přehled"
kontrola_zdroju: "2026-11-18"
stav: "Ověřeno podle oficiálních zdrojů"
translationKey: "news.week-2026-11-18"
temata: [Home Assistant, Novinky, Hardware, Shelly, UniFi, AI, ESPHome]
obrazek: "/assets/images/novinky-2026-11-18.png"
obrazek_alt: "Ilustrace staršího zesilovače připojeného přes chytrý víceúčelový můstek k síti a Home Assistant"
---
## AUX-2 propojuje starší techniku s Home Assistant

Přehled za 11.–17. listopadu 2026 navazuje na [minulý týden](/novinky/2026-11-11-tyden-v-home-assistant/). Největší novinkou je **Home Assistant Connect AUX-2**, malá krabička, která může přivést do chytré domácnosti starší audio techniku, zařízení se sériovým rozhraním, Z-Wave adaptér i Bluetooth senzory.

AUX-2 má kombinovaný analogový a digitální zvukový výstup, dva porty RS-232, USB-A, konektor Grove a Bluetooth. K síti se připojí přes Ethernet nebo Wi-Fi a napájet jej lze přes USB-C nebo PoE. Po jediném ethernetovém kabelu tak mohou vést data i elektřina. Cena při uvedení je 59 eur a prodej byl spuštěn celosvětově.

Pro běžnou domácnost je podstatné, že nejde o další řídicí jednotku Home Assistant. Je to víceúčelový můstek: starý zesilovač může přehrávat zvuk z Music Assistant, sériový port může ovládat podporovaný televizor, klimatizaci či střídač a USB může přesunout adaptér Connect ZWA-2 na vhodnější místo v domě. AUX-2 také funguje jako Bluetooth proxy. Konkrétní zařízení ale musí mít odpovídající integraci a někdy potřebuje zvláštní kabel.

Výrobce uvádí, že síťové připojení Connect ZWA-2 je vyzkoušené. Connect ZBT-2 se Zigbee zatím doporučuje spíše k testování a Thread tímto způsobem spolehlivě nefunguje. To je důležitý rozdíl mezi hotovou funkcí a možností pro experimentování.

## Core 2026.11.2 opravuje každodenní potíže

Home Assistant Core 2026.11.2 vyšel 16. listopadu. Jde o opravnou verzi bez velkých nových funkcí. Řeší například smyčku při opakovaném načítání MQTT integrace s duplicitním ID vypnuté entity, přehrávání záznamů z Reolink NVR a Hubů, připojení starších opakovačů FRITZ! a výpadky LG webOS TV při obnovení spojení.

U UniFi Network opravuje nabídku nastavení ve chvíli, kdy integrace není načtená. V tomto týdnu jsme v oficiálním přehledu nedoložili novou funkci UniFi Protect. Samostatná novinka se neobjevila ani u AI integrací; změny OpenAI a Gemini patřily už do základního vydání 2026.11 a byly v [předchozím přehledu](/novinky/2026-11-11-tyden-v-home-assistant/).

## Shelly 2.2.1 rychle napravuje chybu identifikace

Shelly vydalo 11. listopadu firmware 2.2.0 pro zařízení Gen2 a novější. Přidal mimo jiné zálohu uživatelského nastavení, odklad obnovení výstupu po zapnutí a hromadné povely pro spínače. U zařízení s menší pamětí může aktualizace proběhnout ve dvou krocích a zahrnuje více restartů.

O dva dny později následovala verze 2.2.1. Vrací správné ID modelům Shelly 1PM Mini Gen3 a Gen4, kterým verze 2.2.0 identifikátor omylem změnila. Pokud jste mezitím Home Assistant, MQTT nebo heslo nastavili podle nového ID, po opravě může být nutné vrátit konfiguraci k původnímu identifikátoru. Verze 2.2.1 také opravuje pád Shelly 2PM Gen4, obnovuje Bluetooth relay u Pro 3EM a doplňuje chybějící domovskou stránku žárovky RGBCCT Bulb Gen3.

## Co tento týden nepřinesl

V uzavřeném období nepřibyl nový partner programu Works with Home Assistant ani nová stabilní verze Home Assistant OS. ESPHome 2026.11.0 vyšlo až 18. listopadu, proto patří do příštího přehledu. Uvedené změny jsme ověřili v dokumentaci a poznámkách k vydání; netestovali jsme je na konkrétních zařízeních.

## Zdroje

- [Home Assistant – oznámení Connect AUX-2](https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/)
- [Home Assistant – Connect AUX-2](https://www.home-assistant.io/connect/aux-2/)
- [Home Assistant – úplný přehled změn Core 2026.11.2](https://www.home-assistant.io/changelogs/core-2026.11/)
- [Home Assistant Core 2026.11.2 na GitHubu](https://github.com/home-assistant/core/releases/tag/2026.11.2)
- [Shelly – changelog firmwaru Gen2+](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – integrace UniFi Network](https://www.home-assistant.io/integrations/unifi/)
- [Home Assistant – Works with Home Assistant](https://www.home-assistant.io/blog/categories/works-with-home-assistant)
- [Home Assistant OS – vydání](https://github.com/home-assistant/operating-system/releases)
- [ESPHome – vydání 2026.11.0](https://esphome.io/changelog/2026.11.0/)
