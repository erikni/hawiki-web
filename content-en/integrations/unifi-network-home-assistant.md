---
title: 'UniFi Network in Home Assistant: clients, VLANs, and presence'
seoTitle: 'UniFi Network and Home Assistant: local monitoring and automation'
description: 'A practical guide to connecting UniFi Network with Home Assistant: local account, permissions, clients, APs, VLANs, and presence detection.'
cas: 18 minutes read
obtiznost: Intermediate
kontrola_zdroju: '2026-11-13'
stav: Based on documentation
sourceType: official-docs
obrazek: /assets/images/unifi-network-home-assistant.png
obrazek_alt: Local network with a gateway, switch, access points, two VLANs, and smart home monitoring
temata:
- UniFi Network
- Integration
- Local network
- VLAN
- Presence detection
related:
- guides/unifi-access
- getting-started/devices-entities-and-integrations
- help/automation-not-working
- help/internet-outage
translationKey: "integrations.unifi-network-home-assistant"
---

The official **UniFi Network** integration connects Home Assistant to the UniFi Network application. It can monitor access points, switches, gateways, and connected clients. The phone can be used for presence detection, and for network elements, it can monitor status and utilization, and with appropriate authorization, for example, disable a Wi-Fi network or control a PoE port.

This is a different integration from **UniFi Protect** for cameras and **UniFi Access** for door systems. HACS is not required. The guide is verified according to the documentation, not physical testing of a specific setup.

## How the connection works

Home Assistant communicates directly with the UniFi Network application on the local network. Changes to clients, devices, and configurations are received via a local WebSocket, meaning they are continuous and do not require regular interval polling. If the connection is interrupted, it will attempt to reconnect; until then, entities may be unavailable.

The Ubiquiti SSO cloud account for integrating is not sufficient. In the console, you must create a separate **local user**. This way, client data does not have to pass through the cloud via Home Assistant; however, UniFi remote access and other services can still use the cloud according to your settings.

The integration supports both the UniFi OS console and standalone Network Application. Early Access and Release Candidate are not supported.

## What you will need

- a functional UniFi Network application and at least one managed network device,
- a stable version of UniFi Network and optionally UniFi OS,
- a local address or DNS name for the controller, usually port `443`,
- a separate local username and strong password for Home Assistant,
- a network path from Home Assistant to the controller,
- the correct time on both systems, ideally via NTP.

Home Assistant does not need to be on the same VLAN as the phones or AP. However, it must be able to reach the UniFi Network application. Integration rules between segments do not bypass this, and VLANs do not create it.

## 1. Creating a Local Account

On the UniFi OS console, open user management **People** and create a new administrator restricted to local access. According to current Home Assistant documentation:

1. select **Create New**, fill in the name, username, and password,
2. enable the administrator account and **Restrict to local access only**,
3. disable the default role,
4. set the permission to **Network: Full Management**,
5. leave **None** for **OS Settings**.

The Network application also provides full access via a control entity. However, this is not always necessary: a limited account integration will create fewer entities and may offer only sensors instead of some switches. For security reasons, therefore, first decide whether you only require monitoring or also network changes. Do not use the console owner's personal account.

With a standalone Network Application, the names of the offerings may vary. You still need a local account that can log in directly to the specific application.

## 2. Adding the Integration

1. In Home Assistant, open **Settings → Devices & Services**.
2. Select **Add integration** and search for **UniFi Network**.
3. Enter the local controller address, username, password, and port. The default port is `443`.
4. Keep SSL verification enabled. Only disable it for your own certificate in a trusted local network, and only after considering the risk.
5. If the controller manages multiple sites, select the correct **Site ID**.
6. Once finished, open the integration's devices and entities to verify what your account has actually exposed.

Settings are entirely within the interface; do not configure the integration in `configuration.yaml`.

## Clients, Access Points, and Sensors

In **Settings → Devices & Services → UniFi Network → Configure**, you can specify what should be monitored. Important options include:

- creating `device_tracker` entities for network clients,
- including wired clients,
- monitoring UniFi devices, such as APs and switches,
- limiting the monitoring of wireless clients to selected SSIDs,
- the time since the last appearance in an away state; the default is 300 seconds,
- ignoring clients with random private MAC addresses,
- selecting specific clients for which entities should be created,
- optional throughput and uptime sensors.

Depending on the device and permissions, status, load, temperature, throughput, or port speed sensors, and firmware update entities can be created. Full permissions can add restart, PoE power cycle, and port switch functionality, as well as Wi-Fi or regular operation. Some entities are disabled by default.

Names such as `device_tracker.telefon_anna` or `switch.wifi_hoste` are only examples. You will always find the actual IDs on the entity page.

## VLANs: Avoiding Unnecessary Issues

VLANs divide the physical network into separate logical segments, such as home, guest, and IoT. The gateway and firewall manage the transfer between them.

Two distinct paths are important for integration:

1. Home Assistant must connect to the UniFi Network application.
2. Network clients and UniFi devices must be managed correctly by the controller itself.

Home Assistant does not require direct access to every IoT client just for display within the integration. If the controller is in the management VLAN, allow the connection to its specific address and port, not the entire segment.

