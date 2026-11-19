---
title: "What works when the internet goes down?"
description: "Differentiate between local and cloud functions and test your own home."
cas: "20 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "Internet"
  - "Local control"
translationKey: "help.internet-outage"
---

## Internet and the home network are not the same

Home Assistant runs at home and prioritises local control. However, this does not mean that every connected device functions without the internet. It depends on the integrated component and whether the automation retrieves data locally or sends commands remotely.

An internet outage is not the same as turning off the router. The home Wi-Fi and the connection between devices can continue to work even if the internet is unavailable. For the following test, leave Home Assistant, the router, access points, and necessary gateways powered on.

## Which functions can continue

Local light control can function if Home Assistant communicates directly with the device or a local gateway. An example is connecting Zigbee devices via ZHA or controlling them via Matter. The relevant hardware and network must still be operational.

Automations have a chance of continuing if all necessary components are local: the trigger, conditions, and actions. A motion sensor and locally controlled lights can continue to work together. However, if a rule waits for data from an internet service, the local light alone will not guarantee the correct result.

## Where to expect limitations

Cloud-dependent integrations cannot retrieve new data or send commands via the manufacturer's service during an outage. New weather forecasts or remote access to the home also require the internet. Remote access via Home Assistant Cloud or VPN will not bypass the lack of home internet connection.

Check phone notifications separately. Common push messages use internet services; there are also special options for local delivery, but these cannot be assumed for every setup. The fact that a light turned on does not confirm the delivery of a water leak notification under the washing machine.

## What you learn from the integration documentation

On the specific integration page, look for the **IoT class** designation. The **Local Push** and **Local Polling** values describe local communication, while **Cloud Push** and **Cloud Polling** describe communication via the cloud. Push means sending changes, and polling means regular querying.

Take this as a guide, not a guarantee for the entire home. You should also check the product requirements and other functions you use. The mere designation of Wi-Fi does not determine if a device is cloud-dependent; the [overview of networks and Matter](/buying-guide/zigbee-wifi-thread-matter/) explains this better.

## Try a simple scenario

1. Select one light and a simple rule, such as turning on based on motion. Verify the actual result under normal connection.
2. On a phone connected to the home Wi-Fi, open the local address of Home Assistant. First, verify that it works without using the remote address.
3. According to the router's manual, temporarily disconnect only the internet connection. Do not disconnect the router's power or the cable connecting Home Assistant to the home network. Note how you will restore the connection.
4. On the phone, turn off mobile data, leave Wi-Fi on, and repeat manual control and the actual triggering of the rule. Also check for new changes in sensor states, not just old values on the screen.
5. Reconnect the internet, turn mobile data back on, and verify the restoration of cloud functions.

Perform the test at a time when a short disconnection will not disrupt necessary home services. If you do not know which cable or option to use, first verify the procedure in your router's manual.

## Record the result

Note what worked, what stopped responding, and what was restored after the internet returned. This gives you an overview of your own setup. For important tasks, keep manual control available, and repeat the relevant test after changing devices or integrations.

## Sources

- [Home Assistant: local processing and control](https://www.home-assistant.io/)
- [Home Assistant: classifying the internet of things](https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things/)
- [Home Assistant: ZHA integration](https://www.home-assistant.io/integrations/zha/)
- [Home Assistant: Matter local control](https://www.home-assistant.io/integrations/matter/)
- [Home Assistant: remote access](https://www.home-assistant.io/docs/configuration/remote/)
- [Companion: phone notifications](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
- [Companion: local delivery and its limitations](https://companion.home-assistant.io/docs/notifications/notification-local/)
