---
title: "Water Leak Warning Under Washing Machine"
description: "Receive a notification when the connected sensor detects water."
cas: "20 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Water leak"
  - "Notification"
translationKey: "guides.washing-machine-leak"
---

## What will work in the end

When the connected water leak sensor reports water, Home Assistant will send a notification to your phone. The message helps you determine that the area needs checking. This guide sets up the notification; automatic water shut-off requires additional devices and a separate procedure.

## What you will need

Prepare a functional Home Assistant setup, a connected water leak sensor, and a phone with the [Companion app installed](/getting-started/home-assistant-mobile-app/). Enable notifications. Connect and position the sensor according to the specific manufacturer's manual. This article does not select a specific model.

In Home Assistant, find the water detection entity. For a binary sensor of type **moisture**, `on` means wet and `off` means dry; the interface may display these states in text. Do not confuse it with an air humidity sensor, which shows percentages. Before creating the automation, verify exactly what your device offers.

## First, send a test notification

In **Settings → Tools → Actions**, search for the phone notification action. In older versions, this section might be under Developer Tools. The action name starts with `notify.mobile_app_` and continues with the device name. Enter the message "Water notification test" and run the action.

The message must arrive on the correct phone. If it does not, verify the internet connection, enabled notifications, and Do Not Disturb mode. The functional home control in the app itself does not yet verify message delivery.

## Create the automation without waiting

1. Open **Settings → Automations & Scenes** and create a new empty automation.
2. Add a **State** trigger and select the water detection entity. In the **To** field, enter `on`, or select the corresponding text state Wet. Leave the **From** field empty.
3. Do not set a duration or a wait action. The rule should react when the wet state is reported.
4. Add the tested phone notification action. The message can read: "Washing machine sensor reports water. Check the area."
5. Save the rule under the name **Washing Machine Water** and keep it enabled. Names may vary depending on the version and language.

Leaving the **From** field empty allows the reaction even if the sensor enters the wet state, for example, after restoring availability. However, this does not mean continuous monitoring: if it already has the wet state when the automation is created, a new transition may not occur, and the message will not send itself.

## Test the sensor and the entire automation

Test the detection only in the manner prescribed by the manufacturer in a safe location. Do not water the area under the connected washing machine. Monitor the state change in Home Assistant and the arrival of the message; then, according to the manual, return the sensor to a dry state. A test button may not represent the same test as water detection for every model.

Manually selecting **Run Action** verifies the message sending, but it does not verify the sensor or the trigger. If the physical test fails, check the [automation trace](/help/automation-not-working/) and verify the selected entity.

## What to expect from the notification

The automation does not send repeated reminders during a continuous wet state. Another change to wet may trigger another message. Delivery depends on the functional sensor, Home Assistant, and the notification path to the phone. Therefore, the notification does not replace checking the area or regularly verifying the sensor according to the manufacturer.

## Sources

- [Home Assistant: binary sensors and moisture state](https://www.home-assistant.io/integrations/binary_sensor/)
- [Home Assistant: state trigger](https://www.home-assistant.io/triggers/state/)
- [Companion: sending notifications](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
- [Home Assistant: notify action](https://www.home-assistant.io/integrations/notify/)
- [Home Assistant: automation troubleshooting](https://www.home-assistant.io/docs/automation/troubleshooting/)
