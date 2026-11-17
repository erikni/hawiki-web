---
title: "BTHome v Home Assistantu: senzory, šifrování a Shelly BLU"
seoTitle: "BTHome a Home Assistant: BLE senzory a šifrování"
description: "Praktický český návod na BTHome v Home Assistantu: BLE reklamy, bindkey, Shelly BLU senzory, Bluetooth proxy a automatizace."
cas: "16 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-11-13"
stav: "Podle dokumentace"
sourceType: "official-docs"
obrazek: "/assets/images/bthome-home-assistant.png"
obrazek_alt: "BTHome senzory vysílající šifrované Bluetooth zprávy přes místní proxy do chytré domácnosti"
temata:
  - BTHome
  - Bluetooth Low Energy
  - Shelly BLU
  - Šifrování
  - Automatizace
related:
  - integrace/bluetooth-home-assistant
  - zaciname/zarizeni-entita-integrace
  - pomoc/zarizeni-nereaguje
  - pomoc/automatizace-nefunguje
---

Integrace **BTHome** převádí úsporné Bluetooth Low Energy zprávy na zařízení a entity v Home Assistantu. Senzor může v krátké reklamě vyslat teplotu, vlhkost, stav dveří, pohyb, baterii nebo stisk tlačítka. Nemusí kvůli tomu navazovat trvalé spojení, takže bateriová zařízení mohou pracovat velmi dlouho.

BTHome je otevřený formát, nikoli značka jednoho výrobce. Používají jej vlastní DIY senzory i komerční zařízení, například část rodiny Shelly BLU. Home Assistant jej podporuje přímo; HACS ani MQTT nejsou pro běžný příjem potřeba.

## BTHome není totéž jako Bluetooth

Integrace **Bluetooth** spravuje rádia a skenery: místní USB adaptér, vestavěné rádio nebo vzdálenou proxy. Zachytí reklamu a předá ji správné integraci. **BTHome** potom rozpozná formát zprávy, případně ji dešifruje a vytvoří odpovídající entity.

Bez funkční Bluetooth vrstvy BTHome nic neuslyší. Naopak samotná Bluetooth integrace neví, že konkrétní bajty znamenají 22,5 °C nebo otevřené okno. Obě části se doplňují:

1. adaptér nebo proxy přijme BLE reklamu,
2. Bluetooth ji předá BTHome,
3. BTHome dekóduje měření či událost,
4. Home Assistant aktualizuje entity a automatizace.

Jde o místní push komunikaci bez pravidelného dotazování senzoru. „Push“ však neznamená zaručené doručení: BLE reklama se může ztratit kvůli vzdálenosti, stínění nebo rušení.

## Jak vypadá BTHome reklama

BTHome v2 používá Bluetooth service UUID `0xFCD2`. Za ním následuje informační bajt zařízení a jednotlivé objekty seřazené podle ID. Každý objekt říká, jakou veličinu nese, jak je dlouhá a jakým koeficientem se má hodnota přepočítat.

Zařízení tak může v jedné reklamě poslat například teplotu, vlhkost a baterii. Formát podporuje také spouštěné události, například krátký, dvojitý nebo dlouhý stisk tlačítka. Příznak trigger-based zařízení pomáhá přijímači pochopit, že tlačítko vysílá nepravidelně a nemá být považované za nedostupné jen proto, že dlouho nikdo nestiskl tlačítko.

BTHome v1 je starší a od listopadu 2022 zastaralá varianta. Home Assistant umí v1 i v2, ale u nového zařízení preferujte v2. Při změně firmwaru DIY senzoru ověřte formát i šifrování; v1 a v2 nepoužívají shodný postup.

## Co budete potřebovat

- Home Assistant s funkční integrací Bluetooth,
- místní adaptér nebo proxy v dosahu senzoru,
- zařízení vysílající podporovaný BTHome v1 či v2 formát,
- u šifrovaného zařízení jeho 32znakový hexadecimální bindkey,
- stabilní baterii a vhodné umístění senzoru.

BTHome zařízení, které pouze vysílá reklamy, nepotřebuje proxy s aktivními GATT spojeními. Stačí skener schopný reklamy přijmout. To je rozdíl proti zámku či termostatu, který může vyžadovat obousměrné spojení.

## Přidání zařízení

