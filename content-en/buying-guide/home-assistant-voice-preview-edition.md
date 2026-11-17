---
title: "Home Assistant Voice Preview Edition: Voice-Controlled Home"
description: "What you need to know before buying a Home Assistant voice device, and how to choose between local or cloud speech processing."
cas: "5 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - Voice Preview Edition
  - Assist
  - voice control
  - hardware
translationKey: "buying-guide.home-assistant-voice-preview-edition"
---

Making lights brighter without a phone, checking the temperature, or setting a timer: these are tasks for **Assist**, the Home Assistant voice assistant. The **Home Assistant Voice Preview Edition** adds microphones and a speaker to your room. However, before buying, consider where the speech will be processed and which commands you wish to use.

## What you are buying

It is a small tabletop device with two microphones, a speaker, a button, a rotary dial, and a light ring. A physical mute switch disconnects the microphone power. The dimensions are 84 × 84 × 21 mm, and the weight is 96 g. It also includes a 3.5mm audio output.

The device **does not replace the Home Assistant server**. It connects to it via Wi-Fi 2.4 GHz and serves as a voice point in the home. It is powered via USB-C; plan for a 5 V / 2 A source. The cable and power supply are not included in the box according to the manual.

The official hardware is designed by Nabu Casa, a company based in the USA. This is not a statement about the country of manufacture. According to the manufacturer, the purchase supports the development of Open Home Foundation projects.

## Local, or via the Cloud?

Local speech processing is handled by the home system. The advantage is the ability to function without the internet, provided the entire necessary chain runs locally. However, full speech transcription may react slowly on a weaker computer. The performance of the voice device itself does not guarantee recognition speed on the server.

Home Assistant also offers more efficient local recognition for limited home commands. Before choosing, verify support for your language and commands; limited mode is not the same as free conversation.

**Home Assistant Cloud** moves speech processing to a service. It is a suitable option even for a less powerful home server, but it requires the internet and a subscription. Cloud processing does not mean that the voice remains only at home. The operator specifies the use of Microsoft Azure voice services; details can be found in its privacy information.

## What to expect from Czech

Specifically verify three parts: speech transcription to text, command understanding, and voice response. Language support in one area does not automatically confirm the others. Nabu Casa lists Czech among the voice output languages, but before buying, also verify the chosen speech recognition method.

Start by testing Assist in the Home Assistant mobile app with the planned language and setup. Use actual room and device names. If the desired command doesn't work here, buying the microphones alone will not fix it. The **Preview Edition** designation indicates that the voice solution is still developing; do not expect every sentence to be understood without setup.

## What to prepare before connecting

You need an updated Home Assistant, administrator access, Wi-Fi 2.4 GHz, and power. For easy initial connection, use the current Home Assistant mobile app and a Bluetooth phone. The guide will walk you through connecting to Wi-Fi, adding the device, and selecting voice processing.

The devices you want to control by voice must be accessible to Assist. For the first attempt, select one light and a simple command. Adjust its name or alias so that it is easy to pronounce. This buying guide does not require YAML; perform the setup according to the guide and the manufacturer's manual.

**The Voice Preview Edition makes sense if you want to use Assist without a phone and are willing to adapt its setup to your home.** If you are expecting a standalone assistant without a server, this is not a suitable purchase. Check the current price and retailer on the official product page. In the Czech Republic, you can also check the offer at [Alza – Home Assistant Voice Preview Edition](https://www.alza.cz/home-assistant-voice-preview-edition-d12741248.htm).

## Sources

- [Home Assistant: Voice Preview Edition and specifications](https://www.home-assistant.io/voice-pe/)
- [Nabu Casa: Getting started with Home Assistant Voice Preview Edition](https://support.nabucasa.com/hc/en-us/articles/25918770371229-Getting-started-with-Home-Assistant-Voice-Preview-Edition)
- [Home Assistant: Assist and voice control](https://www.home-assistant.io/voice_control/)
- [Nabu Casa: Voice output and languages](https://support.nabucasa.com/hc/en-us/articles/25619386304541)
- [Nabu Casa: Privacy of voice services and provider information](https://www.nabucasa.com/privacy/)
