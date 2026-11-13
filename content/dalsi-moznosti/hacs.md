---
title: "HACS: instalace a editor konfigurace"
description: "Jak nainstalovat HACS, přidat komunitní rozšíření a používat editor Studio Code Server."
obrazek: "/assets/images/hacs-instalace-nastroje.png"
obrazek_alt: "Ilustrace rozšíření chytré domácnosti a editoru konfigurace."
cas: "6 minut čtení"
obtiznost: "Další krok"
kontrola_zdroju: "2026-10-06"
stav: "Podle dokumentace"
temata:
  - "HACS"
  - "Komunitní integrace"
  - "Aplikace"
  - "Studio Code Server"
---

## HACS a aplikace nejsou totéž
**HACS** (Home Assistant Community Store) spravuje komunitní integrace, karty přehledů a další rozšíření. Použijte ho, když standardní Home Assistant požadovanou funkci nemá. Nejde o oficiální obchod HA a dostupnost projektu není zárukou jeho kvality.

**Aplikace** běží jako samostatné služby v Home Assistant OS. Patří sem například editor Studio Code Server. HACS je neinstaluje. Ve starším rozhraní se aplikace nazývají doplňky. Následující postupy jsou pro **HA OS**; instalace Container nemá tento obchod.

## Před instalací
Vytvořte zálohu v **Nastavení → Systém → Zálohy**. Připravte si účet GitHub. U každého rozšíření čtěte požadavky, návod, historii aktualizací a hlášené problémy. Komunitní integrace spouštějí cizí kód uvnitř HA, proto vybírejte projekty, kterým důvěřujete.

## 1. Stáhněte HACS v HA OS
1. Otevřete **Nastavení → Aplikace → Obchod s aplikacemi**.
2. V nabídce tří teček otevřete **Repozitáře** a přidejte `https://github.com/hacs/addons`.
3. Vyhledejte **Get HACS**, zvolte instalaci a aplikaci spusťte.
4. Otevřete její **Protokoly** a postupujte podle zpráv o dokončení. Get HACS pouze stáhne potřebné soubory.
5. Restartujte **Home Assistant**; pouhý restart aplikace nestačí.

Pro Container použijte jinou větev [oficiálního návodu HACS](https://www.hacs.xyz/docs/use/download/download/). Nekopírujte do něj postup pro obchod HA OS.

## 2. Dokončete nastavení HACS
V **Nastavení → Zařízení a služby → Přidat integraci** vyhledejte **HACS**. Pokud chybí, po restartu obnovte prohlížeč bez mezipaměti. Potvrďte uvedené podmínky.

Zkopírujte zobrazený autorizační kód, otevřete `https://github.com/login/device`, přihlaste se, vložte kód a autorizujte HACS. Vraťte se do HA a dokončete průvodce. Kód není váš GitHub přihlašovací údaj.

V HACS otevřete vybraný projekt a stáhněte ho podle jeho návodu. U integrace obvykle následuje restart HA a přidání v **Zařízení a služby**; karta přehledu má jiný postup. Samotné stažení není hotové nastavení. Před aktualizacemi čtěte změny a zachovejte možnost návratu ze zálohy.

## Studio Code Server: editor v prohlížeči
**[Studio Code Server](https://github.com/hassio-addons/app-vscode)** umožní upravovat konfiguraci HA z prohlížeče. Nabízí zvýraznění YAML a práci se soubory; není nutný pro běžné automatizace vytvářené klikáním.

V obchodě aplikací vyhledejte **Studio Code Server**. Pokud chybí komunitní nabídka, přidejte repozitář `https://github.com/hassio-addons/repository`. Aplikaci nainstalujte, spusťte a otevřete její webové rozhraní. Zapněte případně spouštění při startu a postranní panel.

Před úpravou souboru si uložte původní verzi. U změn `configuration.yaml` zkontrolujte konfiguraci před restartem. Zvýraznění v editoru samo nepotvrzuje funkčnost nastavení.

## Zdroje
- [HACS: stažení a instalace](https://www.hacs.xyz/docs/use/download/download/)
- [HACS: nastavení a autorizace](https://www.hacs.xyz/docs/use/configuration/basic/)
- [Home Assistant: aplikace a repozitáře v HA OS](https://www.home-assistant.io/common-tasks/os/)
- [Studio Code Server: projekt](https://github.com/hassio-addons/app-vscode)
- [Studio Code Server: instalace a použití](https://github.com/hassio-addons/app-vscode/blob/main/vscode/DOCS.md)
