---
title: "MQTT in Home Assistant: Mosquitto, Devices, and Automations"
seoTitle: "MQTT and Home Assistant: A Practical Setup Guide"
description: "How to securely run the Mosquitto MQTT broker, connect devices, use discovery, and create two practical automations."
obrazek: "/assets/images/mqtt-home-assistant.png"
obrazek_alt: "Illustration of an MQTT broker connected to a smart plug, lock, electric vehicle, and sensor."
cas: "15 minutes reading"
obtiznost: "Medium"
kontrola_zdroju: "2026-11-12"
stav: "Based on documentation"
temata:
  - "MQTT"
  - "Mosquitto"
  - "Automations"
  - "Local communication"
translationKey: "integrations.mqtt-home-assistant"
---

MQTT is a lightweight way for devices and services to exchange short messages. A device **publishes** a message to a topic, the broker receives it, and then distributes it to subscribers. Home Assistant can thus read sensors locally, control devices, or receive data from TeslaMate. However, the MQTT integration is not a broker; the easiest option is the official **Mosquitto broker** application.

## Installation and Secure Setup

On Home Assistant OS, open **Settings → Add-ons → Install Add-on**, search for the Mosquitto broker, install it, and start it. Then, in **Settings → Devices & Services**, add the **MQTT** integration. When using the official add-on, Home Assistant can set up the connection automatically and store the credentials itself.

Create accounts and strong passwords for your devices. Do not expose the broker to the internet. Port 1883 is unencrypted, so only use it within a trusted local network. Use TLS, a firewall, and preferably a VPN between networks. Also, back up other Mosquitto credentials.

## Discovery, Devices, and Availability

MQTT discovery is enabled by default in Home Assistant. A device or service sends a description to a topic starting with `homeassistant/`, and Home Assistant creates the corresponding device and entities. The device state should have its own availability topic and `online`/`offline` messages; the broker can send the last will upon connection loss. Retained messages help restore configuration and state, but old retained discovery messages can cause "ghost" entities.

Shelly Gen2+ can send state and receive commands via MQTT, but for general use, the official Shelly integration is simpler. TeslaMate can automatically create entities after setting `MQTT_HOME_ASSISTANT_DISCOVERY=true`; do not use the old `mqtt_sensors.yaml` file simultaneously, or duplicate IDs will be created. For Nuki, verify MQTT support for the specific model and firmware; MQTT is not a universal feature of all locks.

## Two Practical Automations

Place each block separately in **Settings → Automations & Scenes → Create Automation → Edit in YAML**. Replace the topics and entities with your own.

### High Temperature Alert

```yaml
alias: MQTT – High Temperature
triggers:
  - platform: mqtt
    topic: dum/technicka/teplota
conditions:
  - condition: template
    value_template: "{{ trigger.payload | float(0) > 35 }}"
actions:
  - service: persistent_notification.create
    data:
      title: High Temperature
      message: "Sensor reports {{ trigger.payload }} °C."
mode: single
```

The trigger is every message on the topic, the condition only allows values above 35 °C, and the action creates a notification in Home Assistant.

### Notification on Start Charging

```yaml
alias: TeslaMate – Charging Started
triggers:
  - platform: state
    entity_id: sensor.tesla_state
    to: "charging"
conditions: []
actions:
  - service: persistent_notification.create
    data:
      title: TeslaMate
      message: Car started charging.
mode: single
```

The entity is created via TeslaMate discovery; check its actual ID and value in **Developer Tools → States**.

## When MQTT Fails

In the MQTT integration, use **Configure → Listen to Topic** and enter the exact topic or `#`. Also monitor the Mosquitto log. A connection error usually means an incorrect address, port, account, password, or firewall. If messages are passing but no entity is created, check the discovery prefix, JSON, and `unique_id`. For unavailable entities, verify the availability topic. Listening to `#` may display sensitive data, so do not share the output without checking.

MQTT is local and vendor-agnostic, but it requires managing the broker and accounts. For supported products, their [official integration](/integrations/) is usually easier; only use MQTT where it is supported.

## Sources

- [Home Assistant: MQTT](https://www.home-assistant.io/integrations/mqtt/)
- [Home Assistant: MQTT trigger](https://www.home-assistant.io/triggers/mqtt/)
- [Home Assistant: Mosquitto broker](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md)
- [Shelly: MQTT for Gen2+ Devices](https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Mqtt/)
- [TeslaMate: Home Assistant Integration](https://docs.teslamate.org/docs/integrations/home_assistant/)
