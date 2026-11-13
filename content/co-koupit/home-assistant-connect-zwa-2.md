---
title: "Home Assistant Connect ZWA-2: kdy dává smysl"
description: "Oficiální Z-Wave adaptér pro Home Assistant: co umí, co potřebujete a co zkontrolovat před nákupem."
cas: "5 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - ZWA-2
  - Z-Wave
  - Z-Wave Long Range
  - hardware
---

Chcete k Home Assistant připojit Z-Wave čidla, zásuvky nebo hlavice? **Home Assistant Connect ZWA-2** je oficiální USB adaptér, který počítači s Home Assistant přidá Z-Wave rádio. Nenahrazuje [Home Assistant Green](/co-koupit/home-assistant-green/) ani jiný počítač, na kterém systém běží. Smysl má tehdy, když chcete začít se Z-Wave nebo zvažujete výměnu stávajícího adaptéru.

## Co kupujete

ZWA-2 používá čip Z-Wave řady 800 a podporuje běžný Z-Wave i **Z-Wave Long Range**. K počítači se připojuje přes USB; na základně má konektor USB-C. V balení je anténa, základna a kabel dlouhý 1,5 metru.

Rozměry sestaveného zařízení jsou 125 × 125 × 315 mm. Před nákupem proto počítejte s místem pro základnu a přibližně 32 cm vysokou anténu. Je určené pouze pro použití uvnitř.

Oficiální hardware navrhuje Nabu Casa, společnost se sídlem v USA. Sídlo společnosti není údaj o zemi výroby konkrétního kusu. Nákup podle výrobce podporuje rozvoj projektů Open Home Foundation.

## Běžný Z-Wave a Long Range

Klasický Z-Wave může využívat síť, ve které zprávy předávají další zařízení. Long Range používá přímé spojení mezi koncovým zařízením a adaptérem, tedy hvězdicové uspořádání. ZWA-2 zvládá oba typy sítí současně.

**Long Range musí podporovat i čidlo nebo jiný připojený výrobek.** Starší zařízení se pouhou výměnou adaptéru nestane zařízením Long Range. Výhodou je možnost dál používat běžné Z-Wave výrobky a postupně přidávat nové.

## Co ověřit před objednávkou

Nejdůležitější je region. Z-Wave používá v různých částech světa jiné frekvence. Pro domácnost v Česku vybírejte koncová zařízení určená pro evropský region. Americké čidlo není vhodná náhrada jen proto, že se prodává levněji. U koncových zařízení frekvenci běžně nepřepnete.

Ověřte také dostupný USB port a způsob připojení adaptéru k instalaci Home Assistant. U virtuálního stroje potřebujete předat USB zařízení do jeho prostředí. Home Assistant používá pro komunikaci integraci Z-Wave a server Z-Wave JS; s Home Assistant OS je nastavení jednodušší díky spravované aplikaci.

ZWA-2 nepřipojí Zigbee ani Thread zařízení. Pokud kupujete čidlo, zkontrolujte jeho skutečný protokol. S orientací pomůže článek [Zigbee, Wi-Fi, Thread a Matter jednoduše](/co-koupit/zigbee-wifi-thread-matter/).

## Dosah a první zapojení

Velká anténa je navržená pro Z-Wave, ale nezaručuje konkrétní dosah ve vašem domě. Výsledek ovlivní zdi, umístění adaptéru i anténa koncového zařízení. Údaje o dosahu z testů výrobce proto nepovažujte za příslib pro svůj byt nebo zahradu.

Po připojení projděte průvodcem Home Assistant, zkontrolujte region a přidejte první zařízení podle jeho návodu. Pro začátek zvolte jednu zásuvku nebo čidlo, jehož chování můžete snadno ověřit. YAML pro samotný nákup ani tento průvodce není potřeba.

Při výměně stávajícího adaptéru nejprve zazálohujte Z-Wave síť a ověřte postup migrace pro svůj model. Automatický převod je dostupný pro mnoho moderních adaptérů, nikoli bez podmínek pro každý starý kus.

**ZWA-2 dává smysl jako vstup do Z-Wave nebo promyšlený upgrade.** Pokud už vaše síť spolehlivě funguje, nejprve si určete, co má výměna vyřešit. Aktuální cenu a dostupnost ověřte u prodejce z oficiálního seznamu na stránce produktu.

## Zdroje

- [Home Assistant: Connect ZWA-2, specifikace a prodejci](https://www.home-assistant.io/connect/zwa-2/)
- [Home Assistant: integrace Z-Wave, regiony a zálohy](https://www.home-assistant.io/integrations/zwave_js/)
- [Z-Wave Alliance: rozdíl mezi Z-Wave a Long Range](https://z-wavealliance.org/what-is-z-wave-long-range-how-does-it-differ-from-z-wave/)
- [Nabu Casa: podpora Connect ZWA-2](https://support.nabucasa.com/hc/en-us/categories/28669861145885)
- [Nabu Casa: informace o poskytovateli](https://www.nabucasa.com/privacy/)
