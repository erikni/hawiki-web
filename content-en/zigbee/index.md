---
type: hub
title: "Zigbee in Home Assistant: A Complete Guide"
seoTitle: "Zigbee in Home Assistant: ZHA, Zigbee2MQTT and Guides"
description: "Choose a way to connect Zigbee devices, understand the mesh network, and proceed to the right adapter and first guide."
kontrola_zdroju: "2026-10-08"
translationKey: "zigbee.index"
---

## What is Zigbee and where to start

Zigbee connects devices such as lights, sockets, and sensors into its own wireless network. To connect directly to Home Assistant, you need a supported coordinator and software to manage the network. First, clarify which devices you want to control and what functions you require. Buying a radio is a subsequent step.

If you are unsure about the names, start with [explanation of Zigbee, Wi-Fi, Thread, and Matter](/buying-guide/zigbee-wifi-thread-matter/). These are not mutually interchangeable brands. Similarly, a Z-Wave adapter cannot replace a Zigbee coordinator. This guide will walk you through the selection process and link to detailed information where you will need it.

## How the mesh network works

The coordinator establishes the network; devices acting as repeaters can relay messages further. Battery-powered sensors typically do not relay messages from other devices. When expanding your home, therefore, think about placing mains-powered repeaters, not just the number of sensors. Always verify specific capabilities for the given product.

The failure of one sensor is not a reason to change the entire network immediately. First, check the battery, availability, and location. If you encounter problems after moving a device, use the procedure [when a device does not respond](/help/device-not-responding/).

## Coordinator and recommended equipment

Choose a radio based on the support available in the intended software. On the HA wiki, you can find [guide to Home Assistant Connect ZBT-2](/buying-guide/home-assistant-connect-zbt-2/). Before purchasing, also check the adapter's connection to your computer and the documentation for the exact model. One product guide is not a universal promise of compatibility.

## ZHA or Zigbee2MQTT

ZHA is an integration within Home Assistant. Zigbee2MQTT is standalone software that passes devices via MQTT. Both methods require a suitable coordinator. In [comparison of ZHA and Zigbee2MQTT](/zigbee/zha-vs-zigbee2mqtt/), you can find the differences in setup and management. Decide based on your specific devices and willingness to maintain additional software.

## Adding the first device

Start with one sensor or light. Depending on the chosen method, enable the connection and run the pairing procedure according to the manufacturer's instructions. After adding it, verify the required function in Home Assistant before creating automation. For guidance, [explanation of devices, entities, and integrations](/getting-started/devices-entities-and-integrations/).

## Sources

- [Home Assistant: ZHA](https://www.home-assistant.io/integrations/zha/)
- [Zigbee2MQTT: getting started](https://www.zigbee2mqtt.io/guide/getting-started/)
