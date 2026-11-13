---
title: "Home Assistant v mobilu: první kroky"
description: "Připojte mobil k domácnosti a vyzkoušejte první ovládání."
cas: "15 minut"
obtiznost: "Začátečník"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - "Mobilní aplikace"
  - "Začínáme"
---

## Co bude na konci fungovat

V telefonu otevřete přehled své domácnosti a vyzkoušíte ovládání připojeného světla. Oficiální aplikace Home Assistant Companion je dostupná pro Android a iPhone. Mobil se propojí s vaším již běžícím Home Assistantem; samotná instalace aplikace domácí systém nenahradí.

## Co budete potřebovat

Připravte si telefon, přihlašovací jméno a heslo k Home Assistantu. Pro první připojení použijte domácí Wi-Fi ve stejné síti jako Home Assistant. Nejdříve ověřte, že jeho přehled otevřete v prohlížeči. Pokud ještě nemáte připojené světlo, můžete si zatím prohlédnout přehled a Nastavení.

## Připojte telefon

1. Na [oficiální stránce mobilní integrace](https://www.home-assistant.io/integrations/mobile_app/) otevřete odkaz do Google Play nebo App Store a nainstalujte aplikaci.
2. Spusťte ji a zvolte připojení k vlastnímu Home Assistantu. Vyberte nalezenou domácnost. Pokud se neobjeví, zadejte ručně adresu, která vám funguje v prohlížeči telefonu.
3. Přihlaste se svým účtem Home Assistantu. Telefon pojmenujte srozumitelně, například **Janův mobil**, abyste jej později poznali při nastavování upozornění.
4. Projděte nabídnutá oprávnění a dokončete průvodce. Názvy voleb se mohou podle jazyka, systému a verze aplikace lišit.

Integrace **Mobile App**, která propojení zajišťuje, je v běžné výchozí konfiguraci zapnutá. Při obvyklé instalaci proto nemusíte kvůli aplikaci upravovat konfigurační soubory.

## Rozumějte oprávněním

Povolte oznámení, pokud chcete později dostávat zprávy z domácnosti. Sdílení polohy pro automatizace je samostatná volba. Oprávnění k poloze ale může aplikace potřebovat i pro rozpoznání domácí Wi-Fi, protože přístup k údajům o síti omezují Android a iOS.

Používáte-li místní adresu začínající `http://`, průvodce nabídne úroveň zabezpečení spojení. Zvolte doporučenou možnost **Most secure** a potvrďte svou domácí síť. Aplikace potom dovolí nešifrované spojení jen v určené síti. Podrobnosti potřebných oprávnění uvádí dokumentace níže.

## Vyzkoušejte výsledek

Otevřete přehled a zapněte připojené světlo. Zkontrolujte skutečnou lampu, potom ji zase vypněte. Aplikaci zavřete a znovu otevřete. Úspěch znamená, že se vrátíte do domácnosti a ovládání stále funguje. Tato kontrola ověřuje připojení doma; doručování upozornění vyzkoušíme v dalším návodu.

## Když se domácnost neotevře

Zkontrolujte Wi-Fi a vyzkoušejte stejnou adresu v prohlížeči telefonu. Hostovská síť může přístup k domácím zařízením blokovat. Pokud aplikace hlásí omezení zabezpečení, ověřte nastavenou domácí síť a oprávnění pro její rozpoznání.

Samotné připojení doma nezajistí ovládání přes mobilní data. Pro přístup mimo domov potřebujete zvlášť nastavený vzdálený přístup, například Home Assistant Cloud nebo VPN. Tomu věnujeme samostatný článek.

## Zdroje

Ověřeno podle dokumentace 1. října 2026; postup nebyl vyzkoušen na fyzickém telefonu.

- [Home Assistant: integrace Mobile App a oficiální aplikace](https://www.home-assistant.io/integrations/mobile_app/)
- [Companion: první připojení a oprávnění](https://companion.home-assistant.io/docs/getting_started/)
- [Companion: zabezpečení místního připojení](https://companion.home-assistant.io/docs/getting_started/connection-security-level/)
- [Home Assistant: vzdálený přístup](https://www.home-assistant.io/docs/configuration/remote/)
