# Публикация Find Tab Playing Sound в Chrome Web Store

Пошаговая инструкция. Тексты для копирования лежат рядом в этой папке. Код расширения — в `../01/`.

Firefox — отдельный пакет (`../firefox/`) и [PUBLISH-firefox.md](PUBLISH-firefox.md). Не кладите `firefox/` в ZIP для Chrome.

## Что уже готово в репозитории

| Нужно для магазина | Где лежит |
| --- | --- |
| Расширение (Manifest V3) | `../01/` |
| Иконки 16 / 32 / 48 / 128 | `../01/icons/` |
| Английский, русский и ещё de, es, fr, pt_BR, uk, zh_CN | `../01/_locales/` |
| Тексты витрины | [listing-en.md](listing-en.md), [listing-ru.md](listing-ru.md), [listing-de.md](listing-de.md), [listing-es.md](listing-es.md), [listing-fr.md](listing-fr.md), [listing-pt_BR.md](listing-pt_BR.md), [listing-uk.md](listing-uk.md), [listing-zh_CN.md](listing-zh_CN.md) |
| Вкладка Privacy | [privacy-practices.md](privacy-practices.md) |
| Вкладка Distribution | [distribution.md](distribution.md) |
| Политика конфиденциальности | [privacy-policy.html](privacy-policy.html) (+ md) |
| Политика на GitHub Pages | [../Instructions/github-pages-privacy-policy.md](../Instructions/github-pages-privacy-policy.md) |
| Заполнение дашборда после ZIP | [../Instructions/chrome-web-store-after-zip.md](../Instructions/chrome-web-store-after-zip.md) |
| Новый язык позже | [how-to-add-locale.md](how-to-add-locale.md) |

## Чего ещё нет (сделайте до загрузки ZIP)

1. **Скриншоты** 1280×800 (хотя бы один, лучше 3–5) и **small promo tile** 440×280. Иконки расширения уже лежат в `../01/icons/`.
2. Выложить политику по публичному HTTPS. В HTML уже указаны издатель **PeterShift** и email `petershift.dev@gmail.com`.

---

## Шаг 1. Аккаунт разработчика

