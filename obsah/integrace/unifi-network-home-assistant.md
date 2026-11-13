---
title: "UniFi Network v Home Assistantu: klienti, VLAN a přítomnost"
seoTitle: "UniFi Network a Home Assistant: lokální monitoring a automatizace"
description: "Praktický český návod na propojení UniFi Network s Home Assistantem: místní účet, oprávnění, klienti, AP, VLAN a detekce přítomnosti."
cas: "18 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-11-13"
stav: "Podle dokumentace"
sourceType: "official-docs"
obrazek: "/assets/images/unifi-network-home-assistant.png"
obrazek_alt: "Místní síť s bránou, přepínačem, přístupovými body, dvěma VLAN a dohledem chytré domácnosti"
temata:
  - UniFi Network
  - Integrace
  - Lokální síť
  - VLAN
  - Detekce přítomnosti
related:
  - navody/unifi-access
  - zaciname/zarizeni-entita-integrace
  - pomoc/automatizace-nefunguje
  - pomoc/vypadek-internetu
---

Oficiální integrace **UniFi Network** propojí Home Assistant s aplikací UniFi Network. Umí sledovat přístupové body, switche, brány i připojené klienty. Telefon lze využít pro detekci přítomnosti, u síťových prvků sledovat stav a vytížení a s odpovídajícím oprávněním například vypínat Wi-Fi síť nebo ovládat PoE port.

Jde o jinou integraci než **UniFi Protect** pro kamery a **UniFi Access** pro dveřní systém. HACS není potřeba. Návod je ověřený podle dokumentace, nikoli fyzickým testem konkrétní sestavy.

## Jak propojení funguje

Home Assistant komunikuje přímo s aplikací UniFi Network v místní síti. Změny klientů, zařízení a konfigurace přijímá přes místní WebSocket, tedy průběžně a bez běžného dotazování v intervalu. Při přerušení spojení se pokusí znovu připojit; do té doby mohou být entity nedostupné.

Cloudový účet Ubiquiti SSO pro přihlášení integrace nestačí. V konzoli vytvoříte samostatného **místního uživatele**. Data klientů tak nemusí kvůli Home Assistantu procházet cloudem, vzdálený přístup a jiné služby UniFi ale mohou cloud používat podle vašeho nastavení.

Integrace podporuje UniFi OS konzole i samostatně provozovanou Network Application. Early Access a Release Candidate nejsou podporované.

## Co budete potřebovat

- funkční aplikaci UniFi Network a alespoň jeden spravovaný síťový prvek,
- stabilní verzi UniFi Network a případně UniFi OS,
- místní adresu nebo DNS název řadiče, obvykle port `443`,
- samostatné místní uživatelské jméno a silné heslo pro Home Assistant,
- síťovou cestu z Home Assistantu k řadiči,
- správný čas na obou systémech, ideálně přes NTP.

Home Assistant nemusí být ve stejné VLAN jako telefony ani AP. Musí ale dosáhnout na aplikaci UniFi Network. Integrace pravidla mezi segmenty neobchází a VLAN nevytváří.

## 1. Vytvoření místního účtu

Na UniFi OS konzoli otevřete správu uživatelů **People** a vytvořte nového správce omezeného na místní přístup. Podle aktuální dokumentace Home Assistantu:

1. zvolte **Create New**, doplňte název, uživatelské jméno a heslo,
2. zapněte správní účet a **Restrict to local access only**,
3. vypněte předdefinovanou roli,
4. nastavte oprávnění **Network: Full Management**,
5. pro **OS Settings** ponechte **None**.

Plný přístup k aplikaci Network zpřístupní také ovládací entity. Není však vždy nutný: s omezeným účtem integrace vytvoří méně entit a místo některých přepínačů nabídne jen senzory. Z bezpečnostního hlediska proto nejdřív rozhodněte, zda chcete pouze monitoring, nebo i změny sítě. Nepoužívejte osobní účet vlastníka konzole.

U samostatně provozované Network Application se názvy nabídek mohou lišit. Stále potřebujete místní účet, který se umí přihlásit přímo k dané aplikaci.

## 2. Přidání integrace

1. V Home Assistantu otevřete **Nastavení → Zařízení a služby**.
2. Zvolte **Přidat integraci** a vyhledejte **UniFi Network**.
3. Zadejte místní adresu řadiče, uživatelské jméno, heslo a port. Výchozí port je `443`.
4. Ověřování SSL ponechte zapnuté. Vypínejte je jen u vlastního certifikátu v důvěryhodné místní síti a až po zvážení rizika.
5. Pokud řadič spravuje více sites, vyberte správné **Site ID**.
6. Po dokončení otevřete zařízení a entity integrace a ověřte, co váš účet skutečně zpřístupnil.

