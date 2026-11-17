---
title: 'Google Calendar in Home Assistant: OAuth, multiple calendars, and notifications'
seoTitle: 'Google Calendar and Home Assistant: OAuth and automation'
description: 'A practical guide to Google Calendar in Home Assistant: OAuth, multiple calendars, 15-minute event notifications, and troubleshooting.'
cas: 15 minutes read
obtiznost: Medium
kontrola_zdroju: '2026-11-12'
stav: Based on documentation
sourceType: official-docs
obrazek: /assets/images/google-calendar-home-assistant.png
obrazek_alt: Calendar connected via secure OAuth access with notification and smart home
temata:
- Google Calendar
- Integration
- OAuth
- Automation
- Notifications
related:
- getting-started/devices-entities-and-integrations
- help/automation-not-working
- help/internet-outage
translationKey: "integrations.google-calendar-home-assistant"
---

The **Google Calendar** integration connects Google Calendar with Home Assistant. Each calendar from the "My calendars" section can obtain its own entity, for example `calendar.family`. You can then view events in the Calendar overview and trigger automations based on their start or end time—for instance, sending a notification 15 minutes before a meeting or preparing the house for a recurring event.

This is an official integration, not an HACS add-on. If you do not want to send calendar data to Google, use Home Assistant's local calendar.

## How the Connection Works

Home Assistant queries the Google Calendar API over the internet. You approve access using **OAuth 2.0**: Home Assistant does not know the account password, but receives a token for reading, or writing, to calendars.

The integration is cloud-based. Home Assistant requires the internet, and an outage of the Google API, DNS, or connection may delay updates. Event name, time, description, and location can be used in automation, so do not enter data into the calendar that you do not want to have simultaneously with Google and Home Assistant.

## Prerequisites

- A Google account with at least one calendar in the **My calendars** section,
- Home Assistant with a functional internet connection,
- Access to the Google Cloud Console,
- A Google Cloud project with the **Google Calendar API** enabled,
- An OAuth client of type **Web application** and its Client ID and Client Secret,
- The correct time zone set in both Google Calendar and Home Assistant.

Special hardware is not required. Corporate or school Google Workspace may restrict API access; in this case, ask the administrator or use a different account.

## 1. Creating OAuth credentials in Google

Home Assistant now recommends web OAuth credentials. Do not create a Desktop client or the older Device Authorization.

