---
title: "ZHA vs Zigbee2MQTT: what to choose for Home Assistant"
seoTitle: "ZHA vs Zigbee2MQTT: what to choose for Home Assistant"
description: "Compare the direct ZHA integration with standalone Zigbee2MQTT. Decide based on device support and home management style."
cas: "4 min read"
obtiznost: "Beginner"
kontrola_zdroju: "2026-10-08"
stav: "Based on documentation"
sourceType: "official-docs"
temata: ["Zigbee", "ZHA", "Zigbee2MQTT", "Integration"]
translationKey: "zigbee.zha-vs-zigbee2mqtt"
obrazek: "/assets/images/zha-vs-zigbee2mqtt.png"
obrazek_alt: "Illustration of two ways to connect wireless devices to a home: directly and via other software services."
---

## Same Need, Two Connection Paths

You want to use a Zigbee sensor or light in Home Assistant. For direct connection, you need a coordinator and software to manage the network. **ZHA** handles this role as a Home Assistant integration. **Zigbee2MQTT** is standalone software that feeds information into Home Assistant via MQTT. Simply buying an adapter does not solve the entire path choice.

Before you start, review the [Zigbee roadmap](/zigbee/) and verify the specific radio and devices in the documentation of your chosen project. There is no single best option for every home.

## ZHA: Management within Home Assistant

You set up ZHA within Home Assistant and do not require a separate MQTT broker. For the first device, this means fewer components to prepare. The documentation describes supported radio adapters, pairing, and network management options.

The advantage is the centralization of settings in one place. The limitation is that some products have non-standard features that require special support. The Zigbee logo does not guarantee access to every function. Editorial recommendation: if you are starting out and the required devices are supported, ZHA is a straightforward first path.

## Zigbee2MQTT: Standalone Service

Zigbee2MQTT requires a supported adapter, a running service, and an MQTT broker. Home Assistant connects via the MQTT integration; device discovery uses MQTT discovery. The service can run alongside Home Assistant, but its installation and updates must be included in your home management.

The advantage is the separation of Zigbee management and a catalog of supported devices with descriptions of their functions. The disadvantage is the multiple components whose connection must function. Recommendation: consider this path if you have documented support for the required model, or if you want to manage Zigbee separately and understand MQTT.

## What to Verify Before Deciding

- **Coordinator:** Must be supported by the chosen software, including the required firmware.
- **Exact Model:** Compare required functions, not just the manufacturer's name.
- **Management:** For Zigbee2MQTT, also account for the MQTT broker and connection to Home Assistant.
- **Recovery:** Before expanding, find out the method for backing up and restoring your chosen solution.

One coordinator cannot simultaneously run both services. If you want to test a second path alongside your existing network, you need a separate suitable radio. When changing solutions, do not automatically assume all settings will transfer; plan the process according to the documentation and do not mess with the entire home immediately.

## Practical Start

Choose one path, connect one device, and verify the required function. Then proceed to [first automation](/guides/evening-lamp/). If the device does not respond, first check the power and connection according to the [troubleshooting guide](/help/device-not-responding/). Changing software is not the first step in every failure.

## Sources

- [Home Assistant: ZHA](https://www.home-assistant.io/integrations/zha/)
- [Zigbee2MQTT: getting started and requirements](https://www.zigbee2mqtt.io/guide/getting-started/)
- [Zigbee2MQTT: integration with Home Assistant](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html)
- [Zigbee2MQTT: supported devices](https://www.zigbee2mqtt.io/supported-devices/)
