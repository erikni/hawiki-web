---
title: 'Bluetooth in Home Assistant: adapters, proxies, and better range'
seoTitle: 'Bluetooth and Home Assistant: adapters, proxies, and diagnostics'
description: 'A practical Czech guide to Bluetooth in Home Assistant: selecting an adapter, remote ESPHome proxies, range, active connections, and resolving outages.'
cas: 17 minutes' read
obtiznost: Intermediate
kontrola_zdroju: '2026-11-13'
stav: Based on documentation
sourceType: official-docs
obrazek: /assets/images/bluetooth-home-assistant.png
obrazek_alt: A house covered by a local Bluetooth adapter and two remote proxies for sensors and a lock
temata:
- Bluetooth
- Bluetooth proxy
- ESPHome
- Range
- Diagnostics
related:
- getting-started/devices-entities-and-integrations
- help/device-not-responding
- help/automation-not-working
- help/internet-outage
translationKey: "integrations.bluetooth-home-assistant"
---

The **Bluetooth** integration provides Home Assistant with a common layer for local adapters and remote proxies. It scans for nearby devices and passes their data to specific integrations, such as BTHome, SwitchBot Bluetooth, Xiaomi BLE, or Yale Access Bluetooth.

Bluetooth itself therefore usually does not create a temperature sensor or a lock. It ensures the reception of BLE advertisements or an active connection, and Home Assistant will offer an integration for the recognized device. This is local communication.

## What are adapters, proxies, and advertising

A **Bluetooth adapter** is a radio directly connected to the Home Assistant system: a built-in chip, USB dongle, or card. On Linux, Home Assistant communicates with it via BlueZ and D-Bus.

A **Bluetooth proxy** is a standalone network device that you place closer to the sensors. It receives Bluetooth Low Energy (BLE) and forwards the data to Home Assistant via Wi-Fi or Ethernet. Home Assistant aggregates all local adapters and supported proxies, and a suitable integration can use the path with the best signal.

**Advertising** is a short message that a BLE device broadcasts without establishing a connection. Many temperature sensors transmit values this way. Other devices, such as a lock or a thermostat, require an **active connection** for reading or commanding. Not every proxy supports active connections.

The Bluetooth integration is not the same as a manufacturer's "gateway," which may send data to its own application or cloud. A proxy is a general scanner, and the entity itself does not create one.

## Requirements

- Home Assistant OS 9.0 or newer, or a properly configured Linux/Container,
- a supported local Bluetooth adapter or remote proxy,
- a device with its own supported integration in Home Assistant,
- a suitable location without strong metal shielding and USB 3 interference,
- for a proxy, a reliable network between the proxy and Home Assistant.

On Linux, the documentation requires accessible D-Bus, BlueZ at least 5.43 (recommended 5.63 or newer), dbus-broker, and kernel 5.15.62 or newer. Home Assistant OS handles these requirements automatically. The Container must ensure these requirements on the host.

## Local USB Adapter

If the server does not have Bluetooth, use a supported USB adapter. Home Assistant maintains a list of known working models; the chip name is more important than the dongle's similar appearance. Some newer adapters require firmware that cannot be easily updated in Home Assistant OS.

Do not connect the adapter close to a USB 3 drive, SSD, Wi-Fi antenna, or metal enclosure. A short, quality USB 2 extension cable often improves reception more significantly than changing the software. After the initial connection, several restarts may be required before the system correctly recognizes the adapter.

In Home Assistant, open **Settings → Connectivity → Bluetooth → Adapters**. Here you will see local and remote scanners, and clicking on a device shows the details. If a gear icon is available, you can change the scanning mode:

- **Auto** is the recommended option; it listens passively most of the time and uses active scanning when necessary,
- **Active** acquires supplementary data fastest, but increases the power consumption of nearby battery-powered devices,
- **Passive** only listens and may not be sufficient for some integrations.

Auto and Passive require support for passive scanning. If the adapter does not have it, Auto switches to Active.

## Home Assistant Container

The container cannot simply pass through a USB device. The host must run BlueZ, and the container must be able to see D-Bus. The documentation also requires `NET_ADMIN` and `NET_RAW` capabilities; without these, Bluetooth functionality is limited and the adapter cannot be reliably restored.

The following section belongs in the Home Assistant service's `compose.yaml`, not in `configuration.yaml`. Keep the rest of your service's configuration and then recreate the container.

```yaml
services:
  homeassistant:
    cap_add:
      - NET_ADMIN
      - NET_RAW
    volumes:
      - /run/dbus:/run/dbus:ro
```

If the host uses D-Bus in `/var/run/dbus`, map it to `/run/dbus` in the container. The warning "Bluetooth adapter requires additional permissions" in the logs means that one of these permissions is missing.

## Remote Bluetooth Proxy

A proxy is useful when Home Assistant is located in a basement, rack, or on the opposite end of the house. The most common variant is an ESPHome device with a Bluetooth proxy, but Home Assistant also receives advertisements from supported Shelly Gen2+ and SMLIGHT SLZB-U. According to the documentation, these two variants only listen for advertisements and cannot establish active Bluetooth connections.

An ESPHome proxy can receive advertisements and establish active GATT connections. A pre-built ESPHome project is safer for the average user than copying a random configuration. Once added to ESPHome, the proxy will appear among Home Assistant's Bluetooth adapters.

