---
title: "První spuštění Home Assistant Green"
description: "Od zapojení po první otevření ovládání, které běží u vás doma."
obrazek: "/assets/images/prvni-spusteni.png"
obrazek_alt: "Ilustrace prvního nastavení domácí řídicí jednotky s propojením zařízení uvnitř domácnosti."
cas: "30–60 minut"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-10-06"
stav: "Podle dokumentace"
temata:
  - "Home Assistant Green"
  - "Začínáme"
  - "Lokální provoz"
  - "Domácí síť"
---

## Home Assistant běží u vás doma
**Home Assistant na Green je místní systém.** Ovládání, konfigurace a historie jsou uložené na vašem zařízení doma. Pro běžný lokální provoz nepotřebujete cloud ani předplatné Home Assistant Cloud. Účet vytvořený při prvním spuštění je účet vašeho domácího Home Assistant.

Po dokončení instalace může ovládání lokálně připojených zařízení i automatizace fungovat **bez internetu**. Stačí běžící Green, napájení zařízení a funkční domácí síť. Výpadek internetové přípojky není totéž jako vypnutí routeru: router a Wi-Fi potřebujete pro přístup z telefonu nebo počítače.

Záleží také na připojených službách. Zařízení ovládané pouze přes cloud výrobce při výpadku internetu fungovat nemusí. Stejně tak online předpověď počasí nebo cloudový AI model. Při výběru zařízení proto ověřujte podporu místního ovládání.

## Co budete potřebovat
[Home Assistant Green](/co-koupit/home-assistant-green/), jeho napájení, síťový kabel, router a mobil nebo počítač ve stejné domácí síti. **Pro první přípravu potřebujete také internet**, aby se stáhly potřebné součásti. Internet slouží i pro stahování aktualizací.

Green lze koupit například na [Alza.cz – Home Assistant Green](https://www.alza.cz/home-assistant-green-d7998187.htm). Cenu a dostupnost ověřte přímo u prodejce. Pokud sestavu teprve vybíráte, projděte si [co budete potřebovat](/zaciname/co-budu-potrebovat/).

## Postup
1. Propojte Green síťovým kabelem s routerem.
2. Připojte napájení a nechte dokončit úvodní přípravu.
3. V prohlížeči otevřete adresu `http://homeassistant.local:8123`.
4. Pokud adresa nefunguje, zjistěte v routeru IP adresu zařízení a otevřete ji s koncovkou `:8123`.
5. Průvodce vás provede vytvořením účtu a nastavením domácnosti. Heslo bezpečně uložte.
6. Podívejte se, zda Home Assistant našel zařízení v síti. Připojujte pouze ta, která poznáváte.

## Jak poznáte, že je hotovo
Vidíte úvodní přehled a můžete otevřít Nastavení. Přihlášení vyzkoušejte také z dalšího zařízení ve stejné síti.

## Když se stránka neotevře
Ověřte napájení, síťový kabel a společnou domácí síť. Hostovská Wi-Fi může spojení mezi zařízeními blokovat. Při první přípravě zařízení potřebuje čas i přístup k internetu.

## Co dál
[Nastavte zálohování](../../pomoc/zalohovani/), potom připojte první podporované zařízení podle jeho dokumentace.

## Zdroje
- [Instalace Home Assistant Green](https://www.home-assistant.io/installation/green/)
- [Home Assistant Green: místní provoz a první nastavení](https://www.home-assistant.io/green/)
- [Home Assistant: vytvoření účtu a úvodní nastavení](https://www.home-assistant.io/getting-started/onboarding/)
- [Alza.cz: Home Assistant Green](https://www.alza.cz/home-assistant-green-d7998187.htm)
