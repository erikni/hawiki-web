---
title: "Local Models: Self-Hosted AI Server"
description: "Ollama and LM Studio for Mac, connecting to Assist, and setting up local voice with Whisper and Piper."
obrazek: "/assets/images/mistni-modely-vlastni-ai-server.png"
obrazek_alt: "Self-hosted AI computer in the home connected to Home Assistant, a phone, and a lamp."
cas: "8 minutes read"
obtiznost: "Advanced"
kontrola_zdroju: "2026-10-03"
stav: "Documentation-based"
temata:
  - "AI"
  - "Local Models"
  - "Ollama"
  - "LM Studio"
  - "Assist"
  - "Self-Hosted Server"
translationKey: "ai.local-models-own-ai-server"
---

## Local Models and Self-Hosted Voice
Local AI processes requests at home. Both **Ollama** and **LM Studio** can run downloaded models; Home Assistant then controls the devices. The model generates the response, **Whisper** transcribes speech to text, and **Piper** converts the response into voice. These are three separate components [Assist Assistant](/ai/assist-model-voice/).

## Choose Software and Computer
Ollama runs on Linux, Windows, and macOS. LM Studio offers a graphical model search and chat interface; for Mac, it requires Apple Silicon and macOS 14+, and recommends 16 GB of memory. It does not support Intel Macs.

For both, the speed and required memory depend on the model and the length of the conversation. The server must not be asleep. You need the internet for installation and downloading; however, with a local model, processing can run without it. Ollama also offers cloud features, so we will disable them below.

## 1. Download and Test a Model
**Ollama:** Install the application from the [official website](https://ollama.com/download). In the AI computer's terminal, run:

```bash
ollama run llama3.1:8b
```

**LM Studio on Mac:** Install the application from [lmstudio.ai](https://lmstudio.ai/), search for a model, download it, and load it into the chat.

In both cases, try a Czech response and measure the speed. To control devices, you need a model with tool support (**tools**); Llama 3.1 is an example for Ollama. Verify the reliability.

## 2. Run the Server on the Home Network
**Ollama:** On Linux, open `sudo systemctl edit ollama.service` and paste:

```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_NO_CLOUD=1"
```

Save and run in the terminal:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

On Mac, set the same variables according to the Ollama documentation and restart the application.

**LM Studio on Mac:** In **Developer**, load the model, enable **Serve on Local Network**, and **Start server**. The OpenAI compatible API is usually available at `http://MAC-IP:1234/v1`.

Reserve an IP address for the server, restrict the firewall to HA, and do not expose the port to the internet.

## 3. Connect the Model to Assist
**Ollama:** In **Settings → Devices & Services → Add Integration**, select Ollama, use an address like `http://192.168.1.50:11434`, and specify the model `llama3.1:8b`. Replace the IP address with your server's IP; `localhost` here means the HA computer.

**LM Studio:** Requires a conversational integration agent that supports a custom OpenAI compatible address. The official OpenAI integration does not support this, and the Ollama integration uses a different API. Connecting LM Studio therefore requires an additional integration; we will cover the exact procedure separately.

Select the available agent in **Settings → Voice Assistants**, set the language to Czech, and verify the text in Assist. For Ollama, control is experimental. Enable one lamp for the first test, allow the agent to control HA, and verify its actual switching.

## 4. Add Whisper and Piper
**Whisper** recognizes spoken words, but it cannot control a lamp. **Piper** reads the response text, but it does not generate the text. They complement both the local Ollama agent and the suitable LM Studio agent.

In **Home Assistant OS**, open **Settings → Applications → Add-on Store**, install **Whisper** and **Piper**, enable startup, and start both applications. In **Devices & Services**, add the discovered **Wyoming** services. In the older interface, these applications are listed as add-ons.

For the assistant, select Whisper for **speech-to-text** and Piper for **text-to-speech**, set the language to Czech, and select an available Czech voice. Keep the model agent selected. First, verify the transcription, then the response, and finally the playback via phone or voice device. Whisper requires power; on a weak computer, it may react slowly. When installing HA in a container, run the services separately and connect them via Wyoming.

## Sources
- [Home Assistant: Ollama integration](https://www.home-assistant.io/integrations/ollama/)
- [Ollama: Installation](https://ollama.com/download)
- [Ollama: Network, variables, and disabling cloud](https://docs.ollama.com/faq)
- [Ollama: Installation and service on Linux](https://docs.ollama.com/linux)
- [Ollama: Supported hardware](https://docs.ollama.com/gpu)
- [Ollama: Tool calling](https://docs.ollama.com/capabilities/tool-calling)
- [Ollama: Llama 3.1 model](https://ollama.com/library/llama3.1)
- [Home Assistant: Exposing entities](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: Local voice assistant](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [LM Studio: Mac requirements](https://lmstudio.ai/docs/app/system-requirements)
- [LM Studio: Local API server](https://lmstudio.ai/docs/developer/core/server)
- [LM Studio: OpenAI compatible API](https://lmstudio.ai/docs/developer/openai-compat)
- [Home Assistant: OpenAI integration limitations](https://www.home-assistant.io/integrations/openai_conversation/)
- [LM Studio: Access on local network](https://lmstudio.ai/docs/developer/core/server/serve-on-network)
