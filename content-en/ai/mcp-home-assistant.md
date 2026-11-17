---
title: 'MCP and Home Assistant: give AI access to selected devices'
description: What MCP means, how to connect an AI assistant to Home Assistant, and how to allow it access only to lights and sockets. Official and community server, local AI, and Rohlík's example.
obrazek: /assets/images/mcp-home-assistant.png
obrazek_alt: AI assistant connected via MCP with enabled light, socket, and shopping basket.
cas: 9 minutes read
obtiznost: Intermediate
kontrola_zdroju: '2026-10-09'
stav: Based on documentation
temata:
- AI
- MCP
- Assist
- Permissions
- Local models
- LM Studio
translationKey: "ai.mcp-home-assistant"
---

AI can advise how to turn off the light. With a connection via MCP, it can also execute the command. You determine which parts of the home you grant it access to.

## What is MCP

**MCP is Model Context Protocol**, an open standard for connecting AI applications to data and tools. Imagine a common socket: instead of a separate connection for every service, the AI uses the same method of communication.

The AI application is the **client**. The **MCP server** offers it specific capabilities, such as checking the status of a light or turning it on. The **AI agent** is the assistant that uses these tools to fulfill the request. MCP itself is not a model or automation: it does not provide intelligence or determine what should be done.

## What you get in Home Assistant

