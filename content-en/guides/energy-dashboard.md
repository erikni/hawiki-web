---
title: "Energy Consumption Overview"
description: "Find out how much electricity the household and individual appliances consume using the Energy dashboard in Home Assistant."
cas: "20 minutes"
obtiznost: "Intermediate"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - electricity
  - consumption
  - Energy
  - YAML
translationKey: "guides.energy-dashboard"
---

How much electricity does a household consume per day, and which devices contribute to that consumption? Home Assistant can display data from meters in the **Energy** dashboard. Start with one available meter and gradually add more. Home Assistant itself does not measure consumption; you need a device or service that provides data via an integration.

## Power vs. Consumption

**W or kW** indicate the current power draw of a device. **Wh or kWh** express the energy consumed over a period of time. An appliance with a constant power draw of 1,000 W will consume 1 kWh in an hour. Therefore, a short peak does not necessarily mean high daily consumption.

For an overview over a day or month, use energy measurements. You can add the power draw next to it for a view of the current usage. If the device provides both readings, there is no need to calculate the energy.

## What Do You Want to Measure

Monitor the entire household using consumption readings from the grid, for example, from a compatible electricity meter. A single socket with measurement will only show the connected appliance. Therefore, do not enter its data as the entire household's consumption.

For a first attempt, use an already connected meter. If you are selecting a new one, verify the specific integration, energy measurement, and load capacity. Leave the connection of the meter to the distribution board to an electrician. This guide describes working with available data, not electrical installation.

## Adding to the Energy Dashboard

1. On the meter, verify the energy entity and its unit. Check that the data increases when consumption occurs.
2. Open **Settings → Dashboards → Energy** (Settings → Dashboards → Energy).
3. For total grid consumption, add the grid connection section and select the energy statistic drawn from the grid. Only add the feed back if you are actually measuring it.
4. Add measured appliances as individual devices. Do not add the same appliance twice under different names.
5. Save the settings and wait for the statistics to process. The initial data may not appear immediately.

The dashboard only contains compatible statistics. If a sensor is missing, verify the unit, support for long-term statistics, and that it is not excluded from recording. Simply renaming the unit from W to kWh will not fix the measurement.

## When You Only Have Power Draw

Home Assistant offers the **Integration** helper, which estimates energy from the power draw over time. It can be created in the UI among helpers or via YAML. The following example belongs in `configuration.yaml`; if you already have a `sensor:` section, only add the item under it.

The assumption is an existing power draw sensor with the unit W and the device class `power`. Replace `sensor.pracka_prikon` with your own ID, check the configuration, and restart Home Assistant.

```yaml
sensor:
  - platform: integration
    source: sensor.pracka_prikon
    name: Washing Machine Energy
    unit_prefix: k
    unit_time: h
    method: left
    round: 3
    max_sub_interval:
      minutes: 5
```

The result is an estimate in kWh. The `left` method is suitable for power draw that changes abruptly and holds the value between reports. Accuracy depends on the quality and frequency of the measurements. Find the new entity by name and add it as an individual device. If the integration offers its own energy measurement, prioritize it.

## How to Read the Dashboard

Compare the same intervals and let the measurements run for several days. The sum of several sockets does not cover unmeasured appliances. The price data based on a single tariff does not automatically include all items on the bill. The dashboard helps you find changes and large consumption; it does not organize electricity itself.

## Sources

- [Home Assistant: Energy management](https://www.home-assistant.io/docs/energy/)
- [Home Assistant: Adding grid consumption](https://www.home-assistant.io/docs/energy/electricity-grid/)
- [Home Assistant: Measuring individual devices](https://www.home-assistant.io/docs/energy/individual-devices/)
- [Home Assistant: Energy dashboard FAQ](https://www.home-assistant.io/docs/energy/faq/)
- [Home Assistant: Integration and converting power to energy](https://www.home-assistant.io/integrations/integration/)
