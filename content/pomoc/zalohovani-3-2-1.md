---
title: "Zálohování 3–2–1: kam ukládat zálohy a jak dlouho je držet"
description: "Jednoduchý plán, jak nepřijít o nastavení Home Assistant při poruše zařízení nebo problému doma."
cas: "10 minut čtení"
obtiznost: "Snadné"
kontrola_zdroju: "2026-09-30"
stav: "Podle dokumentace"
temata:
  - "Zálohování"
  - "Pravidlo 3–2–1"
---

## Proč nestačí záloha přímo v Home Assistant

Máte nastavená světla, topení a oblíbená tlačítka. Pak se porouchá zařízení, na kterém Home Assistant běží. Pokud na něm byla i jediná záloha, nemusíte se k ní dostat.

Metoda **3–2–1** pomáhá rozložit toto riziko: mít více kopií, oddělit jejich úložiště a jednu uchovat mimo domácnost.

## Co znamenají čísla 3–2–1

| Číslo | Význam | Příklad pro domácnost |
| --- | --- | --- |
| **3** | Tři kopie důležitých dat celkem | Aktuální data a alespoň dvě záložní kopie |
| **2** | Dva různé druhy úložišť | Úložiště zařízení a samostatný záložní disk; další kopie bude na Google Disku |
| **1** | Jedna kopie mimo domov | Šifrovaná kopie na Google Disku |

V běžném výkladu pravidla se do tří kopií počítají i aktuální data. **V našem příkladu půjdeme o krok dál: budeme mít tři záložní kopie navíc k běžícímu systému.** Jednu přímo v Home Assistant, druhou na odděleném domácím úložišti a třetí mimo domov.

## Tři místa pro vaše zálohy

| Místo | K čemu pomůže | Co samo nevyřeší |
| --- | --- | --- |
| **Přímo v Home Assistant** | Rychlý návrat po nepovedené změně | Poruchu zařízení nebo jeho disku |
| **Domácí NAS nebo samostatný USB disk** | Obnovu po poruše hlavního zařízení | Událost, která zasáhne celou domácnost |
| **Cloud, například Google Disk** | Obnovu i při ztrátě domácích zařízení | Potřebujete funkční přístup k účtu a šifrovací klíč |

NAS je domácí krabička s disky dostupná po síti. U USB disku se pro začátečníka nabízí jednoduchá cesta: zkopírovat na něj zálohu přes počítač a poté jej odpojit. Samotné zasunutí USB disku do zařízení s Home Assistant automatické zálohování nenastaví.

USB disk, na který přesunete samotný běžící systém nebo jeho hlavní data, není touto druhou záložní kopií. Potřebujeme **samostatně uložený soubor zálohy**.

Zde pro cloudovou kopii použijeme Google Disk. Dvě složky na stejném disku nebo ve stejném cloudovém účtu nepředstavují dvě nezávislá úložiště.

## Jak začít v Home Assistant

Pokud ještě zálohy nemáte, projděte nejprve [základní návod na zálohování](../zalohovani/).

Následující postup je určený pro Home Assistant OS. Dostupná úložiště se mohou lišit podle instalace a připojených služeb.

1. Otevřete **Nastavení → Systém → Zálohy**.
2. Nastavte automatické zálohování, například každý den.
3. Připravte domácí NAS jako záložní úložiště, případně plán pravidelného kopírování na USB disk.
4. V nastavení záloh zkontrolujte místní ukládání do Home Assistant a zapněte dostupná další umístění. Google Disk připojíte podle následující části.
5. Uložte **nouzovou sadu se šifrovacím klíčem** bezpečně mimo samotné zařízení Home Assistant.
6. Vytvořte zálohu a zkontrolujte, že dorazila do vybraných míst.

Názvy tlačítek se mohou podle verze a jazyka mírně lišit. Kopie mimo domov musí být dostupná také v případě, že svůj Home Assistant vůbec nespustíte.

## Jak připojit Google Disk

Home Assistant má vestavěné propojení **Google Drive**, které lze použít jako umístění záloh. Pro tuto cestu nepotřebujete HACS.

