---
title: 'Sonos in Home Assistant: Installation, Multiroom, and Voice Announcements'
seoTitle: 'Sonos and Home Assistant: Installation, Multiroom, and TTS'
description: 'A practical Czech guide to integrating Sonos with Home Assistant: adding speakers, networks, groups, TTS announcements, and resuming playback.'
cas: 12 minutes read
obtiznost: Intermediate
kontrola_zdroju: '2026-11-04'
stav: Based on documentation
sourceType: official-docs
obrazek: /assets/images/sonos-home-assistant-integrace.png
obrazek_alt: Illustration of Home Assistant connected to three speakers in different rooms
temata:
- Sonos
- Integration
- Multiroom audio
- Voice announcements
- Automation
related:
- getting-started/devices-entities-and-integrations
- help/automation-not-working
- help/internet-outage
translationKey: "integrations.sonos-home-assistant"
---

The **Sonos** integration connects Sonos and IKEA SYMFONISK speakers to Home Assistant. Each speaker will get a `media_player` entity, through which you can control playback and volume, play favorite music, create groups for multiple rooms, or play voice announcements. Communication with the speakers happens on the local network; however, a music service account is still required for services like Spotify.

## Requirements

- A working Sonos system set up in the Sonos app,
- Home Assistant connected to the same local network,
- **UPnP** enabled in Sonos under **Account → Privacy & Security → UPnP**,
- Correctly configured rules between Home Assistant and the speakers for segregated networks or VLANs,
- A configured Text-to-Speech (TTS) service for voice announcements.

Sonos recommends having the app and all products on the same subnet. Home Assistant can handle advanced integration across multiple subnets, but automatic discovery and event reporting depend on the router and firewall settings. The integration runs as **Local Push**: routine control and state changes therefore do not need to pass through the Sonos cloud. However, streamed music or cloud TTS may require the internet.

## Adding Sonos to Home Assistant

1. Open **Settings → Devices & Services**.
2. If Home Assistant detects the Sonos, select **Configure**.
3. If nothing is detected, select **Add integration**, search for **Sonos**, and follow the wizard.
4. Open the added integration and check the devices and entities. Each speaker should have its own entity, for example `media_player.living_room`.
5. In **Developer Tools → Services**, test an action for pausing or changing the volume on one speaker.

The exact entity name is derived from the name of the room or device. Therefore, always replace the IDs in the examples below with the IDs of your own entities. The integration is usually configured via the user interface. YAML is mainly intended for advanced networking scenarios, such as manually listing the IP addresses of the speakers.

## What the integration provides

In addition to basic playback, the control may feature bass, treble, loudness, crossfade, status indicators, or touch buttons, depending on the model. The home cinema can add night mode, speech enhancement, sound delay, and surround speaker settings. Battery models may have a battery and power sensor. Alarms created in the Sonos app are displayed as separate switches.

Not every feature is available on every model or firmware. Older Sonos S1 systems may have limited support for modern announcements. Some changes made outside of Home Assistant are also discovered periodically, so their status may not update instantly.

Favorites from the Sonos app can be played via the media browser. Advanced users can enable the sensor `sensor.sonos_favorites` in the integration page, but the media browser is simpler for general use.

## Multiroom: Joining Speakers into a Group

The `media_player.join` action joins supported players into a synchronized group. The target player becomes the leader, and the other players join it. The `media_player.unjoin` action removes a selected player from the group.

Insert the following complete automation into the YAML editor as a new automation. First, create a **Switch** helper with the ID `input_boolean.hudba_cely_byt`. Replace the three speaker entities. The example only creates the group; you must then start the music on the living room player (the leader).

```yaml
alias: Sonos – music throughout the house
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

To unjoin, create a second automation with a trigger of `to: "off"` and a `media_player.unjoin` action targeting `media_player.kuchyne` and `media_player.loznice`. Only group players that are part of the same Sonos system. A standard group of entities in Home Assistant is not the same as a true synchronized Sonos group.

## Voice announcements without interrupting music

Sonos supports the `announce: true` option in `media_player.play_media`. The announcement will play as an overlay over the current music, the music will be lowered, and upon completion, it will return to its original volume. This is preferable to manually pausing and restarting, if your model and firmware support it.

This example announces an open window for ten minutes. Create a new automation, open **Edit in YAML**, and paste the entire block. Replace the window contact and the speaker. The path `media-source://tts/cloud` assumes an active Home Assistant Cloud; for a different TTS service, use its identifier according to the provider's documentation.

