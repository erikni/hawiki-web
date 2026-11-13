---
title: "Tesla a Home Assistant: TeslaMate, automatizace a BLE ovládání"
description: "Instalace TeslaMate, příklady automatizací a Bluetooth ovládání přes Teslemetry od Home Assistantu 2026.10."
obrazek: "/assets/images/tesla-teslamate.png"
obrazek_alt: "Ilustrace elektromobilu propojeného s domácím serverem a přehledem baterie a nabíjení."
cas: "15 minut čtení"
obtiznost: "Pokročilé"
kontrola_zdroju: "2026-10-14"
stav: "Podle dokumentace"
temata:
  - "Tesla"
  - "TeslaMate"
  - "MQTT"
  - "Automatizace"
  - "Teslemetry"
  - "Bluetooth"
---

## Co TeslaMate přinese do chytré domácnosti
**TeslaMate** je komunitní otevřený projekt pro záznam údajů z Tesly. Uchovává historii jízd a nabíjení ve vlastní databázi. Přehledy v Grafaně pomohou sledovat spotřebu, nabíjecí relace i chování auta v čase. Do Home Assistantu předává údaje přes **MQTT**: službu, která doručuje zprávy mezi aplikacemi.

Na přehledu HA tak můžete mít baterii, odhad dojezdu, stav nabíjení, připojení kabelu, polohu, teplotu nebo otevřená okna. Dostupnost závisí na údajích, které poskytne vaše auto. Z těchto hodnot vytvoříte oznámení nebo reakci domácnosti, například rozsvícení příjezdu. Grafana slouží pro podrobnější historii, HA pro společný přehled a automatizace.

**Vlastní databáze neznamená získávání dat bez internetu.** TeslaMate komunikuje se službami Tesly. Přes MQTT poskytuje údaje ke čtení; samo tímto propojením nezapne klimatizaci, nezmění nabíjecí proud ani neodemkne auto. Pro takové příkazy potřebujete další cestu, například Tesla Fleet, Teslemetry nebo ovladatelný wallbox.

## Kterou cestu vybrat
| Řešení | Co získáte | Co potřebujete |
| --- | --- | --- |
| TeslaMate + MQTT | Vlastní historii a údaje pro automatizace | Server, Docker, MQTT a internet |
| Tesla Fleet | Cloudové sledování a ovládání auta | Tesla účet, vývojářskou aplikaci, veřejný klíč a nastavení API |
| Teslemetry s BLE od HA 2026.10 | Podporované příkazy místně přes Bluetooth, cloud jako zálohu | Předplatné, Bluetooth v dosahu auta a spárovaný klíč |

TeslaMate může zůstat zdrojem historie a další integrace obstará ovládání. V HA pak můžete vidět několik entit pro tutéž baterii nebo klimatizaci. Pojmenujte je podle zdroje a v každé automatizaci vyberte konkrétní entitu. Pro začátek doporučujeme zprovoznit čtení údajů a první oznámení; ovládání přidat až potom.

## Co připravit pro TeslaMate
Potřebujete trvale zapnutý počítač nebo NAS s Dockerem a Docker Compose, účet Tesla a internet. Dokumentace uvádí nejméně 1 GB RAM, doporučuje 2 GB. Podporuje 64bitové platformy amd64 a aarch64; stará 32bitová instalace Raspberry Pi nestačí. Postup níže instaluje samostatné kontejnery vedle HA, nikoli aplikaci přímo do HA OS.

Nejprve připravte **MQTT broker**. V HA OS lze použít aplikaci Mosquitto broker a samostatného uživatele pro TeslaMate. V Nastavení → Zařízení a služby nastavte integraci MQTT. U jiné instalace HA použijte vlastní broker. Home Assistant i TeslaMate se musí připojovat ke stejnému brokeru; dva oddělené brokery si zprávy automaticky nepředají.

## Instalace v Dockeru
Následující konfigurace vychází z Docker návodu TeslaMate a používá už připravený broker HA. Proto neobsahuje druhé Mosquitto. Předpokládá novou instalaci databáze; existující databázi nepřepínejte na jinou hlavní verzi PostgreSQL bez migračního postupu.

Na serveru vytvořte složku `teslamate`. Do souboru `.env` v této složce vložte:

```dotenv
TM_DB_PASSWORD=NAHRADTE_SILNYM_HESLEM
TM_ENCRYPTION_KEY=NAHRADTE_DLOUHYM_NAHODNYM_KLICEM
TM_MQTT_HOST=192.168.1.10
TM_MQTT_USER=teslamate
TM_MQTT_PASSWORD=NAHRADTE_HESLEM_MQTT_UZIVATELE
```