1. Nejdřív ověřte adaptér nebo proxy v **Nastavení → Připojení → Bluetooth → Adaptéry**.
2. Zapněte senzor, případně jej přepněte do párovacího či reklamního režimu podle výrobce.
3. Otevřete **Nastavení → Zařízení a služby** a zkontrolujte část **Objeveno**.
4. Vyberte nalezené zařízení BTHome a dokončete průvodce.
5. U šifrovaného senzoru vložte bindkey, když si jej Home Assistant vyžádá.
6. Otevřete zařízení a ověřte entity, jednotky, čas poslední aktualizace a stav baterie.

Pokud se BTHome automaticky neobjeví, lze integraci přidat přes **Přidat integraci → BTHome**. Konkrétní zařízení se však objeví až po přijetí platné reklamy. YAML konfigurace integrace není pro běžné přidání potřeba.

Názvy entit se odvozují od zařízení a mohou se lišit. Příklady jako `sensor.sklep_teplota` nebo `binary_sensor.okno_otevreno` nejsou univerzální ID.

## Šifrování a bindkey

BTHome v2 umí šifrovat obsah reklam pomocí AES-CCM se sdíleným klíčem. Bindkey má 16 bajtů, zapisuje se jako **32 hexadecimálních znaků**. Bez správného klíče Home Assistant obsah šifrované reklamy nepřečte.

Klíč přeneste pouze přes důvěryhodné prostředí a uložte jej do správce hesel. Nevkládejte jej do veřejného issue, screenshotu ani repozitáře. Při výměně nebo resetu zařízení ověřte, zda se klíč nezměnil.

Šifrování chrání obsah před běžným pasivním čtením, ale není samo o sobě zárukou bezpečné automatizace. Dokumentace BTHome upozorňuje, že přijímač musí správně kontrolovat čítač zpráv a odmítnout opakované pakety. Většina přijímačů včetně Home Assistantu navíc zpracovává šifrované i nešifrované zprávy a útočník může napodobit MAC adresu. BTHome proto nepoužívejte jako jediný podklad pro odemknutí dveří, vypnutí alarmu nebo jinou bezpečnostně kritickou akci.

## Shelly BLU v Home Assistantu

Zařízení Shelly BLU používají BLE a vybrané modely vysílají BTHome v2. Typické příklady zahrnují teplotu a vlhkost, dveřní kontakt, pohyb nebo tlačítko. Přesný seznam entit závisí na modelu a firmwaru.

Pro Home Assistant není nutná Shelly cloudová aplikace ani MQTT, pokud senzor zachytí místní Bluetooth adaptér nebo podporovaná proxy. Zařízení Shelly Gen2+ může Home Assistantu předávat Bluetooth reklamy jako vzdálený adaptér; podle dokumentace Bluetooth však tato cesta nepodporuje aktivní spojení. Pro reklamní BTHome senzory to obvykle nevadí.

Shelly BLU Gateway nebo jiný Shelly přístroj může současně fungovat jako brána ekosystému Shelly. To není automaticky totéž jako Bluetooth proxy Home Assistantu. Vendorová brána může předávat data do Shelly aplikace, lokálního BTHome komponentu nebo přes MQTT podle konfigurace. Pokud chcete přímé objevení BTHome v Home Assistantu, ověřte, že jej Home Assistant vidí jako podporovaný vzdálený skener, nebo použijte ESPHome proxy.

U šifrovaného Shelly BLU zařízení potřebujete jeho klíč. Dokumentace Shelly uvádí možnost získat klíč pomocí nástroje Shelly BLU Debug; konkrétní postup se může měnit podle modelu a firmwaru. Klíč nevymýšlejte ani nezaměňujte s heslem účtu Shelly.

## Příklad 1: dlouho otevřené okno

Příklad vyžaduje BTHome dveřní nebo okenní senzor, který už vytvořil binární entitu. Nahraďte `binary_sensor.okno_loznice` skutečným ID. Celý blok vložte do YAML editoru nové automatizace.

```yaml
alias: BTHome – okno otevřené deset minut
triggers:
  - trigger: state
    entity_id: binary_sensor.okno_loznice
    from: "off"
    to: "on"
    for: "00:10:00"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: "Otevřené okno"
      message: "Okno v ložnici je otevřené déle než deset minut."
mode: single
```

