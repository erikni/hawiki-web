---
title: "One Button for Evening Ambiance"
description: "Save the settings for several lights into a scene and trigger them from the dashboard."
cas: "20 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Scenes"
  - "Lighting"
translationKey: "guides.evening-scene"
---

## What will work in the end

With a single tap, you will turn off the main light and turn on the lamp in a way that suits your evening. You will save these settings as a **scene** named Evening Ambiance. A scene retains the desired states of selected devices; Home Assistant uses these when the scene is triggered.

You can run the scene manually. It does not determine the time or the trigger condition. If you later want to run it automatically, you will add it as an action to an automation.

## What you will need

A working Home Assistant, an administrator account, and two already connected lights. Try controlling them manually. For a lamp connected via a smart plug, you can use the switch on the plug, but the plug itself cannot set the brightness of a standard bulb.

Only set the dimming, colour, or colour temperature if the light and its integration support it. For the first scene, simply turning the lamp on and the main light off is enough.

## Save the evening settings

1. Open **Settings → Automations & Scenes**, navigate to the **Scenes** section, and select to add a new scene.
2. Name it **Evening Ambiance**. Add the specific entities for the main light and the lamp or its plug. Selecting individual entities gives you an overview of what you are including in the scene.
3. In the editor, set the main light as off and the lamp as on. For a supported lamp, also set a pleasant brightness, for example, 30%.
4. Save the scene. Button names may vary depending on the language and version.

When configuring in the editor, the actual lights may change. The editor documentation describes saving the desired states and restoring the previous settings when leaving. Therefore, only assess the result by triggering the saved scene independently.

## Add a button to the dashboard

Open your [home dashboard](/guides/home-dashboard/) and enable its editing mode. Add the built-in **Button** card and select the newly created scene as the entity.

In the tap action settings, select **Execute action**. Choose to activate the scene, labelled `scene.turn_on`, and set **Evening Ambiance** as the target. Give the button the same clear name and save it. This explicitly tells the system that tapping the button should run the scene.

## Test the actual result

Finish editing. Turn the main light and the lamp off so that the default state is different from the saved scene. Tap the new button and check both actual lights. For a dimmable lamp, also verify the brightness. Perform the same test in the mobile application.

If only the details open, check the tap action. If only one light reacts, manually check the other and ensure you included the correct entity in the scene. Make changes to the desired settings in the scene editor and then test the scene again.

## How to end the evening settings

A scene is not a regular switch and does not have an on or off state. Tapping it again will reuse the same settings; it will not revert to the previous state of the lights. Change the lights manually, or create a second scene, **Daytime Lighting**, with its own button.

## Sources

- [Home Assistant: scene editor](https://www.home-assistant.io/docs/scene/editor/)
- [Home Assistant: scenes and their activation](https://www.home-assistant.io/integrations/scene/)
- [Home Assistant: Button card](https://www.home-assistant.io/dashboards/button/)
- [Home Assistant: tap actions](https://www.home-assistant.io/dashboards/actions/)
- [Home Assistant: controlling lights](https://www.home-assistant.io/integrations/light/)
