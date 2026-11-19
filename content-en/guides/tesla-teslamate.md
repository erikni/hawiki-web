---
title: 'Tesla and Home Assistant: TeslaMate, Automations, and BLE Control'
description: Installing TeslaMate, automation examples, and Bluetooth control via Teslemetry from Home Assistant 2026.10.
obrazek: /assets/images/tesla-teslamate.png
obrazek_alt: Illustration of an electric car connected to a home server and showing battery and charging status.
cas: 15 minutes read
obtiznost: Advanced
kontrola_zdroju: '2026-10-14'
stav: Based on documentation
temata:
- Tesla
- TeslaMate
- MQTT
- Automation
- Teslemetry
- Bluetooth
translationKey: "guides.tesla-teslamate"
---

## What TeslaMate brings to the smart home
**TeslaMate** is a community open-source project for recording Tesla data. It stores driving and charging history in its own database. Dashboards in Grafana help track consumption, charging cycles, and vehicle behavior over time. It provides data to Home Assistant via **MQTT**: a service that delivers messages between applications.

On the HA dashboard, you can have the battery level, estimated range, charging status, cable connection, location, temperature, or open windows. Availability depends on the data provided by your car. From these values, you can create home notifications or automations, such as turning on the driveway lighting. Grafana is used for detailed history, HA for the general overview and automations.

**Having its own database does not mean acquiring data without the internet.** TeslaMate communicates with Tesla services. It provides data for reading via MQTT; this connection alone will not activate the air conditioning, change the charging current, or unlock the car. For such commands, you need another method, such as Tesla Fleet, Teslemetry, or a controllable wallbox.

## Which approach to choose
| Solution | What you get | What you need |
| --- | --- | --- |
| TeslaMate + MQTT | Own history and data for automation | Server, Docker, MQTT, and internet |
| Tesla Fleet | Cloud tracking and control of the car | Tesla account, developer application, public key, and API setup |
| Teslemetry with BLE from HA 2026.10 | Supported commands locally via Bluetooth, cloud as backup | Subscription, Bluetooth within range of the car, and paired key |

TeslaMate can remain the source of history, and other integrations provide control. In HA, you can then see several entities for the battery or air conditioning. Name them according to the source, and in every automation, select the specific entity. To start, we recommend enabling data reading and initial notifications; add control later.

## Preparation for TeslaMate
You need a continuously running computer or NAS with Docker and Docker Compose, a Tesla account, and internet access. The documentation specifies a minimum of 1 GB RAM, recommending 2 GB. It supports 64-bit platforms amd64 and aarch64; older 32-bit Raspberry Pi installations are insufficient. The procedure below installs separate containers alongside HA, not the application directly into HA OS.

First, prepare an **MQTT broker**. In HA OS, you can use the Mosquitto broker add-on and a separate user for TeslaMate. In Settings → Devices & Services, set up the MQTT integration. For other HA installations, use your own broker. Both Home Assistant and TeslaMate must connect to the same broker; two separate brokers will not automatically pass messages.

## Installation in Docker
The following configuration is based on the TeslaMate Docker guide and uses your existing HA broker. Therefore, it does not include a second Mosquitto. It assumes a new database installation; do not switch an existing database to a different major PostgreSQL version without a migration process.

On the server, create a directory named `teslamate`. In the `.env` file within this directory, paste the following:

```dotenv
TM_DB_PASSWORD=REPLACE_WITH_STRONG_PASSWORD
TM_ENCRYPTION_KEY=REPLACE_WITH_LONG_RANDOM_KEY
TM_MQTT_HOST=192.168.1.10
TM_MQTT_USER=teslamate
TM_MQTT_PASSWORD=REPLACE_WITH_MQTT_USERNAME_PASSWORD
```

Replace all placeholder values. Change the IP address to the broker address accessible from the Docker server, and the username and password to those of its user. Use different long random values for the database and encryption, for example, from a password manager. The `.env` file contains sensitive data: do not publish it and keep a safe copy of the encryption key.

Next to it, create `docker-compose.yml` with the entire content:

```yaml
services:
  teslamate:
    image: teslamate/teslamate:4.3.0
    restart: unless-stopped
    environment:
      ENCRYPTION_KEY: ${TM_ENCRYPTION_KEY}
      DATABASE_USER: teslamate
      DATABASE_PASS: ${TM_DB_PASSWORD}
      DATABASE_NAME: teslamate
      DATABASE_HOST: database
      MQTT_HOST: ${TM_MQTT_HOST}
      MQTT_USERNAME: ${TM_MQTT_USER}
      MQTT_PASSWORD: ${TM_MQTT_PASSWORD}
      MQTT_HOME_ASSISTANT_DISCOVERY: "true"
      TZ: Europe/Prague
    ports:
      - "4000:4000"
    volumes:
      - ./import:/opt/app/import
    cap_drop:
      - ALL
  database:
    image: postgres:18-trixie
    restart: unless-stopped
    environment:
      POSTGRES_USER: teslamate
      POSTGRES_PASSWORD: ${TM_DB_PASSWORD}
      POSTGRES_DB: teslamate
    volumes:
      - teslamate-db:/var/lib/postgresql
  grafana:
    image: teslamate/grafana:4.3.0
    restart: unless-stopped
    environment:
      DATABASE_USER: teslamate
      DATABASE_PASS: ${TM_DB_PASSWORD}
      DATABASE_NAME: teslamate
      DATABASE_HOST: database
    ports:
      - "3000:3000"
    volumes:
      - teslamate-grafana:/var/lib/grafana
volumes:
  teslamate-db:
  teslamate-grafana:
```

