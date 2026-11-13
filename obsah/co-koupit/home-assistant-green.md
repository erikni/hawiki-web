---
title: "Home Assistant Green: co umí a co mu chybí"
seoTitle: "Home Assistant Green: hardware, možnosti a omezení"
description: "Home Assistant Green z pohledu hardwaru: výkon, porty, spotřeba, chybějící rádia a komu se vyplatí koupit."
obrazek: "/assets/images/home-assistant-green.jpg"
obrazek_alt: "Skutečná produktová fotografie Home Assistant Green s připojeným ethernetovým a napájecím kabelem."
cas: "6 minut čtení"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-11-13"
stav: "Podle dokumentace"
temata:
  - "Home Assistant Green"
  - "Home Assistant OS"
  - "hardware"
  - "Zigbee"
  - "Matter"
---

**Home Assistant Green** je hotová centrální jednotka s předinstalovaným Home Assistant OS. Zapojíte napájení a síťový kabel, dokončíte průvodce a získáte Home Assistant na samostatném zařízení. Nekupujete však univerzální počítač ani bezdrátovou bránu se všemi rádii. Green je především jednoduchý a úsporný základ, který lze podle potřeby doplnit přes USB.

## Hardware bez skládání

Uvnitř je čtyřjádrový procesor Rockchip RK3566 s jádry Arm Cortex-A55 na 1,8 GHz, 4 GB operační paměti a 32 GB vestavěného úložiště eMMC. Home Assistant i data běží lokálně. Velký hliníkový chladič nepotřebuje ventilátor, takže jednotka pracuje bez jeho hluku.

Green má gigabitový Ethernet a dva porty USB 2.0 typu A. Oba porty dohromady poskytují až 5 V / 2 A. Výrobce uvádí spotřebu přibližně 1,7 W v klidu a 3 W při zátěži. Krabička měří 112 × 112 × 32 mm a váží 340 g.

V balení je Green, gigabitový ethernetový kabel a univerzální zdroj 12 V / 1 A s koncovkami pro EU, USA a Velkou Británii. Pro běžné zapojení tedy nemusíte dokupovat napájení ani kabel k routeru.

## Co zvládne

Green provozuje plnou spravovanou instalaci Home Assistant OS včetně aktualizací, záloh a doplňkových aplikací. Připojí zařízení dostupná po domácí síti a podporované cloudové služby. Může lokálně řídit automatizace a ukládat historii; dostupnost konkrétního výrobku vždy závisí na jeho integraci a způsobu komunikace.

Matter zařízení přes Wi‑Fi nebo Ethernet lze používat po nastavení integrace Matter a Matter Serveru. Green přitom nemusí mít vlastní Wi‑Fi: komunikuje s nimi přes router.

## Co vestavěné není

Green se k domácí síti připojuje **pouze ethernetovým kabelem**. Nemá Wi‑Fi ani vestavěné rádio pro Zigbee, Thread či Z‑Wave. Zigbee nebo Thread doplní například [Connect ZBT-2](/co-koupit/home-assistant-connect-zbt-2/), pro Z‑Wave lze použít [Connect ZWA-2](/co-koupit/home-assistant-connect-zwa-2/). Jeden ZBT-2 ale neobslouží Zigbee a Thread současně.

HDMI konektor je určen pouze pro diagnostiku, ne pro běžné připojení monitoru. Slot microSD slouží k obnově systému, nikoli k rozšíření datového prostoru. Vestavěných 32 GB eMMC ani 4 GB RAM nelze běžně vyměnit; kdo chce výrazně rozšiřovat úložiště nebo provozovat další náročné služby, měl by zvážit mini PC či jiný server.

## Komu dává smysl

Green je vhodný pro začátečníka, který chce podporované zařízení bez skládání a správy Linuxu, i pro zkušenějšího uživatele, který chce Home Assistant oddělit od ostatních počítačů. Slabší stránkou je pevně daný hardware a nutnost přikoupit rádia pro některé protokoly. Připojené USB adaptéry navíc zaberou omezené porty.

V Česku jej 13. listopadu 2026 nabízela [Alza.cz](https://www.alza.cz/home-assistant-green-d7998187.htm). Cena a dostupnost se mění, proto je ověřte před objednávkou. Až zařízení vyberete, pokračujte samostatným návodem [První spuštění Home Assistant Green](/zaciname/prvni-spusteni/).

## Zdroje

- [Home Assistant: Home Assistant Green a technické parametry](https://www.home-assistant.io/green/)
- [Home Assistant: instalace Green](https://www.home-assistant.io/installation/green/)
- [Home Assistant: Matter](https://www.home-assistant.io/integrations/matter/)
- [Alza.cz: Home Assistant Green](https://www.alza.cz/home-assistant-green-d7998187.htm)
