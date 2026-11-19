---
title: "Voice Preview Edition: Czech commands and announcements"
description: "Add Voice Preview Edition to Home Assistant, configure Czech speech and create an announcement automation with a complete YAML example."
cas: "6-minute read"
obtiznost: "Intermediate"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
translationKey: "guides.voice-preview-czech-announcements"
temata:
  - Voice Preview Edition
  - Czech
  - Voice announcements
  - Automation
  - Assist
---

Voice Preview Edition can understand Czech commands and speak Czech when its voice assistant is configured accordingly. It can also announce an open window automatically. This procedure uses Home Assistant Cloud from Nabu Casa for speech recognition and a Czech voice. A subscription is required after the trial period, and speech processing needs an internet connection. Cloud processing is not compulsory, but local processing requires a custom setup and a sufficiently powerful server.

## 1. Add the device

Prepare an up-to-date Home Assistant installation, Voice Preview Edition, a USB-C cable, a power supply and the password for a 2.4 GHz Wi-Fi network. On your phone, install the latest Home Assistant app and have an administrator login ready. Enable Bluetooth and grant the permissions required to discover devices.

1. Connect the device to power and open the Home Assistant app.
2. Under **Settings → Devices & services**, open the discovered **Improv via BLE** device. Choose to add it and enter the 2.4 GHz Wi-Fi details.
3. When prompted, press the middle button to confirm the connection.
4. After the device joins Wi-Fi, add the discovered **Home Assistant Voice** through the **ESPHome** integration. Complete the wizard, install any offered update and select a voice assistant.

Do not add the Assist Satellite integration separately. The device provides the relevant entity through ESPHome.

## 2. Configure Czech

Connect Home Assistant to Nabu Casa under **Settings → Home Assistant Cloud**. Then open **Settings → Voice assistants** and configure a Home Assistant Cloud assistant under **Assist**. Give it a clear name such as **Czech**.

Set the assistant language to **Czech** and the conversation agent to **Home Assistant**. Select **Home Assistant Cloud** with Czech for both **Speech-to-text** and **Text-to-speech**, then choose an available Czech voice. Changing the user-interface language alone is not enough.

Under **Settings → Devices & services → ESPHome**, open Voice Preview Edition and assign the **Czech** assistant using its voice-assistant selection control. The device also uses this voice for announcements. Czech commands use speech recognition and Assist; Czech announcements use text-to-speech (TTS). You do not need to speak into the microphone for an announcement.

## 3. Test an announcement

On the device page, find the entity beginning with `assist_satellite.` and copy its ID. In **Developer tools → Actions**, select `assist_satellite.announce`, target that entity and enter a short Czech test message. Run the action. The `preannounce` option plays a sound before the message and is enabled by default.

If you hear nothing, check the volume, entity availability, assigned assistant and its Czech TTS configuration. Also check the internet connection and the device's connection to Home Assistant.

## 4. Add the announcement to an automation

Under **Settings → Automations & scenes**, create an empty automation and choose **Edit in YAML**. Paste the complete example below. Replace both entity IDs: the window contact must use the `on` state, and the target must be your Assist Satellite entity.

```yaml
alias: Voice announcement for open window
triggers:
  - platform: state
    entity_id: binary_sensor.window
    to: "on"
    for: "00:10:00"
condition: []
action:
  - service: assist_satellite.announce
    target:
      entity_id: assist_satellite.home_assistant_voice
    data:
      message: "The window has been open for ten minutes."
      preannounce: true
mode: single
```

You can add the same action visually under **Action → Add action**. Search for `assist_satellite.announce`, select the device and enter the message. Add it after the existing steps in an automation. The ten-minute wait resets if Home Assistant restarts or automations are reloaded.

## Sources

- [Nabu Casa – Getting started with Voice Preview Edition](https://support.nabucasa.com/hc/en-us/articles/25918770371229-Getting-started-with-Home-Assistant-Voice-Preview-Edition)
- [Home Assistant – Setting up a voice assistant using Home Assistant Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)
- [Home Assistant – Supported languages for Assist](https://developers.home-assistant.io/docs/voice/intent-recognition/supported-languages/)
- [Home Assistant – Announcing on a voice device](https://www.home-assistant.io/actions/assist_satellite.announce/)
- [Home Assistant – Assist Satellite](https://www.home-assistant.io/integrations/assist_satellite/)
- [Home Assistant Voice Preview Edition](https://www.home-assistant.io/voice-pe/)
- [Home Assistant – State trigger](https://www.home-assistant.io/docs/automation/trigger/#state-trigger)
