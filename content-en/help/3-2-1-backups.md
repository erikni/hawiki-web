---
title: '3-2-1 Backup: Where to store backups and how long to keep them'
description: A simple plan for what to do if you lose your Home Assistant setup due to device failure or a problem at home.
cas: 10 minutes read
obtiznost: Easy
kontrola_zdroju: '2026-09-30'
stav: Based on documentation
temata:
- Backup
- 3-2-1 Rule
translationKey: "help.3-2-1-backups"
---

## Why a Backup Directly in Home Assistant Is Not Enough

You have configured lights, heating, and favorite buttons. Then, the device running Home Assistant fails. If the only backup was on that device, you may not be able to access it.

The **3–2–1** method helps distribute this risk: having multiple copies, separating their storage, and keeping one off-site.

## What do the numbers 3-2-1 mean

| Number | Meaning | Example for a home setup |
| --- | --- | --- |
| **3** | Three copies of important data in total | Current data and at least two backup copies |
| **2** | Two different types of storage | Device storage and a separate backup drive; another copy will be on Google Drive |
| **1** | One copy offsite | Encrypted copy on Google Drive |

In the common interpretation of the rule, current data is included in the three copies. **In our example, we will go one step further: we will have three backup copies in addition to the running system.** One directly in Home Assistant, a second on a separate home storage, and a third offsite.

## Three places for your backups

| Location | What it helps with | What it won't solve |
| --- | --- | --- |
| **Directly in Home Assistant** | Quick recovery after a failed change | Device or disk failure |
| **Local NAS or standalone USB disk** | Recovery after main device failure | An event that affects the entire home |
| **Cloud, e.g., Google Drive** | Recovery even if local devices are lost | You need functional access to the account and encryption key |

A NAS is a network-accessible box with disks. For beginners using a USB disk, the simple approach is to copy a backup onto it via a computer and then disconnect it. Simply plugging a USB disk into a device with Home Assistant will not automatically set up backups.

A USB disk where you move the running system itself or its main data is not a backup copy. We need a **standalone backup file**.

For the cloud copy, we will use Google Drive. Two folders on the same disk or in the same cloud account do not represent two independent storage locations.

## Getting Started with Home Assistant

If you do not have backups yet, first follow the [basic backup guide](/help/backups/).

The following procedure is intended for Home Assistant OS. Available storage may vary depending on the installation and connected services.

1. Open **Settings → System → Backups**.
2. Set up automatic backups, for example, daily.
3. Prepare a local NAS as a backup storage, or plan regular copying to a USB drive.
4. In the backups settings, check the local storage to Home Assistant and enable available additional locations. You will connect Google Drive according to the following section.
5. Store the **emergency set with the encryption key** safely off the Home Assistant device itself.
6. Create a backup and check that it has arrived at the selected locations.

Button names may vary slightly depending on the version and language. Off-site copies must also be available in case you cannot run your Home Assistant at all.

## How to connect Google Drive

Home Assistant has a built-in connection to **Google Drive**, which can be used as a backup location. You do not need HACS for this path.

The initial connection also requires setup within the Google Cloud Console. This is the more complex part of the preparation, so allow yourself time or ask someone for help. The Google Cloud Console is used here to enable access; the backup files will be stored on your Google Drive.

