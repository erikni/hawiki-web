---
title: "Cloudové modely: rychlý začátek"
description: "Připojte AI k Assist, nastavte češtinu a vyzkoušejte ovládání jedné lampy."
obrazek: "/assets/images/cloudove-modely-rychly-zacatek.png"
obrazek_alt: "Home Assistant propojuje lampu a telefon s cloudem nabízejícím více AI modelů."
cas: "8 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "AI"
  - "Cloudové modely"
  - "Assist"
  - "OpenAI"
  - "Gemini"
  - "Claude"
---

## Co získáte
Cloudový model běží u poskytovatele a v Home Assistant slouží jako konverzační agent: zpracuje váš požadavek a může požádat o ovládání zařízení. Nepotřebujete doma počítač pro provoz velkého modelu, potřebujete však internet a API klíč, tedy přístupový údaj ke službě.

Navazujeme na [Assist, model a hlas](../assist-model-hlas/). Začneme textem a lampou; hlas přidáte později.

## Jakou službu připojit
Home Assistant nabízí integrace **OpenAI**, **Google Gemini** a **Anthropic** pro modely Claude. Každá potřebuje klíč svého poskytovatele. Účet v běžném chatovacím webu sám o sobě nestačí.

U OpenAI je API placené zvlášť od předplatného ChatGPT. Gemini má bezplatný i placený režim s odlišnými limity a pravidly nakládání s daty. Před zapojením domácnosti si přečtěte podmínky vybraného režimu. Níže vyzkoušíme OpenAI.

## 1. Připravte API klíč
V [platformě OpenAI](https://platform.openai.com/) založte účet nebo se přihlaste, nastavte účtování a vytvořte API klíč. Zkontrolujte spotřebu a limity či upozornění. Nespoléhejte automaticky na to, že rozpočtové upozornění zastaví všechny požadavky.

Klíč vložíte jen do integračního formuláře. Nedávejte ho do článku, screenshotu ani veřejného YAML. Platíte za využití API; délka konverzace a zvolený model ovlivňují spotřebu.

## 2. Přidejte integraci
V Home Assistant otevřete **Nastavení → Zařízení a služby → Přidat integraci**, vyhledejte **OpenAI** a vložte klíč. V nastavení konverzačního agenta ponechte pro začátek doporučený model a nastavení. Zatím nepovolujte ovládání Home Assistant.

Do instrukcí doplňte například: „Odpovídej česky, stručně a srozumitelně.“ Zachovejte přitom původní instrukce potřebné pro práci s domácností. Samotná instrukce nezpřístupní žádná zařízení.

## 3. Vyberte agenta v Assist
Otevřete **Nastavení → Hlasoví asistenti**, přidejte asistenta nebo upravte existujícího. Pojmenujte ho třeba **AI cloud**, nastavte jazyk **čeština** a jako konverzačního agenta vyberte vytvořeného agenta OpenAI. Uložte nastavení.

V panelu Assist vyberte tohoto asistenta a napište „Odpovídej česky. Co umíš?“ Tím ověříte spojení s modelem. Pro hlasové použití navíc potřebujete přepis řeči a hlasový výstup s podporou češtiny; můžete využít Home Assistant Cloud nebo místní Whisper a Piper. Volba konverzačního modelu sama nenastaví celý hlasový řetězec.

## 4. Zpřístupněte jednu lampu
V nastavení hlasových asistentů otevřete **Zpřístupnit** a zkontrolujte entity dostupné pro Assist. Pro první zkoušku ponechte jednu lampu, ostatní zpřístupněné entity odeberte. Dejte jí jasný název **Lampa v obýváku**. Pak v možnostech agenta povolte **Ovládat Home Assistant**, tedy přístup k Assist API.

Napište „Zapni lampu v obýváku“ a ověřte skutečné rozsvícení i stav v přehledu. Potom vyzkoušejte vypnutí. Úspěšná slovní odpověď sama nepotvrzuje provedení akce. Citlivá zařízení přidávejte až po zvážení oprávnění.

## Když něco nefunguje
Chyba přístupu může znamenat neplatný klíč, chybějící kredit nebo limit API. Pokud model odpovídá, ale lampu nezapne, ověřte vybraného asistenta, povolení ovládání a zpřístupnění entity. Nejprve vyřešte textový pokyn, potom hlas.

Cloud dostává text požadavku a kontext předaný integrací, například údaje o zpřístupněných entitách. Při výpadku internetu cloudový agent neodpoví. Běžné místní automatizace na něm být závislé nemusí.

Nemusíte zůstat u OpenAI a modelů známých z ChatGPT. Vyzkoušet můžete také **Claude od Anthropic, Google Gemini** nebo další podporované služby. Vždy přidejte odpovídající integraci a její API klíč a nového agenta vyberte v Assist.

## Zdroje
- [Home Assistant: OpenAI](https://www.home-assistant.io/integrations/openai_conversation/)
- [Home Assistant: Google Gemini](https://www.home-assistant.io/integrations/google_generative_ai_conversation/)
- [Home Assistant: Anthropic](https://www.home-assistant.io/integrations/anthropic/)
- [Home Assistant: zpřístupnění entit](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: sestavení hlasového asistenta](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [OpenAI: začátek práce s API](https://developers.openai.com/api/docs/quickstart)
- [OpenAI: účtování ChatGPT a API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)
- [Google: API klíče Gemini](https://ai.google.dev/gemini-api/docs/api-key)
