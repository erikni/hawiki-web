---
title: 'Updating Home Assistant: Why wait for version .2'
description: For a typical household, we recommend skipping versions .0 and .1. How to choose the right time, prepare a backup, and verify the result.
cas: 8 minutes read
obtiznost: Easy
kontrola_zdroju: '2026-09-30'
stav: Editorial recommendation; follow the documentation
temata:
- Updates
- Maintenance
translationKey: "help.updating-home-assistant"
---

## A New Version Does Not Mean You Must Update Immediately

Home Assistant announces a new version. You might be tempted to click update and be done with it. However, if your home is functioning well, you can first choose a suitable time and read about the changes.

**For routine monthly updates, we recommend skipping the initial `.0` release and the first patch version `.1`. Consider upgrading starting from `.2`.** This is our rule for smoother home operation, not a guarantee of a flawless update.

This article concerns **Home Assistant Core**, which is the main program. The operating system, applications, community add-ons, and individual device software have their own versioning and update procedures.

## How to understand the version number

Home Assistant Core uses a version designation in the format **year.month.patch**. The designation `YYYY.MM.0` means the first release in the given month, and `YYYY.MM.1` is the first patch release.

The following numbers are examples, not recommendations for a specific current version:

| Version | What it means | Our usual procedure |
| --- | --- | --- |
| `2026.9.0` | First September release | Wait for a regular upgrade |
| `2026.9.1` | First patch release | Wait longer and monitor for patches |
| `2026.9.2` | Second patch release | Start considering migration based on changes and your setup |
| `2026.9.3` and later | Further patch release | Choose a suitable release based on notes and known issues |

In real designations, the month may be without a leading zero, for example `9` instead of `09`.

## Why We Omit .0 and .1

Monthly releases bring changes and new features. The following patch release fixes bugs. Waiting allows time for further fixes and for experiences from various homes.

Versions `.0` and `.1` are **stable releases, not beta versions**. Home Assistant tests and officially recommends the monthly release. Our recommendation is a safer choice for a home that prioritises predictable operation over the immediate use of new features.

Even `.2` does not guarantee that your specific heating, lighting, or community integration works. The decision must also include changes that affect you specifically. Do not postpone maintenance indefinitely: choose a regular date when you will assess updates.

## When to update sooner

The "wait for .2" rule has exceptions:

- **Critical security fix that affects you.** Follow the announcement and recommended procedure; the version number itself is no reason to delay the fix.
- **Fixing a problem you already have at home.** If the new release addresses a non-functional critical feature, it may make sense to update sooner.

In both cases, you still need a backup and time for verification. If a specific new feature just seems interesting, it is usually not a reason to rush.

## Want to try the beta version?

Beta is a testing release of the upcoming version. You can try out new features and help find bugs. For a typical household that requires reliable heating or lighting, we recommend staying on stable releases. It is best to test the beta on a separate test installation.

### How to enable the beta channel

In Home Assistant OS:

1. First, create a backup of the current stable version and store it off-device.
2. Open **Settings → System → Updates**.
3. Open the **three dots** menu in the top right corner.
4. Select **Join beta channel**; in English, **Join beta**.
5. Check the offered version and then run the Home Assistant Core update.

If the option does not appear, select check for updates. Item names may vary slightly depending on the language and version. The beta channel may change the update offerings for other managed components, so always read which component you are updating. For container installations, the test version is selected using a different procedure; this guide is for Home Assistant OS.

### How to return to a stable release

You leave the beta channel in the same updates menu. **Changing the channel does not automatically reinstall the installed beta to an older stable version.** You can wait for a suitable stable release, or if necessary, follow the procedure of restoring a previous backup. Therefore, keep a backup from the stable version.

You can also try selected upcoming options in **Settings → System → Labs**. Labs is a different feature than installing the entire program's beta version.

## What about updating integrations and other components?

An integration means connecting Home Assistant to a device or service. Updating the connection and updating the device itself are two different things.

| What you are updating | Where the update comes from | Does the "wait for .2" rule apply? |
| --- | --- | --- |
| **Built-in integrations** | Are part of the Home Assistant Core release | Yes, as part of our Core recommendation |
| **Community integrations and UI elements from HACS** | From the author's own project, managed via HACS | No; they have their own versions and requirements |
| **Applications, previously called add-ons** | From their own repository in the add-on store | No; assess each one individually |
| **Home Assistant OS and Supervisor** | From their own update system | No; they do not use the same monthly numbering as Core |
| **Smart device software** | From the manufacturer, sometimes also available via Home Assistant | No; follow the specific device's documentation |

