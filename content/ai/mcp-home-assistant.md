---
title: "MCP a Home Assistant: dejte AI přístup k vybraným zařízením"
description: "Co znamená MCP, jak připojit AI asistenta k Home Assistantu a povolit mu třeba jen světla a zásuvky. Oficiální i komunitní server, místní AI a příklad Rohlíku."
obrazek: "/assets/images/mcp-home-assistant.png"
obrazek_alt: "AI asistent propojený přes MCP s povoleným světlem, zásuvkou a nákupním košíkem."
cas: "9 minut čtení"
obtiznost: "Střední"
kontrola_zdroju: "2026-10-09"
stav: "Podle dokumentace"
temata:
  - AI
  - MCP
  - Assist
  - Oprávnění
  - Místní modely
  - LM Studio
---

AI umí poradit, jak zhasnout světlo. S připojením přes MCP může povel také provést. Vy určujete, které části domácnosti jí zpřístupníte.

## Co znamená MCP

**MCP je Model Context Protocol**, otevřený standard pro propojení AI aplikací s daty a nástroji. Představte si společnou zásuvku: místo zvláštního propojení pro každou službu používá AI stejný způsob komunikace.

AI aplikace je **klient**. **MCP server** jí nabízí konkrétní možnosti, třeba zjištění stavu světla nebo jeho zapnutí. **AI agent** je asistent, který tyto nástroje využívá k plnění zadání. MCP samo není model ani automatizace: neposkytuje inteligenci a neurčuje, co se má udělat.

## Co získáte v Home Assistantu

