---
title: "This week in Home Assistant: AUX-2 revives older gear"
description: "News for 11–17 November 2026: Home Assistant Connect AUX-2, Core 2026.11.2 fixes, Shelly firmware 2.2.1, and checks on UniFi, AI and ESPHome."
cas: "4 minutes"
obtiznost: "Roundup"
kontrola_zdroju: "2026-11-18"
stav: "Verified against official sources"
translationKey: "news.week-2026-11-18"
temata: [Home Assistant, News, Hardware, Shelly, UniFi, AI, ESPHome]
obrazek: "/assets/images/novinky-2026-11-18.png"
obrazek_alt: "Illustration of an older amplifier connected to a network and Home Assistant through a smart multi-purpose bridge"
---
## AUX-2 connects older gear to Home Assistant

This roundup covers 11–17 November 2026. The week’s biggest announcement is **Home Assistant Connect AUX-2**, a small box designed to bring older audio equipment, serial devices, a Z-Wave adapter and Bluetooth sensors into a smart home.

AUX-2 includes a combined analogue and digital audio output, two RS-232 ports, USB-A, a Grove connector and Bluetooth. It can join your network over Ethernet or Wi-Fi and take power from USB-C or Power over Ethernet. PoE carries both data and power over one Ethernet cable. It launched worldwide at €59 or $69.

For most households, the important point is that AUX-2 is not another Home Assistant controller. It is a multi-purpose bridge: an old amplifier can play audio from Music Assistant, a serial port can control a supported television, climate system or inverter, and USB can place a Connect ZWA-2 adapter in a better part of the home. AUX-2 can also work as a Bluetooth proxy. The connected device still needs a suitable integration and may require a specific cable.

The manufacturer says networking a Connect ZWA-2 has been tested. Using Connect ZBT-2 for Zigbee is still presented as something to test, while Thread does not work reliably this way. That distinction matters: some uses are ready for everyday deployment, while others remain experimental.

## Core 2026.11.2 focuses on practical fixes

Home Assistant Core 2026.11.2 arrived on 16 November. It is a maintenance release rather than a feature update. Fixes include an MQTT reload loop caused by a duplicate unique ID on a disabled entity, playback from Reolink NVRs and Hubs, diagnostics for older FRITZ!Repeaters, and LG webOS TVs becoming unavailable when their connection resets.

For UniFi Network, the update fixes the options flow when the integration is not loaded. The official changelog does not show a new UniFi Protect feature for this period. Nor did the AI integrations receive a separate weekly update: the OpenAI and Gemini changes belonged to the main 2026.11 release, outside this roundup’s date range.

## Shelly 2.2.1 quickly corrects an identity problem

Shelly released firmware 2.2.0 for Gen2 and newer devices on 11 November. Among its additions are user-configuration backups, a power-restore delay and commands for changing several switches at once. Devices with limited flash storage may perform the update in two stages with several restarts.

Version 2.2.1 followed two days later. It restores the correct device ID on Shelly 1PM Mini Gen3 and Gen4 models, after 2.2.0 changed it accidentally. If you reconfigured Home Assistant, MQTT or a password around the temporary ID, you may need to point that configuration back to the original identifier after updating. The release also fixes a crash on Shelly 2PM Gen4, restores Bluetooth relay functionality on Pro 3EM and restores the missing home page on the RGBCCT Bulb Gen3 web interface.

## What did not change this week

No new Works with Home Assistant partner or stable Home Assistant OS release appeared during the completed seven-day period. ESPHome 2026.11.0 was published on 18 November, so it belongs in the next roundup. These findings are based on documentation and release notes; we did not test the changes on physical devices.

## Sources

- [Home Assistant – Connect AUX-2 announcement](https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/)
- [Home Assistant – Connect AUX-2](https://www.home-assistant.io/connect/aux-2/)
- [Home Assistant – full Core 2026.11.2 changelog](https://www.home-assistant.io/changelogs/core-2026.11/)
- [Home Assistant Core 2026.11.2 on GitHub](https://github.com/home-assistant/core/releases/tag/2026.11.2)
- [Shelly – Gen2+ firmware changelog](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – UniFi Network integration](https://www.home-assistant.io/integrations/unifi/)
- [Home Assistant – Works with Home Assistant announcements](https://www.home-assistant.io/blog/categories/works-with-home-assistant)
- [Home Assistant OS releases](https://github.com/home-assistant/operating-system/releases)
- [ESPHome 2026.11.0 release](https://esphome.io/changelog/2026.11.0/)
