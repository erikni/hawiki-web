---
title: "Týden v Home Assistant: nová jména, bezpečnější ESPHome a AI v betě"
description: "Přehled za 28. října až 3. listopadu 2026: nové pojmenování v Home Assistant 2026.11, ESPHome 2026.10.2, opravy AI a listopadová výzva WTH."
cas: "4 minuty"
obtiznost: "Přehled"
kontrola_zdroju: "2026-11-04"
stav: "Ověřeno podle oficiálních zdrojů"
temata: [Home Assistant, Novinky, ESPHome, AI, Shelly, UniFi, Komunita]
obrazek: "/assets/images/novinky-2026-11-04.png"
obrazek_alt: "Ilustrace chytrého domu s uspořádanými zařízeními a bezpečnou aktualizací malé řídicí desky"
---
## Jména se mění, automatizace zůstávají

Přehled za 28. října až 3. listopadu 2026 navazuje na [minulý týden](/novinky/2026-10-27-tyden-v-home-assistant/). Mezi obdobími zůstal volný 27. říjen: tehdy vyšel stabilní Home Assistant OS 18.4 a do Works with Home Assistant vstoupily snímače přítomnosti Everything Presence. V tomto vydání se soustředíme na novější události.

## Home Assistant 2026.11 uklidí názvy zařízení

Dne 3. listopadu Home Assistant představil nové zacházení s názvy, které má dorazit ve stabilní verzi 2026.11 následující den. Zařízení a entity se pojmenují jen podle toho, čím skutečně jsou, a rozhraní podle potřeby doplní místnost či nadřazené zařízení. Zásuvková lišta tak může mít každou zásuvku jako samostatné „dětské zařízení“ s vlastním názvem a místností.

Stávající ID entit se při aktualizaci nemají změnit, takže automatizace, skripty, scény a dashboardy mají dál fungovat. Viditelné názvy ale mohou vypadat jinak. Po aktualizaci proto zkontrolujte hlavně vlastní karty a šablony používající atribut `friendly_name`. Podpora dětských zařízení začne u Z-Wave, MQTT, ESPHome a části Tuya; Matter a ZHA mají následovat. K datu kontroly šlo ještě o oznámení změny pro vydání 2026.11, nikoli o stabilní verzi ve sledovaném období.

## ESPHome 2026.10.2 opravuje rizikovou aktualizaci

Opravné ESPHome 2026.10.2 vyšlo 3. listopadu. Nejdůležitější je ochrana zařízení s čipem RTL8710B: obchází problém, při kterém mohla komprimovaná bezdrátová aktualizace zařízení znefunkčnit. Opravuje také TLS 1.3 u `audio_http`, uvolnění držených spojení Bluetooth proxy a nabízí stažení sestaveného programu z Device Builderu pro hostitelská zařízení.

Jde o opravy nástroje ESPHome a jeho firmwaru, ne o novou integraci Home Assistant Core. Před aktualizací vlastních desek je rozumné vytvořit zálohu konfigurace a ověřit, jaký čip zařízení používá.

## AI: dvě opravy zatím jen v betě

Beta Core 2026.11.0b3 z 2. listopadu opravuje blokující načítání schématu při volání nástrojů MCP a situaci, kdy integrace OpenRouter mohla nástroj zavolat dvakrát. To může být důležité pro automatizace, které nechávají jazykový model provádět akce. Nejde však o stabilní aktualizaci; běžná domácnost má počkat na finální 2026.11 a následné opravy.

## Listopad sbírá domácí „Proč tohle nejde?“

Od 29. října běží komunitní měsíc „What the Heck?!“. Autoři vyzývají i netechnické členy domácnosti, aby popsali, co je v Home Assistant matoucí nebo zbytečně složité. Praktický tip: zeptejte se lidí doma, co jim na ovládání vadí, a jejich zkušenost pošlete do vyhrazené kategorie fóra.

V kontrolovaných zdrojích jsme pro 28. říjen až 3. listopad nedoložili novou stabilní verzi firmwaru Shelly ani změnu přímo v integracích Shelly, UniFi Network či UniFi Protect. Shelly 2.2.0 zůstávalo v beta části changelogu. Nové partnerství Works with Home Assistant ani nový vlastní hardware HA v tomto období na oficiálním blogu nepřibyly.

## Zdroje

- [Home Assistant – nové pojmenování zařízení a entit](https://www.home-assistant.io/blog/2026/11/03/naming-things-in-home-assistant/)
- [Home Assistant Core 2026.11.0b3](https://github.com/home-assistant/core/releases/tag/2026.11.0b3)
- [Home Assistant – měsíc What the Heck?! 2026](https://www.home-assistant.io/blog/2026/10/29/what-the-heck-2026/)
- [ESPHome 2026.10 a opravná vydání](https://esphome.io/blog/2026/10/21/esphome-2026-10/)
- [ESPHome 2026.10.2 na GitHubu](https://github.com/esphome/esphome/releases/tag/2026.10.2)
- [Home Assistant OS 18.4](https://github.com/home-assistant/operating-system/releases/tag/18.4)
- [Everything Smart Home v programu Works with Home Assistant](https://www.home-assistant.io/blog/2026/10/27/everything-smart-home-joins-works-with-home-assistant/)
- [Shelly – changelog firmwaru Gen2+](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – integrace Shelly](https://www.home-assistant.io/integrations/shelly/)
- [Home Assistant – integrace UniFi Network](https://www.home-assistant.io/integrations/unifi/)
- [Home Assistant – integrace UniFi Protect](https://www.home-assistant.io/integrations/unifiprotect/)
- [Works with Home Assistant – oznámení partnerů](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
