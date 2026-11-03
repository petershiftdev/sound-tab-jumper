# Как добавить ещё один язык

Интерфейс расширения и витрины Chrome Web Store и Firefox Add-ons завязаны на каталоги `_locales`. Сейчас в обоих пакетах: `en`, `ru`, `de`, `es`, `fr`, `pt_BR`, `uk`, `zh_CN`. Новый язык — это новый каталог с тем же набором ключей.

## 1. Код языка

Возьмите код из [списка локалей Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales), например:

- `ja` — японский
- `ko` — корейский
- `it` — итальянский
- `pl` — польский
- `tr` — турецкий
- `nl` — нидерландский

`default_locale` в `01/manifest.json` и `firefox/manifest.json` не меняйте: он должен остаться `en`, пока английский — запасной язык.

Латиноамериканский испанский (`es_419`) отдельной папкой не заводите: Chrome подставляет строки из `es`. В дашборде Chrome Web Store язык **Español (Latinoamérica)** всё равно заполните тем же текстом, что и **Español** (`store/listing-es.md`).

## 2. Файлы расширения

1. Скопируйте `01/_locales/en/messages.json` в `01/_locales/[код]/messages.json` и то же самое для `firefox/_locales/`.
2. Переведите только значения `"message"`. Ключи (`extensionName`, `extensionDescription` и т.д.) не переименовывайте. Текст `"message"` в Chrome и Firefox должен совпадать.
3. Поле `"description"` можно оставить на английском — его видят разработчики, не пользователи. В пакете Firefox в уже существующих локалях это поле называет Firefox, а не Chrome.
4. Краткое описание (`extensionDescription`) — не длиннее **132** символов.
5. Если в коде появятся строки для пользователя, берите их через `chrome.i18n.getMessage` (Chrome) или `browser.i18n.getMessage` (Firefox), а не хардкодом.

После этого в дашборде Chrome Web Store для этой локали можно заполнить своё подробное описание и свои скриншоты.

## 3. Тексты витрины (папка `store/`)

1. Скопируйте `store/listing-en.md` → `store/listing-[код].md` и `store/listing-firefox-en.md` → `store/listing-firefox-[код].md`. Переведите блоки в тройных кавычках. Пояснения вокруг блоков можно оставить по-русски.
2. Скриншоты с текстом на картинке сделайте отдельно для этого языка (1280×800). Файлы в `screenshots/` без врезанных подписей расширения подходят для всех языков.
3. Политику конфиденциальности: добавьте секцию в `store/privacy-policy.html` (`<article id="ja" lang="ja">`) и файл `store/privacy-policy-[код].md`. Ссылку на новый язык добавьте в `<nav>` с `href="#ja"`. Если код статьи не совпадает с языком браузера (как `pt_BR` и `zh_CN`), укажите варианты в `data-langs`. Страница показывает один язык; общий URL в дашборде не меняется. После пуша в `main` GitHub Pages обновит ту же страницу ([инструкция](../Instructions/github-pages-privacy-policy.md)). Обновите список локалей и якоря в `PROJECT.md` и `PROJECT-ru.md`.

## 4. Проверка

1. `chrome://extensions` → Режим разработчика → Загрузить распакованное расширение → папка `01`. Для Firefox: `about:debugging` → Load Temporary Add-on → `firefox/manifest.json`.
2. Смените язык интерфейса браузера и перезапустите его: имя, описание и подсказка кнопки должны стать на новом языке.
3. Поднимите `version` в обоих манифестах. Упакуйте ZIP заново и загрузите в дашборд, иначе новые локали в витрине не появятся. Для Firefox — отдельный ZIP из `firefox/` (см. [PUBLISH-firefox.md](PUBLISH-firefox.md)).
