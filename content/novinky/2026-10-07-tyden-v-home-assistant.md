---
title: "Týden v Home Assistant: říjnová beta a nový název Cloud"
description: "Přehled za 30. září až 6. října 2026: připravované změny Home Assistant, integrace, hardware a stav ESPHome."
cas: "4 minuty"
obtiznost: "Přehled"
kontrola_zdroju: "2026-10-07"
stav: "Ověřeno podle oficiálních zdrojů"
temata: [Home Assistant, Novinky, Integrace, Hardware, ESPHome]
obrazek: "/assets/images/novinky-2026-10-07.png"
obrazek_alt: "Ilustrace chytrého domu propojeného s mapou, senzorem a vzdáleným přístupem"
---
## Týden ve znamení příprav

Co se dělo kolem Home Assistant od 30. září do 6. října 2026? Do popředí se dostaly přípravy říjnové verze a oznámení nového názvu služby Home Assistant Cloud. U hardwaru a ESPHome oddělujeme novinky od starších zpráv, aby přehled nebudil dojem, že každá zmíněná věc vyšla právě tento týden.

## Home Assistant 2026.10: zatím beta

Na GitHubu je dostupné vydání 2026.10.0b0. Oficiální říjnové poznámky při uzávěrce tohoto přehledu stále nesou označení Beta a upozorňují, že se mohou měnit. Následující body proto berte jako představení připravovaných funkcí.

V poznámkách je přepracovaná mapa: ostřejší zobrazení při přiblížení, přehlednější značky osob a zón a společný přehled lidí, zařízení a zón. Upravený profil seskupuje nastavení vzhledu, jazyka a zabezpečení. Smyslem těchto změn je usnadnit každodenní orientaci.

## Integrace a zařízení: co sledovat

Říjnové poznámky zmiňují rozšíření Matter o ovládání zvukového a světelného alarmu podporovaných senzorů úniku vody. U Philips Hue uvádějí ovládání zón MotionAware a výběr scén. Jsou to změny podpory zařízení v softwaru, nikoli oznámení nového senzoru nebo nové žárovky.

Před nákupem se vyplatí ověřit přesný model i potřebnou verzi Home Assistant. Samotná přítomnost značky v seznamu integrací ještě neříká, které funkce vaše zařízení nabídne. U bety navíc počítejte s tím, že konečný rozsah podpory se může změnit.

## Cloud dostane název Home Assistant Link

Nabu Casa 2. října oznámila přejmenování služby Home Assistant Cloud na **Home Assistant Link**. Podle oznámení poskytovatele má změna v Home Assistant proběhnout 2. prosince 2026 s verzí 2026.12. Předplatitelé kvůli názvu nemusí nic nastavovat; jde o stejné předplatné.

Nový název má lépe vystihovat propojení domácí instalace s volitelnými online službami. Home Assistant nadále běží doma. Link není přesun celé instalace na vzdálený server a předplatné není podmínkou pro používání Home Assistant. Tuto podstatu shodně vysvětlují oznámení Home Assistant i Nabu Casa.

## ESPHome: nepleťme si datum novinky

Oficiální web ESPHome při kontrole uvádí verzi 2026.9.1. Ta vyšla už 29. září, tedy těsně před sledovaným týdnem. Zářijová řada přinesla práci na rychlejším sestavování a šifrovaných bezdrátových aktualizacích; nejde o nové říjnové vydání.

Pro domácí senzory je praktické sledovat zvlášť verzi ESPHome a verzi Home Assistant. Aktualizace jedné aplikace sama o sobě nepřehraje firmware všech čidel. Nové možnosti z připravovaných poznámek HA také nemusí být dostupné ve stávajícím firmwaru. V tomto přehledu je proto nepředkládáme jako hotový návod k zapnutí.

## Co z toho využít doma

Pokud domácnost spolehlivě funguje, není nutné instalovat betu jen kvůli novinkám. Projděte poznámky ke stabilní verzi, až bude dostupná, a před aktualizací připravte zálohu. U názvu Link zatím stačí vědět, že jde o oznámenou prosincovou změnu. Hardware vybírejte podle konkrétní potřeby a doložené podpory, nikoli podle počtu novinek v týdnu.

## Zdroje

- [Home Assistant 2026.10 – beta poznámky](https://rc.home-assistant.io/blog/2026/09/30/release-202610/)
- [Home Assistant Core 2026.10.0b0 na GitHubu](https://github.com/home-assistant/core/releases/tag/2026.10.0b0)
- [Home Assistant – oznámení Home Assistant Link](https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours)
- [Nabu Casa – Cloud becomes Link](https://www.nabucasa.com/news/2026-10-02-cloud-becomes-link/)
- [ESPHome 2026.9 – přehled a opravné vydání](https://esphome.io/blog/2026/09/16/esphome-2026-9/)
- [ESPHome – seznam změn 2026.9](https://esphome.io/changelog/2026.9.0/)
