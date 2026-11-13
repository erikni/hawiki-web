---
title: "Místní modely: vlastní AI server"
description: "Ollama a LM Studio pro Mac, připojení k Assist a instalace místního hlasu s Whisper a Piper."
obrazek: "/assets/images/mistni-modely-vlastni-ai-server.png"
obrazek_alt: "Vlastní AI počítač v domácnosti propojený s Home Assistant, telefonem a lampou."
cas: "8 minut čtení"
obtiznost: "Pokročilejší"
kontrola_zdroju: "2026-10-03"
stav: "Podle dokumentace"
temata:
  - "AI"
  - "Místní modely"
  - "Ollama"
  - "LM Studio"
  - "Assist"
  - "Vlastní server"
---

## Vlastní model a vlastní hlas
Místní AI zpracovává požadavky doma. **Ollama** i **LM Studio** umějí spouštět stažené modely; Home Assistant dál řídí zařízení. Model tvoří odpověď, **Whisper** přepisuje řeč na text a **Piper** převádí odpověď na hlas. Jsou to tři samostatné části [asistenta Assist](../assist-model-hlas/).

## Vyberte program a počítač
Ollama běží na Linuxu, Windows i macOS. LM Studio nabízí grafické hledání modelů a chat; pro Mac vyžaduje Apple Silicon a macOS 14+, doporučuje 16 GB paměti. Intel Macy nepodporuje.

U obou záleží rychlost a potřebná paměť na modelu a délce konverzace. Server se nesmí uspávat. Internet potřebujete pro instalaci a stažení; s místním modelem může zpracování běžet bez něj. Ollama nabízí i cloudové funkce, proto je níže vypneme.

## 1. Stáhněte a vyzkoušejte model
**Ollama:** nainstalujte program z [oficiálního webu](https://ollama.com/download). V terminálu AI počítače spusťte:

```bash
ollama run llama3.1:8b
```

**LM Studio na Macu:** nainstalujte aplikaci z [lmstudio.ai](https://lmstudio.ai/), vyhledejte model, stáhněte ho a načtěte do chatu.

V obou zkuste českou odpověď a změřte rychlost. Pro ovládání zařízení potřebujete model s podporou nástrojů (**tools**); Llama 3.1 je příklad pro Ollama. Spolehlivost ověřte.

## 2. Spusťte server v domácí síti
**Ollama:** na Linuxu se systemd otevřete `sudo systemctl edit ollama.service` a vložte:

```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_NO_CLOUD=1"
```

Uložte a v terminálu spusťte:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Na Macu nastavte stejné proměnné podle dokumentace Ollama a restartujte aplikaci.

**LM Studio na Macu:** v **Developer** načtěte model, zapněte **Serve on Local Network** a **Start server**. OpenAI kompatibilní API bývá na `http://IP-MACU:1234/v1`.

Serveru rezervujte IP, firewall omezte na HA a port nevystavujte internetu.

## 3. Připojte model k Assist
**Ollama:** v **Nastavení → Zařízení a služby → Přidat integraci** vyberte Ollama, adresu například `http://192.168.1.50:11434` a model `llama3.1:8b`. Nahraďte IP adresou serveru; `localhost` zde znamená počítač HA.

**LM Studio:** potřebuje integračního konverzačního agenta podporujícího vlastní OpenAI kompatibilní adresu. Oficiální integrace OpenAI ji nepodporuje a integrace Ollama používá jiné API. Propojení LM Studio proto vyžaduje další integraci; přesný postup rozebereme samostatně.

Dostupného agenta vyberte v **Nastavení → Hlasoví asistenti**, nastavte češtinu a ověřte text v Assist. U Ollama je ovládání experimentální. Zpřístupněte pro první pokus jednu lampu, povolte agentovi ovládání HA a ověřte její skutečné zapnutí.

## 4. Přidejte Whisper a Piper
**Whisper** rozpozná vyslovená slova, ale neovládá lampu. **Piper** přečte text odpovědi, ale nevymýšlí ji. Doplňují jak místního agenta Ollama, tak vhodně připojeného agenta LM Studio.

V **Home Assistant OS** otevřete **Nastavení → Aplikace → Obchod s aplikacemi**, nainstalujte **Whisper** a **Piper**, zapněte spouštění při startu a obě aplikace spusťte. V **Zařízení a služby** přidejte nalezené služby **Wyoming**. Ve starším rozhraní jsou aplikace označené jako doplňky.

U asistenta vyberte Whisper pro **řeč na text** a Piper pro **text na řeč**, nastavte češtinu a dostupný český hlas. Model agenta ponechte vybraný. Ověřte nejprve přepis, potom odpověď a přehrání přes telefon nebo hlasové zařízení. Whisper potřebuje výkon; na slabém počítači může reagovat pomalu. U instalace HA v kontejneru provozujte služby zvlášť a připojte je přes Wyoming.

## Zdroje
- [Home Assistant: integrace Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Ollama: instalace](https://ollama.com/download)
- [Ollama: síť, proměnné a vypnutí cloudu](https://docs.ollama.com/faq)
- [Ollama: instalace a služba na Linuxu](https://docs.ollama.com/linux)
- [Ollama: podporovaný hardware](https://docs.ollama.com/gpu)
- [Ollama: volání nástrojů](https://docs.ollama.com/capabilities/tool-calling)
- [Ollama: model Llama 3.1](https://ollama.com/library/llama3.1)
- [Home Assistant: zpřístupnění entit](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: místní hlasový asistent](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [LM Studio: požadavky pro Mac](https://lmstudio.ai/docs/app/system-requirements)
- [LM Studio: místní API server](https://lmstudio.ai/docs/developer/core/server)
- [LM Studio: OpenAI kompatibilní API](https://lmstudio.ai/docs/developer/openai-compat)
- [Home Assistant: omezení integrace OpenAI](https://www.home-assistant.io/integrations/openai_conversation/)
- [LM Studio: přístup v domácí síti](https://lmstudio.ai/docs/developer/core/server/serve-on-network)