An SSID can be assigned to a specific VLAN. This must be enabled on the trunk between the switch and the AP; handle this configuration in UniFi Network.

## Example 1: Light when the phone arrives

For the first few days, monitor presence detection without critical actions. On the phone for the home Wi-Fi, disable the random MAC address or set a static private address so the UniFi device recognizes it every time. In Home Assistant, replace the tracker and light with actual entities. Insert the entire block into the YAML editor of a new automation.

```yaml
alias: UniFi – Light upon returning home
triggers:
  - trigger: state
    entity_id: device_tracker.telefon_anna
    from: "not_home"
    to: "home"
conditions:
  - condition: state
    entity_id: sun.sun
    state: "below_horizon"
actions:
  - action: light.turn_on
    target:
      entity_id: light.predsin
mode: single
```

The trigger is the phone changing state to home. The condition allows the light to turn on only after sunset. A failure of the phone, Wi-Fi, or controller can distort the state, so do not use the network tracker itself for unlocking doors or disabling security.

## Example 2: Time-based Guest Wi-Fi

This example requires a WLAN switch that is only visible with the appropriate account permissions. Turning off the Wi-Fi triggers a new configuration of the affected APs and disconnects clients. Replace `switch.wifi_hoste` with your actual entity and paste the entire block into the YAML editor of a new automation.

```yaml
alias: UniFi – night guest Wi-Fi schedule
triggers:
  - trigger: time
    at: "23:00:00"
    id: noc
  - trigger: time
    at: "07:00:00"
    id: rano
conditions: []
actions:
  - choose:
      - conditions:
          - condition: trigger
            id: noc
        sequence:
          - action: switch.turn_off
            target:
              entity_id: switch.wifi_hoste
      - conditions:
          - condition: trigger
            id: rano
        sequence:
          - action: switch.turn_on
            target:
              entity_id: switch.wifi_hoste
mode: single
```

The two time triggers have their own IDs. The `noc` branch turns off the network, and the `rano` branch turns it back on. Before activating the plan, ensure that no devices are needed on the specified WLAN overnight.

## Presence Detection: Common Limitations

Phones can change their MAC address for every Wi-Fi network. This creates new client records, and the original tracker may not return home. Only change settings for your own trusted SSID; global privacy protection disabling is not necessary. The integration can also ignore random addresses.

If the phone remains at home even after leaving, check the client status directly in UniFi. The documentation warns that some versions may have disconnection issues with **802.11r Fast Roaming**. Also check the time synchronization between Home Assistant and the router, and appropriately set the "last seen" delay. A shorter delay reacts faster but increases the risk of false departure during a brief Wi-Fi outage.

For important automations, combine network presence with another source. The `home` status means the client is connected, not that the person's identity has been verified.

## When the integration fails

- **Login rejected:** use a local account, not Ubiquiti SSO; verify the password with a direct local login.
- **Cannot connect:** verify the controller address, port, DNS, firewall, and VLAN routing from Home Assistant.
- **Certificate error:** use a valid certificate or a correctly trusted internal authority. Disabling SSL inspection is a last resort.
- **Switches and buttons are missing:** the account does not have the necessary permissions, or the entity is disabled by default. Restricted accounts often only receive sensors.
- **Client has no tracker:** enable client tracking, check the SSID filter, and the list of selected clients. For random MAC, set a static address for the home network.
- **Phone stays at home:** compare the status in UniFi, synchronize the time, consider disabling 802.11r, and adjust the delay.
- **Entities are unavailable:** check the status of the Network application and WebSocket connection; the integration will attempt to reconnect automatically after recovery.
- **Stale entities remain:** the client or device must first be removed from UniFi and unknown upon starting or reloading the integration; then the record can be deleted in Home Assistant.

For detailed logging, you can add the following block to `configuration.yaml` and restart Home Assistant. Use this only for diagnostics, as the log can grow quickly.

```yaml
logger:
  default: info
  logs:
    aiounifi: debug
    homeassistant.components.unifi: debug
```

## Pros, Cons, and Security

The advantage is a local push connection, an overview of clients and network elements, and the ability to use their states in automations without installing agents.

The disadvantage is sensitivity to API changes between UniFi versions, the requirement for a local account, and presence limitations based on phone behaviour. Control entities can change the network, PoE, and firewall rules; therefore, a faulty automation could disconnect a device or user.

Store the account password only in Home Assistant. Use the lowest functional permissions for monitoring. Only enable full access when you truly need control, and test changes to WLAN, ports, or rules manually first. The integration does not replace UniFi configuration backups or availability monitoring from an independent system.

## Sources

- [Home Assistant: UniFi Network integration](https://www.home-assistant.io/integrations/unifi/)
- [Ubiquiti: UniFi Network local API application](https://help.ui.com/hc/en-us/articles/30076656117655-Getting-Started-with-the-Official-UniFi-API)
- [Ubiquiti: VLAN for security and performance](https://help.ui.com/hc/en-us/articles/26136851868695-Using-VLANs-for-Network-Security-and-Performance)
- [Ubiquiti: assigning VLAN to Wi-Fi SSID](https://help.ui.com/hc/en-us/articles/26136823938583-Creating-UniFi-WiFi-SSIDs)
- [Home Assistant: automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
