---
title: "How to install Home Assistant"
seoTitle: "How to install Home Assistant: Green, Raspberry Pi and mini PC"
description: "Choose an installation method that suits your experience and equipment: Green, Raspberry Pi, mini PC, virtual machine or Container."
cas: "5-minute read"
obtiznost: "Beginner"
kontrola_zdroju: "2026-10-08"
stav: "Based on documentation"
sourceType: "official-docs"
translationKey: "getting-started.installing-home-assistant"
temata: ["Home Assistant", "Installation", "Hardware"]
obrazek: "/assets/images/instalace-home-assistant.png"
obrazek_alt: "Illustration of a home and a choice between a ready-made controller, a single-board computer and a mini PC."
related: ["getting-started/first-start", "getting-started/what-you-will-need"]
---

## First choose how you want to manage it

Home Assistant needs a device that remains powered on in your home. For most users, the documentation recommends **Home Assistant OS**. It manages the system and lets you install add-on applications. **Home Assistant Container** is intended for people who manage their own operating system and containers. They are not different home-control platforms, but different ways to install and maintain the same platform.

Before buying anything, read [what you will need](/getting-started/what-you-will-need/) and [how to choose hardware](/buying-guide/how-to-choose/). This article will help you decide; the linked documentation provides the detailed installation steps.

## Home Assistant Green: the least preparation

This is for beginners who want a ready-made solution. Home Assistant OS is pre-installed: connect the network and power, then complete the initial setup. The advantage is an easy start; the disadvantage is the cost of a separate controller. Difficulty is low. Our recommendation is to choose [Home Assistant Green](/buying-guide/home-assistant-green/) if you mainly want to use your smart home rather than maintain a computer. Continue with the [first start on Green](/getting-started/first-start/).

## Raspberry Pi: build your own system

This suits people who already own a Pi or want to assemble the system themselves. Its small size is an advantage. You will need to provide suitable power and storage and write the Home Assistant OS image yourself. The documentation covers Raspberry Pi 4 and 5. Difficulty is moderate. Before buying, compare the cost of the complete system rather than the board alone, and follow the current Raspberry Pi installation guide.

## Mini PC or x86: a dedicated computer

This option suits a home with a compatible computer that can be dedicated to Home Assistant. You can choose the hardware and storage, but preparing the system takes more work. Installing the OS on a selected drive will overwrite its contents. Difficulty is moderate to high; check x86-64 support and the UEFI configuration. Use a computer that you can dedicate to this purpose and back up any data you need first.

## Virtual machine or Proxmox

This is for people who already operate a virtualisation server. It makes use of an existing host, but your smart home then depends on that host and its maintenance. Home Assistant OS runs inside a virtual machine. Difficulty is higher because you must manage networking, storage and, where required, USB radio passthrough. Proxmox is one possible virtualisation platform; this is not a guide to installing it. Choose this route only if you are comfortable maintaining the environment.

## Home Assistant Container

This option is for more experienced Linux and Docker users. You control the environment, but must handle updates and related services yourself. Home Assistant Container does not include the add-on system built into Home Assistant OS. Difficulty is higher. Choose it if you already use containers; for a first smart home, Home Assistant OS is usually easier to understand.

## After installation

Add your [phone](/getting-started/home-assistant-mobile-app/) and configure [backups](/help/backups/). Check one device before creating your first automation.

## Sources

- [Home Assistant – Installation](https://www.home-assistant.io/installation/)
- [Home Assistant – Raspberry Pi](https://www.home-assistant.io/installation/raspberrypi/)
- [Raspberry Pi – Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [Home Assistant – Generic x86-64](https://www.home-assistant.io/installation/generic-x86-64/)
- [Home Assistant – Alternative installations](https://www.home-assistant.io/installation/alternative/)
