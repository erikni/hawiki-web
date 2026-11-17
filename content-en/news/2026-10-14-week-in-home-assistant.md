---
title: 'Week in Home Assistant: Tesla via BLE, Shelly and Easier AI Integration'
description: 'News from October 7–13, 2026: Home Assistant 2026.10 and 2026.10.1, Tesla via BLE, Shelly, UniFi Protect, AI, and certified lighting.'
cas: 4 minutes
obtiznost: Overview
kontrola_zdroju: '2026-10-14'
stav: Verified by official sources
temata:
- Home Assistant
- News
- Tesla
- Shelly
- UniFi
- AI
- Matter
obrazek: /assets/images/novinky-2026-10-14.png
obrazek_alt: Illustration of a smart home with lighting, a map, and connected automation triggers
translationKey: "news.2026-10-14-week-in-home-assistant"
---

## From Beta to Stable Version

The week of October 7 to 13, 2026, brought stable Home Assistant 2026.10 and the first patch release 2026.10.1. Following [the previous overview](/news/2026-10-07-week-in-home-assistant/): alongside maps and automations are local commands for Tesla, changes to Shelly and UniFi, and simpler AI connectivity.

## Map and automation

Version 2026.10 was released on October 7. The vector map remains sharp when zooming and provides an overview of people, devices, and zones. In the automation editor, you can directly check the relevant triggers in the trigger condition; Home Assistant will provide their IDs. Manually entered IDs in YAML still work.

## Tesla via BLE: available since 2026.10

The **Teslemetry** integration can now send commands to a supported Tesla vehicle locally via Bluetooth Low Energy. This feature has been part of version 2026.10, so it is available in 2026.10.1; it was not added with a patch update.

You need an account with an active Teslemetry subscription, a Bluetooth adapter or proxy available to Home Assistant, and the vehicle within range. Local control must be enabled for each vehicle separately and requires pairing the key with the car. The vehicle must support the Tesla Vehicle Command protocol; some older Model S and X units do not. If Bluetooth is unavailable, the integration can switch to the cloud. Therefore, this is not a new, separate Tesla BLE integration, nor is it a cancellation of the subscription.

## Shelly: head unit and camera

In version 2026.10, the option became available to connect the **Shelly BLU TRV** even through supported devices other than the BLU Gateway. This does not mean that the head unit mediates any arbitrary Bluetooth device. The Shelly Camera received a free space sensor in storage, and snapshots are loaded via the moment interface. The corrected version 2026.10.1 adjusts the reporting of the last direction of movement for uncalibrated Shelly blinds. This fix is not a replacement for calibration.

## UniFi Protect: More options via API key

Version 2026.10 expanded the connection mode using only an API key to include additional switches, sensors, events, and sirens. For some functions, a local user account is therefore not required. However, the scope is limited to the public API; full access and key-only mode are not equivalent. Before switching, verify the required functions in the documentation. This specifically concerns **UniFi Protect**, not a sweeping change to all UniFi integrations.

## AI: Simplified connection via MCP

In Settings → System, you will find the **AI** page with the Model Context Protocol server card. The server can be enabled directly, and the address can be copied for the supported AI application. MCP allows the application to communicate with Home Assistant; it is not a new voice model itself.

In the new setup, all offered Home Assistant tools are accessible, and only administrators can connect. The scope and limitations of accounts can be changed. Therefore, before connecting, check what you are allowing the application to use.

## LEDVANCE and initial fixes

On October 13, the brand LEDVANCE, with 116 certified devices, was added to the Works with Home Assistant program. The announced range uses Matter over Wi-Fi and local control. For these devices, you do not need a Thread border router, but you do need a configured Matter integration. Before purchasing, verify the exact model in the certification list.

Version 2026.10.1 from October 10 also brought fixes for Hue lights and logging of automation history. Before updating, prepare a backup and review the changes to your integrations. ESPHome still reports stable version 2026.9.1 during checks; updating Home Assistant itself will not reflash the sensor firmware.

## Sources

- [Home Assistant 2026.10 – stable release and patch version](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [Home Assistant Core 2026.10.1 – list of fixes on GitHub](https://github.com/home-assistant/core/releases/tag/2026.10.1)
- [Automation trigger documentation](https://www.home-assistant.io/docs/automation/trigger/)
- [LEDVANCE joins Works with Home Assistant](https://www.home-assistant.io/blog/2026/10/13/ledvance-joins-works-with-home-assistant/)
- [List of certified LEDVANCE / OSRAM devices](https://works-with.home-assistant.io/certified-products/?brand=ledvance-osram)
- [Matter integration documentation](https://www.home-assistant.io/integrations/matter/)
- [ESPHome – changelog](https://esphome.io/changelog/)
- [Full list of changes Home Assistant 2026.10 and 2026.10.1](https://www.home-assistant.io/changelogs/core-2026.10/)
- [Teslemetry – prerequisites and Bluetooth control](https://www.home-assistant.io/integrations/teslemetry/)
- [Adding Bluetooth commands to Teslemetry](https://github.com/home-assistant/core/pull/176296)
- [Shelly BLU TRV – expanded connection support](https://github.com/home-assistant/core/pull/182422)
- [UniFi Protect – connection modes and their limitations](https://www.home-assistant.io/integrations/unifiprotect/)
- [Model Context Protocol server documentation](https://www.home-assistant.io/integrations/mcp_server/)
