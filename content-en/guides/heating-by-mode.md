---
title: "Heating by Daily Schedule"
description: "Set the thermostat's day and night temperature using a single automation in Home Assistant."
cas: "20 minutes"
obtiznost: "Medium"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - heating
  - thermostat
  - automation
  - YAML
translationKey: "guides.heating-by-mode"
---

Do you lower the thermostat temperature every evening and raise it again in the morning? Home Assistant can perform these changes based on time. Start with one room and a simple schedule. The example sets the target temperature to 21 °C from 6:00 and 19 °C from 22:00, every day. The values are illustrative; adjust them according to your household.

## What you need

The thermostat or radiator must be connected via its integration and available as a `climate` entity. When controlling it, first manually verify that the target temperature can be changed. A simple temperature sensor is not enough.

The example assumes a device with a single target temperature, set to heating, and units of °C. Devices in cooling and heating mode with two setpoints are not covered. The automation changes the desired temperature; the thermostat handles the actual regulation.

Find the entity ID, for example, `climate.living_room`. Also verify the Home Assistant timezone. If the thermostat uses its own time schedule, set the mode according to its manual, ensuring it accepts and holds changes from Home Assistant; two schedules might overwrite each other.

## Implementing the Automation

In **Settings → Automations & Scenes**, create a new empty automation. In the menu top right, select **Edit in YAML** and replace the entire content with the example. This is the YAML for a single automation, not the content of the `configuration.yaml` file.

Replace `climate.living_room` with your own ID. If you change the switching hours, also update the times in `at` and the boundaries `6` and `22` in the temperature calculation. The numbers `21` and `19` are the day and night temperatures.

```yaml
alias: Heating – day and night
description: Day and night target temperature
triggers:
  - trigger: time
    at: "06:00:00"
  - trigger: time
    at: "22:00:00"
actions:
  - action: climate.set_temperature
    target:
      entity_id: climate.living_room
    data:
      temperature: "{{ 21 if 6 <= now().hour < 22 else 19 }}"
mode: single
```

The calculation selects the temperature based on the current local hour. The automation does not change the thermostat's operating mode: if it is switched off, simply setting the temperature may not start the heating.

## Verification and Common Use

Save the automation and run its actions manually. Between 6:00 and 22:00, the thermostat should receive 21 °C, and 19 °C otherwise. Check the **target** temperature; the measured room temperature may not change immediately. If the action fails, open the automation's history and verify the ID, device availability, and supported temperature range.

Manually adjusted temperatures will remain until the next switchover, unless the thermostat or another rule changes them in the meantime. If you want to temporarily stop the schedule, disable the automation and set the temperature manually. After re-enabling it, run its actions so that the temperature corresponding to the current time is used.

Home Assistant must be running at 6:00 and 22:00, and the thermostat must be available. This example does not handle delayed switchovers or repeat changes upon device return. Therefore, check the status after an outage and run the action manually if necessary.

## Sources

- [Home Assistant: climate devices and their modes](https://www.home-assistant.io/integrations/climate/)
- [Home Assistant: setting the thermostat target temperature](https://www.home-assistant.io/actions/climate.set_temperature/)
- [Home Assistant: automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: dates and times in templates](https://www.home-assistant.io/docs/templating/dates-and-times/)
- [Home Assistant: automation editor and YAML implementation](https://www.home-assistant.io/docs/automation/editor/)
