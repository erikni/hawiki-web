---
title: "Assist, Models, and Voice: How the AI Assistant Works in Home Assistant"
description: "What Assist, the conversational agent, speech-to-text, and voice output do, where to set Czech language, and how to verify light control."
obrazek: "/assets/images/assist-model-hlas.png"
obrazek_alt: "The voice command path: microphone, transcription to text, Assist and AI model, light control, and response from the speaker."
cas: "6 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - AI
  - Assist
  - LLM
  - Voice control
  - Czech
translationKey: "ai.assist-model-voice"
---

When you say "Turn on the kitchen light," Home Assistant must capture the speech, understand the request, and perform the action. The voice assistant is not a single model; it is composed of several parts that can be changed independently.

## What Each Part Does

| Part | Function | Examples |
| --- | --- | --- |
| Voice Device | Microphone captures speech, speaker plays the response. | Voice Preview Edition or phone. |
| Speech-to-Text (STT) | Transcribes spoken sentence into text. | Whisper or Home Assistant Cloud. |
| Conversational Agent | Processes the text and may request an action. | Built-in Home Assistant or agent with LLM. |
| Text-to-Speech (TTS) | Creates sound from the text response. | Piper or Home Assistant Cloud. |

**Assist** is the Home Assistant voice assistant through which you use this path. The configuration of individual parts is referred to as the voice pipeline. A wake word or button press initiates listening; transcription and processing only happen afterward.

## When Home Assistant is Enough and When to Add a Model

The built-in conversational agent in **Home Assistant** recognizes supported commands for devices and rooms. For "Turn off the bedroom light," it is not necessary to send the request to a large LLM. What is important are the light names, the assigned area, and the exposed entities for Assist.

An agent with an **LLM** adds more fluid conversation and general questions. For example, you can use a local model via Ollama, or a cloud model via OpenAI, Gemini, or Anthropic. However, the ability to answer is not the same as the ability to control the home: the integration must allow control, and the model must handle tool calls.

Voice Preview Edition also supports a fallback, where Home Assistant handles the known command first, and the model steps in for unhandled requests. This fallback is not a switch for internet failure; the cloud model still requires a connection.

## Where to Configure Czech Language

Open **Settings → Voice Assistants**, and under the **Assist** section, add or edit an assistant. Check its language and these three options:

1. **Conversational Agent:** For initial testing, select Home Assistant. The connected AI agent can be chosen later.
2. **Speech-to-Text:** Select a provider that supports Czech and the Czech language.
3. **Text-to-Speech:** Set Czech and an available Czech voice.

Changing the interface language is not enough. Incorrect transcription can mangle the Czech device name even before the text reaches the agent. Conversely, correct transcription and English TTS can lead to a foreign or poorly pronounced response.

For starters, Home Assistant Cloud offers speech transcription as part of the subscription. For local operation, you can use Whisper and Piper, but you need to verify the Czech model and server performance. Speech-to-Phrase is another local option focused on a limited set of home commands; verify current Czech support before selecting it. The local LLM itself does not guarantee local transcription or voice output.

## Connect Devices and Test the Whole Chain

In Voice Preview Edition, select the configured voice assistant on the device page. In **Settings → Voice Assistants → Expose**, enable at least one light for Assist. Assign it an area and a clear Czech name.

First, try typing the command in Assist. This verifies understanding and action without a microphone. Then, speak the same sentence and check the actual light status. If the text works and the voice does not, look for a problem with listening or transcription. If the light switches but the response is not heard, check TTS and volume.

A few lights are enough for initial tests. LLM control may fail, and Ollama is marked as experimental. Keep fixed automations for regular tasks. Connecting devices and Czech announcements are described in the [Voice Preview Edition guide](/guides/voice-preview-czech-announcements/).

## Sources

- [Home Assistant: Assist](https://www.home-assistant.io/voice_control/)
- [Home Assistant: Voice Assistant via Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)
- [Home Assistant: Local Voice Assistant](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [Home Assistant: Exposing Devices for Assist](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Home Assistant: Voice Preview Edition](https://www.home-assistant.io/voice-pe/)
- [Nabu Casa: Connecting Voice Preview Edition](https://support.nabucasa.com/hc/en-us/articles/25918770371229-Getting-started-with-Home-Assistant-Voice-Preview-Edition)