In the directory, run `docker compose config` to check the configuration, and then `docker compose up -d`. The first command may output passwords, so do not share its output. The example assumes the standard MQTT port 1883 on a trusted home network. For connection over an untrusted network, set up TLS according to the broker and TeslaMate documentation.

Open TeslaMate at `http://IP_SERVER:4000`. According to its documentation on tokens, you will obtain an access and refresh token and enter them on the login page. These are credentials for an account; do not include them in articles, screenshots, or public configurations. In Grafana at `http://IP_SERVER:3000`, use the initial login `admin` / `admin` and change the password. Set the application and graph addresses in TeslaMate. Do not expose ports 3000 and 4000 directly to the internet.

## Connection to HA and Initial Check
The variable `MQTT_HOME_ASSISTANT_DISCOVERY` enables automatic entity creation via MQTT discovery. After the first data points from the car, the MQTT integration should display the TeslaMate device and its entities. You do not need to add another integration named TeslaMate or install HACS. For multiple cars, verify which vehicle each entity belongs to.

In the device details, check the battery and charging against the Tesla app. Note down the actual entity IDs. Older installations may use manual `mqtt_sensors.yaml`; do not leave manual definitions of the same entities active alongside discovery. When migrating from older versions, read the update notes: preserving entity names and settings may not be automatic.

If data is missing, check `docker compose ps` and `docker compose logs --tail=50 teslamate`, the MQTT broker IP, and the login credentials. In the MQTT integration, you can listen to the topic `teslamate/cars/1/#`; replace the number 1 with the car's ID if it is different. When messages arrive but entities are missing, verify discovery and its prefix. Before sharing logs, check for location and other personal data.

## What's New in Home Assistant 2026.10: BLE Control
The **2026.10** release added local vehicle control via Bluetooth Low Energy, or BLE, to the **Teslemetry** integration. This is neither a new feature for TeslaMate nor an automatic extension for Tesla Fleet. Teslemetry still requires an account with an active subscription. The new local capability is particularly useful for cars parked at home, for example, in a garage with a weak mobile signal.

The command for a paired vehicle within range will attempt to pass through Bluetooth. If a local connection is unavailable or the command fails, the integration will use the cloud. Therefore, the same automation can still utilize cloud control when away from home. Supported features include, for example, air conditioning, charging, charging current, or the lock, depending on the vehicle's available entities.

**States in this integration are still read via the cloud or the Teslemetry data stream.** BLE here is used for sending commands. A successfully sent local command therefore may not immediately bring an updated state in HA during an internet outage. This is not a replacement for TeslaMate, nor is it a guarantee of a fully offline vehicle overview.

## Bluetooth Hardware and Pairing
Home Assistant must have an available Bluetooth adapter or a **Bluetooth proxy** within range of the car. A proxy is a small node, for example using ESPHome, that relays Bluetooth over the home network from the garage. It is not enough merely to receive broadcasted data; it requires support for active BLE connections. In ESPHome, check the supported platform and the `bluetooth_proxy` settings; active connections are different from active scanning.

Test the range in an actual parking spot, even with closed gates. Do not rely on a guaranteed distance. The car must support the Tesla command protocol; some Model S and X before 2021 do not offer this capability. Also prepare the car's authorized key card.

1. Update HA to the fixed release series 2026.10.x and verify functional Bluetooth integration.
2. Add **Teslemetry** in Settings → Devices & Services, log in the account, and complete its standard setup, including the required virtual key.
3. In the integration, select **Add local vehicle** or add a local vehicle and choose the car.
4. Let HA search for the vehicle within range. Limit other simultaneous phone Bluetooth connections; there should not be three or more phone keys nearby during pairing.
5. When the wizard asks for HA key authorization, confirm the step and hold the card to the central console reader for approximately 30 seconds. If the time expires, repeat the step.
6. Test a simple command, such as flashing the lights, and only then add the automation.

The key for Bluetooth in HA is another authorization within the car. Removing the pairing or integration from HA will not remove this key from the vehicle. To completely revoke access, also remove it on the car's display in **Controls → Locks**, i.e., in the key list, and confirm with the authorized card as prompted.

## Example 1: Notification of charging completion
In the new automation, open **Edit in YAML** and paste the entire example. Replace `sensor.tesla_charging_state` with the MQTT sensor ID from TeslaMate. In the Developer Tools, verify that its actual values are `Charging` and `Complete`. The message will appear in HA notifications; for a phone, you would use your mobile notification service instead.

