# Distribution (вкладка Distribution в Developer Dashboard)

Скопируйте настройки ниже. После публикации их можно сузить, но для первого релиза обычно достаточно «всем и бесплатно».

---

## Visibility / видимость

```
Public
```

Расширение будет доступно в Chrome Web Store всем пользователям выбранных стран.

Не используйте Unlisted / Trusted testers для финальной публикации, если цель — обычная страница в магазине.

---

## Pricing / цена

```
Free
```

Платных функций, подписок и in-app покупок нет.

---

## Regions / страны

```
All regions
```

Если нужен только определённый список стран — выберите его вручную. Для RU+EN витрины логично оставить все регионы.

---

## Mature content

```
No
```

Расширение не содержит контента 18+.

---

## Test instructions (инструкция для ревьюера)

Вставьте в поле **Test instructions** / **Инструкции по тестированию**:

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

Русский смысл (в дашборд лучше вставлять английский текст выше):

1. Установить расширение.
2. Открыть YouTube (или другой сайт со звуком) и начать воспроизведение — у вкладки должен быть значок динамика.
3. Открыть другую вкладку без звука и оставить её активной.
4. Нажать иконку расширения — Chrome должен переключиться на звучащую вкладку и вынести её окно вперёд.
5. Если звук идёт в двух вкладках, повторный клик переходит к следующей звучащей, затем возвращает на исходную; следующий клик начинает новый цикл.
6. Проверить Ctrl+Shift+S (на Mac Cmd+Shift+S). Если сочетание занято — назначить своё на chrome://extensions/shortcuts.
7. Остаться на единственной звучащей вкладке и нажать иконку — ничего не должно произойти.
8. Аккаунт, пароль и сервер не нужны. Расширение не запрашивает дополнительные разрешения.

---

## Trader / продавец (аккаунт, не карточка товара)

Это настройка **аккаунта издателя**, не вкладки Distribution.

Для бесплатного личного проекта обычно:

```
Non-trader / не является продавцом
```

Выбирайте Trader / продавец, только если публикуете расширение как коммерческую деятельность (продажи, ИП/ООО как продукт). Тогда Google потребует имя, адрес и телефон и покажет их на странице расширения.
