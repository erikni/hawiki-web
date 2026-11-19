---
title: "Zigbee, Wi-Fi, Thread, and Matter Explained"
description: "Understand the labels and learn what to check before buying."
cas: "5 minutes' read"
obtiznost: "Beginner"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Zigbee"
  - "Wi-Fi"
  - "Thread"
  - "Matter"
translationKey: "buying-guide.zigbee-wifi-thread-matter"
---

## First, Choose the Function, Then the Connection

Do you want a window sensor or a smart light? On the box, you will encounter several different labels. They are not four interchangeable options: Wi-Fi, Zigbee, and Thread describe the network communication, while Matter defines the common method of control over the supported network.

For Home Assistant, therefore, verify the specific model and function you need. The network logo alone does not say whether you will be able to, for example, dim a light or read a socket outlet.

## Wi-Fi: Devices on the Home Network

Wi-Fi devices connect to the home wireless network. For Wi-Fi itself, you do not need a Zigbee coordinator or a Thread border router. However, the method of connection to Home Assistant depends on the product: it may use its own integration or Matter.

The Wi-Fi label alone does not confirm control without the internet. Before purchasing, check the integration documentation to verify whether it communicates locally or requires the manufacturer's cloud. Also, find out which functions it enables.

## Zigbee: A Dedicated Smart Home Network

For direct connection via the **ZHA** integration, Home Assistant requires a supported Zigbee coordinator, such as a suitable radio adapter. A Zigbee network can relay messages through other devices that act as repeaters. A battery-powered sensor usually does not perform this task.

ZHA supports standard types of Zigbee devices, but manufacturers may use non-standard functions. Therefore, do not automatically expect full support for every model. If the product uses its own hub, also verify the possibility of connecting that hub to Home Assistant.

## Thread: A Network That Needs a Path to the Home Network

Thread is a network designed for low-power devices and supports message relay between nodes. Connection to the rest of the home network is provided by a **Thread border router**. This function can be provided by devices you already own or suitable Home Assistant equipment.

The Thread integration itself does not replace the necessary radio hardware. And the Thread logo is not confirmation of Matter: there are also Thread devices with different control methods. Verify both labels and the manufacturer's requirements.

## Matter: A Common Control Method

Matter can run over Wi-Fi, Ethernet, or Thread. Home Assistant controls it via the Matter and Matter Server integrations. For **Matter over Thread** devices, you additionally need a Thread border router; for **Matter over Wi-Fi**, you do not need one for this device.

Control via Matter happens locally. However, the manufacturer may require its own account, for example, for initial Matter authorization. Matter does not guarantee all of the product's special functions: the proprietary integration may offer more options. Compare the available functions of both methods.

## Official Home Assistant Adapters

The [Connect ZBT-2](https://www.home-assistant.io/connect/zbt-2/) can be configured for Zigbee or for Thread; both modes cannot operate simultaneously. For Thread, it also requires border router setup.

The [Connect ZWA-2](https://www.home-assistant.io/connect/zwa-2/) is an adapter for another technology, **Z-Wave**. It does not replace a Zigbee coordinator or a Thread adapter.

## What to Check Before Buying

- The exact model and required function in the Home Assistant and manufacturer documentation.
- Whether you need a coordinator, hub, or Thread border router, and if you already have suitable equipment.
- Dependency on the internet and any potential need for a manufacturer account.
- For Matter devices, also check the used network, the availability of a pairing code, and the requirements for adding it to Home Assistant.

For the first attempt, choose one device with a documented connection procedure. Only after verifying its behaviour in your home should you expand to other rooms in the same way.

## Sources

- [Home Assistant: Zigbee and ZHA integration](https://www.home-assistant.io/integrations/zha/)
- [Home Assistant: Thread and border routers](https://www.home-assistant.io/integrations/thread/)
- [Home Assistant: Matter and connection requirements](https://www.home-assistant.io/integrations/matter/)
- [Connectivity Standards Alliance: standard Matter](https://csa-iot.org/all-solutions/matter/)
- [Home Assistant: Connect ZBT-2](https://www.home-assistant.io/connect/zbt-2/)
- [Home Assistant: Connect ZWA-2](https://www.home-assistant.io/connect/zwa-2/)