```yaml
alias: Tesla – charging complete
triggers:
  - platform: state
    entity_id: sensor.tesla_charging_state
    from: "Charging"
    to: "Complete"
conditions: []
actions:
  - service: persistent_notification.create
    data:
      title: "Tesla"
      message: "Charging has reached the set limit."
mode: single
```

The example reacts to a specific state transition. Simply connecting the cable or restoring values after a restart will not trigger it. If the transfer skips the `Charging` state, the notification will not be received; this is a simple basic example, not monitoring every charging cycle.

## Example 2: Morning air conditioning via Teslemetry
This example assumes that Teslemetry, paired BLE, and its controllable air conditioning unit are functional. In a new automation, paste the entire YAML. Replace both IDs: the location entity from TeslaMate and the air conditioning unit from Teslemetry. Adjust the time according to your departure schedule. The example for weekdays will only turn on the air conditioning when the location entity reports `home`.

```yaml
alias: Tesla – preparation before morning departure
triggers:
  - trigger: time
    at: "07:15:00"
conditions:
  - condition: time
    weekday: [mon, tue, wed, thu, fri]
  - condition: state
    entity_id: device_tracker.tesla_location
    state: "home"
actions:
  - action: climate.turn_on
    target:
      entity_id: climate.tesla_teslemetry
mode: single
```

Calling the entity itself does not exclusively enforce BLE. Teslemetry selects the available path and may switch to the cloud. The location from TeslaMate may also be outdated; for more reliable operation, supplement this with vehicle presence checks and custom battery status rules. The time-based automation will not know that you planned your departure in the morning.

## Other useful automations
**Charging from photovoltaics:** Combine the actual surplus measured at the utility connection with the battery state and the cable connection. The panel power itself is not the surplus, as part of it is consumed by the house. Commands are needed to control a smart wallbox or a car integration, such as Teslemetry with BLE. Set the minimum and maximum current according to the device, the delay, and a different threshold for turning on and off, so that charging does not flicker with every cloud.

**Arriving home:** The car's location can only illuminate the driveway after dark. For lighting, the delay is usually more tolerable than for gates. Do not rely on automatic home unlocking solely on location or Bluetooth capture; both pieces of information may be delayed or unavailable.

**Forgotten cables and windows:** In the evening, check if the car is home, the battery is under your threshold, and the cable is disconnected. Or combine the open window data with rain. Start with a notification; adding closing or other controls should wait for verified support and the specific car's conditions.

## Operation, Backups, and Troubleshooting
TeslaMate accounts for the car going to sleep. During sleep or connection interruptions, values may remain the last known; `unknown` and `unavailable` do not mean zero battery or confirmation that the vehicle is at home. Multiple concurrently used applications can affect sleep functionality. Do not enable frequent wake-ups just for a more recent number on the dashboard.

For BLE issues, start with range, functional proxies, and available connections. If the car is not listed, verify compatibility and ensure it has not already been added. For failed authorization, repeat the card application according to the guide. Fixes in series 2026.10.x also address pairing and searching; check the changelog before complex interventions.

HA itself does not automatically back up the database on a separate Docker server. Back up PostgreSQL using the TeslaMate procedure, along with the configuration and encryption key. Docker volumes retain data between normal restarts, but they are not a backup. Before updating, read the release notes, and always separate the application update from the main PostgreSQL version migration when backing up the database.

## Sources
- [TeslaMate: installation in Docker](https://docs.teslamate.org/docs/installation/docker/)
- [TeslaMate: integration with Home Assistant](https://docs.teslamate.org/docs/integrations/home_assistant/)
- [TeslaMate: environment variables](https://docs.teslamate.org/docs/configuration/environment_variables/)
- [TeslaMate: MQTT data](https://docs.teslamate.org/docs/integrations/mqtt/)
- [Home Assistant: MQTT](https://www.home-assistant.io/integrations/mqtt/)
- [Home Assistant: Tesla Fleet](https://www.home-assistant.io/integrations/tesla_fleet/)
- [Home Assistant: automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant 2026.10: new features](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [Home Assistant: Teslemetry and Bluetooth control](https://www.home-assistant.io/integrations/teslemetry/)
- [Home Assistant: pairing Teslemetry in version 2026.10.1](https://github.com/home-assistant/core/blob/2026.10.1/homeassistant/components/teslemetry/config_flow.py)
- [Home Assistant: Bluetooth](https://www.home-assistant.io/integrations/bluetooth/)
- [ESPHome: Bluetooth proxy](https://esphome.io/components/bluetooth_proxy/)
- [Home Assistant: climate control](https://www.home-assistant.io/integrations/climate/)
- [Home Assistant: notifications](https://www.home-assistant.io/integrations/persistent_notification/)
- [Home Assistant 2026.10: changelog](https://www.home-assistant.io/changelogs/core-2026.10)
- [TeslaMate: version 4.3.0](https://github.com/teslamate-org/teslamate/releases/tag/v4.3.0)
- [TeslaMate: dashboards in Grafana](https://docs.teslamate.org/docs/screenshots/)
- [TeslaMate: sleep and FAQ](https://docs.teslamate.org/docs/faq/)
- [TeslaMate: database backups](https://docs.teslamate.org/docs/maintenance/backup/)