Spouštěč čeká deset minut v otevřeném stavu. Po restartu Home Assistantu nebo načtení automatizací se čekání `for` vynuluje. Pro ovládání topení doplňte samostatné bezpečné podmínky a návratovou akci při zavření.

## Příklad 2: vlhkost a riziko plísně

Příklad předpokládá BTHome senzor vlhkosti a nahrazení `sensor.koupelna_vlhkost` skutečnou entitou. Celý blok vložte do YAML editoru nové automatizace.

```yaml
alias: BTHome – vysoká vlhkost v koupelně
triggers:
  - trigger: numeric_state
    entity_id: sensor.koupelna_vlhkost
    above: 75
    for: "00:05:00"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: "Vysoká vlhkost"
      message: >-
        V koupelně je
        {{ states('sensor.koupelna_vlhkost') }} % vlhkosti.
mode: single
```

Pětiminutová prodleva omezuje reakce na krátkou špičku. Pokud senzor vysílá hodnotu jen v určitém intervalu, automatizace reaguje až po přijetí další reklamy.

## Tlačítka a události

BTHome v2 umí události `press`, `double_press`, `long_press` a další typy. Home Assistant je u podporovaného zařízení může zpřístupnit jako událostní entitu nebo zařízení trigger. Nejbezpečnější je vytvořit automatizaci v UI: vyberte zařízení, nabízený typ stisku a cílovou akci. Názvy triggerů závisí na konkrétním modelu, proto je nevkládejte podle cizího YAML bez ověření.

Tlačítko může zprávu vyslat několikrát kvůli spolehlivosti. BTHome používá volitelný packet ID k rozpoznání opakování, ale správné filtrování závisí na vysílači i přijímači. U kritické akce přidejte ochranu proti opakovanému spuštění.

## Když zařízení nefunguje

- **BTHome se neobjeví:** nejdřív ověřte Bluetooth adaptér či proxy a dosah senzoru. Integrace se objeví až po platné reklamě.
- **Home Assistant žádá klíč:** zařízení vysílá šifrovaně. Vložte přesný 32znakový bindkey, ne MAC adresu ani heslo.
- **Po zadání klíče nejsou hodnoty:** klíč může být chybný, zařízení změnilo MAC adresu nebo nevysílá očekávanou verzi BTHome.
- **Hodnoty se zpožďují:** bateriové senzory šetří energii a nevysílají nepřetržitě. Přesuňte skener a ověřte baterii.
- **Tlačítko funguje jen někdy:** přibližte proxy, odstraňte kovové stínění a zkontrolujte, že událostní entita nabízí daný typ stisku.
- **Zařízení je v aplikaci Shelly, ale ne v Home Assistantu:** Shelly gateway nemusí být nakonfigurovaná jako podporovaný vzdálený skener pro Home Assistant. Ověřte cestu dat.
- **Vznikají duplicitní reakce:** zkontrolujte packet ID, firmware senzoru a režim automatizace; nepouštějte stejnou akci současně z aplikace výrobce i Home Assistantu.

## Výhody, omezení a soukromí

Výhodou BTHome je jednoduchý otevřený formát, nízká spotřeba a místní provoz. Jedna reklama může nést více měření a přijmout ji může kterýkoli vhodně umístěný skener. Díky proxy lze pokrytí rozšířit bez vendorového cloudu.

Nevýhodou je nezaručené doručení reklam, kratší dosah BLE a závislost na kvalitě firmwaru senzoru. Nešifrované hodnoty může přečíst kdokoli v dosahu. Ani šifrování podle současných omezení nepoužívejte jako jediný bezpečnostní prvek.

Pro teplotu, vlhkost, otevření, pohyb a běžná tlačítka je BTHome praktická místní volba. Pro povely, které vyžadují potvrzené doručení nebo vysokou bezpečnost, zvolte protokol a zařízení navržené pro daný účel.

## Zdroje

- [Home Assistant: integrace BTHome](https://www.home-assistant.io/integrations/bthome/)
- [BTHome: otevřený standard](https://bthome.io/)
- [BTHome v2: formát reklam](https://bthome.io/format/)
- [BTHome: šifrování a jeho omezení](https://bthome.io/encryption/)
- [Shelly: BTHome komponenty a šifrovací klíč](https://www.shelly.com/blogs/documentation/shelly-blu-assistant-web-interface-guide)
- [Home Assistant: integrace Bluetooth](https://www.home-assistant.io/integrations/bluetooth/)
