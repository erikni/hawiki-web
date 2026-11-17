---
title: "Window Left Open: How to Receive an Alert"
description: "A mobile notification after a window has been open for ten minutes."
cas: "20 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Windows"
  - "Alerts"
  - "Automation"
translationKey: "guides.open-window-alert"
---

## What will work in the end

When a selected window remains open for ten minutes, Home Assistant will send a message to your phone. This reminder is useful when airing out the room, especially if you are busy with something else. We will set up the rule for one window and one mobile device so that it is easy to configure and control.

## What you will need

A working Home Assistant, an already connected window open/close sensor, and a phone with the [Companion app installed](/getting-started/home-assistant-mobile-app/). Enable notifications on the phone. The guide does not assume a specific sensor brand; its connection must be established beforehand.

First, open and close the window. The sensor's state must change accordingly in Home Assistant. For a standard binary sensor type window, the internal value `on` means open and `off` means closed. The overview may display this in text.

## First, test the message

Go to **Settings → Tools → Actions**; in older versions, this section might be under Developer Tools. Search for your phone's notification action. Its identifier starts with `notify.mobile_app_` and continues with the device name. Fill in the message "Household Alert Test" and run the action.

If the message does not arrive, check the notification permissions on your phone, the Do Not Disturb mode, and your internet connection. Before you start creating the rule, run this simple test. Controlling the household via the app and receiving the notification are two different checks.

## Create the rule

1. In **Settings → Automations & Scenes**, create a new empty automation.
2. Add a **State** trigger and select your window sensor. Set the transition from closed to open: **From** `off`, **To** `on`. The dropdown menu may show the words Closed and Open instead of these values.
3. In the duration field, labeled for example **For**, enter ten minutes (`00:10:00`). This is not a separate wait action: you set the duration directly in the trigger.
4. Add the same phone notification action that you already tested. The message can read: "The bedroom window has been open for ten minutes."
5. Save the rule as **Open Window in Bedroom** and keep it enabled. The names of the options may vary depending on the version and language.

## Verify actual opening

For the first test, shorten the duration to one minute. Close and then reopen the window. The message should arrive after one minute. Then check the second scenario: open and close the window within less than a minute. No message should arrive. Finally, restore the duration to ten minutes.

## What to expect from the rule

For one uninterrupted opening, it will send a single message. You will receive another only after closing, reopening, and the full duration having passed. After saving, the rule will not retroactively change a window that was already open; for testing, you must always close and reopen it.

The wait for the duration will be cancelled if Home Assistant restarts or if the automation is reloaded. Because of this simple procedure, it is not a guarantee of notification in every situation. If the message is missing, check the sensor state, the selected phone, and the automation trace log.

## Sources

- [Home Assistant: State trigger, for duration and reminder example](https://www.home-assistant.io/triggers/state/)
- [Home Assistant: Meaning of binary sensor states](https://www.home-assistant.io/integrations/binary_sensor/)
- [Companion: Sending notifications to the phone](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
- [Home Assistant: Notification action](https://www.home-assistant.io/integrations/notify/)
- [Home Assistant: Troubleshooting automation traces](https://www.home-assistant.io/docs/automation/troubleshooting/)
