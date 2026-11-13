---
title: "Upozornění na slabé baterie senzorů"
description: "Nechte Home Assistant každý večer zkontrolovat baterii senzoru a zobrazit připomínku výměny."
cas: "15 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - baterie
  - senzory
  - automatizace
  - YAML
---

Čidlo na okně přestane hlásit změny a teprve potom zjistíte, že potřebuje novou baterii. Home Assistant může stav baterie pravidelně kontrolovat. Začněte jedním senzorem: každý večer v 18:00 ověří jeho hodnotu. Zareaguje také při změně údaje baterie. Při 20 % nebo méně zobrazí připomínku přímo v rozhraní Home Assistant.

## Vyberte správnou entitu

U zařízení najděte entitu baterie, například `sensor.okno_baterie`. Příklad potřebuje číselnou hodnotu v procentech. Některá zařízení poskytují jen informaci „slabá baterie“ jako `binary_sensor`; pro ně tento YAML není vhodný.

Ověřte ID entity a jednotku %. Hranice 20 % je ukázková, upravte ji podle zařízení. Upozornění se opírá o poslední dostupný údaj; automatizace sama nevynutí nové měření baterie. Neslibuje ani konkrétní počet zbývajících dnů provozu.

## Vložte automatizaci

V **Nastavení → Automatizace a scény** vytvořte prázdnou automatizaci. V nabídce vpravo nahoře zvolte **Upravit v YAML** a nahraďte celý obsah následujícím blokem. Patří do editoru jedné automatizace, nikoli do `configuration.yaml`.

Nahraďte všechny výskyty `sensor.okno_baterie` vlastním ID. Upravte název čidla ve zprávě, případně čas `18:00:00` a hranici `20`. Hranice zahrnuje i přesně 20 %. Pokud ji změníte, upravte číslo v podmínce šablony.

```yaml
alias: Slabá baterie čidla na okně
triggers:
  - trigger: time
    at: "18:00:00"
  - trigger: state
    entity_id: sensor.okno_baterie
    to: null
actions:
  - condition: template
    value_template: >-
      {{ is_number(states('sensor.okno_baterie'))
         and states('sensor.okno_baterie') | float(101) <= 20 }}
  - action: persistent_notification.create
    data:
      title: Slabá baterie
      message: Zkontrolujte baterii čidla na okně.
      notification_id: baterie_okno
mode: single
```

Podmínka je součástí akcí, takže se kontroluje i při jejich ručním spuštění. Spouštěč reaguje na změnu hodnoty baterie, nikoli na změnu pouhých atributů. Hranice se kontroluje až v podmínce před oznámením. Při změně na 20 % nebo méně se připomínka vytvoří nebo aktualizuje, například i při poklesu z 20 % na 19 %. Při vyšší hodnotě se oznámení nevytvoří. Stejné `notification_id` aktualizuje existující připomínku místo vytváření dalších kopií.

## Kde zprávu uvidíte

Jde o trvalé oznámení v rozhraní Home Assistant, které můžete zavřít. Není to push zpráva na zamčenou obrazovku telefonu; pro takovou zprávu by bylo potřeba přidat oznámení mobilní aplikaci.

Po výměně baterie zkontrolujte nový údaj a připomínku ručně zavřete. Příklad ji při zlepšení stavu automaticky nemaže. Pokud ji zavřete a baterie zůstane na hranici nebo pod ní, následující večerní kontrola ji vytvoří znovu.

## Ověřte výsledek

Uložte automatizaci a spusťte její akce. Má-li baterie 20 % nebo méně, zkontrolujte oznámení. Jinak můžete pro krátkou zkoušku zvýšit hranici nad aktuální hodnotu a po kontrole ji vrátit zpět. Ve stopě automatizace uvidíte, zda ji zastavila podmínka.

Stavy `unknown` a `unavailable` nejsou číslo: tento příklad při nich zprávu o slabé baterii nevytvoří. Návrat z takového stavu na číselnou hodnotu spustí kontrolu znovu. Nedostupné zařízení proto kontrolujte samostatně. Home Assistant musí při kontrole běžet. Zmeškaný čas se nedohání; další změna údaje baterie nebo večerní kontrola stav vyhodnotí znovu.

Pro další čidlo automatizaci zkopírujte a změňte ID entity, text i `notification_id`, aby mělo vlastní připomínku.

## Zdroje

- [Home Assistant: číselné podmínky](https://www.home-assistant.io/docs/scripts/conditions/)
- [Home Assistant: trvalá oznámení](https://www.home-assistant.io/integrations/persistent_notification/)
- [Home Assistant: vytvoření oznámení](https://www.home-assistant.io/actions/persistent_notification.create/)
- [Home Assistant: časové spouštěče](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: šablony](https://www.home-assistant.io/docs/templating/)
- [Home Assistant: editor automatizací](https://www.home-assistant.io/docs/automation/editor/)
