---
title: "Bluetooth v Home Assistantu: adaptéry, proxy a lepší dosah"
seoTitle: "Bluetooth a Home Assistant: adaptéry, proxy a diagnostika"
description: "Praktický český návod na Bluetooth v Home Assistantu: výběr adaptéru, vzdálené ESPHome proxy, dosah, aktivní spojení a řešení výpadků."
cas: "17 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-11-13"
stav: "Podle dokumentace"
sourceType: "official-docs"
obrazek: "/assets/images/bluetooth-home-assistant.png"
obrazek_alt: "Dům pokrytý místním Bluetooth adaptérem a dvěma vzdálenými proxy pro senzory a zámek"
temata:
  - Bluetooth
  - Bluetooth proxy
  - ESPHome
  - Dosah
  - Diagnostika
related:
  - zaciname/zarizeni-entita-integrace
  - pomoc/zarizeni-nereaguje
  - pomoc/automatizace-nefunguje
  - pomoc/vypadek-internetu
---

Integrace **Bluetooth** dává Home Assistantu společnou vrstvu pro místní adaptéry i vzdálené proxy. Vyhledává zařízení v okolí a předává jejich data konkrétním integracím, například BTHome, SwitchBot Bluetooth, Xiaomi BLE nebo Yale Access Bluetooth.

Samotný Bluetooth proto obvykle nevytvoří teplotní senzor ani zámek. Zajistí příjem BLE reklam nebo aktivní spojení a Home Assistant nabídne integraci rozpoznaného zařízení. Jde o místní komunikaci.

## Co znamenají adaptér, proxy a reklama

**Bluetooth adaptér** je rádio přímo připojené k systému s Home Assistantem: vestavěný čip, USB dongle nebo karta. Na Linuxu s ním Home Assistant komunikuje přes BlueZ a D-Bus.

**Bluetooth proxy** je samostatné síťové zařízení, které umístíte blíž k senzorům. Přijímá Bluetooth Low Energy (BLE) a předává data Home Assistantu přes Wi-Fi nebo Ethernet. Home Assistant všechny místní adaptéry a podporované proxy sdružuje a vhodná integrace může použít cestu s lepším signálem.

**Reklama** je krátká zpráva, kterou BLE zařízení vysílá bez navázání spojení. Mnoho teplotních čidel předává hodnoty právě takto. Jiné zařízení, například zámek nebo termostat, potřebuje **aktivní spojení** pro čtení či příkaz. Ne každá proxy aktivní spojení podporuje.

Bluetooth integrace není totéž jako „gateway“ výrobce, která může posílat data do vlastní aplikace či cloudu. Proxy je obecný skener a sama entity nevytváří.

## Co budete potřebovat

- Home Assistant OS 9.0 nebo novější, případně správně připravený Linux/Container,
- podporovaný místní Bluetooth adaptér nebo vzdálenou proxy,
- zařízení s vlastní podporovanou integrací v Home Assistantu,
- vhodné umístění bez silného stínění kovem a USB 3 rušení,
- u proxy spolehlivou síť mezi proxy a Home Assistantem.

Na Linuxu dokumentace vyžaduje přístupný D-Bus, BlueZ alespoň 5.43 (doporučeno 5.63 nebo novější), dbus-broker a jádro 5.15.62 nebo novější. Home Assistant OS tyto požadavky řeší automaticky. U Containeru je musí zajistit hostitel.

## Místní USB adaptér

Pokud server nemá Bluetooth, použijte podporovaný USB adaptér. Home Assistant udržuje seznam známých funkčních modelů; název čipu je důležitější než podobný vzhled donglu. Některé novější adaptéry potřebují firmware, který v Home Assistant OS nelze snadno doplnit.

Adaptér nepřipojujte těsně vedle USB 3 disku, SSD, Wi-Fi antény ani kovové skříně. Krátký kvalitní USB 2 prodlužovací kabel často zlepší příjem výrazněji než výměna softwaru. Po prvním připojení může být potřeba několik restartů, než systém adaptér správně rozpozná.

V Home Assistantu otevřete **Nastavení → Připojení → Bluetooth → Adaptéry**. Zde uvidíte místní i vzdálené skenery a po otevření zařízení podrobnosti. Pokud se nabídne ozubené kolo, lze změnit režim skenování:

