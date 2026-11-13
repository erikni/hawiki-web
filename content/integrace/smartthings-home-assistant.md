---
title: "SmartThings a Home Assistant: propojení krok za krokem"
description: "Jak připojit SmartThings k Home Assistantu, co funguje se Samsung TV a na co dát pozor u cloudu, oprávnění a VLAN."
obrazek: "/assets/images/smartthings-home-assistant.png"
obrazek_alt: "Ilustrace chytré domácnosti propojené s Home Assistantem přes internetový cloud."
cas: "10 minut čtení"
obtiznost: "Další krok"
kontrola_zdroju: "2026-11-03"
stav: "Podle dokumentace"
temata:
  - "SmartThings"
  - "Samsung TV"
  - "Cloud"
  - "Automatizace"
---

## Co propojení přinese

Oficiální integrace **SmartThings** zpřístupní v Home Assistantu zařízení a scény z domácnosti SmartThings. Hodí se hlavně pro spotřebiče Samsung, televizory a již používaný SmartThings Hub. Podle konkrétního zařízení mohou vzniknout světla, senzory, zámky, termostaty, přehrávače nebo další entity. Ne každá funkce z aplikace je ale dostupná přes API.

Jde o integraci **Cloud Push**: Home Assistant posílá příkazy do cloudu SmartThings a změny dostává zpět jako cloudové události. Bez internetu proto propojení nefunguje. Přihlašovací tokeny spravuje OAuth průvodce; nevytvářejte starý dlouhodobý osobní token podle zastaralých návodů. Samsung navíc oznámil přechod přístupu k API na placený osobní plán od října 2026, proto před instalací ověřte aktuální podmínky.

## Co potřebujete a jak integraci přidat

Potřebujete účet Samsung, zařízení už přidaná v mobilní aplikaci SmartThings a aktuální Home Assistant s načtenou výchozí cloudovou komponentou. Integrace se nastavuje v rozhraní, nikoli v `configuration.yaml`.

1. V Home Assistantu otevřete **Nastavení → Zařízení a služby → Přidat integraci → SmartThings**.
2. Přihlaste se k účtu Samsung a schvalte požadovaná oprávnění. Povolte pouze domácnost a přístup, který chcete Home Assistantu svěřit.
3. Po návratu zkontrolujte vytvořená zařízení a entity. Názvy jako `media_player.obyvak_tv` jsou jen příklady; použijte vlastní ID z HA.

Samsung TV se může objevit jako přehrávač, jen pokud přes SmartThings poskytuje potřebné schopnosti. Pro místní ovládání podporované televize bývá vhodnější samostatná integrace Samsung Smart TV. U ní může být překážkou oddělená VLAN: televizory nepřijímají WebSocket spojení z jiné podsítě. SmartThings toto místní spojení nepoužívá, ale závisí na internetu a cloudu Samsungu.

## Dva praktické příklady

Každý blok vložte **samostatně** do nové automatizace přes **Upravit v YAML**. Nejdřív nahraďte ukázková ID skutečnými entitami.

### Rozsvícení při otevření dveří

```yaml
alias: SmartThings – světlo při otevření dveří
triggers:
  - trigger: state
    entity_id: binary_sensor.vstupni_dvere
    from: "off"
    to: "on"
conditions:
  - condition: state
    entity_id: sun.sun
    state: below_horizon
actions:
  - action: light.turn_on
    target:
      entity_id: light.predsin
mode: single
```

Spouštěčem je změna kontaktu dveří, podmínkou noc a akcí zapnutí světla.

### Upozornění po dokončení praní

```yaml
alias: SmartThings – pračka dokončila program
triggers:
  - trigger: state
    entity_id: sensor.pracka_stav
    to: "complete"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: Pračka
      message: Program skončil. Prádlo můžete vyndat.
mode: single
```

Hodnota `complete` je pouze příklad. V **Nástroje pro vývojáře → Stavy** nejprve zjistěte skutečnou entitu a hodnotu, kterou váš model hlásí.

## Když něco chybí nebo nefunguje

Otevřete integraci SmartThings, zařízení a **Stáhnout diagnostiku**; u problémů se stavy zapněte ladicí protokolování. Chybějící funkce často zařízení neposkytuje přes API nebo ji integrace dosud nemapuje. Při chybě přihlášení zopakujte autorizaci a zkontrolujte oprávnění. Ověřte internet, DNS a odchozí HTTPS z VLAN Home Assistantu; příchozí port do domácí sítě neotevírejte. Tokeny nikam nekopírujte.

Výhodou je široký záběr zařízení a snadné UI nastavení. Nevýhodou je cloud, proměnlivá podpora funkcí a nové podmínky API. Pro Zigbee, Z-Wave nebo Matter zařízení zvažte přímé místní připojení k HA; pro televizi porovnejte místní integraci Samsung Smart TV.

## Zdroje

- [Home Assistant: SmartThings](https://www.home-assistant.io/integrations/smartthings/)
- [SmartThings: Authorization and Permissions](https://developer.smartthings.com/docs/getting-started/authorization-and-permissions)
- [SmartThings: Architecture and Authorization Flow](https://developer.smartthings.com/docs/service-integrations/architecture-and-auth-flow)
- [SmartThings: A New Enhanced SmartThings API Experience](https://community.smartthings.com/t/a-new-enhanced-smartthings-api-experience/309947)
- [Home Assistant: Samsung Smart TV](https://www.home-assistant.io/integrations/samsungtv/)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: trvalá oznámení](https://www.home-assistant.io/integrations/persistent_notification/)
