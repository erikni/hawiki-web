---
title: 'Cameras in Home Assistant: Local with Frigate'
description: Image, recording, and person detection without reliance on manufacturer cloud. How RTSP and ONVIF help.
obrazek: /assets/images/kamery-frigate.png
obrazek_alt: Illustration of an IP camera connected to a local server and a detected person overview.
cas: 6 minutes read
obtiznost: Next step
kontrola_zdroju: '2026-10-06'
stav: Based on documentation
temata:
- Cameras
- Frigate
- RTSP
- ONVIF
- Local operation
translationKey: "guides.frigate-cameras"
---

## Camera, Frigate, and Home Assistant
**Frigate** is an open-source Network Video Recorder (NVR): it records footage and detects people or cars at home. HA receives the image and sensors for automation. With a local stream, you do not need the manufacturer's cloud; remote access may require the internet.

**RTSP** transmits live video. **ONVIF** helps with discovery and supported camera control, including pan, tilt, and zoom (PTZ). You can combine brands, but not every camera can do everything. For basic RTSP recording in Frigate, ONVIF is not necessary; automatic PTZ tracking requires specific supported features.

## What Frigate can do
- **Motion detection** looks for changes in the image and selects areas for recognition. Motion itself does not mean a person.
- **Object detection** distinguishes, for example, a person from a car based on the model used.
- **Zones** define an entrance or driveway. You can limit an event to a person entering the zone; the position is determined by the bottom centre of the object's bounding box.
- **Motion masks** suppress distracting areas, such as a clock. They are not a guarantee that an object will never be detected in them.
- **Recordings and snapshots** allow you to review events; you can set storage and retention time. It also supports live view, multi-camera overview, and supported PTZ tracking.

## Examples of Cameras and Brands
**EU: [Shelly Camera Black](https://www.shelly.com/products/shelly-camera-black)** from a group based in Bulgaria offers a local RTSP stream. It does not support ONVIF specifications.

**USA: [Ubiquiti UniFi Cameras](https://eu.store.ui.com/eu/en/category/all-physical-security)**. For the G5 series and newer, according to Frigate, you require a **UniFi Protect** server to access the stream; therefore, it is not always a direct RTSP connection from the camera.

A cheaper alternative may be **[TP-Link Tapo](https://www.tp-link.com/us/support/faq/4465/)** with RTSP/ONVIF support on selected models. The brand originated in China; international TP-Link lists headquarters in the USA and Singapore and a division from the Chinese company. Always verify compatibility for the specific model and firmware.

## What you need at home
Frigate runs as an application in HA OS or in Docker on another computer. It requires disk space for recordings and performance for video decoding and detection. Start with one camera according to the [installation guide](https://docs.frigate.video/frigate/installation/). Set the actual RTSP address, detection, and storage, and verify the image.

For easy compatibility, choose **H.264**, and AAC for audio. The advantage is two streams: a higher quality one for recording and a smaller one for detection at around **5 frames per second**.

## Connecting to Home Assistant
1. Enable an MQTT broker, such as Mosquitto, and set up the **MQTT** integration in HA. Frigate must have MQTT enabled and use the same broker.
2. Download the **Frigate** integration via [HACS](/more-options/hacs/) and restart HA. This does not install the video recorder itself.
3. In **Settings → Devices & Services → Add Integration**, select Frigate and enter the address of its instance according to your installation method.

You will receive camera entities, object sensors, and access to recordings.

## Example: person at the entrance
It is assumed that a functional integration and its binary sensor for person detection are available. In the new automation, open **Edit in YAML** and paste the entire example. Replace `binary_sensor.vchod_person_occupancy` with your actual entity. The notification will appear within HA.

```yaml
alias: Frigate – person at the entrance
triggers:
  - trigger: state
    entity_id: binary_sensor.vchod_person_occupancy
    from: "off"
    to: "on"
conditions: []
actions:
  - action: persistent_notification.create
    data:
      title: Camera at the entrance
      message: Frigate detected a person at the entrance.
mode: single
```

## Sources
- [Frigate: project and features](https://github.com/blakeblackshear/frigate)
- [Frigate: integration with Home Assistant](https://docs.frigate.video/integrations/home-assistant/)
- [Frigate: installation](https://docs.frigate.video/frigate/installation/)
- [Frigate: camera and stream setup](https://docs.frigate.video/frigate/camera_setup/)
- [Frigate: ONVIF and auto-tracking](https://docs.frigate.video/configuration/autotracking/)
- [Home Assistant: ONVIF](https://www.home-assistant.io/integrations/onvif/)
- [Home Assistant: MQTT](https://www.home-assistant.io/integrations/mqtt/)
- [Home Assistant: automation triggers](https://www.home-assistant.io/docs/automation/trigger/)
- [Home Assistant: persistent notifications](https://www.home-assistant.io/integrations/persistent_notification/)
- [Shelly Camera Black: specifications](https://www.shelly.com/products/shelly-camera-black)
- [Shelly: corporate headquarters](https://corporate.shelly.com/en/page/impressum)
- [Ubiquiti: camera offerings](https://eu.store.ui.com/eu/en/category/all-physical-security)
- [Ubiquiti: contact](https://www.ui.com/contact/)
- [Frigate: UniFi camera specifics](https://docs.frigate.video/configuration/camera_specific/)
- [TP-Link Tapo: RTSP and ONVIF](https://www.tp-link.com/us/support/faq/4465/)
- [TP-Link: corporate restructuring](https://www.tp-link.com/us/press/news/21130/)
- [Frigate: motion detection](https://docs.frigate.video/configuration/motion_detection/)
- [Frigate: zones](https://docs.frigate.video/configuration/zones/)
