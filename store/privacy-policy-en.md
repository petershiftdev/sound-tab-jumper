# Privacy Policy — Find Tab Playing Sound

**Last updated:** 20 September 2026

This policy describes how the Chrome and Firefox extensions **Find Tab Playing Sound** (“the Extension”) handle information.

## Who provides the Extension

The Extension is published by **PeterShift**.  
Contact: **petershift.dev@gmail.com**

## What the Extension does

The Extension switches the browser to the next open tab that is currently playing sound. You can trigger this with the toolbar icon or with the keyboard shortcut.

## Data the Extension accesses

To find tabs that are playing sound, the Extension reads, **in the browser only**, whether an open tab is currently audible (`audible`). It may also use the tab identifier and window identifier so it can activate that tab. The Extension does **not** request the `tabs` permission, so it cannot read tab URLs, titles, or favicons.

The Extension does **not** read the content of web pages.

## What we do not collect

The Extension does **not**:

- collect names, emails, account data, or other personal information;
- store tab URLs, titles, or browsing history;
- send any data to a server operated by the developer;
- use analytics, advertising, crash reporting, or cookies;
- sell or share user data with third parties.

There is no developer backend and no user account.

## How information is used

Tab information is kept in memory only for as long as needed to jump to the next audible tab (including a short in-memory cycle of audible tabs). It is discarded when that action finishes or when the background worker or event page stops. Nothing is written to extension storage, disk, or the network for this purpose.

## Permissions

| Permission | Why it is requested |
| --- | --- |
| None declared | The Extension does not declare any extra permissions. Finding audible tabs and switching to them does not require the `tabs` permission. |

## Remote code

The Extension runs only the local files shipped in the Chrome Web Store or Firefox Add-ons package. It does not download or execute remote JavaScript.

## Children

The Extension is not directed at children and does not knowingly collect data from anyone, including children.

## European Economic Area and California

The Extension does not collect personal data, so it does not sell personal information and does not process personal data on a server. Installing the Extension in the browser is handled by Google or Mozilla under their own policies.

## Changes

If data practices change, this policy will be updated and the Chrome Web Store and Firefox Add-ons privacy disclosures will be updated before that version is published.

## Contact

Questions about this policy: **petershift.dev@gmail.com**
