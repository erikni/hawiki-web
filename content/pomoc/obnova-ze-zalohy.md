---
title: "Obnova ze zálohy: domácnost nemusíte nastavovat znovu"
description: "Jak se vrátit po nepovedené změně nebo obnovit Home Assistant na náhradním zařízení."
cas: "10 minut čtení; na samotnou obnovu si vyhraďte alespoň hodinu"
obtiznost: "Krok za krokem"
kontrola_zdroju: "2026-09-30"
stav: "Podle dokumentace"
temata:
  - "Zálohování"
  - "Obnova"
---

## Když se něco pokazí, začněte v klidu

Po aktualizaci něco nefunguje, odejde disk nebo přestane reagovat celé zařízení. Použitelná záloha vám může ušetřit nové nastavování domácnosti. Obnovíte uložený stav a potom zkontrolujete připojená zařízení.

**Obnova vrací stav z okamžiku zálohování.** Změny provedené později v ní nejsou. Cílem je zachránit to, co bylo skutečně zálohované; žádná záloha neslibuje ochranu před úplně všemi situacemi.

Tento průvodce je zaměřený na **Home Assistant OS**, například na [Home Assistant Green](/co-koupit/home-assistant-green/). U jiného typu instalace použijte odpovídající dokumentaci.

## Vyberte svou situaci

| Co se stalo | Kudy pokračovat |
| --- | --- |
| Home Assistant otevřete, ale potřebujete vrátit změnu | Obnova na současném zařízení |
| Původní zařízení je rozbité nebo systém nelze spustit | Obnova na čisté instalaci nebo náhradním zařízení |
| Nereaguje jen jedno zařízení | Nejprve [základní kontrola problémů](../zarizeni-nereaguje/) |

Výpadek internetu nebo vybitá baterie senzoru obvykle není důvod obnovovat celou domácnost.

## Co si připravit

- **Vhodnou zálohu.** Vyberte kopii z doby, kdy domácnost fungovala, a ponechte si originál.
- **Odpovídající šifrovací klíč**, pokud je soubor šifrovaný. Najdete ho v uložené nouzové sadě.
- **Přihlašovací údaje platné v době zálohy.** Po obnově mohou být novější změny účtu pryč.
- **Počítač s přístupem k záloze**, domácí síť a dostatek času.
- Při poruše hlavního zařízení také **náhradní zařízení s připraveným Home Assistant OS**, dostatečným úložištěm a původními dostupnými rádiovými adaptéry.

Velikost souboru zálohy sama neříká, kolik místa bude obnovená instalace potřebovat. Řiďte se požadavky v dokumentaci obnovy.

## Kde zálohu získat, když Home Assistant neběží

V našem [plánu 3–2–1](../zalohovani-3-2-1/) uchováváme kopie přímo v HA, na domácím NAS nebo USB disku a mimo domov, například na Google Disku.

Pokud se k HA nedostanete:

1. Na počítači otevřete NAS nebo připojte záložní USB disk.
2. Případně se přihlaste přímo na Google Disk a vyhledejte složku se zálohami Home Assistant nebo svůj samostatný archiv.
3. Vybraný soubor stáhněte do počítače. Zkontrolujte datum, velikost a dokončení přenosu.

K získání cloudové kopie nepotřebujete nejprve znovu zprovozňovat integraci v HA. Potřebujete přístup k účtu, souboru a případnému klíči. Zálohu nerozbalujte ani neupravujte před nahráním.

## Varianta A: obnova na současném zařízení

1. Otevřete **Nastavení → Systém → Zálohy** a vyberte vhodnou zálohu.
2. Zkontrolujte její obsah a vyberte části k obnově. Pro celý uložený stav zvolte všechny potřebné části.
3. Potvrďte obnovu a nechte ji dokončit.
4. Po návratu přihlašovací obrazovky použijte údaje platné v době zálohy.

Obnova přepíše vybrané části současné instalace. Pokud to systém ještě umožňuje, předem si uchovejte i jeho nynější stav pro případ dalšího porovnávání.

