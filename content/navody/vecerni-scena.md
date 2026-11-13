---
title: "Jedno tlačítko pro večerní pohodu"
description: "Uložte nastavení několika světel do scény a vyvolejte je z přehledu."
cas: "20 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Scény"
  - "Osvětlení"
---

## Co bude na konci fungovat

Jedním klepnutím zhasnete hlavní světlo a rozsvítíte lampu tak, jak vám večer vyhovuje. Nastavení uložíte jako **scénu** s názvem Večerní pohoda. Scéna uchovává požadované stavy vybraných položek; při vyvolání je Home Assistant použije.

Scénu můžete spustit ručně. Sama neurčuje čas ani podmínku spuštění. Pokud ji později budete chtít vyvolávat automaticky, přidáte ji jako akci do automatizace.

## Co budete potřebovat

Fungující Home Assistant, účet správce a dvě již připojená světla. Vyzkoušejte jejich ruční ovládání. U lampy přes chytrou zásuvku můžete použít zapnutí spínače, ale zásuvka sama nenastaví jas běžné žárovky.

Stmívání, barvu nebo teplotu bílé nastavujte pouze tehdy, pokud je světlo a jeho integrace podporují. Pro první scénu úplně stačí zapnutí lampy a vypnutí hlavního světla.

## Uložte večerní nastavení

1. Otevřete **Nastavení → Automatizace a scény**, přejděte do části **Scény** a zvolte přidání nové scény.
2. Pojmenujte ji **Večerní pohoda**. Přidejte konkrétní entity hlavního světla a lampy nebo její zásuvky. Výběrem jednotlivých entit máte přehled, co do scény zahrnujete.
3. V editoru nastavte hlavní světlo jako vypnuté a lampu jako zapnutou. U podporované lampy nastavte i příjemný jas, například 30 %.
4. Scénu uložte. Názvy tlačítek se mohou lišit podle jazyka a verze.

Při nastavování v editoru se mohou skutečná světla měnit. Dokumentace editoru popisuje uložení požadovaných stavů a obnovení předchozího nastavení při jeho opuštění. Výsledek proto posuzujte až samostatným vyvoláním uložené scény.

## Přidejte tlačítko do přehledu

Otevřete svůj [vlastní přehled domácnosti](../prehled-domacnosti/) a zapněte jeho úpravy. Přidejte vestavěnou kartu **Tlačítko** neboli **Button** a jako entitu vyberte právě vytvořenou scénu.

V nastavení chování při klepnutí vyberte **Provést akci**. Zvolte aktivaci scény, označenou `scene.turn_on`, a jako cíl určete **Večerní pohoda**. Tlačítku dejte stejný srozumitelný název a uložte je. Tím výslovně určíte, že klepnutí má scénu spustit.

## Vyzkoušejte skutečný výsledek

Ukončete úpravy. Zapněte hlavní světlo a lampu vypněte, aby výchozí stav byl jiný než uložená scéna. Klepněte na nové tlačítko a zkontrolujte obě skutečná světla. U stmívatelné lampy ověřte i jas. Stejnou zkoušku proveďte v mobilní aplikaci.

Pokud se otevřou jen podrobnosti, zkontrolujte akci při klepnutí. Jestli reaguje jen jedno světlo, ověřte druhé ručně a zkontrolujte, zda jste do scény zahrnuli správnou entitu. Změnu požadovaného nastavení provádějte v editoru scény a potom scénu znovu vyzkoušejte.

## Jak večerní nastavení ukončit

Scéna není běžný vypínač a nemá stav zapnuto či vypnuto. Dalším klepnutím znovu použijete stejné nastavení; nevrátíte tím předchozí stav světel. Světla změňte ručně, nebo si vytvořte druhou scénu **Běžné osvětlení** s vlastním tlačítkem.

## Zdroje

- [Home Assistant: editor scén](https://www.home-assistant.io/docs/scene/editor/)
- [Home Assistant: scény a jejich aktivace](https://www.home-assistant.io/integrations/scene/)
- [Home Assistant: karta Tlačítko](https://www.home-assistant.io/dashboards/button/)
- [Home Assistant: akce při klepnutí](https://www.home-assistant.io/dashboards/actions/)
- [Home Assistant: ovládání světel](https://www.home-assistant.io/integrations/light/)
