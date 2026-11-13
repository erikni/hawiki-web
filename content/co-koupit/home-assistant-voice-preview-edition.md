---
title: "Home Assistant Voice Preview Edition: domácnost ovládaná hlasem"
description: "Co potřebujete před nákupem hlasového zařízení Home Assistant a jak zvolit místní nebo cloudové zpracování řeči."
cas: "5 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - Voice Preview Edition
  - Assist
  - hlasové ovládání
  - hardware
---

Rozsvítit bez telefonu, zjistit teplotu nebo nastavit časovač: to jsou úkoly pro **Assist**, hlasového asistenta Home Assistant. **Home Assistant Voice Preview Edition** mu přidá mikrofony a reproduktor do místnosti. Před nákupem si ale rozmyslete, kde se bude řeč zpracovávat a které povely chcete používat.

## Co kupujete

Jde o malé stolní zařízení se dvěma mikrofony, reproduktorem, tlačítkem, otočným ovladačem a světelným prstencem. Fyzický přepínač ztlumení odpojuje napájení mikrofonů. Rozměry jsou 84 × 84 × 21 mm, hmotnost 96 g. K dispozici je také 3,5mm zvukový výstup.

Zařízení **nenahrazuje server Home Assistant**. Připojuje se k němu přes Wi-Fi 2,4 GHz a slouží jako hlasový bod v domácnosti. Napájí se přes USB-C; počítejte se zdrojem 5 V / 2 A. Kabel ani zdroj nejsou podle návodu součástí balení.

Oficiální hardware navrhuje Nabu Casa, společnost se sídlem v USA. To není údaj o zemi výroby konkrétního kusu. Podle výrobce nákup podporuje rozvoj projektů Open Home Foundation.

## Místně, nebo přes cloud?

U místní cesty zpracování řeči zajišťuje domácí systém. Výhodou je možnost fungovat bez internetu, pokud místně běží celý potřebný řetězec. Plný přepis řeči ale může na slabším počítači reagovat pomalu. Výkon samotného hlasového zařízení nezaručuje rychlost rozpoznávání na serveru.

Home Assistant nabízí i úspornější místní rozpoznávání omezených domácích povelů. Před výběrem ověřte podporu svého jazyka a povelů; omezený režim není totéž co volná konverzace.

**Home Assistant Cloud** přesouvá zpracování řeči do služby. Je vhodnou možností i pro méně výkonný domácí server, ale potřebuje internet a předplatné. Cloudové zpracování neznamená, že hlas zůstává pouze doma. Provozovatel uvádí využití hlasových služeb Microsoft Azure; podrobnosti najdete v jeho informacích o soukromí.

## Co čekat od češtiny

Zvlášť ověřte tři části: přepis řeči do textu, porozumění povelu a hlasovou odpověď. Podpora jazyka v jedné části automaticky nepotvrzuje ostatní. Nabu Casa uvádí češtinu mezi jazyky hlasového výstupu, ale před nákupem si ověřte také zvolený způsob rozpoznávání řeči.

Začněte zkouškou Assist v mobilní aplikaci Home Assistant s plánovaným jazykem a nastavením. Použijte skutečné názvy místností a zařízení. Pokud nefunguje požadovaný povel už zde, samotný nákup mikrofonů ho nevyřeší. Označení **Preview Edition** vyjadřuje, že hlasové řešení se dál vyvíjí; nečekejte bez nastavení porozumění každé větě.

## Co připravit před zapojením

Potřebujete aktualizovaný Home Assistant, přístup správce, Wi-Fi 2,4 GHz a napájení. Pro snadné první připojení použijte aktuální mobilní aplikaci Home Assistant a Bluetooth telefonu. Průvodce vás provede připojením k Wi-Fi, přidáním zařízení a volbou zpracování hlasu.

Zařízení, která chcete hlasem ovládat, musí být zpřístupněná pro Assist. Pro první pokus vyberte jedno světlo a jednoduchý povel. Upravte jeho název nebo alias tak, aby se vám dobře vyslovoval. Tento nákupní přehled nevyžaduje YAML; nastavení proveďte podle průvodce a návodu výrobce.

**Voice Preview Edition dává smysl, když chcete Assist používat bez telefonu a jste ochotni jeho nastavení přizpůsobit domácnosti.** Pokud čekáte samostatného asistenta bez serveru, není to vhodný nákup. Aktuální cenu a prodejce ověřte na oficiální stránce produktu. V Česku můžete nabídku zkontrolovat také u [Alzy – Home Assistant Voice Preview Edition](https://www.alza.cz/home-assistant-voice-preview-edition-d12741248.htm).

## Zdroje

- [Home Assistant: Voice Preview Edition a specifikace](https://www.home-assistant.io/voice-pe/)
- [Nabu Casa: první zapojení a požadavky](https://support.nabucasa.com/hc/en-us/articles/25918770371229-Getting-started-with-Home-Assistant-Voice-Preview-Edition)
- [Home Assistant: Assist a hlasové ovládání](https://www.home-assistant.io/voice_control/)
- [Nabu Casa: hlasový výstup a jazyky](https://support.nabucasa.com/hc/en-us/articles/25619386304541)
- [Nabu Casa: soukromí hlasových služeb a informace o poskytovateli](https://www.nabucasa.com/privacy/)
