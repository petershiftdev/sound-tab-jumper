# Публикация Find Tab Playing Sound на Firefox Add-ons (AMO)

Пошаговая инструкция. Тексты для копирования: `listing-firefox-*.md` в этой папке (локали `en`, `ru`, `de`, `es`, `fr`, `pt_BR`, `uk`, `zh_CN`). Код дополнения — в `../firefox/`.

Chrome Web Store — отдельный пакет (`../01/`) и [PUBLISH.md](PUBLISH.md). Не смешивайте ZIP.

## Что уже готово в репозитории

| Нужно для магазина | Где лежит |
| --- | --- |
| Дополнение (Manifest V3, event page) | `../firefox/` |
| Иконки 16 / 32 / 48 / 128 | `../firefox/icons/` |
| Английский, русский и ещё de, es, fr, pt_BR, uk, zh_CN | `../firefox/_locales/` |
| Тексты витрины | [listing-firefox-en.md](listing-firefox-en.md), [listing-firefox-ru.md](listing-firefox-ru.md), [listing-firefox-de.md](listing-firefox-de.md), [listing-firefox-es.md](listing-firefox-es.md), [listing-firefox-fr.md](listing-firefox-fr.md), [listing-firefox-pt_BR.md](listing-firefox-pt_BR.md), [listing-firefox-uk.md](listing-firefox-uk.md), [listing-firefox-zh_CN.md](listing-firefox-zh_CN.md) |
| Политика конфиденциальности | [privacy-policy.html](privacy-policy.html) (тот же URL, что у Chrome) |
| Политика на GitHub Pages | [../Instructions/github-pages-privacy-policy.md](../Instructions/github-pages-privacy-policy.md) |

Gecko ID в манифесте: `@find-tab-playing-sound`. Сбор данных: `none`.

## Чего ещё нет (сделайте до загрузки ZIP)

1. **Скриншоты** для AMO (рекомендуется 1280×800, хотя бы один). Промо-тайлы Chrome (440×280) AMO не требует.
2. Выложить политику по публичному HTTPS, если workflow ещё не публиковал страницу. Адрес — в `PROJECT.md`. Проверка в инкогнито, без логина. В HTML должны быть и Chrome, и Firefox.

---

## Шаг 1. Аккаунт разработчика

1. Войдите на [addons.mozilla.org](https://addons.mozilla.org/) тем Firefox-аккаунтом, который читаете.
2. Откройте [Developer Hub](https://addons.mozilla.org/developers/). Примите соглашение разработчика. **Взноса нет** (в отличие от Chrome Web Store).
3. Имя издателя на витрине: **PeterShift**. Контактный email: `petershift.dev@gmail.com`.

---

## Шаг 2. Проверить дополнение локально

Временная загрузка снимается при перезапуске Firefox — это нормально для проверки.

1. Firefox → `about:debugging#/runtime/this-firefox`.
2. **Load Temporary Add-on** / **Загрузить временное дополнение** → выберите **`firefox/manifest.json`**, не корень репозитория и не `01`.
3. Откройте вкладку со звуком (YouTube) и тихую вкладку. Клик по иконке или `Ctrl+Shift+S` (`Cmd+Shift+S` на Mac) должен переключить на звучащую.
4. Смените язык интерфейса Firefox на русский, перезапустите браузер и загрузите дополнение снова: название и подсказка кнопки должны стать русскими. Так же проверяются German, Spanish, French, Portuguese (Brazil), Ukrainian и Chinese (Simplified).
5. Если горячая клавиша не сработала: `about:addons` → шестерёнка → **Manage Extension Shortcuts** / **Управление сочетаниями клавиш**.

---

## Шаг 3. Собрать ZIP

В архиве **корень = содержимое `firefox`**, чтобы сразу был `manifest.json`.

Не кладите в ZIP: папку `01`, `store`, `Instructions`, `.git`, `PROJECT*.md`, `.cursor`, `sites`.

**Windows (PowerShell), из корня проекта:**

```powershell
Set-Location "e:\Projects\ChromeExtensions\sound-tab-jumper"
if (Test-Path "jump-to-sound-tab-firefox.zip") { Remove-Item "jump-to-sound-tab-firefox.zip" }
tar -a -c -f jump-to-sound-tab-firefox.zip -C firefox *
```

Проверьте архив: внутри должны быть `manifest.json`, `background.js`, `_locales\en`, `_locales\ru`, `_locales\de`, `_locales\es`, `_locales\fr`, `_locales\pt_BR`, `_locales\uk`, `_locales\zh_CN` (в каждой папке `messages.json`), `icons\icon16.png` … `icon128.png`. Не должно быть вложенной папки `firefox` как единственного корня.

Версия в манифесте сейчас `1.2`. Каждая новая загрузка после публикации требует **больший** номер версии.

---

## Шаг 4. Создать дополнение на AMO

1. [Developer Hub](https://addons.mozilla.org/developers/) → **Submit a New Add-on**.
2. Загрузите `jump-to-sound-tab-firefox.zip`.
3. Канал: **On this site** (listed), не Unlisted, если цель — публичная страница.
4. После валидации заполните листинг.

Если валидатор ругается на отсутствие `data_collection_permissions` — в манифесте уже стоит `"required": ["none"]`. Не добавляйте другие категории.

---

## Шаг 5. Листинг

English из [listing-firefox-en.md](listing-firefox-en.md), Русский из [listing-firefox-ru.md](listing-firefox-ru.md), затем German, Spanish, French, Portuguese (Brazil), Ukrainian и Chinese (Simplified) из `listing-firefox-de.md`, `listing-firefox-es.md`, `listing-firefox-fr.md`, `listing-firefox-pt_BR.md`, `listing-firefox-uk.md`, `listing-firefox-zh_CN.md`.

- Категория: **Tabs**.
- Политика: тот же URL, что у Chrome.
- Support email: `petershift.dev@gmail.com`.
- Android не отмечайте (в манифесте нет `gecko_android`).

---

## Шаг 6. Отправить на ревью

1. Сохраните листинг.
2. Submit for review.
3. Срок — обычно от нескольких часов до нескольких дней. Письма смотрите на email аккаунта Firefox.

Официально: [Publish a Firefox extension](https://extensionworkshop.com/documentation/publish/submitting-an-add-on/).

---

## Шаг 7. После публикации

- Обновление: поднимите `version` в `firefox/manifest.json` → новый ZIP → Upload a New Version.
- Не добавляйте сеть, аналитику или разрешения «тихо»: на AMO это должно совпасть с `data_collection_permissions` и политикой.
- Если меняете названия или email — обновите и `01/_locales`, и `firefox/_locales`, и оба `PROJECT*.md`.

## Куда смотреть, если что-то не так

| Проблема | Что проверить |
| --- | --- |
| Временное дополнение пропало | Перезапуск Firefox снимает temporary add-on; загрузите снова |
| Имя всегда английское | Язык интерфейса Firefox; `default_locale` — `en` |
| Валидатор просит gecko id | В манифесте `browser_specific_settings.gecko.id` = `@find-tab-playing-sound` |
| Валидатор просит data collection | `"required": ["none"]` уже в манифесте |
| Горячая клавиша не работает | Занята в Firefox; запасной путь — клик по иконке |
