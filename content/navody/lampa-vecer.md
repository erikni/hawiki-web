---
title: "Lampa, která se večer rozsvítí sama"
description: "První jednoduché pravidlo nastavíte klikáním."
obrazek: "/assets/images/lampa-vecer.png"
obrazek_alt: "Večerní obývací pokoj s automaticky rozsvícenou lampou, hodinami ukazujícími 19:00 a telefonem s časovým pravidlem."
cas: "20 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-09-30"
stav: "Podle dokumentace"
temata:
  - "Osvětlení"
  - "Automatizace"
---

## Co bude na konci fungovat
Každý den v 19:00 se rozsvítí vybraná lampa. Čas si později upravíte podle sebe.

## Co potřebujete
Fungující Home Assistant a již připojenou lampu nebo podporovanou chytrou zásuvku s lampou. Nejdříve ověřte, že ji lze ručně zapnout z přehledu. U zásuvky musí být běžný vypínač lampy zapnutý.

## Postup
1. Otevřete **Nastavení → Automatizace a scény**.
2. Zvolte vytvoření nové automatizace a začněte prázdným pravidlem.
3. Přidejte spouštěč **Čas** a nastavte `19:00:00`.
4. Přidejte akci zapnutí. Pro chytrou žárovku vyberte zapnutí světla, pro zásuvku zapnutí spínače.
5. Jako cíl vyberte právě svou lampu nebo zásuvku.
6. Uložte pravidlo pod názvem **Večerní lampa**.

Názvy tlačítek se mohou podle jazyka a verze mírně lišit. Spouštěč znamená „kdy se něco stane“, akce „co má domácnost udělat“.

## Vyzkoušejte výsledek
Nejprve spusťte akce pravidla ručně. Potom nastavte čas na několik minut dopředu, lampu zhasněte a počkejte. Tím ověříte i časové spuštění. Nakonec vraťte 19:00.

## Když se lampa nerozsvítí
Zkontrolujte, zda funguje ruční ovládání, je vybrán správný cíl a pravidlo je zapnuté. Ověřte také časové pásmo domácnosti.

## Co můžete přidat
Druhé podobné pravidlo může lampu večer vypnout. Začněte jednoduchým pevným časem a až potom zvažujte podmínky podle přítomnosti.

## Zdroj
[Oficiální editor automatizací](https://www.home-assistant.io/docs/automation/editor/)
