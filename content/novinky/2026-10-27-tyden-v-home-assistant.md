---
title: "Týden v Home Assistant: opravy UniFi Access a nové ESPHome"
description: "Přehled za 20.–26. října 2026: Core 2026.10.3 a 2026.10.4, ESPHome 2026.10, HAOS 18.4.rc2 a stav Shelly, AI i Works with HA."
cas: "4 minuty"
obtiznost: "Přehled"
kontrola_zdroju: "2026-10-27"
stav: "Ověřeno podle oficiálních zdrojů"
temata: [Home Assistant, Novinky, ESPHome, UniFi, Shelly, AI, Hardware]
obrazek: "/assets/images/novinky-2026-10-27.png"
obrazek_alt: "Ilustrace chytrého domu s deskou pro vlastní senzory, přístupovou čtečkou a reproduktorem"
---
## Dvě opravy Core a nové ESPHome

Přehled za 20.–26. října 2026 navazuje na [minulý týden](/novinky/2026-10-21-tyden-v-home-assistant/). Období se tentokrát překrývá o jeden den; už popsaný HAOS 18.4.rc1 neopakujeme. Hlavními novinkami jsou dvě opravné verze Home Assistant, oprava událostí UniFi Access a říjnové ESPHome pro vlastní zařízení.

## Core 2026.10.3 a 2026.10.4

Verze 2026.10.3 vyšla 23. října. Vedle dalších oprav řeší detekci verze aktualizací Proxmox VE a situaci, kdy posluchač událostí Home Connect přestal pracovat při chybě obnovení přístupového tokenu. Pro uživatele těchto integrací tak může mít aktualizace větší význam než samotné číslo vydání.

O den později následovala 2026.10.4. Zvyšuje povolenou velikost HTTP hlaviček klienta a aktualizuje knihovnu pro Lutron Caséta. První změna řeší mimo jiné stahování firmwaru přes přesměrování GitHubu: příliš dlouhá hlavička mohla stahování zastavit. Nejde o nový hardware ani novou integraci, ale o opravu přenosu souborů.

## UniFi Access: jedna událost místo dvou

Konkrétní oprava UniFi je součástí 2026.10.3 a týká se **UniFi Access**, systému přístupu ke dveřím. Řadič mohl stejnou událost poslat dvěma různými zprávami a integrace obě zpracovala zvlášť. Výsledkem byly například dvě položky v historii nebo dvě oznámení po jednom rozpoznání obličeje.

Oprava odstraňuje toto zdvojení. Neznamená rozšíření podpory kamer UniFi Protect ani změnu UniFi Network. Pokud používáte automatizace reagující na přístupové události, právě tento rozdíl je prakticky důležitý.

## ESPHome 2026.10: menší aktualizace a pozor na zvuk

ESPHome 2026.10.0 vyšlo 21. října. Rozšiřuje komprimované bezdrátové aktualizace na další podporované platformy; podle autorů se přenáší přibližně o třetinu méně dat. Starší firmware se napoprvé aktualizuje dosavadním způsobem. ESP8266 zároveň přechází na nové výchozí sestavovací nástroje.

Před aktualizací vlastních reproduktorů zkontrolujte změny konfigurace. Zařízení Sendspin nově vyžadují šifrované spojení a Music Assistant alespoň 2.10.7 nebo 2.11.0b4; nejprve tedy aktualizujte Music Assistant. U světel s nastaveným počátečním stavem ověřte chování po restartu: nastavení se nyní skutečně respektuje.

## HAOS: další kandidát opravuje Bluetooth

Dne 23. října přibyl **Home Assistant OS 18.4.rc2**. Přidává bezpečnostní aktualizace a opravu nefunkčních Bluetooth adaptérů RTL8761B s identifikátorem 0bda:a728 po změně jádra. Stále jde o předběžné vydání, nikoli stabilní HAOS 18.4. Tato zpráva o podpoře adaptéru není oznámením nového fyzického výrobku.

## Shelly, AI a Works with HA

V kontrolovaném changelogu Shelly zůstává poslední stabilní položkou 2.1.0 ze 14. října; cloudové NILM jsme popsali minule. Další změny jsou v sekci Unreleased s označením 2.2.0-beta1, proto je nepřisuzujeme nové stabilní verzi tohoto týdne.

Ve vydáních Core 2026.10.3 a 2026.10.4 jsme nenašli samostatnou novinku integrací AI ani oznámení nové integrace. Změny MCP a předchozí opravy Gemini patří ke starším přehledům. Nové komponenty ESPHome také nejsou totéž co nové integrace Core.

Na hlavním blogu HA a v oznámeních Works with Home Assistant zůstává poslední zprávou o partnerovi LEDVANCE z 13. října. Nové partnerství ani nový vlastní hardware HA za tento týden v těchto zdrojích doložené nemáme. Před aktualizací domácnosti připravte zálohu a projděte změny, které se týkají vašich zařízení.

## Zdroje

- [Home Assistant Core 2026.10.3](https://github.com/home-assistant/core/releases/tag/2026.10.3)
- [Home Assistant Core 2026.10.4](https://github.com/home-assistant/core/releases/tag/2026.10.4)
- [Říjnové poznámky Home Assistant a opravná vydání](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [UniFi Access – oprava duplicitních událostí](https://github.com/home-assistant/core/pull/185160)
- [UniFi Access – dokumentace integrace](https://www.home-assistant.io/integrations/unifi_access/)
- [Oprava limitu HTTP hlaviček](https://github.com/home-assistant/core/pull/188329)
- [ESPHome 2026.10 – přehled změn a omezení](https://esphome.io/blog/2026/10/21/esphome-2026-10/)
- [ESPHome 2026.10.0 – vydání na GitHubu](https://github.com/esphome/esphome/releases/tag/2026.10.0)
- [ESPHome – bezdrátové aktualizace](https://esphome.io/components/ota/esphome/)
- [ESPHome – Sendspin](https://esphome.io/components/sendspin/)
- [Home Assistant OS 18.4.rc2](https://github.com/home-assistant/operating-system/releases/tag/18.4.rc2)
- [HAOS – oprava adaptéru RTL8761B](https://github.com/home-assistant/operating-system/pull/5112)
- [Shelly – changelog firmwaru](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – katalog integrací](https://www.home-assistant.io/integrations/)
- [Home Assistant – hlavní blog](https://www.home-assistant.io/blog/)
- [Works with Home Assistant – oznámení partnerů](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
