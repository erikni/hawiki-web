---
title: "Upozornění na vodu pod pračkou"
description: "Nechte si poslat zprávu, když připojený senzor zaznamená vodu."
cas: "20 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Únik vody"
  - "Upozornění"
---

## Co bude na konci fungovat

Když připojený senzor úniku vody ohlásí vodu, Home Assistant odešle upozornění do vašeho telefonu. Zpráva vám pomůže zjistit, že je potřeba místo zkontrolovat. Tento návod nastavuje oznámení; automatické uzavření vody vyžaduje další zařízení a samostatný postup.

## Co budete potřebovat

Připravte si fungující Home Assistant, již připojený senzor úniku vody a telefon s [nastavenou aplikací Companion](../../zaciname/home-assistant-v-mobilu/). Povolte oznámení. Připojení senzoru i jeho umístění proveďte podle návodu konkrétního výrobce. Článek nevybírá konkrétní model.

V Home Assistantu najděte entitu detekce vody. U binárního senzoru typu **moisture** znamená `on` mokro a `off` sucho; rozhraní může tyto stavy zobrazovat slovně. Nezaměňte ji se senzorem vzdušné vlhkosti, který ukazuje procenta. Před tvorbou pravidla ověřte, co přesně vaše zařízení nabízí.

## Nejprve odešlete zkušební zprávu

V **Nastavení → Nástroje → Akce** vyhledejte oznamovací akci telefonu. Ve starších verzích může být tato část pod Vývojářskými nástroji. Označení akce začíná `notify.mobile_app_` a pokračuje názvem zařízení. Zadejte zprávu „Zkouška upozornění na vodu“ a akci spusťte.

Zpráva musí přijít na správný telefon. Pokud nepřijde, ověřte připojení k internetu, povolená oznámení a režim Nerušit. Samotné fungující ovládání domácnosti v aplikaci ještě neověřuje doručování zpráv.

## Vytvořte pravidlo bez čekání

1. Otevřete **Nastavení → Automatizace a scény** a vytvořte novou prázdnou automatizaci.
2. Přidejte spouštěč **Stav** a vyberte entitu detekce vody. Do pole **Do** vložte `on`, případně vyberte odpovídající slovní stav Mokro. Pole **Z** ponechte prázdné.
3. Nenastavujte dobu trvání ani akci čekání. Pravidlo má reagovat při oznámení mokrého stavu.
4. Přidejte vyzkoušenou oznamovací akci telefonu. Zpráva může znít: „Senzor u pračky hlásí vodu. Zkontrolujte místo.“
5. Pravidlo uložte pod názvem **Voda u pračky** a ponechte je zapnuté. Názvy voleb se mohou lišit podle verze a jazyka.

Prázdné pole Z dovolí reakci i tehdy, když senzor přejde do mokrého stavu například po obnovení dostupnosti. Neznamená to však pravidelnou kontrolu: pokud už má při vytvoření pravidla stav mokro, nemusí vzniknout nový přechod a zpráva se sama neodešle.

## Ověřte senzor i celé pravidlo

Na bezpečném místě vyzkoušejte detekci pouze způsobem předepsaným výrobcem. Nepolévejte prostor pod připojenou pračkou. Sledujte změnu stavu v Home Assistantu a příchod zprávy; potom senzor podle návodu vraťte do suchého stavu. Testovací tlačítko nemusí u každého modelu představovat stejnou zkoušku jako detekce vody.

Ruční volba **Spustit akce** prověří odeslání zprávy, ale neověří senzor ani spouštěč. Když fyzická zkouška nevyjde, podívejte se na [záznam průběhu automatizace](../../pomoc/automatizace-nefunguje/) a ověřte vybranou entitu.

## Co od upozornění čekat

Pravidlo neposílá opakované připomínky během nepřerušeného mokrého stavu. Další změna do mokra může vyvolat další zprávu. Doručení závisí na funkčním senzoru, Home Assistantu a oznamovací cestě do telefonu. Oznámení proto nenahrazuje kontrolu místa ani pravidelné ověřování senzoru podle výrobce.

## Zdroje

- [Home Assistant: binární senzory a stav moisture](https://www.home-assistant.io/integrations/binary_sensor/)
- [Home Assistant: stavový spouštěč](https://www.home-assistant.io/triggers/state/)
- [Companion: odesílání oznámení](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
- [Home Assistant: oznamovací akce](https://www.home-assistant.io/integrations/notify/)
- [Home Assistant: zkoušky automatizací](https://www.home-assistant.io/docs/automation/troubleshooting/)
