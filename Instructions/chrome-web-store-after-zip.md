# Заполнение дашборда после загрузки ZIP

ZIP уже в Chrome Web Store. Этот файл — что вставлять на вкладках **Витрина**, **Конфиденциальность** и **Распространение**.

Издатель: **PeterShift**. Email: **petershift.dev@gmail.com**.  
Политика на GitHub Pages: [github-pages-privacy-policy.md](github-pages-privacy-policy.md).

Исходники в репозитории (если тексты разойдутся, верны файлы в `store/` и `PROJECT.md`):

- витрина: `store/listing-en.md`, `store/listing-ru.md`, `store/listing-de.md`, `store/listing-es.md`, `store/listing-fr.md`, `store/listing-pt_BR.md`, `store/listing-uk.md`, `store/listing-zh_CN.md`
- Privacy: `store/privacy-practices.md`
- Distribution: `store/distribution.md`

---

## Перед заполнением

1. Имя издателя в аккаунте дашборда — **PeterShift**.
2. Contact email — `petershift.dev@gmail.com`.
3. Статус продавца для личного бесплатного проекта — **не продавец / non-trader** (это настройка аккаунта, не карточки товара).
4. ZIP собран из содержимого `01/` (в корне архива есть `manifest.json`).

На ревью **не отправляйте**, пока нет публичного HTTPS URL политики и обязательных картинок.

---

## 1. Витрина / Store listing — English

Вверху страницы язык: **English**.

### Название (до 45 символов)

```
Find Tab Playing Sound
```

### Краткое описание (до 132)

Часто подставляется из ZIP. Если поле пустое или старое — вставьте:

```
Find which tab is playing audio and switch to it. Click or shortcut to cycle sound tabs.
```

### Подробное описание

Поле вроде «Опишите функции, которые выполняет продукт…». Вставьте целиком:

```
Find Tab Playing Sound finds the tab that is currently playing audio and switches to it — including in another Chrome window. Click the toolbar icon or press Ctrl+Shift+S (Cmd+Shift+S on Mac). If several tabs are playing sound, each press jumps to the next one, then back to where you started.

How to use
• Click the extension icon in the toolbar.
• Or press Ctrl+Shift+S (Cmd+Shift+S on Mac). You can change the shortcut at chrome://extensions/shortcuts.

What it does
• Looks for other open tabs that are currently audible (not the tab you are already on).
• Activates that tab and focuses its window.
• If several tabs are playing sound, each click or shortcut press jumps to the next one, then back to the tab you started from. After that, the cycle starts over.
• If no other tab is playing sound, the click or shortcut does nothing.

What it does not do
• It does not mute, pause, or control media players.
• It does not collect, store, or send your browsing data.
• It does not require an account and has no ads or analytics.

Permissions
The extension does not request extra Chrome permissions. It only checks, in the browser, which open tabs are currently playing sound, then switches to the next one. Tab identifiers are kept in memory for that action and are not saved or transmitted.
```

### Категория

**Функции и интерфейс** (Functionality & UI).

В группе **Ваш персональный Chrome**. Старой категории Productivity в дашборде нет.

Не выбирайте: Работа и планирование, Инструменты, Спец. возможности, Для удовольствия.

### Язык элемента

English (для этой локали витрины).

---

## 2. Витрина / Store listing — Русский

Переключите язык витрины на **Русский**. Без этого русская выдача магазина покажет английский текст.

### Название

```
Найти вкладку со звуком
```

### Краткое описание

```
Находит вкладку, которая сейчас играет звук, и сразу переключает на неё.
```

### Подробное описание

```
«Найти вкладку со звуком» находит вкладку, которая сейчас играет, и сразу переключает на неё — в том числе в другом окне Chrome. Нажмите значок на панели или Ctrl+Shift+S (на Mac — Cmd+Shift+S). Если звук идёт сразу в нескольких вкладках, каждое нажатие переходит к следующей, затем возвращает туда, откуда вы начали.

Как пользоваться
• Нажмите значок расширения на панели инструментов.
• Или нажмите Ctrl+Shift+S (на Mac — Cmd+Shift+S). Сочетание можно изменить на chrome://extensions/shortcuts.

Что делает расширение
• Ищет другие открытые вкладки, которые сейчас воспроизводят звук (не ту, на которой вы уже находитесь).
• Активирует такую вкладку и переводит её окно на передний план.
• Если звук идёт сразу в нескольких вкладках, каждый клик или нажатие горячей клавиши переходит к следующей, затем возвращает на вкладку, с которой вы начали. После этого цикл собирается заново.
• Если кроме текущей звучащих вкладок нет, клик или горячая клавиша ничего не делают.

Чего расширение не делает
• Не отключает звук, не ставит видео на паузу и не управляет плеером.
• Не собирает, не сохраняет и не отправляет данные о просмотре.
• Не требует аккаунта, не показывает рекламу и не использует аналитику.

Разрешения
Расширение не запрашивает дополнительные разрешения Chrome. Оно только в браузере смотрит, какие открытые вкладки сейчас звучат, и переключается на следующую. Идентификаторы вкладок держатся в памяти на время этого действия и никуда не сохраняются и не передаются.
```

Категория одна на весь элемент: уже **Функции и интерфейс**.

---

## 2a. Другие языки витрины

Для каждого языка переключите список вверху и вставьте название, краткое и подробное описание из файла. Категория уже одна на весь элемент. Краткое описание часто подставляется из ZIP само.

