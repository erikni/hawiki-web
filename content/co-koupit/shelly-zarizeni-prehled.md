---
title: "Zařízení Shelly pro Home Assistant: co vybrat do domácnosti"
description: "Přehled Shelly vypínačů, senzorů, světel, kamer, zásuvek a měřičů elektřiny a jejich připojení k Home Assistant."
cas: "6 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - Shelly
  - Chytré osvětlení
  - Senzory
  - Měření spotřeby
  - Chytré zásuvky
  - Kamery
---

Shelly nabízí zařízení pro osvětlení, ovládání spotřebičů, měření elektřiny i hlídání domácnosti. Skupina má sídlo v Bulharsku, tedy v EU; tento údaj není místem výroby konkrétního kusu. Při výběru začněte tím, co chcete doma řešit, a potom ověřte přesný model a jeho připojení k Home Assistant.

## Zařízení podle typu

- **Světla a stmívače:** Shelly Duo Bulb E27 Gen3 mění jas a odstín bílé. U samostatného stmívače ověřte vhodnost pro použitý světelný zdroj.
- **Chytré zásuvky:** Shelly Plug M Gen3 spíná spotřebič, měří příkon a podporuje Matter. Ověřte provedení pro českou síť a povolenou zátěž.
- **Vypínače a relé:** Shelly 1PM Mini Gen3 je modul za původní vypínač se spínáním a měřením příkonu. Shelly BLU Wall Switch 4 je čtyřtlačítkový Bluetooth ovladač pro povely a scény.
- **Detekce pohybu:** Shelly BLU Motion ZB detekuje pohyb a měří okolní osvětlení. Může rozsvítit chodbu, případně jen tehdy, když je tma.
- **Dveře a okna:** Shelly BLU Door/Window ZB zaznamená otevření a zavření. Hodí se pro upozornění na větrání nebo regulaci topení.
- **Únik vody:** Shelly Flood S Gen4 hlídá vodu pod pračkou, dřezem nebo u potrubí. Může spustit upozornění; samotný senzor přívod vody neuzavře.
- **Měření elektřiny:** Shelly Pro 3EM v2 slouží pro třífázové měření v rozvaděči přes Wi-Fi nebo LAN. Ověřte vhodné měřicí transformátory. Zásuvka s měřením naopak sleduje jeden spotřebič.
- **Kamery:** Shelly Camera nabízí obraz přes RTSP. Pro Home Assistant zapněte RTSP Streaming v místním panelu **Camera → Settings**. Cloudové funkce posuzujte zvlášť.

Varianty najdete v [oficiální nabídce Shelly](https://www.shelly.com/collections/all-products). Začít lze zásuvkou nebo bateriovým senzorem. Montáž modulů a měřičů do rozvodu 230 V svěřte kvalifikovanému elektrikáři.

## Připojení k Home Assistant

Podporovaná Wi-Fi zařízení přidejte přes **Nastavení → Zařízení a služby → Přidat integraci → Shelly**, případně potvrďte automatické objevení. [Oficiální integrace Shelly v Home Assistant](https://www.home-assistant.io/integrations/shelly/) komunikuje přímo se zařízením a nepotřebuje Shelly Cloud. Dostupné entity a funkce závisí na modelu.

Bluetooth senzory a ovladače **BLU** se běžně přidávají přes [BTHome](https://www.home-assistant.io/integrations/bthome/), nikoli přes integraci Shelly. Potřebujete Bluetooth adaptér nebo podporovaný přijímač v dosahu. Varianty **ZB** mohou nabídnout Zigbee; řada **Wave** používá Z-Wave. Pro tyto protokoly potřebujete odpovídající řadič a integraci. Před nákupem proto ověřte přesný název a protokol.

## Příklad: pohyb rozsvítí světlo

Nejprve přidejte pohybový senzor i světlo do Home Assistant. Například Bluetooth senzor Shelly BLU připojíte přes BTHome a Wi-Fi světlo Shelly přes integraci Shelly. Na stránce senzoru ověřte, že detekce mění stav pohybové entity na `on`.

V **Nastavení → Automatizace a scény** vytvořte prázdnou automatizaci, v nabídce otevřete **Upravit v YAML** a vložte celý příklad. Nahraďte obě ID skutečnými entitami svého pohybového senzoru a světla.

```yaml
alias: Pohyb rozsvítí chodbu
triggers:
  - trigger: state
    entity_id: binary_sensor.pohyb_chodba
    to: "on"
conditions: []
actions:
  - action: light.turn_on
    target:
      entity_id: light.chodba
mode: single
```

Příklad pouze rozsvěcí. Zhasnutí po době bez pohybu přidejte jako další automatizaci. Chytrá žárovka musí zůstat napájená i při zhasnutí; řešení původního vypínače najdete v návodu [Chytré světlo a klasický vypínač](/navody/chytre-svetlo-klasicky-vypinac/).

## Zdroje

- [Shelly: všechny produkty](https://www.shelly.com/collections/all-products)
- [Home Assistant: Shelly a kamery RTSP](https://www.home-assistant.io/integrations/shelly/)
- [Home Assistant: BTHome](https://www.home-assistant.io/integrations/bthome/)
- [Shelly Group: sídlo společnosti](https://corporate.shelly.com/en/page/impressum)
- [Shelly 1PM Mini Gen3](https://www.shelly.com/products/shelly-1pm-mini-gen3)
- [Shelly BLU Wall Switch 4](https://www.shelly.com/products/shelly-blu-wall-switch-4)
- [Shelly BLU Motion ZB](https://www.shelly.com/products/shelly-blu-motion-zb)
- [Shelly BLU Door/Window ZB](https://www.shelly.com/products/shelly-blu-door-window-zb-white)
- [Shelly Flood S Gen4](https://www.shelly.com/products/shelly-flood-s-gen4)
- [Shelly Plug M Gen3](https://www.shelly.com/products/shelly-plug-m-gen3-white)
- [Shelly Pro 3EM v2](https://www.shelly.com/products/shelly-pro-3em-v2)
- [Shelly Duo Bulb E27 Gen3](https://www.shelly.com/products/shelly-duo-bulb-e27-gen3)
- [Shelly Camera](https://www.shelly.com/products/shelly-camera)
- [Home Assistant: rozsvícení světla](https://www.home-assistant.io/actions/light.turn_on/)
