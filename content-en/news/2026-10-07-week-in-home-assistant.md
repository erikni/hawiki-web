---
title: "Week in Home Assistant: October Beta and New Cloud Name"
description: "A roundup from September 30 to October 6, 2026: upcoming changes to Home Assistant, integrations, hardware, and the status of ESPHome."
cas: "4 minutes"
obtiznost: "Overview"
kontrola_zdroju: "2026-10-07"
stav: "Verified by official sources"
temata: [Home Assistant, News, Integrations, Hardware, ESPHome]
obrazek: "/assets/images/novinky-2026-10-07.png"
obrazek_alt: "Illustration of a smart home connected to a map, sensor, and remote access"
translationKey: "news.2026-10-07-week-in-home-assistant"
---
## A Week in Preparation

What happened around Home Assistant from September 30 to October 6, 2026? The focus was on preparations for the October release and the announcement of the new name for the Home Assistant Cloud service. For hardware and ESPHome, we separate the new news from older reports so that the roundup doesn't give the impression that everything mentioned was released this week.

## Home Assistant 2026.10: Beta for now

The 2026.10.0b0 release is available on GitHub. The official October release notes, as of the end of this roundup, still carry the Beta designation and warn that they may change. Therefore, treat the following points as a preview of upcoming features.

The notes feature a reworked map: sharper display when zooming, clearer labels for people and zones, and a unified overview of people, devices, and zones. The updated profile groups appearance, language, and security settings. The goal of these changes is to simplify daily navigation.

## Integrations and Devices: What to watch for

The October notes mention the expansion of Matter support to control sound and light alarms for supported water leak sensors. For Philips Hue, they list control over MotionAware zones and scene selection. These are software device support changes, not announcements of new sensors or light bulbs.

Before purchasing, it is advisable to verify the exact model and the required Home Assistant version. The mere presence of a brand in the integrations list does not indicate which features your device will offer. Furthermore, with a beta, be prepared for the final scope of support to change.

## Cloud gets the name Home Assistant Link

Nabu Casa announced on October 2nd that the Home Assistant Cloud service is being renamed to **Home Assistant Link**. According to the provider's announcement, the change in Home Assistant will take place on December 2, 2026, with version 2026.12. Subscribers do not need to configure anything due to the name change; it is the same subscription.

The new name is better suited to capture the connection between the home installation and optional online services. Home Assistant still runs at home. Link is not a move of the entire installation to a remote server, and the subscription is not a prerequisite for using Home Assistant. This core point is explained identically in the Home Assistant and Nabu Casa announcements.

## ESPHome: Let's not confuse the news date

The official ESPHome website shows version 2026.9.1. This was released on September 29, meaning it was just before the week covered. The September series brought work on faster compiling and encrypted wireless updates; it is not a new October release.

For home sensors, it is practical to track the ESPHome version and the Home Assistant version separately. Updating one application does not automatically flash the firmware of all sensors. New features from the upcoming HA notes may also not be available in the current firmware. Therefore, we do not present this in the roundup as a ready-to-use guide.

## What to use at home

If your home is running reliably, there is no need to install the beta just for the novelty. Review the notes for the stable version when it becomes available, and prepare a backup before updating. Regarding the Link name, for now, it is enough to know that it is an announced December change. Choose hardware based on specific needs and documented support, not based on the number of new features in the week.

## Sources

- [Home Assistant 2026.10 – beta notes](https://rc.home-assistant.io/blog/2026/09/30/release-202610/)
- [Home Assistant Core 2026.10.0b0 on GitHub](https://github.com/home-assistant/core/releases/tag/2026.10.0b0)
- [Home Assistant – Home Assistant Link announcement](https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours)
- [Nabu Casa – Cloud becomes Link](https://www.nabucasa.com/news/2026-10-02-cloud-becomes-link/)
- [ESPHome 2026.9 – overview and patch release](https://esphome.io/blog/2026/09/16/esphome-2026-9/)
- [ESPHome – changelog 2026.9](https://esphome.io/changelog/2026.9.0/)