| Язык в дашборде | Файл |
| --- | --- |
| Deutsch / Немецкий | `store/listing-de.md` |
| Español / Испанский | `store/listing-es.md` |
| Español (Latinoamérica) / Испанский (Латинская Америка) | тот же `store/listing-es.md` |
| Français / Французский | `store/listing-fr.md` |
| Português (Brasil) / Португальский (Бразилия) | `store/listing-pt_BR.md` |
| Українська / Украинский | `store/listing-uk.md` |
| 中文（简体） / Китайский (упрощенный) | `store/listing-zh_CN.md` |

Без заполненного языка витрина в этой локали магазина покажет английский текст. Скриншоты из `screenshots/` без подписей расширения можно поставить на все языки.

---

## 3. Картинки и ролик

| Материал | Размер | Нужно? | Где взять |
| --- | --- | --- | --- |
| Иконка витрины | 128×128 PNG | Да | `01/icons/icon128.png` |
| Скриншоты | 1280×800, 1–5 штук | Да, минимум 1 | папка `screenshots/` |
| Small promo tile | 440×280 | Да | папка `promo/` |
| Marquee | 1400×560 | Нет | папка `marquee/`, если появится |
| YouTube-ролик | ссылка | Нет | не заполнять, пока ролика нет |

Правила картинок: [Supplying Images](https://developer.chrome.com/docs/webstore/images). Без полей, прямые углы. Текущие файлы в `screenshots/` без подписей расширения — один набор подходит всем языкам витрины. Если позже врежете текст в картинку, сделайте копию на каждый язык.

---

## 4. Дополнительные поля витрины

Сейчас **оставьте пустыми**:

| Поле | Значение |
| --- | --- |
| Официальный URL | Нет. Только сайт, подтверждённый в Search Console. |
| URL главной страницы | Пусто. Сайта продукта нет. Позже можно поставить публичный Google Sites, это не обязательно. |
| URL поддержки | Пусто. Вопросы — в Support hub магазина. |

Не подставляйте GitHub, Drive и чужие сайты.

**Контент для взрослых / Mature content:** Нет / No.

---

## 5. Конфиденциальность / Privacy

Дашборд ждёт **английский** текст.

Страница на GitHub Pages должна открываться **до** финального сохранения этой вкладки: [github-pages-privacy-policy.md](github-pages-privacy-policy.md).

### Single purpose

```
Switch to the next open browser tab that is currently playing sound.
```

### Разрешения

В манифесте **нет** `permissions`. Полей «зачем tabs» быть не должно.

Если появилось обоснование для `tabs` — загружен не тот ZIP. Нужен архив из содержимого `01/`.

### Remote code

**Does this item use remote code?** → **No** / «Нет, я не использую удалённый код».

Если попросят пояснение:

```
The extension runs only local code from the installed package (background.js). It does not fetch or execute JavaScript from the network.
```

### Сбор данных

**Does this item collect or use user data?** → **No**.

Не отмечайте ни один тип данных (PII, история, содержимое сайтов, аналитика, crash reports).

**Limited Use** — поставьте **все** обязательные галочки (только заявленная цель, не продаём, не реклама, не брокеры). Их просят даже если данных нет.

### Privacy policy URL

Вставьте URL из `PROJECT.md` (главная страница GitHub Pages). Ссылка «Русский» на этой же странице открывает русский текст. Проверка в инкогнито, без входа в GitHub.  
Пока ссылки нет, вкладку до конца не закрывайте и на ревью не отправляйте.

---

## 6. Распространение / Distribution

| Поле | Значение |
| --- | --- |
| Visibility / видимость | Public / всем |
| Price / цена | Free / бесплатно |
| Regions / регионы | All regions / все |
| Mature content | No |

Не выбирайте Unlisted / Trusted testers, если нужна обычная карточка в магазине.

### Test instructions (для ревьюера)

Вставляйте английский текст:

```
How to test Find Tab Playing Sound

1. Install the extension.
2. Open YouTube (or another site with audio) in a tab and start playback. Confirm the tab shows the speaker icon.
3. Open a different tab that is silent and keep that silent tab active.
4. Click the extension icon in the toolbar.
   Expected: Chrome switches to the audible tab and focuses its window.
5. Optional: start audio in a second tab as well, then click the icon again.
   Expected: Chrome jumps to the next audible tab. Click again until you return to the silent tab you started from; the next click starts a new cycle.
6. Keyboard shortcut: press Ctrl+Shift+S (Cmd+Shift+S on Mac) from a silent tab.
   Expected: same jump as clicking the icon.
   If the shortcut is taken by another extension, open chrome://extensions/shortcuts and assign one, then retry.
7. Stay on the only audible tab and click the icon.
   Expected: nothing happens (there is no other sound tab to jump to).

No account, password, or backend is required. The extension does not load remote code, does not request extra permissions, and does not send data to a server.
```

---

## 7. Сохранить и отправить

1. Сохраните каждую вкладку.
2. Когда политика открывается в инкогнито, картинки на месте, EN и RU витрина заполнены — **Submit for review**.
3. Имеет смысл включить **deferred publishing**: после одобрения расширение не выйдет само, вы нажмёте Publish.
4. Письма об отказе придут на email аккаунта разработчика.

Частые отказы: политика не открывается без логина, нет иконки/скриншота/promo 440×280, лишние разрешения, скриншоты не про переход к звучащей вкладке.

---

## После публикации

- Отвечайте в Support hub карточки.
- Обновление: больший `version` в `01/manifest.json` → новый ZIP из `01/` → Upload → снова Submit for review.
- Сеть, аналитику и новые разрешения нельзя добавлять «тихо»: сначала политика и вкладка Privacy, потом новая версия.
