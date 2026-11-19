---
title: "Device Not Responding. What Now?"
description: "Start with the simplest checks."
cas: "10 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-09-30"
stav: "Based on documentation"
temata:
  - "Smart devices"
  - "Troubleshooting"
translationKey: "help.device-not-responding"
---

## First, determine the scope of the problem
Is one device failing, or is the entire home affected? If you open Home Assistant and other devices are responding, start with the specific product.

## Check the basics
1. Does the device have power or a charged battery?
2. Was the light disconnected by a regular switch?
3. Does the control work directly on the device?
4. For cloud-dependent devices, is the internet and the manufacturer's service working?
5. Has there been a recent change to the Wi-Fi or router?

## Check the connection
In **Settings → Devices & Services**, open the relevant integration. Read any error messages. The next steps depend on the specific connection; use its documentation.

## Do not delete the device as a first step
Removing and re-adding can change bindings for your automations. First, note the error and check common causes.

## What to prepare when asking for help
The exact model, connection method, Home Assistant version, error text, and information on what changed before the problem occurred. Do not share passwords or access tokens.

## Sources
- [Official help with installation troubleshooting](https://www.home-assistant.io/installation/troubleshooting/)
