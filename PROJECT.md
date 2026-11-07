# Project facts — Find Tab Playing Sound

Source of truth for names, contact, listing copy, and current package facts.
Russian copy: `PROJECT-ru.md`. If any of this changes, update **both** files in the same change.

**Last updated:** 7 November 2026 (Romanian privacy policy)

---

## Publisher

| Field | Value |
| --- | --- |
| Display name (Chrome Web Store / privacy policy) | PeterShift |
| Public contact email | `petershift.dev@gmail.com` |
| Trader status | Non-trader (personal free project) |
| Developer Dashboard fee | Paid ($5) |

This email is public: Chrome Web Store listing and the hosted privacy policy.
Use the same address in the dashboard **Contact email** field.

---

## Product

| Locale | Name | Short description (max 132) | Toolbar tooltip | Shortcut description |
| --- | --- | --- | --- | --- |
| en | Find Tab Playing Sound | Find which tab is playing audio and switch to it. Click or shortcut to cycle sound tabs. | Go to the tab playing sound | Go to the next tab playing sound |
| ru | Найти вкладку со звуком | Находит вкладку, которая сейчас играет звук, и сразу переключает на неё. | Перейти к вкладке со звуком | Перейти к следующей вкладке со звуком |
| de | Tab mit Ton finden | Findet den Tab, der gerade Ton wiedergibt, und wechselt dorthin. Klick oder Tastenkürzel schaltet zwischen Ton-Tabs um. | Zum Tab mit Ton wechseln | Zum nächsten Tab mit Ton wechseln |
| es | Encontrar la pestaña con sonido | Encuentra la pestaña que reproduce audio y cambia a ella. Clic o atajo para recorrer las pestañas con sonido. | Ir a la pestaña con sonido | Ir a la siguiente pestaña con sonido |
| fr | Trouver l'onglet avec du son | Trouve l'onglet qui lit du son et y bascule. Un clic ou un raccourci parcourt les onglets avec du son. | Aller à l'onglet avec du son | Aller à l'onglet suivant avec du son |
| pt_BR | Encontrar a aba com som | Encontra a aba que está tocando áudio e muda para ela. Clique ou atalho para percorrer as abas com som. | Ir para a aba com som | Ir para a próxima aba com som |
| uk | Знайти вкладку зі звуком | Знаходить вкладку, яка зараз відтворює звук, і одразу перемикає на неї. Клік або комбінація гортає такі вкладки. | Перейти до вкладки зі звуком | Перейти до наступної вкладки зі звуком |
| zh_CN | 查找正在播放声音的标签页 | 查找正在播放音频的标签页并切换过去。点击图标或按快捷键，可在有声音的标签页之间循环。 | 转到正在播放声音的标签页 | 转到下一个正在播放声音的标签页 |

**One-line purpose (Privacy tab):** Switch to the next open browser tab that is currently playing sound.

**Detailed listing copy:** Chrome — `store/listing-<locale>.md`. Firefox — `store/listing-firefox-<locale>.md`. Locales: `en`, `ru`, `de`, `es`, `fr`, `pt_BR`, `uk`, `zh_CN`. Paste the Spanish copy into Chrome’s Español (Latinoamérica) listing as well; extension strings for that UI come from `es`.

---

## Package

| Field | Value |
| --- | --- |
| Repo / folder | `sound-tab-jumper` |
| Chrome extension root (load unpacked / ZIP contents) | `01/` |
| Firefox extension root (temporary load / AMO ZIP contents) | `firefox/` |
| Manifest | V3, `default_locale` `en`, version **1.2** (both packages) |
| Locales shipped | `en`, `ru`, `de`, `es`, `fr`, `pt_BR`, `uk`, `zh_CN` |
| Permissions | none (no `permissions` in either manifest) |
| Keyboard shortcut | Ctrl+Shift+S (Cmd+Shift+S on Mac), command `jump-to-sound-tab` |
| Chrome upload ZIP | `jump-to-sound-tab.zip` (rebuild from `01/`; do not keep older zip names) |
| Firefox upload ZIP | `jump-to-sound-tab-firefox.zip` (rebuild from `firefox/`) |
| Firefox add-on ID | `@find-tab-playing-sound` |

---

## Chrome Web Store

| Field | Value |
| --- | --- |
| Category | Functionality & UI |
| Price | Free |
| Visibility | Public |
| Regions | All |
| Mature content | No |
| Item URL | https://chromewebstore.google.com/detail/find-tab-playing-sound/djhgnhefakcclbpcciijegaaflkmaknd |
| Item ID | `djhgnhefakcclbpcciijegaaflkmaknd` |
| Homepage / Support / Official URL | none |
| Privacy policy URL | https://petershiftdev.github.io/sound-tab-jumper/ (source: `store/privacy-policy.html`). One language per address: `#en`, `#ru`, `#de`, `#es`, `#fr`, `#pt_BR`, `#ro`, `#uk`, `#zh_CN`. The bare URL opens the browser language. |

Dashboard copy: Privacy → `store/privacy-practices.md`; Distribution / test instructions → `store/distribution.md`; publish steps → `store/PUBLISH.md`. After ZIP: `Instructions/chrome-web-store-after-zip.md`. Host policy: `Instructions/github-pages-privacy-policy.md`.

---

## Firefox Add-ons (AMO)

| Field | Value |
| --- | --- |
| Category | Tabs |
| Price | Free |
| Visibility | Listed / public (submitted, awaiting review) |
| Add-on URL | https://addons.mozilla.org/firefox/addon/find-tab-playing-sound/ |
| Add-on ID | `@find-tab-playing-sound` |
| Minimum Firefox | 109.0 (desktop; Android not listed) |
| Data collection | `none` (`browser_specific_settings.gecko.data_collection_permissions`) |
| Privacy policy URL | https://petershiftdev.github.io/sound-tab-jumper/ (source: `store/privacy-policy.html`). One language per address: `#en`, `#ru`, `#de`, `#es`, `#fr`, `#pt_BR`, `#ro`, `#uk`, `#zh_CN`. The bare URL opens the browser language. |

Listing copy: `store/listing-firefox-<locale>.md` for the locales above. Publish steps: `store/PUBLISH-firefox.md`.

---

## Store graphics

| Asset | Size | Location |
| --- | --- | --- |
| Extension / store icon | 16 / 32 / 48 / 128 | `01/icons/` (Chrome); copy in `firefox/icons/` |
| Screenshots | 1280×800 | `screenshots/` |
| Small promo tile | 440×280 (required) | `promo/` |
| Marquee | 1400×560 (optional) | `marquee/` |
