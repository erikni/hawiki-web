---
title: "First start with Home Assistant Green"
description: "From connecting the controller to opening the smart-home dashboard running in your home."
obrazek: "/assets/images/prvni-spusteni.png"
obrazek_alt: "Illustration of the initial setup of a home controller connected to devices inside the home."
cas: "30–60 minutes"
obtiznost: "Beginner"
kontrola_zdroju: "2026-10-06"
stav: "Based on documentation"
translationKey: "getting-started.first-start"
temata:
  - "Home Assistant Green"
  - "Getting started"
  - "Local operation"
  - "Home network"
---

## Home Assistant runs in your home

**Home Assistant on Green is a local system.** Its configuration, controls and history are stored on your device at home. Normal local operation does not require a cloud service or a Home Assistant Cloud subscription. The account you create during onboarding belongs to your own Home Assistant installation.

After setup, locally connected devices and automations can work **without an internet connection**. Green must remain powered on and your home network must be working. An internet outage is not the same as switching off the router: you still need the router and Wi-Fi to connect from a phone or computer.

The services used by your devices also matter. A device controlled only through its manufacturer's cloud may stop working without the internet. The same applies to an online weather forecast or a cloud AI model. Check for local-control support when choosing equipment.

## What you will need

You need [Home Assistant Green](/buying-guide/home-assistant-green/), its power supply, a network cable, a router and a phone or computer on the same home network. **The initial preparation also requires internet access** to download the necessary components. Internet access is also needed for updates.

Check price, availability, delivery and warranty directly with a retailer in your country. If you are still choosing your setup, read [what you will need](/getting-started/what-you-will-need/).

## Procedure

1. Connect Green to your router with a network cable.
2. Connect the power supply and allow the initial preparation to finish.
3. Open `http://homeassistant.local:8123` in a browser.
4. If that address does not work, find the device's IP address in your router and open it with `:8123` appended.
5. The wizard will guide you through creating an account and setting up your home. Store the password securely.
6. Check whether Home Assistant has discovered devices on the network. Connect only devices you recognise.

## How to tell when it is ready

You can see the initial dashboard and open Settings. Also try signing in from another device on the same network.

## If the page does not open

Check the power supply, network cable and connection to the same home network. A guest Wi-Fi network may prevent devices from communicating. During its first preparation, Green needs both time and internet access.

## What next

[Set up backups](/help/backups/), then connect your first supported device by following its documentation.

## Sources

- [Home Assistant – Installing Home Assistant Green](https://www.home-assistant.io/installation/green/)
- [Home Assistant Green](https://www.home-assistant.io/green/)
- [Home Assistant – Onboarding](https://www.home-assistant.io/getting-started/onboarding/)
- [Alza.cz – Home Assistant Green](https://www.alza.cz/home-assistant-green-d7998187.htm)