Nahraďte všechny zástupné hodnoty. IP adresu změňte na adresu brokeru dostupnou ze serveru s Dockerem, jméno a heslo na jeho uživatele. Pro databázi a šifrování použijte různé dlouhé náhodné hodnoty, například ze správce hesel. `.env` obsahuje tajné údaje: nezveřejňujte jej a uložte si bezpečně kopii šifrovacího klíče.

Vedle vytvořte `docker-compose.yml` s celým obsahem:

```yaml
services:
  teslamate:
    image: teslamate/teslamate:4.3.0
    restart: unless-stopped
    environment:
      ENCRYPTION_KEY: ${TM_ENCRYPTION_KEY}
      DATABASE_USER: teslamate
      DATABASE_PASS: ${TM_DB_PASSWORD}
      DATABASE_NAME: teslamate
      DATABASE_HOST: database
      MQTT_HOST: ${TM_MQTT_HOST}
      MQTT_USERNAME: ${TM_MQTT_USER}
      MQTT_PASSWORD: ${TM_MQTT_PASSWORD}
      MQTT_HOME_ASSISTANT_DISCOVERY: "true"
      TZ: Europe/Prague
    ports:
      - "4000:4000"
    volumes:
      - ./import:/opt/app/import
    cap_drop:
      - ALL
  database:
    image: postgres:18-trixie
    restart: unless-stopped
    environment:
      POSTGRES_USER: teslamate
      POSTGRES_PASSWORD: ${TM_DB_PASSWORD}
      POSTGRES_DB: teslamate
    volumes:
      - teslamate-db:/var/lib/postgresql
  grafana:
    image: teslamate/grafana:4.3.0
    restart: unless-stopped
    environment:
      DATABASE_USER: teslamate
      DATABASE_PASS: ${TM_DB_PASSWORD}
      DATABASE_NAME: teslamate
      DATABASE_HOST: database
    ports:
      - "3000:3000"
    volumes:
      - teslamate-grafana:/var/lib/grafana
volumes:
  teslamate-db:
  teslamate-grafana:
```

Ve složce spusťte `docker compose config` pro kontrolu konfigurace a potom `docker compose up -d`. První příkaz může vypsat hesla, proto jeho výstup nesdílejte. Uvedený příklad počítá s běžným MQTT portem 1883 v důvěryhodné domácí síti. Pro spojení přes nedůvěryhodnou síť nastavte TLS podle dokumentace brokeru a proměnných TeslaMate.

Na `http://IP_SERVERU:4000` otevřete TeslaMate. Podle jeho návodu na tokeny získáte přístupový a obnovovací token a vložíte je na přihlašovací stránku. Jsou to přístupové údaje k účtu; nedávejte je do článků, screenshotů ani veřejných konfigurací. V Grafaně na `http://IP_SERVERU:3000` použijte první přihlášení `admin` / `admin` a heslo změňte. Nastavte adresy aplikace a grafů v TeslaMate. Porty 3000 a 4000 nevystavujte přímo do internetu.

## Připojení do HA a první kontrola
Proměnná `MQTT_HOME_ASSISTANT_DISCOVERY` zapíná automatické vytvoření entit přes MQTT discovery. Po prvních údajích z auta by se v integraci MQTT mělo objevit zařízení TeslaMate a jeho entity. Nemusíte přidávat další integraci nazvanou TeslaMate ani instalovat HACS. U více aut ověřte, ke kterému vozidlu každá entita patří.

V detailu zařízení zkontrolujte baterii a nabíjení proti aplikaci Tesla. Poznamenejte si skutečná ID entit. Starší instalace mohou používat ruční `mqtt_sensors.yaml`; neponechávejte ruční definice stejných entit současně s discovery. Při přechodu ze starších vydání si přečtěte poznámky k aktualizaci: zachování úprav názvů a nastavení entit nemusí být automatické.

Když data chybí, zkontrolujte `docker compose ps` a `docker compose logs --tail=50 teslamate`, IP brokeru a přihlášení. V MQTT integraci můžete poslouchat téma `teslamate/cars/1/#`; číslo 1 nahraďte ID auta, pokud je jiné. Když zprávy přicházejí, ale entity chybí, prověřte discovery a jeho prefix. Výpisy před sdílením zkontrolujte kvůli poloze a dalším osobním údajům.

## Co je nové od Home Assistantu 2026.10: BLE ovládání
Vydání **2026.10** přidalo do integrace **Teslemetry** místní ovládání vozidla přes Bluetooth Low Energy, zkráceně BLE. Není to nová funkce TeslaMate ani automatické rozšíření Tesla Fleet. Teslemetry nadále vyžaduje účet s aktivním předplatným. Nová místní cesta dává smysl zejména pro auto zaparkované doma, například v garáži se slabým mobilním signálem.

