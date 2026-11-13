---
title: "ZHA vs Zigbee2MQTT: co zvolit pro Home Assistant"
seoTitle: "ZHA vs Zigbee2MQTT: co zvolit pro Home Assistant"
description: "Porovnejte přímou integraci ZHA a samostatné Zigbee2MQTT. Rozhodujte podle podpory zařízení a způsobu správy domácnosti."
cas: "4 minuty čtení"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-10-08"
stav: "Podle dokumentace"
sourceType: "official-docs"
temata: ["Zigbee", "ZHA", "Zigbee2MQTT", "Integrace"]
obrazek: "/assets/images/zha-vs-zigbee2mqtt.png"
obrazek_alt: "Ilustrace dvou cest propojení bezdrátových zařízení s domácností: přímo a prostřednictvím dalších softwarových služeb."
---

## Stejná potřeba, dvě cesty připojení

Chcete používat Zigbee senzor nebo světlo v Home Assistantu. Pro přímé připojení potřebujete koordinátor a software, který síť spravuje. **ZHA** tuto roli řeší jako integrace Home Assistantu. **Zigbee2MQTT** je samostatný software, který předává informace do Home Assistantu prostřednictvím MQTT. Samotná koupě adaptéru tedy volbu celé cesty neřeší.

Než začnete, projděte si [rozcestník Zigbee](/zigbee/) a ověřte konkrétní rádio i zařízení v dokumentaci zvoleného projektu. Neexistuje jedna nejlepší varianta pro všechny domácnosti.

## ZHA: správa v Home Assistantu

ZHA nastavujete v Home Assistantu a nepotřebujete k němu samostatný MQTT broker. Pro první zařízení je to méně součástí k přípravě. Dokumentace popisuje podporované rádiové adaptéry, párování a možnosti správy sítě.

Výhodou je soustředění nastavení na jednom místě. Omezením je, že některé výrobky mají nestandardní funkce a potřebují zvláštní podporu. Logo Zigbee nezaručuje zpřístupnění každé funkce. Redakční doporučení: pokud začínáte a potřebná zařízení jsou podporovaná, ZHA je přehledná první cesta.

## Zigbee2MQTT: samostatná služba

Zigbee2MQTT potřebuje podporovaný adaptér, běžící službu a MQTT broker. Home Assistant se připojí přes integraci MQTT; automatické rozpoznání zařízení využívá MQTT discovery. Služba může běžet vedle Home Assistantu, ale její instalaci a aktualizace musíte zahrnout do správy domácnosti.

Výhodou je oddělená správa Zigbee a katalog podporovaných zařízení s popisem jejich funkcí. Nevýhodou je více součástí, jejichž spojení musí fungovat. Doporučení: zvažte tuto cestu, pokud v ní máte doloženou podporu potřebného modelu nebo chcete Zigbee spravovat samostatně a rozumíte MQTT.

## Co ověřit před rozhodnutím

- **Koordinátor:** musí být podporován zvoleným softwarem, včetně požadovaného firmwaru.
- **Přesný model:** porovnávejte požadované funkce, ne jen jméno výrobce.
- **Správa:** u Zigbee2MQTT počítejte také s MQTT brokerem a propojením do Home Assistantu.
- **Obnova:** před rozšiřováním si zjistěte způsob zálohy a obnovy zvoleného řešení.

Jeden koordinátor nemohou současně řídit obě služby. Pokud chcete druhou cestu zkoušet vedle stávající sítě, potřebujete oddělené vhodné rádio. Při změně řešení nepočítejte automaticky s přenosem všech nastavení; naplánujte postup podle dokumentace a nezasahujte hned do celé domácnosti.

## Praktický začátek

Vyberte jednu cestu, připojte jedno zařízení a ověřte potřebnou funkci. Pak pokračujte na [první automatizaci](/navody/lampa-vecer/). Pokud zařízení nereaguje, nejdříve prověřte napájení a spojení podle [návodu k potížím](/pomoc/zarizeni-nereaguje/). Změna softwaru není první krok při každém výpadku.

## Zdroje

- [Home Assistant: ZHA](https://www.home-assistant.io/integrations/zha/)
- [Zigbee2MQTT: první kroky a požadavky](https://www.zigbee2mqtt.io/guide/getting-started/)
- [Zigbee2MQTT: propojení s Home Assistantem](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html)
- [Zigbee2MQTT: podporovaná zařízení](https://www.zigbee2mqtt.io/supported-devices/)
