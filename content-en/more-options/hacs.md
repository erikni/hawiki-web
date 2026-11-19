---
title: "HACS: Installation and Configuration Editor"
description: "How to install HACS, add community add-ons, and use the Studio Code Server editor."
obrazek: "/assets/images/hacs-instalace-nastroje.png"
obrazek_alt: "Illustration of the smart home add-on and configuration editor."
cas: "6 minutes read"
obtiznost: "Advanced"
kontrola_zdroju: "2026-10-06"
stav: "Based on documentation"
temata:
  - "HACS"
  - "Community Integrations"
  - "Applications"
  - "Studio Code Server"
translationKey: "more-options.hacs"
---

## HACS and Applications are Not the Same
**HACS** (Home Assistant Community Store) manages community integrations, dashboard cards, and other add-ons. Use it when standard Home Assistant does not have the required functionality. It is not the official HA store, and the availability of a project does not guarantee its quality.

**Applications** run as standalone services in Home Assistant OS. The Studio Code Server editor is an example of this. HACS does not install applications. In older interfaces, applications were called add-ons. The following procedures are for **HA OS**; the Container installation does not have this store.

## Before Installation
Create a backup in **Settings → System → Backups**. Prepare a GitHub account. For every add-on, read the requirements, instructions, update history, and reported issues. Community integrations run external code inside HA, so choose projects that you trust.

## 1. Download HACS in HA OS
1. Open **Settings → Add-on Store**.
2. In the three-dot menu, open **Repositories** and add `https://github.com/hacs/addons`.
3. Search for **Get HACS**, select the installation, and run the application.
4. Open its **Logs** and follow the completion messages. Get HACS only downloads the necessary files.
5. Restart **Home Assistant**; a simple application restart is not enough.

For Container, use the different branch in the [official HACS guide](https://www.hacs.xyz/docs/use/download/download/). Do not copy the procedure for the HA OS store.

## 2. Complete HACS Setup
In **Settings → Devices & Services → Add integration**, search for **HACS**. If it is missing, restore the browser without cache after restarting. Confirm the stated terms.

Copy the displayed authorization code, open `https://github.com/login/device`, log in, paste the code, and authorize HACS. Return to HA and complete the wizard. The code is not your GitHub login credential.

In HACS, open the selected project and download it according to its instructions. For integrations, a HA restart and addition in **Devices & Services** usually follow; the dashboard card has a different procedure. The download itself is not the complete setup. Before updates, read the changes and keep the option to revert from a backup.

## Studio Code Server: Editor in the Browser
**[Studio Code Server](https://github.com/hassio-addons/app-vscode)** allows editing HA configuration from the browser. It offers YAML highlighting and file management; it is not necessary for common click-based automations.

In the add-on store, search for **Studio Code Server**. If the community listing is missing, add the repository `https://github.com/hassio-addons/repository`. Install the application, run it, and open its web interface. Optionally enable startup and sidebar panel.

Before editing a file, save the original version. When making changes to `configuration.yaml`, check the configuration before restarting. Highlighting in the editor does not guarantee the functionality of the settings.

## Sources
- [HACS: Download and Installation](https://www.hacs.xyz/docs/use/download/download/)
- [HACS: Configuration and Authorization](https://www.hacs.xyz/docs/use/configuration/basic/)
- [Home Assistant: Applications and Repositories in HA OS](https://www.home-assistant.io/common-tasks/os/)
- [Studio Code Server: Project](https://github.com/hassio-addons/app-vscode)
- [Studio Code Server: Installation and Usage](https://github.com/hassio-addons/app-vscode/blob/main/vscode/DOCS.md)