The official integration [**Model Context Protocol Server**](https://www.home-assistant.io/integrations/mcp_server/) exposes the home to an external AI assistant via the Assist interface. The agent can retrieve a current overview and control supported, enabled entities. An entity is a specific element in HA: a light, a switch, or a sensor.

You can expose multiple devices, or just two lights and one switch. However, the built-in Assist API is not for HA administration: do not expect it to install integrations or make arbitrary configuration changes. The selection of entities for Assist is common for other assistants using this interface.

## Cloud and local AI: MCP does not require the cloud

**You can also use MCP with a model running on your own computer.** You need an application that can connect the MCP server, and a model capable of reliably calling tools. Simply downloading the model is not enough: the application must provide the model with a set of tools and execute its requests.

| Variant | Where the model and connection run |
| :--- | :--- |
| Cloud AI with remote connector | The model runs with the provider, and its server connects to HA. It requires an accessible address. |
| Local AI with local client | Both the model and the application run at your location. They can connect to HA directly on the local network. |

For example, **LM Studio** can run local models and connect MCP servers. **Ollama** can provide a local model to another application; that application must handle the MCP and tool usage. For choosing a computer and model, the article [Local models: own AI server](https://www.hawiki.cz/ai/local-models-own-ai-server/) is relevant.

Note the difference: Claude Desktop with local connection to HA still uses a cloud model. A local connection to a device does not automatically mean local conversation processing. Conversely, a local model and local MCP server can operate at home without cloud AI; connecting to an internet service, such as Rohlík, still requires the internet.

## Allow only selected entities

**You do not have to expose all entities to AI.** When starting with the official Assist server, begin with one light and one socket. In **Settings → Voice Assistants → Expose**, select only these entities for Assist and also check previously allowed items. You can leave locks, gates, or the refrigerator socket unexposed.

Distinguish between two settings: selecting the **LLM API** determines the available interface and tools, while selecting **entities for Assist** determines the devices available via Assist. Turning off "Expose all LLM APIs" does not automatically select lights. Similarly, logging in a user does not replace controlling the exposed entities.

This limitation applies to the described official Assist API. Other or community interfaces may have different options and scope of access. The instruction "only control lights" in a conversation is a prompt for the model, not a technical permission limitation.

## How to set up MCP

It is assumed that you have a functioning HA with connected devices and an AI application that supports MCP. Here we will use the remote Claude connector; this requires an internet-accessible HTTPS address for HA, such as from Home Assistant Cloud. The `homeassistant.local` address alone is insufficient because the connection originates from the Anthropic cloud.

1. In HA, open **Settings → Devices & Services → Add integration** and search for **Model Context Protocol Server**.
2. In the integration configuration, disable **Expose all LLM APIs** and select only **Assist**. Do not enable any other interfaces that you do not need.
3. In **Settings → Voice assistants → Enable**, check the selection for **Assist**. For starters, leave only selected lights and sockets; remove all other entities. Give them clear names and rooms.
4. In Claude, open **Customize → Connectors → Add custom connector**. Enter the Home Assistant name and the URL `https://YOUR-HA-ADDRESS/api/mcp`; replace the domain with your actual HA address.
5. Select **OAuth** for login. If the client requires a custom OAuth Client ID, use `https://claude.ai` for Claude. Connect the connector and log in to HA; the new integration settings usually require an administrator account.
6. Enable the connector in the conversation. First, try "Which lights are on?" and then "Turn off the living room light." Also check the result in HA and on the light.

If HA must remain accessible only at home, the documentation describes connecting Claude Desktop locally via the `mcp-proxy` utility. This procedure is different from the cloud connector.

## Example with a Local Model in LM Studio

For this process, use the official server set up in Assist and the selected entity. You do not need to expose HA to the internet for the local client.

1. In HA, open **User Profile → Security → Long-Lived Access Tokens** and create a token for this connection. When prompted by the integration, use the corresponding account for administrator access.
2. In LM Studio, open the right panel **Program → Install → Edit mcp.json**.
3. If the file does not already contain other servers, paste the following entire content. If it does, only add the `homeassistant` item to the existing `mcpServers` object.

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

Replace `192.168.1.20` with the actual HA IP address and `VAS_TOKEN` with the created token. The example assumes HA over HTTP within a trusted home network; if you use HTTPS, enter your HTTPS address. The token is saved to the file: do not share it, do not paste it into a chat, or onto GitHub. Revoke it in HA when you are finished using it.

After saving, verify the MCP connection and enable its tools in the conversation with the local model. Ask for the status of a light and then ask it to turn on. Check the actual result. The model may respond well in Czech but still call tools incorrectly; judge suitability based on the executed actions, not just the text response.

## Official server, or community ha-mcp?

The [Official MCP Server](https://www.home-assistant.io/integrations/mcp_server/) is part of HA. The described Assist API is suitable for reading the status and controlling selected devices. It is a straightforward path for initially connecting a home with AI.

The [**Unofficial ha-mcp from homeassistant-ai**](https://github.com/homeassistant-ai/ha-mcp) is a standalone community project. It additionally offers the creation and modification of automations, scripts, or dashboards, and work with history and diagnostics. According to its README, the scope of entities across HA: **does not limit the selection of entities for Assist in the same way as the official server**. It offers a read-only mode for switching individual tools; however, this is not the same as allowing only two specific lights.

Its documentation recommends a custom component via HACS and describes an application for HA or Docker. Please take the installation procedure and connection address from this project; they are not the same as the official integration and its `/api/mcp`. If you want to allow the agent to change the configuration, first prepare a backup and review the proposed changes.

## From Household to Shopping

Other examples of MCP servers work with files in selected folders or with Git repositories. One agent can thus use multiple different services; each connection has its own options and access.

The Czech [**Rohlík offers a dedicated MCP server**](https://www.rohlik.cz/stranka/mcp-server) for shopping. It offers MCP for searching for goods, managing the basket, and order information. You can enter, "Prepare a basket of pasta for four people." However, according to its terms, you complete the order by confirming it in the e-shop, not through the MCP client. The service is experimental.

For household use, try "Turn off all permitted lights and switch off the lamp socket." Limit permissions in HA, not just with a chat message. The socket might power an important appliance; start with a lamp and confirm the first action. When using cloud AI, be aware that accessible household data will be transferred to its provider.

## Sources

- [Home Assistant: Model Context Protocol Server](https://www.home-assistant.io/integrations/mcp_server/)
- [Home Assistant: Exposing entities for Assist](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/)
- [Home Assistant: Capabilities and limitations of the Assist API](https://developers.home-assistant.io/docs/core/llm/)
- [MCP: Protocol architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [Anthropic: Connecting remote MCP servers](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [MCP: Examples of servers for files and Git](https://github.com/modelcontextprotocol/servers)
- [Rohlík: MCP server, connection and terms](https://www.rohlik.cz/stranka/mcp-server)

- [Community project: Unofficial ha-mcp](https://github.com/homeassistant-ai/ha-mcp)
- [LM Studio: Connecting MCP servers](https://lmstudio.ai/docs/app/mcp)