1. According to the [official Google Drive guide](https://www.home-assistant.io/integrations/google_drive/), prepare the access credentials and enable the Google Drive API.
2. In Home Assistant, open **Settings → Devices & Services → Add integration** and search for **Google Drive**.
3. Complete the connection with your Google account following the on-screen instructions.
4. In the automatic backup settings, select Google Drive as another location and verify that encryption is enabled for it.
5. Create a backup. Check the **Home Assistant** folder and the file date on Google Drive.

Detailed preparation of the access credentials is in the linked guide. This article explains the backup plan; it does not replace the entire process of setting up the Google account.

## Retention: How long to keep backups

**Retention refers to how long or how many backups you keep before deleting older ones.** Multiple storage locations protect against failure. Keeping multiple older versions helps if you discover an error several weeks later.

The following figures are **our suggested baseline for a typical household**, not mandatory settings or Home Assistant defaults.

| Storage | Suggested Retention | Why |
| --- | --- | --- |
| **Home Assistant** | Last **7 daily backups** | Quick recovery of recent state without filling the main drive for long |
| **Home NAS** | Last **30 daily backups + 12 monthly** | Return to the last month, and to a specific state from last year |
| **USB drive instead of NAS** | **8 weekly backups + 12 monthly** | This plan is easier to maintain for manual weekly copying |
| **Google Drive** | Last **14 daily backups + 6 monthly** | Current copy off-site and longer history with reasonable space demands |

A monthly backup means, for example, one selected copy from the first day of the month. You do not need to archive every day for a whole year. One copy can simultaneously fulfill both the daily and monthly selection; it is not necessary to save it twice.

### Directly in Home Assistant: short history

If you create one backup daily and keep seven successful backups, you will get approximately a week's history. If a backup is missed or multiple backups are made in a day, the number of files is not the same as the number of days.

Keep a copy before an important change separately until you verify that everything is working. Before deleting a local backup, ensure you have a usable copy elsewhere.

### NAS or USB: longer home archive

On a NAS, you can use your own archiving or versioning if your storage supports it. For USB, set a regular day for copying. Name files by date and only delete old copies after successfully saving the new one.

After copying, safely disconnect the USB drive. An archive on a constantly connected drive can suffer the same failure or unwanted deletion as the main system.

### Google Drive: history off-site too

On Google Drive, check the last successful transfer and available space. Keep monthly copies in a separate archive that is not part of the automatic deletion of regular backups.

To start, you can create a separate copy of a verified backup monthly in the Google Drive interface into a dedicated archive folder. You are copying an already stored encrypted file; keep the corresponding key. A separate archive in the same account adds history, but is not counted as a fourth independent storage location.

### What Home Assistant settings can do

Built-in automatic backup allows you to define the number of retained backups. **The table above is the resulting plan; it is not a guide to four separate retention switches in Home Assistant.** Available options depend on the storage and tool used.

If your setup uses a common number of copies for multiple locations, you cannot set different retention rates just by this number. For longer history, use a separate archive on NAS and Google Drive, the backup tool's own options, or manual selection of monthly copies.

For example: Home Assistant keeps seven daily copies in managed locations. On NAS, you continuously archive copies to achieve 30 daily and 12 monthly; on Google Drive, similarly 14 daily and 6 monthly. **Without this extra step, there would only be those seven everywhere.** If you want everything automatic, you need a tool that actually supports this archival plan.

### How much space to prepare

Find the size of one typical backup and multiply it by the number of planned copies. At a size of 1 GB, the estimate is roughly:

- Home Assistant: 7 GB.
- NAS: up to approximately 42 GB for the stated plan.
- USB: up to approximately 20 GB.
- Google Drive: up to approximately 20 GB.

This is a rough estimate without growth and with the possibility of overlap between daily and monthly copies. Prepare a reserve and consider other files. NAS and USB are two alternatives for a second location; you do not need to acquire both.

## The Encryption Key Must Be Kept with the Backup

An encrypted backup can only be restored using the corresponding key. Store the emergency set, for example, in a password manager that you can access even without Home Assistant. Do not publish the key.

Caution regarding manually downloaded files: when downloading via the Home Assistant backups page, the backup is decrypted according to the documentation. Do not upload such a file to a public directory; if you wish to keep it encrypted, use suitable secure storage or encrypt it separately.

## How do you know the plan works?

Periodically ask yourself these questions:

- Do I see a fresh backup directly in Home Assistant, on NAS, USB, or Google Drive?
- Are the planned weekly or monthly copies also preserved?
- Can I log into Google Drive and find the backup, even if Home Assistant is down?
- Do I have the corresponding key and login credentials available?
- Do I know which parts of the home the backup includes?

True verification is a test restore on spare equipment. First, keep the restored system separate from the actual home devices so that it does not start running the same rules simultaneously. Do not perform a restore on a live home system just for testing: it would overwrite its configuration.

## Common Mistakes

- **"I have three backups on one disk."** They help in reverting to an older version, but they won't help if this disk fails.
- **"My NAS is outside Home Assistant, so it's outside the home."** It can still be affected by the same event as the rest of the household.
- **"I no longer need to check automatic backups."** The storage may be unavailable or full.
- **"A backup file means I can restore."** You also need access to the file, the key, and a usable restoration procedure.

## Sources and further reading

- [Home Assistant: explanation of the 3-2-1 rule](https://www.home-assistant.io/blog/2025/01/03/3-2-1-backup/)
- [Current backup and restore documentation](https://www.home-assistant.io/common-tasks/general/)
- [Official Google Drive integration](https://www.home-assistant.io/integrations/google_drive/)
- [Our basic backup guide](/help/backups/)