Příkaz se u spárovaného auta v dosahu pokusí projít přes Bluetooth. Když místní spojení není dostupné nebo příkaz nedokončí, integrace použije cloud. Mimo domov tedy může stejná automatizace dál využívat cloudové ovládání. Podpora zahrnuje například klimatizaci, nabíjení, nabíjecí proud či limit a zámek podle dostupných entit vozidla.

**Stavy se v této integraci dál čtou přes cloud nebo datový stream Teslemetry.** BLE zde slouží k odesílání příkazů. Úspěšně odeslaný místní příkaz proto nemusí při výpadku internetu hned přinést aktualizovaný stav v HA. Nejde o náhradu TeslaMate ani o záruku plně offline přehledu auta.

## Bluetooth hardware a párování
Home Assistant musí mít dostupný Bluetooth adaptér nebo **Bluetooth proxy** v dosahu auta. Proxy je malý uzel, například s ESPHome, který přes domácí síť zprostředkuje Bluetooth u garáže. Nestačí pouze přijímat vysílané údaje: potřebuje podporu aktivních BLE spojení. U ESPHome zkontrolujte podporovanou platformu a nastavení `bluetooth_proxy`; aktivní spojení jsou odlišná od aktivního skenování.

Dosah ověřte na skutečném parkovacím místě, i se zavřenými vraty. Nepočítejte s pevně zaručenou vzdáleností. Auto musí podporovat protokol příkazů Tesly; některé Model S a X před rokem 2021 se pro tuto cestu nenabízejí. Připravte také autorizovanou klíčovou kartu auta.

1. Aktualizujte HA na opravené vydání řady 2026.10.x a ověřte funkční Bluetooth integraci.
2. Přidejte **Teslemetry** v Nastavení → Zařízení a služby, přihlaste účet a dokončete jeho běžné nastavení včetně potřebného virtuálního klíče.
3. V integraci vyberte **Add local vehicle** neboli přidání místního vozidla a zvolte auto.
4. Nechte HA vyhledat vůz v dosahu. Omezte další současná telefonní Bluetooth spojení; při párování nemají být poblíž tři nebo více telefonních klíčů.
5. Když průvodce požádá o autorizaci klíče HA, potvrďte krok a přiložte kartu na čtečku ve středové konzoli přibližně do 30 sekund. Při vypršení času krok zopakujte.
6. Vyzkoušejte jednoduchý příkaz, například bliknutí světly, a až poté přidejte automatizaci.

Klíč pro Bluetooth v HA je další oprávnění v autě. Odstranění párování nebo integrace z HA samo tento klíč z vozidla neodebere. Při úplném zrušení přístupu jej odstraňte také na displeji auta v **Controls → Locks**, tedy v seznamu klíčů, a potvrďte autorizovanou kartou podle výzvy.

## Příklad 1: oznámení o dokončení nabíjení
V nové automatizaci otevřete **Upravit v YAML** a vložte celý příklad. `sensor.tesla_charging_state` nahraďte ID MQTT senzoru z TeslaMate. V nástrojích pro vývojáře ověřte, že jeho skutečné hodnoty jsou `Charging` a `Complete`. Zpráva se objeví v oznámeních HA; pro telefon byste místo ní použili svou službu mobilních oznámení.

```yaml
alias: Tesla – nabíjení dokončeno
triggers:
  - trigger: state
    entity_id: sensor.tesla_charging_state
    from: "Charging"
    to: "Complete"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: "Tesla"
      message: "Nabíjení dosáhlo nastaveného limitu."
mode: single
```

Příklad reaguje na konkrétní přechod stavů. Pouhé připojení kabelu ani obnova hodnot po restartu jej nespustí. Pokud přenos přeskočí stav `Charging`, oznámení nepřijde; jde o jednoduchý výchozí příklad, nikoli dohled nad každou nabíjecí relací.

## Příklad 2: ranní klimatizace přes Teslemetry
Předpokladem je funkční Teslemetry, spárované BLE a její ovladatelná klimatizace. V další nové automatizaci vložte celý YAML. Nahraďte obě ID: polohovou entitu z TeslaMate a klimatizaci z Teslemetry. Čas upravte podle odjezdu. Příklad ve všední dny zapne klimatizaci pouze tehdy, když polohová entita hlásí `home`.

```yaml
alias: Tesla – příprava před ranním odjezdem
triggers:
  - trigger: time
    at: "07:15:00"
conditions:
  - condition: time
    weekday: [mon, tue, wed, thu, fri]
  - condition: state
    entity_id: device_tracker.tesla_location
    state: "home"
actions:
  - action: climate.turn_on
    target:
      entity_id: climate.tesla_teslemetry
mode: single
```

