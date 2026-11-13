---
title: "Google Kalendář v Home Assistantu: OAuth, více kalendářů a upozornění"
seoTitle: "Google Kalendář a Home Assistant: OAuth a automatizace"
description: "Praktický český návod na Google Kalendář v Home Assistantu: OAuth, více kalendářů, upozornění 15 minut před událostí a řešení chyb."
cas: "15 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-11-12"
stav: "Podle dokumentace"
sourceType: "official-docs"
obrazek: "/assets/images/google-calendar-home-assistant.png"
obrazek_alt: "Kalendář propojený bezpečným OAuth přístupem s oznámením a chytrou domácností"
temata:
  - Google Kalendář
  - Integrace
  - OAuth
  - Automatizace
  - Upozornění
related:
  - zaciname/zarizeni-entita-integrace
  - pomoc/automatizace-nefunguje
  - pomoc/vypadek-internetu
---

Integrace **Google Calendar** propojí Google Kalendář s Home Assistantem. Každý kalendář z části „Moje kalendáře“ může získat vlastní entitu, například `calendar.rodina`. Události pak uvidíte v přehledu Kalendář a můžete podle jejich začátku nebo konce spouštět automatizace – třeba poslat upozornění 15 minut před schůzkou nebo připravit dům na pravidelnou událost.

Jde o oficiální integraci, nikoli HACS doplněk. Pokud nechcete kalendářní data odesílat ke Googlu, použijte místní kalendář Home Assistantu.

## Jak propojení funguje

Home Assistant se přes internet dotazuje služby Google Calendar API. Přístup schválíte pomocí **OAuth 2.0**: Home Assistant nezná heslo k účtu, ale dostane token pro čtení, případně zápis do kalendářů.

Integrace je cloudová. Home Assistant potřebuje internet a výpadek Google API, DNS nebo připojení může aktualizaci pozdržet. Název, čas, popis a místo události se mohou použít v automatizaci, proto do kalendáře nevkládejte údaje, které nechcete mít současně u Googlu i v Home Assistantu.

## Co budete potřebovat

- účet Google s alespoň jedním kalendářem v části **Moje kalendáře**,
- Home Assistant s funkčním internetovým připojením,
- přístup do Google Cloud Console,
- projekt v Google Cloud se zapnutým **Google Calendar API**,
- OAuth klient typu **Web application** a jeho Client ID a Client Secret,
- správně nastavené časové pásmo v Google Kalendáři i v Home Assistantu.

Není potřeba zvláštní hardware. Firemní či školní Google Workspace může přístup k API omezit; pak požádejte správce nebo použijte jiný účet.

## 1. Vytvoření OAuth údajů u Googlu

Home Assistant nyní doporučuje webové OAuth údaje. Nevytvářejte klienta typu Desktop ani starší Device Authorization.

