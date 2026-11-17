---
title: "Devices, entities and integrations: what the terms mean"
description: "Understand essential Home Assistant terminology through the example of a smart plug."
cas: "5-minute read"
obtiznost: "Beginner"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
translationKey: "getting-started.devices-entities-integrations"
temata:
  - "Devices"
  - "Entities"
  - "Integrations"
---

## One plug, several items

After connecting a smart plug, Home Assistant may show more items than you expected. As well as an on/off control, you might see power or energy readings. This does not mean that you have several plugs. Home Assistant distinguishes the connection to a product, the device itself and each of its functions.

The plug below is only an example, not a recommendation for a particular manufacturer. Measurements are available only when both the model and its integration support them.

## Integration: the connection to Home Assistant

An **integration** is the software component that connects Home Assistant to a device or service. It allows the system to receive information and send supported commands. Depending on the product, the connection may work directly over your home network, through a hub or through an internet service.

One integration can expose several devices. For example, an integration for a particular hub may connect all the lights that communicate with that hub. An integration's name therefore does not necessarily describe a single product. Always check the integration documentation for the appropriate connection method.

## Device: one place for related functions

A **device** groups related items. For our smart plug, think of it as the page for the complete product, where its available functions and information appear together.

A device often represents one physical product, but this is not a strict rule. Home Assistant may also use a device to represent a service or several parts of a more complex product. For now, it is enough to know that a device page brings its related entities together.

## Entity: a particular control or value

An **entity** represents one measured value, control or other function. The example plug might provide these entities:

| Entity | Purpose |
| --- | --- |
| Plug switch | Turns the power on and off |
| Power sensor | Shows current power, usually in watts |
| Energy sensor | Shows measured energy, for example in kilowatt-hours |

Every entity has a state. A switch can be on or off, while a sensor displays a measured value. An entity may also have additional attributes, such as its unit of measurement.

An entity ID might look like `switch.lamp` or `sensor.lamp_power`. The part before the dot identifies its type, known as the domain. Its displayed name can be friendlier, such as **Living-room lamp**. These IDs are examples; the ones in your home will be different.

## Where to find them

Open **Settings → Devices & services**. The Integrations tab shows configured connections, Devices lists individual devices and Entities lists the specific controls and values. Open a device you recognise and inspect its entities. You do not need to rename or delete anything for this exercise.

## Why this helps when following guides

When you add a card to your [dashboard](/guides/home-dashboard/), you select a particular control or value. To turn a lamp on through the plug, choose its switch. To see its current power, choose the power sensor. It is the same product, but a different function.

When a guide asks you to select an entity, look for the required function rather than relying on a similar product name. Understanding this distinction makes dashboards easier to build and automations easier to troubleshoot.

## Sources

- [Home Assistant – Concepts and terminology](https://www.home-assistant.io/getting-started/concepts-terminology/)
- [Home Assistant – Entities and domains](https://www.home-assistant.io/docs/configuration/entities_domains/)
- [Home Assistant – Setting up an integration](https://www.home-assistant.io/getting-started/integration/)
- [Home Assistant developer documentation – Device registry](https://developers.home-assistant.io/docs/device_registry_index/)
