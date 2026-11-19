---
title: 'Areas and Floors: Brighten the Whole Living Room with One Command'
description: What Area means, how to divide a home into areas and floors, and how to control lights throughout an entire room.
cas: 15 minutes
obtiznost: Beginner
kontrola_zdroju: '2026-09-30'
stav: Based on documentation; YAML syntax verified
temata:
- Areas
- Floors
- Lighting
- YAML
translationKey: "guides.areas-and-floors"
---

## Why Divide the Home into Rooms

In the living room, you have a ceiling light, a lamp by the sofa, and a light strip behind the TV. You want to turn them all on at once. Instead of selecting each one separately, it is enough to enter: **turn on lights in the living room**.

If you add another lamp and assign it to the living room, the command for the lights in this room will include it too. You do not need to type it into the list of lights in the automation.

## What are Area and Floor

**Area means an area.** Think of it at home as a room: Living room, Kitchen, or Bedroom. An area can also be a patio or a garage.

**Floor means a floor level.** You assign rooms to a floor, and devices to the rooms. This means you don't have to assign every light individually to the ground floor.

The organization of a house might look like this:

| Floor | Room (Area) | Example devices |
| --- | --- | --- |
| Ground floor | Living room | Ceiling light, lamp, thermometer |
| Ground floor | Kitchen | Light above the table, water leak sensor |
| Ground floor | Downstairs hallway | Light, motion sensor |
| First floor | Bedroom | Bedside lamps, thermostat |
| First floor | Upstairs hallway | Light, motion sensor |

In an apartment, you can start just with rooms. Use the names you commonly use at home. For example, name two hallways **Downstairs hallway** and **Upstairs hallway** so they don't get confused when controlling them.

## Practical Benefits

When searching for devices, you start with rooms: "Where is the thermometer in the bedroom?" This same division helps when setting up the dashboard and automations.

For example, you might want to:

- Turn on lights in the hallway upon arrival.
- Turn off lights in the living room before going to sleep.
- Turn off lights on the ground floor when leaving.

Rooms and floors give you a common target for these commands. However, simply assigning devices does not create any automation. First, you organize the home, and then you set what should happen.

## Create Areas and Floors

1. Open **Settings → Areas, labels & zones**. In English, this is **Settings → Areas, labels & zones**; the Czech name may vary slightly depending on the translation.
2. If you have multiple floors, create floors, for example, **Ground floor** and **First floor**.
3. Create areas for individual rooms, for example, **Living room**, **Kitchen**, and **Bedroom**.
4. For each room, select its floor if you use one.

## Assigning Devices

In **Settings → Devices & Services → Devices**, open the device and select an area in its settings. In the device list, you can also select multiple items and move them to an area together.

Start with one room. Assign the ceiling light, lamp, and strip light to the living room. Check that you have not selected a similarly named light from the bedroom.

A single device can have multiple items, which Home Assistant calls an **entity**. For a light bulb, controlling the light is one of these entities. These items usually inherit the device's area. If a specific item has its own configured area, its own assignment will be used. This is useful, for example, for a device that controls lights in multiple rooms.

## Light up the living room without writing code

In the automation editor, add an action to **turn on the light**. As the target, select the **Living Room area**. You do not need to list individual lights.

The command will turn on available lights assigned to the living room. You will not turn on the thermometer or the TV: you selected the action for lights.

Want to light up only the lamp by the sofa? As the target, select the lamp directly. Use the area when you want to control lights in the entire room.

## Same example in YAML

This is **one action**, not an entire automation:

```yaml
action: light.turn_on
target:
  area_id: obyvak
```

`light.turn_on` means turn on the lights. `area_id` selects the room. The example value `obyvak` is the internal area ID, and you must replace it with the actual ID of your room.

**Do not guess the ID based on the name.** Select the area in the standard action editor, and then switch this action to YAML. Home Assistant will fill in the correct ID for you.

To turn off, use:

```yaml
action: light.turn_off
target:
  area_id: obyvak
```

Do you want to edit [motion-based automation](/guides/motion-activated-light/)? In both of its light actions, replace the target `entity_id: light.chodba` with the `area_id` using the actual ID of the hallway. Keep the specific sensor in the triggers. Motion will then turn on all lights in the hallway, and after the motion stops and the set delay expires, it will turn off.

## Socket-powered lamp: a small exception

A smart socket can be represented as a **switch** (`switch`), even if you have a lamp connected to it. The `light.turn_on` action will therefore not include it, even in the correct room.

For such a lamp, add a separate action to turn on the specific socket. Do not turn on all sockets in the room indiscriminately: there might be other appliances among them.

## Whole Floor Control

You can use rooms on the same floor as a common target, for example, to turn off the lights on the ground floor. In the corresponding action in the editor, select the floor as the target.

Floors are mainly useful in larger homes. For daily control, a room is often sufficient: when you go to sleep, you can turn off the living room and leave the kitchen lit, where someone might still be.

## Test the result

1. Check the light assignment in one room.
2. Run the action to turn on the lights using this room as the target.
3. Verify that the correct lights turn on and the lights in the adjacent room remain unchanged.
4. Test turning them off as well.

If some lights do not react? Try controlling them individually. Then check the device area and the entity itself to ensure it is listed as a light or a switch.

If you move a light to a different room, change its assignment. The commands for the new room will then include it. However, automations that control the light directly by its ID will continue to control it regardless of the room.

**Before deleting a room, check the rules that use it.** Automations referencing a deleted area need to update their target.

## Sources

- [Areas and device assignment](https://www.home-assistant.io/docs/organizing/areas/)
- [Floors](https://www.home-assistant.io/docs/organizing/floors/)
- [Selecting a room as an action target](https://www.home-assistant.io/docs/scripts/perform-actions/)
