---
type: hub
title: "Integrace Home Assistant"
seoTitle: "Home Assistant integrace: zařízení a služby"
description: "Propojte zařízení a služby různých výrobců. Začněte pojmy, vyberte způsob připojení a pokračujte k existujícím návodům."
kontrola_zdroju: "2026-10-08"
---

## Co integrace znamená

Integrace je propojení Home Assistantu s konkrétním zařízením, službou nebo technologií. Zpřístupňuje jejich funkce, které pak můžete používat v přehledu a automatizacích. Název výrobce ale neříká, že každý jeho produkt nabízí stejný způsob připojení. Hledejte přesný model a funkci, kterou opravdu potřebujete.

Začněte [vysvětlením zařízení, entity a integrace](/zaciname/zarizeni-entita-integrace/). Potom si vyberte první malý úkol: například ovládání světla nebo sledování otevřeného okna. Díky tomu budete vědět, zda hledáte vypínač, senzor nebo službu pro oznámení.

## Jak vybrat způsob připojení

U některých zařízení najde Home Assistant integraci automaticky, jiné přidáte ručně v Nastavení → Zařízení a služby. Postup vždy ověřte v dokumentaci dané integrace. Rozlišujte připojení přímo v domácí síti a připojení přes službu výrobce na internetu. Požadavky na účet a dostupné funkce se liší.

Před nákupem si projděte [průvodce protokoly](/co-koupit/zigbee-wifi-thread-matter/). U Zigbee pokračujte přes [tematický rozcestník](/zigbee/), který pomůže s koordinátorem a volbou softwaru. U zařízení s Matter nebo Thread zkontrolujte i potřebné vybavení domácí sítě.

## Zařízení Shelly

[Shrnutí zařízení Shelly](/co-koupit/shelly-zarizeni-prehled/) vysvětluje rozdíly mezi řadami a typy připojení. Oficiální integrace Shelly komunikuje s podporovanými zařízeními přímo; cloud není pro tuto komunikaci nutný. Nezaměňujte ale tuto cestu s připojením všech Bluetooth nebo Zigbee výrobků značky. Rozhoduje konkrétní model.

## Kamery a další software

Pokud řešíte kamery, projděte si [úvod do Frigate](/navody/kamery-frigate/). Pro rozšíření mimo standardní nabídku je k dispozici [průvodce HACS](/dalsi-moznosti/hacs/). Vždy nejprve ověřte, zda potřebná funkce už není v běžné integraci a kdo doplněk spravuje.

## Po připojení a při potížích

Zkontrolujte, že zařízení nabízí požadovanou entitu a reaguje na ovládání. Pojmenujte je srozumitelně podle místnosti a účelu. Teprve poté pokračujte k [automatizacím](/automatizace/). Pokud zařízení mizí nebo nereaguje, začněte kontrolou napájení a připojení; při závislosti na cloudu ověřte také internet.

Pro další značky zatím využijte katalog integrací v dokumentaci Home Assistantu. Samostatné průvodce na HAwiki přibudou s dostatkem ověřeného obsahu.

## Zdroje

- [Home Assistant: integrace a základní pojmy](https://www.home-assistant.io/getting-started/concepts-terminology/)
- [Home Assistant: integrace Shelly](https://www.home-assistant.io/integrations/shelly/)
- [Shelly: technická dokumentace](https://shelly-api-docs.shelly.cloud/)
