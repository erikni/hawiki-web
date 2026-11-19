---
title: "Home Dashboard Overview"
description: "Create a simple control panel for lights, temperature, and window status."
cas: "20–30 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Home Dashboard"
  - "Dashboard"
translationKey: "guides.home-dashboard"
---

## What it will look like in the end

In Home Assistant, you will create a custom dashboard with several important elements: lights, temperature, and window status. The dashboard, also known as the overview, is used to display data and control your home. For this guide, you only need standard built-in cards and the visual editor.

## What you will need

Log in with administrator credentials. Prepare your already connected lights and optionally a temperature or window open/close sensor. Simply omit any missing items. First, verify that the devices work in the current overview. Clear names and [room assignment](../areas-and-floors/) will make selection easier.

Start with the top five items that you actually use every day. The goal is to quickly find controls and data, not to place every device on the first page.

## Create your own dashboard

1. Open **Settings → Dashboards** and select to add a dashboard. In English, this section is called **Dashboards**.
2. Select a new empty dashboard, for example, the option **New dashboard from scratch**. Name it **My Home** and enable sidebar visibility.
3. If the family needs to use it, do not restrict its visibility only to the administrator. Confirm the creation and open the dashboard.
4. In the top right corner, enable editing. Use the **Section** view for organisation; if it is already selected, leave it.

You manually edit the new dashboard. You will add cards for other devices later yourself. The names of the options may vary depending on the version and language of Home Assistant.

## Add three simple cards

In the first section, select **Add Card** and choose the **Tile** type. Select your light. Edit the displayed name, for example, to **Living Room Lamp**, and save the card.

In the same way, add a tile for the temperature sensor and then for the window sensor. Select the specific data point: for a device with multiple sensors, you need the temperature, not, for example, its battery status. Keep the visible status on the cards so you can recognise the measured value or the open window.

For lights, the tile differs between tapping the icon and tapping the rest of the card: the icon switches the light, and the rest of the card opens the details. The behaviour can be changed in the card's action settings. For a temperature sensor, tapping does not set a temperature; it is for displaying a measurement.

## Organise the screen

In the editing mode with the Section view, you can drag cards to other locations. Place the most frequently used light at the beginning. If you have multiple rooms, add another section and name its heading according to the room. For the first attempt, however, one section with three cards is enough.

## Verify the result on mobile

Finish the edits and open the dashboard in the [mobile app](../../getting-started/home-assistant-mobile-app/). Turn the actual light on and off. Open the window and verify the change in its status. Check that the names are readable even on a small screen.

If the family cannot see the dashboard, verify the visibility in the sidebar and the administrator restrictions. If the value is unavailable, check the relevant sensor in Home Assistant. The device card itself cannot fix it. Only add another item when you actually need it in daily use.

## Sources

- [Home Assistant: dashboards and visual editing](https://www.home-assistant.io/dashboards/)
- [Home Assistant: creating a custom dashboard](https://www.home-assistant.io/dashboards/dashboards/)
- [Home Assistant: tiles and their actions](https://www.home-assistant.io/dashboards/tile/)
- [Home Assistant: sections and card moving](https://www.home-assistant.io/dashboards/sections/)
