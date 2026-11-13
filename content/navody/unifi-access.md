---
title: "UniFi Access a Home Assistant: dveře, světla a upozornění"
description: "Jak připojit UniFi Access do Home Assistantu a využít stav dveří, zvonek a události vstupu v automatizacích."
obrazek: "/assets/images/unifi-access.png"
obrazek_alt: "Ilustrace vstupních dveří se čtečkou propojených s domácí automatizací, světlem a upozorněním."
cas: "5 minut čtení"
obtiznost: "Další krok"
kontrola_zdroju: "2026-10-27"
stav: "Podle dokumentace"
temata:
  - "UniFi Access"
  - "Dveře"
  - "Automatizace"
  - "Lokální provoz"
---

## Co propojení přinese

UniFi Access je systém řízení vstupu od Ubiquiti se sídlem v USA. Spravuje čtečky, dveřní zámky a přístupová oprávnění. Home Assistant k němu přidává návaznosti na domácnost: rozsvícení předsíně, upozornění na otevřené dveře nebo oznámení při zazvonění.

Použijte integraci **UniFi Access**, nikoli UniFi Network pro síť nebo Protect pro kamery. Je součástí HA od verze 2026.4, HACS nepotřebujete. S řadičem komunikuje v místní síti přes API a průběžné aktualizace WebSocket.

## Co potřebujete a jak začít

Potřebujete funkční systém Access s aplikací na podporované UniFi konzoli, dveřním hubem a odpovídajícím zapojením. HA musí na konzoli dosáhnout v síti. Samotný Wi-Fi přístupový bod nestačí.

1. V aplikaci **Access → Settings → General** vyhledejte **API Token**, případně v části **Advanced**. Vytvořte token pro HA, nastavte oprávnění a bezpečně jej uložte; zobrazí se jen jednou. Nevytvářejte klíč na stránce Integrations konzole pro Protect.
2. V HA otevřete **Nastavení → Zařízení a služby → Přidat integraci → UniFi Access**. Zadejte adresu řadiče a token.
3. Ověřte vytvořené entity. Tlačítko odemknutí vyšle impulz na dobu nastavenou v Access. Binární senzor dveří hlásí otevřeno (`on`) a zavřeno (`off`); pro skutečnou polohu potřebujete správně zapojený dveřní kontakt.

Tlačítko odemknutí není důkazem zavřených ani zamčených dveří. Běžné odemykání také není příkaz k trvalému odemčení.

## Dva příklady k vložení

Každý blok vložte **samostatně** do nové automatizace přes **Upravit v YAML**. Nahraďte `binary_sensor.vchod_door` skutečným senzorem Access a `light.predsin` vlastním světlem. Světlo musí být už připojené do HA.

### Rozsvícení při otevření po západu slunce

```yaml
alias: Access – světlo při otevření dveří
triggers:
  - trigger: state
    entity_id: binary_sensor.vchod_door
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

Příklad světlo pouze zapne. Pro automatické zhasnutí lze přidat samostatnou automatizaci podle pohybu.

### Dveře otevřené déle než dvě minuty

```yaml
alias: Access – dlouho otevřené dveře
triggers:
  - trigger: state
    entity_id: binary_sensor.vchod_door
    from: "off"
    to: "on"
    for: "00:02:00"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: Vstupní dveře
      message: Dveře jsou otevřené déle než dvě minuty.
mode: single
```

Oznámení najdete uvnitř HA; nejde o push zprávu do telefonu. Čekání `for` se při restartu HA nebo načtení automatizací vynuluje.

## Zvonek a zamítnutý vstup

Další automatizaci sestavte v editoru: jako spouštěč vyberte přijetí události příslušné entity Access a typ `access_denied`, jako akci vytvoření oznámení. Pro zvonek použijte jeho událost `ring`, například k bliknutí světla. Událost `access_granted` může spustit uvítací scénu; sama ale nepotvrzuje, že člověk prošel dovnitř. Zvonění nepodporuje každá kombinace hardwaru, přesto může entita vzniknout.

Oprávnění a časové plány návštěv spravujte v Access. Režimy **Evacuation** a **Lockdown** zasahují všechny dveře řadiče; nepoužívejte je jako běžné odemknutí jedněch dveří. Po nastavení ručně otevřete a zavřete dveře, ověřte senzor a prohlédněte stopu automatizace. Při chybě připojení zkontrolujte dostupnost konzole, firewall a platnost tokenu.

## Zdroje

- [Home Assistant: UniFi Access](https://www.home-assistant.io/integrations/unifi_access/)
- [Ubiquiti: oficiální UniFi API](https://help.ui.com/hc/en-us/articles/30076656117655-Getting-Started-with-the-Official-UniFi-API)
- [Ubiquiti: dokumentace Access API](https://assets.identity.ui.com/unifi-access/api_reference.pdf)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: trvalá oznámení](https://www.home-assistant.io/integrations/persistent_notification/)
- [Ubiquiti: sídlo společnosti](https://www.ui.com/contact/)