1. V [Google Cloud Console](https://console.cloud.google.com/) vytvořte nebo vyberte projekt určený pro Home Assistant.
2. Otevřete **Google Calendar API** a zvolte **Enable**.
3. V části **Google Auth Platform → Branding** spusťte nastavení. Jako název aplikace můžete uvést „Home Assistant“ a doplňte svůj kontaktní e-mail.
4. Jako typ publika vyberte **External**. Na stránce Branding nastavte pro domovskou stránku, zásady ochrany soukromí a podmínky adresu `https://home-assistant.io` a mezi autorizované domény přidejte `home-assistant.io`.
5. V části **Audience** změňte stav aplikace na produkční. V režimu Testing přidejte účet jako testovacího uživatele, ale token obvykle vyprší po sedmi dnech.
6. V části **Clients** vytvořte klienta typu **Web application**.
7. Do **Authorized redirect URIs** vložte přesně `https://my.home-assistant.io/redirect/oauth`. Nejde o zástupný text ani adresu vašeho serveru.
8. Uložte si zobrazené **Client ID** a **Client Secret** do správce hesel. Secret nevkládejte do článků, snímků obrazovky ani veřejného repozitáře.

Nové údaje mohou začít fungovat až po několika hodinách. Produkční stav osobního klienta je důležitý hlavně kvůli sedmidennímu vypršení testovacího tokenu.

## 2. Přidání integrace v Home Assistantu

1. Otevřete **Nastavení → Zařízení a služby**.
2. Zvolte **Přidat integraci** a vyhledejte **Google Calendar**.
3. Když vás Home Assistant vyzve, vložte Client ID a Client Secret. Ukládejte je pouze do rozhraní své instalace.
4. Vyberte správný Google účet a projděte souhlasem OAuth. U osobní aplikace může Google zobrazit varování; pokračujte jen u projektu, který jste vytvořili.
5. Na stránce **Link account to Home Assistant?** zkontrolujte uvedenou adresu své instance a propojení potvrďte.
6. Po návratu do Home Assistantu otevřete integraci a ověřte vytvořené entity kalendářů.

Integrace se přidává v UI. Starší `google_calendars.yaml` je pro existující instalace z doby před Home Assistantem 2022.6 a novým uživatelům se nedoporučuje. Události filtrujte podmínkou automatizace.

## Více kalendářů a oprávnění

Každý kalendář z části **Moje kalendáře** dostane samostatnou entitu. „Rodina“ může být `calendar.rodina`, ale skutečné ID ověřte v **Nastavení → Zařízení a služby → Entity**. Nepotřebné entity vypněte. U sdílených kalendářů rozhodují práva přidělená v Googlu.

Pro spouštění automatizací stačí přístup jen pro čtení. Akce `google.create_event` se objeví až s přístupem pro čtení a zápis; změna může vyžadovat novou autorizaci.

Entita ukazuje probíhající a jednu nejbližší událost. Při překryvu proto v automatizaci nepoužívejte její atribut `message`; správnou událost poskytne `trigger.calendar_event`.

## Příklad 1: upozornění 15 minut před událostí

Nejdřív v Home Assistantu zjistěte službu telefonu v **Nástroje pro vývojáře → Akce**. V příkladu nahraďte `notify.mobile_app_muj_telefon` skutečnou akcí a `calendar.rodina` vlastním kalendářem. Celý blok vložte do YAML editoru jedné nové automatizace.

```yaml
alias: Kalendář – upozornění 15 minut předem
triggers:
  - trigger: calendar
    event: start
    entity_id: calendar.rodina
    offset: "-00:15:00"
conditions: []
actions:
  - action: notify.mobile_app_muj_telefon
    data:
      title: "Za 15 minut"
      message: >-
        {{ trigger.calendar_event.summary }}
        {% if trigger.calendar_event.location %}
        – {{ trigger.calendar_event.location }}
        {% endif %}
mode: parallel
max: 10
```

Spouštěč reaguje 15 minut před začátkem každé události ve vybraném kalendáři. Podmínky jsou prázdné, takže upozornění dostanete vždy. Akce použije název a případné místo přímo z události, která trigger vyvolala. Režim `parallel` dovolí zpracovat více událostí se stejným časem začátku; dokumentace kalendáře proto nedoporučuje režim `single`.

Home Assistant načítá kalendáře přibližně každých 15 minut. Testovací událost proto naplánujte alespoň 30 minut dopředu.

Pro více kalendářů přidejte další trigger se stejným offsetem a jiným `entity_id`. Pomocí `trigger.entity_id` poznáte zdrojový kalendář.

## Příklad 2: zapsání dokončeného praní do kalendáře

Tento příklad vyžaduje, aby integrace měla oprávnění pro zápis a aby existoval senzor pračky s hodnotou `finished`. Skutečnou hodnotu ověřte v **Nástroje pro vývojáře → Stavy**. Nahraďte senzor i kalendář a celý blok vložte do YAML editoru nové automatizace.

```yaml
alias: Kalendář – zapsat dokončené praní
triggers:
  - trigger: state
    entity_id: sensor.pracka_stav
    to: "finished"
conditions: []
actions:
  - action: google.create_event
    target:
      entity_id: calendar.domaci_provoz
    data:
      summary: "Pračka doprala"
      start_date_time: "{{ now().strftime('%Y-%m-%d %H:%M:%S') }}"
      end_date_time: >-
        {{ (now() + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S') }}
      description: "Záznam vytvořil Home Assistant."
mode: queued
```

Spouštěč reaguje na stav `finished`. Akce vytvoří minutovou událost jako záznam historie; režim `queued` zachová pořadí souběžných zápisů.

Pokud akci `google.create_event` nevidíte, povolte integraci čtení a zápis. Do rodinného kalendáře zapisujte jen sdílené údaje.

## Co integrace zpřístupní a co neumí

Získáte kalendářní entity, přehled, spouštěče začátku a konce s posunem, data pro šablony a při povoleném zápisu akci pro vytvoření události.

Home Assistant nenahrazuje Google Kalendář. Sdílení, hosty, videohovory a složité opakování řešte u Googlu. Názvy entit se odvozují od vašich kalendářů; příklady nejsou univerzální ID.

Celodenní událost začíná na začátku dne a její konec je reprezentován následujícím dnem. Před ovládáním topení nebo zámku otestujte běžnou i celodenní událost.

## Bezpečnost a soukromí

- Client Secret a OAuth tokeny zálohujte a chraňte stejně jako heslo; neposílejte je do issue ani veřejného repozitáře.
- Povolte jen čtení, pokud nepotřebujete vytvářet události.
- Citlivé názvy, místa a popisy událostí neposílejte bez rozmyslu do mobilních oznámení, hlasových asistentů nebo logů.
- U sdíleného kalendáře počítejte s tím, že událost vytvořenou Home Assistantem uvidí i další členové.

Přístup lze v účtu Google odvolat; změna bezpečnostních nastavení může vyžadovat novou autorizaci.

## Když integrace nefunguje

- **Invalid client nebo redirect URI mismatch:** ověřte webový typ klienta a přesnou adresu `https://my.home-assistant.io/redirect/oauth`, včetně HTTPS a bez vlastní domény.
- **Access blocked:** v režimu Testing přidejte účet mezi testovací uživatele. U Workspace může přístup blokovat správce.
- **Po sedmi dnech je integrace nedostupná:** OAuth aplikace pravděpodobně zůstala v režimu Testing. Přepněte ji do produkčního stavu a účet znovu propojte.
- **Authentication code expired:** spusťte přidání integrace znovu a dokončete celý souhlas bez dlouhé prodlevy.
- **Kalendář chybí:** zkontrolujte, zda je v Googlu v části Moje kalendáře, zda jej vybraný účet vidí a zda jeho entita není vypnutá.
- **Automatizace se nespustila:** testovací událost vytvořte více než 15 minut dopředu, ověřte časové pásmo a otevřete trasování automatizace.
- **Upozornění má jinou událost:** v šabloně používejte `trigger.calendar_event.summary`, ne atribut `message` kalendářní entity.
- **Nelze vytvořit událost:** povolte integraci čtení a zápis a ověřte, že účet smí zapisovat do cílového kalendáře.

Při potížích otevřete **Nastavení → Systém → Protokoly**. Chybné Client ID nebo Secret lze v přihlašovacích údajích aplikací odstranit a zadat znovu. Před smazáním integrace si poznamenejte názvy entit.

## Výhody, nevýhody a alternativy

Výhodou je propojení rodinného plánu s domácností, samostatné entity více kalendářů a triggery pro překrývající se události.

Nevýhodou je složitější první nastavení v Google Cloud, závislost na internetu a předání kalendářních dat cloudové službě. Polling navíc znamená, že událost vytvořená těsně před začátkem nemusí automatizaci včas spustit.

Pro čistě domácí plán bez cloudu použijte **Local Calendar**. Pro veřejný nebo sdílený kalendář jen ke čtení může být vhodný **Remote Calendar**, pokud máte jeho iCalendar URL a nevadí vám omezené možnosti zápisu. Výběr závisí hlavně na tom, kde mají data vznikat a kdo je smí číst.

## Zdroje

- [Home Assistant: integrace Google Calendar](https://www.home-assistant.io/integrations/google/)
- [Home Assistant: kalendářní integrace a automatizace](https://www.home-assistant.io/integrations/calendar/)
- [Home Assistant: spouštěč začátku události](https://www.home-assistant.io/triggers/calendar.event_started/)
- [Home Assistant: akce Create event in Google Calendar](https://www.home-assistant.io/actions/google.create_event/)
- [Google: OAuth 2.0 pro přístup k API](https://developers.google.com/identity/protocols/oauth2)
- [Google Calendar API: OAuth rozsahy](https://developers.google.com/workspace/calendar/api/auth)
