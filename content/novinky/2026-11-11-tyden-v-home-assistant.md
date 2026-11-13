---
title: "Týden v Home Assistant: Marketplace, chytřejší AI a bezpečnější HAOS"
description: "Přehled za 4.–10. listopadu 2026: Home Assistant 2026.11, vestavěný Marketplace, AI diagnostika, HAOS 18.5 a opravy Shelly i UniFi."
cas: "4 minuty"
obtiznost: "Přehled"
kontrola_zdroju: "2026-11-11"
stav: "Ověřeno podle oficiálních zdrojů"
temata: [Home Assistant, Novinky, Marketplace, AI, HAOS, Shelly, UniFi]
obrazek: "/assets/images/novinky-2026-11-11.png"
obrazek_alt: "Ilustrace chytrého domu s tržištěm komunitních doplňků, diagnostikou a chráněnou aktualizací domácího serveru"
---
## Největší vydání přineslo Marketplace

Přehled za 4.–10. listopadu 2026 navazuje na [minulý týden](/novinky/2026-11-04-tyden-v-home-assistant/). Hlavní událostí je stabilní Home Assistant 2026.11, následovaný první opravnou verzí a bezpečnostní aktualizací systému pro Raspberry Pi a Home Assistant Yellow.

Home Assistant 2026.11 vyšel 4. listopadu a začlenil HACS přímo do systému pod názvem **Marketplace**. Najdete jej v Nastavení a funguje u všech způsobů instalace včetně Home Assistant Container. Stávající instalace HACS se při prvním spuštění po aktualizaci převede automaticky: nainstalované projekty, vlastní repozitáře i jejich aktualizace mají zůstat zachované. Samostatný instalátor HACS už pro verzi 2026.11 není určen.

Pohodlnější instalace ale neznamená, že jsou komunitní doplňky oficiálně otestované. Home Assistant upozorňuje, že mohou přistupovat k internetu či datům a ovlivnit stabilitu systému. Před instalací proto zkontrolujte autora, požadovanou verzi, otevřené chyby a stáří poslední aktualizace.

## Praktičtější automatizace a přehledy

Nová verze umí z cíle automatizace něco výslovně vynechat. Můžete například rozsvítit celé patro kromě kuchyně; pokud do kuchyně později přidáte další světlo, zůstane také vynechané. Dashboardy dostaly automatické sekce, které samy zobrazují vybrané typy entit, zařízení, oblasti či štítky a průběžně se aktualizují.

Přibylo také ukládání záloh a médií na místní disky, obousměrný zvuk u podporovaných Matter kamer, LoRaWAN a 38 nových integrací. Kvůli novému skládání názvů mohou některé viditelné názvy v dashboardech vypadat jinak; ID entit a automatizace se podle oznámení měnit nemají.

## AI může hledat problém, ale potřebuje hranice

Kompatibilní AI asistenti přes Home Assistant LLM API nově dokážou číst systémový protokol, zjistit informace o instalaci, vyhledat dostupné akce, jednu z nich spustit a vypsat či znovu načíst integraci. Přístup k logům vyžaduje účet správce a LLM API musí správce výslovně připojit ke konverzačnímu agentovi nebo MCP serveru.

To je užitečné při hledání závady, ale jde i o možnost zasahovat do domácnosti. MCP server lze omezit jen na nástroje pro čtení; dávejte proto AI pouze oprávnění, která skutečně potřebuje. Google Gemini TTS v tomto vydání přešlo na Gemini 3.8 Flash a přidalo řízení stylu řeči, další hlasy a jazyky; integrace OpenAI doplnila podporu GPT-6.1 Terra.

## Opravy pro Shelly a UniFi, HAOS 18.5 pro Raspberry Pi

Core 2026.11.1 z 9.11 opravuje situaci, kdy se u obnoveného spícího Shelly RPC zařízení po probuzení nepřidaly nové entity. Součástí je také aktualizace knihovny `aiounifi` na verzi 98; poznámky k vydání však z této položky samy o sobě nedokládají novou funkci UniFi Network nebo Protect.

Home Assistant OS 18.5 vyšel 6.11. Pro Raspberry Pi a Home Assistant Yellow aktualizuje jádro na 6.18.59 kvůli opravě CVE-2026-98432 v síťové části Linuxu. Ostatní platformy dostaly opravu už v HAOS 18.4. Podle autorů nebylo známé rozsáhlé zneužívání, aktualizaci ale zvlášť doporučují systémům přímo vystaveným internetu nebo nedůvěryhodné síti.

V kontrolovaných zdrojích jsme pro tento týden nedoložili novou stabilní verzi firmwaru Shelly; verze 2.2.0 zůstávala v části beta. Na oficiálním blogu nepřibylo nové partnerství Works with Home Assistant ani nový vlastní hardware Home Assistant.

## Zdroje

- [Home Assistant 2026.11 – poznámky k vydání a oprava 2026.11.1](https://www.home-assistant.io/blog/2026/11/04/release-202611/)
- [Home Assistant Core 2026.11.1](https://github.com/home-assistant/core/releases/tag/2026.11.1)
- [Shelly – oprava obnovených spících zařízení](https://github.com/home-assistant/core/pull/190447)
- [UniFi – aktualizace knihovny aiounifi](https://github.com/home-assistant/core/pull/190145)
- [Home Assistant OS 18.5](https://github.com/home-assistant/operating-system/releases/tag/18.5)
- [Home Assistant – integrace Shelly](https://www.home-assistant.io/integrations/shelly/)
- [Shelly – changelog firmwaru Gen2+](https://shelly-api-docs.shelly.cloud/gen2/changelog/)
- [Home Assistant – integrace UniFi Network](https://www.home-assistant.io/integrations/unifi/)
- [Home Assistant – integrace UniFi Protect](https://www.home-assistant.io/integrations/unifiprotect/)
- [Works with Home Assistant – oznámení partnerů](https://www.home-assistant.io/blog/categories/works-with-home-assistant/)