### Built-in integrations

For example, an integration that is part of standard Home Assistant is usually updated with the Core. You do not need to look for a separate button to install a new version of the integration. Changes in the Core release notes may therefore affect your lights or backup.

The **Reload** button on an integration only reloads the connection. It does not install newer code itself.

### Community integrations from HACS

Every project has its own release rules. The designation `1.0` or `2.1` for a community integration is not the same as the monthly version `.0` and `.1` of Home Assistant Core. Therefore, do not refuse an update just because of the last number.

Before installing, read the changes, the required Core version, and any restart instructions. Update one extension and test its functionality. If the author offers a test release, it is selected separately via the HACS options and the specific project; the Home Assistant beta channel does not automatically enable it.

**The update order depends on the author's requirements.** Some new versions of extensions require a newer Core first, while others are best updated before switching to a new Core. If a suitable compatible version is not yet available and you need the integration, postpone the regular upgrade.

### Applications and device software

Here too, read the change information and available rollback options. A Home Assistant backup may not restore the previous software for a bulb, thermostat, or other standalone box. Therefore, do not rely on HA restoration to revert every update in the home.

For critical components, such as a sensor connecting service, we recommend a planned manual update followed by a check. If you use automatic updates, consider whether you have an overview of what has changed and how you will verify the result.

## Before updating: prepare a rollback path

1. **Read the release notes.** Look for your devices, used integrations, and configuration changes requiring adjustment. If skipping multiple months, review the missed monthly releases as well.
2. **Check community integrations.** If you use HACS, check the requirements and known issues of important projects.
3. **Create a fresh backup before upgrading.** Verify its completion, a copy off the main device, and the availability of the encryption key. Do not rely only on an old entry in the list.
4. **Note the original version.** Label the backup with a date and reason, for example, "before September upgrade."
5. **Choose a quiet time.** Update when you are at home and can troubleshoot any issues. Not shortly before leaving or when critical operations depend on the system.

A detailed plan for storing and retaining copies can be found in the [3-2-1 backup article](/help/3-2-1-backups/).

## How to perform an update

For Home Assistant OS, open **Settings** and navigate to the updates overview. Select the **Home Assistant Core** update, read its information, and verify the version it offers.

Once preparation is complete, start the installation and let it run. Control may be temporarily unavailable during the restart. The exact names of the buttons may vary depending on the version and language.

For easier troubleshooting, we recommend changing **one component at a time**. Choose the order based on the requirements of the individual components, and verify functionality between changes. For a different installation, use the procedure from its documentation.

## After updating: Opening the page is not enough

Test several functions that you commonly use:

- Controlling lights from the dashboard and physical buttons.
- A single automation, including an actual trigger.
- Heating, blinds, or any other important function you have at home.
- Mobile notifications and the availability of important devices.
- Backup and transfer to other storage locations.

Also check for reported issues in Settings. Do not delete the previous backup immediately after logging in; keep it to verify normal operation, for example, until the following day. For routines that run once a week, you need to verify this longer cycle as well.

## When something stops working

First, determine if it is a single device, a single connection, or the entire system. Check the release reports and known issues. Do not make several changes at once.

If a rollback is necessary, follow the [official guide to restoring a backup](https://www.home-assistant.io/common-tasks/general/#restoring-a-backup). Restoring will return selected parts to the saved state; changes made after the backup may be lost. Allow yourself time for this.

## Simple Household Rule

**Routine monthly upgrade: Skip .0 and .1, assess changes from .2 onwards, prepare a backup, and update when calm. Handle security fixes according to their severity.**

## Sources and further reading

- [Home Assistant: stable releases and patch versions](https://www.home-assistant.io/faq/)
- [Updating Home Assistant OS and its components](https://www.home-assistant.io/common-tasks/os/)
- [Managing community projects in HACS](https://www.hacs.xyz/docs/use/repositories/dashboard/)
- [Official announcements of new versions](https://www.home-assistant.io/blog/)
- [Backing up using the 3-2-1 method](/help/3-2-1-backups/)
