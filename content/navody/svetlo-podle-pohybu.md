---
title: "Světlo podle pohybu: rozsvícení i zhasnutí v jedné automatizaci"
description: "Senzor rozsvítí světlo při pohybu a po dvou minutách bez pohybu ho zhasne. Jeden návod, jedna automatizace a hotový YAML."
cas: "20 minut"
obtiznost: "Snadné; vložení YAML"
kontrola_zdroju: "2026-09-30"
stav: "Podle dokumentace; YAML syntakticky ověřen"
temata:
  - "Osvětlení"
  - "Pohybový senzor"
  - "Automatizace"
  - "YAML"
---

## Co bude na konci fungovat

Přijdete na chodbu a světlo se rozsvítí. Odejdete a senzor začne hlásit, že pohyb není. Po dvou minutách tohoto stavu světlo zhasne.

Všechno zařídí **jedna automatizace se dvěma spouštěči**:

- **Pohyb:** rozsvítit.
- **Dvě minuty bez pohybu:** zhasnout.

Pokud senzor během čekání znovu zaznamená pohyb, čekání na zhasnutí se zruší. Nové dvě minuty začnou až při dalším přechodu do stavu bez pohybu.

## Co potřebujete

- Fungující Home Assistant.
- Připojený senzor pohybu se stavem pohyb / bez pohybu.
- Připojené světlo, které už umíte z Home Assistant zapnout a vypnout.

Tento příklad používá světlo typu `light`. Zásuvka označená jako `switch` potřebuje jiné akce; úpravu najdete níže. Návod rozsvěcí i ve dne a při zhasnutí vypne vybrané světlo bez ohledu na to, zda jste ho předtím zapnuli ručně.

## Najděte názvy senzoru a světla

V Home Assistant má každá ovládaná nebo sledovaná položka své ID, tedy přesný název používaný v pravidlech.

V **Nastavení → Zařízení a služby → Entity** vyhledejte senzor a světlo. V detailu si zkopírujte jejich ID. V našem příkladu jsou vymyšlená:

| Položka | Ukázkové ID |
| --- | --- |
| Senzor pohybu | `binary_sensor.pohyb_chodba` |
| Světlo na chodbě | `light.chodba` |

Vyberte skutečnou položku detekce pohybu, nikoliv baterii nebo sílu signálu senzoru. Používáme přímo spouštěče **Pohyb detekován** (`motion.detected`) a **Pohyb skončil** (`motion.cleared`). Nemusíte ručně nastavovat přechody stavů `on` a `off`. Senzor musí být v Home Assistant rozpoznaný jako senzor pohybu a vaše verze musí tyto spouštěče podporovat.

## Vložte automatizaci

1. Otevřete **Nastavení → Automatizace a scény**.
2. Vytvořte novou prázdnou automatizaci.
3. V nabídce tří teček vyberte **Upravit v YAML**.
4. Obsah editoru nahraďte kódem níže.
5. Změňte obě ID na své skutečné hodnoty ve všech výskytech.
6. Uložte a ověřte, že je automatizace zapnutá.

Kód je určený **do YAML editoru jedné automatizace**. Nepřidávejte před něj `automation:` ani úvodní pomlčku seznamu.

## Hotový YAML

```yaml
alias: Chodba – světlo podle pohybu
description: Rozsvítí při pohybu a zhasne po dvou minutách bez pohybu.
triggers:
  # Senzor začne detekovat pohyb.
  - trigger: motion.detected
    target:
      entity_id: binary_sensor.pohyb_chodba
    id: pohyb

  # Senzor musí být nepřetržitě dvě minuty bez pohybu.
  - trigger: motion.cleared
    target:
      entity_id: binary_sensor.pohyb_chodba
    options:
      for: "00:02:00"
    id: bez_pohybu

conditions: []
actions:
  - choose:
      # Větev pro spouštěč s ID „pohyb“.
      - conditions:
          - condition: trigger
            id: pohyb
        sequence:
          - action: light.turn_on
            target:
              entity_id: light.chodba

      # Větev pro spouštěč s ID „bez_pohybu“.
      - conditions:
          - condition: trigger
            id: bez_pohybu
        sequence:
          - action: light.turn_off
            target:
              entity_id: light.chodba
mode: restart
```

