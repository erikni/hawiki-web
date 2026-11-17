---
title: "Home Assistant and AI: What are your options"
description: "An introduction to cloud and local models, voice control, and AI agents like Hermes in the smart home."
cas: "6 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-01"
stav: "Based on documentation"
temata:
  - AI
  - LLM
  - Assist
  - Local models
  - Cloud models
  - AI agents
translationKey: "ai.home-assistant-ai-options"
---

AI in Home Assistant can hold conversations, determine the status of available devices, and execute commands using natural language. The foundation is a Large Language Model (LLM), which processes text. To actually switch something on, it must have an integrated tool enabled to control Home Assistant. The response "I switched it on" does not automatically confirm the action taken.

## Assist, Models, and Voice

**Assist** handles common household commands even without an LLM. The conversational agent determines whether the built-in Home Assistant or a connected model will process the text. An LLM can act as the primary agent or assist as a fallback for requests that standard Assist does not understand.

Voice control has three parts: **speech → text**, **request processing**, and **text → speech**. Voice Preview Edition provides microphones and a speaker; the large model runs on a server or in the cloud. Verify Czech support in all three parts, not just based on the Czech voice.

## Cloud Models: Quick Start

Home Assistant offers integrations for **OpenAI, Google Gemini, and Anthropic**. You typically enter the service access key, select a model, and specify whether it can control the home. You then choose the conversational agent in the voice assistant settings.

The cloud reduces the demands on your own computer, but it requires the internet and sends requests to the provider. The cost depends on the service, the model, and API usage. A subscription to a general chat application does not automatically mean paid API access. Nor is Home Assistant Cloud from Nabu Casa the same as a subscription to an external LLM: it can provide voice services, but you connect the model separately.

## Local Models: Your Own AI Server

**Ollama** runs the model on your computer, and the Home Assistant integration connects to its server over the network. The **llama.cpp** integration connects to a server with a compatible interface; it supports, for example, llama.cpp or vLLM. These names refer to the method of operation, not a specific model.

The model can run on a different computer than Home Assistant. The required memory and speed depend on the model, its size, and the hardware. In addition to Czech, verify tool calling support: a model capable of conversation may not reliably control devices.

For a complete offline voice system, you also need local speech recognition and voice output, such as **Whisper and Piper**. A small server suitable for automation may not handle all these parts with a pleasant response.

## Combinations and LiteLLM

You can combine local voice services with a cloud model, or vice versa. Therefore, a dedicated LLM does not guarantee that the audio will remain local. **LiteLLM** provides a common gateway to multiple models, and Home Assistant has an integration for connecting to it. Both the gateway and the models need to be operational; the integration itself does not automatically create smart switching between them.

## Hermes Agents

The **Hermes Agent from Nous Research** combines a model with tools, memory, and planned tasks. It can solve multiple steps, such as preparing a summary from available data. It is a standalone project, not a synonym for LLM or built-in Assist. It can connect to further tools via MCP, which is an interface for exposing functions to the agent.

The connection to Home Assistant must define the available data and permitted actions. An agent on a local computer can still use a cloud model. The access settings for an external agent may also not have the same boundaries as the list of entities available to Assist.

## Where to Start in Further Guides

First, we connect a cloud model, then a local model via Ollama or llama.cpp. We build upon Czech voice, combined operation, and Hermes. Start with a few lights: LLM control may fail, and for example, Ollama is marked as experimental in the documentation. For every variant, we verify the response, correct actions, costs, and operation without the internet.

## Sources

- [Home Assistant: LLM](https://www.home-assistant.io/integrations/llm/)
- [Home Assistant: OpenAI](https://www.home-assistant.io/integrations/openai_conversation/)
- [Home Assistant: Google Gemini](https://www.home-assistant.io/integrations/google_generative_ai_conversation/)
- [Home Assistant: Anthropic](https://www.home-assistant.io/integrations/anthropic/)
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Home Assistant: llama.cpp](https://www.home-assistant.io/integrations/llama_cpp/)
- [Home Assistant: local voice assistant](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [Nous Research: Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [Home Assistant: LiteLLM](https://www.home-assistant.io/integrations/litellm/)
- [Home Assistant: Voice Preview Edition](https://www.home-assistant.io/voice-pe/)
- [Hermes Agent: MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/)
