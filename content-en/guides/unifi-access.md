---
title: "UniFi Access and Home Assistant: Doors, Lights, and Alerts"
description: "How to connect UniFi Access to Home Assistant and use the status of doors, intercoms, and entry events in automations."
obrazek: "/assets/images/unifi-access.png"
obrazek_alt: "Illustration of entry doors with a reader connected to home automation, lights, and alerts."
cas: "5 minutes read"
obtiznost: "Advanced"
kontrola_zdroju: "2026-10-27"
stav: "Based on documentation"
temata:
  - "UniFi Access"
  - "Doors"
  - "Automation"
  - "Local operation"
translationKey: "guides.unifi-access"
---

## What the Connection Provides

UniFi Access is an entry control system from Ubiquiti, based in the USA. It manages readers, door locks, and access credentials. Home Assistant adds domestic functionality to it: hallway lighting, alerts for open doors, or notifications upon ringing the bell.

Use the **UniFi Access** integration, not UniFi Network for the mesh or Protect for cameras. It has been part of HA since version 2026.4, so you do not need HACS. It communicates with the controller on the local network via API and continuous WebSocket updates.

## What You Need and How to Start

You need a functional Access system with an application on a supported UniFi console, a door hub, and the appropriate wiring. HA must be able to reach the console on the network. A standalone Wi-Fi access point is not enough.

1. In the **Access → Settings → General** application, search for the **API Token**, or check the **Advanced** section. Create a token for HA, set permissions, and save it securely; it will only be displayed once. Do not create the key on the Integrations console page for Protect.
2. In HA, open **Settings → Devices & Services → Add Integration → UniFi Access**. Enter the controller address and the token.
3. Verify the created entities. The unlock button sends a pulse for the duration set in Access. The door binary sensor reports open (`on`) and closed (`off`); for the actual position, you need a correctly wired door contact.

The unlock button is not proof that the door is closed or locked. A routine unlock is also not a command for permanent unlocking.

## Two Examples to Implement

Implement each block **separately** into a new automation via **Edit in YAML**. Replace `binary_sensor.vchod_door` with your actual Access sensor and `light.predsin` with your own light. The light must already be connected to HA.

### Lighting when opening after sunset

```yaml
alias: Access – light on door opening
triggers:
  - trigger: state
    entity_id: binary_sensor.vchod_door
    from: "off"
    to: "on"
conditions:
  - condition: state
    entity_id: sun.sun
    state: below_horizon
actions:
  - action: light.turn_on
    target:
      entity_id: light.predsin
mode: single
```

This example only turns the light on. For automatic switching off, you can add a separate automation based on motion.

### Door open for more than two minutes

```yaml
alias: Access – door open for too long
triggers:
  - trigger: state
    entity_id: binary_sensor.vchod_door
    from: "off"
    to: "on"
    for: "00:02:00"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: Entry Door
      message: The door has been open for more than two minutes.
mode: single
```

The notification can be found within HA; it is not a push message to your phone. The `for` wait period resets upon HA restart or automation reload.

## Intercom and Denied Entry

Create another automation in the editor: select the relevant Access entity event as the trigger and the `access_denied` type, and use creating a notification as the action. For the intercom, use its `ring` event, for example, to flash a light. The `access_granted` event can trigger a welcome scene; however, it does not confirm that a person has passed through. Not every hardware combination supports ringing, but the entity may still be created.

Manage credentials and visit schedules in Access. The **Evacuation** and **Lockdown** modes affect all controller doors; do not use them for routine unlocking of single doors. After setup, manually open and close the door, verify the sensor, and review the automation trace. If connection errors occur, check the availability of the console, firewall, and token validity.

## Sources

- [Home Assistant: UniFi Access](https://www.home-assistant.io/integrations/unifi_access/)
- [Ubiquiti: Official UniFi API](https://help.ui.com/hc/en-us/articles/30076656117655-Getting-Started-with-the-Official-UniFi-API)
- [Ubiquiti: Access API documentation](https://assets.identity.ui.com/unifi-access/api_reference.pdf)
- [Home Assistant: Automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: Persistent notifications](https://www.home-assistant.io/integrations/persistent_notification/)
- [Ubiquiti: Company headquarters](https://www.ui.com/contact/)
