---
title: "Ollama: instalace a první místní model"
description: "Stáhněte Ollama, spusťte první model a vyzkoušejte místní AI na Windows, Linuxu nebo Macu."
obrazek: "/assets/images/ollama-instalace-modely-hardware.png"
obrazek_alt: "Domácí počítače různých velikostí s ilustrací místního AI chatu a modelů."
cas: "6 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-03"
stav: "Podle dokumentace"
temata:
  - "AI"
  - "Ollama"
  - "Místní modely"
---

## Program a model jsou dvě různé věci
**Ollama** spouští jazykové modely na vašem počítači. Program je „přehrávač“, model je stažený „obsah“, který vytváří odpovědi. Po instalaci stáhnete model.

Při místním provozu zpracovává dotazy váš počítač. Ollama nabízí i cloudové modely, proto si ověřte, že používáte staženou místní variantu. Internet potřebujete pro instalaci a stažení, potom může místní chat fungovat bez něj. Výběru vhodného počítače se budeme věnovat samostatně.

Velkou výhodou je menší **vendor lock-in**, tedy závislost na jednom dodavateli. Ollama sjednocuje spouštění a API podporovaných modelů: můžete měnit modely, aniž pokaždé měníte celé připojení aplikace. Nezpřístupňuje tím uzavřené modely OpenAI nebo Gemini; schopnosti a licence modelů se stále liší.

## Kde Ollama stáhnout
Začněte na **[ollama.com/download](https://ollama.com/download)** a vyberte svůj systém. Používejte oficiální instalátor.

- **Windows:** stáhněte `OllamaSetup.exe`, spusťte ho a dokončete průvodce. Potřebujete Windows 10 22H2 nebo novější. Ollama pak běží na pozadí; příkazy zadáte do PowerShellu nebo Příkazového řádku.
- **Mac:** potřebujete macOS 14 nebo novější. Otevřete stažený `.dmg`, přetáhněte Ollama do Aplikací a spusťte ji. Povolte nabídnuté zpřístupnění příkazu `ollama`. Příkazy potom zadáte v aplikaci Terminál.
- **Linux:** v terminálu spusťte následující oficiální příkaz. Stáhne a spustí instalační skript, který nainstaluje Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Tyto příkazy patří do terminálu počítače s Ollama, nikoli do YAML editoru Home Assistant.

## Spusťte první model
Pro první pokus použijte malý model. V PowerShellu nebo terminálu napište:

```bash
ollama run llama3.2:3b
```

Ollama nejprve stáhne model a potom otevře konverzaci. Při dalším spuštění už použije soubor z disku. Zadejte například „Odpověz česky: co je Home Assistant?“ a vyzkoušejte krátký navazující dotaz. Kvalita češtiny a odpovědí se liší; model může podat i chybnou informaci. Konverzaci ukončíte příkazem `/bye`.

## Který model zkusit
Modely najdete v **[knihovně Ollama](https://ollama.com/library)**. U každého si přečtěte podporované schopnosti a vyberte konkrétní variantu. Název za dvojtečkou je označení varianty; například `3b` rozlišuje velikost modelu.

Pro srovnání můžete vyzkoušet jinou rodinu, například Gemma od Google:

```bash
ollama run gemma3:4b
```

Další možnost je **Qwen 3.8**, například `ollama run qwen3.8:27b`. Jde o výrazně náročnější model; nejprve ověřte požadavky jeho varianty v knihovně. Modelům položte stejnou otázku a porovnejte správnost, češtinu a rychlost.

## Stažené modely a místo na disku
Seznam stažených modelů zobrazíte:

```bash
ollama list
```

Pro stažení bez otevření chatu použijte `ollama pull gemma3:4b`. Nepoužívaný model odstraníte příkazem `ollama rm gemma3:4b`; smaže se jeho místní kopie a později ho můžete stáhnout znovu. Ověřte přesný název.

## Co potom s Home Assistant
Ollama má v Home Assistant vlastní integraci pro konverzačního agenta Assist. Server musí být dosažitelný z HA přes domácí síť; samotné spuštění chatu na notebooku ho ještě nepřipojí.

Pro ovládání zařízení vyberte model s podporou **tools**. Model vhodný pro běžný chat nemusí tuto schopnost mít. Ovládání přes Ollama je v HA experimentální, proto začněte jednou lampou a ověřujte skutečné provedení akce. Připojení serveru a místní hlas popisuje [návod na vlastní AI server](../mistni-modely-vlastni-ai-server/).

## Zdroje
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Ollama: stažení](https://ollama.com/download)
- [Ollama: Windows](https://docs.ollama.com/windows)
- [Ollama: macOS](https://docs.ollama.com/macos)
- [Ollama: Linux](https://docs.ollama.com/linux)
- [Ollama: místní provoz a cloud](https://docs.ollama.com/faq)
- [Ollama: knihovna modelů](https://ollama.com/library)
- [Ollama: Llama 3.2](https://ollama.com/library/llama3.2)
- [Ollama: Gemma 3](https://ollama.com/library/gemma3)
- [Ollama: Qwen 3.8](https://ollama.com/library/qwen3.8)
- [Ollama: společné API](https://docs.ollama.com/api/introduction)