- **Auto** je doporučená volba; většinu času poslouchá pasivně a aktivní sken použije podle potřeby,
- **Active** získává doplňující data nejrychleji, ale zvyšuje spotřebu okolních bateriových zařízení,
- **Passive** pouze poslouchá a některým integracím nemusí stačit.

Auto a Passive vyžadují podporu pasivního skenování. Když ji adaptér nemá, Auto přejde na Active.

## Home Assistant Container

U Containeru nestačí předat pouze USB zařízení. Hostitel musí provozovat BlueZ a kontejner musí vidět D-Bus. Dokumentace vyžaduje také schopnosti `NET_ADMIN` a `NET_RAW`; bez nich Bluetooth funguje omezeně a adaptér nelze spolehlivě obnovit.

Následující část patří do `compose.yaml` služby Home Assistantu, nikoli do `configuration.yaml`. Zachovejte ostatní nastavení své služby a kontejner potom znovu vytvořte.

```yaml
services:
  homeassistant:
    cap_add:
      - NET_ADMIN
      - NET_RAW
    volumes:
      - /run/dbus:/run/dbus:ro
```

Používá-li hostitel D-Bus v `/var/run/dbus`, namapujte jej do `/run/dbus` v kontejneru. Varování „Bluetooth adapter requires additional permissions“ v opravách znamená, že některá z těchto oprávnění chybí.

## Vzdálená Bluetooth proxy

Proxy je vhodná, když je Home Assistant ve sklepě, racku nebo na opačném konci domu. Nejčastější variantou je ESPHome zařízení s Bluetooth proxy, ale Home Assistant přijímá reklamy také z podporovaných Shelly Gen2+ a SMLIGHT SLZB-U. Tyto dvě varianty podle dokumentace pouze poslouchají reklamy a neumějí aktivní Bluetooth spojení.

ESPHome proxy může reklamy přijímat i navazovat aktivní GATT spojení. Připravený projekt ESPHome je pro běžného uživatele bezpečnější než kopírování náhodné konfigurace. Proxy se po přidání do ESPHome objeví mezi Bluetooth adaptéry Home Assistantu.

Při vlastním ESPHome projektu závisí `bluetooth_proxy` na BLE trackeru dané platformy. Následuje pouze příslušná část; celý firmware musí obsahovat také desku, síť, API, aktualizace a bezpečnostní údaje.

```yaml
bluetooth_proxy:
  active: true
```

Na ESP32 jsou aktivní spojení standardně zapnutá a výchozí jsou tři sloty. ESPHome doporučuje nepřekračovat pět. Reklamy sloty nespotřebovávají, trvale připojený zámek ano.

Proxy umístěte do stejné místnosti nebo poblíž problematických zařízení, ne těsně vedle Wi-Fi AP. Více proxy rozmístěte s odstupem, aby zbytečně nepokrývaly totožné místo. Ethernet omezuje souběh Wi-Fi a Bluetooth na jednom rádiu, ale není podmínkou.

## Jak zařízení přidat

1. Přidejte a ověřte místní adaptér nebo proxy.
2. Otevřete **Nastavení → Zařízení a služby** a zkontrolujte část **Objeveno**.
3. Vyberte integraci konkrétního zařízení, nikoli Bluetooth znovu.
4. Dokončete její průvodce. Šifrované zařízení může vyžadovat klíč nebo údaje z aplikace výrobce.
5. Na stránce zařízení ověřte, že se hodnoty mění a entity nejsou nedostupné.

Integraci Bluetooth lze přidat ručně přes **Přidat integraci → Bluetooth**, pokud se nevytvořila automaticky. Další adaptéry však Home Assistant spravuje společně; pro každý dongle se nepřidává samostatná Bluetooth integrace.

## Příklad 1: upozornění na vysokou teplotu

Příklad předpokládá BLE teplotní senzor, který už jeho vlastní integrace zpřístupnila jako entitu. Nahraďte `sensor.ble_sklep_teplota` skutečným ID. Celý blok vložte do YAML editoru nové automatizace.

```yaml
alias: Bluetooth – vysoká teplota ve sklepě
triggers:
  - trigger: numeric_state
    entity_id: sensor.ble_sklep_teplota
    above: 28
    for: "00:05:00"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: "Teplota ve sklepě"
      message: >-
        Bluetooth senzor hlásí
        {{ states('sensor.ble_sklep_teplota') }} °C.
mode: single
```

