---
title: "Automatizace nefunguje: jak zjistit proč"
description: "Najděte problém ve spouštěči, podmínce nebo akci jednoduchého pravidla."
cas: "15–20 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Automatizace"
  - "Řešení problémů"
---

## Začněte jedním pravidlem

Světlo se nerozsvítilo nebo nepřišlo upozornění? Vyberte jednu automatizaci a napište si, co měla udělat a kdy. Například: „Po deseti minutách otevřeného okna má přijít zpráva do mobilu.“ Měňte vždy jen jednu věc, abyste poznali, která úprava pomohla.

Automatizace má tři části: **spouštěč** určuje, kdy začne kontrola, **podmínky** rozhodují, zda smí pokračovat, a **akce** říkají, co má provést. Podmínky jsou volitelné. Pokud některá hlavní podmínka není splněna, akce se neprovedou.

## 1. Ověřte zařízení a vybraný cíl

Nejdříve zkuste světlo ovládat ručně z přehledu. U upozornění odešlete zprávu přímo do telefonu podle [návodu o otevřeném okně](../../navody/otevrene-okno-upozorneni/). Když nefunguje ani ruční ovládání, začněte připojením zařízení či oznámeními v mobilu.

V pravidle zkontrolujte konkrétní světlo nebo telefon. Podobné názvy mohou svádět k výběru jiného cíle. Akce pro zapnutí světla musí mířit na světlo; chytrá zásuvka s lampou může být vedena jako spínač.

## 2. Prohlédněte si záznam průběhu

V **Nastavení → Automatizace a scény** otevřete pravidlo a zvolte **Traces**, tedy záznamy průběhu. Na menší obrazovce může být volba v nabídce. Vyberte běh podle času problému a projděte jednotlivé kroky: co pravidlo spustilo, která podmínka prošla a kde skončilo.

Zastavení na nesplněné podmínce nemusí být chyba. Pravidlo „světlo jen večer“ má přes den akci odmítnout. Ověřte, jestli podmínka odpovídá vašemu záměru.

## 3. Rozlišujte ruční zkoušku a skutečné spuštění

Volba **Spustit akce** vyzkouší posloupnost akcí, ale obejde spouštěče a hlavní podmínky. Podmínky vložené dovnitř akcí se stále vyhodnocují. Úspěch této zkoušky proto nepotvrzuje celé pravidlo. Akce se provádějí doopravdy, takže u světla ověřte i skutečnou lampu.

Potom vyvolejte běžnou událost: u okna je zavřete a znovu otevřete, u časového pravidla nastavte čas několik minut dopředu. Nakonec vraťte původní nastavení. Tak ověříte i cestu od spouštěče.

## 4. Když se pravidlo vůbec nerozběhne

Zkontrolujte, že je automatizace zapnutá a sleduje správný senzor. Stavový spouštěč reaguje na změnu: už otevřené okno samo o sobě není novým otevřením. Musí nastat přechod, který jste nastavili.

Má-li spouštěč dobu trvání, musí stav vydržet celou tuto dobu. Zavření okna před limitem čekání přeruší. Restart Home Assistantu nebo znovunačtení automatizací čekání zruší také. Chybějící zpráva po restartu proto může vyplývat z tohoto omezení.

## Jak poznáte, že je opraveno

Zopakujte situaci, kdy má pravidlo zafungovat, i situaci, kdy zafungovat nemá. U okna vyzkoušejte dlouhé otevření i krátké větrání. Porovnejte skutečný výsledek se záznamem průběhu. Poznamenejte si, co jste změnili; bude se to hodit, pokud se problém vrátí.

## Zdroje

Ověřeno podle dokumentace 1. října 2026; bez testování na zařízení. Názvy voleb se mohou lišit podle verze a jazyka.

- [Home Assistant: testování a záznamy průběhu](https://www.home-assistant.io/docs/automation/troubleshooting/)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: stavový spouštěč a čekání](https://www.home-assistant.io/triggers/state/)
- [Home Assistant: podmínky automatizací](https://www.home-assistant.io/docs/automation/condition/)
- [Home Assistant: akce automatizací](https://www.home-assistant.io/docs/automation/action/)