První připojení vyžaduje také nastavení v Google Cloud Console. Je to složitější část přípravy, proto si na ni nechte čas nebo požádejte někoho o pomoc. Google Cloud Console zde slouží k povolení přístupu; záložní soubory budou uložené na vašem Google Disku.

1. Podle [oficiálního průvodce Google Drive](https://www.home-assistant.io/integrations/google_drive/) připravte přístupové údaje a povolte Google Drive API.
2. V Home Assistant otevřete **Nastavení → Zařízení a služby → Přidat integraci** a vyhledejte **Google Drive**.
3. Dokončete propojení se svým účtem Google podle pokynů na obrazovce.
4. V nastavení automatických záloh vyberte Google Drive jako další umístění a ověřte, že je pro něj zapnuté šifrování.
5. Vytvořte zálohu. Na Google Disku zkontrolujte složku **Home Assistant** a datum souboru.

Podrobná příprava přístupových údajů je v odkazovaném průvodci. Tento článek vysvětluje zálohovací plán; nenahrazuje celý postup nastavení účtu Google.

## Retence: jak dlouho zálohy uchovávat

**Retence znamená, jak dlouho nebo kolik záloh ponecháte, než smažete starší.** Více úložišť chrání před poruchou. Více starších verzí pomůže, když chybu objevíte až za několik týdnů.

Následující čísla jsou **náš výchozí návrh pro běžnou domácnost**, nikoliv povinné nastavení nebo výchozí hodnoty Home Assistant.

| Úložiště | Navržená retence | Proč |
| --- | --- | --- |
| **Home Assistant** | Posledních **7 denních záloh** | Rychlá obnova nedávného stavu bez dlouhého zaplňování hlavního disku |
| **Domácí NAS** | Posledních **30 denních záloh + 12 měsíčních** | Návrat do posledního měsíce i k vybranému stavu z minulého roku |
| **USB disk místo NAS** | **8 týdenních záloh + 12 měsíčních** | Pro ruční kopírování jednou týdně je tento plán snáze udržitelný |
| **Google Disk** | Posledních **14 denních záloh + 6 měsíčních** | Aktuální kopie mimo domov a delší historie při rozumných nárocích na místo |

Měsíční záloha znamená například jednu vybranou kopii z prvního dne měsíce. Nemusíte archivovat každý den po celý rok. Jedna kopie může současně splňovat denní i měsíční výběr; není nutné ji ukládat dvakrát.

### Přímo v Home Assistant: krátká historie

Pokud vytváříte jednu zálohu denně a ponecháte sedm úspěšných záloh, získáte přibližně týden historie. Při vynechaném zálohování nebo více zálohách za den není počet souborů totéž co počet dní.

Kopii před důležitou změnou držte zvlášť, dokud neověříte, že vše funguje. Před smazáním místní zálohy se ujistěte, že máte použitelnou kopii i jinde.

### NAS nebo USB: delší domácí archiv

Na NAS můžete využít vlastní archivaci či verzování, pokud je vaše úložiště podporuje. U USB si stanovte pravidelný den pro kopírování. Soubory pojmenujte podle data a staré kopie mažte teprve po úspěšném uložení nové.

USB disk po kopírování bezpečně odpojte. Archiv na stále připojeném disku může zasáhnout stejná chyba nebo nežádoucí smazání jako hlavní systém.

### Google Disk: historie i mimo domácnost

Na Google Disku kontrolujte poslední úspěšný přenos a dostupné místo. Měsíční kopie uchovávejte v samostatném archivu, který není součástí automatického promazávání běžných záloh.

Pro začátek můžete jednou měsíčně v rozhraní Google Disku vytvořit samostatnou kopii ověřené zálohy do vlastní archivní složky. Kopírujete už uložený šifrovaný soubor; ponechte si odpovídající klíč. Samostatný archiv ve stejném účtu přidává historii, ale nepočítá se jako čtvrté nezávislé úložiště.

### Co umí nastavení v Home Assistant

Vestavěné automatické zálohování umožňuje určit počet uchovávaných záloh. **Tabulka výše je výsledný plán; není to návod na čtyři samostatné přepínače retence v Home Assistant.** Dostupné možnosti závisejí na použitém úložišti a nástroji.

Pokud vaše nastavení používá společný počet kopií pro více míst, samotným tímto číslem rozdílnou retenci nenastavíte. Pro delší historii využijte samostatný archiv na NAS a Google Disku, vlastní možnosti zálohovacího nástroje nebo ruční výběr měsíčních kopií.

Například: Home Assistant ponechá sedm denních kopií ve spravovaných umístěních. Na NAS průběžně archivujete kopie, abyste dosáhli 30 denních a 12 měsíčních; na Google Disku podobně 14 denních a 6 měsíčních. **Bez tohoto dalšího kroku by všude zůstalo jen těch sedm.** Pokud chcete vše automaticky, potřebujete nástroj, který tento archivní plán skutečně podporuje.

### Kolik místa si připravit

Zjistěte velikost jedné běžné zálohy a vynásobte ji počtem plánovaných kopií. Při velikosti 1 GB vychází orientačně:

- Home Assistant: 7 GB.
- NAS: nejvýše přibližně 42 GB pro uvedený plán.
- USB: nejvýše přibližně 20 GB.
- Google Disk: nejvýše přibližně 20 GB.

Je to hrubý odhad bez růstu a s možným překryvem denních a měsíčních kopií. Připravte rezervu a zohledněte ostatní soubory. NAS a USB jsou zde dvě alternativy pro druhé umístění; nemusíte pořizovat obě.

## Šifrovací klíč patří k záloze

Šifrovanou zálohu lze obnovit jen s příslušným klíčem. Uložte nouzovou sadu například do správce hesel, ke kterému se dostanete i bez Home Assistant. Klíč nezveřejňujte.

Pozor na ručně stažené soubory: při stažení přes stránku záloh Home Assistant se záloha podle dokumentace dešifruje. Takový soubor nenahrávejte do veřejné složky; chcete-li ho uchovat šifrovaný, použijte vhodné zabezpečené úložiště nebo jej samostatně zašifrujte.

## Jak poznáte, že plán funguje?

Jednou za čas si položte tyto otázky:

- Vidím čerstvou zálohu přímo v Home Assistant, na NAS nebo USB i na Google Disku?
- Zůstaly zachované také plánované týdenní nebo měsíční kopie?
- Dokážu se přihlásit na Google Disk a najít zálohu, i když Home Assistant neběží?
- Mám dostupný odpovídající klíč a přihlašovací údaje?
- Vím, které části domácnosti záloha zahrnuje?

Skutečné ověření je zkušební obnova na náhradním zařízení. Obnovený systém nejprve držte oddělený od skutečných zařízení domácnosti, aby nezačal současně spouštět stejná pravidla. Obnovu na běžícím domácím systému neprovádějte jen na zkoušku: přepsala by jeho nastavení.

## Nejčastější omyly

- **„Mám tři zálohy na jednom disku.“** Pomohou při návratu ke starší verzi, ale nepomohou při poruše tohoto disku.
- **„NAS je mimo Home Assistant, takže je mimo domov.“** Stále může být zasažený stejnou událostí jako zbytek domácnosti.
- **„Automatické zálohy už nemusím kontrolovat.“** Úložiště může být nedostupné nebo plné.
- **„Soubor zálohy znamená, že zvládnu obnovu.“** Potřebujete také přístup k souboru, klíč a použitelný postup obnovy.

## Zdroje a další čtení

- [Home Assistant: vysvětlení pravidla 3–2–1](https://www.home-assistant.io/blog/2025/01/03/3-2-1-backup/)
- [Aktuální dokumentace záloh a obnovy](https://www.home-assistant.io/common-tasks/general/)
- [Oficiální propojení Google Drive](https://www.home-assistant.io/integrations/google_drive/)
- [Náš základní návod na zálohování](../zalohovani/)
