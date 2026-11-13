---
title: "Okno zůstalo otevřené: nechte si poslat upozornění"
description: "Jedna zpráva do mobilu po deseti minutách otevřeného okna."
cas: "20 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Okna"
  - "Upozornění"
  - "Automatizace"
---

## Co bude na konci fungovat

Když vybrané okno zůstane deset minut otevřené, Home Assistant pošle zprávu do vašeho telefonu. Připomínka se hodí při větrání, když vás mezitím zaměstná něco jiného. Pravidlo připravíme pro jedno okno a jeden mobil, aby se snadno nastavovalo i kontrolovalo.

## Co budete potřebovat

Fungující Home Assistant, již připojený senzor otevření okna a telefon s [nastavenou aplikací Companion](../../zaciname/home-assistant-v-mobilu/). V telefonu povolte oznámení. Návod nepředpokládá konkrétní značku senzoru; jeho připojení musí být hotové předem.

Nejdříve okno otevřete a zavřete. V Home Assistantu se musí odpovídajícím způsobem změnit stav senzoru. U běžného binárního senzoru typu okno znamená vnitřní hodnota `on` otevřeno a `off` zavřeno. Přehled je může zobrazovat slovně.

## Nejprve vyzkoušejte zprávu

Otevřete **Nastavení → Nástroje → Akce**; ve starších verzích může být tato část pod Vývojářskými nástroji. Vyhledejte oznamovací akci svého telefonu. Její označení začíná `notify.mobile_app_` a pokračuje názvem zařízení. Vyplňte zprávu „Zkouška upozornění z domácnosti“ a akci spusťte.

Pokud zpráva nepřijde, zkontrolujte oprávnění oznámení v telefonu, režim Nerušit a připojení k internetu. Než začnete vytvářet pravidlo, zprovozněte tuto jednoduchou zkoušku. Ovládání domácnosti v aplikaci a doručení oznámení jsou dvě různé kontroly.

## Vytvořte pravidlo

1. V **Nastavení → Automatizace a scény** vytvořte novou prázdnou automatizaci.
2. Přidejte spouštěč **Stav** a vyberte senzor svého okna. Nastavte přechod ze zavřeného stavu do otevřeného: **Z** `off`, **Do** `on`. V nabídce mohou být místo těchto hodnot slova Zavřeno a Otevřeno.
3. Do pole pro dobu trvání, označeného například **Po dobu**, vložte deset minut (`00:10:00`). Nejde o samostatnou akci čekání: dobu nastavujete přímo u spouštěče.
4. Přidejte stejnou oznamovací akci telefonu, kterou jste už vyzkoušeli. Zpráva může znít: „Okno v ložnici je už deset minut otevřené.“
5. Uložte pravidlo jako **Otevřené okno v ložnici** a ponechte je zapnuté. Názvy voleb se mohou podle verze a jazyka lišit.

## Ověřte skutečné otevření

Pro první zkoušku zkraťte dobu na jednu minutu. Okno zavřete a znovu otevřete. Po minutě má přijít zpráva. Potom ověřte druhý případ: okno otevřete a zavřete dříve než za minutu. Zpráva přijít nemá. Nakonec vraťte deset minut.

## Co od pravidla čekat

Za jedno nepřerušené otevření pošle jedinou zprávu. Další dostanete až po zavření, novém otevření a uplynutí celé doby. Pravidlo po uložení zpětně nezměří okno, které už bylo otevřené; pro zkoušku je vždy zavřete a znovu otevřete.

Čekání na dobu trvání se při restartu Home Assistantu nebo znovunačtení automatizací zruší. Tento jednoduchý postup proto není zárukou upozornění v každé situaci. Pokud zpráva chybí, ověřte stav senzoru, vybraný telefon a záznam průběhu automatizace.

## Zdroje

- [Home Assistant: spouštěč Stav, doba trvání a příklad připomínky](https://www.home-assistant.io/triggers/state/)
- [Home Assistant: význam stavů binárních senzorů](https://www.home-assistant.io/integrations/binary_sensor/)
- [Companion: odesílání oznámení do telefonu](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
- [Home Assistant: oznamovací akce](https://www.home-assistant.io/integrations/notify/)
- [Home Assistant: kontrola průběhu automatizací](https://www.home-assistant.io/docs/automation/troubleshooting/)
