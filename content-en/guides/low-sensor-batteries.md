---
title: "Low Sensor Battery Warning"
description: "Set Home Assistant to check the sensor battery every evening and display a replacement reminder."
cas: "15 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - battery
  - sensors
  - automation
  - YAML
translationKey: "guides.low-sensor-batteries"
---

A window sensor might stop reporting changes, and you only discover later that it needs a new battery. Home Assistant can check the battery status regularly. Start with one sensor: check its value every evening at 18:00. It will also react when the battery reading changes. When it reaches 20% or less, it will display a reminder directly in the Home Assistant interface.

## Select the correct entity

On the device, find the battery entity, for example, `sensor.window_battery`. The example requires a numerical value in percentages. Some devices only provide an "low battery" status as a `binary_sensor`; this YAML is not suitable for those.

Verify the entity ID and the unit %. The 20% threshold is illustrative; adjust it according to your device. The warning relies on the last available reading; the automation itself does not force a new battery measurement. It does not promise a specific number of remaining operational days.

## Insert the automation

In **Settings → Automations & Scenes**, create an empty automation. In the menu in the top right, select **Edit in YAML** and replace the entire content with the following block. This belongs in the editor of a single automation, not in `configuration.yaml`.

Replace all instances of `sensor.window_battery` with your own ID. Adjust the sensor name in the message, or the time `18:00:00` and the threshold `20`. The threshold includes exactly 20%. If you change it, update the number in the template condition.

```yaml
alias: Low Battery Window Sensor
triggers:
  - trigger: time
    at: "18:00:00"
  - trigger: state
    entity_id: sensor.window_battery
    to: null
actions:
  - condition: template
    value_template: >-
      {{ is_number(states('sensor.window_battery'))
         and states('sensor.window_battery') | float(101) <= 20 }}
  - action: persistent_notification.create
    data:
      title: Low Battery
      message: Check the window sensor battery.
      notification_id: battery_window
mode: single
```

The condition is part of the actions, so it is checked even when running manually. The trigger reacts to a change in the battery value, not just a change in attributes. The threshold is checked only in the condition before the notification is created. When it changes to 20% or less, the reminder will be created or updated, for example, even when dropping from 20% to 19%. If the value is higher, no notification will be created. Using the same `notification_id` updates the existing reminder instead of creating multiple copies.

## Where to view the message

This is a persistent notification in the Home Assistant interface that you can dismiss. It is not a push message to the locked phone screen; for such a message, you would need to add mobile app notifications.

After replacing the battery, check the new reading and manually dismiss the reminder. The example will not automatically clear it when the status improves. If you dismiss it and the battery remains at or below the threshold, the next evening check will recreate it.

## Test the result

Save the automation and run its action. If the battery is 20% or less, check the notification. Otherwise, for a short test, you can temporarily increase the threshold above the current value and then revert it after checking. In the automation trace, you can see if the condition stopped it.

`unknown` and `unavailable` states are not numbers: this example will not create a low battery message for them. Returning from such a state to a numerical value will trigger the check again. Therefore, check unavailable devices separately. Home Assistant must be running to check. A delayed time will not be corrected; the next change in the battery value or the evening check will re-evaluate it.

For another sensor, copy the automation and change the entity ID, text, and `notification_id` so that it has its own reminder.

## Sources

- [Home Assistant: numerical conditions](https://www.home-assistant.io/docs/scripts/conditions/)
- [Home Assistant: persistent notifications](https://www.home-assistant.io/integrations/persistent_notification/)
- [Home Assistant: creating notifications](https://www.home-assistant.io/actions/persistent_notification.create/)
- [Home Assistant: time triggers](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: templates](https://www.home-assistant.io/docs/templating/)
- [Home Assistant: automation editor](https://www.home-assistant.io/docs/automation/editor/)
