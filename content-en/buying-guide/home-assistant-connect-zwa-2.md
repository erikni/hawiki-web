---
title: "Home Assistant Connect ZWA-2: When Does It Make Sense?"
description: "The official Z-Wave adapter for Home Assistant: what it does, what you need, and what to check before buying."
cas: "5 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - ZWA-2
  - Z-Wave
  - Z-Wave Long Range
  - hardware
translationKey: "buying-guide.home-assistant-connect-zwa-2"
---

Do you want to connect Z-Wave sensors, sockets, or switches to Home Assistant? The **Home Assistant Connect ZWA-2** is the official USB adapter that adds Z-Wave radio capability to a computer running Home Assistant. It does not replace the [Home Assistant Green](/buying-guide/home-assistant-green/) or any other computer on which the system runs. It makes sense if you want to start with Z-Wave or are considering replacing an existing adapter.

## What You Are Buying

The ZWA-2 uses a Z-Wave Series 800 chip and supports both standard Z-Wave and **Z-Wave Long Range**. It connects to the computer via USB; the base features a USB-C connector. The box includes an antenna, a base, and a 1.5-metre cable.

The dimensions of the assembled device are 125 × 125 × 315 mm. Therefore, when buying, account for space for the base and an antenna approximately 32 cm high. It is intended for indoor use only.

The official hardware is designed by Nabu Casa, a company based in the USA. The company's headquarters is not the country of manufacture for the specific unit. Purchasing from the manufacturer supports the development of the Open Home Foundation projects.

## Standard Z-Wave vs. Long Range

Classic Z-Wave can use a network where messages are relayed by other devices. Long Range uses a direct connection between the end device and the adapter, forming a star topology. The ZWA-2 handles both types of networks simultaneously.

**Long Range must support a sensor or other connected product.** Older devices cannot become Long Range devices simply by replacing the adapter. The advantage is the ability to continue using standard Z-Wave products while gradually adding new ones.

## What to Verify Before Ordering

The most important factor is the region. Z-Wave uses different frequencies in different parts of the world. For a household in the Czech Republic, choose end devices designated for the European region. An American sensor is not a suitable replacement just because it is cheaper. You generally cannot change the frequency on end devices.

Also, check for available USB ports and the method of connecting the adapter to your Home Assistant installation. For a virtual machine, you need to pass the USB device through to its environment. Home Assistant uses the Z-Wave integration and Z-Wave JS server for communication; setting up with Home Assistant OS is simpler thanks to the managed application.

The ZWA-2 does not connect Zigbee or Thread devices. If you are buying a sensor, check its actual protocol. For guidance, the article [Zigbee, Wi-Fi, Thread and Matter simply](/buying-guide/zigbee-wifi-thread-matter/) can help.

## Range and Initial Setup

The large antenna is designed for Z-Wave but does not guarantee specific range within your home. The result will be influenced by walls, the placement of the adapter, and the end device's antenna. Therefore, do not consider range data from manufacturer tests as a promise for your flat or garden.

After connecting, follow the Home Assistant guide, check the region, and add your first device according to its manual. To start, choose a socket or sensor whose behaviour you can easily verify. YAML is not needed for the purchase itself or for this guide.

When replacing an existing adapter, first back up your Z-Wave network and verify the migration procedure for your model. Automatic conversion is available for many modern adapters, not without conditions for every old unit.

**The ZWA-2 makes sense as an entry point into Z-Wave or a considered upgrade.** If your network is already functioning reliably, first determine what the replacement needs to solve. Check the current price and availability with a retailer from the official list on the product page.

## Sources

- [Home Assistant: Connect ZWA-2, specifications and retailers](https://www.home-assistant.io/connect/zwa-2/)
- [Home Assistant: Z-Wave integration, regions and backups](https://www.home-assistant.io/integrations/zwave_js/)
- [Z-Wave Alliance: difference between Z-Wave and Long Range](https://z-wavealliance.org/what-is-z-wave-long-range-how-does-it-differ-from-z-wave/)
- [Nabu Casa: Connect ZWA-2 support](https://support.nabucasa.com/hc/en-us/categories/28669861145885)
- [Nabu Casa: provider information](https://www.nabucasa.com/privacy/)

