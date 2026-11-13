---
title: "Jaký počítač potřebujete pro místní AI?"
description: "CPU, GPU a paměť srozumitelně. Kdy zvolit Mac mini a kdy počítač s NVIDIA."
obrazek: "/assets/images/hardware-pro-mistni-modely.png"
obrazek_alt: "Mac mini a stolní počítač s grafickou kartou jako dvě možnosti pro domácí AI server."
cas: "7 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-03"
stav: "Podle dokumentace"
temata:
  - "AI"
  - "Místní modely"
  - "Hardware"
  - "GPU"
  - "Mac mini"
  - "NVIDIA"
---

## Proč provozovat AI doma
Místní model zpracovává požadavky na vašem počítači. Se staženým modelem a místními službami můžete pracovat bez internetu a neposílat dotazy cloudovému poskytovateli. Neplatíte za odpovědi v API. Platíte však hardware, elektřinu a vlastní údržbu.

Pro Home Assistant může AI běžet na samostatném počítači. HA dál řídí zařízení a přes domácí síť oslovuje model. Hlas potřebuje navíc přepis a syntézu řeči; místní model s cloudovým přepisem ještě neznamená plně soukromého asistenta.

## Co skutečně ovlivňuje výkon
- **CPU** je hlavní procesor. Model na něm může odpovídat pomalu.
- **GPU** provádí mnoho výpočtů souběžně. Podporovaná grafická karta může generování výrazně urychlit; samotný počet jader CPU není dobré nákupní vodítko.
- **Paměť** musí pojmout model i pracovní data konverzace. Dlouhá historie a více souběžných požadavků nároky zvyšují.
- **SSD** drží stažené modely a urychluje jejich načítání. Disk nenahradí paměť.

U samostatné NVIDIA karty sledujte **VRAM**, její vlastní paměť. 32 GB RAM v PC neznamená 32 GB pro GPU. Pokud se model nevejde do VRAM, část výpočtu může přejít na CPU a zpomalit. Na Macu CPU a GPU sdílejí **jednotnou paměť**, ale část zabere systém a ostatní aplikace.

## Kolik paměti vybrat
Tabulka je odhad pro krátkou konverzaci, ne záruka výkonu. Rozhoduje konkrétní model, jeho kvantizace a nastavení. Kvantizace ukládá parametry úsporněji, někdy za cenu kvality.

| Účel | Mac: jednotná paměť | PC: orientační VRAM |
| --- | --- | --- |
| Malé modely 1–4B, první pokusy | 16 GB | 8 GB |
| Modely přibližně 7–12B | 24–32 GB | 12–16 GB |
| Větší modely a delší konverzace | 48–64 GB a více | 24 GB a více |

**B** označuje miliardy parametrů. Hranice nejsou pevné: model se může vejít, ale reagovat příliš pomalu. PC potřebuje také systémovou RAM; jako praktický začátek bych volil 32 GB. Před nákupem model vyzkoušejte na podobné sestavě.

## Proč Mac mini M4 nebo M6
Mac mini je celý kompaktní počítač s GPU. Sdílená paměť dovoluje GPU využívat větší část paměťového prostoru bez nákupu samostatné karty. Pro běžného domácího uživatele bych začal konfigurací **24–32 GB**; 16 GB je vhodných spíš pro malé modely.

M4 může být zajímavý za výhodnou cenu, M6 je novější možnost. Paměť vybírejte při nákupu, nepočítejte s pozdějším běžným rozšířením. Základní M4 i M6 končí na 32 GB; pro 48–64 GB potřebujete odpovídající variantu Pro nebo jiný Mac. Záleží i na rychlosti čtení paměti. Novější čip s malou pamětí nevyřeší příliš velký model.

## Kdy dává smysl NVIDIA
Podporovaná NVIDIA karta je dobrá volba, pokud už máte vhodné PC nebo chcete GPU později měnit. Nabízí výkon a širokou podporu AI softwaru. Například RTX 5070 má 12 GB VRAM, RTX 5070 Ti 16 GB; právě paměť může rozhodnout, jaký model provozujete.

K ceně karty připočtěte zbytek PC, dostatečný zdroj, chlazení a provozní spotřebu. Mac není vždy levnější a NVIDIA není vždy rychlejší: porovnejte stejný model a celkovou cenu sestavy. Funkční kartu, kterou už máte, nejprve využijte. Kompatibilitu ověřte v dokumentaci Ollama.

## Co místní AI neumí stejně dobře
Domácí hardware obvykle vede k menším modelům. Ty mohou hůře chápat složité pokyny, češtinu nebo spolehlivě volat nástroje než silné cloudové modely. Nejsou automaticky „hloupé“: pro úzký úkol mohou stačit. Větší model také není záruka správné odpovědi.

Pro Assist začněte jednou lampou a ověřujte skutečné akce. Ovládání přes Ollama je experimentální. Instalaci popisuje [průvodce Ollama](../ollama-instalace-modely-hardware/), propojení s HA [vlastní AI server](../mistni-modely-vlastni-ai-server/).

## Zdroje
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Ollama: podporovaný hardware](https://docs.ollama.com/gpu)
- [Ollama: paměť, místní provoz a souběžné požadavky](https://docs.ollama.com/faq)
- [Apple: Mac mini M4](https://support.apple.com/cs-cz/121555)
- [Apple: Mac mini M6 a varianty Pro](https://www.apple.com/cz/mac-mini/specs/)
- [NVIDIA: RTX 5070 a 5070 Ti](https://www.nvidia.com/cs-cz/geforce/graphics-cards/50-series/rtx-5070-family/)
