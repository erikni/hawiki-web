---
title: "Week in Home Assistant: Marketplace, Smarter AI, and Safer HAOS"
description: "A roundup for 4–10 November 2026: Home Assistant 2026.11, built-in Marketplace, AI diagnostics, HAOS 18.5, and fixes for Shelly and UniFi."
cas: "4 minutes"
obtiznost: "Overview"
kontrola_zdroju: "2026-11-11"
stav: "Verified by official sources"
temata: [Home Assistant, News, Marketplace, AI, HAOS, Shelly, UniFi]
obrazek: "/assets/images/novinky-2026-11-11.png"
obrazek_alt: "Illustration of a smart home with a marketplace of community add-ons, diagnostics, and a secured home server update"
translationKey: "news.2026-11-11-week-in-home-assistant"
---
## The Biggest Release Brings the Marketplace

The roundup for 4–10 November 2026 follows [last week](/news/2026-11-04-week-in-home-assistant/). The main event is the stable Home Assistant 2026.11, followed by the first patch release and system security update for Raspberry Pi and Home Assistant Yellow.

Home Assistant 2026.11 was released on 4 November and integrated HACS directly into the system under the name **Marketplace**. You can find it in Settings and it works across all installation methods, including Home Assistant Container. Existing HACS installations will automatically convert upon first launch after the update: installed projects, custom repositories, and their updates will be preserved. The standalone HACS installer is no longer intended for version 2026.11.

While the installation is more convenient, it does not mean that community add-ons are officially tested. Home Assistant warns that they may access the internet or data and affect system stability. Therefore, before installing, check the author, required version, open issues, and the age of the last update.

## More Practical Automations and Dashboards

The new version can now exclude something explicitly from an automation's target. For example, you can turn off an entire floor except for the kitchen; if you later add another light in the kitchen, it will also remain excluded. Dashboards have received automatic sections that display selected types of entities, devices, areas, or tags and update continuously.

There is also increased support for saving backups and media to local drives, two-way audio for supported Matter cameras, LoRaWAN, and 38 new integrations. Due to the new naming structure, some visible names in dashboards may appear different; entity and automation IDs are not expected to change according to the announcement.

## AI Can Find Problems, But It Needs Boundaries

Compatible AI assistants can now read the system protocol via the Home Assistant LLM API, determine installation information, search for available actions, execute one of them, and list or reload an integration. Accessing logs requires an administrator account, and the LLM API must be explicitly connected to the conversational agent or MCP server by the administrator.

This is useful for troubleshooting, but it also represents a potential ability to interfere with the home. The MCP server can be limited only to read tools; therefore, only grant the AI the permissions it genuinely needs. Google Gemini TTS in this release has migrated to Gemini 3.8 Flash and added speech style control, additional voices, and languages; the OpenAI integration has added support for GPT-6.1 Terra.

## Fixes for Shelly and UniFi, HAOS 18.5 for Raspberry Pi

Core 2026.11.1 from 9.11 fixes an issue where newly added entities were not included when a sleeping Shelly RPC device woke up. It also includes an update to the `aiounifi` library to version 98; however, the release notes do not document any new functionality for UniFi Network or Protect from this item alone.

Home Assistant OS 18.5 was released on 6.11. For Raspberry Pi and Home Assistant Yellow, the core is updated to 6.18.59 due to a fix for CVE-2026-98432 in the Linux networking stack. Other platforms received the fix already in HAOS 18.4. According to the authors, no widespread exploitation was known, but they particularly recommend the update for systems exposed directly to the internet or an untrusted network.

In monitored sources, we did not find a new stable firmware version for Shelly this week; version 2.2.0 remained in the beta section. There were no new Works with Home Assistant partnerships or new proprietary Home Assistant hardware announced on the official blog.

## Sources

- [Home Assistant 2026.11 – release notes and fix 2026.11.1](https://www.home-assistant.io/blog/2026/11/04/release-202611/)
- [Home Assistant Core 2026.11.1](https://github.com/home-assistant/core/releases/tag/2026.11.1)
- [Shelly – fix for woken sleeping devices](https://github.com/home-assistant/core/pull/190447)
- [UniFi – aiounifi library update](https://github.com/home-assistant/core/pull/190145)
- [Home Assistant OS 18.5](https://github.com/home-assistant/operating-system/releases/tag/18.5)
- [Home Assistant – Shelly integration](https://www.home-assistant.io/integrations/shelly/)
- [Shelly – Gen2+ firmware changelog](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – UniFi Network integration](https://www.home-assistant.io/integrations/unifi/)
- [Home Assistant – UniFi Protect integration](https://www.home-assistant.io/integrations/unifiprotect/)
- [Works with Home Assistant – partner announcements](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
