---
title: 'Week in Home Assistant: Gemini fixes and new Shelly firmware'
description: 'Overview for 14–20 October 2026: Home Assistant 2026.10.2, AI and voice, Shelly 2.1.0, UniFi status, integrations and Works with Home Assistant.'
cas: 4 minutes
obtiznost: Overview
kontrola_zdroju: '2026-10-21'
stav: Verified by official sources
temata:
- Home Assistant
- News
- Shelly
- UniFi
- AI
- Integrations
- Hardware
obrazek: /assets/images/novinky-2026-10-21.png
obrazek_alt: Illustration of a smart home with an electricity meter, network camera, and voice assistant symbol
translationKey: "news.2026-10-21-week-in-home-assistant"
---

## Week of fixes and consumption monitoring

From October 14 to 20, 2026, the maintenance release Home Assistant 2026.10.2 and Shelly firmware 2.1.0 arrived. For AI, there are significant fixes for Gemini and voice output. We follow up on [previous overview](/news/2026-10-14-week-in-home-assistant/).

## Home Assistant 2026.10.2

The second October maintenance release was released on October 16. It fixes, for example, the double triggering of MQTT device and attribute triggers after reloading the configuration. Tesla Fleet received a fix for an unexpected heating level error. Tesla Fleet and Teslemetry diagnostics now hide coordinates from schedules.

Before updating, prepare a backup and review the changes to your integrations.

On October 20, **Home Assistant OS 18.4.rc1** was also available, which is a pre-release version. It fixes, for example, VLAN on Realtek adapters and issues with startup or USB storage. RC is not a stable update for a typical home setup.

## AI: Gemini has more reliable voice output

Version 2026.10.2 adjusts requirement parameters according to the capabilities of individual Gemini model families. It also fixes the processing of finished audio responses in WAV format. Previously, the converter expecting a different format might reject it, even though Google created the audio. For a home with a voice assistant, this is a specific fix for text-to-speech conversion, not an announcement of new voice hardware.

We described connecting AI via MCP previously, and we are not presenting it again as a new feature this week. Gemini still requires an API key; home control depends on which entities you grant it access to.

## Shelly 2.1.0: Manufacturer update, not new HA entity

Shelly dated firmware 2.1.0 to October 14. For devices with power and energy measurement, it lists support for **Shelly Cloud NILM services**. NILM is an acronym for Non-Intrusive Load Monitoring, which analyzes electrical load without individually measuring every appliance. However, the changelog does not describe the details of the results or their availability in Home Assistant.

Therefore, the announcement does not mean that HA will automatically recognize individual appliances after an update. The Shelly integration communicates with devices locally; the manufacturer's cloud service is a different layer. Verify the firmware availability for your exact model, as not all Shelly devices receive the same updates. LoRa, the new web interface, and other changes listed in the Unreleased section are not yet part of the stable 2.1.0.

## UniFi: no documented new HA features this week

The 2026.10.2 release list does not include standalone changes for UniFi Network or UniFi Protect. The expansion of Protect mode using an API key was covered in 2026.10 and was featured in a previous overview. It still has limited scope compared to full access. A new version of the Ubiquiti application or camera itself does not document a new feature in HA; the support for a specific device and its public API determines this.

## Integrations, hardware, and Works with HA

The maintenance release 2026.10.2 does not announce any new integrations. The integrations catalog is used to verify support; the mere presence of an item does not indicate when it was added. We also did not find any announcements of new proprietary HA hardware on the main blog for the monitored week.

The last announced partner for Works with Home Assistant remains LEDVANCE from October 13, meaning from the previous week. We do not have any new partnerships documented in the program overview for October 14–20. When selecting devices, verify the certification of the exact model.

## New Home for Contributors

Next to the main blog is an announcement from October 16th on the new portal contributors.home-assistant.io. It collects guides for development, translations, documentation, and testing. You can also get involved by correcting Czech text or improving the clarity of guides.

## Sources

- [Home Assistant Core 2026.10.2 – release and fixes](https://github.com/home-assistant/core/releases/tag/2026.10.2)
- [Home Assistant 2026.10 – release notes and patch release](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [Gemini – fix for parameters and WAV responses](https://github.com/home-assistant/core/pull/185723)
- [Google Gemini – integration documentation](https://www.home-assistant.io/integrations/google_generative_ai_conversation/)
- [Shelly – firmware 2.1.0 and planned changes](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Shelly – integration documentation](https://www.home-assistant.io/integrations/shelly/)
- [UniFi Protect – modes and connection limitations](https://www.home-assistant.io/integrations/unifiprotect/)
- [Home Assistant integration catalog](https://www.home-assistant.io/integrations/)
- [Home Assistant – main blog](https://www.home-assistant.io/blog/)
- [Works with Home Assistant – partner announcements](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
- [Works with Home Assistant – program terms](https://works-with.home-assistant.io/)
- [New portal for Home Assistant contributors](https://contributors.home-assistant.io/blog/2026/10/16/a-new-home-for-every-contributor/)
- [Home Assistant OS 18.4.rc1 – pre-release](https://github.com/home-assistant/operating-system/releases/tag/18.4.rc1)
