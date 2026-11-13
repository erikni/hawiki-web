---
title: "Kamery v Home Assistant: lokálně s Frigate"
description: "Obraz, záznam a rozpoznání osob bez závislosti na cloudu výrobce. Jak pomáhají RTSP a ONVIF."
obrazek: "/assets/images/kamery-frigate.png"
obrazek_alt: "Ilustrace IP kamery propojené s domácím serverem a přehledem detekované osoby."
cas: "6 minut čtení"
obtiznost: "Další krok"
kontrola_zdroju: "2026-10-06"
stav: "Podle dokumentace"
temata:
  - "Kamery"
  - "Frigate"
  - "RTSP"
  - "ONVIF"
  - "Lokální provoz"
---

## Kamera, Frigate a Home Assistant
**Frigate** je otevřený síťový videorekordér: ukládá záznam a doma rozpoznává osoby či auta. HA získá obraz a senzory pro automatizace. S lokálním streamem nepotřebujete cloud výrobce; vzdálený přístup může vyžadovat internet.

**RTSP** přenáší živé video. **ONVIF** pomáhá s vyhledáním a podporovaným ovládáním kamery, včetně otáčení a zoomu (PTZ). Můžete kombinovat značky, ale ne každá kamera umí vše. Pro běžný RTSP záznam ve Frigate ONVIF není nutný; automatické PTZ sledování vyžaduje konkrétní podporované funkce.

## Co Frigate umí
- **Pohybová detekce** hledá změny obrazu a vybírá oblasti pro rozpoznávání. Pohyb sám ještě neznamená člověka.
- **Rozpoznání objektů** rozlišuje například osobu a auto podle použitého modelu.
- **Zóny** vymezí vchod nebo příjezdovou cestu. Událost můžete omezit na osobu, která vstoupí do zóny; poloha se posuzuje podle spodního středu rámečku objektu.
- **Masky pohybu** potlačí rušivé oblasti, například časový údaj. Nejsou zárukou, že se v nich objekt nikdy nerozpozná.
- **Záznamy a snímky** umožní zpětně prohlížet události; nastavíte ukládání a dobu uchování. Umí i živý obraz, přehled více kamer a podporované PTZ sledování.

## Příklady kamer a značek
**EU: [Shelly Camera Black](https://www.shelly.com/products/shelly-camera-black)** od skupiny se sídlem v Bulharsku nabízí lokální RTSP stream. ONVIF specifikace nedokládá.

**USA: [Ubiquiti UniFi kamery](https://eu.store.ui.com/eu/en/category/all-physical-security)**. U řady G5 a novějších podle Frigate potřebujete server **UniFi Protect** pro zpřístupnění streamu; nejde tedy vždy o přímé RTSP připojení kamery.

Levnější variantou mohou být **[TP-Link Tapo](https://www.tp-link.com/us/support/faq/4465/)** s podporou RTSP/ONVIF u vybraných modelů. Značka vznikla v Číně; mezinárodní TP-Link uvádí ústředí v USA a Singapuru a oddělení od čínské společnosti. Kompatibilitu vždy ověřte pro konkrétní model a firmware.

## Co potřebujete doma
Frigate běží jako aplikace v HA OS nebo v Dockeru na jiném počítači. Potřebuje disk na záznamy a výkon pro dekódování videa i detekci. Začněte jednou kamerou podle [instalačního návodu](https://docs.frigate.video/frigate/installation/). Nastavte skutečnou RTSP adresu, detekci a ukládání a ověřte obraz.

Pro snadnou kompatibilitu volte **H.264**, u zvuku AAC. Výhodou jsou dva streamy: kvalitnější pro záznam a menší pro detekci kolem **5 snímků za sekundu**.

## Připojení do Home Assistant
1. Zprovozněte MQTT broker, například Mosquitto, a v HA nastavte integraci **MQTT**. Frigate musí mít MQTT zapnuté a používat stejný broker.
2. Přes [HACS](/dalsi-moznosti/hacs/) stáhněte integraci **Frigate** a restartujte HA. Tím se neinstaluje samotný videorekordér.
3. V **Nastavení → Zařízení a služby → Přidat integraci** vyberte Frigate a zadejte adresu jeho instance podle způsobu instalace.

Získáte kamerové entity, senzory objektů a přístup k záznamům.

## Příklad: osoba u vchodu
Předpokladem je funkční integrace a její binární senzor detekce osoby. V nové automatizaci otevřete **Upravit v YAML** a vložte celý příklad. `binary_sensor.vchod_person_occupancy` nahraďte skutečnou entitou. Oznámení se zobrazí uvnitř HA.

```yaml
alias: Frigate – osoba u vchodu
triggers:
  - trigger: state
    entity_id: binary_sensor.vchod_person_occupancy
    from: "off"
    to: "on"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: Kamera u vchodu
      message: Frigate rozpoznal osobu u vchodu.
mode: single
```

## Zdroje
- [Frigate: projekt a funkce](https://github.com/blakeblackshear/frigate)
- [Frigate: integrace s Home Assistant](https://docs.frigate.video/integrations/home-assistant/)
- [Frigate: instalace](https://docs.frigate.video/frigate/installation/)
- [Frigate: nastavení kamer a streamů](https://docs.frigate.video/frigate/camera_setup/)
- [Frigate: ONVIF a automatické sledování](https://docs.frigate.video/configuration/autotracking/)
- [Home Assistant: ONVIF](https://www.home-assistant.io/integrations/onvif/)
- [Home Assistant: MQTT](https://www.home-assistant.io/integrations/mqtt/)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: trvalá oznámení](https://www.home-assistant.io/integrations/persistent_notification/)
- [Shelly Camera Black: specifikace](https://www.shelly.com/products/shelly-camera-black)
- [Shelly: sídlo skupiny](https://corporate.shelly.com/en/page/impressum)
- [Ubiquiti: nabídka kamer](https://eu.store.ui.com/eu/en/category/all-physical-security)
- [Ubiquiti: kontakty](https://www.ui.com/contact/)
- [Frigate: specifika UniFi kamer](https://docs.frigate.video/configuration/camera_specific/)
- [TP-Link Tapo: RTSP a ONVIF](https://www.tp-link.com/us/support/faq/4465/)
- [TP-Link: změna struktury společnosti](https://www.tp-link.com/us/press/news/21130/)
- [Frigate: pohybová detekce](https://docs.frigate.video/configuration/motion_detection/)
- [Frigate: zóny](https://docs.frigate.video/configuration/zones/)
