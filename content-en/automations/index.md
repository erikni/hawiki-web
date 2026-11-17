---
type: hub
title: "Automations in Home Assistant"
seoTitle: "Automations in Home Assistant: Lights, Heating, and Alerts"
description: "Start with one rule and progress to lights, heating, or alerts. Choose a guide based on what you need at home."
kontrola_zdroju: "2026-10-08"
translationKey: "automations.index"
---

## From Idea to Simple Rule

An automation connects an event with a specific action. It can react to time, a change in device state, or other triggers. A condition specifies when the action should take place. For a first attempt, choose one need and one reliable device. You will track changes better than with a rule that immediately controls the entire house.

Start with a [light that turns on in the evening](/guides/evening-lamp/). Once the rule works, add other situations one by one. The prerequisite is a device added to Home Assistant and knowledge of its entity; the [guide to basic concepts](/getting-started/devices-entities-and-integrations/) will help.

## Lights, Motion, and Evening Mode

For walking through the hallway, the [motion-activated light](/guides/motion-activated-light/) is useful. For relaxation, try the [evening scene](/guides/evening-scene/), which unifies the desired state of multiple devices. A scene and an automation are not the same thing: a scene describes a state, while an automation determines when to trigger an action.

When dealing with lights, always consider regular manual control. The guide [smart light with a classic switch](/guides/smart-light-with-conventional-switch/) shows why it is important to start with specific connections and the needs of the household.

## Heating and Alerts

[Heating by mode](/guides/heating-by-mode/) helps with clear temperature switching. Before expanding the rule, verify how it behaves during manual changes and if it matches your normal routine. You can use alerts for an [open window](/guides/open-window-alert/) or [finished laundry](/guides/washing-machine-finished/).

Choose an alert that leads to a real action. First, try one message and a phone notification, then address repetitions. The goal is to help the household, not to create a long list of alerts.

## Energy and Other Triggers

To work with consumption, start with the [electricity overview](/guides/energy-dashboard/). Check available measurements and units before creating a rule based on them. Time, sun, presence, or calendar can be used later depending on needs; detailed guides for these scenarios will be added gradually.

## When the Rule Doesn't Work

Verify that the action works when triggered independently, and check the automation's history. Furthermore, follow the [guide to troubleshooting automations](/help/automation-not-working/). Before major changes, keep a [backup](/help/backups/).

## Sources

- [Home Assistant: Automation basics](https://www.home-assistant.io/docs/automation/basics/)
- [Home Assistant: Automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
