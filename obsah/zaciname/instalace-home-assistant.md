---
title: "Jak nainstalovat Home Assistant"
seoTitle: "Jak nainstalovat Home Assistant: Green, Raspberry Pi a mini PC"
description: "Vyberte způsob instalace podle zkušeností a vybavení. Green, Raspberry Pi, mini PC, virtuální stroj nebo Container."
cas: "5 minut čtení"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-10-08"
stav: "Podle dokumentace"
sourceType: "official-docs"
temata: ["Home Assistant", "Instalace", "Hardware"]
obrazek: "/assets/images/instalace-home-assistant.png"
obrazek_alt: "Ilustrace domácnosti a volby mezi hotovou řídicí jednotkou, jednodeskovým počítačem a mini PC."
related: ["zaciname/prvni-spusteni", "zaciname/co-budu-potrebovat", "pomoc/zalohovani"]
---

## Nejdříve zvolte způsob správy

Home Assistant potřebuje zařízení, které doma trvale běží. Pro většinu uživatelů dokumentace doporučuje **Home Assistant OS**: zahrnuje správu systému i možnost instalovat doplňkové aplikace. **Container** je určen pro lidi, kteří si spravují operační systém a kontejnery sami. Nejde o dva různé systémy ovládání domácnosti, ale o různé způsoby instalace a údržby.

Než nakoupíte, projděte si [co budete potřebovat](/zaciname/co-budu-potrebovat/) a [jak vybírat hardware](/co-koupit/jak-vybirat/). Tento článek pomáhá rozhodnout; podrobné instalační kroky najdete v odkazovaných návodech.

## Home Assistant Green: nejméně přípravy

Pro začátečníka, který chce hotové řešení. Home Assistant OS je předinstalovaný; zapojíte síť a napájení a dokončíte úvodní nastavení. Výhodou je jednoduchý začátek, nevýhodou nákup samostatné jednotky. Složitost je nízká. Redakční doporučení: zvolte [Home Assistant Green](/co-koupit/home-assistant-green/), pokud chcete hlavně používat domácnost a méně řešit počítač. Pokračujte na [první spuštění Green](/zaciname/prvni-spusteni/).

## Raspberry Pi: využití vlastní sestavy

Pro uživatele, kteří Pi už mají nebo chtějí sestavu připravit sami. Výhodou je malé zařízení, nevýhodou nutnost zajistit napájení a úložiště a nahrát obraz Home Assistant OS. Dokumentace popisuje Raspberry Pi 4 a 5. Složitost je střední. Doporučení: před nákupem porovnejte cenu celé sestavy, ne samotné desky; při instalaci postupujte podle aktuálního návodu pro Pi.

## Mini PC / x86: samostatný počítač

Pro domácnost s vhodným počítačem, který může být vyhrazen Home Assistantu. Výhodou je volba vybavení a úložiště, nevýhodou více práce s přípravou systému. Instalace OS na vybraný disk jeho obsah přepíše. Složitost je střední až vyšší; je potřeba ověřit podporu x86-64 a nastavení UEFI. Doporučení: použijte počítač, který můžete vyhradit tomuto účelu, a předem zachraňte potřebná data.

## Virtuální stroj / Proxmox

Pro uživatele, kteří už provozují virtualizační server. Výhodou je využití stávajícího hostitele, nevýhodou závislost domácnosti i na jeho správě. Home Assistant OS běží uvnitř virtuálního stroje. Složitost je vyšší: řešíte síť, úložiště a případné předání USB rádia. Proxmox je jedna z cest virtualizace; zde nejde o podrobný návod k jeho instalaci. Doporučení: zvolte tuto variantu, pokud prostředí umíte udržovat.

## Home Assistant Container

Pro zkušenější uživatele Linuxu a Dockeru. Výhodou je vlastní správa prostředí, nevýhodou ruční aktualizace a samostatná správa dalších služeb. Container nemá vestavěný systém doplňkových aplikací Home Assistant OS. Složitost je vyšší. Doporučení: vyberte jej, pokud už kontejnery používáte; pro první domácnost bývá OS přehlednější volba.

## Po instalaci

Přidejte [telefon](/zaciname/home-assistant-v-mobilu/) a nastavte [zálohování](/pomoc/zalohovani/). Potom ověřte jedno zařízení a teprve následně vytvořte první pravidlo.

## Zdroje

- [Home Assistant: možnosti instalace](https://www.home-assistant.io/installation/)
- [Home Assistant: Raspberry Pi](https://www.home-assistant.io/installation/raspberrypi/)
- [Raspberry Pi: příprava počítače a úložiště](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [Home Assistant: x86-64](https://www.home-assistant.io/installation/generic-x86-64/)
- [Home Assistant: virtuální stroje a Container](https://www.home-assistant.io/installation/alternative/)
