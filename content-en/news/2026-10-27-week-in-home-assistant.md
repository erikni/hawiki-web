---
title: 'Week in Home Assistant: UniFi Access fixes and new ESPHome'
description: 'Overview for 20–26 October 2026: Core 2026.10.3 and 2026.10.4, ESPHome 2026.10, HAOS 18.4.rc2 and status of Shelly, AI and Works with HA.'
cas: 4 minutes
obtiznost: Overview
kontrola_zdroju: '2026-10-27'
stav: Verified against official sources
temata:
- Home Assistant
- News
- ESPHome
- UniFi
- Shelly
- AI
- Hardware
obrazek: /assets/images/novinky-2026-10-27.png
obrazek_alt: Illustration of a smart home with a custom sensor board, access reader, and speaker
translationKey: "news.2026-10-27-week-in-home-assistant"
---

## Two Core Fixes and New ESPHome

The overview for 20–26 October 2026 follows [last week](/news/2026-10-21-week-in-home-assistant/). This period overlaps by one day; we will not repeat the already described HAOS 18.4.rc1. The main news includes two fixed versions of Home Assistant, a fix for UniFi Access events, and October ESPHome for custom devices.

## Core 2026.10.3 and 2026.10.4

Version 2026.10.3 was released on October 23. Alongside other fixes, it addresses Proxmox VE update version detection and the situation where the Home Connect event listener stopped working due to an access token refresh error. For users of these integrations, the update may therefore be more significant than the version number itself.

A day later, 2026.10.4 followed. It increases the allowed size of client HTTP headers and updates the library for Lutron Caséta. The first change, for example, resolves firmware downloading via GitHub redirects: an overly long header could stop the download. This is not new hardware or a new integration, but a fix for file transfer.

## UniFi Access: one event instead of two

A specific fix for UniFi is included in 2026.10.3 and concerns **UniFi Access**, the door access system. The controller could send the same event with two different messages, and the integration processed both separately. The result was, for example, two entries in the history or two notifications after one face recognition.

The fix removes this duplication. It does not mean an expansion of UniFi Protect camera support or a change to UniFi Network. If you use automations reacting to access events, this difference is practically important.

## ESPHome 2026.10: Minor update and audio notes

ESPHome 2026.10.0 was released on October 21. It expands compressed over-the-air (OTA) updates to additional supported platforms; according to the authors, this transmits approximately one-third less data. Older firmware will now update using the previous method for the first time. The ESP8266 also transitions to new default build tools.

Before updating your speakers, check for configuration changes. Sendspin devices now require an encrypted connection, and Music Assistant requires at least 2.10.7 or 2.11.0b4; therefore, update Music Assistant first. For lights with a configured initial state, verify the behavior after a restart: the setting is now genuinely respected.

## HAOS: Another Candidate Fixes Bluetooth

On October 23, **Home Assistant OS 18.4.rc2** arrived. It adds a security update and a fix for malfunctioning Bluetooth adapters RTL8761B with identifier 0bda:a728 following a kernel change. This is still a pre-release version, not the stable HAOS 18.4. This adapter support report is not an announcement of a new physical product.

## Shelly, AI and Works with HA

In the controlled changelog, the latest stable item remains 2.1.0 from October 14; we covered the cloud NILM previously. Further changes are in the Unreleased section marked 2.2.0-beta1, so we do not attribute a new stable version this week.

In the Core releases 2026.10.3 and 2026.10.4, we found no separate new AI integration features or announcements of new integrations. MCP changes and previous Gemini fixes belong to older overviews. New ESPHome components are also not the same as new Core integrations.

On the main HA blog and in the Works with Home Assistant announcements, the last report regarding the partner LEDVANCE remains from October 13. We have no record of new partnerships or new HA proprietary hardware this week in these sources. Before updating your home, prepare a backup and review the changes that affect your devices.

## Sources

- [Home Assistant Core 2026.10.3](https://github.com/home-assistant/core/releases/tag/2026.10.3)
- [Home Assistant Core 2026.10.4](https://github.com/home-assistant/core/releases/tag/2026.10.4)
- [Home Assistant October notes and patch release](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [UniFi Access – fix duplicate events](https://github.com/home-assistant/core/pull/185160)
- [UniFi Access – integration documentation](https://www.home-assistant.io/integrations/unifi_access/)
- [Fix HTTP header limit](https://github.com/home-assistant/core/pull/188329)
- [ESPHome 2026.10 – overview of changes and limitations](https://esphome.io/blog/2026/10/21/esphome-2026-10/)
- [ESPHome 2026.10.0 – release on GitHub](https://github.com/esphome/esphome/releases/tag/2026.10.0)
- [ESPHome – Over-The-Air (OTA) updates](https://esphome.io/components/ota/esphome/)
- [ESPHome – Sendspin](https://esphome.io/components/sendspin/)
- [Home Assistant OS 18.4.rc2](https://github.com/home-assistant/operating-system/releases/tag/18.4.rc2)
- [HAOS – fix RTL8761B adapter](https://github.com/home-assistant/operating-system/pull/5112)
- [Shelly – firmware changelog](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – integration catalog](https://www.home-assistant.io/integrations/)
- [Home Assistant – main blog](https://www.home-assistant.io/blog/)
- [Works with Home Assistant – partner announcements](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