Nastavení je celé v rozhraní; integraci nekonfigurujte v `configuration.yaml`.

## Klienti, přístupové body a senzory

V **Nastavení → Zařízení a služby → UniFi Network → Nastavit** můžete určit, co se má sledovat. Důležité volby jsou:

- vytváření `device_tracker` entit pro síťové klienty,
- zahrnutí kabelových klientů,
- sledování UniFi zařízení, například AP a switchů,
- omezení sledování bezdrátových klientů na vybraná SSID,
- doba od posledního výskytu do stavu mimo domov; výchozí je 300 sekund,
- ignorování klientů s náhodnou soukromou MAC adresou,
- výběr konkrétních klientů, pro které mají vzniknout entity,
- volitelné senzory přenosové rychlosti a doby provozu.

Podle zařízení a oprávnění mohou vzniknout senzory stavu, vytížení, teploty, přenosů nebo rychlosti portu a update entity firmwaru. Plná práva mohou přidat restart, PoE power cycle a přepínače portů, Wi-Fi či pravidel provozu. Některé entity jsou ve výchozím stavu vypnuté.

Názvy jako `device_tracker.telefon_anna` nebo `switch.wifi_hoste` jsou pouze příklady. Skutečné ID vždy zjistěte na stránce entity.

## VLAN bez zbytečných problémů

VLAN rozdělují fyzickou síť na oddělené logické segmenty, například domácí, hostovský a IoT. Přenos mezi nimi řídí brána a firewall.

Pro integraci jsou důležité dvě odlišné cesty:

1. Home Assistant se musí připojit k aplikaci UniFi Network.
2. Síťoví klienti a UniFi prvky musí být správně spravované samotným řadičem.

Home Assistant nepotřebuje přímý přístup ke každému IoT klientovi jen kvůli zobrazení v integraci. Je-li řadič v management VLAN, povolte spojení na jeho konkrétní adresu a port, ne celý segment.

SSID lze přiřadit ke konkrétní VLAN. Na trunku mezi switchem a AP musí být povolená; tuto konfiguraci řešte v UniFi Network.

## Příklad 1: světlo při příchodu telefonu

Detekci přítomnosti nejdřív několik dnů sledujte bez kritických akcí. V telefonu pro domácí Wi-Fi vypněte náhodnou MAC adresu nebo nastavte stálou soukromou adresu, aby UniFi zařízení pokaždé poznalo. V Home Assistantu nahraďte tracker a světlo skutečnými entitami. Celý blok vložte do YAML editoru jedné nové automatizace.

```yaml
alias: UniFi – světlo při návratu domů
triggers:
  - trigger: state
    entity_id: device_tracker.telefon_anna
    from: "not_home"
    to: "home"
conditions:
  - condition: state
    entity_id: sun.sun
    state: "below_horizon"
actions:
  - action: light.turn_on
    target:
      entity_id: light.predsin
mode: single
```

Spouštěčem je přechod telefonu do stavu doma. Podmínka dovolí rozsvícení jen po západu slunce. Výpadek telefonu, Wi-Fi nebo řadiče může stav zkreslit, proto samotný síťový tracker nepoužívejte k odemykání dveří ani vypnutí zabezpečení.

## Příklad 2: hostovská Wi-Fi podle času

Tento příklad vyžaduje přepínač WLAN, který se zobrazí jen s odpovídajícím oprávněním účtu. Vypnutí Wi-Fi vyvolá novou konfiguraci dotčených AP a odpojí klienty. Nahraďte `switch.wifi_hoste` skutečnou entitou a celý blok vložte do YAML editoru nové automatizace.

```yaml
alias: UniFi – noční plán hostovské Wi-Fi
triggers:
  - trigger: time
    at: "23:00:00"
    id: noc
  - trigger: time
    at: "07:00:00"
    id: rano
conditions: []
actions:
  - choose:
      - conditions:
          - condition: trigger
            id: noc
        sequence:
          - action: switch.turn_off
            target:
              entity_id: switch.wifi_hoste
      - conditions:
          - condition: trigger
            id: rano
        sequence:
          - action: switch.turn_on
            target:
              entity_id: switch.wifi_hoste
mode: single
```

