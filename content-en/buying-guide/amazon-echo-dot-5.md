---
title: "Amazon Echo Dot 5: Voice Control for Home Assistant via Alexa"
description: "What you need for the Amazon Echo Dot 5, how to connect it to Home Assistant, and what to consider when buying in the Czech Republic."
cas: "5 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - Amazon Echo Dot 5
  - Alexa
  - Voice control
  - Home Assistant Cloud
translationKey: "buying-guide.amazon-echo-dot-5"
---

The Amazon Echo Dot 5 is a small smart speaker with the Alexa voice assistant. It is suitable for music, timers, and home voice control. Once connected, it can also control devices in Home Assistant. It is a product of the American company Amazon, which has headquarters in Seattle and Arlington; this information does not state where the specific unit was manufactured.

## What you need

You need mains power, home Wi-Fi, internet connection, an Amazon account, and the Alexa app on your phone. To control devices from Home Assistant, you also need your own running Home Assistant instance. The Echo Dot does not replace its server.

The speaker supports 2.4 GHz and 5 GHz Wi-Fi bands and Bluetooth. On the top surface, it has a volume control and a microphone mute button. If you do not want to use voice commands, you can mute the microphones with this button.

## Alexa and Czech

Czech is not among the supported languages for the Alexa service. For example, plan for English or German, and choose the names of lights accordingly. A simple English name like "Kitchen light" makes the command "Alexa, turn on the kitchen light" easier.

The availability of skills and music services varies by account region. Before purchasing, check if you can find the Home Assistant skill in the chosen Amazon store and if your music service is available. The Czech store selling the speaker itself does not guarantee Czech voice control.

## Connecting to Home Assistant

For beginners, the easiest route is Home Assistant Cloud from Nabu Casa. After the trial period, it requires a paid subscription. Connecting does not require opening ports on your home router. Manual connection via your own Alexa skill is also possible, but it requires an Amazon developer account, AWS services, and further setup.

To perform the initial connection, use this procedure:

1. Activate the Echo Dot in the Alexa app and link Home Assistant to Home Assistant Cloud.
2. In Home Assistant, open **Settings → Voice Assistants** and enable Alexa.
3. On the **Discover** card, first select a light or switch you want to control by voice.
4. In the Alexa app, open **Skills & Games**, add **Home Assistant Smart Home**, and link the Nabu Casa account.
5. Run the device discovery search with the command "Alexa, discover new devices" and test turning on the light.

You set up this procedure through the interface; you do not need YAML for the initial connection. Only enable devices that you genuinely want to control by voice.

## What to expect when using it normally

Voice control via Alexa uses cloud services. Therefore, do not rely on this control method during an internet outage. Connection also does not mean that the Echo Dot becomes a microphone for the Assist voice assistant in Home Assistant. For devices designed specifically for Assist, see [Home Assistant Voice Preview Edition](/buying-guide/home-assistant-voice-preview-edition/).

The Echo Dot 5 makes sense if you are comfortable with Alexa in a supported language and want to connect the speaker to home control. You can buy it, for example, at [Alza.cz – Amazon Echo Dot (5th Gen) Charcoal](https://www.alza.cz/amazon-echodot-5th-gen-charcoal-d7581917.htm). Before ordering, check the variant, included power supply, and current service conditions.

## Sources

- [Home Assistant: Amazon Alexa](https://www.home-assistant.io/integrations/alexa/)
- [Nabu Casa: Connecting Amazon Alexa to Home Assistant](https://support.nabucasa.com/hc/en-us/articles/25619363899677-Configuring-Amazon-Alexa-to-work-with-Home-Assistant)
- [Amazon: Supported languages and regions for Alexa](https://developer.amazon.com/en-US/alexa/devices/alexa-built-in/international)
- [Amazon: Muting Echo microphones](https://digprjsurvey.amazon.com/csad/help/node/GKA25FVYEV5PY8C9)
- [Amazon: Corporate offices](https://www.aboutamazon.com/workplace/corporate-offices)
- [Alza.cz: Amazon Echo Dot (5th Gen) Charcoal](https://www.alza.cz/amazon-echodot-5th-gen-charcoal-d7581917.htm)

