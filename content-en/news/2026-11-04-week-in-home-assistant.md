---
title: "Week in Home Assistant: New Naming Conventions, Safer ESPHome, and AI in Beta"
description: "A roundup from October 28th to November 3rd, 2026: new naming conventions in Home Assistant 2026.11, ESPHome 2026.10.2, AI fixes, and the November WTH challenge."
cas: "4 minutes"
obtiznost: "Overview"
kontrola_zdroju: "2026-11-04"
stav: "Verified against official sources"
temata: [Home Assistant, News, ESPHome, AI, Shelly, UniFi, Community]
obrazek: "/assets/images/novinky-2026-11-04.png"
obrazek_alt: "Illustration of a smart home with organized devices and a secure update of a small control board"
translationKey: "news.2026-11-04-week-in-home-assistant"
---
## Names are changing, automations remain

The roundup from October 28th to November 3rd, 2026, follows [last week](/news/2026-10-27-week-in-home-assistant/). The period included a free day on October 27th: this is when stable Home Assistant OS 18.4 was released, and Everything Presence presence sensors joined Works with Home Assistant. In this edition, we focus on the more recent events.

## Home Assistant 2026.11 cleans up device names

On November 3rd, Home Assistant introduced new handling for names, which will arrive in the stable 2026.11 version the following day. Devices and entities will be named only by what they actually are, and the interface will supplement this with a room or parent device as needed. For example, a power strip can have every socket treated as a separate "child device" with its own name and room.

Existing entity IDs should not change during the update, so automations, scripts, scenes, and dashboards will continue to function. However, visible names might look different. Therefore, after updating, be sure to check custom cards and templates that use the `friendly_name` attribute. Support for child devices will begin with Z-Wave, MQTT, ESPHome, and parts of Tuya; Matter and ZHA are expected to follow. At the time of checking, this was only an announcement of the change for the 2026.11 release, not the stable version during the covered period.

## ESPHome 2026.10.2 fixes risky update

The patch ESPHome 2026.10.2 was released on November 3rd. The most important fix is for devices with the RTL8710B chip: it bypasses an issue where a compressed wireless device update could cause malfunction. It also fixes TLS 1.3 for `audio_http`, releases held Bluetooth proxy connections, and offers downloading compiled firmware from Device Builder for host devices.

These are fixes for the ESPHome tool and its firmware, not a new Home Assistant Core integration. Before updating your own boards, it is advisable to back up the configuration and verify which chip the device uses.

## AI: two fixes still only in beta

Beta Core 2026.11.0b3 from November 2nd fixes blocking schema loading when calling MCP tools and the situation where the OpenRouter integration could call a tool twice. This may be important for automations that allow a language model to perform actions. However, this is not a stable update; regular users should wait for the final 2026.11 and subsequent fixes.

## November collects home "Why isn't this working?"

The community month "What the Heck?!" runs from October 29th. Authors invite even non-technical household members to describe what is confusing or unnecessarily complicated in Home Assistant. Practical tip: ask people at home what bothers them about the controls, and send their experience to the dedicated forum category.

In the checked sources, we did not find a new stable firmware version for Shelly or any changes directly in the Shelly, UniFi Network, or UniFi Protect integrations between October 28th and November 3rd. Shelly 2.2.0 remained in the beta part of the changelog. No new Works with Home Assistant partnerships or new HA proprietary hardware appeared on the official blog during this period.

## Sources

- [Home Assistant – new device and entity naming](https://www.home-assistant.io/blog/2026/11/03/naming-things-in-home-assistant/)
- [Home Assistant Core 2026.11.0b3](https://github.com/home-assistant/core/releases/tag/2026.11.0b3)
- [Home Assistant – What the Heck?! month 2026](https://www.home-assistant.io/blog/2026/10/29/what-the-heck-2026/)
- [ESPHome 2026.10 and patch release](https://esphome.io/blog/2026/10/21/esphome-2026-10/)
- [ESPHome 2026.10.2 on GitHub](https://github.com/esphome/esphome/releases/tag/2026.10.2)
- [Home Assistant OS 18.4](https://github.com/home-assistant/operating-system/releases/tag/18.4)
- [Everything Smart Home joins Works with Home Assistant](https://www.home-assistant.io/blog/2026/10/27/everything-smart-home-joins-works-with-home-assistant/)
- [Shelly – Gen2+ firmware changelog](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – Shelly integration](https://www.home-assistant.io/integrations/shelly/)
- [Home Assistant – UniFi Network integration](https://www.home-assistant.io/integrations/unifi/)
- [Home Assistant – UniFi Protect integration](https://www.home-assistant.io/integrations/unifiprotect/)
- [Works with Home Assistant – partner announcement](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
