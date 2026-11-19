---
title: 'Restoring from a backup: You don''t have to set up your home again'
description: How to revert after a failed change or restore Home Assistant on a spare device.
cas: 10 minutes reading; allow at least an hour for the actual restore
obtiznost: Step by step
kontrola_zdroju: '2026-09-30'
stav: Based on documentation
temata:
- Backups
- Restoring
translationKey: "help.restoring-a-backup"
---

## If Something Goes Wrong, Start Calmly

Something isn't working after an update, a disk goes down, or the entire device stops responding. A usable backup can save you from reconfiguring your entire home. You will restore the saved state and then check the connected devices.

**Restoring reverts the state to the moment the backup was taken.** Changes made afterward are not included. The goal is to save what was actually backed up; no backup promises protection against every single situation.

This guide is focused on **Home Assistant OS**, such as the [Home Assistant Green](/buying-guide/home-assistant-green/). For a different type of installation, use the corresponding documentation.

## Select your scenario

| What happened | Next steps |
| --- | --- |
| You opened Home Assistant, but need to revert a change | Restore on the current device |
| The original device is broken or the system cannot be started | Restore on a clean installation or replacement device |
| Only one device is not responding | First [basic troubleshooting](/help/device-not-responding/) |

An internet outage or a dead sensor battery is usually not a reason to restore the entire home.

## What to prepare

- **A suitable backup.** Select a copy from a time when the home was functioning, and keep the original.
- **The corresponding encryption key**, if the file is encrypted. You can find it in the stored emergency kit.
- **Login credentials valid at the time of the backup.** Newer account changes may be lost after restoration.
- **A computer with access to the backup**, a home network, and enough time.
- If the main device fails, also have a **replacement device with pre-installed Home Assistant OS**, sufficient storage, and the original available radio adapters.

The size of the backup file does not indicate how much space the restored installation will require. Follow the requirements in the restore documentation.

## Where to retrieve a backup when Home Assistant is unavailable

In our [3-2-1 backup plan](/help/3-2-1-backups/), we store copies directly in HA, on a local NAS or USB drive, and offsite, for example on Google Drive.

If you cannot access HA:

1. On a computer, open the NAS or connect the backup USB drive.
2. Alternatively, log directly into Google Drive and locate the Home Assistant backup folder or your separate archive.
3. Download the selected file to the computer. Check the date, size, and completion of the transfer.

To obtain a cloud copy, you do not need to re-enable the integration in HA first. You need access to the account, the file, and any necessary key. Do not unpack or modify the backup before uploading it.

## Option A: Restore on the current device

1. Navigate to **Settings → System → Backups** and select the appropriate backup.
2. Check its contents and select the parts to restore. For the entire saved state, select all necessary parts.
3. Confirm the restore and allow it to complete.
4. After returning to the login screen, use the credentials valid at the time of the backup.

The restore will overwrite the selected parts of the current installation. If the system still allows it, save its current state beforehand in case of further comparison.

## Variant B: Original device is not working

1. Prepare the replacement device according to the [installation guide](https://www.home-assistant.io/installation/).
2. Disconnect the original system so that two installations do not control the home simultaneously.
3. Connect the available original Zigbee or Z-Wave adapter, if you are using one.
4. On the initial screen of a clean installation, select **Restore backup / Upload backup** and choose a file from your computer.
5. Select the parts to restore, optionally enter an encryption key, and start the restore.
6. After completion, log in with the original credentials.

Do not refresh the page or disconnect the power during restoration. Temporary loss of control is expected; speed depends on the installation, device, and network.

## What you can get back and what you must check

Only the content included in the specific backup and selected during the restore will be recovered. A partial backup or excluded media may not contain everything you expect.

The HA backup is also not a copy of the entire home. Standalone files on a NAS, router settings, or device software may require their own backup plan.

When replacing a Zigbee or Z-Wave radio, a special network migration may be necessary. Do not immediately re-pair all sensors: first verify the procedure for your specific connection and adapter. External services may also require re-authentication.

## After restoration: test your home thoroughly

Before marking the restoration as complete:

- Verify lights, heating, and other important controls.
- Test automations with their actual triggers.
- Check notifications and household member access.
- For battery sensors, wait for further reports or wake them up according to the manufacturer's instructions.
- Verify NAS, Google Drive connections, and backup retention settings.
- Create a new backup of the working state and verify its copy.

Keep older verified copies until you have also tested less frequent rules. Some issues may only appear in the morning or during the next scheduled run.

## When restoration fails

**Missing key:** Look for a corresponding emergency set or another available unencrypted copy. Encryption cannot be bypassed with a new account password.

**File cannot be loaded:** Download it again, or use a copy from another location. Keep the other backups.

**Insufficient space:** Select a more suitable target storage. A small compressed file can take up significantly more space after restoration.

**Control does not return:** Verify that the restoration has finished, the power, and the assigned network address. When requesting help, prepare the device model, backup date, and exact error.

## Prepare a recovery plan in advance

Note the location of copies, where you keep the key, how you access the Google account, and which adapter you use, in a safe place. Store passwords in a password manager, not in a public note.

Periodically perform a test recovery on an isolated installation without access to the actual home devices. Only this way do you verify the usability of the backup, not just the existence of the file.

## Sources and further reading

- [Official Home Assistant restore procedure](https://www.home-assistant.io/common-tasks/general/#restoring-a-backup)
- [Emergency kit and encryption key](https://www.home-assistant.io/more-info/backup-emergency-kit/)
- [Installation on a backup device](https://www.home-assistant.io/installation/)
- [3-2-1 backup and retention](/help/3-2-1-backups/)
- [Updating Home Assistant](/help/updating-home-assistant/)
