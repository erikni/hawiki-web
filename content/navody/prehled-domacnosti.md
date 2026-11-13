---
title: "Přehled domácnosti na jedné obrazovce"
description: "Vytvořte jednoduché ovládání se světlem, teplotou a stavem okna."
cas: "20–30 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Přehled domácnosti"
  - "Dashboard"
---

## Co bude na konci fungovat

V Home Assistantu vytvoříte vlastní přehled s několika důležitými položkami: světlem, teplotou a stavem okna. Přehled, označovaný také jako dashboard, slouží k zobrazení údajů a ovládání domácnosti. Pro tento návod stačí běžné vestavěné karty a vizuální editor.

## Co budete potřebovat

Přihlaste se účtem správce. Připravte si již připojené světlo a případně senzor teploty nebo otevření okna. Chybějící položky jednoduše vynechte. Nejdříve ověřte, že zařízení fungují v dosavadním přehledu. Srozumitelné názvy a [přiřazení místností](../mistnosti-a-patra/) vám usnadní výběr.

Začněte nejvýše pěti položkami, které skutečně používáte každý den. Smyslem je rychle najít ovládání a údaje, nikoli na první stránku umístit všechna zařízení.

## Vytvořte vlastní přehled

1. Otevřete **Nastavení → Přehledy** a zvolte přidání přehledu. V angličtině se tato část jmenuje **Dashboards**.
2. Vyberte nový prázdný přehled, například volbu **New dashboard from scratch**. Pojmenujte jej **Moje domácnost** a zapněte zobrazení v postranním panelu.
3. Pokud jej má používat rodina, neomezujte jeho viditelnost pouze na správce. Vytvoření potvrďte a přehled otevřete.
4. Vpravo nahoře zapněte úpravy. Pro uspořádání použijte zobrazení **Sekce**; pokud už je vybrané, ponechte je.

Nový přehled si upravujete ručně. Karty pro další zařízení do něj později přidáte sami. Názvy voleb se mohou lišit podle verze a jazyka Home Assistantu.

## Přidejte tři jednoduché karty

V první sekci zvolte **Přidat kartu** a typ **Dlaždice** neboli **Tile**. Vyberte své světlo. Upravte zobrazený název například na **Lampa v obýváku** a kartu uložte.

Stejným způsobem přidejte dlaždici pro senzor teploty a potom pro senzor okna. Vybírejte konkrétní údaj: u zařízení s více senzory potřebujete teplotu, nikoli třeba stav jeho baterie. Na kartách ponechte viditelný stav, abyste poznali naměřenou hodnotu nebo otevřené okno.

U světla se při výchozím nastavení dlaždice liší klepnutí na ikonu a na zbytek karty: ikona světlo přepíná, zbytek karty otevírá podrobnosti. Chování lze v nastavení akcí karty změnit. U teplotního senzoru se klepnutím žádná teplota nenastavuje; jde o zobrazení měření.

## Uspořádejte obrazovku

V režimu úprav zobrazení Sekce můžete karty přetáhnout na jiné místo. Nejčastěji používané světlo dejte na začátek. Máte-li více místností, přidejte další sekci a pojmenujte její nadpis podle místnosti. Pro první pokus ale stačí jedna sekce se třemi kartami.

## Ověřte výsledek v mobilu

Ukončete úpravy a otevřete přehled v [mobilní aplikaci](../../zaciname/home-assistant-v-mobilu/). Zapněte a vypněte skutečné světlo. Otevřete okno a ověřte změnu jeho stavu. Zkontrolujte, že názvy jsou čitelné i na malé obrazovce.

Pokud rodina přehled nevidí, ověřte zobrazení v postranním panelu a omezení na správce. Je-li hodnota nedostupná, zkontrolujte příslušný senzor v Home Assistantu. Samotná karta zařízení neopraví. Další položku přidejte až ve chvíli, kdy vám v běžném používání chybí.

## Zdroje

- [Home Assistant: přehledy a vizuální úpravy](https://www.home-assistant.io/dashboards/)
- [Home Assistant: vytvoření vlastního přehledu](https://www.home-assistant.io/dashboards/dashboards/)
- [Home Assistant: dlaždice a jejich akce](https://www.home-assistant.io/dashboards/tile/)
- [Home Assistant: sekce a přesouvání karet](https://www.home-assistant.io/dashboards/sections/)
