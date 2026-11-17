---
title: 'Motion-activated light: turning on and off in one automation'
description: The sensor turns on the light when motion is detected and turns it off after two minutes of no motion. One guide, one automation, and finished YAML.
cas: 20 minutes
obtiznost: Easy; pasting YAML
kontrola_zdroju: '2026-09-30'
stav: Based on documentation; YAML syntax verified
temata:
- Lighting
- Motion sensor
- Automation
- YAML
translationKey: "guides.motion-activated-light"
---

## How it will work

When you enter the hallway, the light turns on. When you leave, the sensor begins reporting no movement. After two minutes in this state, the light turns off.

Everything is managed by **one automation with two triggers**:

- **Movement:** turn on.
- **Two minutes without movement:** turn off.

If the sensor detects movement again during the wait, the turn-off wait is cancelled. A new two minutes only starts upon the next transition to the no-movement state.

## What you need

- A working Home Assistant.
- A connected motion sensor with a motion/no-motion state.
- A connected light that you already know how to turn on and off from Home Assistant.

This example uses a light of type `light`. An outlet designated as `switch` requires different actions; you can find the adjustment below. The routine will turn on even during the day and will turn off the selected light regardless of whether you previously turned it on manually.

## Find Sensor and Light Names

In Home Assistant, every controlled or monitored entity has an ID, which is the precise name used in automations.

In **Settings → Devices & Services → Entities**, search for the sensor and light. In the details, copy their ID. In our example, these are fictional:

| Entity | Example ID |
| --- | --- |
| Motion sensor | `binary_sensor.pohyb_chodba` |
| Hallway light | `light.chodba` |

Select a real motion detection entity, not the sensor's battery or signal strength. We use the triggers **Motion detected** (`motion.detected`) and **Motion cleared** (`motion.cleared`) directly. You do not need to manually set the `on` and `off` state transitions. The sensor must be recognized by Home Assistant as a motion sensor, and your version must support these triggers.

## Add the automation

1. Open **Settings → Automations & Scenes**.
2. Create a new empty automation.
3. From the three-dot menu, select **Edit in YAML**.
4. Replace the editor content with the code below.
5. Change both IDs to your actual values in all instances.
6. Save and verify that the automation is enabled.

The code is intended **for the YAML editor of a single automation**. Do not add `automation:` or an introductory list bullet point before it.

## Complete YAML

```yaml
alias: Hallway – motion-activated light
description: Turns on when motion is detected and turns off after two minutes of no motion.
triggers:
  # Sensor starts detecting motion.
  - trigger: motion.detected
    target:
      entity_id: binary_sensor.pohyb_chodba
    id: pohyb

  # Sensor must be continuously clear of motion for two minutes.
  - trigger: motion.cleared
    target:
      entity_id: binary_sensor.pohyb_chodba
    options:
      for: "00:02:00"
    id: bez_pohybu

conditions: []
actions:
  - choose:
      # Branch for trigger with ID "pohyb".
      - conditions:
          - condition: trigger
            id: pohyb
        sequence:
          - action: light.turn_on
            target:
              entity_id: light.chodba

      # Branch for trigger with ID "bez_pohybu".
      - conditions:
          - condition: trigger
            id: bez_pohybu
        sequence:
          - action: light.turn_off
            target:
              entity_id: light.chodba
mode: restart
```

## How the trigger works

Every trigger has its own **`id`**. This allows the automation to know why it was triggered. In the **`choose`** section, it will run the corresponding branch: turning on upon `motion`, turning off upon `no_motion`.

**`options.for: "00:02:00"`** in `motion.cleared` means two minutes of continuous no motion. Want five minutes? Change the value to `"00:05:00"`.

**`mode: restart`** determines the behavior upon a new trigger: any previous run of the action will be cancelled and a new one will start. However, the two-minute wait itself is handled by `options.for` in the trigger; the mode does not override it.

## Test both triggers

1. Set the sensor to a no-motion state and turn off the light.
2. Walk in front of the sensor. Verify that the light turns on.
3. Move out of range and wait until the sensor genuinely registers "no motion."
4. From this point, wait another two minutes. The light should turn off.
5. Repeat the attempt, but return before the end of the wait. If the sensor reports motion again, the original wait will be canceled.

The time from leaving to the light turning off may be longer than two minutes: some sensors retain the motion state for a short time even after you have left.

**Simply manually triggering actions is not the correct test for this example.** It will not create an actual trigger ID that the automation selects. Test by triggering the sensor or by viewing the actual run trace of the automation.

## If controlling a light via an outlet

When the target is, for example, `switch.zasuvka_lampa`, change:

- `light.turn_on` to `switch.turn_on`.
- `light.turn_off` to `switch.turn_off`.
- Both occurrences of `light.chodba` to `switch.zasuvka_lampa`.

The light's regular switch must remain on for the outlet to be able to control it.

## When something doesn't work

**Doesn't turn on:** Verify the actual ID, sensor state, and manual control of the light. The trigger reacts to the start of motion detection; simply saving the rule when the sensor is already active is not considered new motion. If the editor does not recognize `motion.detected` or `motion.cleared`, check their availability in your version of Home Assistant.

**Doesn't turn off:** Determine if the sensor stops detecting motion and maintains that state for the required duration. Also check if the light is not being turned on by another rule.

**Turns off when you are standing still:** The motion sensor may not recognize a stationary person. Extend the time or consider a presence sensor suitable for the specific room.

**What about sensor restart or failure?** The `for` wait does not survive a Home Assistant restart or automation reload. This simple example does not include a special branch for checking after system startup. Therefore, it does not guarantee that the light will match the sensor state after a failure; depending on the situation, the light may need to be controlled manually and allowed to complete a new motion cycle.

## Sources and further reading

- [Motion detected: motion.detected](https://www.home-assistant.io/triggers/motion.detected/)
- [Motion cleared: motion.cleared](https://www.home-assistant.io/triggers/motion.cleared/)
- [Automation triggers and their IDs](https://www.home-assistant.io/docs/automation/trigger/)
- [Choosing actions using choose](https://www.home-assistant.io/docs/scripts/#choose-a-group-of-actions)
- [Automation editor](https://www.home-assistant.io/docs/automation/editor/)
- [Simple evening lighting of the lamp](/guides/evening-lamp/)
