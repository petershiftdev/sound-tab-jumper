# Политика конфиденциальности на GitHub Pages

Магазину нужна постоянная публичная HTTPS-ссылка. В ZIP расширения политики нет.

Источник страницы — `store/privacy-policy.html`. Workflow `.github/workflows/pages.yml` копирует этот файл как `index.html` и публикует только его. Адрес один на все языки: переключатель вверху страницы (`#en`, `#ru`, `#de`, `#es`, `#fr`, `#pt_BR`, `#uk`, `#zh_CN`).

Живой URL записан в `PROJECT.md` и `PROJECT-ru.md`.

## Обновить текст

1. Правьте `store/privacy-policy.html` и тот же смысл в `store/privacy-policy-*.md`.
2. Закоммитьте и отправьте в ветку `main`.
3. Дождитесь зелёного workflow **Publish privacy policy**. Адрес страницы от этого не меняется.
4. Откройте URL в режиме инкогнито, без входа в GitHub: видны имя **PeterShift** и `petershift.dev@gmail.com`.

В Chrome Web Store и Firefox Add-ons вставляйте этот же URL. Отдельные страницы на язык не нужны.

## Если страница не открывается

- Репозиторий должен быть публичным: бесплатный GitHub Pages для приватного репозитория недоступен.
- Settings → Pages → Source: **GitHub Actions**.
- В Actions у workflow **Publish privacy policy** должен быть успешный запуск. Пустой первый запуск можно запустить вручную: **Run workflow**.