Spouštěč čeká pět minut nad 28 °C, aby nereagoval na jediný chybný paket. Oznámení vznikne uvnitř Home Assistantu. Přesnost a rychlost aktualizací určuje konkrétní senzor a jeho integrace, ne samotná Bluetooth vrstva.

## Příklad 2: slabá baterie BLE senzoru

Nahraďte bateriovou entitu skutečným ID. Ne každý Bluetooth přístroj úroveň baterie vysílá. Blok vložte do YAML editoru samostatné automatizace.

```yaml
alias: Bluetooth – slabá baterie senzoru
triggers:
  - trigger: numeric_state
    entity_id: sensor.ble_sklep_baterie
    below: 15
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: "Vyměňte baterii"
      message: >-
        BLE senzor ve sklepě má
        {{ states('sensor.ble_sklep_baterie') }} % baterie.
mode: single
```

Automatizace se spustí při přechodu pod 15 %. Pokud zařízení odešle stav baterie jen několikrát denně, upozornění přijde až s další reklamou.

## Jak diagnostikovat dosah

Nejdřív rozlište, zda zařízení pouze vysílá reklamy, nebo potřebuje spojení. Proxy bez aktivních spojení může skvěle vidět teploměr, ale nepomůže zámku, který vyžaduje příkazy.

Na stránce Bluetooth otevřete jednotlivé skenery a sledujte, zda je problematické zařízení v jejich dosahu. Začněte jednou změnou: přesuňte proxy nebo USB adaptér, použijte prodlužovací kabel a několik minut sledujte aktualizace. Nepřidávejte hned několik proxy, jinak nezjistíte příčinu.

Bluetooth pracuje ve stejném pásmu 2,4 GHz jako Wi-Fi. Kov, železobeton, rozvaděč, USB 3 zařízení a nevhodně umístěné Wi-Fi rádio mohou příjem zhoršit. Vyšší počet čárek v aplikaci výrobce není důkaz, že Home Assistant přijímá stejné reklamy přes stejnou cestu.

## Když Bluetooth nefunguje

- **Adaptér není vidět:** restartujte hostitele, zkontrolujte USB a stránku adaptérů. U Linuxu ověřte BlueZ, D-Bus a podporované jádro.
- **Container hlásí omezená oprávnění:** přidejte D-Bus, `NET_ADMIN` a `NET_RAW` a kontejner znovu vytvořte.
- **Zařízení je objevené, ale nelze dokončit nastavení:** může vyžadovat aktivní spojení, které použitá proxy neumí, nebo jsou všechny sloty obsazené.
- **Hodnoty chodí nepravidelně:** přesuňte skener, oddalte USB adaptér od rušení a ověřte režim skenování.
- **Zařízení se neobjeví:** ověřte podporovanou integraci, zapněte zařízení a případně použijte jeho párovací režim. Ne každé Bluetooth zařízení Home Assistant podporuje.
- **Po přidání další proxy se nic nezlepšilo:** zkontrolujte její síťové spojení a zda skutečně pokrývá jiné místo.
- **Aktivní zařízení se odpojuje:** ověřte počet volných slotů a sílu signálu; přechodná selhání spojení jsou u BLE běžná.

## Soukromí, bezpečnost a omezení

Bluetooth reklamy může přijmout každý kompatibilní skener v dosahu. U citlivých údajů preferujte zařízení s podporovaným šifrováním a klíče ukládejte pouze do Home Assistantu. Proxy připojujte do důvěryhodné sítě a aktualizujte její firmware.

Bluetooth není vhodná náhrada zabezpečeného alarmového protokolu. Dostupnost závisí na rádiu, baterii, rušení a síti proxy. Automatizace pro zámky nebo ochranu majetku musí počítat s nedostupností a bezpečným výchozím stavem.

Výhodou společné vrstvy je kombinace více adaptérů, automatický výběr vhodné cesty a lokální provoz. Nevýhodou je kratší dosah, omezené aktivní sloty a rozdílná kvalita adaptérů. Pro celý dům bývá praktičtější několik promyšleně umístěných proxy než jeden silný dongle v technické místnosti.

## Zdroje

- [Home Assistant: integrace Bluetooth](https://www.home-assistant.io/integrations/bluetooth/)
- [Home Assistant: Bluetooth Adapters](https://www.home-assistant.io/integrations/bluetooth_adapters/)
- [ESPHome: Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy/)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