```yaml
alias: Sonos – window open announcement
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

The `volume` value is the announcement volume in the range of 0 to 100, not the entity's usual decimal volume. Home Assistant must be able to provide the created audio file to Sonos, and the speaker must be reachable on TCP port 1443. For TTS, the correct local URL in **Settings → System → Network** is also important. The player may reject a self-signed HTTPS certificate.

## When to use snapshot and restore

The `sonos.snapshot` action saves the current playback, and `sonos.restore` restores it later. This is useful for older devices without reliable `announce` support or for custom sounds that need to genuinely interrupt playback. The `with_group: true` option also saves and restores the group arrangement and the status of other speakers within it.

However, Snapshot **does not save the playlist/queue**. Therefore, do not change it during the interruption. A cloud queue started, for example, directly from Spotify or via Amazon Alexa, cannot be restarted. For standard short announcements, `announce: true` is safer.

Insert the following complete script into a new script in the YAML editor. Replace the speaker ID and the sound address. The file must be directly accessible to the speaker; saving it to `config/www/zvuky/zvonek.mp3` corresponds to the URL `/local/zvuky/zvonek.mp3`.

```yaml
alias: Sonos – doorbell with playback retention
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

Adjust the four-second delay to match the file length. A fixed delay is simple, but it may not be accurate for a file with a variable length. First test the script with low volume and without an important, developed queue.

## Network, VLAN, and Privacy

For rapid status changes, the speakers connect back to Home Assistant on TCP port 1400. If the connection is blocked, the integration switches to slower polling, and Home Assistant will report an issue. If port 1400 is occupied, Home Assistant may try one of the other 100 ports. For `announce` and TTS, Home Assistant must reach every speaker on TCP port 1443.

In segregated VLANs, simply allowing internet access is not enough. Device discovery, UPnP, and two-way communication must be resolved. If automatic discovery is not possible, the speakers' static IP addresses can be specified in `configuration.yaml`. For installations with multiple network interfaces, the **Network** integration allows selecting the interface for automatic discovery. The `advertise_addr` setting is intended for advanced scenarios, such as NAT or a container without a host network.

The integration controls Sonos locally, which limits dependency on the cloud for basic commands. Music services, registration, updates, and some TTS sources may communicate over the internet according to the service's rules. Do not unnecessarily place Home Assistant or Sonos on a publicly accessible network, and do not open the specified ports to the internet.

## When the integration fails

- **Sonos cannot be found:** check UPnP in the Sonos app, ensure they are on the same network, and that Home Assistant can see the local network. Restart the integration first, not the entire system.
- **Error 403 appears during setup:** according to Home Assistant documentation, the cause is often disabled UPnP in the Sonos system.
- **States change slowly:** check that the speakers are reachable on Home Assistant via TCP port 1400. A slower polling method is used if blocked.
- **TTS does not replay:** check TCP 1443 towards the speaker, the local Home Assistant URL, the audio format, and the availability of the TTS service.
- **Notifications do not resume music:** use `announce: true`; do not change the queue in the snapshot and account for the limitation of cloud queues.
- **Group does not play synchronously:** use `media_player.join`, not a general group of entities, and verify that all players belong to the same Sonos system.

To troubleshoot, run the individual action in **Developer Tools → Services** and open its trace in the automation. This separates the integration problem from an error in the automation's trigger or condition.

## Advantages and limitations

The biggest advantage is local control, automatic discovery, support for true Sonos groups, and notifications that won't stop the music. Home Assistant also unifies speakers with sensors, doors, calendars, and other automations.

The disadvantages include higher network requirements when using VLANs, differences between S1/S2 models and firmware, and limited recovery of cloud fronts. Home Assistant also does not replace the Sonos app for initial system setup and adding music service accounts.

## Sources

- [Home Assistant: Sonos integration](https://www.home-assistant.io/integrations/sonos/)
- [Home Assistant: Snapshot action](https://www.home-assistant.io/actions/sonos.snapshot/)
- [Home Assistant: Restore action](https://www.home-assistant.io/actions/sonos.restore/)
- [Home Assistant: Joining media players to a group](https://www.home-assistant.io/actions/media_player.join/)
- [Home Assistant: Text-to-speech (TTS)](https://www.home-assistant.io/integrations/tts/)
- [Sonos: System and network requirements](https://support.sonos.com/en-us/article/sonos-system-requirements)
- [Sonos: Configuring your firewall](https://support.sonos.com/en/article/configure-your-firewall-to-work-with-sonos)
