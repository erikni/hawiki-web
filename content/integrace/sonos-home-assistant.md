---
title: "Sonos v Home Assistantu: instalace, multiroom a hlasová oznámení"
seoTitle: "Sonos a Home Assistant: instalace, multiroom a TTS"
description: "Praktický český návod na integraci Sonos s Home Assistantem: přidání reproduktorů, síť, skupiny, TTS oznámení a obnovení přehrávání."
cas: "12 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-11-04"
stav: "Podle dokumentace"
sourceType: "official-docs"
obrazek: "/assets/images/sonos-home-assistant-integrace.png"
obrazek_alt: "Ilustrace Home Assistantu propojeného se třemi reproduktory v různých místnostech"
temata:
  - Sonos
  - Integrace
  - Multiroom audio
  - Hlasová oznámení
  - Automatizace
related:
  - zaciname/zarizeni-entita-integrace
  - pomoc/automatizace-nefunguje
  - pomoc/vypadek-internetu
---

Integrace **Sonos** propojí reproduktory Sonos a IKEA SYMFONISK s Home Assistantem. Každý reproduktor získá entitu `media_player`, přes kterou lze ovládat přehrávání a hlasitost, spouštět oblíbenou hudbu, vytvářet skupiny pro více místností nebo přehrát hlasové oznámení. Komunikace se reproduktory probíhá v místní síti; účet hudební služby je ale stále potřeba pro služby, jako je Spotify.

## Co budete potřebovat

- fungující systém Sonos nastavený v aplikaci Sonos,
- Home Assistant připojený do stejné místní sítě,
- v Sonos zapnuté **UPnP** v nabídce **Účet → Soukromí a zabezpečení → UPnP**,
- u oddělených sítí nebo VLAN správně nastavená pravidla mezi Home Assistantem a reproduktory,
- pro hlasová oznámení nakonfigurovanou službu převodu textu na řeč (TTS).

Sonos doporučuje mít aplikaci a všechny produkty ve stejné podsíti. Home Assistant umí pokročilé zapojení přes více podsítí, ale automatické vyhledání a zpětné události pak závisejí na nastavení routeru a firewallu. Integrace je vedena jako **Local Push**: běžné řízení a změny stavu tedy nemusí procházet cloudem Sonos. Streamovaná hudba nebo cloudové TTS však mohou internet potřebovat.

## Přidání Sonosu do Home Assistantu

1. Otevřete **Nastavení → Zařízení a služby**.
2. Pokud Home Assistant zobrazil objevený Sonos, vyberte **Nastavit**.
3. Když se nic neobjevilo, zvolte **Přidat integraci**, vyhledejte **Sonos** a dokončete průvodce.
4. Otevřete přidanou integraci a zkontrolujte zařízení i entity. Každý přehrávač by měl mít vlastní entitu, například `media_player.obyvaci_pokoj`.
5. V **Nástroje pro vývojáře → Akce** vyzkoušejte na jednom reproduktoru akci pro pozastavení nebo změnu hlasitosti.

Přesný název entity se odvodí od názvu místnosti nebo zařízení. ID z příkladů níže proto vždy nahraďte ID svých entit. Integrace se běžně nastavuje přes uživatelské rozhraní. YAML je určen hlavně pro pokročilé síťové případy, například pro ruční seznam IP adres reproduktorů.

## Co integrace zpřístupní

Vedle základního přehrávání se podle modelu objeví ovládání basů, výšek, loudness, crossfade, stavové kontrolky nebo dotykových tlačítek. Domácí kino může přidat noční režim, zvýraznění řeči, zpoždění zvuku a nastavení prostorových reproduktorů. Bateriové modely mohou mít snímač nabití a napájení. Alarmy vytvořené v aplikaci Sonos se zobrazují jako samostatné přepínače.

Ne každá funkce je dostupná na každém modelu nebo firmwaru. Starší systém Sonos S1 může mít omezenou podporu moderních oznámení. Některé změny provedené mimo Home Assistant se navíc zjišťují periodicky, takže se jejich stav nemusí aktualizovat okamžitě.

Oblíbené položky z aplikace Sonos lze přehrávat přes prohlížeč médií. Pokročilí uživatelé mohou zapnout ve stránce integrace ve výchozím stavu vypnutý senzor `sensor.sonos_favorites`, ale pro běžné použití je prohlížeč médií jednodušší.

## Multiroom: spojení reproduktorů do skupiny

