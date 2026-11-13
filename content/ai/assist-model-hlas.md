---
title: "Assist, model a hlas: jak funguje AI asistent v Home Assistant"
description: "Co dělají Assist, konverzační agent, přepis řeči a hlasový výstup, kde nastavit češtinu a jak ověřit ovládání světla."
obrazek: "/assets/images/assist-model-hlas.png"
obrazek_alt: "Cesta hlasového povelu: mikrofon, přepis do textu, Assist a AI model, ovládání světla a odpověď z reproduktoru."
cas: "6 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - AI
  - Assist
  - LLM
  - Hlasové ovládání
  - Čeština
---

Když řeknete „Rozsviť v kuchyni“, Home Assistant musí zachytit řeč, pochopit požadavek a provést akci. Hlasový asistent není jeden model: skládá se z několika částí, které lze měnit samostatně.

## Co dělá která část

| Část | Úloha | Příklady |
| --- | --- | --- |
| Hlasové zařízení | Mikrofon zachytí řeč, reproduktor přehraje odpověď. | Voice Preview Edition nebo telefon. |
| Řeč na text (STT) | Přepíše vyslovenou větu do textu. | Whisper nebo Home Assistant Cloud. |
| Konverzační agent | Zpracuje text a případně požádá o akci. | Vestavěný Home Assistant nebo agent s LLM. |
| Text na řeč (TTS) | Vytvoří zvuk z textové odpovědi. | Piper nebo Home Assistant Cloud. |

**Assist** je hlasový asistent Home Assistant, přes který tuto cestu používáte. Nastavení jednotlivých částí se označuje jako hlasová pipeline. Probuzení heslem nebo tlačítkem spustí poslech; teprve potom přichází přepis a zpracování.

## Kdy stačí Home Assistant a kdy přidat model

Vestavěný konverzační agent **Home Assistant** rozpoznává podporované povely pro zařízení a místnosti. Pro „Zhasni světlo v ložnici“ není nutné posílat požadavek velkému LLM. Důležité jsou názvy světel, přiřazené oblasti a zpřístupnění entit pro Assist.

Agent s **LLM** přidává volnější rozhovor a obecné otázky. Například přes Ollama lze použít místní model, přes OpenAI, Gemini či Anthropic cloudový. Schopnost odpovídat ale není totéž jako schopnost řídit domácnost: integrace musí ovládání povolit a model musí zvládat volání nástrojů.

Voice Preview Edition podporuje také uspořádání, kdy známý povel nejprve řeší Home Assistant a model nastoupí u nezpracovaného požadavku. Taková záloha není přepnutí při výpadku internetu; cloudový model stále potřebuje spojení.

## Kde se nastavuje čeština

Otevřete **Nastavení → Hlasoví asistenti**, v části **Assist** přidejte nebo upravte asistenta. Zkontrolujte jeho jazyk a tyto tři volby:

1. **Konverzační agent:** pro první ověření vyberte Home Assistant. Připojený AI agent lze zvolit později.
2. **Řeč na text:** zvolte poskytovatele podporujícího češtinu a český jazyk.
3. **Text na řeč:** nastavte češtinu a dostupný český hlas.

Změna jazyka rozhraní nestačí. Chybně nastavený přepis může zkomolit český název zařízení ještě předtím, než text dostane agent. Naopak správný přepis a anglické TTS mohou vést k cizojazyčné nebo špatně vyslovené odpovědi.

Pro začátek nabízí Home Assistant Cloud převod řeči v rámci předplatného. Pro místní provoz lze použít Whisper a Piper, ale je potřeba ověřit český model a výkon serveru. Speech-to-Phrase je další místní možnost zaměřená na omezenou sadu domácích povelů; před výběrem ověřte aktuální podporu češtiny. Samotný místní LLM nezajistí místní přepis ani hlas.

## Připojte zařízení a ověřte celý řetězec

U Voice Preview Edition na stránce zařízení vyberte připraveného hlasového asistenta. V **Nastavení → Hlasoví asistenti → Zpřístupnit** povolte pro Assist nejprve jedno světlo. Přiřaďte mu oblast a srozumitelný český název.

Nejprve zkuste povel napsat v Assist. Tím ověříte porozumění a akci bez mikrofonu. Potom stejnou větu vyslovte a zkontrolujte skutečný stav světla. Pokud text funguje a hlas ne, hledejte problém v poslechu nebo přepisu. Pokud se světlo přepne, ale odpověď není slyšet, ověřte TTS a hlasitost.

Pro první zkoušky stačí několik světel. Ovládání přes LLM může chybovat a u Ollama je označeno jako experimentální. Pevné automatizace ponechte pro pravidelné úkoly. Připojení zařízení a české oznámení popisuje [návod pro Voice Preview Edition](/navody/voice-preview-cesky-oznameni/).

## Zdroje

- [Home Assistant: Assist](https://www.home-assistant.io/voice_control/)
- [Home Assistant: hlasový asistent přes Cloud](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/)
- [Home Assistant: místní hlasový asistent](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [Home Assistant: zpřístupnění zařízení pro Assist](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Home Assistant: Voice Preview Edition](https://www.home-assistant.io/voice-pe/)
- [Nabu Casa: připojení Voice Preview Edition](https://support.nabucasa.com/hc/en-us/articles/25918770371229-Getting-started-with-Home-Assistant-Voice-Preview-Edition)
