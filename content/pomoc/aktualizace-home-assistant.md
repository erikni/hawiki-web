---
title: "Aktualizace Home Assistant: proč počkat na verzi .2"
description: "Pro běžnou domácnost doporučujeme vynechat verze .0 a .1. Jak vybrat správný čas, připravit zálohu a ověřit výsledek."
cas: "8 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-09-30"
stav: "Redakční doporučení; postup podle dokumentace"
temata:
  - "Aktualizace"
  - "Údržba"
---

## Nová verze neznamená, že musíte hned aktualizovat

Home Assistant oznámí novou verzi. Máte chuť kliknout na aktualizaci a mít hotovo. Pokud vám ale domácnost funguje, můžete si nejprve vybrat vhodný čas a přečíst, co se mění.

**Pro běžné měsíční aktualizace doporučujeme vynechat první vydání `.0` i první opravnou verzi `.1`. O přechodu uvažujte nejdříve od `.2`.** Jde o naše pravidlo pro klidnější provoz domácnosti, nikoliv o záruku bezproblémové aktualizace.

Tento článek se týká **Home Assistant Core**, tedy hlavního programu. Operační systém, aplikace, komunitní rozšíření a software jednotlivých zařízení mají vlastní číslování a vlastní postupy aktualizace.

## Jak se vyznat v čísle verze

Home Assistant Core používá označení ve tvaru **rok.měsíc.oprava**. Zápis `YYYY.MM.0` znamená první vydání v daném měsíci, `YYYY.MM.1` první opravné vydání.

Následující čísla jsou příklady, nikoliv doporučení konkrétní aktuální verze:

| Verze | Co znamená | Náš běžný postup |
| --- | --- | --- |
| `2026.9.0` | První zářijové vydání | S běžným upgradem počkat |
| `2026.9.1` | První opravné vydání | Ještě počkat a sledovat opravy |
| `2026.9.2` | Druhé opravné vydání | Začít posuzovat přechod podle změn a své domácnosti |
| `2026.9.3` a další | Další opravná vydání | Vybrat vhodné vydání podle poznámek a známých problémů |

V reálném označení může být měsíc bez úvodní nuly, například `9` místo `09`.

## Proč vynecháváme .0 a .1

Měsíční vydání přináší změny a nové možnosti. Následující opravná vydání řeší chyby. Vyčkání dává čas na další opravy a na zkušenosti z různých domácností.

Verze `.0` a `.1` přitom **jsou stabilní vydání, nikoliv beta verze**. Home Assistant měsíční vydání testuje a oficiálně je doporučuje. Naše doporučení je opatrnější volba pro domácnost, která dává přednost předvídatelnému provozu před okamžitým používáním novinek.

Ani `.2` nezaručuje, že funguje vaše konkrétní topení, osvětlení nebo komunitní propojení. Rozhodnutí musí zahrnovat i změny, které se týkají právě vás. Neodkládejte zároveň údržbu na neurčito: vyberte si pravidelný termín, kdy aktualizace posoudíte.

## Kdy aktualizovat dříve

Pravidlo „počkám na .2“ má výjimky:

- **Důležitá bezpečnostní oprava, která se vás týká.** Řiďte se oznámením a doporučeným postupem; samotné číslo verze není důvod opravu odkládat.
- **Oprava problému, který už doma máte.** Pokud nové vydání řeší nefunkční důležitou funkci, může dávat smysl přejít dříve.

V obou případech stále potřebujete zálohu a čas na ověření. Pokud vám konkrétní novinka jen připadá zajímavá, obvykle to není důvod ke spěchu.

## Chcete vyzkoušet beta verzi?

Beta je testovací vydání připravované verze. Můžete si v něm vyzkoušet novinky a pomoci odhalit chyby. Pro běžnou domácnost, kde potřebujete spolehlivé topení nebo osvětlení, doporučujeme zůstat u stabilních vydání. Betu si nejlépe vyzkoušejte na oddělené testovací instalaci.

### Kde zapnout beta kanál

V Home Assistant OS:

1. Nejdříve vytvořte zálohu současné stabilní verze a uložte ji i mimo zařízení.
2. Otevřete **Nastavení → Systém → Aktualizace**.
3. Vpravo nahoře otevřete nabídku **tří teček**.
4. Vyberte **Připojit se k beta kanálu**; v angličtině **Join beta**.
5. Zkontrolujte nabídnutou verzi a až poté spusťte aktualizaci Home Assistant Core.

Pokud se nabídka neobjeví, zvolte kontrolu aktualizací. Názvy položek se mohou podle jazyka a verze mírně lišit. Beta kanál může změnit nabídku aktualizací i dalších spravovaných součástí, proto vždy čtěte, kterou součást právě aktualizujete. U instalace v kontejneru se testovací verze vybírá jiným postupem; tento návod je pro Home Assistant OS.

### Jak se vrátit ke stabilním vydáním

Ve stejné nabídce aktualizací opustíte beta kanál. **Změna kanálu sama nepřeinstaluje už nainstalovanou betu na starší stabilní verzi.** Můžete počkat na vhodné stabilní vydání, nebo se při potřebě návratu řídit postupem obnovy předchozí zálohy. Zálohu ze stabilní verze si proto ponechte.

V nabídce **Nastavení → Systém → Labs** lze také vyzkoušet vybrané připravované možnosti. Labs je jiná funkce než instalace beta verze celého programu.

## Jak je to s aktualizacemi integrací a dalších součástí?

Integrace znamená propojení Home Assistant se zařízením nebo službou. Aktualizace propojení a aktualizace samotného zařízení jsou dvě různé věci.

| Co aktualizujete | Odkud přichází aktualizace | Platí pravidlo „počkat na .2“? |
| --- | --- | --- |
| **Vestavěné integrace** | Jsou součástí vydání Home Assistant Core | Ano, jako součást našeho doporučení pro Core |
| **Komunitní integrace a prvky rozhraní z HACS** | Z vlastního projektu autora, spravovaného přes HACS | Ne; mají vlastní verze a požadavky |
| **Aplikace, dříve označované add-ons** | Ze svého repozitáře v nabídce aplikací | Ne; posuzujte každou zvlášť |
| **Home Assistant OS a Supervisor** | Z vlastního aktualizačního systému | Ne; nepoužívají stejné měsíční číslování jako Core |
| **Software chytrého zařízení** | Od výrobce, někdy dostupný také přes Home Assistant | Ne; řiďte se dokumentací konkrétního zařízení |

### Vestavěné integrace

Například propojení, které je součástí standardního Home Assistant, se běžně aktualizuje s Core. Nemusíte pro něj zvlášť hledat tlačítko pro instalaci nové verze integrace. Změny v poznámkách k vydání Core se proto mohou týkat i vašich světel nebo zálohování.

Tlačítko **Znovu načíst** u integrace pouze znovu načte propojení. Samo nenainstaluje novější kód.

### Komunitní integrace z HACS

Každý projekt má vlastní pravidla vydávání. Označení `1.0` nebo `2.1` u komunitní integrace není totéž co měsíční verze `.0` a `.1` Home Assistant Core. Neodmítejte tedy aktualizaci jen podle posledního čísla.

Před instalací si přečtěte změny, požadovanou verzi Core a případné pokyny k restartu. Aktualizujte jedno rozšíření a vyzkoušejte jeho funkce. Pokud autor nabízí testovací vydání, vybírá se samostatně podle možností HACS a daného projektu; beta kanál Home Assistant ho automaticky nezapne.

**Pořadí aktualizací závisí na požadavcích autora.** Některé nové verze rozšíření potřebují nejprve novější Core, jiné je vhodné aktualizovat před přechodem na nový Core. Když vhodná kompatibilní verze ještě není dostupná a integraci potřebujete, běžný upgrade odložte.

### Aplikace a software zařízení

Také zde čtěte informace o změnách a dostupném návratu. Záloha Home Assistant nemusí obnovit předchozí software žárovky, termostatu nebo jiné samostatné krabičky. Nespoléhejte proto na to, že obnova HA vrátí úplně každou aktualizaci v domácnosti.

