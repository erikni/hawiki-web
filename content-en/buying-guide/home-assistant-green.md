---
title: "Home Assistant Green: capabilities and limitations"
seoTitle: "Home Assistant Green: hardware, capabilities, and limitations"
description: "Home Assistant Green from a hardware perspective: performance, ports, consumption, missing radios, and who should buy it."
obrazek: "/assets/images/home-assistant-green.jpg"
obrazek_alt: "Actual product photograph of the Home Assistant Green with connected Ethernet and power cables."
cas: "6 minutes' read"
obtiznost: "Beginner"
kontrola_zdroju: "2026-11-13"
stav: "Based on documentation"
temata:
  - "Home Assistant Green"
  - "Home Assistant OS"
  - "hardware"
  - "Zigbee"
  - "Matter"
translationKey: "buying-guide.home-assistant-green"
---

**Home Assistant Green** is a complete central unit with Home Assistant OS pre-installed. You connect the power and network cable, follow the guide, and you have Home Assistant on a standalone device. However, you are not buying a universal computer or a wireless hub with all radios. The Green is primarily a simple and efficient base that can be supplemented via USB as needed.

## Hardware without assembly

Inside is a quad-core Rockchip RK3566 processor with Arm Cortex-A55 cores at 1.8 GHz, 4 GB of RAM, and 32 GB of embedded eMMC storage. Both Home Assistant and data run locally. The large aluminium cooler does not require a fan, so the unit operates silently.

The Green features gigabit Ethernet and two USB 2.0 Type-A ports. Both ports together provide up to 5 V / 2 A. The manufacturer states the consumption is approximately 1.7 W at idle and 3 W under load. The enclosure measures 112 × 112 × 32 mm and weighs 340 g.

The package includes the Green, a gigabit Ethernet cable, and a universal 12 V / 1 A power supply with plugs for the EU, USA, and Great Britain. Therefore, for standard setup, you do not need to purchase power or a cable for your router.

## What it can do

The Green runs a full, managed installation of Home Assistant OS, including updates, backups, and add-on applications. It connects to devices available on the home network and supported cloud services. It can locally control automations and store history; the availability of specific products always depends on their integration and communication method.

Matter devices via Wi-Fi or Ethernet can be used after setting up the Matter and Matter Server integrations. The Green does not need its own Wi-Fi: it communicates with them via the router.

## What is not built-in

The Green connects to the home network **only via an Ethernet cable**. It does not have Wi-Fi or a built-in radio for Zigbee, Thread, or Z-Wave. Zigbee or Thread can be supplemented, for example, with [Connect ZBT-2](/buying-guide/home-assistant-connect-zbt-2/), and for Z-Wave, [Connect ZWA-2](/buying-guide/home-assistant-connect-zwa-2/) can be used. However, one ZBT-2 will not handle both Zigbee and Thread simultaneously.

The HDMI connector is intended only for diagnostics, not for regular monitor connection. The microSD slot is for system recovery, not for expanding data storage. The built-in 32 GB eMMC or 4 GB RAM cannot be easily replaced; anyone who wants to significantly expand storage or run other demanding services should consider a mini PC or another server.

## Who it is suitable for

The Green is suitable for beginners who want supported devices without the complexity of managing Linux, and also for more experienced users who want to separate Home Assistant from other computers. Its weakness is the fixed hardware and the necessity of purchasing radios for certain protocols. Additionally, connected USB adapters take up limited ports.

In the Czech Republic, it was offered by [Alza.cz](https://www.alza.cz/home-assistant-green-d7998187.htm) on 13 November 2026. Price and availability change, so please verify before ordering. Once you have selected a device, continue with the separate guide [First Boot of Home Assistant Green](/getting-started/first-start/).

## Sources

- [Home Assistant: Home Assistant Green and technical specifications](https://www.home-assistant.io/green/)
- [Home Assistant: Installing Green](https://www.home-assistant.io/installation/green/)
- [Home Assistant: Matter](https://www.home-assistant.io/integrations/matter/)
- [Alza.cz: Home Assistant Green](https://www.alza.cz/home-assistant-green-d7998187.htm)