For a custom ESPHome project, `bluetooth_proxy` depends on the BLE tracker of the given platform. The following is only the relevant part; the entire firmware must also include board, network, API, update, and security data.

```yaml
bluetooth_proxy:
  active: true
```

On the ESP32, active connections are enabled by default, and there are three slots by default. ESPHome recommends not exceeding five. Advertisement slots do not consume resources, and permanently connected locks do.

Place the proxy in the same room or near the problematic devices, but not right next to the Wi-Fi AP. Use multiple proxies with spacing so they do not unnecessarily cover the same area. Ethernet limits the concurrency of Wi-Fi and Bluetooth on one radio, but it is not a requirement.

## How to add a device

1. Add and verify a local adapter or proxy.
2. Open **Settings → Devices & Services** and check the **Discovered** section.
3. Select the integration for the specific device, not Bluetooth again.
4. Complete its wizard. Encrypted devices may require a key or credentials from the manufacturer's app.
5. On the device page, verify that the values change and that entities are available.

The Bluetooth integration can be added manually via **Add integration → Bluetooth** if it was not created automatically. However, Home Assistant manages other adapters together; a separate Bluetooth integration is not added for every dongle.

## Example 1: High temperature alert

This example assumes a BLE temperature sensor that has exposed itself as an entity via its own integration. Replace `sensor.ble_sklep_teplota` with your actual ID. Insert the entire block into the YAML editor for a new automation.

```yaml
alias: Bluetooth – high temperature in the basement
triggers:
  - platform: numeric_state
    entity_id: sensor.ble_sklep_teplota
    above: 28
    for: "00:05:00"
condition: []
action:
  - service: persistent_notification.create
    data:
      title: "Basement Temperature"
      message: >-
        Bluetooth sensor reports
        {{ states('sensor.ble_sklep_teplota') }} °C.
mode: single
```

The trigger waits for five minutes above 28 °C to avoid reacting to a single faulty packet. The notification will be created within Home Assistant. The accuracy and speed of updates are determined by the specific sensor and its integration, not the Bluetooth layer itself.

## Example 2: Low battery BLE sensor

Replace the battery entity with a real ID. Not every Bluetooth device reports battery level. Insert the block into the YAML editor as a separate automation.

```yaml
alias: Bluetooth – low battery sensor
triggers:
  - trigger: numeric_state
    entity_id: sensor.ble_sklep_baterie
    below: 15
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: "Replace battery"
      message: >-
        The BLE sensor in the basement has
        {{ states('sensor.ble_sklep_baterie') }} % battery.
mode: single
```

The automation will trigger when the value drops below 15%. If the device reports the battery status only a few times a day, the notification will only arrive with the next report.

## How to diagnose range

First, distinguish whether the device is only advertising, or if it requires a connection. A proxy without active connections can easily detect a thermometer, but it will not help a lock that requires commands.

On the Bluetooth page, open individual scanners and monitor whether the problematic device is within their range. Start with one change: move the proxy or USB adapter, use an extension cable, and monitor the updates for several minutes. Do not add several proxies at once, or you won't find the cause.

Bluetooth operates in the same 2.4 GHz band as Wi-Fi. Metal, reinforced concrete, distribution boards, USB 3 devices, and poorly placed Wi-Fi radios can degrade reception. A higher number of bars in the manufacturer's app is not proof that Home Assistant is receiving the same advertisements via the same path.

## When Bluetooth doesn't work

- **Adapter is not visible:** restart the host, check the USB and the adapter page. On Linux, verify BlueZ, D-Bus, and kernel support.
- **Container reports limited permissions:** add D-Bus, `NET_ADMIN`, and `NET_RAW`, and recreate the container.
- **Device is discovered, but setup cannot be completed:** it may require an active connection that the proxy cannot handle, or all slots may be occupied.
- **Values fluctuate irregularly:** move the scanner, distance the USB adapter from interference, and verify the scanning mode.
- **Device is not found:** verify supported integration, power on the device, and use its pairing mode if necessary. Not all Bluetooth devices are supported by Home Assistant.
- **Nothing improved after adding another proxy:** check its network connection and whether it actually covers a different area.
- **Active device disconnects:** check the number of available slots and signal strength; temporary connection failures are common with BLE.

## Privacy, Security, and Limitations

Bluetooth advertisements can be received by any compatible scanner within range. For sensitive data, prefer devices with supported encryption and store keys only in Home Assistant. Connect proxies to a trusted network and update their firmware.

Bluetooth is not a suitable replacement for a secure alarm protocol. Availability depends on radio, battery, interference, and the proxy network. Automations for locks or property protection must account for unavailability and a safe default state.

The advantage of mesh networks is the combination of multiple adapters, automatic selection of the best path, and local operation. The disadvantage is shorter range, limited active slots, and varying adapter quality. For an entire house, several strategically placed proxies are often more practical than one powerful dongle in a utility room.

## Sources

- [Home Assistant: Bluetooth integration](https://www.home-assistant.io/integrations/bluetooth/)
- [Home Assistant: Bluetooth Adapters](https://www.home-assistant.io/integrations/bluetooth_adapters/)
- [ESPHome: Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy/)
- [Home Assistant: automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
