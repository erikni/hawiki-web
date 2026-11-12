---
title: "MQTT v Home Assistantu: Mosquitto, zařízení a automatizace"
seoTitle: "MQTT a Home Assistant: praktický průvodce nastavením"
description: "Jak bezpečně zprovoznit MQTT broker Mosquitto, připojit zařízení, použít discovery a vytvořit dvě praktické automatizace."
obrazek: "/assets/images/mqtt-home-assistant.png"
obrazek_alt: "Ilustrace MQTT brokeru propojeného s chytrou zásuvkou, zámkem, elektromobilem a čidlem."
cas: "15 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-11-12"
stav: "Podle dokumentace"
temata:
  - "MQTT"
  - "Mosquitto"
  - "Automatizace"
  - "Lokální komunikace"
---

MQTT je lehký způsob, jak si zařízení a služby předávají krátké zprávy. Zařízení zprávu **publikuje** do tématu (topic), broker ji převezme a rozešle odběratelům. Home Assistant tak může místně číst čidla, ovládat zařízení nebo přijímat data z TeslaMate. Integrace MQTT ale není broker: nejsnazší volbou je oficiální aplikace **Mosquitto broker**.

## Instalace a bezpečné nastavení

Na Home Assistant OS otevřete **Nastavení → Aplikace → Instalovat aplikaci**, vyhledejte Mosquitto broker, nainstalujte jej a spusťte. Potom v **Nastavení → Zařízení a služby** přidejte integraci **MQTT**. Při použití oficiální aplikace může Home Assistant spojení nastavit automaticky a přihlašovací údaje uchovat sám.

Pro zařízení vytvořte účty a silná hesla. Broker nevystavujte do internetu. Port 1883 je nešifrovaný, proto jej používejte jen v důvěryhodné místní síti. Mezi sítěmi použijte TLS, firewall a raději VPN. Zálohujte také další přihlášení Mosquitto.

## Discovery, zařízení a dostupnost

MQTT discovery je v Home Assistantu standardně zapnuté. Zařízení nebo služba pošle popis do tématu začínajícího `homeassistant/` a Home Assistant vytvoří odpovídající zařízení a entity. Stav zařízení má mít vlastní téma dostupnosti a zprávy `online`/`offline`; broker může poslední vůli odeslat při výpadku spojení. Retained zprávy pomohou obnovit konfiguraci a stav, ale staré retained discovery zprávy mohou vracet „duchové“ entity.

Shelly Gen2+ umí posílat stav a přijímat příkazy přes MQTT, ale pro běžné použití je jednodušší oficiální integrace Shelly. TeslaMate může po zapnutí `MQTT_HOME_ASSISTANT_DISCOVERY=true` vytvořit entity automaticky; nepoužívejte současně starý soubor `mqtt_sensors.yaml`, jinak vzniknou duplicitní ID. U Nuki ověřte podporu MQTT pro konkrétní model a firmware; MQTT není univerzální vlastnost všech zámků.

## Dvě praktické automatizace

Každý blok vložte samostatně do **Nastavení → Automatizace a scény → Vytvořit automatizaci → Upravit v YAML**. Témata a entity nahraďte vlastními.

### Upozornění při přehřátí

```yaml
alias: MQTT – vysoká teplota
triggers:
  - trigger: mqtt
    topic: dum/technicka/teplota
conditions:
  - condition: template
    value_template: "{{ trigger.payload | float(0) > 35 }}"
actions:
  - action: persistent_notification.create
    data:
      title: Vysoká teplota
      message: "Čidlo hlásí {{ trigger.payload }} °C."
mode: single
```

Spouštěčem je každá zpráva v tématu, podmínka propustí jen hodnotu nad 35 °C a akce vytvoří oznámení v Home Assistantu.

### Oznámení po zahájení nabíjení

```yaml
alias: TeslaMate – začalo nabíjení
triggers:
  - trigger: state
    entity_id: sensor.tesla_state
    to: "charging"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: TeslaMate
      message: Auto se začalo nabíjet.
mode: single
```

Entity vzniká přes discovery TeslaMate; její skutečné ID i hodnotu zkontrolujte v **Nástroje pro vývojáře → Stavy**.

## Když MQTT nefunguje

V integraci MQTT použijte **Konfigurovat → Poslouchat téma** a zadejte přesné téma nebo `#`. Sledujte také protokol Mosquitto. Chyba připojení obvykle znamená špatnou adresu, port, účet, heslo nebo firewall. Když chodí zprávy, ale nevzniká entita, zkontrolujte discovery prefix, JSON a `unique_id`. U nedostupné entity ověřte téma dostupnosti. Poslech `#` může zobrazit citlivé údaje, proto výpis nesdílejte bez kontroly.

MQTT je místní a nezávislé na výrobci, ale vyžaduje správu brokeru a účtů. Pro podporované produkty bývá snazší jejich [oficiální integrace](/integrace/); MQTT volte jen tam, kde je podporované.

## Zdroje

- [Home Assistant: MQTT](https://www.home-assistant.io/integrations/mqtt/)
- [Home Assistant: MQTT trigger](https://www.home-assistant.io/triggers/mqtt/)
- [Home Assistant: Mosquitto broker](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md)
- [Shelly: MQTT pro zařízení Gen2+](https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Mqtt/)
- [TeslaMate: integrace s Home Assistantem](https://docs.teslamate.org/docs/integrations/home_assistant/)