Akce `media_player.join` spojí podporované přehrávače do synchronizované skupiny. Cílový reproduktor se stane vedoucím a další reproduktory se k němu připojí. Akce `media_player.unjoin` vybraný přehrávač ze skupiny zase odebere.

Následující kompletní automatizaci vložte do YAML editoru jedné nové automatizace. Předem vytvořte pomocníka **Přepínač** s ID `input_boolean.hudba_cely_byt`. Nahraďte tři entity reproduktorů. Příklad pouze vytvoří skupinu; hudbu pak spusťte na vedoucím přehrávači v obývacím pokoji.

```yaml
alias: Sonos – hudba v celém bytě
triggers:
  - trigger: state
    entity_id: input_boolean.hudba_cely_byt
    to: "on"
conditions: []
actions:
  - action: media_player.join
    target:
      entity_id: media_player.obyvaci_pokoj
    data:
      group_members:
        - media_player.kuchyne
        - media_player.loznice
mode: single
```

Pro rozpojení vytvořte druhou automatizaci se spouštěčem `to: "off"` a akcí `media_player.unjoin` cílenou na `media_player.kuchyne` a `media_player.loznice`. Seskupejte jen přehrávače, které jsou součástí stejného systému Sonos. Běžná skupina entit v Home Assistantu není totéž co skutečná synchronizovaná skupina Sonos.

## Hlasové oznámení bez přerušení hudby

Sonos podporuje u `media_player.play_media` volbu `announce: true`. Oznámení se přehraje jako překryv přes současnou hudbu, hudba se ztiší a po skončení se vrátí na původní hlasitost. Je to vhodnější než ruční pozastavení a opětovné spuštění, pokud jej váš model a firmware podporují.

Tento příklad oznámí deset minut otevřené okno. Vytvořte novou automatizaci, otevřete **Upravit v YAML** a vložte celý blok. Nahraďte kontakt okna i reproduktor. Cesta `media-source://tts/cloud` předpokládá aktivní Home Assistant Cloud; při jiné TTS službě použijte její identifikátor podle dokumentace poskytovatele.

```yaml
alias: Sonos – upozornění na otevřené okno
triggers:
  - trigger: state
    entity_id: binary_sensor.okno_obyvaci_pokoj
    to: "on"
    for: "00:10:00"
conditions: []
actions:
  - action: media_player.play_media
    target:
      entity_id: media_player.obyvaci_pokoj
    data:
      announce: true
      media_content_type: music
      media_content_id: >-
        media-source://tts/cloud?message="Okno v obývacím pokoji je deset minut otevřené."
      extra:
        volume: 35
mode: single
```

Hodnota `volume` je hlasitost oznámení v rozsahu 0 až 100, nikoli běžná desetinná hlasitost entity. Home Assistant musí umět Sonosu zpřístupnit vytvořený zvukový soubor a reproduktor musí být dosažitelný na TCP portu 1443. U TTS je důležitá také správná místní URL v **Nastavení → Systém → Síť**. Samopodepsaný HTTPS certifikát může přehrávač odmítnout.

## Kdy použít snapshot a restore

Akce `sonos.snapshot` uloží aktuální přehrávání a `sonos.restore` je později obnoví. Hodí se pro starší zařízení bez spolehlivé podpory `announce` nebo pro vlastní zvuk, který má přehrávání skutečně přerušit. Volba `with_group: true` uloží a obnoví také uspořádání skupiny a stav dalších reproduktorů v ní.

Snapshot ale **neukládá frontu skladeb**. Během přerušení ji proto neměňte. Cloudovou frontu spuštěnou například přímo ze Spotify nebo přes Amazon Alexa nelze znovu nastartovat. Pro běžné krátké hlášení je proto `announce: true` bezpečnější.

Následující kompletní skript vložte do YAML editoru jednoho nového skriptu. Nahraďte ID reproduktoru a adresu zvuku. Soubor musí být dostupný přímo reproduktoru; při uložení do `config/www/zvuky/zvonek.mp3` odpovídá URL `/local/zvuky/zvonek.mp3`.

```yaml
alias: Sonos – zvonek se zachováním přehrávání
sequence:
  - action: sonos.snapshot
    target:
      entity_id: media_player.obyvaci_pokoj
    data:
      with_group: true
  - action: media_player.play_media
    target:
      entity_id: media_player.obyvaci_pokoj
    data:
      media_content_type: music
      media_content_id: "http://192.168.1.50:8123/local/zvuky/zvonek.mp3"
  - delay: "00:00:04"
  - action: sonos.restore
    target:
      entity_id: media_player.obyvaci_pokoj
    data:
      with_group: true
mode: single
```

