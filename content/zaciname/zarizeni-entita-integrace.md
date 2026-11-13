---
title: "Zařízení, entita a integrace: co tato slova znamenají"
description: "Na příkladu chytré zásuvky se vyznáte v základních pojmech Home Assistantu."
cas: "5 minut čtení"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Zařízení"
  - "Entity"
  - "Integrace"
---

## Jedna zásuvka, několik položek

Připojíte chytrou zásuvku a Home Assistant ukáže víc položek, než jste čekali. Vedle zapnutí můžete vidět příkon nebo spotřebu. Neznamená to, že máte několik zásuvek. Systém odděluje připojení výrobku, samotné zařízení a jeho jednotlivé funkce.

Následující zásuvka je ilustrační příklad, nikoli doporučení konkrétního výrobku. Měření nabídne jen model a integrace, které tuto funkci podporují.

## Integrace: spojení s Home Assistantem

**Integrace** je softwarová část, která propojí Home Assistant se zařízením nebo službou. Zajišťuje, aby systém získával údaje a mohl posílat podporované povely. Podle výrobku může spojení vést přímo po domácí síti, přes bránu nebo přes službu na internetu.

Jedna integrace může zpřístupnit více zařízení. Například integrace pro určitou bránu může připojit světla, která s bránou komunikují. Název integrace proto nemusí být názvem jednoho výrobku. Vhodný způsob připojení vždy ověřte v dokumentaci dané integrace.

## Zařízení: společné místo pro funkce výrobku

**Zařízení** seskupuje související položky. U naší zásuvky si jej představte jako stránku celého výrobku: najdete na ní jeho dostupné funkce a údaje.

V běžných případech odpovídá jednomu fyzickému výrobku, ale není to pevné pravidlo. Home Assistant může takto reprezentovat i službu nebo více částí složitějšího výrobku. Pro začátek vám stačí vědět, že stránka zařízení pomáhá najít jeho související entity pohromadě.

## Entita: konkrétní ovládání nebo údaj

**Entita** představuje jednu sledovanou veličinu, ovládání nebo jinou funkci. U příkladové zásuvky může jít o tyto položky:

| Entita | K čemu slouží |
| --- | --- |
| Spínač zásuvky | Zapnutí a vypnutí napájení |
| Senzor příkonu | Aktuální odběr, obvykle ve wattech |
| Senzor energie | Naměřená spotřeba, například v kilowatthodinách |

Každá entita má svůj stav. Spínač může být zapnutý nebo vypnutý, senzor ukazuje naměřenou hodnotu. Entita může mít také doplňující údaje, například jednotku měření.

Technický identifikátor entity vypadá například jako `switch.lampa` nebo `sensor.lampa_prikon`. Část před tečkou označuje typ, zvaný doména. Zobrazený název může být přívětivější, například **Lampa v obýváku**. Uvedené identifikátory jsou pouze příklady; ve vaší domácnosti budou jiné.

## Kde se na to podívat

Otevřete **Nastavení → Zařízení a služby**. V části Integrace najdete nastavená propojení, v části Zařízení jednotlivá zařízení a v části Entity seznam konkrétních položek. Otevřete známé zařízení a podívejte se, které entity nabízí. Pro tuto orientaci není potřeba nic přejmenovávat ani mazat.

## Proč vám to pomůže v návodech

Při přidávání karty do [přehledu domácnosti](../../navody/prehled-domacnosti/) vybíráte konkrétní ovládání nebo údaj. Chcete-li lampu zapínat přes zásuvku, potřebujete její spínač. Chcete-li vidět odběr, vyberete senzor příkonu. Stejný výrobek, ale jiný účel.

Když návod žádá výběr entity, hledejte především správnou funkci. Samotný podobný název výrobku nestačí. Toto rozlišení usnadní tvorbu přehledů i hledání chyb v automatizacích.

## Zdroje

Ověřeno podle dokumentace 1. října 2026; ilustrační příklad nebyl testován na zařízení.

- [Home Assistant: základní pojmy](https://www.home-assistant.io/getting-started/concepts-terminology/)
- [Home Assistant: entity, domény a identifikátory](https://www.home-assistant.io/docs/configuration/entities_domains/)
- [Home Assistant: přidání integrace a zobrazení podrobností](https://www.home-assistant.io/getting-started/integration/)
- [Vývojářská dokumentace Home Assistantu: zařízení a seskupení entit](https://developers.home-assistant.io/docs/device_registry_index/)
