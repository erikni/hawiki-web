---
title: "Zigbee, Wi-Fi, Thread a Matter jednoduše"
description: "Vyznáte se v označeních a zjistíte, co ověřit před nákupem."
cas: "5 minut čtení"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Zigbee"
  - "Wi-Fi"
  - "Thread"
  - "Matter"
---

## Nejdříve vyberte funkci, potom připojení

Chcete senzor okna nebo chytré světlo? Na krabičce narazíte na několik různých označení. Nejsou to čtyři vzájemně zaměnitelné možnosti: Wi-Fi, Zigbee a Thread popisují síťovou komunikaci, zatímco Matter určuje společný způsob ovládání nad podporovanou sítí.

Pro Home Assistant proto ověřujte konkrétní model a funkce, které potřebujete. Samotné logo sítě ještě neříká, zda budete moci například stmívat světlo nebo číst příkon zásuvky.

## Wi-Fi: zařízení v domácí síti

Wi-Fi zařízení se připojuje k domácí bezdrátové síti. Pro samotné Wi-Fi nepotřebujete Zigbee koordinátor ani Thread border router. Způsob propojení s Home Assistantem ale závisí na výrobku: může používat vlastní integraci nebo Matter.

Označení Wi-Fi samo nepotvrzuje ovládání bez internetu. Před nákupem si v dokumentaci integrace ověřte, zda komunikuje místně, nebo potřebuje cloud výrobce. Zjistěte také, které funkce zpřístupňuje.

## Zigbee: vlastní síť pro chytrou domácnost

Pro přímé připojení přes integraci **ZHA** potřebuje Home Assistant podporovaný Zigbee koordinátor, například vhodný rádiový adaptér. Zigbee síť může předávat zprávy přes další zařízení, která fungují jako směrovače. Bateriový senzor obvykle tuto úlohu neplní.

ZHA podporuje standardní typy Zigbee zařízení, ale výrobci mohou používat nestandardní funkce. Nečekejte proto automaticky plnou podporu každého modelu. Pokud výrobek používá svou vlastní bránu, ověřte také možnost jejího propojení s Home Assistantem.

## Thread: síť, která potřebuje cestu do domácí sítě

Thread je síť navržená pro zařízení s nízkou spotřebou a podporuje předávání zpráv mezi uzly. Spojení s ostatní domácí sítí zajišťuje **Thread border router**, česky hraniční směrovač. Tuto funkci může poskytovat zařízení, které už doma máte, nebo vhodně nastavené vybavení Home Assistantu.

Samotná integrace Thread nenahrazuje potřebný rádiový hardware. A logo Thread není potvrzením Matter: existují i Thread zařízení s jiným způsobem ovládání. Ověřte obě označení a požadavky výrobce.

## Matter: společný způsob ovládání

Matter může běžet přes Wi-Fi, Ethernet nebo Thread. Home Assistant jej ovládá přes integraci Matter a Matter Server. U zařízení **Matter over Thread** navíc potřebujete Thread border router; u **Matter over Wi-Fi** jej kvůli tomuto zařízení nepotřebujete.

Ovládání přes Matter probíhá místně. Výrobce ale může například pro úvodní povolení Matter vyžadovat vlastní účet. Ani Matter nezaručuje všechny speciální funkce výrobku: vlastní integrace může nabídnout více možností. Porovnejte dostupné funkce obou cest.

## Oficiální adaptéry Home Assistant

[Connect ZBT-2](https://www.home-assistant.io/connect/zbt-2/) lze nastavit pro Zigbee, nebo pro Thread; oba režimy neprovozuje současně. Pro Thread potřebuje také nastavení hraničního směrovače.

[Connect ZWA-2](https://www.home-assistant.io/connect/zwa-2/) je adaptér pro další technologii **Z-Wave**. Nenahrazuje Zigbee koordinátor ani Thread adaptér.

## Co ověřit před nákupem

- Přesný model a požadovanou funkci v dokumentaci Home Assistantu a výrobce.
- Zda potřebujete koordinátor, bránu nebo Thread border router a zda už vhodné vybavení máte.
- Závislost na internetu a případnou potřebu účtu výrobce.
- U Matter zařízení také použitou síť, dostupnost párovacího kódu a požadavky na přidání do Home Assistantu.

Pro první pokus vyberte jedno zařízení s doloženým postupem připojení. Až ověříte jeho chování ve své domácnosti, rozšiřujte stejným způsobem další místnosti.

## Zdroje

- [Home Assistant: Zigbee a integrace ZHA](https://www.home-assistant.io/integrations/zha/)
- [Home Assistant: Thread a hraniční směrovače](https://www.home-assistant.io/integrations/thread/)
- [Home Assistant: Matter a požadavky na připojení](https://www.home-assistant.io/integrations/matter/)
- [Connectivity Standards Alliance: standard Matter](https://csa-iot.org/all-solutions/matter/)
- [Home Assistant: Connect ZBT-2](https://www.home-assistant.io/connect/zbt-2/)
- [Home Assistant: Connect ZWA-2](https://www.home-assistant.io/connect/zwa-2/)
