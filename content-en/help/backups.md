---
title: "Backups: How to recover when things go wrong"
description: "Store your home settings even off the main device."
cas: "15 minutes"
obtiznost: "Easy"
kontrola_zdroju: "2026-09-30"
stav: "Based on documentation"
temata:
  - "Backups"
translationKey: "help.backups"
---

## What backups protect you from
Backups help restore your settings after an incident or an unintended change. A copy stored only on the same device will not protect you if that device is lost.

## Procedure for Home Assistant OS
1. Open **Settings → System → Backups**.
2. Follow the wizard to set up automatic backups.
3. Select an available location for a copy off the main device.
4. Securely store the recovery set or encryption key provided by the wizard.
5. Create the first backup and verify that it appears in the list and in the target storage.

Storage options depend on your installation and connected services. For a different installation, follow the corresponding documentation.

## Before making major changes
Check your latest backup and ensure you can access it. Restoring an encrypted backup may require the stored key.

## How to store backups in multiple locations

Read about [backing up using the 3-2-1 method](/help/3-2-1-backups/). The example shows why you should have separate copies and one stored off-site.

## Sources
- [Official backup documentation](https://www.home-assistant.io/common-tasks/general/)
