---
title: "Shelly Devices for Home Assistant: What to Choose for Your Home"
description: "An overview of Shelly switches, sensors, lights, cameras, sockets, and electricity meters and how they connect to Home Assistant."
cas: "6 minutes' read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Documentation-based"
temata:
  - Shelly
  - Smart Lighting
  - Sensors
  - Energy Monitoring
  - Smart Plugs
  - Cameras
translationKey: "buying-guide.shelly-devices-overview"
---

Shelly offers devices for lighting, appliance control, electricity monitoring, and home security. The group is based in Bulgaria, which is in the EU; this is not the place of manufacture for any specific unit. When choosing, start with what you want to solve at home, and then verify the exact model and its connection to Home Assistant.

## Devices by Type

- **Lights and Dimmers:** The Shelly Duo Bulb E27 Gen3 changes brightness and white colour temperature. For a standalone dimmer, verify its suitability for the light source you are using.
- **Smart Plugs:** The Shelly Plug M Gen3 switches appliances, measures consumption, and supports Matter. Verify the version for the Czech network and the allowed load.
- **Switches and Relays:** The Shelly 1PM Mini Gen3 is a module for an existing switch that provides switching and consumption measurement. The Shelly BLU Wall Switch 4 is a four-button Bluetooth controller for commands and scenes.
- **Motion Detection:** The Shelly BLU Motion ZB detects movement and measures ambient lighting. It can turn on a hallway light, or only when it is dark.
- **Doors and Windows:** The Shelly BLU Door/Window ZB records opening and closing. This is useful for alerting about ventilation or regulating heating.
- **Water Leakage:** The Shelly Flood S Gen4 monitors water under a washing machine, sink, or pipework. It can trigger an alert; the sensor itself cannot shut off the water supply.
- **Electricity Monitoring:** The Shelly Pro 3EM v2 is used for three-phase measurement in a distribution board via Wi-Fi or LAN. Verify suitable measuring transformers. A socket with measurement, conversely, monitors a single appliance.
- **Cameras:** The Shelly Camera offers video via RTSP. For Home Assistant, enable RTSP Streaming in the local panel under **Camera → Settings**. Treat cloud functions separately.

You can find variants in the [official Shelly store](https://www.shelly.com/collections/all-products). You can start with a plug or a battery sensor. For mounting modules and meters into a 230 V distribution board, entrust the work to a qualified electrician.

## Connecting to Home Assistant

Add supported Wi-Fi devices via **Settings → Devices & Services → Add Integration → Shelly**, or confirm automatic discovery. The [official Shelly integration in Home Assistant](https://www.home-assistant.io/integrations/shelly/) communicates directly with the device and does not require Shelly Cloud. Available entities and functions depend on the model.

Bluetooth sensors and controllers **BLU** are usually added via [BTHome](https://www.home-assistant.io/integrations/bthome/), not through the Shelly integration. You need a Bluetooth adapter or a supported receiver within range. **ZB** variants may offer Zigbee; the **Wave** series uses Z-Wave. For these protocols, you need a corresponding controller and integration. Therefore, verify the exact name and protocol before purchasing.

## Example: Motion Turning On a Light

First, add both a motion sensor and a light to Home Assistant. For example, connect the Shelly BLU Bluetooth sensor via BTHome and the Shelly Wi-Fi light via the Shelly integration. On the sensor's page, verify that detection changes the state of the motion entity to `on`.

In **Settings → Automations & Scenes**, create an empty automation, open the dropdown, and select **Edit in YAML** and paste the entire example. Replace both IDs with the actual entities of your motion sensor and light.

```yaml
alias: Motion turns on hallway
triggers:
  - platform: state
    entity_id: binary_sensor.hallway_motion
    to: "on"
condition: []
action:
  - service: light.turn_on
    target:
      entity_id: light.hallway
mode: single
```

This example only turns the light on. Add the turning off after a period of no motion as a separate automation. A smart bulb must remain powered even when switched off; you can find solutions for the original switch in the guide [Smart Lighting and Classic Switch](/guides/smart-light-with-conventional-switch/).

## Sources

- [Shelly: all products](https://www.shelly.com/collections/all-products)
- [Home Assistant: Shelly and RTSP cameras](https://www.home-assistant.io/integrations/shelly/)
- [Home Assistant: BTHome](https://www.home-assistant.io/integrations/bthome/)
- [Shelly Group: company headquarters](https://corporate.shelly.com/en/page/impressum)
- [Shelly 1PM Mini Gen3](https://www.shelly.com/products/shelly-1pm-mini-gen3)
- [Shelly BLU Wall Switch 4](https://www.shelly.com/products/shelly-blu-wall-switch-4)
- [Shelly BLU Motion ZB](https://www.shelly.com/products/shelly-blu-motion-zb)
- [Shelly BLU Door/Window ZB](https://www.shelly.com/products/shelly-blu-door-window-zb-white)
- [Shelly Flood S Gen4](https://www.shelly.com/products/shelly-flood-s-gen4)
- [Shelly Plug M Gen3](https://www.shelly.com/products/shelly-plug-m-gen3-white)
- [Shelly Pro 3EM v2](https://www.shelly.com/products/shelly-pro-3em-v2)
- [Shelly Duo Bulb E27 Gen3](https://www.shelly.com/products/shelly-duo-bulb-e27-gen3)
- [Shelly Camera](https://www.shelly.com/products/shelly-camera)
- [Home Assistant: turning on a light](https://www.home-assistant.io/actions/light.turn_on/)
