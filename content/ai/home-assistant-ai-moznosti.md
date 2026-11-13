---
title: "Home Assistant a AI: jaké máte možnosti"
description: "Úvod do cloudových a místních modelů, hlasového ovládání a AI agentů typu Hermes v chytré domácnosti."
cas: "6 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - AI
  - LLM
  - Assist
  - Místní modely
  - Cloudové modely
  - AI agenti
---

AI v Home Assistant může vést rozhovor, zjistit stav zpřístupněných zařízení a provést povel běžným jazykem. Základem je jazykový model (LLM), který zpracovává text. Aby skutečně rozsvítil, musí mít přes integraci povolený nástroj pro ovládání Home Assistant. Odpověď „rozsvítil jsem“ sama nepotvrzuje provedenou akci.

## Assist, model a hlas

**Assist** zvládá běžné domácí povely i bez LLM. Konverzační agent určuje, kdo text zpracuje: vestavěný Home Assistant, nebo připojený model. LLM může být hlavním agentem nebo pomáhat jako záloha u požadavků, kterým běžný Assist nerozumí.

Hlasové ovládání má tři části: **řeč → text**, **zpracování požadavku**, **text → řeč**. Voice Preview Edition poskytuje mikrofony a reproduktor; velký model běží na serveru nebo v cloudu. Češtinu ověřujte ve všech třech částech, ne jen podle českého hlasu.

## Cloudové modely: rychlý začátek

Home Assistant nabízí integrace **OpenAI, Google Gemini a Anthropic**. Obvykle zadáte přístupový klíč služby, vyberete model a určíte, zda smí ovládat domácnost. Konverzačního agenta pak zvolíte v nastavení hlasového asistenta.

Cloud snižuje nároky na vlastní počítač, ale vyžaduje internet a požadavky posílá poskytovateli. Cena závisí na službě, modelu a využití API. Předplatné běžné chatovací aplikace automaticky neznamená zaplacené API. Ani Home Assistant Cloud od Nabu Casa není totéž jako předplatné cizího LLM: může zajišťovat hlasové služby, zatímco model připojíte zvlášť.

## Místní modely: vlastní AI server

**Ollama** provozuje model na vašem počítači a integrace Home Assistant se k jejímu serveru připojí přes síť. **llama.cpp** integrace připojuje server s kompatibilním rozhraním; podporuje například llama.cpp nebo vLLM. Tyto názvy označují způsob provozu, nikoli jeden konkrétní model.

Model může běžet na jiném počítači než Home Assistant. Potřebná paměť a rychlost závisejí na modelu, jeho velikosti a hardwaru. Vedle češtiny ověřujte podporu volání nástrojů: model schopný rozhovoru nemusí spolehlivě ovládat zařízení.

Pro celý hlasový systém bez cloudu potřebujete také místní rozpoznávání řeči a hlasový výstup, například **Whisper a Piper**. Menší server vhodný pro automatizace nemusí zvládnout všechny tyto části s příjemnou odezvou.

## Kombinace a LiteLLM

Můžete spojit místní hlasové služby s cloudovým modelem nebo naopak. Vlastní LLM tedy samo nezaručuje, že audio zůstane doma. **LiteLLM** poskytuje společnou bránu k více modelům a Home Assistant má integraci pro její připojení. Bránu i modely je potřeba zprovoznit; samotná integrace automaticky nevytvoří chytré přepínání mezi nimi.

## Agenti typu Hermes

**Hermes Agent od Nous Research** spojuje model s nástroji, pamětí a plánovanými úlohami. Může řešit více kroků, třeba připravit přehled z dostupných údajů. Je to samostatný projekt, nikoli synonymum pro LLM nebo vestavěný Assist. K dalším nástrojům se může připojit přes MCP, tedy rozhraní pro zpřístupnění funkcí agentovi.

Propojení s Home Assistant musí určit dostupné údaje a povolené akce. Agent na domácím počítači může stále používat cloudový model. Nastavení přístupu pro externího agenta také nemusí mít stejné hranice jako seznam entit zpřístupněných Assist.

## Čím začneme v dalších návodech

Nejprve připojíme cloudový model, potom místní model přes Ollama či llama.cpp. Navážeme českým hlasem, kombinovaným provozem a Hermesem. Začněte několika světly: ovládání LLM může chybovat a například Ollama je v dokumentaci označuje jako experimentální. U každé varianty ověříme odezvu, správné akce, náklady a provoz bez internetu.

## Zdroje

- [Home Assistant: LLM](https://www.home-assistant.io/integrations/llm/)
- [Home Assistant: OpenAI](https://www.home-assistant.io/integrations/openai_conversation/)
- [Home Assistant: Google Gemini](https://www.home-assistant.io/integrations/google_generative_ai_conversation/)
- [Home Assistant: Anthropic](https://www.home-assistant.io/integrations/anthropic/)
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Home Assistant: llama.cpp](https://www.home-assistant.io/integrations/llama_cpp/)
- [Home Assistant: místní hlasový asistent](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [Nous Research: Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [Home Assistant: LiteLLM](https://www.home-assistant.io/integrations/litellm/)
- [Home Assistant: Voice Preview Edition](https://www.home-assistant.io/voice-pe/)
- [Hermes Agent: MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/)
