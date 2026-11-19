---
title: "Home Assistant on your phone: first steps"
description: "Connect your phone to your home and try your first control."
cas: "15 minutes"
obtiznost: "Beginner"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
translationKey: "getting-started.home-assistant-mobile-app"
temata:
  - "Mobile app"
  - "Getting started"
---

## What you will achieve

You will open your home's dashboard on your phone and try controlling a connected light. The official Home Assistant Companion app is available for Android and iPhone. Your phone connects to an existing Home Assistant installation; installing the app does not replace the system running in your home.

## What you will need

Have your phone and your Home Assistant username and password ready. For the first connection, join the same home Wi-Fi network as Home Assistant. First check that you can open its dashboard in your phone's browser. If you have not connected a light yet, you can still explore the dashboard and Settings.

## Connect your phone

1. Open the [official Mobile App integration page](https://www.home-assistant.io/integrations/mobile_app/), follow the link to Google Play or the App Store and install the app.
2. Launch the app and choose to connect to your own Home Assistant. Select the home it discovers. If it does not appear, manually enter the address that works in your phone's browser.
3. Sign in with your Home Assistant account. Give the phone a clear name, such as **Jan's phone**, so that you can recognise it later when configuring notifications.
4. Review the requested permissions and complete the setup wizard. Option names may differ by language, operating system and app version.

The **Mobile App** integration that provides this connection is enabled in a standard default configuration. In a typical installation, you therefore do not need to edit configuration files to use the app.

## Understand the permissions

Allow notifications if you want to receive messages from your home later. Sharing your location for automations is a separate choice. The app may also need location permission to recognise your home Wi-Fi because Android and iOS restrict access to network information.

If you use a local address beginning with `http://`, the wizard will offer a connection security level. Choose the recommended **Most secure** option and confirm your home network. The app will then permit an unencrypted connection only on that specified network. The documentation linked below explains the required permissions in detail.

## Test the result

Open the dashboard and turn on a connected light. Check the physical lamp, then turn it off again. Close and reopen the app. The connection is working if you return to your home and can still use the control. This test checks access while you are at home; notification delivery is covered in a separate guide.

## If your home does not open

Check the Wi-Fi connection and try the same address in your phone's browser. A guest network may block access to devices on your home network. If the app reports a security restriction, check the selected home network and the permissions needed to recognise it.

A working connection at home does not automatically provide access over mobile data. To connect while away from home, configure remote access separately, for example through Home Assistant Cloud or a VPN.

## Sources

- [Home Assistant – Mobile App integration](https://www.home-assistant.io/integrations/mobile_app/)
- [Home Assistant Companion – Getting started](https://companion.home-assistant.io/docs/getting_started/)
- [Home Assistant Companion – Connection security level](https://companion.home-assistant.io/docs/getting_started/connection-security-level/)
- [Home Assistant – Remote access](https://www.home-assistant.io/docs/configuration/remote/)
