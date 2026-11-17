---
title: "A lamp that turns on by itself in the evening"
description: "You can set up your first simple rule by clicking."
obrazek: "/assets/images/lampa-vecer.png"
obrazek_alt: "Evening living room with an automatically lit lamp, clocks showing 19:00, and a phone with a time zone setting."
cas: "20 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-09-30"
stav: "Based on documentation"
temata:
  - "Lighting"
  - "Automation"
translationKey: "guides.evening-lamp"
---

## What will work in the end
Every day at 19:00, the selected lamp will turn on. You can adjust the time later to suit your needs.

## What you need
A working Home Assistant and a connected lamp or a supported smart plug with a lamp. First, verify that you can manually turn it on from the dashboard. The plug must have the lamp's regular switch turned on.

## Steps
1. Open **Settings → Automations & Scenes**.
2. Select to create a new automation and start with an empty rule.
3. Add a **Time** trigger and set it to `19:00:00`.
4. Add an 'on' action. For a smart bulb, select turning on the light; for a plug, select turning on the switch.
5. As the target, select your lamp or plug.
6. Save the rule under the name **Evening lamp**.

Button names may vary slightly depending on the language and version. A trigger means "when something happens," and an action means "what the home should do."

## Test the result
First, run the rule's action manually. Then, set the time a few minutes into the future, turn off the lamp, and wait. This will also verify the time-based triggering. Finally, reset it to 19:00.

## If the lamp doesn't turn on
Check if manual control works, if the correct target is selected, and if the rule is enabled. Also, verify the home's time zone.

## What you can add
A second similar rule can turn the lamp off in the evening. Start with a simple fixed time and only consider presence-based conditions afterwards.

## Sources
- [Official automation editor](https://www.home-assistant.io/docs/automation/editor/)
