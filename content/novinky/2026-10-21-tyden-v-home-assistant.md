---
title: "Týden v Home Assistant: opravy Gemini a nový firmware Shelly"
description: "Přehled za 14.–20. října 2026: Home Assistant 2026.10.2, AI a hlas, Shelly 2.1.0, stav UniFi, integrací a Works with Home Assistant."
cas: "4 minuty"
obtiznost: "Přehled"
kontrola_zdroju: "2026-10-21"
stav: "Ověřeno podle oficiálních zdrojů"
temata: [Home Assistant, Novinky, Shelly, UniFi, AI, Integrace, Hardware]
obrazek: "/assets/images/novinky-2026-10-21.png"
obrazek_alt: "Ilustrace chytrého domu s elektroměrem, síťovou kamerou a symbolem hlasového asistenta"
---
## Týden oprav a měření spotřeby

Od 14. do 20. října 2026 přibylo opravné vydání Home Assistant 2026.10.2 a firmware Shelly 2.1.0. U AI jsou podstatné opravy Gemini a hlasového výstupu. Navazujeme na [minulý přehled](/novinky/2026-10-14-tyden-v-home-assistant/).

## Home Assistant 2026.10.2

Druhá říjnová opravná verze vyšla 16. října. Řeší například dvojí spuštění MQTT spouštěčů zařízení a štítků po opětovném načtení konfigurace. Tesla Fleet dostala opravu chyby při neočekávané úrovni vyhřívání. Diagnostika Tesla Fleet a Teslemetry nově skrývá souřadnice z časových plánů.

Před aktualizací připravte zálohu a projděte změny svých integrací.

Dne 20. října přibyl také **Home Assistant OS 18.4.rc1**, zatím předběžné vydání. Opravuje například VLAN na adaptérech Realtek a potíže se startem či USB úložišti. RC není stabilní aktualizace pro běžnou domácnost.

## AI: Gemini má spolehlivější hlasový výstup

Verze 2026.10.2 upravuje parametry požadavků podle možností jednotlivých rodin modelů Gemini. Opravuje také zpracování hotové zvukové odpovědi ve formátu WAV. Dříve ji převodník očekávající jiný formát mohl odmítnout, přestože Google zvuk vytvořil. Pro domácnost s hlasovým asistentem je to konkrétní oprava převodu textu na řeč, nikoli oznámení nového hlasového zařízení.

Propojení AI přes MCP jsme popsali minule a tento týden je nepředstavujeme znovu jako novinku. Gemini nadále vyžaduje API klíč; ovládání domácnosti závisí na tom, které entity mu zpřístupníte.

## Shelly 2.1.0: novinka výrobce, ne nová entita HA

Shelly datuje firmware 2.1.0 na 14. října. Pro zařízení s měřením příkonu a energie uvádí podporu **Shelly Cloud NILM services**. NILM je označení pro analýzu elektrické zátěže bez samostatného měření každého spotřebiče. Changelog však nepopisuje podrobnosti výsledků ani jejich zpřístupnění v Home Assistant.

Oznámení proto neznamená, že HA po aktualizaci automaticky pozná jednotlivé spotřebiče. Integrace Shelly komunikuje se zařízeními místně; cloudová služba výrobce je jiná vrstva. Dostupnost firmwaru ověřte pro přesný model, protože všechna Shelly nedostávají stejné aktualizace. LoRa, nové webové rozhraní a další změny uvedené v sekci Unreleased zatím nepatří do stabilní 2.1.0.

## UniFi: tento týden bez doložené nové funkce HA

V seznamu vydání 2026.10.2 není samostatná změna UniFi Network ani UniFi Protect. Rozšíření režimu Protect pouze s API klíčem patří už k 2026.10 a bylo v minulém přehledu. Nadále má omezený rozsah proti plnému přístupu. Nová verze aplikace nebo kamery Ubiquiti sama o sobě nedokládá novou funkci v HA; rozhoduje podpora konkrétního zařízení a veřejného API.

## Integrace, hardware a Works with HA

V opravném vydání 2026.10.2 nejsou oznámené nové integrace. Katalog integrací slouží k ověření podpory; pouhá přítomnost položky neříká, kdy přibyla. Ani na hlavním blogu jsme pro sledovaný týden nenašli oznámení nového vlastního hardwaru HA.

Posledním oznámeným partnerem Works with Home Assistant zůstává LEDVANCE z 13. října, tedy z předchozího týdne. Nové partnerství za 14.–20. října v přehledu programu doložené nemáme. Při výběru zařízení ověřujte certifikaci přesného modelu.

## Nový domov pro přispěvatele

Vedle hlavního blogu stojí za pozornost oznámení ze 16. října na novém portálu contributors.home-assistant.io. Sdružuje návody pro vývoj, překlady, dokumentaci i testování. Zapojit se tak můžete také opravou českého textu nebo srozumitelnosti návodu.

## Zdroje

- [Home Assistant Core 2026.10.2 – vydání a opravy](https://github.com/home-assistant/core/releases/tag/2026.10.2)
- [Home Assistant 2026.10 – poznámky a opravná vydání](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [Gemini – oprava parametrů a WAV odpovědí](https://github.com/home-assistant/core/pull/185723)
- [Google Gemini – dokumentace integrace](https://www.home-assistant.io/integrations/google_generative_ai_conversation/)
- [Shelly – firmware 2.1.0 a připravované změny](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Shelly – dokumentace integrace](https://www.home-assistant.io/integrations/shelly/)
- [UniFi Protect – režimy a omezení připojení](https://www.home-assistant.io/integrations/unifiprotect/)
- [Katalog integrací Home Assistant](https://www.home-assistant.io/integrations/)
- [Home Assistant – hlavní blog](https://www.home-assistant.io/blog/)
- [Works with Home Assistant – oznámení partnerů](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
- [Works with Home Assistant – podmínky programu](https://works-with.home-assistant.io/)
- [Nový portál pro přispěvatele Home Assistant](https://contributors.home-assistant.io/blog/2026/10/16/a-new-home-for-every-contributor/)
- [Home Assistant OS 18.4.rc1 – předběžné vydání](https://github.com/home-assistant/operating-system/releases/tag/18.4.rc1)
