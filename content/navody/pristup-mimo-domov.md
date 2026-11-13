---
title: "Jak ovládat domácnost mimo domov"
description: "Zapněte vzdálený přístup přes Home Assistant Cloud, ověřte připojení a zabezpečte svůj účet."
cas: "20 minut"
obtiznost: "Snadné"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - vzdálený přístup
  - Home Assistant Cloud
  - zabezpečení
---

Chcete cestou z práce zkontrolovat teplotu nebo zjistit, zda zůstalo rozsvíceno? Home Assistant je ve výchozím nastavení dostupný v domácí síti. Pro připojení odjinud potřebuje další způsob přístupu. Samotná instalace mobilní aplikace nestačí.

## Kterou cestu zvolit

Pro začátečníka je nejsnazší **Home Assistant Cloud** od Nabu Casa, poskytovatele se sídlem v USA. Jde o placenou službu, která zprostředkuje šifrované spojení bez otevírání portů na routeru. Předplatné také podporuje vývoj Home Assistant. Aktuální cenu si ověřte na webu poskytovatele.

Alternativou je **VPN**, tedy zabezpečené spojení do domácí sítě. Vyžaduje vlastní nastavení a před přístupem musí být připojená. Pokud už VPN používáte a spravujete, může vám stačit. Ruční zpřístupnění přes router vyžaduje více znalostí sítí a zabezpečení; pro první připojení zvolte jednodušší cestu.

## Zapnutí Home Assistant Cloud

Postup proveďte nejprve doma, když máte běžný přístup do Home Assistant. Potřebujete běžící systém, internetové připojení a účet Home Assistant Cloud. Toto nastavení provedete v rozhraní, YAML není potřeba.

1. Otevřete **Nastavení → Home Assistant Cloud** a přihlaste se k účtu služby. Pokud účet nemáte, založte jej a projděte nabízenými podmínkami předplatného.
2. V části **Vzdálený přístup** (Remote access) zapněte přepínač. Při prvním přihlášení může příprava trvat několik minut. Vytvoření a ověření certifikátu po zapnutí může trvat až minutu.
3. Zobrazenou vzdálenou adresu si uložte. Právě přes ni se připojíte mimo domácí síť. K přihlášení do samotného Home Assistant použijete svůj účet v Home Assistant.
4. Na telefonu vypněte Wi-Fi a zapněte mobilní data. V prohlížeči otevřete uloženou adresu. Tím ověříte, že přístup funguje i mimo domácí síť.
5. Zkontrolujte aktuální teplotu nebo stav světla. Pro první zkoušku vyberte činnost, jejíž výsledek můžete snadno ověřit.

## Zabezpečte přihlášení

Šifrované spojení chrání přenos dat, ale účet stále potřebuje silné, jedinečné heslo. V uživatelském profilu Home Assistant otevřete záložku **Zabezpečení** a zapněte dvoufaktorové ověřování pomocí autentizační aplikace. Naskenujte QR kód a potvrďte nastavení aktuálním kódem. Toto ověření nastavte pro každý účet, který vzdálený přístup používá. Home Assistant také pravidelně aktualizujte.

## Když spojení nefunguje

Nejprve zkontrolujte, zda je v Home Assistant Cloud vzdálený přístup zapnutý a zda otevíráte správnou adresu. Pokud doma vypadne internet nebo se vypne počítač s Home Assistant, tato cesta nebude dostupná. Cloud nenahrazuje domácí server.

Při vypnutém vzdáleném přístupu jej nelze automaticky zapnout odkudkoli: vzdálená aktivace vyžaduje předem povolenou volbu **Allow external activation of remote access**. Pro první nastavení proto zůstaňte v domácí síti.

Lokální automatizace mohou při výpadku internetu dál běžet, pokud mají potřebná zařízení dostupná doma. Podrobnosti najdete v článku [Co bude fungovat, když vypadne internet?](/pomoc/vypadek-internetu/).

## Zdroje

- [Home Assistant: vzdálený přístup](https://www.home-assistant.io/docs/configuration/remote/)
- [Nabu Casa: zapnutí vzdáleného přístupu](https://support.nabucasa.com/hc/en-us/articles/26474279202973-Enabling-remote-access-to-Home-Assistant)
- [Nabu Casa: zabezpečení vzdáleného přístupu](https://support.nabucasa.com/hc/en-us/articles/26508882007581-Remote-access-Security-aspects)
- [Home Assistant: dvoufaktorové ověřování](https://www.home-assistant.io/docs/authentication/multi-factor-auth/)
- [Nabu Casa: informace o soukromí a poskytovateli](https://www.nabucasa.com/privacy/)
