# Листинг Firefox Add-ons — французский

Скопируйте эти поля в листинг AMO, когда выбран язык **French** / **Français**.

Отображаемое имя издателя: **PeterShift**. Контактный email: `petershift.dev@gmail.com`.

## Сведения о продукте

**Название (до 50 символов):**
```
Trouver l'onglet avec du son
```

**Краткое описание (до 250 символов):**
```
Trouve l'onglet qui lit du son et y bascule. Un clic ou un raccourci parcourt les onglets avec du son.
```

**Подробное описание:**
```
« Trouver l'onglet avec du son » trouve l'onglet qui lit actuellement de l'audio et y bascule, y compris dans une autre fenêtre Firefox. Cliquez sur l'icône de la barre d'outils ou appuyez sur Ctrl+Maj+S (sur Mac : Cmd+Maj+S). Si plusieurs onglets lisent du son, chaque appui passe au suivant, puis revient là où vous avez commencé.

Utilisation
• Cliquez sur l'icône de l'extension dans la barre d'outils.
• Ou appuyez sur Ctrl+Maj+S (sur Mac : Cmd+Maj+S). Vous pouvez modifier le raccourci dans about:addons → Gérer les raccourcis des extensions.

Ce que fait l'extension
• Elle cherche les autres onglets ouverts qui sont audibles (pas celui sur lequel vous êtes déjà).
• Elle active cet onglet et met sa fenêtre au premier plan.
• Si plusieurs onglets lisent du son, chaque clic ou raccourci passe au suivant, puis revient à l'onglet de départ. Ensuite, le cycle recommence.
• Si aucun autre onglet ne lit de son, le clic ou le raccourci ne fait rien.

Ce qu'elle ne fait pas
• Elle ne coupe pas le son, ne met pas en pause et ne commande pas les lecteurs.
• Elle ne collecte, n'enregistre et n'envoie pas vos données de navigation.
• Elle ne demande pas de compte et n'affiche ni publicité ni analyse d'audience.

Autorisations
Le module complémentaire ne demande aucune autorisation Firefox supplémentaire. Il vérifie seulement, dans le navigateur, quels onglets ouverts lisent du son, puis passe au suivant. Les identifiants d'onglets restent en mémoire le temps de cette action et ne sont ni enregistrés ni transmis.
```

**Категория:** Tabs

## Графические материалы

Файлы в `screenshots/FireFox/` без врезанных подписей расширения — их можно загрузить и для этого языка. Если делаете отдельные картинки с текстом, подписи такие:

1. Icône de la barre + texte : « Cliquez pour aller à l'onglet avec du son ».
2. Raccourci : Ctrl+Maj+S / Cmd+Maj+S.
3. Plusieurs onglets audibles : « Cliquez encore pour passer à l'onglet suivant ».

| Материал | Размер | Обязательно |
| --- | --- | --- |
| Иконка | 128×128 PNG (в ZIP как `icons/icon128.png`) | Да |
| Скриншоты | рекомендуется 1280×800 | Да, минимум 1 |

## Дополнительные поля

**Домашняя страница / поддержка:** необязательно; или `petershift.dev@gmail.com`

**URL политики конфиденциальности:**
```
https://petershiftdev.github.io/sound-tab-jumper/
```

**Сбор данных:** нет (уже указано в манифесте)

**Firefox для Android:** нет (только десктоп)
