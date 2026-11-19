---
title: "Home Assistant Connect AUX-2: Vintage Audio in a Smart Home"
seoTitle: "Connect AUX-2: Audio, RS-232 and PoE for Home Assistant"
description: "What the Home Assistant Connect AUX-2 can do, how it connects older audio and serial equipment, and what to check before buying."
obrazek: "/assets/images/home-assistant-connect-aux-2.png"
obrazek_alt: "Illustration of the AUX-2 connected to a home router via an RJ45 cable and to active speakers via a 3.5mm output."
cas: "6 minutes read"
obtiznost: "Next step"
kontrola_zdroju: "2026-11-13"
stav: "Based on documentation"
temata:
  - "Connect AUX-2"
  - "Music Assistant"
  - "RS-232"
  - "PoE"
  - "hardware"
translationKey: "buying-guide.home-assistant-connect-aux-2"
---

**Home Assistant Connect AUX-2** is a small box from Nabu Casa designed to connect older equipment to Home Assistant. It can stream music to a receiver or active speakers, control supported devices via a serial link, and function as a network hub for selected USB adapters. It is not a new Home Assistant nor an amplifier: it requires a running Home Assistant 2026.9 or newer.

## Music for Older Receivers or Active Speakers

The AUX-2 integrates into Home Assistant via the ESPHome integration. It receives music over the home network using the open Sendspin protocol; a practical source is the free **Music Assistant**. This can stream local files and supported streaming services, and group the AUX-2 with other compatible players.

The combined 3.5mm output offers either analogue audio or optical S/PDIF, but only one method at a time. It supports stereo up to 24 bit / 48 kHz and FLAC, MP3, and WAV formats. The device only has an **audio output**: it does not record sound from a turntable or CD into Home Assistant, nor does it transmit Bluetooth audio, and it cannot power passive speakers. These require their own amplifier.

## Two RS-232 Ports and Other Options

The two 3.5mm RS-232 ports can control, for example, a compatible TV, AV receiver, projector, UPS, or regulator. However, the connector itself does not guarantee support: an integration must exist in Home Assistant that can handle the serial proxy of the AUX-2. For different devices, you will need the correct cable, such as 3.5mm–DB9. The switches on the bottom allow swapping the TX and RX wires.

The serial ports must not be confused with the audio output. They carry a ±5 V signal and can damage audio equipment. RS-485 requires a separate supported USB adapter. USB-A can only be used simultaneously for one purpose: an RS-485 adapter, Connect ZWA-2, or experimentally, Connect ZBT-2. Zigbee via ZBT-2 only works with ZHA and Home Assistant 2026.11+, and is not widely tested. Thread is not supported.

The AUX-2 also functions as a Bluetooth proxy for BLE devices; however, it is not a Bluetooth speaker. The Grove port allows advanced users to add supported inputs or outputs via ESPHome.

## Network, Power, and Box Contents

The cleanest connection is offered by Ethernet with **PoE 802.3af**, which transmits both data and power over a single cable. Alternatively, you can use Ethernet or 2.4GHz Wi-Fi and a 5 V / 2 A USB-C power supply. The manufacturer recommends the wired connection as the most reliable. The device measures 106 × 63 × 25 mm and weighs 104 g.

The box contains the AUX-2, a brief manual, and safety information. The power supply, Ethernet, audio, or serial cables must be chosen according to the setup and purchased separately. Therefore, before ordering, check the amplifier input, serial connector, and compatible integration.

## Is it worth buying?

The AUX-2 makes sense if you want to keep high-quality vintage receivers or active speakers, locally control devices with supported RS-232, or move a Z-Wave adapter to a more suitable location in the network. For simple streaming to a modern network speaker or for devices without serial integration, it might be unnecessarily universal.

In the Czech Republic, Alza.cz offered it for pre-order on 13 November 2026. Availability and price may change, so check the current product page before purchasing. For Zigbee, also compare the separate [Connect ZBT-2](/buying-guide/home-assistant-connect-zbt-2/) and for Z-Wave [Connect ZWA-2](/buying-guide/home-assistant-connect-zwa-2/).

## Sources

- [Home Assistant: Connect AUX-2](https://www.home-assistant.io/connect/aux-2/)
- [Nabu Casa: What is Connect AUX-2 and how does it work](https://support.nabucasa.com/hc/en-us/articles/40528879660317-What-Connect-AUX-2-is-and-how-it-works)
- [Nabu Casa: Set up Home Assistant Connect AUX-2](https://support.nabucasa.com/hc/en-us/articles/40527754954653-Set-up-Home-Assistant-Connect-AUX-2)
- [ESPHome Devices: Home Assistant Connect AUX-2](https://devices.esphome.io/devices/home-assistant-connect-aux-2/)
- [Root.cz: Connect AUX-2](https://www.root.cz/clanky/home-assistant-connect-aux-2-novy-hardware-pro-streamovani-hudby-a-seriove-ovladani/)
- [Alza.cz: Home Assistant Connect AUX-2](https://www.alza.cz/home-assistant-connect-aux-2-d13674192.htm)