## Jak kód funguje

Každý spouštěč má vlastní **`id`**. Díky tomu automatizace pozná, proč právě začala. V části **`choose`**, tedy „vyber“, spustí odpovídající větev: zapnutí při `pohyb`, vypnutí při `bez_pohybu`.

**`options.for: "00:02:00"`** u `motion.cleared` znamená dvě minuty nepřetržitě ve stavu bez pohybu. Chcete pět minut? Změňte hodnotu na `"00:05:00"`.

**`mode: restart`** určuje chování při novém spuštění: případný předchozí běh akcí se ukončí a začne nový. Samotné čekání dvou minut ale zajišťuje `options.for` ve spouštěči; režim ho nenahrazuje.

## Vyzkoušejte oba spouštěče

1. Nechte senzor přejít do stavu bez pohybu a světlo zhasněte.
2. Projděte před senzorem. Ověřte, že se světlo zapnulo.
3. Odejděte z dosahu a počkejte, až senzor skutečně přejde na „bez pohybu“.
4. Od tohoto okamžiku počkejte další dvě minuty. Světlo má zhasnout.
5. Pokus opakujte, ale před koncem čekání se vraťte. Pokud senzor znovu ohlásí pohyb, původní čekání se zruší.

Doba od odchodu do zhasnutí může být delší než dvě minuty: některé senzory ještě chvíli drží stav pohybu, i když už jste odešli.

**Pouhé ruční spuštění akcí není správný test tohoto příkladu.** Nevytvoří skutečné ID spouštěče, podle kterého se vybírá větev. Testujte přechodem senzoru nebo si prohlédněte stopu skutečného běhu automatizace.

## Pokud ovládáte lampu přes zásuvku

Když je cílem například `switch.zasuvka_lampa`, změňte:

- `light.turn_on` na `switch.turn_on`.
- `light.turn_off` na `switch.turn_off`.
- Oba výskyty `light.chodba` na `switch.zasuvka_lampa`.

Běžný vypínač lampy musí zůstat zapnutý, aby ji zásuvka mohla ovládat.

## Když něco nefunguje

**Nerozsvítí se:** ověřte skutečná ID, stav senzoru a ruční ovládání světla. Spouštěč reaguje na začátek detekce pohybu; samotné uložení pravidla při již aktivním senzoru není nový pohyb. Pokud editor nepozná `motion.detected` nebo `motion.cleared`, zkontrolujte jejich dostupnost ve své verzi Home Assistant.

**Nezhasne:** zjistěte, zda senzor přestane detekovat pohyb a vydrží bez něj požadovanou dobu. Zkontrolujte také, zda světlo znovu nezapíná jiné pravidlo.

**Zhasne, když stojíte na místě:** senzor pohybu nemusí poznat nehybného člověka. Prodlužte čas nebo zvažte senzor přítomnosti vhodný pro danou místnost.

**Co restart nebo výpadek senzoru?** Čekání `for` nepřežije restart Home Assistant ani znovunačtení automatizací. Tento jednoduchý příklad neobsahuje zvláštní větev pro kontrolu po startu systému. Nezaručuje tedy srovnání světla se stavem senzoru po výpadku; podle situace může být potřeba světlo ovládat ručně a nechat proběhnout nový cyklus pohybu.

## Zdroje a další čtení

- [Pohyb detekován: motion.detected](https://www.home-assistant.io/triggers/motion.detected/)
- [Pohyb skončil: motion.cleared](https://www.home-assistant.io/triggers/motion.cleared/)
- [Spouštěče automatizací a jejich ID](https://www.home-assistant.io/docs/automation/trigger/)
- [Výběr akcí pomocí choose](https://www.home-assistant.io/docs/scripts/#choose-a-group-of-actions)
- [Editor automatizací](https://www.home-assistant.io/docs/automation/editor/)
- [Jednoduché večerní rozsvícení lampy](../lampa-vecer/)
