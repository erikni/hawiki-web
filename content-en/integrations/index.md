---
type: hub
title: "Home Assistant Integrations"
seoTitle: "Home Assistant Integrations: Devices and Services"
description: "Connect devices and services from various manufacturers. Start by understanding the concepts, select the connection method, and proceed to existing guides."
kontrola_zdroju: "2026-10-08"
translationKey: "integrations.index"
---

## What are Integrations

An integration is the connection between Home Assistant and a specific device, service, or technology. It makes their functions available, which you can then use in dashboards and automations. However, the manufacturer's name does not mean that every product they offer uses the same connection method. Look for the exact model and function you actually need.

Start with [understanding devices, entities, and integrations](/getting-started/devices-entities-and-integrations/). Then, choose a small initial task: for example, controlling a light or monitoring an open window. This will help you determine whether you need a switch, a sensor, or a service for notifications.

## How to Choose a Connection Method

For some devices, Home Assistant will find the integration automatically; for others, you will add it manually in Settings → Devices & Services. Always verify the procedure in the specific integration's documentation. Be sure to distinguish between connections directly on the local network and connections via the manufacturer's cloud service over the internet. Account requirements and available features vary.

Before purchasing, review the [protocol guide](/buying-guide/zigbee-wifi-thread-matter/). For Zigbee, continue through the [topic index](/zigbee/), which helps with the coordinator and software selection. For Matter or Thread devices, also check for necessary home network equipment.

## Shelly Devices

[Overview of Shelly Devices](/buying-guide/shelly-devices-overview/) explains the differences between ranges and connection types. The official Shelly integration communicates directly with supported devices; the cloud is not necessary for this communication. However, do not confuse this method with connecting all Bluetooth or Zigbee products from the brand. The specific model determines the method.

## Cameras and Other Software

If you are dealing with cameras, read the [introduction to Frigate](/guides/frigate-cameras/). For expanding beyond the standard offering, the [HACS guide](/more-options/hacs/) is available. Always verify first whether the required function is already in a standard integration and who manages the add-on.

## After Connecting and Troubleshooting

Check that the device offers the required entity and responds to control. Name them clearly according to the room and purpose. Only then should you proceed to [automations](/automations/). If a device disappears or does not respond, start by checking the power and connection; if it relies on the cloud, also verify the internet connection.

For other brands, use the integration catalog in the Home Assistant documentation for now. Independent guides on the HA wiki will be added with plenty of verified content.

## Sources

- [Home Assistant: Integrations and basic concepts](https://www.home-assistant.io/getting-started/concepts-terminology/)
- [Home Assistant: Shelly integration](https://www.home-assistant.io/integrations/shelly/)
- [Shelly: Technical documentation](https://shelly-api-docs.shelly.cloud/)
