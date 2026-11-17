---
title: "SmartThings and Home Assistant: A Step-by-Step Connection Guide"
description: "How to connect SmartThings to Home Assistant, what works with Samsung TVs, and what to watch out for regarding the cloud, permissions, and VLANs."
obrazek: "/assets/images/smartthings-home-assistant.png"
obrazek_alt: "Illustration of a smart home connected to Home Assistant via the internet cloud."
cas: "10 minutes reading time"
obtiznost: "Advanced"
kontrola_zdroju: "2026-11-03"
stav: "Documentation-based"
temata:
  - "SmartThings"
  - "Samsung TV"
  - "Cloud"
  - "Automation"
translationKey: "integrations.smartthings-home-assistant"
---

## What the Connection Provides

The official **SmartThings** integration exposes SmartThings home devices and scenes within Home Assistant. It is particularly useful for Samsung appliances, televisions, and existing SmartThings Hubs. Depending on the specific device, you may get lights, sensors, locks, thermostats, media players, or other entities. However, not every function from the application is available via the API.

This is a **Cloud Push** integration: Home Assistant sends commands to the SmartThings cloud and receives changes back as cloud events. Therefore, the connection requires an internet connection to function. Authentication tokens are managed by the OAuth flow; do not create old long-term personal tokens based on outdated guides. Furthermore, Samsung has announced a transition to a paid personal plan for API access starting October 2026, so please verify the current conditions before installation.

## What You Need and How to Add the Integration

You need a Samsung account, devices already added to the SmartThings mobile app, and a current Home Assistant installation with the default cloud component loaded. The integration is configured in the UI, not in `configuration.yaml`.

1. In Home Assistant, open **Settings → Devices & Services → Add Integration → SmartThings**.
2. Log in with your Samsung account and approve the required permissions. Only enable the home and access that you want to grant to Home Assistant.
3. Upon return, check the created devices and entities. Names like `media_player.living_room_tv` are just examples; use your own IDs from HA.

A Samsung TV may appear as a media player only if it provides the necessary capabilities via SmartThings. For local control of supported televisions, a dedicated Samsung Smart TV integration is often more suitable. A potential hurdle here is a segmented VLAN: televisions do not accept WebSocket connections from a different subnet. SmartThings does not use this local connection, but rather relies on the internet and the Samsung cloud.

## Two Practical Examples

Please add each block **separately** to a new automation via **Edit in YAML**. First, replace the example IDs with your actual entities.

### Lighting when the door opens

```yaml
alias: SmartThings – Light when door opens
triggers:
  - platform: state
    entity_id: binary_sensor.entrance_door
    from: "off"
    to: "on"
conditions:
  - condition: state
    entity_id: sun.sun
    state: below_horizon
actions:
  - service: light.turn_on
    target:
      entity_id: light.hallway
mode: single
```

The trigger is the change in the door contact, the condition is night time, and the action is turning on the light.

### Notification after laundry is finished

```yaml
alias: SmartThings – Washing machine finished cycle
triggers:
  - platform: state
    entity_id: sensor.washing_machine_status
    to: "complete"
conditions: []
actions:
  - service: persistent_notification.create
    data:
      title: Washing Machine
      message: Cycle finished. You can take out the laundry.
mode: single
```

The value `complete` is only an example. In **Developer Tools → States**, first determine the actual entity and value that your model reports.

## When Something Is Missing or Not Working

Open the SmartThings integration, the device, and **Download diagnostics**; for status issues, enable debug logging. Missing functionality often means the device does not provide it via the API, or the integration has not mapped it yet. If there is a login error, repeat the authorization process and check the permissions. Verify the internet, DNS, and outgoing HTTPS from the Home Assistant VLAN; do not open incoming ports to the local network. Do not copy tokens anywhere.

The advantage is the wide range of supported devices and the easy UI setup. The disadvantage is the cloud dependency, variable feature support, and changing API conditions. For Zigbee, Z-Wave, or Matter devices, consider direct local connection to HA; for the TV, compare the local Samsung Smart TV integration.

## Sources

- [Home Assistant: SmartThings](https://www.home-assistant.io/integrations/smartthings/)
- [SmartThings: Authorization and Permissions](https://developer.smartthings.com/docs/getting-started/authorization-and-permissions)
- [SmartThings: Architecture and Authorization Flow](https://developer.smartthings.com/docs/service-integrations/architecture-and-auth-flow)
- [SmartThings: A New Enhanced SmartThings API Experience](https://community.smartthings.com/t/a-new-enhanced-smartthings-api-experience/309947)
- [Home Assistant: Samsung Smart TV](https://www.home-assistant.io/integrations/samsungtv/)
- [Home Assistant: Automation Triggers](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: Persistent Notifications](https://www.home-assistant.io/integrations/persistent_notification/)