Volání entity samo nevynucuje výhradně BLE. Dostupnou cestu vybere Teslemetry a může přejít na cloud. Poloha z TeslaMate také může být stará; pro spolehlivější provoz doplňte ověření přítomnosti auta a vlastní pravidla pro stav baterie. Časová automatizace nepozná, že jste si ráno odjezd rozmysleli.

## Další užitečné automatizace
**Nabíjení z fotovoltaiky:** spojte skutečný přebytek měřený u přípojky se stavem baterie a připojením kabelu. Samotný výkon panelů není přebytek, protože část spotřebuje dům. Příkazy obstará ovladatelný wallbox nebo integrace auta, například Teslemetry s BLE. Nastavte minimální a maximální proud podle zařízení, prodlevu a odlišné hranice pro zapnutí a vypnutí, aby nabíjení nekmitalo při každém mraku.

**Příjezd domů:** poloha auta může rozsvítit příjezd pouze po setmění. Pro světlo je zpoždění obvykle snesitelnější než pro vrata. Automatické odemykání domu neopírejte jen o polohu nebo zachycení Bluetooth; obě informace mohou být opožděné či nedostupné.

**Zapomenutý kabel a okna:** večer zkontrolujte, zda je auto doma, baterie pod vaším prahem a kabel odpojený. Nebo spojte údaj o otevřených oknech s deštěm. Začněte oznámením; zavírání či jiné ovládání doplňte až s ověřenou podporou a podmínkami konkrétního auta.

## Provoz, zálohy a řešení potíží
TeslaMate počítá s uspáváním auta. Při spánku nebo přerušení spojení mohou hodnoty zůstat poslední známé; `unknown` a `unavailable` nejsou nulová baterie ani potvrzení, že je vůz doma. Více současně používaných aplikací může ovlivnit uspávání. Nezapínejte časté probouzení jen kvůli čerstvějšímu číslu na přehledu.

U BLE potíží začněte dosahem, funkční proxy a volnými spojeními. Pokud není auto v nabídce, ověřte kompatibilitu a zda už není přidané. U neúspěšné autorizace zopakujte přiložení karty podle průvodce. Opravy řady 2026.10.x řeší i párování a vyhledávání; před složitými zásahy zkontrolujte changelog.

Záloha HA sama automaticky nezálohuje databázi na samostatném Docker serveru. Zálohujte PostgreSQL postupem TeslaMate, konfiguraci a šifrovací klíč. Docker volumes uchovávají data mezi běžnými restarty, ale nejsou záloha. Před aktualizací si přečtěte poznámky k vydání a u databáze vždy oddělte aktualizaci aplikace od migrace hlavní verze PostgreSQL.

## Zdroje
- [TeslaMate: instalace v Dockeru](https://docs.teslamate.org/docs/installation/docker/)
- [TeslaMate: propojení s Home Assistantem](https://docs.teslamate.org/docs/integrations/home_assistant/)
- [TeslaMate: proměnné prostředí](https://docs.teslamate.org/docs/configuration/environment_variables/)
- [TeslaMate: MQTT údaje](https://docs.teslamate.org/docs/integrations/mqtt/)
- [Home Assistant: MQTT](https://www.home-assistant.io/integrations/mqtt/)
- [Home Assistant: Tesla Fleet](https://www.home-assistant.io/integrations/tesla_fleet/)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant 2026.10: novinky](https://www.home-assistant.io/blog/2026/10/07/release-202610/)
- [Home Assistant: Teslemetry a Bluetooth ovládání](https://www.home-assistant.io/integrations/teslemetry/)
- [Home Assistant: párování Teslemetry ve verzi 2026.10.1](https://github.com/home-assistant/core/blob/2026.10.1/homeassistant/components/teslemetry/config_flow.py)
- [Home Assistant: Bluetooth](https://www.home-assistant.io/integrations/bluetooth/)
- [ESPHome: Bluetooth proxy](https://esphome.io/components/bluetooth_proxy/)
- [Home Assistant: ovládání klimatizace](https://www.home-assistant.io/integrations/climate/)
- [Home Assistant: oznámení](https://www.home-assistant.io/integrations/persistent_notification/)
- [Home Assistant 2026.10: changelog](https://www.home-assistant.io/changelogs/core-2026.10)
- [TeslaMate: verze 4.3.0](https://github.com/teslamate-org/teslamate/releases/tag/v4.3.0)
- [TeslaMate: přehledy v Grafaně](https://docs.teslamate.org/docs/screenshots/)
- [TeslaMate: uspávání a časté otázky](https://docs.teslamate.org/docs/faq/)
- [TeslaMate: zálohy databáze](https://docs.teslamate.org/docs/maintenance/backup/)