1. Включите [двухэтапную аутентификацию](https://myaccount.google.com/signinoptions/twosv) у Google-аккаунта.
2. Откройте [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole).
3. Примите соглашение разработчика и оплатите разовый взнос **$5**.
4. Укажите имя издателя **PeterShift** и email, который вы читаете (туда придут отказ или снятие с витрины).
5. На вопрос про ЕЭЗ / продавца для бесплатного личного проекта обычно выбирайте **не продавец / non-trader**. Если это коммерческая деятельность — **продавец / trader** (тогда публично покажут имя, адрес и телефон). Подробности: [политика Google](https://developer.chrome.com/docs/webstore/program-policies/trader-disclosure).

Новым издателям доступны **два** опубликованных расширения.

---

## Шаг 2. Выложить политику конфиденциальности (HTTPS)

Магазину нужна **постоянная публичная HTTPS-ссылка**, не файл из ZIP.

Пошагово: [../Instructions/github-pages-privacy-policy.md](../Instructions/github-pages-privacy-policy.md). Страницу публикует GitHub Actions из `store/privacy-policy.html`.

Итоговый URL должен открываться **в режиме инкогнито**, без логина. Ссылка не должна меняться после ревью. Сохраните её в `PROJECT.md` / `PROJECT-ru.md`.

---

## Шаг 3. Проверить расширение локально

1. Chrome → `chrome://extensions` → включите **Режим разработчика**.
2. **Загрузить распакованное расширение** → выберите папку **`01`**, не корень репозитория и не `store`.
3. Откройте вкладку со звуком (YouTube) и тихую вкладку. Клик по иконке или `Ctrl+Shift+S` (`Cmd+Shift+S` на Mac) должен переключить на звучащую.
4. Смените язык интерфейса Chrome на русский, перезапустите браузер: название и подсказка кнопки должны стать русскими. Для английского — наоборот. Так же проверяются Deutsch, Español, Français, Português (Brasil), Українська и 中文（简体）.
5. Если горячая клавиша не сработала: `chrome://extensions/shortcuts`.

---

## Шаг 4. Собрать ZIP

В архиве **корень = содержимое `01`**, чтобы сразу был `manifest.json`.

Не кладите в ZIP: папку `store`, `Instructions`, `.git`, README репозитория, исходники политики.

**Windows (PowerShell), из корня проекта:**

```powershell
Set-Location "e:\Projects\ChromeExtensions\sound-tab-jumper"
if (Test-Path "jump-to-sound-tab.zip") { Remove-Item "jump-to-sound-tab.zip" }
tar -a -c -f jump-to-sound-tab.zip -C 01 *
```

Проверьте архив: внутри должны быть `manifest.json`, `background.js`, `_locales\en`, `_locales\ru`, `_locales\de`, `_locales\es`, `_locales\fr`, `_locales\pt_BR`, `_locales\uk`, `_locales\zh_CN` (в каждой папке `messages.json`), `icons\icon16.png` … `icon128.png`. Не должно быть вложенной папки `01` как единственного корня и не должно быть `.py` / папки `store`.

Версия в манифесте сейчас `1.2`. Каждая новая загрузка после публикации требует **больший** номер версии (`1.3`, `1.2.1` и т.д.).

---

## Шаг 5. Создать элемент в магазине

1. [Dashboard](https://chrome.google.com/webstore/devconsole) → **New item** / **Добавить элемент**.
2. Загрузите `jump-to-sound-tab.zip`.
3. Если ошибка про иконки — проверьте, что в ZIP есть `icons/icon16.png` … `icon128.png`, и соберите архив заново.
4. После успешной загрузки появятся вкладки Package, Store listing, Privacy, Distribution.

---

## Шаг 6. Store listing (витрина)

Готовые поля и что вставлять: [../Instructions/chrome-web-store-after-zip.md](../Instructions/chrome-web-store-after-zip.md).

Кратко: English из [listing-en.md](listing-en.md), Русский из [listing-ru.md](listing-ru.md), затем Deutsch, Español, Français, Português (Brasil), Українська и 中文（简体） из одноимённых `listing-*.md`. Для **Español (Latinoamérica)** вставьте тот же текст, что в [listing-es.md](listing-es.md). Категория **Функции и интерфейс**. Official / Homepage / Support — пусто. Нужны иконка 128, скриншот 1280×800 и small promo 440×280. Ролик необязателен. Скриншоты из `screenshots/` без подписей расширения подходят всем языкам.

---

## Шаг 7. Privacy

Скопируйте ответы из [../Instructions/chrome-web-store-after-zip.md](../Instructions/chrome-web-store-after-zip.md) (раздел Privacy) или из [privacy-practices.md](privacy-practices.md). URL политики — из `PROJECT.md` (GitHub Pages, шаг 2).

---

## Шаг 8. Distribution

Public / Free / All regions и английские test instructions — в [../Instructions/chrome-web-store-after-zip.md](../Instructions/chrome-web-store-after-zip.md) или [distribution.md](distribution.md).

---

## Шаг 9. Отправить на ревью

1. Сохраните все вкладки.
2. **Submit for review**.
3. Имеет смысл включить **deferred publishing**: после одобрения расширение не выйдет само, вы нажмёте Publish.
4. Срок ревью — от нескольких часов до нескольких дней. Письма об отказе смотрите на email аккаунта.
5. Частые причины отказа: нет иконки, политика не открывается, лишние разрешения, скриншоты не про то, что делает расширение, keyword spam в описании.

Официально: [Publish in the Chrome Web Store](https://developer.chrome.com/docs/webstore/publish).

---

## Шаг 10. После публикации

- Включите уведомления на странице аккаунта дашборда.
- Отвечайте в Support hub карточки расширения.
- Обновление: поднимите `version` в `manifest.json` → новый ZIP → Upload → снова Submit for review.
- Не добавляйте сеть, аналитику или новые разрешения «тихо»: это снятие с витрины, если не совпадает с Privacy.

---

## Куда смотреть, если что-то не так

| Проблема | Что проверить |
| --- | --- |
| В витрине только часть языков | ZIP собран из `01\*`, внутри есть `_locales` для `en`, `ru`, `de`, `es`, `fr`, `pt_BR`, `uk`, `zh_CN`, и каждый язык заполнен в дашборде |
| Имя всегда английское | Язык интерфейса Chrome; `default_locale` в манифесте — `en` |
| Отказ по privacy | URL политики в инкогнито, плейсхолдеры заменены, галочки = текст политики |
| Горячая клавиша не работает у ревьюера | Это нормально, если занята; в test instructions есть запасной путь через иконку |
| Нужен ещё один язык | [how-to-add-locale.md](how-to-add-locale.md) |