Pro důležité součásti, například službu propojující senzory, doporučujeme plánovanou ruční aktualizaci a následnou kontrolu. Pokud používáte automatické aktualizace, zvažte, zda máte přehled o tom, co se změnilo a jak ověříte výsledek.

## Před aktualizací: připravte si cestu zpět

1. **Přečtěte si poznámky k vydání.** Hledejte svá zařízení, používaná propojení a změny vyžadující úpravu nastavení. Při přeskoku více měsíců projděte i vynechaná měsíční vydání.
2. **Ověřte komunitní rozšíření.** Používáte-li HACS, zkontrolujte požadavky a známé problémy důležitých projektů.
3. **Vytvořte čerstvou zálohu před upgradem.** Ověřte její dokončení, kopii mimo hlavní zařízení a dostupný šifrovací klíč. Nespoléhejte jen na starou položku v seznamu.
4. **Poznamenejte si původní verzi.** Zálohu označte datem a důvodem, například „před zářijovým upgradem“.
5. **Vyberte klidný čas.** Aktualizujte, když jste doma a můžete řešit případný problém. Ne těsně před odjezdem ani ve chvíli, kdy na systému závisí důležitý provoz.

Podrobný plán uložení a uchovávání kopií najdete v [článku o zálohování 3–2–1](../zalohovani-3-2-1/).

## Jak provést aktualizaci

Pro Home Assistant OS otevřete **Nastavení** a přejděte do přehledu aktualizací. Vyberte aktualizaci **Home Assistant Core**, přečtěte její informace a ověřte, jakou verzi nabízí.

Po dokončení přípravy spusťte instalaci a nechte ji doběhnout. Během restartu může být ovládání dočasně nedostupné. Přesné názvy tlačítek se mohou lišit podle verze a jazyka.

Pro snadnější hledání případné příčiny problému doporučujeme měnit **jednu součást po druhé**. Pořadí zvolte podle požadavků jednotlivých součástí, mezi změnami ověřujte fungování. U jiné instalace použijte postup z její dokumentace.

## Po aktualizaci: nestačí, že se otevře stránka

Vyzkoušejte několik funkcí, které běžně používáte:

- Ovládání světla z přehledu i fyzickým tlačítkem.
- Jednu automatizaci včetně skutečného spouštěče.
- Topení, žaluzie nebo jinou důležitou funkci, kterou doma máte.
- Upozornění na mobilu a dostupnost důležitých zařízení.
- Zálohování a přenos do dalších úložišť.

Zkontrolujte také hlášené problémy v Nastavení. Předchozí zálohu nemažte hned po přihlášení; ponechte ji do ověření běžného provozu, například do následujícího dne. U pravidel, která se spouštějí jednou týdně, potřebujete ověřit i tento delší cyklus.

## Když něco přestane fungovat

Nejdříve zjistěte, zda jde o jedno zařízení, jedno propojení, nebo celý systém. Podívejte se na hlášení a známé problémy vydání. Neprovádějte několik dalších změn najednou.

Pokud je potřeba návrat, postupujte podle [oficiálního návodu na obnovu zálohy](https://www.home-assistant.io/common-tasks/general/#restoring-a-backup). Obnova vrátí vybrané části do uloženého stavu; změny provedené po záloze se mohou ztratit. Vyhraďte si na ni čas.

## Jednoduché pravidlo pro domácnost

**Běžný měsíční upgrade: .0 a .1 vynechat, od .2 posoudit změny, připravit zálohu a aktualizovat v klidu. Bezpečnostní opravy řešit podle jejich závažnosti.**

## Zdroje a další čtení

- [Home Assistant: stabilní vydání a opravné verze](https://www.home-assistant.io/faq/)
- [Aktualizace Home Assistant OS a jeho součástí](https://www.home-assistant.io/common-tasks/os/)
- [Správa komunitních projektů v HACS](https://www.hacs.xyz/docs/use/repositories/dashboard/)
- [Oficiální oznámení nových verzí](https://www.home-assistant.io/blog/)
- [Zálohování metodou 3–2–1](../zalohovani-3-2-1/)