Oficiální integrace [**Model Context Protocol Server**](https://www.home-assistant.io/integrations/mcp_server/) zpřístupní domácnost externímu AI asistentovi přes rozhraní Assist. Agent může získat aktuální přehled a ovládat podporované, povolené entity. Entita je konkrétní prvek v HA: světlo, spínač zásuvky nebo senzor.

Můžete zpřístupnit více zařízení, nebo jen dvě světla a jednu zásuvku. Vestavěné Assist API ale neslouží k administraci HA: instalaci integrací či libovolnou změnu konfigurace od něj nečekejte. Výběr entit pro Assist je společný i pro další asistenty využívající toto rozhraní.

## Cloudová i místní AI: MCP nevyžaduje cloud

**MCP můžete používat také s modelem běžícím na vlastním počítači.** Potřebujete aplikaci, která umí připojit MCP server, a model schopný spolehlivě volat nástroje. Samotné stažení modelu nestačí: aplikace musí předat modelu nabídku nástrojů a vykonat jeho požadavky.

| Varianta | Kde běží model a připojení |
| --- | --- |
| Cloudová AI se vzdáleným konektorem | Model běží u poskytovatele a jeho server se připojuje k HA. Potřebuje dosažitelnou adresu. |
| Místní AI s místním klientem | Model i aplikace běží u vás. K HA se mohou připojit přímo v domácí síti. |

Například **LM Studio** umí spouštět místní modely a připojovat MCP servery. **Ollama** může poskytovat místní model jiné aplikaci; tato aplikace musí zajistit MCP a práci s nástroji. Pro výběr počítače a modelu navazuje článek [Místní modely: vlastní AI server](https://www.hawiki.cz/ai/mistni-modely-vlastni-ai-server/).

Pozor na rozdíl: Claude Desktop s místním propojením k HA stále používá cloudový model. Místní připojení k zařízení samo neznamená místní zpracování rozhovoru. Naopak místní model a místní MCP server mohou pracovat doma bez cloudové AI; připojení k internetové službě, například Rohlíku, dál potřebuje internet.

## Povolte jen vybrané entity

**Nemusíte AI zpřístupnit všechny entity.** U oficiálního serveru s Assist začněte jednou lampou a jednou zásuvkou. V **Nastavení → Hlasoví asistenti → Zpřístupnit** vyberte pro Assist právě tyto entity a zkontrolujte i dříve povolené položky. Zámky, vrata nebo zásuvku lednice můžete ponechat nezpřístupněné.

Rozlišujte dvě nastavení: výběr **LLM API** určuje nabídku rozhraní a nástrojů, zatímco výběr **entit pro Assist** určuje zařízení dostupná přes Assist. Vypnutí „Expose all LLM APIs“ samo o sobě nevybere světla. Stejně tak přihlášení uživatele nenahrazuje kontrolu zpřístupněných entit.

Toto omezení platí pro popsané oficiální Assist API. Další nebo komunitní rozhraní mohou mít jiné možnosti a rozsah přístupu. Pokyn „ovládej pouze světla“ v rozhovoru je zadání pro model, nikoli technické omezení oprávnění.

## Jak MCP rozchodit

Předpokladem je fungující HA s připojenými zařízeními a AI aplikace podporující MCP. Zde použijeme vzdálený konektor Claude; vyžaduje internetově dostupnou HTTPS adresu HA, například z Home Assistant Cloud. Samotné `homeassistant.local` mu nestačí, protože připojení vede z cloudu Anthropic.

1. V HA otevřete **Nastavení → Zařízení a služby → Přidat integraci** a vyhledejte **Model Context Protocol Server**.
2. V konfiguraci integrace vypněte **Expose all LLM APIs** a vyberte pouze **Assist**. Nepovolujte další rozhraní, která nepotřebujete.
3. V **Nastavení → Hlasoví asistenti → Zpřístupnit** zkontrolujte výběr pro **Assist**. Pro začátek ponechte jen vybraná světla a zásuvky; ostatní entity odeberte. Dejte jim jasné názvy a místnosti.
4. V Claude otevřete **Customize → Connectors → Add custom connector**. Zadejte název Home Assistant a URL `https://VASE-ADRESA-HA/api/mcp`; nahraďte doménu svou skutečnou adresou HA.
5. Zvolte přihlášení **OAuth**. Pokud klient vyžaduje vlastní OAuth Client ID, pro Claude použijte `https://claude.ai`. Připojte konektor a přihlaste se do HA; nové nastavení integrace standardně vyžaduje administrátorský účet.
6. Povolte konektor v rozhovoru. Zkuste nejprve „Která světla jsou rozsvícená?“ a potom „Zhasni lampu v obýváku“. Výsledek zkontrolujte také v HA a na lampě.

Pokud má HA zůstat dostupný jen doma, dokumentace popisuje místní připojení Claude Desktop přes pomocný program `mcp-proxy`. Tento postup je odlišný od cloudového konektoru.

## Příklad s místním modelem v LM Studio

Pro tuto cestu použijte oficiální server nastavený na Assist a už vybrané entity. V LM Studio načtěte místní model podporující nástroje. HA nemusíte kvůli místnímu klientovi zpřístupňovat z internetu.

1. V HA otevřete **Uživatelský profil → Zabezpečení → Dlouhodobé přístupové tokeny** a vytvořte token pro toto připojení. Při výchozím požadavku integrace na administrátora použijte odpovídající účet.
2. V LM Studio otevřete pravý panel **Program → Install → Edit mcp.json**.
3. Pokud soubor ještě nemá jiné servery, vložte následující celý obsah. Pokud je má, přidejte pouze položku `homeassistant` do existujícího objektu `mcpServers`.

```json
{
  "mcpServers": {
    "homeassistant": {
      "url": "http://192.168.1.20:8123/api/mcp",
      "headers": {
        "Authorization": "Bearer VAS_TOKEN"
      }
    }
  }
}
```

Nahraďte `192.168.1.20` skutečnou IP adresou HA a `VAS_TOKEN` vytvořeným tokenem. Příklad předpokládá HA přes HTTP v důvěryhodné domácí síti; pokud používáte HTTPS, zadejte svou HTTPS adresu. Token se ukládá do souboru: nesdílejte jej, nevkládejte jej do chatu ani na GitHub. Při ukončení používání jej v HA odvolejte.

Po uložení ověřte připojení MCP a povolte jeho nástroje v rozhovoru s místním modelem. Zeptejte se na stav lampy a potom ji nechte zapnout. Zkontrolujte skutečný výsledek. Model může česky odpovídat dobře a přesto chybně volat nástroje; vhodnost posuzujte podle provedených akcí, nejen podle textové odpovědi.

## Oficiální server, nebo komunitní ha-mcp?

[Oficiální MCP Server](https://www.home-assistant.io/integrations/mcp_server/) je součástí HA. Popsané Assist API je vhodné pro čtení stavu a ovládání vybraných zařízení. Pro první propojení domácnosti s AI je to přehledná cesta.

[**Neoficiální ha-mcp od homeassistant-ai**](https://github.com/homeassistant-ai/ha-mcp) je samostatný komunitní projekt. Nabízí navíc tvorbu a úpravy automatizací, skriptů či dashboardů a práci s historií a diagnostikou. Podle svého README má rozsah entit napříč HA: **výběr entit pro Assist jej neomezuje stejným způsobem jako oficiální server**. Nabízí režim pouze pro čtení a vypínání jednotlivých nástrojů; to ale není totéž jako povolení pouze dvou konkrétních světel.

Jeho dokumentace doporučuje vlastní komponentu přes HACS a popisuje i aplikaci pro HA nebo Docker. Postup instalace a připojovací adresu přebírejte z tohoto projektu; nejsou totožné s oficiální integrací a jejím `/api/mcp`. Pokud chcete agentovi dovolit měnit konfiguraci, nejprve připravte zálohu a kontrolujte návrhy změn.

## Od domácnosti k nákupům

Další příklady MCP serverů pracují se soubory ve vybraných složkách nebo s Git repozitáři. Jeden agent tak může používat více různých služeb; každé připojení má vlastní možnosti a přístup.

Český [**Rohlík nabízí vlastní MCP server**](https://www.rohlik.cz/stranka/mcp-server) pro nákupy. Nabízí MCP pro hledání zboží, správu košíku a informace o objednávkách. Můžete zadat „Připrav mi košík na těstoviny pro čtyři lidi“. Podle jeho podmínek však objednávku dokončujete potvrzením v e-shopu, nikoli přes MCP klienta. Služba je experimentální.

U domácnosti zkuste „Zhasni všechna povolená světla a vypni zásuvku u lampy“. Povolení omezujte v HA, nejen větou v chatu. Zásuvka může napájet i důležitý spotřebič; začněte lampou a první akce potvrzujte. U cloudové AI počítejte s předáním zpřístupněných údajů o domácnosti jejímu poskytovateli.

## Zdroje

- [Home Assistant: Model Context Protocol Server](https://www.home-assistant.io/integrations/mcp_server/)
- [Home Assistant: zpřístupnění entit pro Assist](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: možnosti a omezení Assist API](https://developers.home-assistant.io/docs/core/llm/)
- [MCP: architektura protokolu](https://modelcontextprotocol.io/docs/learn/architecture)
- [Anthropic: připojení vzdálených MCP serverů](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [MCP: příklady serverů pro soubory a Git](https://github.com/modelcontextprotocol/servers)
- [Rohlík: MCP server, připojení a podmínky](https://www.rohlik.cz/stranka/mcp-server)

- [Komunitní projekt: neoficiální ha-mcp](https://github.com/homeassistant-ai/ha-mcp)
- [LM Studio: připojení MCP serverů](https://lmstudio.ai/docs/app/mcp)
