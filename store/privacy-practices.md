# Privacy practices (вкладка Privacy в Developer Dashboard)

Скопируйте ответы ниже. Дашборд чаще показывает поля на английском — используйте английский текст. Русский дан как смысл, его в эти поля вставлять не нужно.

Перед отправкой сверьте, что поведение кода не изменилось: нет сети, нет хранения, в манифесте нет `permissions`.

---

## 1. Single purpose description

**Поле:** Describe the single purpose of your extension

```
Switch to the next open browser tab that is currently playing sound.
```

Смысл: одно узкое назначение — переключиться на следующую вкладку, которая сейчас воспроизводит звук.

---

## 2. Permission justification

В манифесте **нет** массива `permissions`. На вкладке Privacy не должно быть полей обоснования для `tabs` или других разрешений.

Если в списке появится `tabs` (или любое другое разрешение) — загружен не тот ZIP. Соберите архив из содержимого папки `01/` после удаления `permissions` из `manifest.json`.

Смысл: расширение смотрит флаг `audible` и переключает вкладку через обычные API, для которых разрешение `tabs` не нужно. `tabs` даёт доступ к URL и заголовкам — это лишнее.

---

## 3. Remote code

**Вопрос:** Does this item use remote code?

**Ответ:**
```
No, I am not using remote code.
```

Смысл: нет. Service worker локальный (`background.js`), скрипты с других сайтов не загружаются.

Если дашборд просит пояснение при выборе No — оставьте пустым или напишите:

```
The extension runs only local code from the installed package (background.js). It does not fetch or execute JavaScript from the network.
```

---

## 4. Data usage / certify data collection

Отметьте только то, что расширение **реально** делает. При текущем коде:

**Does this item collect or use user data?** → **No**  
(или не отмечайте ни один тип данных: PII, health, financial, authentication, personal communications, location, web history, user activity, website content.)

Не включайте аналитику, crash reports и телеметрию — в коде их нет.

**Limited Use certification** — поставьте все обязательные галочки согласия, что:

- данные используются только для заявленной цели;
- данные не продаются;
- данные не используются для персонализированной рекламы;
- вы не передаёте данные брокерам.

Это сертификация политики Google, даже если вы ничего не собираете.

---

## 5. Privacy policy URL

Вставьте публичный HTTPS-адрес:

```
https://sites.google.com/view/find-tab-playing-sound
```

Файл для публикации: [privacy-policy.html](privacy-policy.html).  
Тексты: [privacy-policy-en.md](privacy-policy-en.md), [privacy-policy-ru.md](privacy-policy-ru.md).

Проверьте URL в режиме инкогнито до отправки на ревью.

Политика должна совпадать с галочками выше: нет сбора, нет передачи, локальное использование идентификаторов вкладок только для переключения, дополнительных разрешений нет.
