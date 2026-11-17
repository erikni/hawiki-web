---
title: "How to Control Your Home Remotely"
description: "Enable remote access via Home Assistant Cloud, verify the connection, and secure your account."
cas: "20 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - remote access
  - Home Assistant Cloud
  - security
translationKey: "guides.remote-access"
---

Do you want to check the temperature or see if a light is left on from work? Home Assistant is available in the local network by default. To connect from elsewhere, you need an additional method of access. Simply installing the mobile application is not enough.

## Which Method to Choose

For beginners, **Home Assistant Cloud** from Nabu Casa, a provider based in the USA, is the easiest option. It is a paid service that provides an encrypted connection without requiring you to open ports on your router. The subscription also supports Home Assistant development. Check the provider's website for the current price.

An alternative is **VPN**, which is a secure connection to your home network. It requires manual setup and must be connected before access is possible. If you already use and manage a VPN, this might be sufficient. Manual access through the router requires advanced knowledge of networking and security; for your first connection, choose the simpler route.

## Enabling Home Assistant Cloud

Perform these steps first at home when you have regular access to Home Assistant. You will need a running system, an internet connection, and a Home Assistant Cloud account. This setup is done through the user interface; YAML is not required.

1. Open **Settings → Home Assistant Cloud** and log in to the service account. If you do not have an account, create one and review the subscription terms.
2. In the **Remote access** section, enable the switch. The initial setup may take several minutes. Creating and verifying the certificate after enabling can take up to a minute.
3. Save the displayed remote address. This is the address you will use to connect from outside your home network. You will use your Home Assistant account credentials to log into Home Assistant itself.
4. On your phone, turn off Wi-Fi and enable mobile data. Open the saved address in a browser. This verifies that access works even outside your home network.
5. Check the current temperature or the status of a light. For a first test, select an action whose result you can easily verify.

## Securing Your Login

The encrypted connection protects data transmission, but the account still requires a strong, unique password. In the Home Assistant user profile, open the **Security** tab and enable two-factor authentication using an authenticator application. Scan the QR code and confirm the setup with the current code. Set this verification for every account that uses remote access. Also, keep Home Assistant regularly updated.

## When the Connection Fails

First, check that remote access is enabled in Home Assistant Cloud and that you are using the correct address. If the internet goes down or the computer running Home Assistant is turned off at home, this method will not be available. The Cloud does not replace the local server.

If remote access is disabled, it cannot be automatically enabled from anywhere: remote activation requires the pre-approved option **Allow external activation of remote access**. Therefore, for the initial setup, remain within your home network.

Local automations can continue to run during an internet outage, provided the necessary devices are available at home. Details can be found in the article [What will work if the internet goes down?](/help/internet-outage/).

## Sources

- [Home Assistant: remote access](https://www.home-assistant.io/docs/configuration/remote/)
- [Nabu Casa: enabling remote access](https://support.nabucasa.com/hc/en-us/articles/26474279202973-Enabling-remote-access-to-Home-Assistant)
- [Nabu Casa: remote access security](https://support.nabucasa.com/hc/en-us/articles/26508882007581-Remote-access-Security-aspects)
- [Home Assistant: two-factor authentication](https://www.home-assistant.io/docs/authentication/multi-factor-auth/)
- [Nabu Casa: privacy and provider information](https://www.nabucasa.com/privacy/)
