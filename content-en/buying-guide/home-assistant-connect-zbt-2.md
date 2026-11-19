---
title: "Home Assistant Connect ZBT-2: Zigbee or Thread?"
description: "What the official ZBT-2 USB adapter can do and how to decide between Zigbee and Thread before buying."
cas: "5 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - ZBT-2
  - Zigbee
  - Thread
  - Matter
  - hardware
translationKey: "buying-guide.home-assistant-connect-zbt-2"
---

Do you want to connect Zigbee sensors and lights directly to Home Assistant, or are you building a Thread network? The **Home Assistant Connect ZBT-2** is the official USB adapter for both purposes. It supplements a computer running Home Assistant; the system does not operate itself. Before purchasing, decide which devices it needs to control.

## One Radio, One Choice

The ZBT-2 supports **Zigbee 3.0 or Thread**, but not both protocols simultaneously. If you want your own Zigbee network and your own Thread radio, you need two separate radios. However, for Thread, you can also use a suitable border router that you already own.

For Zigbee, the ZBT-2 can be used as a coordinator with the **ZHA** integration. Home Assistant documentation recommends it for a new Zigbee network. The [Home Assistant Green](/buying-guide/home-assistant-green/) does not have a built-in Zigbee radio, so this adapter provides the necessary connection.

In Thread mode, the adapter, along with the appropriate Home Assistant software, serves as part of a **Thread border router**, which connects the Thread network to your home network. For this setup, plan to configure the OpenThread Border Router application according to the manufacturer's instructions.

## Where Matter Fits In

Thread provides the network connection, while **Matter** determines how the devices are controlled. Therefore, the Matter label on the box alone does not mean you need the ZBT-2. Matter devices over Wi-Fi use your home network; Matter over Thread requires a Thread border router. To control Matter devices in Home Assistant, you also set up the Matter integration.

If you already have a functional Thread border router, first verify if you can use its network. Buying another radio may not be necessary. For a specific product, check whether it actually uses Zigbee, Matter over Thread, or Matter over Wi-Fi.

## What You Get and Where to Place the Adapter

The ZBT-2 uses the **Silicon Labs MG24** radio chip and connects via USB-C. The assembled device measures 83 × 83 × 179 mm and weighs 157 g. The package includes the base, an antenna, and a 1.5-meter USB-C cable. It is intended for indoor use.

The adapter is significantly larger than a small USB dongle. Allocate it a space of approximately 18 cm in height and use the cable for proper placement. Range depends on walls, surrounding interference, and device placement. Newer chips or larger antennas do not guarantee full home coverage on their own.

The official hardware is designed by Nabu Casa, a company based in the USA. The company's headquarters is not the country of manufacture for a specific unit. According to the manufacturer, the purchase supports the development of Open Home Foundation projects.

## What to Check Before Buying

Verify a free USB port and access to it from your Home Assistant installation. For a virtual machine, the USB device must be passed through to its environment. For beginners, it is easiest to follow the current guide for Home Assistant OS and the chosen protocol.

When switching from an older adapter, first create a backup and read the migration procedure for your integration. Do not remove the original network just because you connected a new radio. If you already have a ZBT-1 and everything works, its support in ZHA continues; replacement is not automatically necessary.

**The ZBT-2 is suitable for starting with Zigbee or for a dedicated Thread connection.** It does not connect Z-Wave devices; the [Home Assistant Connect ZWA-2](/buying-guide/home-assistant-connect-zwa-2/) is intended for that. You can find the current price and retailers on the official product page. The actual setup is governed by the guide and documentation for the chosen mode; this buying guide YAML is not required.

## Sources

- [Home Assistant: Connect ZBT-2 and specifications](https://www.home-assistant.io/connect/zbt-2/)
- [Home Assistant: ZHA, compatible adapters and migration](https://www.home-assistant.io/integrations/zha/)
- [Home Assistant: Thread and border routers](https://www.home-assistant.io/integrations/thread/)
- [Home Assistant: Matter](https://www.home-assistant.io/integrations/matter/)
- [Nabu Casa: Connect ZBT-2 support](https://support.nabucasa.com/hc/en-us/categories/29400540866973)
- [Nabu Casa: provider information](https://www.nabucasa.com/privacy/)

