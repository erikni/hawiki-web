---
title: "Amazon Echo Dot 5: hlasové ovládání Home Assistant přes Alexu"
description: "Co potřebujete pro Amazon Echo Dot 5, jak jej propojit s Home Assistant a na co myslet při nákupu v Česku."
cas: "5 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - Amazon Echo Dot 5
  - Alexa
  - Hlasové ovládání
  - Home Assistant Cloud
---

Amazon Echo Dot 5 je malý chytrý reproduktor s hlasovou asistentkou Alexa. Hodí se pro hudbu, časovače a hlasové ovládání domácnosti. Po propojení může ovládat také zařízení v Home Assistant. Jde o výrobek americké společnosti Amazon, která má centrály v Seattlu a Arlingtonu; tento údaj neříká, kde byl konkrétní kus vyroben.

## Co potřebujete

Počítejte s napájením ze zásuvky, domácí Wi-Fi, připojením k internetu, účtem Amazon a aplikací Alexa v telefonu. Pro ovládání zařízení z Home Assistant potřebujete také vlastní běžící Home Assistant. Echo Dot jeho server nenahrazuje.

Reproduktor podporuje Wi-Fi v pásmech 2,4 a 5 GHz a Bluetooth. Na horní straně má ovládání hlasitosti a tlačítko pro odpojení mikrofonů. Když nechcete používat hlasové povely, můžete mikrofony tímto tlačítkem vypnout.

## Alexa a čeština

Čeština není mezi podporovanými jazyky služby Alexa. Počítejte například s angličtinou nebo němčinou a podle toho volte i názvy světel. Jednoduchý anglický název „Kitchen light“ usnadní povel „Alexa, turn on the kitchen light“.

Dostupnost dovedností a hudebních služeb se liší podle regionu účtu. Před nákupem zkontrolujte, zda ve zvoleném obchodě Amazon najdete dovednost Home Assistant a zda je dostupná vaše hudební služba. Český obchod s reproduktorem sám o sobě české hlasové ovládání nezaručuje.

## Propojení s Home Assistant

Pro začátečníka je nejsnazší cestou Home Assistant Cloud od Nabu Casa. Po zkušebním období vyžaduje placené předplatné. Propojení nevyžaduje otevírat porty domácího routeru. Ruční připojení přes vlastní dovednost Alexa je také možné, ale vyžaduje vývojářský účet Amazon, služby AWS a další nastavení.

Pro první propojení použijte tento postup:

1. Zprovozněte Echo Dot v aplikaci Alexa a přihlaste Home Assistant k Home Assistant Cloud.
2. V Home Assistant otevřete **Nastavení → Hlasoví asistenti** a povolte Alexu.
3. Na kartě **Zpřístupnit** vyberte nejprve jedno světlo nebo vypínač, které chcete hlasem ovládat.
4. V aplikaci Alexa otevřete **Skills & Games**, přidejte **Home Assistant Smart Home** a propojte účet Nabu Casa.
5. Spusťte vyhledání zařízení povelem „Alexa, discover new devices“ a vyzkoušejte zapnutí světla.

Tento postup nastavíte přes rozhraní; YAML pro první propojení nepotřebujete. Zpřístupněte jen zařízení, která opravdu chcete ovládat hlasem.

## Co čekat při běžném používání

Hlasové ovládání přes Alexu používá cloudové služby. Při výpadku internetu proto s touto cestou ovládání nepočítejte. Propojení také neznamená, že se Echo Dot stane mikrofonem pro hlasového asistenta Assist v Home Assistant. Pro zařízení navržené přímo pro Assist se podívejte na [Home Assistant Voice Preview Edition](/co-koupit/home-assistant-voice-preview-edition/).

Echo Dot 5 dává smysl, pokud vám vyhovuje Alexa v podporovaném jazyce a chcete spojit reproduktor s ovládáním domácnosti. Koupit jej můžete například na [Alza.cz – Amazon Echo Dot (5th Gen) Charcoal](https://www.alza.cz/amazon-echodot-5th-gen-charcoal-d7581917.htm). Před objednáním zkontrolujte variantu, dodávané napájení a aktuální podmínky služeb.

## Zdroje

- [Home Assistant: Amazon Alexa](https://www.home-assistant.io/integrations/alexa/)
- [Nabu Casa: propojení Amazon Alexa s Home Assistant](https://support.nabucasa.com/hc/en-us/articles/25619363899677-Configuring-Amazon-Alexa-to-work-with-Home-Assistant)
- [Amazon: podporované jazyky a regiony Alexa](https://developer.amazon.com/en-US/alexa/devices/alexa-built-in/international)
- [Amazon: vypnutí mikrofonů Echo](https://digprjsurvey.amazon.com/csad/help/node/GKA25FVYEV5PY8C9)
- [Amazon: firemní centrály](https://www.aboutamazon.com/workplace/corporate-offices)
- [Alza.cz: Amazon Echo Dot (5th Gen) Charcoal](https://www.alza.cz/amazon-echodot-5th-gen-charcoal-d7581917.htm)
