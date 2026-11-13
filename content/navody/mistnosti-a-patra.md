---
title: "Místnosti a patra: rozsvěťte celý obývák jedním příkazem"
description: "Co znamená Area, jak rozdělit domácnost do místností a pater a jak ovládat světla v celé místnosti."
cas: "15 minut"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-09-30"
stav: "Podle dokumentace; YAML syntakticky ověřen"
temata:
  - "Místnosti"
  - "Patra"
  - "Osvětlení"
  - "YAML"
---

## Proč rozdělovat domácnost do místností

V obýváku máte stropní světlo, lampu u pohovky a světelný pásek za televizí. Chcete je rozsvítit najednou. Místo vybírání každého zvlášť stačí zadat: **rozsviť světla v obýváku**.

Až přidáte další lampu a přiřadíte ji do obýváku, příkaz pro světla této místnosti ji zahrne také. Nemusíte ji dopisovat do seznamu světel v automatizaci.

## Co znamená Area a Floor

**Area znamená oblast.** Doma si ji představte jako místnost: Obývák, Kuchyň nebo Ložnice. Oblastí může být také terasa či garáž.

**Floor znamená patro nebo podlaží.** Do patra zařadíte místnosti a do místností zařízení. Každé světlo tedy nemusíte zvlášť přiřazovat do přízemí.

Takto by mohlo vypadat uspořádání domu:

| Patro | Místnost (oblast) | Příklady zařízení |
| --- | --- | --- |
| Přízemí | Obývák | Stropní světlo, lampa, teploměr |
| Přízemí | Kuchyň | Světlo nad stolem, senzor úniku vody |
| Přízemí | Chodba dole | Světlo, senzor pohybu |
| První patro | Ložnice | Noční lampičky, termostat |
| První patro | Chodba nahoře | Světlo, senzor pohybu |

V bytě klidně začněte jen místnostmi. Používejte názvy, kterými o nich doma běžně mluvíte. Dvě chodby pojmenujte například **Chodba dole** a **Chodba nahoře**, aby se vám při ovládání nepletly.

## Co vám to usnadní v praxi

Při hledání zařízení začnete místností: „Kde je teploměr v ložnici?“ Stejné rozdělení pomůže při přípravě ovládací obrazovky i automatizací.

Například můžete chtít:

- Při příchodu rozsvítit světla na chodbě.
- Před spaním zhasnout světla v obýváku.
- Při odchodu zhasnout světla v přízemí.

Místnosti a patra vám dávají společný cíl pro tyto příkazy. Samotné přiřazení zařízení ale žádnou automatizaci nevytvoří. Nejprve domácnost uspořádáte a potom nastavíte, co se má stát.

## Vytvořte místnosti a patra

1. Otevřete **Nastavení → Oblasti, štítky a zóny**. V angličtině jde o **Settings → Areas, labels & zones**; český název se může podle překladu mírně lišit.
2. Máte-li více podlaží, vytvořte patra, například **Přízemí** a **První patro**.
3. Vytvořte oblasti pro jednotlivé místnosti, například **Obývák**, **Kuchyň** a **Ložnice**.
4. U každé místnosti vyberte její patro, pokud ho používáte.

## Přiřaďte zařízení

V **Nastavení → Zařízení a služby → Zařízení** otevřete zařízení a v jeho nastavení vyberte oblast. V seznamu zařízení můžete také označit více položek a přesunout je do oblasti společně.

Začněte jednou místností. Do obýváku přiřaďte jeho stropní světlo, lampu a pásek. Zkontrolujte, že jste nevybrali podobně pojmenované světlo z ložnice.

Jedno zařízení může mít více položek, kterým Home Assistant říká **entity**. U žárovky je jednou z nich ovládání světla. Tyto položky běžně přebírají místnost zařízení. Má-li konkrétní položka nastavenou vlastní oblast, použije se její vlastní přiřazení. To se hodí třeba u zařízení, které ovládá světla ve více pokojích.

## Rozsviťte obývák bez psaní kódu

V editoru automatizace přidejte akci pro **zapnutí světla**. Jako cíl vyberte **oblast Obývák**. Jednotlivá světla nemusíte vypisovat.

Příkaz zapne dostupná světla přiřazená do obýváku. Teploměr ani televizi tím nezapnete: vybrali jste akci pro světla.

Chcete rozsvítit jen lampu u pohovky? Jako cíl vyberte přímo lampu. Oblast použijte, když chcete ovládat světla v celé místnosti.

## Stejný příklad v YAML

Toto je **jedna akce**, nikoliv celá automatizace:

```yaml
action: light.turn_on
target:
  area_id: obyvak
```

`light.turn_on` znamená zapnout světla. `area_id` vybírá místnost. Ukázková hodnota `obyvak` je vnitřní ID oblasti a musíte ji nahradit skutečným ID své místnosti.

**ID neodhadujte podle názvu.** Vyberte oblast v běžném editoru akce a potom tuto akci přepněte do YAML. Home Assistant správné ID doplní za vás.

Pro zhasnutí použijte:

```yaml
action: light.turn_off
target:
  area_id: obyvak
```

Chcete upravit [automatizaci podle pohybu](../svetlo-podle-pohybu/)? V obou jejích akcích pro světlo nahraďte cíl `entity_id: light.chodba` cílem `area_id` se skutečným ID chodby. Konkrétní senzor ve spouštěčích ponechte. Pohyb pak rozsvítí všechna světla na chodbě a po skončení pohybu a nastaveném čekání je zhasne.

## Lampa přes zásuvku: malá výjimka

Chytrá zásuvka může být vedená jako **spínač** (`switch`), i když do ní máte zapojenou lampu. Akce `light.turn_on` ji potom nezahrne ani ve správné místnosti.

Pro takovou lampu přidejte samostatnou akci pro zapnutí konkrétní zásuvky. Nezapínejte bez rozmyslu všechny zásuvky v místnosti: může mezi nimi být i jiný spotřebič.

## Ovládání celého patra

Místnosti ve stejném patře můžete použít jako společný cíl, například pro zhasnutí světel v přízemí. V editoru odpovídající akce vyberte patro jako cíl.

Patra pomohou hlavně ve větším domě. Pro každodenní ovládání často stačí místnost: když jdete spát, můžete zhasnout obývák a nechat rozsvícenou kuchyň, kde ještě někdo je.

## Vyzkoušejte výsledek

1. Zkontrolujte přiřazení světel v jedné místnosti.
2. Spusťte akci zapnutí světel s touto místností jako cílem.
3. Ověřte, že se rozsvítila správná světla a světla ve vedlejším pokoji zůstala beze změny.
4. Vyzkoušejte i zhasnutí.

Některé světlo nereaguje? Zkuste ho ovládat samostatně. Potom zkontrolujte oblast zařízení i samotné entity a zda je vedené jako světlo, nebo spínač.

Když lampu přenesete do jiného pokoje, změňte její přiřazení. Příkazy pro novou místnost ji pak zahrnou. Automatizace ovládající lampu přímo jejím ID ji ovšem bude dál ovládat bez ohledu na místnost.

**Než místnost smažete, zkontrolujte pravidla, která ji používají.** Automatizace odkazující na odstraněnou oblast potřebují upravit cíl.

## Zdroje

- [Oblasti a přiřazování zařízení](https://www.home-assistant.io/docs/organizing/areas/)
- [Patra](https://www.home-assistant.io/docs/organizing/floors/)
- [Výběr místnosti jako cíle akce](https://www.home-assistant.io/docs/scripts/perform-actions/)
