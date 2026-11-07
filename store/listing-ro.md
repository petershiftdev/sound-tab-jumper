# Листинг Chrome Web Store — румынский

Скопируйте эти поля во вкладку **Витрина** / **Store listing**, когда в списке языков выбран **Română** / **Румынский**.

Пункт языка появляется в кабинете после загрузки пакета, в котором есть `01/_locales/ro`. Сейчас этого каталога в пакете нет: название и краткое описание ниже совпадают со строками, которые нужно положить в `messages.json`, если будете добавлять локаль сами. Подробное описание в пакет не входит.

Отображаемое имя издателя: **PeterShift** (то же имя укажите в Developer Dashboard). Контактный email: `petershift.dev@gmail.com`.

## Сведения о продукте

**Язык:** Română

**Название (до 45 символов):**
```
Găsește fila cu sunet
```

**Краткое описание (из расширения; до 132 символов):**
```
Găsește fila care redă acum sunet și trece la ea. Un clic sau o scurtătură parcurge filele cu sunet.
```

**Подробное описание:**
```
„Găsește fila cu sunet” găsește fila care redă acum sunet și trece la ea, inclusiv într-o altă fereastră Chrome. Apăsați pictograma din bara de instrumente sau Ctrl+Shift+S (pe Mac: Cmd+Shift+S). Dacă mai multe file redau sunet, fiecare apăsare trece la următoarea, apoi înapoi acolo unde ați început.

Cum se folosește
• Apăsați pictograma extensiei din bara de instrumente.
• Sau apăsați Ctrl+Shift+S (pe Mac: Cmd+Shift+S). Scurtătura se poate schimba la chrome://extensions/shortcuts.

Ce face
• Caută alte file deschise care se aud acum (nu fila pe care vă aflați deja).
• Activează acea filă și aduce fereastra ei în prim-plan.
• Dacă mai multe file redau sunet, fiecare clic sau scurtătură trece la următoarea, apoi înapoi la fila de la care ați pornit. După aceea, ciclul o ia de la capăt.
• Dacă nicio altă filă nu redă sunet, clicul și scurtătura nu fac nimic.

Ce nu face
• Nu oprește sunetul, nu pune pauză și nu controlează playerele media.
• Nu colectează, nu stochează și nu trimite date despre navigare.
• Nu cere un cont și nu are reclame sau analitice.

Permisiuni
Extensia nu cere permisiuni Chrome suplimentare. Verifică numai în browser care file deschise redau acum sunet, apoi trece la următoarea. Identificatorii filelor rămân în memorie pentru această acțiune și nu sunt salvați sau transmiși.
```

**Категория:** уже задана для всего элемента — Функции и интерфейс / Functionality & UI

**Язык элемента:** Română

### Строки для `01/_locales/ro/messages.json` и `firefox/_locales/ro/messages.json`

Значения `message` в обоих пакетах должны совпадать. Поле `description` пользователь не видит.

```json
{
  "extensionName": {
    "message": "Găsește fila cu sunet",
    "description": "The extension name shown in Chrome and the Web Store."
  },
  "extensionDescription": {
    "message": "Găsește fila care redă acum sunet și trece la ea. Un clic sau o scurtătură parcurge filele cu sunet.",
    "description": "Short description. Chrome limit: 132 characters."
  },
  "actionDefaultTitle": {
    "message": "Mergi la fila cu sunet",
    "description": "Toolbar button tooltip."
  },
  "commandJumpToSoundTab": {
    "message": "Mergi la următoarea filă cu sunet",
    "description": "Keyboard shortcut description in chrome://extensions/shortcuts."
  }
}
```

## Графические материалы

Файлы в `screenshots/` без врезанных подписей расширения — их можно загрузить и для этого языка. Если делаете отдельные картинки с текстом, подписи такие:

1. Pictogramă în bara de instrumente + text: „Apăsați ca să treceți la fila cu sunet”.
2. Scurtătură: Ctrl+Shift+S / Cmd+Shift+S.
3. Mai multe file cu sunet: „Apăsați din nou ca să treceți la următoarea filă cu sunet”.

| Материал | Размер | Обязательно |
| --- | --- | --- |
| Иконка витрины | 128×128 PNG | Да (`01/icons/icon128.png`; в ZIP как `icons/icon128.png`) |
| Скриншоты | 1280×800 PNG/JPEG, 1–5 штук | Да, минимум 1 (`screenshots/`) |
| Маленький промо-тайл | 440×280 PNG/JPEG | Да (`promo/`) |
| Marquee | 1400×560 PNG/JPEG | Нет (`marquee/`) |
| Видео на YouTube | короткая ссылка | Нет (ролика нет) |

## Дополнительные поля

**Официальный URL:** пусто (сайта, подтверждённого в Search Console, нет)

**URL домашней страницы:** пусто

**URL поддержки:** пусто; вопросы — в Support hub магазина

**URL политики конфиденциальности** (без якоря; страница откроет язык браузера):
```
https://petershiftdev.github.io/sound-tab-jumper/
```
Адреса языков: `#en`, `#ru`, `#de`, `#es`, `#fr`, `#pt_BR`, `#ro`, `#uk`, `#zh_CN`.

**Контент для взрослых:** Нет
