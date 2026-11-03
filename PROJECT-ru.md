# Данные проекта — «Найти вкладку со звуком»

Источник правды по именам, контактам, текстам витрины и текущему пакету.
Если что-то из этого меняется, обновите этот файл и английский `PROJECT.md` в том же изменении.

**Дата обновления:** 3 ноября 2026 (публичный контактный email)

---

## Издатель

| Поле | Значение |
| --- | --- |
| Отображаемое имя (Chrome Web Store / политика) | PeterShift |
| Публичный контактный email | `petershift.dev@gmail.com` |
| Статус продавца | Не продавец / non-trader (личный бесплатный проект) |
| Взнос Developer Dashboard | Оплачен ($5) |

Этот email публичный: карточка в Chrome Web Store и выложенная политика конфиденциальности.
Тот же адрес укажите в поле **Contact email** дашборда.

---

## Продукт

| Локаль | Название | Краткое описание (до 132) | Подсказка на кнопке | Описание горячей клавиши |
| --- | --- | --- | --- | --- |
| en | Find Tab Playing Sound | Find which tab is playing audio and switch to it. Click or shortcut to cycle sound tabs. | Go to the tab playing sound | Go to the next tab playing sound |
| ru | Найти вкладку со звуком | Находит вкладку, которая сейчас играет звук, и сразу переключает на неё. | Перейти к вкладке со звуком | Перейти к следующей вкладке со звуком |
| de | Tab mit Ton finden | Findet den Tab, der gerade Ton wiedergibt, und wechselt dorthin. Klick oder Tastenkürzel schaltet zwischen Ton-Tabs um. | Zum Tab mit Ton wechseln | Zum nächsten Tab mit Ton wechseln |
| es | Encontrar la pestaña con sonido | Encuentra la pestaña que reproduce audio y cambia a ella. Clic o atajo para recorrer las pestañas con sonido. | Ir a la pestaña con sonido | Ir a la siguiente pestaña con sonido |
| fr | Trouver l'onglet avec du son | Trouve l'onglet qui lit du son et y bascule. Un clic ou un raccourci parcourt les onglets avec du son. | Aller à l'onglet avec du son | Aller à l'onglet suivant avec du son |
| pt_BR | Encontrar a aba com som | Encontra a aba que está tocando áudio e muda para ela. Clique ou atalho para percorrer as abas com som. | Ir para a aba com som | Ir para a próxima aba com som |
| uk | Знайти вкладку зі звуком | Знаходить вкладку, яка зараз відтворює звук, і одразу перемикає на неї. Клік або комбінація гортає такі вкладки. | Перейти до вкладки зі звуком | Перейти до наступної вкладки зі звуком |
| zh_CN | 查找正在播放声音的标签页 | 查找正在播放音频的标签页并切换过去。点击图标或按快捷键，可在有声音的标签页之间循环。 | 转到正在播放声音的标签页 | 转到下一个正在播放声音的标签页 |

**Назначение в одну строку (вкладка Privacy):** Switch to the next open browser tab that is currently playing sound.

**Подробные тексты витрины:** Chrome — `store/listing-<локаль>.md`. Firefox — `store/listing-firefox-<локаль>.md`. Локали: `en`, `ru`, `de`, `es`, `fr`, `pt_BR`, `uk`, `zh_CN`. Испанский текст вставьте и в язык витрины Español (Latinoamérica): в пакете для него нет отдельной папки, строки берутся из `es`.

---

## Пакет

| Поле | Значение |
| --- | --- |
| Репозиторий / папка | `sound-tab-jumper` |
| Корень расширения Chrome (распакованная загрузка / содержимое ZIP) | `01/` |
| Корень расширения Firefox (временная загрузка / содержимое ZIP для AMO) | `firefox/` |
| Манифест | V3, `default_locale` `en`, версия **1.2** (оба пакета) |
| Локали в пакете | `en`, `ru`, `de`, `es`, `fr`, `pt_BR`, `uk`, `zh_CN` |
| Разрешения | нет (в обоих манифестах нет `permissions`) |
| Горячая клавиша | Ctrl+Shift+S (на Mac — Cmd+Shift+S), команда `jump-to-sound-tab` |
| ZIP для Chrome | `jump-to-sound-tab.zip` (собирать из `01/`; старые имена архивов не оставлять) |
| ZIP для Firefox | `jump-to-sound-tab-firefox.zip` (собирать из `firefox/`) |
| ID дополнения Firefox | `@find-tab-playing-sound` |

---

## Chrome Web Store

| Поле | Значение |
| --- | --- |
| Категория | Functionality & UI / Функции и интерфейс |
| Цена | Бесплатно |
| Видимость | Public / всем |
| Регионы | Все |
| Контент для взрослых | Нет |
| URL карточки | https://chromewebstore.google.com/detail/find-tab-playing-sound/djhgnhefakcclbpcciijegaaflkmaknd |
| ID расширения | `djhgnhefakcclbpcciijegaaflkmaknd` |
| Homepage / Support / Official URL | нет |
| URL политики конфиденциальности | https://sites.google.com/view/find-tab-playing-sound (источник: `store/privacy-policy.html`) |

Тексты дашборда: Privacy → `store/privacy-practices.md`; Distribution / инструкция для ревьюера → `store/distribution.md`; шаги публикации → `store/PUBLISH.md`. После ZIP: `Instructions/chrome-web-store-after-zip.md`. Политика на GitHub Pages: `Instructions/github-pages-privacy-policy.md`.

---

## Firefox Add-ons (AMO)

| Поле | Значение |
| --- | --- |
| Категория | Tabs / Вкладки |
| Цена | Бесплатно |
| Видимость | Listed / всем (отправлено, ждёт ревью) |
| URL карточки | https://addons.mozilla.org/firefox/addon/find-tab-playing-sound/ |
| ID дополнения | `@find-tab-playing-sound` |
| Минимальный Firefox | 109.0 (только десктоп; Android не выкладываем) |
| Сбор данных | `none` (`browser_specific_settings.gecko.data_collection_permissions`) |
| URL политики конфиденциальности | https://sites.google.com/view/find-tab-playing-sound (источник: `store/privacy-policy.html`) |

Тексты витрины: `store/listing-firefox-<локаль>.md` для локалей выше. Шаги публикации: `store/PUBLISH-firefox.md`.

---

## Графика витрины

| Материал | Размер | Где лежит |
| --- | --- | --- |
| Иконка расширения / витрины | 16 / 32 / 48 / 128 | `01/icons/` (Chrome); копия в `firefox/icons/` |
| Скриншоты | 1280×800 | `screenshots/` |
| Маленький промо-тайл | 440×280 (обязателен) | `promo/` |
| Marquee | 1400×560 (необязателен) | `marquee/` |
