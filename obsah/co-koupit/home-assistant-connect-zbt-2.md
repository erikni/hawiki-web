---
title: "Home Assistant Connect ZBT-2: Zigbee, nebo Thread?"
description: "Co umí oficiální USB adaptér ZBT-2 a jak se před nákupem rozhodnout mezi Zigbee a Thread."
cas: "5 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - ZBT-2
  - Zigbee
  - Thread
  - Matter
  - hardware
---

Chcete připojit Zigbee čidla a světla přímo k Home Assistant, nebo budujete síť Thread? **Home Assistant Connect ZBT-2** je oficiální USB adaptér pro tyto dva účely. Doplňuje počítač s Home Assistant, sám systém neprovozuje. Před nákupem si vyberte, jaká zařízení má obsluhovat.

## Jedno rádio, jedna volba

ZBT-2 podporuje **Zigbee 3.0 nebo Thread**, nikoli oba protokoly současně. Pokud chcete vlastní Zigbee síť i vlastní Thread rádio, potřebujete dvě samostatná rádia. Pro Thread ale můžete využít i vhodný border router, který už doma máte.

Pro Zigbee lze ZBT-2 použít jako koordinátor s integrací **ZHA**. Dokumentace Home Assistant jej doporučuje pro novou Zigbee síť. [Home Assistant Green](/co-koupit/home-assistant-green/) nemá Zigbee rádio vestavěné, takže mu tento adaptér doplní potřebné připojení.

V režimu Thread slouží adaptér s příslušným softwarem Home Assistant jako součást **Thread border routeru**, který propojuje Thread síť s domácí sítí. Pro tuto cestu počítejte s nastavením aplikace OpenThread Border Router podle návodu výrobce.

## Kde do toho patří Matter

Thread zajišťuje síťové spojení, **Matter** určuje způsob ovládání zařízení. Samotný nápis Matter na krabičce proto neznamená, že potřebujete ZBT-2. Matter zařízení přes Wi-Fi používá domácí síť; Matter přes Thread potřebuje Thread border router. Pro ovládání Matter zařízení v Home Assistant nastavíte také integraci Matter.

Pokud už máte funkční Thread border router, nejprve ověřte možnost využití jeho sítě. Nákup dalšího rádia nemusí být nutný. U konkrétního výrobku zkontrolujte, zda skutečně používá Zigbee, Matter přes Thread, nebo Matter přes Wi-Fi.

## Co dostanete a kam adaptér umístit

ZBT-2 používá rádiový čip **Silicon Labs MG24** a připojení USB-C. Sestavené zařízení měří 83 × 83 × 179 mm a váží 157 g. V balení je základna, anténa a USB-C kabel dlouhý 1,5 metru. Je určené pro použití uvnitř.

Adaptér je výrazně větší než malý USB dongle. Vyhraďte mu místo přibližně 18 cm na výšku a využijte kabel k vhodnému umístění. Dosah závisí na zdech, okolním rušení i rozmístění zařízení. Novější čip nebo větší anténa samy o sobě nezaručují pokrytí celého domu.

Oficiální hardware navrhuje Nabu Casa, společnost se sídlem v USA. Sídlo firmy není údaj o zemi výroby konkrétního kusu. Podle výrobce nákup podporuje rozvoj projektů Open Home Foundation.

## Co zkontrolovat před koupí

Ověřte volný USB port a přístup k němu z instalace Home Assistant. U virtuálního stroje je potřeba USB zařízení předat do jeho prostředí. Pro začátečníka je nejjednodušší vycházet z aktuálního návodu pro Home Assistant OS a zvolený protokol.

Při přechodu ze staršího adaptéru nejprve vytvořte zálohu a přečtěte postup migrace pro svou integraci. Neodstraňujte původní síť jen proto, že jste připojili nové rádio. Pokud už máte ZBT-1 a vše funguje, jeho podpora v ZHA pokračuje; výměna není automaticky nutná.

**ZBT-2 je vhodný pro začátek se Zigbee nebo pro vlastní Thread připojení.** Z-Wave zařízení nepřipojí: pro ně je určen [Home Assistant Connect ZWA-2](/co-koupit/home-assistant-connect-zwa-2/). Aktuální cenu a prodejce najdete na oficiální stránce produktu. Samotné zprovoznění se řídí průvodcem a dokumentací zvoleného režimu; tento nákupní přehled YAML nevyžaduje.

## Zdroje

- [Home Assistant: Connect ZBT-2 a specifikace](https://www.home-assistant.io/connect/zbt-2/)
- [Home Assistant: ZHA, kompatibilní adaptéry a migrace](https://www.home-assistant.io/integrations/zha/)
- [Home Assistant: Thread a border routery](https://www.home-assistant.io/integrations/thread/)
- [Home Assistant: Matter](https://www.home-assistant.io/integrations/matter/)
- [Nabu Casa: podpora Connect ZBT-2](https://support.nabucasa.com/hc/en-us/categories/29400540866973)
- [Nabu Casa: informace o poskytovateli](https://www.nabucasa.com/privacy/)