1. In the [Google Cloud Console](https://console.cloud.google.com/), create or select a project dedicated to Home Assistant.
2. Open **Google Calendar API** and select **Enable**.
3. In the **Google Auth Platform → Branding** section, start the setup. For the application name, you can use 'Home Assistant' and add your contact email.
4. Select **External** as the public type. On the Branding page, set the homepage, privacy policy, and terms address to `https://home-assistant.io` and add `home-assistant.io` to the authorized domains.
5. In the **Audience** section, change the application status to production. In Testing mode, add the account as a test user, but the token usually expires after seven days.
6. In the **Clients** section, create a **Web application** client.
7. In **Authorized redirect URIs**, enter exactly `https://my.home-assistant.io/redirect/oauth`. This is not a placeholder or your server's address.
8. Save the displayed **Client ID** and **Client Secret** in a password manager. Do not include the Secret in articles, screenshots, or public repositories.

The new credentials may take several hours to become active. The production status of the personal client is important mainly due to the seven-day expiration of the test token.

## 2. Adding the integration in Home Assistant

1. Open **Settings → Devices & Services**.
2. Select **Add integration** and search for **Google Calendar**.
3. When Home Assistant prompts you, enter the Client ID and Client Secret. Only save these within your installation's interface.
4. Select the correct Google account and proceed with the OAuth consent. Google may display a warning for a personal application; only continue with the project you created.
5. On the **Link account to Home Assistant?** page, verify the listed address of your instance and confirm the linking.
6. Upon returning to Home Assistant, open the integration and verify the created calendar entities.

The integration is added via the UI. The older `google_calendars.yaml` is for existing installations from before Home Assistant 2022.6 and is not recommended for new users. Filter events using an automation condition.

## Multiple Calendars and Permissions

Each calendar from the **My calendars** section will receive a separate entity. The "Family" calendar might be `calendar.family`, but always verify the actual ID in **Settings → Devices & Services → Entities**. Turn off any unnecessary entities. For shared calendars, the permissions are determined by Google.

Read-only access is sufficient for running automations. The `google.create_event` action only appears with read and write access; changing this may require new authorization.

The entity displays the ongoing and the nearest event. Therefore, do not use its `message` attribute in an automation due to potential overlaps; the correct event is provided by `trigger.calendar_event`.

## Example 1: Notification 15 minutes before an event

First, find the phone service in **Developer Tools → Services**. In this example, replace `notify.mobile_app_muj_telefon` with your actual service and `calendar.rodina` with your own calendar. Insert the entire block into the YAML editor of a new automation.

```yaml
alias: Calendar – Notification 15 minutes before
triggers:
  - platform: calendar
    event: start
    entity_id: calendar.rodina
    offset: "-00:15:00"
condition: []
action:
  - service: notify.mobile_app_muj_telefon
    data:
      title: "In 15 minutes"
      message: >-
        {{ trigger.calendar_event.summary }}
        {% if trigger.calendar_event.location %}
        – {{ trigger.calendar_event.location }}
        {% endif %}
mode: parallel
max: 10
```

The trigger reacts 15 minutes before the start of every event in the selected calendar. The conditions are empty, so you will always receive the notification. The action uses the name and any location directly from the event that triggered it. The `parallel` mode allows processing multiple events with the same start time; therefore, the calendar documentation does not recommend the `single` mode.

Home Assistant loads calendars approximately every 15 minutes. Therefore, plan your test event at least 30 minutes in advance.

For multiple calendars, add another trigger with the same offset and a different `entity_id`. You can determine the source calendar using `trigger.entity_id`.

## Example 2: Logging completed laundry to the calendar

This example requires the integration to have write permissions and for a washing machine sensor to exist with the value `finished`. Verify the actual value in **Developer Tools → States**. Replace the sensor, the calendar, and the entire block when adding it to a new automation in the YAML editor.

```yaml
alias: Calendar – Log finished laundry
triggers:
  - platform: state
    entity_id: sensor.washing_machine_status
    to: "finished"
conditions: []
actions:
  - service: google.create_event
    data:
      summary: "Laundry finished"
      start_date_time: "{{ now().strftime('%Y-%m-%d %H:%M:%S') }}"
      end_date_time: >-
        {{ (now() + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S') }}
      description: "Record created by Home Assistant."
mode: queued
```

The trigger reacts to the `finished` state. The action will create a one-minute event as a history record; the `queued` mode will preserve the order of concurrent entries.

If you do not see the `google.create_event` action, enable read and write permissions for the integration. Only log shared data to the family calendar.

## What the integration provides and what it doesn't

You get calendar entities, overview, start and end triggers with offset, dates for templates, and, if enabled, an action to create an event.

Home Assistant does not replace Google Calendar. Handle sharing, guests, video calls, and complex recurrence with Google. Entity names are derived from your calendars; examples are not universal IDs.

An all-day event starts at the beginning of the day and its end is represented by the following day. Before controlling heating or locks, test both regular and all-day events.

## Security and Privacy

*   Back up and protect Client Secrets and OAuth tokens like a password; do not send them to an issue or public repository.
*   Only enable read access if you do not need to create events.
*   Do not send sensitive names, locations, or event descriptions to mobile notifications, voice assistants, or logs without careful consideration.
*   With a shared calendar, be aware that events created by Home Assistant will be visible to other members as well.

Access can be revoked in your Google account; changing security settings may require re-authorisation.

## When the integration fails

- **Invalid client or redirect URI mismatch:** verify the web client type and the exact address `https://my.home-assistant.io/redirect/oauth`, including HTTPS and without a custom domain.
- **Access blocked:** In Testing mode, add the account among the test users. A Workspace administrator may block access.
- **Integration unavailable after seven days:** The OAuth application was likely left in Testing mode. Switch it to production status and re-link the account.
- **Authentication code expired:** Restart the integration setup and complete the entire consent process without delay.
- **Calendar is missing:** Check if the selected account can see it in the "My Calendars" section of Google and if its entity is not disabled.
- **Automation did not trigger:** Create a test event more than 15 minutes in advance, verify the time zone, and open the automation trace.
- **The notification has a different event:** Use `trigger.calendar_event.summary` in the template, not the `message` attribute of the calendar entity.
- **Cannot create event:** Enable read and write access for the integration and verify that the account is allowed to write to the target calendar.

If you encounter difficulties, open **Settings → System → Logs**. Incorrect Client ID or Secret can be removed and re-entered in the application credentials. Before deleting the integration, note down the entity names.

## Advantages, disadvantages, and alternatives

The advantage is linking the family calendar to the home, separate entities for multiple calendars, and triggers for overlapping events.

The disadvantage is more complex initial setup in Google Cloud, dependency on the internet, and handing over calendar data to a cloud service. Polling also means that an event created shortly before the start might not trigger the automation in time.

For a purely local calendar without the cloud, use **Local Calendar**. For a public or shared read-only calendar, **Remote Calendar** may be suitable if you have its iCalendar URL and limited write options are acceptable. The choice mainly depends on where the data must originate and who is allowed to read it.

## Sources

- [Home Assistant: Google Calendar integration](https://www.home-assistant.io/integrations/google/)
- [Home Assistant: calendar integrations and automations](https://www.home-assistant.io/integrations/calendar/)
- [Home Assistant: event started trigger](https://www.home-assistant.io/triggers/calendar.event_started/)
- [Home Assistant: action Create event in Google Calendar](https://www.home-assistant.io/actions/google.create_event/)
- [Google: OAuth 2.0 for API access](https://developers.google.com/identity/protocols/oauth2)
- [Google Calendar API: OAuth scopes](https://developers.google.com/workspace/calendar/api/auth)