Čtyřsekundovou prodlevu přizpůsobte délce souboru. Pevná prodleva je jednoduchá, ale u souboru s proměnlivou délkou nemusí být přesná. Skript nejprve otestujte s nízkou hlasitostí a bez důležité rozpracované fronty.

## Síť, VLAN a soukromí

Pro rychlé změny stavu se reproduktory připojují zpět k Home Assistantu na TCP port 1400. Když je spojení blokované, integrace přejde na pomalejší dotazování a Home Assistant na problém upozorní. Pokud je port 1400 obsazený, může Home Assistant zkusit některý z dalších 100 portů. Pro `announce` a TTS musí Home Assistant dosáhnout na TCP port 1443 každého reproduktoru.

V oddělených VLAN nestačí povolit pouze internet. Je nutné vyřešit vyhledání zařízení, UPnP a spojení v obou směrech. Pokud automatické hledání není možné, lze v `configuration.yaml` uvést pevné IP adresy reproduktorů. U instalace s více síťovými rozhraními lze v integraci **Síť** vybrat rozhraní pro automatické hledání. Nastavení `advertise_addr` je určeno pro pokročilé případy, například NAT nebo kontejner bez hostitelské sítě.

Integrace ovládá Sonos místně, což omezuje závislost na cloudu pro základní povely. Hudební služby, registrace, aktualizace a některé zdroje TTS mohou komunikovat přes internet podle pravidel dané služby. Home Assistant ani Sonos nevkládejte bez rozmyslu do veřejně přístupné sítě a neotevírejte uvedené porty do internetu.

## Když integrace nefunguje

- **Sonos se nenajde:** ověřte UPnP v aplikaci Sonos, stejnou podsíť a to, že Home Assistant vidí místní síť. Restartujte nejdříve integraci, ne celý systém.
- **Při nastavení se objeví chyba 403:** podle dokumentace Home Assistantu bývá příčinou vypnuté UPnP v systému Sonos.
- **Stavy se mění pomalu:** zkontrolujte, zda reproduktory dosáhnou na Home Assistant na TCP portu 1400. Při blokaci se používá pomalejší dotazování.
- **TTS se nepřehraje:** ověřte TCP 1443 směrem k reproduktoru, místní URL Home Assistantu, formát zvuku a dostupnost TTS služby.
- **Oznámení neobnoví hudbu:** použijte `announce: true`; u snapshotu neměňte frontu a počítejte s omezením cloudových front.
- **Skupina nehraje synchronně:** použijte `media_player.join`, ne obecnou skupinu entit, a ověřte, že všechny přehrávače patří do stejného systému Sonos.

Pro hledání chyby spusťte jednotlivou akci v **Nástroje pro vývojáře → Akce** a u automatizace otevřete její trasování. Tím oddělíte problém integrace od chyby ve spouštěči nebo podmínce automatizace.

## Výhody a omezení

Největší výhodou je místní ovládání, automatické nalezení, podpora skutečných skupin Sonos a oznámení, která nemusí zastavit hudbu. Home Assistant navíc sjednotí reproduktory s čidly, dveřmi, kalendářem a dalšími automatizacemi.

Nevýhodou jsou vyšší nároky na síť při použití VLAN, rozdíly mezi modely a firmwarem S1/S2 a omezené obnovení cloudových front. Home Assistant také nenahrazuje aplikaci Sonos pro prvotní nastavení systému a přidání účtů hudebních služeb.

## Zdroje

- [Home Assistant: integrace Sonos](https://www.home-assistant.io/integrations/sonos/)
- [Home Assistant: akce Snapshot](https://www.home-assistant.io/actions/sonos.snapshot/)
- [Home Assistant: akce Restore](https://www.home-assistant.io/actions/sonos.restore/)
- [Home Assistant: spojení přehrávačů do skupiny](https://www.home-assistant.io/actions/media_player.join/)
- [Home Assistant: Text-to-speech (TTS)](https://www.home-assistant.io/integrations/tts/)
- [Sonos: systémové a síťové požadavky](https://support.sonos.com/en-us/article/sonos-system-requirements)
- [Sonos: nastavení firewallu](https://support.sonos.com/en/article/configure-your-firewall-to-work-with-sonos)
