---
title: "Ollama: Installing and Running Your First Local Model"
description: "Download Ollama, run your first model, and try local AI on Windows, Linux, or Mac."
obrazek: "/assets/images/ollama-instalace-modely-hardware.png"
obrazek_alt: "Home computers of various sizes with an illustration of local AI chat and models."
cas: "6 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-03"
stav: "Documented"
temata:
  - "AI"
  - "Ollama"
  - "Local Models"
translationKey: "ai.ollama-installation-models-hardware"
---

## Program and Model are Two Different Things
**Ollama** runs language models on your computer. The program is the "player," and the model is the downloaded "content" that generates answers. After installation, you download the model.

When running locally, your computer processes the queries. Ollama also offers cloud models, so ensure you are using the downloaded local version. You need the internet for installation and downloading, but the local chat can function without it afterward. We will cover choosing suitable hardware separately.

A major advantage is reduced **vendor lock-in**, meaning less dependence on a single provider. Ollama unifies the running and API support for various models: you can change models without having to change the entire application connection every time. This does not make closed models like OpenAI or Gemini available; the capabilities and licenses of the models still differ.

## Where to Download Ollama
Start at **[ollama.com/download](https://ollama.com/download)** and select your system. Use the official installer.

- **Windows:** Download `OllamaSetup.exe`, run it, and follow the wizard. You need Windows 10 22H2 or newer. Ollama then runs in the background; you enter commands into PowerShell or Command Prompt.
- **Mac:** You need macOS 14 or newer. Open the downloaded `.dmg`, drag Ollama to Applications, and run it. Allow the requested accessibility for the `ollama` command. You then enter commands in the Terminal application.
- **Linux:** Run the following official command in the terminal. It downloads and runs an installation script that installs Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

These commands belong in the computer's terminal with Ollama, not in the Home Assistant YAML editor.

## Running Your First Model
For your first attempt, use a small model. In PowerShell or the terminal, type:

```bash
ollama run llama3.2:3b
```

Ollama will first download the model and then open a conversation. On subsequent runs, it will use the file from the disk. Ask, for example, "Answer in Czech: what is Home Assistant?" and try a short follow-up question. The quality of the Czech and the answers varies; the model may also provide incorrect information. You can end the conversation with the command `/bye`.

## Which Model to Try
You can find models in the **[Ollama library](https://ollama.com/library)**. Read the supported capabilities for each one and select a specific variant. The name after the colon is the variant identifier; for example, `3b` distinguishes the model size.

For comparison, you could try another family, such as Gemma from Google:

```bash
ollama run gemma3:4b
```

Another option is **Qwen 3.8**, for example `ollama run qwen3.8:27b`. This is a significantly more demanding model; first verify the requirements of its variant in the library. Ask the models the same question and compare the accuracy, Czech quality, and speed.

## Downloaded Models and Disk Space
You can list downloaded models using:

```bash
ollama list
```

To download without opening a chat, use `ollama pull gemma3:4b`. To remove an unused model, use the command `ollama rm gemma3:4b`; this deletes its local copy, which you can download again later. Verify the exact name.

## What Next with Home Assistant
Ollama has its own integration in Home Assistant for the Assist conversational agent. The server must be reachable from HA over the local network; simply running the chat on a laptop does not connect it.

To control devices, select a model that supports **tools**. A model suitable for general chat may not have this capability. Controlling via Ollama in HA is experimental, so start with one light and verify the actual execution of the action. Connecting the server and local voice is described in [guide to self-hosted AI server](/ai/local-models-own-ai-server/).

## Sources
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Ollama: Download](https://ollama.com/download)
- [Ollama: Windows](https://docs.ollama.com/windows)
- [Ollama: macOS](https://docs.ollama.com/macos)
- [Ollama: Linux](https://docs.ollama.com/linux)
- [Ollama: Local vs Cloud](https://docs.ollama.com/faq)
- [Ollama: Model Library](https://ollama.com/library)
- [Ollama: Llama 3.2](https://ollama.com/library/llama3.2)
- [Ollama: Gemma 3](https://ollama.com/library/gemma3)
- [Ollama: Qwen 3.8](https://ollama.com/library/qwen3.8)
- [Ollama: Common API](https://docs.ollama.com/api/introduction)
