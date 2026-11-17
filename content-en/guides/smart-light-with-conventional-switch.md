---
title: "Smart Lights and Conventional Switches: Do Not Cut the Power"
description: "How to keep a conventional switch with Shelly in Detached mode and control smart lighting with different brightness levels during the day and at night."
cas: "6 minutes read"
obtiznost: "Intermediate"
kontrola_zdroju: "2026-10-01"
stav: "Documented"
temata:
  - Smart lighting
  - Shelly
  - Zigbee
  - Detached
  - Automation
translationKey: "guides.smart-light-conventional-switch"
---

You cannot simply screw in a smart bulb and turn it off with a conventional switch. As soon as the switch cuts the power, the light stops communicating. Home Assistant cannot turn it back on, nor can it change the brightness or colour. This applies to Wi-Fi, Zigbee, and Matter-controlled lights. A light turned off by a command remains powered; a light disconnected by a switch does not.

## Why the Zigbee network matters

Many Zigbee lights function as routers: they relay messages to other devices. By disconnecting such a light, you might degrade the connection for sensors or other lights. Not every bulb plays this role; verify the specific model. Zigbee routers must remain available even when they are off.

The solution is to provide continuous power to the light and use a controller that only sends a command. This could be a wireless button or a module installed behind the original switch with a separate input.

## Shelly retains the original switch

An example is the [Shelly 1PM Mini Gen3](https://www.shelly.com/products/shelly-1pm-mini-gen3), a Wi-Fi module from the Shelly group, based in Bulgaria, thus in the EU. The manufacturer's headquarters does not dictate where a specific unit was made. Other brands exist; choose based on support for a detached input and local integration, not just origin.

The module also requires a neutral wire (N), which may not be present in an old box. You must verify the space and suitability for wiring. Wiring the installation into a 230 V distribution board must be done by a qualified electrician according to the manufacturer's documentation.

After installation, connect the Shelly to Wi-Fi and open its local web interface by entering the IP address into a browser. On the initial page, open the input/output settings:

- **Input mode: Switch** for a standard toggle switch.
- **Output type: Detached Switch** separates the input from the relay.
- **Action on power on: Turn ON** restores power after an outage.

Manually turn the relay on and off, and disable automatic switching timers and schedules. Detached does not power the relay itself and cannot prevent switching off via the app or the module's protection. Automations should control the light, not the Shelly relay.

In Home Assistant, add **Shelly** in **Settings → Devices & Services**. The integration works locally; you do not need a Shelly Cloud account. Find the input binary sensor; it is created when the Switch mode is used. When toggling, verify the change between `on` and `off`.

## Brightness by time

Example: Every time the switch is toggled, the lit light turns off, or the unlit light turns on. From 22:00 to 4:59, it sets 50%; from 5:00 to 21:59, it sets 100%. Brightness is chosen upon turning on; at 22:00, the lit light will not automatically dim. The switch position therefore does not determine on/off: the change in position does.

Create an empty automation in **Settings → Automations & Scenes**, open **Edit in YAML**, and paste the entire example. Replace `binary_sensor.shelly_vstup` and `light.pokoj` with your IDs. The light must be added to Home Assistant and support dimming.

```yaml
alias: Switch and smart light by time
triggers:
  - platform: state
    entity_id: binary_sensor.shelly_vstup
    from: "off"
    to: "on"
  - platform: state
    entity_id: binary_sensor.shelly_vstup
    from: "on"
    to: "off"
conditions: []
actions:
  - choose:
      - conditions: "{{ is_state('light.pokoj', 'on') }}"
        sequence:
          - service: light.turn_off
            target:
              entity_id: light.pokoj
    default:
      - service: light.turn_on
        target:
          entity_id: light.pokoj
        data:
          brightness_pct: "{{ 50 if now().hour >= 22 or now().hour < 5 else 100 }}"
mode: single
```

You can similarly set 20% for a night corridor or other values for a bedroom. During a failure of Home Assistant or Wi-Fi, this automation will not process the switch; continuous power does not guarantee backup control.

## Sources

- [Home Assistant: Shelly and binary inputs](https://www.home-assistant.io/integrations/shelly/)
- [Home Assistant: Zigbee and mains-powered routers](https://www.home-assistant.io/integrations/zha/)
- [Shelly: 1PM Mini Gen3](https://www.shelly.com/products/shelly-1pm-mini-gen3)
- [Shelly: 1PM Mini Gen3 technical specifications and wiring](https://kb.shelly.cloud/knowledge-base/shelly-1pm-mini-gen3)
- [Shelly: web interface and Detached Switch](https://kb.shelly.cloud/knowledge-base/shelly-1pm-mini-gen3-web-interface-guide)
- [Shelly Group: company headquarters](https://corporate.shelly.com/en/page/impressum)
- [Home Assistant: controlling lights](https://www.home-assistant.io/integrations/light/)