Dva časové spouštěče mají vlastní ID. Větev `noc` síť vypne a větev `rano` ji znovu zapne. Než plán aktivujete, ověřte, že na daném WLAN nejsou zařízení potřebná přes noc.

## Detekce přítomnosti: nejčastější omezení

Telefon může měnit MAC adresu pro každou Wi-Fi síť. Pak vznikají nové klientské záznamy a původní tracker se nevrátí domů. Nastavení měňte pouze pro vlastní důvěryhodné SSID; globální vypnutí ochrany soukromí není potřeba. Integrace také umí náhodné adresy ignorovat.

Když telefon zůstává doma i po odchodu, zkontrolujte stav klienta přímo v UniFi. Dokumentace upozorňuje, že u některých verzí může odpojení zkreslovat **802.11r Fast Roaming**. Zkontrolujte také shodný čas Home Assistantu a řadiče a vhodně nastavte prodlevu „last seen“. Kratší prodleva reaguje rychleji, ale zvyšuje riziko falešného odchodu při krátkém výpadku Wi-Fi.

Pro důležité automatizace kombinujte síťovou přítomnost s dalším zdrojem. Stav `home` znamená připojený klient, nikoli ověřenou totožnost člověka.

## Když integrace nefunguje

- **Přihlášení je odmítnuto:** použijte místní účet, ne Ubiquiti SSO; ověřte heslo přímým místním přihlášením.
- **Nelze se připojit:** z Home Assistantu ověřte adresu řadiče, port, DNS, firewall a směrování mezi VLAN.
- **Chyba certifikátu:** použijte platný certifikát nebo správně důvěryhodnou interní autoritu. Vypnutí kontroly SSL je až poslední možnost.
- **Chybějí přepínače a tlačítka:** účet nemá potřebná práva nebo je entita ve výchozím stavu vypnutá. Omezený účet často dostane pouze senzory.
- **Klient nemá tracker:** zapněte sledování klientů, zkontrolujte filtr SSID a seznam vybraných klientů. U náhodné MAC nastavte stálou adresu pro domácí síť.
- **Telefon zůstává doma:** porovnejte stav v UniFi, synchronizujte čas, zvažte vypnutí 802.11r a upravte prodlevu.
- **Entity jsou nedostupné:** zkontrolujte stav aplikace Network a WebSocket spojení; integrace se po obnovení pokusí připojit sama.
- **Zůstaly staré entity:** klient nebo zařízení musí být nejprve odstraněné z UniFi a neznámé při startu či znovunačtení integrace; potom lze záznam odstranit v Home Assistantu.

Pro podrobné logování lze do `configuration.yaml` přidat následující blok a Home Assistant restartovat. Použijte jej jen po dobu diagnostiky, protože log může rychle růst.

```yaml
logger:
  default: info
  logs:
    aiounifi: debug
    homeassistant.components.unifi: debug
```

## Výhody, nevýhody a bezpečnost

Výhodou je místní push spojení, přehled o klientech a síťových prvcích a využití jejich stavů v automatizacích bez instalace agentů.

Nevýhodou je citlivost na změny API mezi verzemi UniFi, požadavek na místní účet a omezení přítomnosti dané chováním telefonu. Ovládací entity mohou měnit síť, PoE i pravidla firewallu; chybná automatizace proto může odpojit zařízení nebo uživatele.

Heslo účtu uložte pouze do Home Assistantu. Pro monitoring použijte co nejnižší funkční oprávnění. Plný přístup povolte jen tehdy, když opravdu potřebujete ovládání, a změny WLAN, portů či pravidel nejdřív vyzkoušejte ručně. Integrace nenahrazuje zálohy konfigurace UniFi ani dohled dostupnosti z nezávislého systému.

## Zdroje

- [Home Assistant: integrace UniFi Network](https://www.home-assistant.io/integrations/unifi/)
- [Ubiquiti: místní API aplikace UniFi Network](https://help.ui.com/hc/en-us/articles/30076656117655-Getting-Started-with-the-Official-UniFi-API)
- [Ubiquiti: VLAN pro bezpečnost a výkon](https://help.ui.com/hc/en-us/articles/26136851868695-Using-VLANs-for-Network-Security-and-Performance)
- [Ubiquiti: přiřazení VLAN k Wi-Fi SSID](https://help.ui.com/hc/en-us/articles/26136823938583-Creating-UniFi-WiFi-SSIDs)
- [Home Assistant: spouštěče automatizací](https://www.home-assistant.io/docs/automation/trigger/)
