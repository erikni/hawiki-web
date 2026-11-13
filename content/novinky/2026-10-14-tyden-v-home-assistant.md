---
title: "Týden v Home Assistant: Tesla přes BLE, Shelly a snazší propojení AI"
description: "Novinky za 7.–13. října 2026: Home Assistant 2026.10 a 2026.10.1, Tesla přes BLE, Shelly, UniFi Protect, AI a certifikovaná světla."
cas: "4 minuty"
obtiznost: "Přehled"
kontrola_zdroju: "2026-10-14"
stav: "Ověřeno podle oficiálních zdrojů"
temata: [Home Assistant, Novinky, Tesla, Shelly, UniFi, AI, Matter]
obrazek: "/assets/images/novinky-2026-10-14.png"
obrazek_alt: "Ilustrace chytrého domu s osvětlením, mapou a propojenými spouštěči automatizací"
---
## Od bety ke stabilní verzi

Týden od 7. do 13. října 2026 přinesl stabilní Home Assistant 2026.10 a první opravné vydání 2026.10.1. Navazujeme na [minulý přehled](/novinky/2026-10-07-tyden-v-home-assistant/): vedle mapy a automatizací stojí za pozornost místní příkazy pro Teslu, změny Shelly a UniFi i jednodušší připojení AI.

## Mapa a automatizace

Verze 2026.10 vyšla 7. října. Vektorová mapa zůstává ostrá při přibližování a přidává přehled osob, zařízení a zón. V editoru automatizací lze v podmínce podle spouštěče přímo zaškrtnout příslušné spouštěče; jejich ID obstará Home Assistant. Ručně zadaná ID v YAML dál fungují.

## Tesla přes BLE: už od 2026.10

Integrace **Teslemetry** nově umí posílat příkazy podporovanému vozu Tesla místně přes Bluetooth Low Energy. Funkce je součástí už verze 2026.10, takže je dostupná i v 2026.10.1; nepřibyla až s opravnou aktualizací.

Potřebujete účet s aktivním předplatným Teslemetry, Bluetooth adaptér nebo proxy dostupnou Home Assistant a vůz v dosahu. Místní ovládání se zapíná pro každý vůz zvlášť a vyžaduje spárování klíče s autem. Vůz musí podporovat protokol Tesla Vehicle Command; některé starší Model S a X jej nepodporují. Při nedostupném Bluetooth může integrace přejít na cloud. Nejde tedy o novou samostatnou integraci Tesla BLE ani o zrušení předplatného.

## Shelly: hlavice a kamera

V řadě 2026.10 přibyla možnost připojit hlavici **Shelly BLU TRV i přes jiné podporované zařízení než BLU Gateway**. Neznamená to, že hlavici zprostředkuje libovolné Bluetooth zařízení. Shelly Camera získala senzor volného místa v úložišti a snímky se načítají přes rozhraní pro momentky.

Opravná verze 2026.10.1 pak upravuje hlášení posledního směru pohybu u nekalibrovaných rolet Shelly. Tato oprava není náhradou kalibrace.

## UniFi Protect: více možností přes API klíč

Verze 2026.10 rozšířila režim připojení pouze přes API klíč například o další přepínače, senzory, události a sirény. Pro část funkcí tak není nutný místní uživatelský účet. Rozsah je ale omezený veřejným API; plný přístup a režim pouze s klíčem nejsou rovnocenné. Před přepnutím ověřte potřebné funkce v dokumentaci. Jde konkrétně o **UniFi Protect**, nikoli plošnou změnu všech integrací UniFi.

## AI: jednodušší připojení přes MCP

V Nastavení → Systém najdete stránku **AI** s kartou serveru Model Context Protocol. Server lze zapnout přímo a zkopírovat adresu pro podporovanou AI aplikaci. MCP umožňuje aplikaci komunikovat s Home Assistant; samo o sobě není novým hlasovým modelem.

U nového nastavení se zpřístupňují všechny nabízené nástroje Home Assistant a připojit se mohou jen správci. Rozsah i omezení účtů lze změnit. Před připojením proto zkontrolujte, co aplikaci dovolujete používat.

## LEDVANCE a první opravy

Dne 13. října přibyla do programu Works with Home Assistant značka LEDVANCE se 116 certifikovanými zařízeními. Oznámená řada používá Matter přes Wi-Fi a místní ovládání. Pro tato zařízení nepotřebujete Thread hraniční směrovač, ale potřebujete připravenou integraci Matter. Před nákupem ověřte přesný model v certifikačním seznamu.

Verze 2026.10.1 z 10. října přinesla také opravy světel Hue a ukládání záznamů průběhu automatizací. Před aktualizací připravte zálohu a projděte změny svých integrací. ESPHome při kontrole stále uvádí stabilní verzi 2026.9.1; aktualizace Home Assistant sama nepřehraje firmware čidel.

## Zdroje

- [Home Assistant 2026.10 – stabilní vydání a opravné verze](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [Home Assistant Core 2026.10.1 – seznam oprav na GitHubu](https://github.com/home-assistant/core/releases/tag/2026.10.1)
- [Dokumentace spouštěčů automatizací](https://www.home-assistant.io/docs/automation/trigger/)
- [LEDVANCE vstupuje do Works with Home Assistant](https://www.home-assistant.io/blog/2026/10/13/ledvance-joins-works-with-home-assistant/)
- [Seznam certifikovaných zařízení LEDVANCE / OSRAM](https://works-with.home-assistant.io/certified-products/?brand=ledvance-osram)
- [Dokumentace integrace Matter](https://www.home-assistant.io/integrations/matter/)
- [ESPHome – přehled změn](https://esphome.io/changelog/)
- [Úplný seznam změn Home Assistant 2026.10 a 2026.10.1](https://www.home-assistant.io/changelogs/core-2026.10/)
- [Teslemetry – předpoklady a Bluetooth ovládání](https://www.home-assistant.io/integrations/teslemetry/)
- [Přidání Bluetooth příkazů do Teslemetry](https://github.com/home-assistant/core/pull/176296)
- [Shelly BLU TRV – rozšíření podpory připojení](https://github.com/home-assistant/core/pull/182422)
- [UniFi Protect – režimy připojení a jejich omezení](https://www.home-assistant.io/integrations/unifiprotect/)
- [Dokumentace serveru Model Context Protocol](https://www.home-assistant.io/integrations/mcp_server/)
