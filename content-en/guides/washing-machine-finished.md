---
title: "Washing Machine Finished: Notification Instead of Monitoring"
description: "Detect the end of the wash cycle based on power consumption and send a notification to your phone."
cas: "30 minutes setup; verification during wash cycle"
obtiznost: "Intermediate"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Washing Machine"
  - "Alerting"
  - "Automation"
translationKey: "guides.washing-machine-finished"
---

## What will work in the end

Home Assistant recognizes the increased power consumption of the washing machine as the start of the cycle. When the consumption remains sufficiently low, it will send a notification to your mobile device. This is an estimation based on measurements, so you must first verify it on a full wash program.

## What you will need

You need a connected measurement of the washing machine's instantaneous power consumption in **watts**, a functional [phone notification](../open-window-alert/), and administrator credentials. An energy sensor in kWh is insufficient for this process.

If you use a measured socket, the manufacturer must allow its use with the specific appliance and its load. Check both the socket and the washing machine manuals; the maximum current alone is not confirmation of suitability. The socket automation does not switch off.

## First, understand the washing cycle

In the sensor history, monitor one entire program: the quiet period before starting, the wash cycle including pauses, and the state after completion. The waiting period for the end must be longer than normal low-consumption pauses.

The **20 W for one minute** for the start and **less than 5 W for five minutes** for the end listed below are only examples. Use them only if they match your measured cycle. If the pause and the end cannot be distinguished this way, this simple method is not suitable for the given program.

## Add memory that the washing machine is running

In **Settings → Devices & Services → Helpers**, create a **Toggle** helper, name it **Washing Machine Running**, and leave it switched off. This is a helper entity `input_boolean`, which stores information for the second rule; it does not control the washing machine's power.

## Example automation in YAML

Instead of clicking rules, you can use these blocks. Enter each one separately into the YAML editor as a new automation, without the wrapping key `automation:`. Replace `sensor.pracka_prikon`, `input_boolean.pracka_pracuje`, and `notify.mobile_app_muj_telefon` with your own identifiers. Adjust the values and times according to your measurements.

The first rule remembers the start:

```yaml
alias: Washing Machine Started
triggers:
  - trigger: numeric_state
    entity_id: sensor.pracka_prikon
    above: 20
    for: "00:01:00"
actions:
  - action: input_boolean.turn_on
    target:
      entity_id: input_boolean.pracka_pracuje
mode: single
```

The second, after the drop, checks the helper, switches it off, and sends a notification. If the notification fails, the message will not repeat automatically.

```yaml
alias: Washing Machine Finished
triggers:
  - trigger: numeric_state
    entity_id: sensor.pracka_prikon
    below: 5
    for: "00:05:00"
conditions:
  - condition: state
    entity_id: input_boolean.pracka_pracuje
    state: "on"
actions:
  - action: input_boolean.turn_off
    target:
      entity_id: input_boolean.pracka_pracuje
  - action: notify.mobile_app_muj_telefon
    data:
      message: "Washing machine consumption is low. Check the wash cycle."
mode: single
```

Create the helper using the previous section in the UI, or alternatively, add the following to `configuration.yaml`. If the `input_boolean:` section already exists, only add the `pracka_pracuje` item to it. Do not create the helper in both ways. It will be available after checking the configuration and restarting; without `initial`, it retains the previous state, and upon first startup, it is switched off.

```yaml
input_boolean:
  pracka_pracuje:
    name: Washing Machine Running
```

## Test the entire program

Set up the rules before starting the wash cycle. Monitor that the helper switches on upon startup and that no premature notification is received during normal pauses. After the end, verify both the notification and the switching off of the helper.

The numeric trigger reacts to crossing a threshold, not continuously. The waiting period is cancelled upon restarting or reloading the automation. If the program is interrupted or the measurement fails, the estimate may be incorrect; manually check the actual state and switch off the helper if necessary.

## Sources

- [Home Assistant: numeric_state trigger and its limitations](https://www.home-assistant.io/triggers/numeric_state/)
- [Home Assistant: input_boolean helper](https://www.home-assistant.io/integrations/input_boolean/)
- [Home Assistant: automation conditions](https://www.home-assistant.io/docs/automation/condition/)
- [Home Assistant: automation actions](https://www.home-assistant.io/docs/automation/action/)
- [Companion: phone notification](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
