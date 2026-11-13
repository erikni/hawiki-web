---
title: "Pračka doprala: zpráva místo hlídání"
description: "Rozpoznejte konec praní podle příkonu a odešlete zprávu do telefonu."
cas: "30 minut nastavení; ověření během praní"
obtiznost: "Mírně pokročilé"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Pračka"
  - "Upozornění"
  - "Automatizace"
---

## Co bude na konci fungovat

Home Assistant pozná zvýšený příkon pračky jako začátek práce. Když potom odběr zůstane dostatečně dlouho nízký, pošle zprávu do mobilu. Jde o odhad podle měření, proto jej nejprve ověřte na celém pracím programu.

## Co budete potřebovat

Potřebujete připojené měření okamžitého příkonu pračky ve **wattech**, funkční [oznámení do telefonu](../otevrene-okno-upozorneni/) a účet správce. Senzor energie v kWh pro tento postup nestačí.

Použijete-li zásuvku s měřením, musí výrobce dovolovat použití s daným spotřebičem a jeho zátěží. Ověřte návody zásuvky i pračky; samotný maximální proud není potvrzením vhodnosti. Automatizace zásuvku nevypíná.

## Nejdříve poznejte průběh praní

V historii senzoru sledujte jeden celý program: klid před spuštěním, praní včetně přestávek a stav po dokončení. Čekání na konec musí být delší než běžné přestávky s nízkým odběrem.

Níže uvedené **20 W po jednu minutu** pro začátek a **méně než 5 W po pět minut** pro konec jsou pouze příklad. Použijte je jen tehdy, pokud odpovídají vašemu naměřenému průběhu. Když se pauza a konec nedají takto odlišit, tento jednoduchý postup není pro daný program vhodný.

## Přidejte paměť, že pračka pracuje

V **Nastavení → Zařízení a služby → Pomocníci** vytvořte pomocníka typu **Přepínač** neboli **Toggle**, pojmenujte jej **Pračka pracuje** a nechte jej vypnutý. Jde o pomocnou entitu `input_boolean`, která uchová informaci pro druhé pravidlo; neovládá napájení pračky.

## Příklad automatizací v YAML

Místo naklikání pravidel můžete použít tyto bloky. Každý vložte zvlášť do YAML editoru nové automatizace, bez obalového klíče `automation:`. Nahraďte `sensor.pracka_prikon`, `input_boolean.pracka_pracuje` a `notify.mobile_app_muj_telefon` vlastními identifikátory. Prahy a doby upravte podle měření.

První pravidlo zapamatuje začátek:

```yaml
alias: Pračka začala
triggers:
  - trigger: numeric_state
    entity_id: sensor.pracka_prikon
    above: 20
    for: "00:01:00"
actions:
  - action: input_boolean.turn_on
    target:
      entity_id: input_boolean.pracka_pracuje
mode: single
```

Druhé po poklesu zkontroluje pomocníka, vypne jej a pošle zprávu. Při selhání oznámení se zpráva automaticky neopakuje.

```yaml
alias: Pračka dokončila
triggers:
  - trigger: numeric_state
    entity_id: sensor.pracka_prikon
    below: 5
    for: "00:05:00"
conditions:
  - condition: state
    entity_id: input_boolean.pracka_pracuje
    state: "on"
actions:
  - action: input_boolean.turn_off
    target:
      entity_id: input_boolean.pracka_pracuje
  - action: notify.mobile_app_muj_telefon
    data:
      message: "Příkon pračky zůstal nízký. Zkontrolujte praní."
mode: single
```

Pomocníka vytvořte podle předchozí části v rozhraní, nebo alternativně přidejte následující do `configuration.yaml`. Pokud už sekce `input_boolean:` existuje, vložte do ní jen položku `pracka_pracuje`. Nevytvářejte pomocníka oběma způsoby. Po kontrole konfigurace a restartu bude dostupný; bez `initial` obnovuje předchozí stav, při prvním spuštění je vypnutý.

```yaml
input_boolean:
  pracka_pracuje:
    name: Pračka pracuje
```

## Vyzkoušejte celý program

Pravidla nastavte před začátkem praní. Sledujte, že se pomocník po rozběhu zapne a během běžných přestávek nepřijde předčasná zpráva. Po konci ověřte oznámení i vypnutí pomocníka.

Číselný spouštěč reaguje na překročení hranice, nikoli stále dokola. Čekání se při restartu nebo znovunačtení automatizací zruší. Po přerušení programu či výpadku měření může být odhad chybný; zkontrolujte skutečný stav a pomocníka podle potřeby ručně vypněte.

## Zdroje

- [Home Assistant: číselný spouštěč a jeho omezení](https://www.home-assistant.io/triggers/numeric_state/)
- [Home Assistant: pomocný přepínač](https://www.home-assistant.io/integrations/input_boolean/)
- [Home Assistant: podmínky automatizací](https://www.home-assistant.io/docs/automation/condition/)
- [Home Assistant: pořadí akcí](https://www.home-assistant.io/docs/automation/action/)
- [Companion: oznámení do telefonu](https://companion.home-assistant.io/docs/notifications/notifications-basic/)
