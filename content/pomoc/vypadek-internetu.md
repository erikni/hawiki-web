---
title: "Co bude fungovat, když vypadne internet?"
description: "Rozlište místní a cloudové funkce a vyzkoušejte vlastní domácnost."
cas: "20 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Internet"
  - "Lokální ovládání"
---

## Internet a domácí síť nejsou totéž

Home Assistant běží doma a upřednostňuje místní ovládání. To ale neznamená, že každé připojené zařízení funguje bez internetu. Záleží na použité integraci i na tom, odkud automatizace získává údaje a kam posílá povely.

Výpadek internetu navíc není vypnutí routeru. Domácí Wi-Fi a spojení mezi zařízeními mohou dál pracovat, přestože není dostupný internet. Pro následující zkoušku ponechte Home Assistant, router, přístupové body a potřebné brány zapnuté.

## Které funkce mohou pokračovat

Místní ovládání světla může fungovat, pokud Home Assistant komunikuje přímo se zařízením nebo místní bránou. Příkladem je připojení Zigbee zařízení přes ZHA nebo ovládání přes Matter. Pořád musí fungovat příslušný hardware a síť.

Automatizace má šanci pokračovat, když jsou místní všechny potřebné části: spouštěč, podmínky i akce. Senzor pohybu a místně ovládané světlo mohou spolupracovat dál. Pokud však pravidlo čeká na údaj z internetové služby, samotné místní světlo nezajistí jeho správný výsledek.

## Kde čekat omezení

Integrace závislé na cloudu nemohou při výpadku získávat nové údaje nebo posílat povely přes službu výrobce. Internet potřebují také například nové předpovědi počasí nebo přístup k domácnosti zvenčí. Vzdálený přístup přes Home Assistant Cloud či VPN neobejde chybějící připojení domácnosti k internetu.

Oznámení do telefonu ověřujte samostatně. Běžné push zprávy používají internetové služby; existují i zvláštní možnosti místního doručování, ale nelze je předpokládat u každého nastavení. To, že se rozsvítilo světlo, nepotvrzuje doručení zprávy o vodě pod pračkou.

## Co zjistíte v dokumentaci integrace

Na stránce konkrétní integrace hledejte označení **IoT class**. Hodnoty **Local Push** a **Local Polling** popisují místní komunikaci, **Cloud Push** a **Cloud Polling** komunikaci přes cloud. Push znamená zasílání změn, polling pravidelné dotazování.

Berete tím první vodítko, nikoli záruku celé domácnosti. Ověřte i požadavky výrobku a další funkce, které používáte. Samotné označení Wi-Fi nerozhoduje, zda je zařízení závislé na cloudu; více vysvětluje [přehled sítí a Matter](../../co-koupit/zigbee-wifi-thread-matter/).

## Vyzkoušejte jednoduchý scénář

1. Vyberte jedno světlo a jednoduché pravidlo, například rozsvícení podle pohybu. Za běžného připojení ověřte skutečný výsledek.
2. V telefonu připojeném k domácí Wi-Fi otevřete místní adresu Home Assistantu. Nejdříve ověřte, že funguje i bez použití vzdálené adresy.
3. Podle návodu routeru dočasně odpojte pouze internetové připojení. Neodpojujte napájení routeru ani kabel spojující Home Assistant s domácí sítí. Poznamenejte si, jak připojení obnovíte.
4. V telefonu vypněte mobilní data, ponechte Wi-Fi a zopakujte ruční ovládání i skutečné spuštění pravidla. Zkontrolujte také nové změny stavů senzorů, ne jen staré hodnoty na obrazovce.
5. Internet znovu připojte, vraťte mobilní data a ověřte obnovení cloudových funkcí.

Zkoušku provádějte v době, kdy krátké odpojení nenaruší potřebné služby domácnosti. Pokud nevíte, který kabel nebo volbu použít, nejprve si postup ověřte v návodu svého routeru.

## Zapište si výsledek

Poznamenejte si, co fungovalo, co přestalo reagovat a co se po návratu internetu obnovilo. Tak získáte přehled o vlastní sestavě. Pro důležité úkoly si ponechte dostupné ruční ovládání a po změně zařízení nebo integrace příslušnou zkoušku zopakujte.

## Zdroje

- [Home Assistant: místní zpracování a ovládání](https://www.home-assistant.io/)
- [Home Assistant: klasifikace místní a cloudové komunikace](https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things/)
- [Home Assistant: integrace ZHA](https://www.home-assistant.io/integrations/zha/)
- [Home Assistant: místní ovládání Matter](https://www.home-assistant.io/integrations/matter/)
- [Home Assistant: vzdálený přístup](https://www.home-assistant.io/docs/configuration/remote/)
- [Companion: oznámení do telefonu](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
- [Companion: místní doručování a jeho omezení](https://companion.home-assistant.io/docs/notifications/notification-local/)
