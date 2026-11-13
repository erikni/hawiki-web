---
title: "Chytré světlo a klasický vypínač: neodpojujte napájení"
description: "Jak zachovat klasický vypínač se Shelly v režimu Detached a ovládat chytré světlo s jiným jasem ve dne a v noci."
cas: "6 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - Chytré osvětlení
  - Shelly
  - Zigbee
  - Detached
  - Automatizace
---

Chytrou žárovku nestačí zašroubovat a dál ji vypínat běžným vypínačem. Jakmile vypínač přeruší napájení, světlo přestane komunikovat. Home Assistant ho nezapne, nezmění jas ani barvu. Platí to pro Wi-Fi, Zigbee i světla ovládaná přes Matter. Světlo vypnuté příkazem zůstává napájené; světlo odpojené vypínačem nikoli.

## Proč záleží i na Zigbee síti

Mnohá Zigbee světla fungují jako router: předávají zprávy dalším zařízením. Odpojením takového světla můžete zhoršit spojení senzorů nebo jiných světel. Ne každá žárovka tuto roli má; ověřte konkrétní model. Zigbee routery mají zůstávat dostupné i tehdy, když nesvítí.

Řešením je trvalé napájení světla a ovladač, který pouze posílá povel. Může to být bezdrátové tlačítko nebo modul za původním vypínačem s odděleným vstupem.

## Shelly zachová původní vypínač

Příkladem je [Shelly 1PM Mini Gen3](https://www.shelly.com/products/shelly-1pm-mini-gen3), Wi-Fi modul od skupiny Shelly se sídlem v Bulharsku, tedy v EU. Sídlo výrobce neříká, kde vznikl konkrétní kus. Existují i jiné značky; vybírejte podle podpory odděleného vstupu a místní integrace, ne pouze podle původu.

Modul potřebuje také nulový vodič N, který ve staré krabici nemusí být. Ověřit je potřeba prostor i vhodnost zapojení. Montáž do rozvodu 230 V svěřte kvalifikovanému elektrikáři podle dokumentace výrobce.

Po montáži připojte Shelly k Wi-Fi a otevřete jeho místní webové rozhraní zadáním IP adresy do prohlížeče. Na úvodní stránce otevřete nastavení vstupu/výstupu:

- **Input mode: Switch** pro běžný kolébkový vypínač.
- **Output type: Detached Switch** oddělí vstup od relé.
- **Action on power on: Turn ON** obnoví napájení po výpadku.

Relé ručně zapněte a vypněte automatické vypínací časovače i plány. Detached samo relé nezapne a nezabrání vypnutí přes aplikaci nebo ochrany modulu. Automatizace mají ovládat žárovku, nikoli relé Shelly.

V Home Assistant přidejte **Shelly** v **Nastavení → Zařízení a služby**. Integrace pracuje místně, účet Shelly Cloud nepotřebujete. Najděte binární senzor vstupu; vzniká při režimu Switch. Při překlopení ověřte změnu mezi `on` a `off`.

## Jas podle času

Příklad při každém překlopení vypínače zhasne rozsvícené světlo, nebo rozsvítí zhasnuté. Od 22:00 do 4:59 nastaví 50 %, od 5:00 do 21:59 nastaví 100 %. Jas volí při zapnutí; ve 22:00 už rozsvícené světlo automaticky neztlumí. Poloha kolébky proto neurčuje zapnuto/vypnuto: rozhoduje změna polohy.

Vytvořte prázdnou automatizaci v **Nastavení → Automatizace a scény**, otevřete **Upravit v YAML** a vložte celý příklad. Nahraďte `binary_sensor.shelly_vstup` a `light.pokoj` svými ID. Světlo musí být přidané do Home Assistant a podporovat stmívání.

```yaml
alias: Vypínač a chytré světlo podle času
triggers:
  - trigger: state
    entity_id: binary_sensor.shelly_vstup
    from: "off"
    to: "on"
  - trigger: state
    entity_id: binary_sensor.shelly_vstup
    from: "on"
    to: "off"
conditions: []
actions:
  - choose:
      - conditions: "{{ is_state('light.pokoj', 'on') }}"
        sequence:
          - action: light.turn_off
            target:
              entity_id: light.pokoj
    default:
      - action: light.turn_on
        target:
          entity_id: light.pokoj
        data:
          brightness_pct: "{{ 50 if now().hour >= 22 or now().hour < 5 else 100 }}"
mode: single
```

Stejně můžete nastavit 20 % pro noční chodbu nebo jiné hodnoty pro ložnici. Při výpadku Home Assistant či Wi-Fi tato automatizace nezpracuje vypínač; trvalé napájení samo nezajistí náhradní ovládání.

## Zdroje

- [Home Assistant: Shelly a binární vstupy](https://www.home-assistant.io/integrations/shelly/)
- [Home Assistant: Zigbee a trvale napájené routery](https://www.home-assistant.io/integrations/zha/)
- [Shelly: 1PM Mini Gen3](https://www.shelly.com/products/shelly-1pm-mini-gen3)
- [Shelly: technické údaje a zapojení 1PM Mini Gen3](https://kb.shelly.cloud/knowledge-base/shelly-1pm-mini-gen3)
- [Shelly: webové rozhraní a Detached Switch](https://kb.shelly.cloud/knowledge-base/shelly-1pm-mini-gen3-web-interface-guide)
- [Shelly Group: sídlo společnosti](https://corporate.shelly.com/en/page/impressum)
- [Home Assistant: ovládání světel](https://www.home-assistant.io/integrations/light/)
