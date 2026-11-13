---
title: "Přehled spotřeby elektřiny"
description: "Zjistěte, kolik elektřiny domácnost a jednotlivé spotřebiče využívají, pomocí panelu Energie v Home Assistant."
cas: "20 minut"
obtiznost: "Střední"
kontrola_zdroju: "2026-10-01"
stav: "Podle dokumentace"
temata:
  - elektřina
  - spotřeba
  - Energie
  - YAML
---

Kolik elektřiny spotřebuje domácnost za den a které zařízení se na tom podílí? Home Assistant umí údaje z měřidel zobrazit v panelu **Energie**. Začněte jedním dostupným měřením a další přidávejte postupně. Samotná instalace Home Assistant spotřebu nezměří: potřebujete zařízení nebo službu, které dodávají data přes integraci.

## Příkon není spotřeba

**W nebo kW** říkají, jaký příkon má zařízení právě teď. **Wh nebo kWh** vyjadřují energii spotřebovanou za určitou dobu. Spotřebič s konstantním příkonem 1 000 W za hodinu spotřebuje 1 kWh. Krátká špička proto nemusí znamenat velkou denní spotřebu.

Pro přehled za den či měsíc použijte měření energie. Příkon můžete přidat vedle něj pro pohled na aktuální odběr. Pokud zařízení poskytuje oba údaje, není potřeba energii dopočítávat.

## Co chcete měřit

Celou domácnost sledujte podle měření odběru ze sítě, například z kompatibilního elektroměru. Jedna zásuvka s měřením ukáže pouze připojený spotřebič. Její údaj tedy nevkládejte jako odběr celé domácnosti.

Pro první pokus využijte již připojené měřidlo. Pokud vybíráte nové, ověřte konkrétní integraci, měření energie a dovolené zatížení. Zapojení měřidla do rozvaděče svěřte elektrikáři. Tento návod popisuje práci s dostupnými daty, nikoli elektroinstalaci.

## Přidání do panelu Energie

1. U měřidla ověřte entitu energie a její jednotku. Zkontrolujte, zda při spotřebě údaj roste.
2. Otevřete **Nastavení → Přehledy → Energie** (Settings → Dashboards → Energy).
3. Pro celkový odběr v části elektrické sítě přidejte připojení k síti a vyberte statistiku energie odebrané ze sítě. Dodávku zpět přidávejte pouze tehdy, pokud ji skutečně měříte.
4. Měřené spotřebiče přidejte jako jednotlivá zařízení. Nepřidávejte stejný spotřebič dvakrát pod různými názvy.
5. Uložte nastavení a vyčkejte na zpracování statistik. První data se nemusí objevit okamžitě.

Nabídka obsahuje jen kompatibilní statistiky. Pokud senzor chybí, ověřte jednotku, podporu dlouhodobých statistik a to, že není vyloučený ze zaznamenávání. Pouhé přejmenování jednotky z W na kWh měření neopraví.

## Když máte pouze příkon

Home Assistant nabízí pomocníka **Integral**, který z průběhu příkonu odhaduje energii. Lze jej vytvořit v rozhraní mezi pomocníky nebo pomocí YAML. Následující příklad patří do `configuration.yaml`; máte-li už sekci `sensor:`, přidejte pouze položku pod ni.

Předpokladem je existující senzor příkonu s jednotkou W a třídou zařízení `power`. Nahraďte `sensor.pracka_prikon` vlastním ID, zkontrolujte konfiguraci a restartujte Home Assistant.

```yaml
sensor:
  - platform: integration
    source: sensor.pracka_prikon
    name: Pracka energie
    unit_prefix: k
    unit_time: h
    method: left
    round: 3
    max_sub_interval:
      minutes: 5
```

Výsledkem je odhad v kWh. Metoda `left` se hodí pro příkon, který se skokově mění a mezi hlášeními drží hodnotu. Přesnost závisí na kvalitě a četnosti měření. Novou entitu najděte podle názvu a přidejte jako jednotlivé zařízení. Pokud integrace nabízí vlastní měření energie, upřednostněte je.

## Jak přehled číst

Porovnávejte stejné intervaly a nechte měření běžet několik dní. Součet několika zásuvek nepokrývá neměřené spotřebiče. Údaj ceny založený na jedné sazbě navíc nezahrnuje automaticky všechny položky faktury. Přehled vám pomůže najít změny a velké odběry; sám o sobě elektřinu neuspoří.

## Zdroje

- [Home Assistant: správa energie](https://www.home-assistant.io/docs/energy/)
- [Home Assistant: přidání odběru ze sítě](https://www.home-assistant.io/docs/energy/electricity-grid/)
- [Home Assistant: měření jednotlivých zařízení](https://www.home-assistant.io/docs/energy/individual-devices/)
- [Home Assistant: časté otázky k panelu Energie](https://www.home-assistant.io/docs/energy/faq/)
- [Home Assistant: Integral a převod příkonu na energii](https://www.home-assistant.io/integrations/integration/)
