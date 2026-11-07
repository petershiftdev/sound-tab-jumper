# Листинг Firefox Add-ons — румынский

Скопируйте эти поля в листинг AMO, когда выбран язык **Romanian** / **Română**.

Пункт языка в интерфейсе расширения появляется после каталога `firefox/_locales/ro`. Сейчас его в пакете нет. Название и краткое описание ниже — те же строки `message`, что и для Chrome.

Отображаемое имя издателя: **PeterShift**. Контактный email: `petershift.dev@gmail.com`.

## Сведения о продукте

**Название (до 50 символов):**
```
Găsește fila cu sunet
```

**Краткое описание (до 250 символов):**
```
Găsește fila care redă acum sunet și trece la ea. Un clic sau o scurtătură parcurge filele cu sunet.
```

**Подробное описание:**
```
„Găsește fila cu sunet” găsește fila care redă acum sunet și trece la ea, inclusiv într-o altă fereastră Firefox. Apăsați pictograma din bara de instrumente sau Ctrl+Shift+S (pe Mac: Cmd+Shift+S). Dacă mai multe file redau sunet, fiecare apăsare trece la următoarea, apoi înapoi acolo unde ați început.

Cum se folosește
• Apăsați pictograma extensiei din bara de instrumente.
• Sau apăsați Ctrl+Shift+S (pe Mac: Cmd+Shift+S). Scurtătura se poate schimba din about:addons → Gestionați scurtăturile extensiilor.

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
Suplimentul nu cere permisiuni Firefox suplimentare. Verifică numai în browser care file deschise redau acum sunet, apoi trece la următoarea. Identificatorii filelor rămân în memorie pentru această acțiune și nu sunt salvați sau transmiși.
```

**Категория:** Tabs

Строки `messages.json` — в `store/chrome/listing-ro.md`. Значения `message` те же.

## Графические материалы

Файлы в `screenshots/FireFox/` без врезанных подписей расширения — их можно загрузить и для этого языка. Если делаете отдельные картинки с текстом, подписи такие:

1. Pictogramă în bara de instrumente + text: „Apăsați ca să treceți la fila cu sunet”.
2. Scurtătură: Ctrl+Shift+S / Cmd+Shift+S.
3. Mai multe file cu sunet: „Apăsați din nou ca să treceți la următoarea filă cu sunet”.

| Материал | Размер | Обязательно |
| --- | --- | --- |
| Иконка | 128×128 PNG (`firefox/icons/icon128.png`; в ZIP как `icons/icon128.png`) | Да |
| Скриншоты | 1280×800 (`screenshots/FireFox/`) | Да, минимум 1 |

## Дополнительные поля

**Домашняя страница:** пусто

**Email поддержки:** `petershift.dev@gmail.com`

**Сайт поддержки:** пусто

**URL политики конфиденциальности** (без якоря; страница откроет язык браузера):
```
https://petershiftdev.github.io/sound-tab-jumper/
```
Адреса языков: `#en`, `#ru`, `#de`, `#es`, `#fr`, `#pt_BR`, `#ro`, `#uk`, `#zh_CN`.

**Сбор данных:** нет (`data_collection_permissions`: `none`)

**Firefox для Android:** не отмечать. Минимум в манифесте — 142.0, ключа `gecko_android` нет.

**Сборка кода:** нет. ZIP и есть исходник: без webpack, минификации и шаблонов.