## Varianta B: původní zařízení nefunguje

1. Připravte náhradní zařízení podle [návodu k instalaci](https://www.home-assistant.io/installation/).
2. Původní systém odpojte, aby současně neovládaly domácnost dvě instalace.
3. Připojte dostupný původní Zigbee nebo Z-Wave adaptér, pokud ho používáte.
4. Na úvodní obrazovce čisté instalace zvolte **Nahrát zálohu / Upload backup** a vyberte soubor z počítače.
5. Vyberte části k obnově, případně zadejte šifrovací klíč a spusťte obnovu.
6. Po dokončení se přihlaste původními údaji.

Během obnovy neobnovujte stránku a neodpojujte napájení. Dočasná nedostupnost ovládání je očekávaná; rychlost závisí na instalaci, zařízení i síti.

## Co můžete získat zpět a co musíte zkontrolovat

Obnoví se pouze obsah zahrnutý v konkrétní záloze a vybraný při obnově. Částečná záloha nebo vynechaná média nemusí obsahovat vše, co čekáte.

Záloha HA také není kopií celé domácnosti. Samostatné soubory na NAS, nastavení routeru nebo software zařízení mohou potřebovat vlastní zálohovací plán.

Při výměně rádia Zigbee či Z-Wave může být potřeba zvláštní migrace sítě. Nevytvářejte hned nová párování všech senzorů: nejprve ověřte postup pro své propojení a adaptér. Také externí služby mohou požadovat nové přihlášení.

## Po obnově: domácnost skutečně vyzkoušejte

Než označíte obnovu za hotovou:

- Ověřte světla, topení a další důležité ovládání.
- Vyzkoušejte automatizaci jejím skutečným spouštěčem.
- Zkontrolujte upozornění a přístup členů domácnosti.
- U bateriových senzorů počkejte na další hlášení nebo je probuďte podle návodu výrobce.
- Prověřte připojení NAS, Google Disku a nastavení uchovávání záloh.
- Vytvořte novou zálohu fungujícího stavu a ověřte její kopie.

Starší ověřené kopie ponechte, dokud neotestujete i méně častá pravidla. Některé problémy se projeví až ráno nebo při dalším plánovaném spuštění.

## Když obnova nejde

**Chybí klíč:** hledejte odpovídající nouzovou sadu nebo jinou dostupnou nešifrovanou kopii. Šifrování nelze obejít novým heslem účtu.

**Soubor nelze načíst:** stáhněte jej znovu, případně použijte kopii z jiného místa. Zachovejte ostatní zálohy.

**Nedostatek místa:** vyberte vhodnější cílové úložiště. Malý komprimovaný soubor může po obnově zabrat výrazně více místa.

**Ovládání se nevrací:** ověřte, že obnova už skončila, napájení a přidělenou síťovou adresu. Při žádosti o pomoc si připravte model zařízení, datum zálohy a přesnou chybu.

## Připravte si záchranný lístek předem

Na bezpečné místo si poznamenejte umístění kopií, kde máte klíč, jak získáte přístup k účtu Google a který adaptér používáte. Hesla ukládejte do správce hesel, ne do veřejné poznámky.

Jednou za čas proveďte zkušební obnovu na oddělené instalaci bez přístupu ke skutečným zařízením domácnosti. Teprve tím ověříte i použitelnost zálohy, nejen existenci souboru.

## Zdroje a další čtení

- [Oficiální postup obnovy Home Assistant](https://www.home-assistant.io/common-tasks/general/#restoring-a-backup)
- [Nouzová sada a šifrovací klíč](https://www.home-assistant.io/more-info/backup-emergency-kit/)
- [Instalace na náhradní zařízení](https://www.home-assistant.io/installation/)
- [Zálohování 3–2–1 a retence](../zalohovani-3-2-1/)
- [Aktualizace Home Assistant](../aktualizace-home-assistant/)
