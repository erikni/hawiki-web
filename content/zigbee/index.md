---
type: hub
title: "Zigbee v Home Assistant: kompletní průvodce"
seoTitle: "Zigbee v Home Assistant: ZHA, Zigbee2MQTT a návody"
description: "Vyberte způsob připojení Zigbee zařízení, pochopte síť mesh a pokračujte k vhodnému adaptéru i prvnímu návodu."
kontrola_zdroju: "2026-10-08"
---

## Co je Zigbee a kde začít

Zigbee propojuje například světla, zásuvky a senzory do vlastní bezdrátové sítě. Pro přímé připojení k Home Assistantu potřebujete podporovaný koordinátor a software, který síť spravuje. Nejdříve si ujasněte, jaké zařízení chcete ovládat a které jeho funkce potřebujete. Nákup rádia je až další krok.

Pokud v názvech tápete, začněte [vysvětlením Zigbee, Wi-Fi, Thread a Matter](/co-koupit/zigbee-wifi-thread-matter/). Nejde o vzájemně zaměnitelné značky. Stejně tak adaptér pro Z-Wave nenahradí Zigbee koordinátor. Tento rozcestník vás provede výběrem a odkáže na podrobnosti tam, kde je budete potřebovat.

## Jak funguje síť mesh

Koordinátor zakládá síť; zařízení v roli směrovačů mohou předávat zprávy dál. Bateriové senzory obvykle zprávy dalších zařízení nepřenášejí. Při rozšiřování domácnosti proto myslete na rozmístění napájených směrovačů, nejen na počet senzorů. Konkrétní schopnosti vždy ověřte pro daný výrobek.

Výpadek jednoho senzoru není důvodem hned měnit celou síť. Nejprve zkontrolujte baterii, dostupnost a umístění. Při problémech po přesunu zařízení využijte postup [když zařízení nereaguje](/pomoc/zarizeni-nereaguje/).

## Koordinátor a doporučené vybavení

Vyberte rádio podle podpory v zamýšleném softwaru. Na HAwiki najdete [průvodce Home Assistant Connect ZBT-2](/co-koupit/home-assistant-connect-zbt-2/). Před nákupem zkontrolujte také připojení adaptéru k vašemu počítači a dokumentaci přesného modelu. Jeden návod k produktu není univerzálním příslibem kompatibility.

## ZHA nebo Zigbee2MQTT

ZHA je integrace uvnitř Home Assistantu. Zigbee2MQTT je samostatný software, který předává zařízení přes MQTT. Obě cesty vyžadují vhodný koordinátor. V [porovnání ZHA a Zigbee2MQTT](/zigbee/zha-vs-zigbee2mqtt/) najdete rozdíly v přípravě a správě. Rozhodujte se podle konkrétních zařízení a ochoty udržovat další software.

## Přidání prvního zařízení

Začněte jedním senzorem nebo světlem. Podle zvolené cesty povolte připojení a spusťte párování postupem výrobce. Po přidání ověřte požadovanou funkci v Home Assistantu, teprve potom stavte automatizaci. Pro orientaci pomůže [vysvětlení zařízení, entity a integrace](/zaciname/zarizeni-entita-integrace/).

## Zdroje

- [Home Assistant: ZHA](https://www.home-assistant.io/integrations/zha/)
- [Zigbee2MQTT: první kroky](https://www.zigbee2mqtt.io/guide/getting-started/)
