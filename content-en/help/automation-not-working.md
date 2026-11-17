---
title: "Automation not working: how to find out why"
description: "Find the problem in the trigger, condition, or action of a simple rule."
cas: "15–20 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Automation"
  - "Troubleshooting"
translationKey: "help.automation-not-working"
---

## Start with one rule

The light didn't turn on or the notification didn't arrive? Select one automation and write down what it was supposed to do and when. For example: "After the window has been open for ten minutes, a message should arrive on the mobile." Always change only one thing at a time to know which adjustment helped.

An automation has three parts: the **trigger** determines when the check starts, the **conditions** decide if it can proceed, and the **actions** state what must be done. Conditions are optional. If any main condition is not met, the actions will not execute.

## 1. Verify the device and target

First, try controlling the light manually from the dashboard. For notifications, send a message directly to the phone according to the [open window guide](/guides/open-window-alert/). If even manual control doesn't work, start by checking the device connection or mobile notifications.

In the rule, check the specific light or phone. Similar names can lead to selecting the wrong target. The action to turn on the light must target the light; a smart socket with a lamp might be treated as a switch.

## 2. Review the execution trace

In **Settings → Automations & Scenes**, open the rule and select **Traces**, which are the execution logs. On the smaller screen, this option may be in the menu. Select the run corresponding to the time of the problem and review the individual steps: what triggered the rule, which condition passed, and where it stopped.

Stopping due to an unmet condition might not be an error. A rule like "light only in the evening" has an action to deny execution during the day. Verify whether the condition matches your intention.

## 3. Distinguish between manual testing and actual triggering

Selecting **Run action** tests the sequence of actions, but it bypasses the triggers and main conditions. Conditions placed inside actions are still evaluated. Therefore, the success of this test does not confirm the entire rule. Actions are executed in reality, so for lights, also check the actual lamp.

Next, trigger a normal event: close and reopen the window, or set the time for a time-based rule several minutes into the future. Finally, restore the original settings. This way, you also test the path from the trigger.

## 4. When the rule doesn't run at all

Check that the automation is enabled and monitoring the correct sensor. A state trigger reacts to a change: an already open window is not a new opening. A transition must occur that you have set up.

If the trigger has a duration, the state must persist for the entire duration. Closing the window before the waiting limit will interrupt it. Restarting Home Assistant or reloading automations also cancels the waiting period. A missing message after a restart may therefore be due to this limitation.

## How to know it's fixed

Repeat the situation where the rule should function, as well as a situation where it should not function. For a window, try both a long open period and a short airing. Compare the actual result with the execution trace. Make a note of what you changed; this will be useful if the problem returns.

## Sources

- [Home Assistant: testing and execution traces](https://www.home-assistant.io/docs/automation/troubleshooting/)
- [Home Assistant: automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: state trigger and wait](https://www.home-assistant.io/triggers/state/)
- [Home Assistant: automation conditions](https://www.home-assistant.io/docs/automation/condition/)
- [Home Assistant: automation actions](https://www.home-assistant.io/docs/automation/action/)
