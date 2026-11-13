---
title: "Home Assistant Connect AUX-2: staré audio v chytré domácnosti"
seoTitle: "Connect AUX-2: audio, RS-232 a PoE pro Home Assistant"
description: "Co umí Home Assistant Connect AUX-2, jak připojí starší audio a sériová zařízení a co zkontrolovat před koupí."
obrazek: "/assets/images/home-assistant-connect-aux-2.png"
obrazek_alt: "Ilustrace AUX-2 připojeného k domácímu routeru kabelem RJ45 a k aktivním reproduktorům přes 3,5mm výstup."
cas: "6 minut čtení"
obtiznost: "Další krok"
kontrola_zdroju: "2026-11-13"
stav: "Podle dokumentace"
temata:
  - "Connect AUX-2"
  - "Music Assistant"
  - "RS-232"
  - "PoE"
  - "hardware"
---

**Home Assistant Connect AUX-2** je malá krabička od Nabu Casa pro propojení starší techniky s Home Assistantem. Umí přehrávat hudbu do receiveru nebo aktivních reproduktorů, ovládat podporovaná zařízení přes sériovou linku a fungovat jako síťové místo pro vybrané USB adaptéry. Není to nový Home Assistant ani zesilovač: potřebuje běžící Home Assistant 2026.9 nebo novější.

## Hudba pro starší receiver nebo aktivní repro

AUX-2 se v Home Assistantu přidá přes integraci ESPHome. Hudbu přijímá po domácí síti pomocí otevřeného protokolu Sendspin; praktickým zdrojem je bezplatný **Music Assistant**. Ten může přehrávat místní soubory i podporované streamovací služby a seskupit AUX-2 s dalšími kompatibilními přehrávači.

Kombinovaný 3,5mm výstup nabízí analogový zvuk nebo optický S/PDIF, vždy jen jeden způsob současně. Podporuje stereo až 24 bitů / 48 kHz a formáty FLAC, MP3 a WAV. Zařízení má pouze **audio výstup**: zvuk z gramofonu či CD do Home Assistantu nenahrává, Bluetooth audio nepřenáší a pasivní reproduktory nenapájí. Ty potřebují vlastní zesilovač.

## Dva porty RS-232 a další možnosti

Dva 3,5mm porty RS-232 mohou ovládat například kompatibilní televizi, AV receiver, projektor, UPS nebo regulaci. Samotný konektor ale podporu nezaručuje: v Home Assistantu musí existovat integrace, která umí sériový proxy AUX-2. Pro různé přístroje budete potřebovat správný kabel, například 3,5mm–DB9. Přepínače na spodní straně dovolují prohodit vodiče TX a RX.

Sériové zdířky nesmějí být zaměněny za audio výstup. Nesou signál ±5 V a mohou audio zařízení poškodit. RS-485 vyžaduje zvláštní podporovaný USB adaptér. USB-A lze současně použít jen pro jeden účel: adaptér RS-485, Connect ZWA-2, nebo experimentálně Connect ZBT-2. Zigbee přes ZBT-2 funguje pouze se ZHA a Home Assistantem 2026.11+, zatím není široce otestované. Thread podporovaný není.

AUX-2 zároveň funguje jako Bluetooth proxy pro zařízení BLE; nejde však o Bluetooth reproduktor. Grove port dovoluje pokročilým uživatelům přidat podporované vstupy či výstupy přes ESPHome.

## Síť, napájení a obsah balení

Nejčistší zapojení nabízí Ethernet s **PoE 802.3af**, který přenese data i napájení jedním kabelem. Alternativou je Ethernet nebo 2,4GHz Wi-Fi a zdroj USB-C 5 V / 2 A. Kabelové připojení výrobce doporučuje jako spolehlivější. Zařízení měří 106 × 63 × 25 mm a váží 104 g.

V krabičce je AUX-2, stručný návod a bezpečnostní informace. Napájecí zdroj, Ethernet, audio ani sériové kabely je nutné zvolit podle sestavy a koupit zvlášť. Před objednáním proto zkontrolujte vstup zesilovače, sériový konektor a kompatibilní integraci.

## Vyplatí se koupit?

AUX-2 dává smysl, pokud chcete zachovat kvalitní starší receiver či aktivní reproduktory, lokálně ovládat zařízení s podporovaným RS-232 nebo přesunout Z-Wave adaptér na vhodnější místo v síti. Pro samotné přehrávání do moderního síťového reproduktoru nebo pro zařízení bez sériové integrace může být zbytečně univerzální.

V Česku jej 13. listopadu 2026 nabízela Alza.cz v předobjednávce. Dostupnost a cena se mohou měnit, proto před nákupem zkontrolujte aktuální produktovou stránku. Pro Zigbee porovnejte také samostatný [Connect ZBT-2](/co-koupit/home-assistant-connect-zbt-2/) a pro Z-Wave [Connect ZWA-2](/co-koupit/home-assistant-connect-zwa-2/).

## Zdroje

- [Home Assistant: Connect AUX-2](https://www.home-assistant.io/connect/aux-2/)
- [Nabu Casa: co je Connect AUX-2 a jak funguje](https://support.nabucasa.com/hc/en-us/articles/40528879660317-What-Connect-AUX-2-is-and-how-it-works)
- [Nabu Casa: nastavení Connect AUX-2](https://support.nabucasa.com/hc/en-us/articles/40527754954653-Set-up-Home-Assistant-Connect-AUX-2)
- [ESPHome Devices: Home Assistant Connect AUX-2](https://devices.esphome.io/devices/home-assistant-connect-aux-2/)
- [Root.cz: Connect AUX-2](https://www.root.cz/clanky/home-assistant-connect-aux-2-novy-hardware-pro-streamovani-hudby-a-seriove-ovladani/)
- [Alza.cz: Home Assistant Connect AUX-2](https://www.alza.cz/home-assistant-connect-aux-2-d13674192.htm)
