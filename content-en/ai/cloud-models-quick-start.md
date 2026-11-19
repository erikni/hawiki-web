---
title: "Cloud Models: Quick Start"
description: "Connect AI to Assist, set the language to Czech, and try controlling a single light."
obrazek: "/assets/images/cloudove-modely-rychly-zacatek.png"
obrazek_alt: "Home Assistant connects a light and a phone to the cloud offering multiple AI models."
cas: "8 minutes reading"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - "AI"
  - "Cloud Models"
  - "Assist"
  - "OpenAI"
  - "Gemini"
  - "Claude"
translationKey: "ai.cloud-models-quick-start"
---

## What you will get
A cloud model runs with the provider and serves as a conversational agent in Home Assistant: it processes your request and can request device control. You do not need a computer at home to run a large model, but you do need the internet and an API key, which is the access credential for the service.

We build upon [Assist, model and voice](/ai/assist-model-voice/). We start with text and a light; you can add voice later.

## Which service to connect
Home Assistant offers integrations for **OpenAI**, **Google Gemini**, and **Anthropic** for Claude models. Each requires its own provider key. A standard chat website account is not enough on its own.

OpenAI's API is paid separately from the ChatGPT subscription. Gemini has both free and paid modes with different limits and data handling rules. Before connecting your home, please read the terms of the chosen mode. Below, we test OpenAI.

## 1. Prepare the API Key
Create an account or log in at the [OpenAI platform](https://platform.openai.com/), set up billing, and create an API key. Check consumption, limits, or alerts. Do not rely automatically on budget alerts to stop all requests.

You only enter the key into the integration form. Do not put it in an article, screenshot, or public YAML. You pay for API usage; the length of the conversation and the selected model affect consumption.

## 2. Add the Integration
In Home Assistant, open **Settings → Devices & Services → Add integration**, search for **OpenAI**, and paste the key. In the conversational agent settings, leave the recommended model and settings for now. Do not enable Home Assistant control yet.

To the instructions, add something like: "Respond in Czech, concisely and clearly." While maintaining the original instructions necessary for working with the home. The instruction itself does not enable any devices.

## 3. Select the Agent in Assist
Open **Settings → Voice Assistants**, add or edit an existing assistant. Name it something like **AI cloud**, set the language to **Czech**, and select the created OpenAI agent as the conversational agent. Save the settings.

In the Assist panel, select this assistant and type "Odpovídej česky. Co umíš?" (Respond in Czech. What can you do?). This verifies the connection to the model. For voice use, you additionally need speech-to-text and text-to-speech with Czech support; you can use Home Assistant Cloud or local Whisper and Piper. Choosing the conversational model does not set up the entire voice chain.

## 4. Expose a Single Light
In the voice assistant settings, open **Expose** and check the entities available for Assist. For the first test, leave one light, and remove all other exposed entities. Give it a clear name, **Lampa v obýváku** (Living room light). Then, in the agent options, enable **Control Home Assistant**, meaning access to the Assist API.

Type "Zapni lampu v obýváku" (Turn on the living room light) and verify the actual illumination and status in the overview. Then try turning it off. A successful verbal response does not confirm the execution of the action. Only add sensitive devices after careful consideration of permissions.

## When something doesn't work
An access error can mean an invalid key, missing credit, or API limit. If the model responds, but the light doesn't turn on, check the selected assistant, control permissions, and entity exposure. First, resolve the text command, then the voice command.

The cloud receives the text request and context passed by the integration, such as data about exposed entities. During a power outage, the cloud agent will not respond. Standard local automations do not need to depend on it.

You do not have to stick with OpenAI and models known from ChatGPT. You can also try **Claude from Anthropic, Google Gemini**, or other supported services. Always add the corresponding integration and its API key, and select the new agent in Assist.

## Sources
- [Home Assistant: OpenAI](https://www.home-assistant.io/integrations/openai_conversation/)
- [Home Assistant: Google Gemini](https://www.home-assistant.io/integrations/google_generative_ai_conversation/)
- [Home Assistant: Anthropic](https://www.home-assistant.io/integrations/anthropic/)
- [Home Assistant: Exposing entities](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: Building a voice assistant](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [OpenAI: Getting started with the API](https://developers.openai.com/api/docs/quickstart)
- [OpenAI: Billing for ChatGPT and the API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
- [Google: Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key)
