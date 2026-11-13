---
title: "Topení podle denního režimu"
description: "Nastavte termostatu denní a noční teplotu pomocí jedné automatizace v Home Assistant."
cas: "20 minut"
obtiznost: "Střední"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - topení
  - termostat
  - automatizace
  - YAML
---

Každý večer snižujete teplotu na termostatu a ráno ji vracíte zpět? Home Assistant může tyto změny provádět podle času. Začněte jednou místností a jednoduchým plánem. Příklad nastaví od 6:00 cílovou teplotu 21 °C a od 22:00 teplotu 19 °C, každý den stejně. Hodnoty jsou ukázkové; upravte je podle své domácnosti.

## Co potřebujete

Termostat nebo hlavice musí být připojené přes svou integraci a dostupné jako entita `climate`. V jejím ovládání nejprve ručně ověřte, že lze měnit cílovou teplotu. Pouhý teplotní senzor nestačí.

Příklad předpokládá zařízení s jednou cílovou teplotou, nastavené na vytápění, a jednotky °C. Neřeší zařízení v režimu současného vytápění a chlazení se dvěma mezními teplotami. Automatizace mění požadovanou teplotu, vlastní regulaci dál provádí termostat.

Zjistěte ID entity, například `climate.obyvaci_pokoj`. Ověřte také časové pásmo Home Assistant. Pokud termostat používá vlastní časový plán, nastavte podle jeho návodu režim, ve kterém přijímá a drží změny z Home Assistant; dva plány se mohou navzájem přepisovat.

## Vložení automatizace

V **Nastavení → Automatizace a scény** vytvořte novou prázdnou automatizaci. V nabídce vpravo nahoře vyberte **Upravit v YAML** a celý obsah nahraďte příkladem. Jde o YAML jedné automatizace, nikoli o obsah souboru `configuration.yaml`.

Nahraďte `climate.obyvaci_pokoj` vlastním ID. Pokud změníte hodiny přepnutí, upravte současně časy v `at` i hranice `6` a `22` ve výpočtu teploty. Čísla `21` a `19` jsou denní a noční teplota.

```yaml
alias: Topení – den a noc
description: Denní a noční cílová teplota
triggers:
  - trigger: time
    at: "06:00:00"
  - trigger: time
    at: "22:00:00"
actions:
  - action: climate.set_temperature
    target:
      entity_id: climate.obyvaci_pokoj
    data:
      temperature: "{{ 21 if 6 <= now().hour < 22 else 19 }}"
mode: single
```

Výpočet vybere teplotu podle aktuální místní hodiny. Automatizace nemění provozní režim termostatu: pokud je vypnutý, samotné nastavení teploty nemusí spustit topení.

## Ověření a běžné používání

Uložte automatizaci a spusťte její akce ručně. Mezi 6:00 a 22:00 má termostat dostat 21 °C, jindy 19 °C. Kontrolujte **cílovou** teplotu; naměřená teplota místnosti se nemusí změnit hned. Pokud akce selže, otevřete stopu automatizace a ověřte ID, dostupnost zařízení i podporovaný rozsah teplot.

Ručně upravená teplota zůstane do dalšího přepnutí, pokud ji mezitím nezmění termostat nebo jiné pravidlo. Chcete-li plán dočasně zastavit, automatizaci vypněte a teplotu nastavte ručně. Po opětovném zapnutí spusťte její akce, aby se použila teplota odpovídající aktuálnímu času.

Home Assistant musí v 6:00 a 22:00 běžet a termostat musí být dostupný. Tento příklad zmeškané přepnutí nedohání a při návratu zařízení změnu neopakuje. Po výpadku proto stav zkontrolujte a případně spusťte akce ručně.

## Zdroje

- [Home Assistant: zařízení climate a jejich režimy](https://www.home-assistant.io/integrations/climate/)
- [Home Assistant: nastavení cílové teploty termostatu](https://www.home-assistant.io/actions/climate.set_temperature/)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: datum a čas v šablonách](https://www.home-assistant.io/docs/templating/dates-and-times/)
- [Home Assistant: editor automatizací a vložení YAML](https://www.home-assistant.io/docs/automation/editor/)
