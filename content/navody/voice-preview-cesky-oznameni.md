---
title: "Voice Preview Edition: čeština a hlasová oznámení"
description: "Přidání Voice Preview Edition do Home Assistant, nastavení českého hlasu a oznámení z automatizace s úplným YAML příkladem."
cas: "6 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - Voice Preview Edition
  - Čeština
  - Hlasová oznámení
  - Automatizace
  - Assist
---

Voice Preview Edition umí s nastaveným hlasovým asistentem přijímat české povely a mluvit česky. Může také samo oznámit otevřené okno. Tento postup používá Home Assistant Cloud od Nabu Casa pro rozpoznávání řeči i český hlas. Po zkušebním období vyžaduje předplatné a pro zpracování řeči internet. Zařízení cloud povinně nevyžaduje; místní zpracování potřebuje vlastní nastavení a vhodný výkon serveru.

## 1. Přidejte zařízení

Připravte aktualizovaný Home Assistant, Voice Preview Edition, USB-C kabel, napájecí zdroj a heslo k Wi-Fi 2,4 GHz. V telefonu mějte aktuální aplikaci Home Assistant, přihlášení správce, zapnutý Bluetooth a potřebná oprávnění pro vyhledání zařízení.

1. Připojte zařízení k napájení a otevřete aplikaci Home Assistant.
2. V **Nastavení → Zařízení a služby** najděte objevené zařízení **Improv via BLE**. Vyberte přidání a zadejte údaje Wi-Fi 2,4 GHz.
3. Na výzvu stiskněte prostřední tlačítko pro potvrzení připojení.
4. Po připojení k Wi-Fi přidejte objevený **Home Assistant Voice** přes integraci **ESPHome**. Dokončete průvodce, aktualizaci a výběr hlasového asistenta.

Integraci Assist Satellite samostatně nepřidáváte: příslušnou entitu poskytne zařízení přes ESPHome.

## 2. Nastavte češtinu

Přihlaste Home Assistant k Nabu Casa v **Nastavení → Home Assistant Cloud**. Potom otevřete **Nastavení → Hlasoví asistenti**, v části **Assist** upravte asistenta Home Assistant Cloud a pojmenujte jej třeba „Česky“.

Nastavte jazyk asistenta na **češtinu**, konverzačního agenta na **Home Assistant** a u **Řeč na text** i **Text na řeč** zvolte **Home Assistant Cloud** s českým jazykem. V části Text na řeč vyberte nabízený český hlas. Pouhá změna jazyka uživatelského rozhraní nestačí.

V **Nastavení → Zařízení a služby → ESPHome** otevřete Voice Preview Edition a v jeho ovládacím prvku pro výběr hlasového asistenta přiřaďte „Česky“. Zařízení používá tento hlas i pro oznámení. České povely zpracuje rozpoznávání řeči a Assist; česká oznámení vytváří Text na řeč (TTS). Pro oznámení nemusíte nic říkat do mikrofonu.

## 3. Vyzkoušejte oznámení

Na stránce zařízení najděte entitu začínající `assist_satellite.` a zkopírujte její ID. V **Nástroje pro vývojáře → Akce** vyberte `assist_satellite.announce`, jako cíl tuto entitu a jako zprávu napište „Ahoj, toto je české hlasové oznámení.“ Spusťte akci. Volba `preannounce` zapíná zvuk před oznámením; standardně je zapnutá.

Pokud nic neslyšíte, ověřte hlasitost, dostupnost entity, přiřazeného asistenta a jeho české TTS. Zkontrolujte také internet a spojení zařízení s Home Assistant.

## 4. Přidejte oznámení do automatizace

V **Nastavení → Automatizace a scény** vytvořte novou prázdnou automatizaci a v nabídce otevřete **Upravit v YAML**. Vložte celý příklad. Nahraďte obě ID skutečnými entitami: kontakt okna musí mít otevřený stav `on`, cílem je vaše entita Assist Satellite.

```yaml
alias: Hlasové upozornění na otevřené okno
triggers:
  - trigger: state
    entity_id: binary_sensor.okno
    to: "on"
    for: "00:10:00"
conditions: []
actions:
  - action: assist_satellite.announce
    target:
      entity_id: assist_satellite.home_assistant_voice
    data:
      message: "Okno je už deset minut otevřené."
      preannounce: true
mode: single
```

Vizuálně lze stejnou akci přidat v části **Pak provést → Přidat akci**, vyhledat `assist_satellite.announce`, zvolit zařízení a zadat text. Do existující automatizace vložte tuto akci za dosavadní kroky. Čekání deset minut se při restartu Home Assistant nebo znovunačtení automatizací vynuluje.

## Zdroje

- [Nabu Casa: první nastavení Voice Preview Edition](https://support.nabucasa.com/hc/en-us/articles/25918770371229-Getting-started-with-Home-Assistant-Voice-Preview-Edition)
- [Home Assistant: nastavení hlasového asistenta přes Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)
- [Home Assistant: podporované jazyky Assist](https://developers.home-assistant.io/docs/voice/intent-recognition/supported-languages/)
- [Home Assistant: oznámení na hlasovém zařízení](https://www.home-assistant.io/actions/assist_satellite.announce/)
- [Home Assistant: Assist Satellite](https://www.home-assistant.io/integrations/assist_satellite/)
- [Home Assistant: Voice Preview Edition a jazyky](https://www.home-assistant.io/voice-pe/)
- [Home Assistant: stavové spouštěče a čekání](https://www.home-assistant.io/docs/automation/trigger/#state-trigger)
