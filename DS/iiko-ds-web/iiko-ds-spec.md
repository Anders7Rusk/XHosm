# iiko Design System — база компонентов и токенов

## ⚡ Как этим пользоваться

Скопируйте строку ниже и отправьте своему ИИ (Hermes, ChatGPT, Claude, Copilot — любому):

> **Собери прототип по дизайн-системе iiko, используя этот файл: https://anders7rusk.github.io/iiko-ds-web/iiko-ds-spec.md**

Дальше просто опишите экран словами или приложите скриншот/макет. ИИ прочитает этот файл и соберёт прототип на компонентах ДС: возьмёт классы из [карты классов](#карта-классов-css-библиотеки), стили — из раздела [Полные CSS-стили](#полные-css-стили-всех-компонентов), значения — из таблиц токенов. **Скачивать ничего не нужно — всё внутри этого файла.**

Главное правило для ИИ: референс задаёт структуру и тексты, **внешний вид — только из этой ДС** (см. [Общие правила](#общие-правила), пункт 0).

---

Единый источник для сборки прототипов: **токены + компоненты + иконки + правила**.
Любой человек или ИИ, используя этот файл как инструкцию, собирает прототипы, которые выглядят одинаково — общая база компонентов и токенов.

> Назначение файла: сколько угодно людей и ИИ ссылаются на один этот файл и собирают свои прототипы по своим задачам — компоненты и токены у всех одни.

Главное для ИИ: работать как разработчик высокой квалификации — сначала разобрать макет/описание и составить план, потом верстать. Порядок разбора — в разделе [Как думать при сборке](#как-думать-при-сборке-порядок-работы-опытного-разработчика).

## Содержание

1. [Общие правила](#общие-правила)
2. [Как думать при сборке (порядок работы разработчика)](#как-думать-при-сборке-порядок-работы-опытного-разработчика)
3. [Токены](#токены)
   - Палитра · Семантические цвета · Компонентные цвета · Размеры · Отступы · Радиусы · Типографика · Тени
4. [Компоненты](#компоненты)
   - [Каталог компонентов Figma](#каталог-компонентов-figma-все-106)
   - [Карта классов CSS-библиотеки](#карта-классов-css-библиотеки)
5. [Иконки](#иконки-google-material-icons)
6. [Полные CSS-стили всех компонентов](#полные-css-стили-всех-компонентов)
7. [Чек-лист соответствия ДС](#чек-лист-соответствия-дс)
## Общие правила

0. **⛔ НЕ ГАДАТЬ (закон над законом).** Права гадать нет. Каждое значение (ширина, цвет, размер, шрифт, иконка, состояние) берётся ТОЛЬКО из источника — код макета (`mockup.md`) + этот спек. Нет значения/компонента в источнике → СТОП, СПРОСИТЬ и предложить замену из ДС. «Свериться, а не гадать» = действие ДО правки, не фраза; сказать «сверюсь» и угадать = нарушение.
0. **Приоритет ДС над референсом (главное правило).** Референс (скриншот, макет, описание) задаёт **структуру, состав блоков и тексты**. Внешний вид берётся **только из этой дизайн-системы**. Если компонент на референсе отличается от ДС (другой цвет, радиус, высота, шрифт, самодельная панель) — использовать компонент ДС, а не копировать референс. Ничего не подгонять «на глаз» под картинку: размеры, отступы, типографика — только из токенов и параметров компонентов ниже. Если подходящего компонента в ДС нет — взять ближайший из каталога и явно пометить это в результате.

**ЗАКОН №1 (никогда не нарушать): компоненты — ТОЛЬКО из ДС.** Есть ДС-компонент (ds-card, ds-stepper, ds-expansion-panel/group/content, ds-table-header/content-row/cell, ds-list-item, ds-search, ds-btn, ds-input, ds-banner, ds-tabs, ds-slide-toggle, ds-input-number) → использовать ЕГО, **НЕ рисовать свой класс**. Свои классы допускаются **только** для каркаса/лейаута, у которого нет ДС-компонента (page/grid/modal/toolbar/footer). Нет ДС-компонента → **остановиться, СПРОСИТЬ и ПРЕДЛОЖИТЬ замену из ДС**; если замены нет — только тогда рисовать своё, строго в рамках ДС (токены), ничего не выдумывать и не подбирать «похожее». Иконки берём из Google Material Icons (раздел «Иконки»).
1. **Никаких хардкодов.** Цвета, радиусы, отступы, размеры и шрифты — только через токены `var(--ds-*)`.
2. **Классы компонентов** — префикс `ds-`: `ds-btn`, `ds-input`, `ds-checkbox`, `ds-radio`, `ds-badge`. Модификаторы через `--`: `ds-btn--m`, `ds-btn--accent`, `ds-btn--filled`.
3. **Шрифт** — Roboto 400/500 (размеры, веса, letter-spacing — из токенов типографики).
4. **Иконки** — Google Material Icons, вставляются по имени (`<span class="material-icons">имя</span>`), цвет наследуется `currentColor`. Обязательного списка нет — берём из каталога Google (раздел «Иконки»); исключение — бренд-иконка iiko (SVG).
5. **Состояния** — нативные: hover/press через CSS, disabled через атрибут, error через класс `--error`.
6. **Компонентные токены** — использовать специфичные для компонента (`--ds-color-button-*`, `--ds-color-checkbox-*`), а не общие (`--ds-color-text-*`, `--ds-color-icon-*`).

### Как думать при сборке: порядок работы опытного разработчика

Общие рекомендации для любого экрана и любой задачи. Смотреть на макет, скриншот или текстовое описание
нужно **как разработчик высокой квалификации, который получил задание сверстать интерфейс**: сначала разбор
и план, потом код. Не начинать с написания HTML.

**Шаг 1. Понять экран целиком.** Определить тип страницы (например: форма, пошаговый мастер, настройки,
список или таблица, карточка объекта, диалог) и главное действие пользователя. Тип экрана подсказывает
набор компонентов: где шаги — компоненты шагов, где набор настроек — контейнеры-карточки с переключателями
и полями, где перечень данных — таблица или список.

**Шаг 2. Разложить на зоны сверху вниз.** Типичные зоны: шапка, строка заголовка с действиями, навигация,
тело (секции/группы), панель действий. Для каждой зоны определить ширину и выравнивание, а также
вертикальные ритмы — отступы между зонами берутся из токенов отступов, а не подбираются на глаз.

**Шаг 3. Сопоставить каждый блок с компонентом ДС** по карте классов и каталогу компонентов:
«блок → компонент → вариант (Size/Type/State)». Ориентиры выбора носят условный характер, проверять по
каталогу: рамка вокруг группы контента — контейнер-карточка; раскрывающаяся панель-пояснение — панель
раскрытия; короткое сообщение в строку — баннер; подсказка по наведению — тултип; поле с выпадающим
значением — поле ввода с иконкой-стрелкой; включение/выключение настройки — переключатель;
выбор нескольких значений — чекбоксы; выбор одного значения — радиокнопки.
Если точного компонента в ДС нет — взять ближайший и **явно пометить** это, а не рисовать свой.

**Шаг 3а. Однотипных элементов больше одного → групповой компонент.** Если элементов одного вида
**два и более** (кнопки, чекбокса, радио) и у компонента в ДС есть **группа** — использовать именно
**групповой компонент**: 2+ кнопки → `Button group` (`.ds-btn-group`), 2+ чекбокса → `Checkbox group`,
2+ радио → `Radio group`. Одиночный элемент — обычный компонент. У `Button group` есть версия с маржинс
(`--margins`, паддинг 8px 16px) — она в основном для **футера/нижней панели** (отступ от краёв контейнера,
напр. «Отмена/Сохранить» в `__footer`); в тулбаре/списке (середина экрана) группа — **без маржинс**.

**Зазор между кнопками в группе — только из токена, НЕ ставить произвольный отступ.**
`Button group` задаёт `gap` токеном `--ds-button-group-gap` (= `--ds-space-2x`, 8px). Не выставлять
`margin`/`gap` у отдельных кнопок вручную — это ломает единый интервал и «разъезжается» вид.
Разметка горизонтальной группы: `<div class="ds-btn-group ds-btn-group--horizontal">КНОПКИ</div>`.
Одна кнопка — обычный `Button`, **без** обёртки `ds-btn-group`.

**Шаг 4. Определить данные и состояния.** Что заполнено, что плейсхолдер, что обязательно, что включено или
выключено, что недоступно, где ошибка. Тексты — дословно из задания, без переписывания и «улучшений».

**Шаг 5. Спланировать раскладку до кода.** Один общий слой CSS каркаса (сетка, отступы, ограничения ширины)
на flex/grid с отступами из токенов. Компоненты ДС в этом слое **не переопределять** — они приходят
готовыми; каркас только расставляет их. Никаких `style="..."` в разметке.

**Шаг 6. Собирать в правильном порядке.** Сначала скелет зон и порядок блоков (пустые контейнеры) →
затем компоненты сверху вниз → затем иконки (Material Icons по имени) и состояния → в конце отступы и выравнивание.
Так дефекты видны сразу, а не всплывают в конце.

**Шаг 7. Ничего не добавлять от себя.** В прототипе только то, что есть в задании: не тащить слоты
компонента (подвал, панель действий, разделители), которых нет в описании, не придумывать иконки, поля и
кнопки. Не хватает данных — спросить, а не додумать.

**Шаг 8. Проверить как на код-ревью.** Пройти чек-лист и сверить в инспекторе: высоты, радиусы и отступы
совпадают с параметрами компонентов, цвета равны значениям токенов, нет горизонтального скролла, консоль
без ошибок, все иконки видимы (не нулевого размера). Если строки или колонки «разъезжаются» — причина
почти всегда в **разной высоте строк**, а не в ширине колонок: выравнивать высоту/`vertical-align`.

**Типичные ошибки, за которые вёрстку возвращают:** свои классы вместо классов ДС; отдельные элементы
вместо группового компонента при двух и более однотипных; `style="..."` в разметке;
подгонка размеров «на глаз» под картинку; переопределение стилей компонента;
свой класс рядом с уже существующим в ДС; блоки, которых не было в задании.

## Токены

Все токены сгенерированы из Figma (DS.json → tokens.css). В прототипах использовать эти имена как CSS-переменные: `var(--ds-palette-accent-500)`.

### Палитра (Base Color)

Базовые цвета бренда. Семантические и компонентные токены ссылаются на них.

| Токен | Значение |
|---|---|

### Семантические цвета (Color)

Цвета смысловых состояний: brand (акцент), positive, negative, neutral, contrast-1…4.

| Токен | Значение |
|---|---|

### Компонентные цвета (Component)

Цвета конкретных компонентов. **В прототипах использовать именно эти токены**, а не общие (Text/Icon).

### Base Size

| Токен | Значение |
|---|---|

### Space

| Токен | Значение |
|---|---|

### Radius

| Токен | Значение |
|---|---|

### Base Stroke

| Токен | Значение |
|---|---|

### Типографика (Typography + Base Typography)

Шрифт: **Roboto** (400/500). Размеры, веса, межбуквенные расстояния и высоты строк — только из токенов.

| Токен | Значение |
|---|---|

### Тени (Shadows)

| Токен | Значение |
|---|---|

### Текстовые стили ДС (готовые классы)

Стили из Figma один в один. В разметке ставить **класс**, а не набор свойств: `<span class="ds-text-body-m-normal-regular">`.

| Стиль Figma | Класс | font (вес размер/интерлиньяж) | Трекинг | Регистр |
|---|---|---|---|---|
| Header L (34)/Normal/Regular | `.ds-text-header-l-34-normal-regular` | `400 34px/40px "Roboto"` | 0px | none |
| Header L (34) / Normal / Medium | `.ds-text-header-l-34-normal-medium` | `500 34px/40px "Roboto"` | 0px | none |
| Header L (34) / Caps / Regular | `.ds-text-header-l-34-caps-regular` | `400 34px/40px "Roboto"` | 0px | uppercase |
| Header L (34) / Caps / Medium | `.ds-text-header-l-34-caps-medium` | `500 34px/40px "Roboto"` | 0px | uppercase |
| Header M (24) / Normal / Regular | `.ds-text-header-m-24-normal-regular` | `400 24px/32px "Roboto"` | 0.5px | none |
| Header M (24) / Normal / Medium | `.ds-text-header-m-24-normal-medium` | `500 24px/32px "Roboto"` | 0.5px | none |
| Header M (24) / Caps / Regular | `.ds-text-header-m-24-caps-regular` | `400 24px/32px "Roboto"` | 0.5px | uppercase |
| Header M (24) / Caps / Medium | `.ds-text-header-m-24-caps-medium` | `500 24px/32px "Roboto"` | 0.5px | uppercase |
| Header S (20) / Normal / Regular | `.ds-text-header-s-20-normal-regular` | `400 20px/28px "Roboto"` | 0.5px | none |
| Header S (20) / Normal / Medium | `.ds-text-header-s-20-normal-medium` | `500 20px/28px "Roboto"` | 0.5px | none |
| Header S (20) / Caps / Regular | `.ds-text-header-s-20-caps-regular` | `400 20px/28px "Roboto"` | 0.5px | uppercase |
| Header S (20) / Caps / Medium | `.ds-text-header-s-20-caps-medium` | `500 20px/28px "Roboto"` | 0.5px | uppercase |
| Body L (18) / Normal / Regular | `.ds-text-body-l-18-normal-regular` | `400 18px/24px "Roboto"` | 0.5px | none |
| Body L (18) / Normal / Medium | `.ds-text-body-l-18-normal-medium` | `500 18px/24px "Roboto"` | 0.5px | none |
| Body L (18) / Caps / Regular | `.ds-text-body-l-18-caps-regular` | `400 18px/24px "Roboto"` | 0.5px | uppercase |
| Body L (18) / Caps / Medium | `.ds-text-body-l-18-caps-medium` | `500 18px/24px "Roboto"` | 0.5px | uppercase |
| Body M (16) / Normal / Regular | `.ds-text-body-m-16-normal-regular` | `400 16px/24px "Roboto"` | 0.5px | none |
| Body M (16) / Normal / Medium | `.ds-text-body-m-16-normal-medium` | `500 16px/24px "Roboto"` | 0.5px | none |
| Body M (16) / Caps / Regular | `.ds-text-body-m-16-caps-regular` | `400 16px/24px "Roboto"` | 0.5px | uppercase |
| Body M (16) / Caps / Medium | `.ds-text-body-m-16-caps-medium` | `500 16px/24px "Roboto"` | 0.5px | uppercase |
| Body S (14) / Normal / Regular | `.ds-text-body-s-14-normal-regular` | `400 14px/20px "Roboto"` | 0.5px | none |
| Body S (14) / Normal / Medium | `.ds-text-body-s-14-normal-medium` | `500 14px/20px "Roboto"` | 0.5px | none |
| Body S (14) / Caps / Regular | `.ds-text-body-s-14-caps-regular` | `400 14px/20px "Roboto"` | 0.5px | uppercase |
| Body S (14) / Caps / Medium | `.ds-text-body-s-14-caps-medium` | `500 14px/20px "Roboto"` | 0.5px | uppercase |
| Caption L (12) / Normal / Regular | `.ds-text-caption-l-12-normal-regular` | `400 12px/16px "Roboto"` | 0.5px | none |
| Caption L (12) / Normal / Medium | `.ds-text-caption-l-12-normal-medium` | `500 12px/16px "Roboto"` | 0.5px | none |
| Caption L (12) / Caps / Regular | `.ds-text-caption-l-12-caps-regular` | `400 12px/16px "Roboto"` | 0.5px | uppercase |
| Caption L (12) / Caps / Medium | `.ds-text-caption-l-12-caps-medium` | `500 12px/16px "Roboto"` | 0.5px | uppercase |
| Caption M (10) / Normal / Regular | `.ds-text-caption-m-10-normal-regular` | `400 10px/12px "Roboto"` | 0.5px | none |
| Caption M (10)/Normal/Medium | `.ds-text-caption-m-10-normal-medium` | `500 10px/12px "Roboto"` | 0.5px | capitalize |
| Caption M (10) / Caps / Regular | `.ds-text-caption-m-10-caps-regular` | `400 10px/12px "Roboto"` | 0.5px | uppercase |
| Caption M (10) / Caps / Medium | `.ds-text-caption-m-10-caps-medium` | `500 10px/12px "Roboto"` | 0.5px | uppercase |
| Caption S (8) / Normal / Regular | `.ds-text-caption-s-8-normal-regular` | `400 8px/10px "Roboto"` | 0.5px | none |
| Caption S (8) / Normal / Medium | `.ds-text-caption-s-8-normal-medium` | `500 8px/10px "Roboto"` | 0.5px | none |
| Caption S (8) / Caps / Regular | `.ds-text-caption-s-8-caps-regular` | `400 8px/10px "Roboto"` | 0.5px | uppercase |
| Caption S (8) / Caps / Medium | `.ds-text-caption-s-8-caps-medium` | `500 8px/10px "Roboto"` | 0.5px | uppercase |

### Эффект-стили ДС (тени как готовые значения)

Ставить `box-shadow: var(--ds-shadow-…)`, не переписывать пиксели.

| Стиль Figma | Токен | Значение box-shadow |
|---|---|---|
| Shadows/None | `--ds-shadow-shadows-none` | `0px 2px 0px 0px #ffffff` |
| Shadows/01 dp Sl | `--ds-shadow-shadows-01-dp-sl` | `0px 0px 4px 0px rgba(33, 33, 33, 0.12), 0px 2px 2px 0px rgba(33, 33, 33, 0.04)` |
| Shadows/08 dp S | `--ds-shadow-shadows-08-dp-s` | `0px 0px 16px 0px rgba(33, 33, 33, 0.12), 0px 4px 6px 0px rgba(33, 33, 33, 0.1)` |
| Shadows/12 dp M | `--ds-shadow-shadows-12-dp-m` | `0px 0px 28px 0px rgba(33, 33, 33, 0.12), 0px 10px 24px 0px rgba(33, 33, 33, 0.12)` |
| Shadows/24 dp XL | `--ds-shadow-shadows-24-dp-xl` | `0px 0px 32px 0px rgba(33, 33, 33, 0.16), 0px 12px 16px 0px rgba(33, 33, 33, 0.16)` |

### Цветовые стили ДС

Цветовые стили Figma. Для компонентов приоритет у компонентных токенов `--ds-color-*`.

| Стиль Figma | Токен | Значение |
|---|---|---|
| Surface / Default | `--ds-paint-surface-default` | #ffffff |
| Surface / Default V2 | `--ds-paint-surface-default-v2` | #f8f9fc |
| Surface / Hover | `--ds-paint-surface-hover` | #f5f5f5 |
| Surface / Selected | `--ds-paint-surface-selected` | #ebebeb |
| Surface / Press | `--ds-paint-surface-press` | #e0e0e0 |
| Surface / Disable | `--ds-paint-surface-disable` | #e0e0e0 |
| Surface/SnackTooltip | `--ds-paint-surface-snacktooltip` | #424242 |
| Surface/Sidebar | `--ds-paint-surface-sidebar` | #f8f9fc |
| Surface/Sidebar_Selected | `--ds-paint-surface-sidebar-selected` | #f0f5ff |
| Surface / Sidebar_Active | `--ds-paint-surface-sidebar-active` | #a8c9ff |
| Table surfase / Default | `--ds-paint-table-surfase-default` | #ffffff |
| Table surfase / Hover | `--ds-paint-table-surfase-hover` | #f5f5f5 |
| Table surfase / Selected | `--ds-paint-table-surfase-selected` | #ebebeb |
| Table surfase / Group | `--ds-paint-table-surfase-group` | #ebebeb |
| Table surfase / Head | `--ds-paint-table-surfase-head` | #f0f5ff |
| Table surfase / Head Group | `--ds-paint-table-surfase-head-group` | #a8c9ff |
| Text/Primary | `--ds-paint-text-primary` | #333333 |
| Text/Inversive | `--ds-paint-text-inversive` | #ffffff |
| Text / Caption | `--ds-paint-text-caption` | #616161 |
| Text / Placeholder | `--ds-paint-text-placeholder` | #d6d6d6 |
| Text / Disable | `--ds-paint-text-disable` | #9e9e9e |
| Text/Accent | `--ds-paint-text-accent` | #448aff |
| Text/Positive | `--ds-paint-text-positive` | #14b456 |
| Text / Warning | `--ds-paint-text-warning` | #ffab40 |
| Text/Negative | `--ds-paint-text-negative` | #ff5252 |
| Button / Neutral / Default | `--ds-paint-button-neutral-default` | #ffffff |
| Button / Neutral / Hover | `--ds-paint-button-neutral-hover` | #f5f5f5 |
| Button / Neutral / Press | `--ds-paint-button-neutral-press` | #ebebeb |
| Button / Neutral / Disable | `--ds-paint-button-neutral-disable` | #ebebeb |
| Button/Accent/Default | `--ds-paint-button-accent-default` | #448aff |
| Button/Accent/Hover | `--ds-paint-button-accent-hover` | #3969d5 |
| Button/Accent/Press | `--ds-paint-button-accent-press` | #2651b5 |
| Button/Positive/Default | `--ds-paint-button-positive-default` | #14b456 |
| Button/Positive/Hover | `--ds-paint-button-positive-hover` | #0f852c |
| Button/Positive/Press | `--ds-paint-button-positive-press` | #0a571a |
| Button/Warning/Default | `--ds-paint-button-warning-default` | #ffab40 |
| Button/Warning/Hover | `--ds-paint-button-warning-hover` | #ea7806 |
| Button/Warning/Press | `--ds-paint-button-warning-press` | #994000 |
| Button/Negative/Default | `--ds-paint-button-negative-default` | #ff5252 |
| Button/Negative/Hover | `--ds-paint-button-negative-hover` | #de1a12 |
| Button/Negative/Press | `--ds-paint-button-negative-press` | #7f0f0a |
| Icon/Primary | `--ds-paint-icon-primary` | #616161 |
| Icon/Inversive | `--ds-paint-icon-inversive` | #ffffff |
| Icon/Disable | `--ds-paint-icon-disable` | #9e9e9e |
| Icon/Accent | `--ds-paint-icon-accent` | #448aff |
| Icon/Positive | `--ds-paint-icon-positive` | #14b456 |
| Icon/Warning | `--ds-paint-icon-warning` | #ea7806 |
| Icon/Negative | `--ds-paint-icon-negative` | #ff5252 |
| Shapes / Default | `--ds-paint-shapes-default` | #ffffff |
| Shapes / SuperLight NT | `--ds-paint-shapes-superlight-nt` | #f5f5f5 |
| Shapes / Lightest NT | `--ds-paint-shapes-lightest-nt` | #ebebeb |
| Shapes / Lighter NT | `--ds-paint-shapes-lighter-nt` | #e0e0e0 |
| Shapes / Lighter PR | `--ds-paint-shapes-lighter-pr` | #f8f9fc |
| Shapes / Lighter SC | `--ds-paint-shapes-lighter-sc` | #ebfbf2 |
| Shapes/Lighter WR | `--ds-paint-shapes-lighter-wr` | #fff9f0 |
| Shapes / Lighter ER | `--ds-paint-shapes-lighter-er` | #fff2f2 |
| Shapes / Lightest MG | `--ds-paint-shapes-lightest-mg` | #fbf7fc |
| Shapes / Lightest BR | `--ds-paint-shapes-lightest-br` | #f7e9e3 |
| Shapes / Lightest DB | `--ds-paint-shapes-lightest-db` | #f9fafb |
| Stroke / Default | `--ds-paint-stroke-default` | #e0e0e0 |
| Stroke / Hover | `--ds-paint-stroke-hover` | #9e9e9e |
| Stroke / Disable | `--ds-paint-stroke-disable` | #ebebeb |
| Stroke / Primary | `--ds-paint-stroke-primary` | #448aff |
| Stroke / Secondary | `--ds-paint-stroke-secondary` | #14b456 |
| Stroke / Warning | `--ds-paint-stroke-warning` | #ffab40 |
| Stroke / Error | `--ds-paint-stroke-error` | #ff5252 |

### Сетка (Grid / Контейнер)

Контент собирается в Контейнер (max-width) с 4 брейкпоинтами. Ширина контейнера и поля (margin) — из Figma _Grids_DS_; отступы между блоками внутри контейнера — из шкалы Space (`--ds-space-*`). Проверять по `border-box`.

| Брейкпоинт | Экран | Контент (Container) | Поля (margin) | gap между блоками |
|---|---|---|---|---|
| Desktop | 1440 | 1176 | 32 + 32 | 24 / 16 / 8 |
| Tablet | 768 | 652 | 32 + 32 | 16 / 8 |
| Phone | 374 | 342 | 16 + 16 | 8 |

**Отступы между блоками/компонентами в контейнере** — только из шкалы Space:
| Токен | Значение | Для чего |
|---|---|---|
| `--ds-space-1x` | 4 | микро-отступ внутри инлайн (иконка·текст) |
| `--ds-space-2x` | 8 | мелкий блок (gap иконки/кнопок, Tab-строки) |
| `--ds-space-3x` | 12 | средний между компонентами в строке |
| `--ds-space-4x` | 16 | средний блок (паддинг контента, gap разделов) |
| `--ds-space-5x` | 20 | крупный внутри секции |
| `--ds-space-6x` | 24 | крупный блок (gap секций контейнера) |
| `--ds-space-7x` | 28 | между крупными секциями |
| `--ds-space-8x` | 32 | поля (margin) контейнера Desktop/Tablet |

`Container` Desktop 1176 ширина + поля 32. На Phone поля сжимаются до 16. Колонки в сетке колоночные не заданы (в Figma `layoutGrids` пуст) — раскладка строится на flex/grid и шкале Space.

## Компоненты

### Каталог компонентов Figma (все 106)

Полный набор компонентов дизайн-системы (сканирование всех страниц файла Figma CJBjyS1OnRXqiOqaXYVCVd, включая неопубликованные и вложенные): свойства, все значения вариантов и токены компонента.

**Всего компонентов: 106**

#### Arrow `[55939:14119]` — 13 вариантов
**Описание и рекомендации по применению:**
Набор стрелок — направление действия и раскрытие: возврат назад, шаг по периоду, сортировка, раскрытие списка.  
Берите стрелку из этого набора, а не рисуйте свою: размер и толщина линий согласованы с иконками ДС.  

Как выбрать вариант: по смыслу действия — назад/вперёд, вверх/вниз, раскрыть, свернуть.
- **Content** (VARIANT): arrow_back, arrow_downward_alt, arrow_drop_down, arrow_drop_up, arrow_forward, arrow_left, arrow_right, arrow_upward_alt, keyboard_arrow_down, keyboard_arrow_left, keyboard_arrow_right, keyboard_arrow_up, unfold_less
- Размеры и параметры:
    - высота: `var(--ds-size-6x)` (фикс.)
    - ширина: `var(--ds-size-6x)` (фикс.)
    - фон: `#ffffff`
- Разметка:

```html
<div class="ds-arrow">
  <div class="ds-arrow__drop-down"></div>
  <span class="ds-arrow__icon"><!-- иконка: material-icons по имени --></span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-arrow {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow__icon svg path {
  fill: currentColor;
}
.ds-arrow__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
```
</details>

#### Arrow list `[55939:13307]` — 13 вариантов
**Описание и рекомендации по применению:**
Стрелка в пункте списка — показывает, что пункт раскрывается или ведёт внутрь раздела.  
Служебный элемент списка: ставится справа в пункте List item, отдельно на экран не выносится.  

Как выбрать вариант: по смыслу — переход внутрь, раскрытие или свёртывание пункта.
- **Content** (VARIANT): arrow_back, arrow_downward_alt, arrow_drop_down, arrow_drop_up, arrow_forward, arrow_left, arrow_right, arrow_upward_alt, keyboard_arrow_down, keyboard_arrow_left, keyboard_arrow_right, keyboard_arrow_up, unfold_less
- Размеры и параметры:
    - высота: `var(--ds-size-6x)` (фикс.)
    - ширина: `var(--ds-size-6x)` (фикс.)
    - фон: `#ffffff`
- Разметка:

```html
<div class="ds-arrow-list">
  <div class="ds-arrow-list__drop-down"></div>
  <span class="ds-arrow-list__icon"><!-- иконка: material-icons по имени --></span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-arrow-list {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow-list__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow-list__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow-list__icon svg path {
  fill: currentColor;
}
.ds-arrow-list__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
```
</details>

#### Arrow menu `[56090:1628]` — 13 вариантов
**Описание и рекомендации по применению:**
Стрелка в пункте меню — показывает вложенное подменю или направление перехода.  
Служебный элемент меню: ставится справа в пункте Menu item, отдельно на экран не выносится.  

Как выбрать вариант: по смыслу — вложенное подменю, возврат или раскрытие.
- **Content** (VARIANT): arrow_back, arrow_downward_alt, arrow_drop_down, arrow_drop_up, arrow_forward, arrow_left, arrow_right, arrow_upward_alt, keyboard_arrow_down, keyboard_arrow_left, keyboard_arrow_right, keyboard_arrow_up, unfold_less
- Размеры и параметры:
    - высота: `var(--ds-size-6x)` (фикс.)
    - ширина: `var(--ds-size-6x)` (фикс.)
    - фон: `#ffffff`
- Разметка:

```html
<div class="ds-arrow-menu">
  <div class="ds-arrow-menu__drop-down"></div>
  <span class="ds-arrow-menu__icon"><!-- иконка: material-icons по имени --></span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-arrow-menu {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow-menu__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow-menu__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow-menu__icon svg path {
  fill: currentColor;
}
.ds-arrow-menu__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
```
</details>

#### Arrow select `[57735:17989]` — 13 вариантов
**Описание и рекомендации по применению:**
Стрелка в поле выбора — показывает, что список раскрывается, и его текущее состояние.  
Служебный элемент Select: ставится справа в поле, отдельно на экран не выносится.  

Как выбрать вариант: список закрыт или раскрыт, направление перехода.
- **Content** (VARIANT): arrow_back, arrow_downward_alt, arrow_drop_down, arrow_drop_up, arrow_forward, arrow_left, arrow_right, arrow_upward_alt, keyboard_arrow_down, keyboard_arrow_left, keyboard_arrow_right, keyboard_arrow_up, unfold_less
- Размеры и параметры:
    - высота: `var(--ds-size-6x)` (фикс.)
    - ширина: `var(--ds-size-6x)` (фикс.)
    - фон: `#ffffff`
- Разметка:

```html
<div class="ds-arrow-select">
  <div class="ds-arrow-select__drop-down"></div>
  <span class="ds-arrow-select__icon"><!-- иконка: material-icons по имени --></span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-arrow-select {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow-select__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow-select__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow-select__icon svg path {
  fill: currentColor;
}
.ds-arrow-select__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
```
</details>

#### Autocomplete form `[58107:8230]` — 10 вариантов
**Описание и рекомендации по применению:**
Поле с подсказкой из справочника — ввод с поиском по большому списку: товар, контрагент, сотрудник.  
Берите его, когда вариантов слишком много для обычного списка; подсказки показывайте по мере ввода.  

Как выбрать вариант:  
Variant=Empty — значение не выбрано; Populated — значение выбрано.  
Состояния: Default, Hover, Focus, Focus+Value, Error, Disable.
- **Variant** (VARIANT): Empty, Populated
- **State** (VARIANT): Default, Disable, Error, Focus, Focus+Value, Hover
- Размеры и параметры:
    - высота: минимум `48px`, растёт по контенту
    - ширина: `250px` (фикс.)
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--empty`: color `var(--ds-color-form-field-input-label-text-color, #616161)`, color `var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e)`
    - `--populated`: color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`, color `var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e)`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-autocomplete-form ds-autocomplete-form--disabled">
  <span class="ds-autocomplete-form__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-autocomplete-form__input"></div>
  <div class="ds-autocomplete-form__input-frame"></div>
  <span class="ds-autocomplete-form__label">Текст</span>
  <span class="ds-autocomplete-form__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-autocomplete-form {
  min-height: 48px;
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-autocomplete-form__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-autocomplete-form__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-autocomplete-form__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-autocomplete-form__icon svg path {
  fill: currentColor;
}
.ds-autocomplete-form__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-autocomplete-form__input-frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-autocomplete-form__support {
  display: flex;
  flex-direction: row;
}
.ds-autocomplete-form--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-autocomplete-form--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-autocomplete-form--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-autocomplete-form--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-autocomplete-form--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-autocomplete-form--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-autocomplete-form--empty.ds-autocomplete-form--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-autocomplete-form--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-autocomplete-form--populated.ds-autocomplete-form--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-autocomplete-form--disabled {
  pointer-events: none;
}
```
</details>

#### Backdrop `[53623:806]` — 1 вариантов
**Описание и рекомендации по применению:**
Затемнение под диалогом — перекрывает экран, пока открыто модальное окно или панель.  
Берите его вместе с диалогом; клик по затемнению закрывает окно только там, где нет несохранённых данных.
- **Type** (VARIANT): Default
- CSS не требуется: собственного оформления нет — компонент задаёт только структуру/поведение, вид приходит от вложенных элементов.

#### Badge `[54428:187]` — 8 вариантов
**Описание и рекомендации по применению:**
Бейдж — отметка о новом или требующем внимания на элементе: пункте меню, кнопке, вкладке, пункте списка.  
Показывает количество или сам факт события; для метки состояния объекта используйте Status.  

Как выбрать вариант:  
Type=Counter — с числом, когда количество важно; Type=Point — точка, когда важен только факт.  
Style=Accent — обычное новое; Positive — успешно; Warning — требует внимания; Negative — ошибка или просрочено.  

Число не выдумывайте: бейдж показывает реальное количество, при большом значении — сокращение вида «99+».
- **Style** (VARIANT): Accent, Negative, Positive, Warning
- **Type** (VARIANT): Counter, Point
- CSS: выверено вручную, см. `components/Badge_DS/badge.css` в разделе «Полные CSS-стили всех компонентов»

#### Banners `[54367:2566]` — 12 вариантов
**Описание и рекомендации по применению:**
Баннер — контекстное сообщение на странице: подсказка, предупреждение, ошибка, подтверждение.  
Показывайте поверх контента вверху страницы или блока, когда нужно привлечь внимание к событию.  

Как выбрать вариант:  
Neutral — нейтральное сообщение, без эмоциональной окраски.  
Accent — информационное или рекламное сообщение.  
Positive — успех, подтверждение.  
Warning — событие требует внимания, но не критично.  
Negative — ошибка или блокирующее событие: «Счёт не оплачен».  
Tip — подсказка с пунктирной обводкой, совет по продукту.  

Orientation=Horizontal — иконка, текст и кнопки в одну строку. Vertical — иконка и текст сверху, кнопки снизу.  
Состав настраивается внутри: Element left (иконка), Buttons, Close (крестик).  
Фронт: https://frontend-common.iiko.ru/components/banners
- **Style** (VARIANT): Accent, Negative, Neutral, Positive, Tip, Warning
- **Orientation** (VARIANT): Horizontal, Vertical
- Прочие свойства: Element left#18321:0 (BOOLEAN), Buttons#54443:2 (BOOLEAN), Close#54443:4 (BOOLEAN)
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Button `[17022:63091]` — 153 вариантов
**Описание и рекомендации по применению:**
Кнопка действия. Используйте для основного действия на экране.  
Одна акцентная кнопка на область. Кнопки только с иконкой — это Button icon; группы — Button group.  

Состав: текст + иконка (слева или справа), можно без иконки.  
Варианты:  
Accent Filled — основная.  
Neutral Outlined — второстепенная.  
Neutral Text — третьестепенная.  
Positive / Negative — успех / ошибка.  

Размеры: M (36px), S (28px), XS (24px).  
Состояния: default, hover, pressed, disabled, loading.  
Фронт: \<button restoButton\> — https://frontend-common.iiko.ru/components/button
- **Size** (VARIANT): M, S, XS
- **Style** (VARIANT): Accent, Disable, Negative, Neutral, Positive, Warning
- **Type** (VARIANT): Filled, Outlined, Text
- **State** (VARIANT): Default, Disable, Hover, Loading, Press
- Прочие свойства: Element left#17025:2 (BOOLEAN), Element right#17025:123 (BOOLEAN), Button text#17039:607 (TEXT), Text#17053:733 (BOOLEAN)
- CSS: выверено вручную, см. `components/Button_DS/button.css` в разделе «Полные CSS-стили всех компонентов»

#### Button group `[53619:15772]` — 4 вариантов
**Описание и рекомендации по применению:**
Группа кнопок — несколько действий рядом с единым выравниванием и отступами: подвал диалога, шапка блока, панель над таблицей.  
Порядок слева направо: сначала второстепенные действия, главное — последним справа. Больше трёх кнопок в группу не ставьте, лишнее уводите в меню.  

Как выбрать вариант:  
Orientation=Horizontally — в строку, основной случай; Vertically — в столбец, для узких блоков и мобильных экранов.  
Margins=On — с внешними отступами группы; Off — без них, когда отступы задаёт контейнер.
- **Orientation** (VARIANT): Horizontally, Vertically
- **Margins** (VARIANT): Off, On
- Прочие свойства: Slot#60175:12 (SLOT)
- CSS: выверено вручную, см. `components/Button_DS/button.css` в разделе «Полные CSS-стили всех компонентов»

#### Button icon `[17123:81299]` — 153 вариантов
**Описание и рекомендации по применению:**
Кнопка-иконка — действие без подписи, когда смысл понятен по иконке и место ограничено: строки таблиц, шапки блоков, панели инструментов.  
Всегда добавляйте тултип с названием действия; если действие важное или неочевидное — берите обычную кнопку с текстом (Button).  

Как выбрать вариант:  
Style=Neutral — обычное действие; Accent — акцентное; Positive — подтверждение; Warning — действие с последствиями; Negative — удаление и необратимое.  
Type=Filled — заметная; Outlined — второй план; Text — в таблицах и шапках, не перетягивает внимание.  
Size=M — основной; S — панели и плотные блоки; XS — строки таблиц и ячейки.  

Состояния: Default, Hover, Press, Disable, Loading.
- **Size** (VARIANT): M, S, XS
- **Style** (VARIANT): Accent, Negative, Neutral, Positive, Warning
- **Type** (VARIANT): Filled, Outlined, Text
- **State** (VARIANT): Default, Disable, Hover, Loading, Press
- CSS: выверено вручную, см. `components/Button-Icon_DS/button-icon.css` в разделе «Полные CSS-стили всех компонентов»

#### Button icon group `[53828:5738]` — 2 вариантов
**Описание и рекомендации по применению:**
Группа кнопок-иконок — набор действий одной иконкой рядом: панель инструментов, действия в строке таблицы, шапка карточки.  
Всем кнопкам в группе давайте тултипы; разнородные действия не смешивайте в одну группу.  

Как выбрать вариант: Horizontally — в строку (основной случай), Vertically — в столбец для узких панелей.
- **Orientation** (VARIANT): Horizontally, Vertically
- Прочие свойства: Slot#60176:0 (SLOT)
- CSS: выверено вручную, см. `components/Button-Icon_DS/button-icon.css` в разделе «Полные CSS-стили всех компонентов»

#### Button toggle `[17039:71554]` — 12 вариантов
**Описание и рекомендации по применению:**
Кнопка-переключатель — кнопка с состоянием «нажата / не нажата»: режим отображения, фильтр, форматирование.  
Собирается в группы (Toggle buttons); для обычных действий берите Button, для действия одной иконкой — Button icon.  

Как выбрать вариант:  
Type=Filled — активный, выбранный переключатель; Type=Outlined — невыбранный.  
Content=Icon / Text — только иконка (режим понятен по иконке) / с текстом.  
Size=M, S, XS — по плотности интерфейса: M в формах, S и XS в таблицах и панелях.
- **Size** (VARIANT): M, S, XS
- **Type** (VARIANT): Filled, Outlined
- **Content** (VARIANT): Icon, Text
- Прочие свойства: Button container#59885:13 (SLOT)
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-button-toggle-pad-top, 4px) var(--ds-button-toggle-pad-right, 4px) var(--ds-button-toggle-pad-bottom, 4px) var(--ds-button-toggle-pad-left, 4px)`
    - промежуток между элементами: `var(--ds-button-toggle-gap, 4px)`
    - скругление: `var(--ds-button-toggle-border-radius, 12px)`
- Модификаторы (что меняет каждый):
    - `--filled`: фон `var(--ds-color-button-toggle-filled-background, #ffffff)`, color `var(--ds-color-button-accent-outlined-default-text-color, #448aff)`, рамка `none`, тень `none`
    - `--outlined`: фон `var(--ds-color-button-toggle-outlined-background, #ffffff)`, рамка `1px solid var(--ds-color-button-toggle-outlined-border-color, #e0e0e0)`, color `var(--ds-color-button-accent-filled-default-text-color, #ffffff)`, тень `none`
    - `--s`: ширина `var(--ds-size-5x)`, высота `var(--ds-size-5x)`
    - `--xs`: ширина `var(--ds-size-4x)`, высота `var(--ds-size-4x)`
- Разметка:

```html
<div class="ds-button-toggle ds-button-toggle--filled">
  <span class="ds-button-toggle__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-button-toggle__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-button-toggle {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-toggle-gap, 4px);
  padding: var(--ds-button-toggle-pad-top, 4px) var(--ds-button-toggle-pad-right, 4px) var(--ds-button-toggle-pad-bottom, 4px) var(--ds-button-toggle-pad-left, 4px);
  border-radius: var(--ds-button-toggle-border-radius, 12px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-button-toggle__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-button-accent-outlined-default-text-color, #448aff);
  white-space: nowrap;
}
.ds-button-toggle__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-button-toggle__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-button-toggle__icon svg path {
  fill: currentColor;
}
.ds-button-toggle--s .ds-button-toggle__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-button-toggle--xs .ds-button-toggle__icon {
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
}
.ds-button-toggle--filled.ds-button-toggle--text {
  background: var(--ds-color-button-toggle-filled-background, #ffffff);
  color: var(--ds-color-button-accent-outlined-default-text-color, #448aff);
  border: none;
  box-shadow: none;
}
.ds-button-toggle--outlined.ds-button-toggle--text {
  background: var(--ds-color-button-toggle-outlined-background, #ffffff);
  border: 1px solid var(--ds-color-button-toggle-outlined-border-color, #e0e0e0);
  color: var(--ds-color-button-accent-filled-default-text-color, #ffffff);
  box-shadow: none;
}
.ds-button-toggle--outlined.ds-button-toggle--icon {
  background: var(--ds-color-button-toggle-outlined-background, #ffffff);
  border: 1px solid var(--ds-color-button-toggle-outlined-border-color, #e0e0e0);
}
.ds-button-toggle--filled.ds-button-toggle--icon {
  background: var(--ds-color-button-toggle-filled-background, #ffffff);
}
```
</details>

#### Card content `[53744:3079]` — 2 вариантов
**Описание и рекомендации по применению:**
Содержимое карточки — область с текстом, значениями или своим набором элементов.  
Как выбрать вариант: готовая раскладка или собственное содержимое.
- **Content** (VARIANT): Custom, Default
- Прочие свойства: Title#56245:7 (BOOLEAN), Content#58799:0 (SLOT)
- CSS: выверено вручную, см. `components/Card_DS/card-view.css` в разделе «Полные CSS-стили всех компонентов»

#### Card footer `[53744:3139]` — 1 вариантов
**Описание и рекомендации по применению:**
Подвал карточки — кнопки или дополнительная информация под содержимым.  
Добавляйте его только если действия действительно есть — иначе карточка обходится без подвала.
- **Content** (VARIANT): Default
- Прочие свойства: Divider#53753:1 (BOOLEAN)
- CSS: выверено вручную, см. `components/Card_DS/card-view.css` в разделе «Полные CSS-стили всех компонентов»

#### Card header `[52916:15126]` — 1 вариантов
**Описание и рекомендации по применению:**
Шапка карточки — заголовок, подзаголовок и действия карточки.  
Действия ставьте справа кнопкой-иконкой; заголовок не дублируйте в содержимом.
- **Content** (VARIANT): Default
- Прочие свойства: Divider#53766:0 (BOOLEAN), Title#56245:0 (BOOLEAN), Label up#56245:1 (BOOLEAN), Label down#56245:2 (BOOLEAN)
- CSS: выверено вручную, см. `components/Card_DS/card-view.css` в разделе «Полные CSS-стили всех компонентов»

#### Card view `[53744:3181]` — 3 вариантов
**Описание и рекомендации по применению:**
Карточка целиком — блок с самостоятельным содержимым: карточка новости на главной iikoWeb, инвойс в E-invoice, карта гостя, адрес в колл-центре.  
Собирается из шапки (Card header), содержимого (Card content) и подвала (Card footer) — лишние части не добавляйте, если их нет на экране.  

Как выбрать вариант:  
Type=Filled — с заливкой, для плиток и списков карточек.  
Type=Outlined — с рамкой, когда карточек много и фон один.  
Type=Shadow — с тенью, когда карточка отделена от фона или кликабельна.
- **Type** (VARIANT): Filled, Outlined, Shadow
- Прочие свойства: Shadow#53237:9 (BOOLEAN)
- CSS: выверено вручную, см. `components/Card_DS/card-view.css` в разделе «Полные CSS-стили всех компонентов»

#### Checkbox `[53806:5694]` — 21 вариантов
**Описание и рекомендации по применению:**
Чекбокс — выбор нескольких независимых пунктов или включение отдельной настройки.  
Используйте, когда пунктов несколько и можно выбрать любое их число; если выбор строго один — берите Radio button, если это переключатель режима «вкл/выкл» — Slide toggle.  

Состав: квадратный индикатор без подписи. С подписью и support-текстом — Checkbox label; для набора пунктов с общим заголовком — Checkbox group.  

Как выбрать вариант:  
Type=Deselected / Selected — пункт не выбран / выбран.  
Type=Indeterminate — часть вложенных пунктов выбрана (родительский пункт списка).  
Variant=Normal / Error / Disable — обычный, с ошибкой (в группе не выбран обязательный пункт), недоступный.  

Состояния: Default, Hover, Press.
- **Variant** (VARIANT): Disable, Error, Normal
- **Type** (VARIANT): Deselected, Indeterminate, Selected
- **State** (VARIANT): Default, Hover, Press
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Checkbox group `[53810:889]` — 3 вариантов
**Описание и рекомендации по применению:**
Группа чекбоксов — набор пунктов выбора с общим заголовком и общим support-текстом или текстом ошибки.  
Используйте, когда пункты относятся к одному вопросу: «Товары и склад» с подсказкой «Выберите один вариант (обязательно)».  

Состав: заголовок группы (Support up), пункты Checkbox label, общий текст под группой (Support down) — в ошибке он становится текстом ошибки для всей группы.  

Как выбрать вариант:  
Orientation=Vertical — пункты в столбец, основной случай.  
Orientation=Horizontal — в строку, когда пунктов мало и они короткие.  
Orientation=Group — вложенная группа: родительский пункт и подчинённые под ним.
- **Orientation** (VARIANT): Group, Horizontal, Vertical
- Прочие свойства: Slot vertical#57252:0 (SLOT), Slot group#57252:4 (SLOT), Slot horizontal#57252:8 (SLOT), Support up#58195:66 (BOOLEAN), Support down#58195:70 (BOOLEAN)
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Checkbox label `[53810:880]` — 9 вариантов
**Описание и рекомендации по применению:**
Чекбокс с подписью — основной способ показать пункт выбора: индикатор + текст, при необходимости support-текст под подписью.  
Используйте в настройках и формах: «Фасовки у товаров», «Добавлять товары, которых не было в заказе».  

Состав: чекбокс слева или справа от подписи (Checkbox left / Checkbox right), Label, Support text.  
Кликабельна вся строка вместе с подписью — не ставьте отдельный текст рядом с чекбоксом.  

Как выбрать вариант:  
Type=Deselected / Selected / Inderterminate — не выбран / выбран / частичный выбор.  
Variant=Normal / Error / Disable — обычный, с ошибкой (support-текст становится текстом ошибки), недоступный.
- **Variant** (VARIANT): Disable, Error, Normal
- **Type** (VARIANT): Deselected, Inderterminate, Selected
- Прочие свойства: Checkbox left#17172:1340 (BOOLEAN), Checkbox right#17172:1349 (BOOLEAN), Label#54065:0 (BOOLEAN), Support text#58192:0 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-5x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-checkbox-label-gap-support, 4px)`
- Модификаторы (что меняет каждый):
    - `--disable`: color `var(--ds-color-checkbox-label-text-disable-color, #9e9e9e)`
    - `--error`: color `var(--ds-color-checkbox-label-text-color, #333333)`
    - `--normal`: color `var(--ds-color-checkbox-label-text-color, #333333)`
- Разметка:

```html
<div class="ds-checkbox-label ds-checkbox-label--disable">
  <div class="ds-checkbox-label__form"></div>
  <span class="ds-checkbox-label__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-checkbox-label__label">Текст</span>
  <div class="ds-checkbox-label__left"></div>
  <div class="ds-checkbox-label__right"></div>
  <span class="ds-checkbox-label__support">Текст</span>
  <div class="ds-checkbox-label__support-text"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-checkbox-label {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-checkbox-label-gap-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-checkbox-label__label {
  font-size: var(--ds-typography-font-size-3-5x);
  font-weight: var(--ds-typography-font-weight-regular);
  line-height: var(--ds-typography-line-height-5x);
  letter-spacing: 0.25px;
  color: var(--ds-color-checkbox-label-text-color, #333333);
  white-space: nowrap;
}
.ds-checkbox-label__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-checkbox-label__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-checkbox-label__icon svg path {
  fill: currentColor;
}
.ds-checkbox-label__form {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-checkbox-label-gap, 8px);
}
.ds-checkbox-label__left {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-checkbox-label__right {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-checkbox-label__support {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 var(--ds-checkbox-label-pad-left-support-7x, 28px);
}
.ds-checkbox-label__support-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-checkbox-label-text-support-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-checkbox-label-text-support-color, #616161);
}
.ds-checkbox-label--normal.ds-checkbox-label--deselected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--normal.ds-checkbox-label--selected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--normal.ds-checkbox-label--inderterminate {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--error.ds-checkbox-label--deselected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--error.ds-checkbox-label--selected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--error.ds-checkbox-label--inderterminate {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--disable.ds-checkbox-label--deselected {
  color: var(--ds-color-checkbox-label-text-disable-color, #9e9e9e);
}
.ds-checkbox-label--disable.ds-checkbox-label--selected {
  color: var(--ds-color-checkbox-label-text-disable-color, #9e9e9e);
}
.ds-checkbox-label--disable.ds-checkbox-label--inderterminate {
  color: var(--ds-color-checkbox-label-text-disable-color, #9e9e9e);
}
```
</details>

#### Chips `[17168:83542]` — 18 вариантов
**Описание и рекомендации по применению:**
Чип — компактная метка-фильтр или выбранное значение, которое можно снять: применённые фильтры над таблицей, выбранные товары, теги.  
Чип всегда относится к чему-то выбранному пользователем; для статуса объекта берите Status, для количества — Badge.  

Состав: текст, элемент слева (иконка или аватар) и элемент справа (крестик для снятия).  

Как выбрать вариант:  
Type=Filled — выбранный, активный чип; Outlined — доступный к выбору.  
Size=M — основной; S — плотные панели и строки таблиц.  
Состояния: Default, Hover, Focus, Press, Disable.
- **Size** (VARIANT): M, S
- **Type** (VARIANT): Filled, Outlined
- **State** (VARIANT): Default, Disable, Focus, Hover, Press
- Прочие свойства: Element left#17172:1340 (BOOLEAN), Element right#17172:1349 (BOOLEAN)
- Размеры и параметры:
    - высота: `var(--ds-size-8x)` (фикс.)
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-chips-m-size-pad-top, 6px) var(--ds-chips-m-size-pad-right, 8px) var(--ds-chips-m-size-pad-bottom, 6px) var(--ds-chips-m-size-pad-left, 8px)`
    - промежуток между элементами: `var(--ds-chips-m-size-gap, 8px)`
    - скругление: `var(--ds-chips-m-size-border-radius, 12px)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--filled`: фон `var(--ds-color-chips-filled-default-background, #f8f9fc)`, color `var(--ds-color-chips-text-color, #333333)`, фон `var(--ds-color-chips-disable-background-filled, #ebebeb)`, color `var(--ds-color-chips-disable-text-color, #9e9e9e)`
    - `--outlined`: фон `var(--ds-color-chips-outlined-default-background, #ffffff)`, рамка `1px solid var(--ds-color-chips-outlined-default-border-color, #e0e0e0)`, color `var(--ds-color-chips-text-color, #333333)`, фон `var(--ds-color-chips-disable-background-outlined, #ffffff)`
    - `--s`: промежуток между элементами `var(--ds-chips-s-size-gap, 4px)`, внутренние отступы `var(--ds-chips-s-size-pad-top, 4px) var(--ds-chips-s-size-pad-right, 6px) var(--ds-chips-s-size-pad-bottom, 4px) var(--ds-chips-s-size-pad-left, 6px)`, скругление `var(--ds-chips-s-size-border-radius, 8px)`, ширина `var(--ds-size-4x)`
- Состояния: `:active` (нажатие), `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-chips ds-chips--disabled">
  <div class="ds-chips__add"></div>
  <div class="ds-chips__chip-container"></div>
  <div class="ds-chips__chip-text"></div>
  <div class="ds-chips__close"></div>
  <span class="ds-chips__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-chips__icon-size"></div>
  <span class="ds-chips__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-chips {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  height: var(--ds-size-8x);
  padding: var(--ds-chips-m-size-pad-top, 6px) var(--ds-chips-m-size-pad-right, 8px) var(--ds-chips-m-size-pad-bottom, 6px) var(--ds-chips-m-size-pad-left, 8px);
  gap: var(--ds-chips-m-size-gap, 8px);
  border-radius: var(--ds-chips-m-size-border-radius, 12px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-chips-text-color, #333333);
  white-space: nowrap;
}
.ds-chips__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips__icon svg path {
  fill: currentColor;
}
.ds-chips__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-chips__add {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-chips__chip-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
}
.ds-chips__chip-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-chips-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-chips-text-color, #333333);
}
.ds-chips__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-chips--s {
  gap: var(--ds-chips-s-size-gap, 4px);
  padding: var(--ds-chips-s-size-pad-top, 4px) var(--ds-chips-s-size-pad-right, 6px) var(--ds-chips-s-size-pad-bottom, 4px) var(--ds-chips-s-size-pad-left, 6px);
  border-radius: var(--ds-chips-s-size-border-radius, 8px);
}
.ds-chips--s .ds-chips__icon {
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
}
.ds-chips--outlined {
  background: var(--ds-color-chips-outlined-default-background, #ffffff);
  border: 1px solid var(--ds-color-chips-outlined-default-border-color, #e0e0e0);
  color: var(--ds-color-chips-text-color, #333333);
}
.ds-chips--outlined:hover {
  background: var(--ds-color-chips-outlined-hover-background, #ffffff);
  border: 1px solid var(--ds-color-chips-outlined-hover-border-color, #9e9e9e);
}
.ds-chips--outlined:focus-visible {
  background: var(--ds-color-chips-outlined-focus-background, #ffffff);
}
.ds-chips--outlined:active {
  background: var(--ds-color-chips-outlined-press-background, #e0e0e0);
  border: 1px solid var(--ds-color-chips-outlined-press-border-color, #e0e0e0);
}
.ds-chips--outlined:disabled {
  background: var(--ds-color-chips-disable-background-outlined, #ffffff);
  border: 1px solid var(--ds-color-chips-disable-border-color, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--outlined.ds-chips--disabled {
  background: var(--ds-color-chips-disable-background-outlined, #ffffff);
  border: 1px solid var(--ds-color-chips-disable-border-color, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--filled {
  background: var(--ds-color-chips-filled-default-background, #f8f9fc);
  color: var(--ds-color-chips-text-color, #333333);
}
.ds-chips--filled:hover {
  background: var(--ds-color-chips-filled-hover-background, #f5f5f5);
}
.ds-chips--filled:active {
  background: var(--ds-color-chips-filled-press-background, #e0e0e0);
}
.ds-chips--filled:disabled {
  background: var(--ds-color-chips-disable-background-filled, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--filled.ds-chips--disabled {
  background: var(--ds-color-chips-disable-background-filled, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--disabled {
  pointer-events: none;
}
```
</details>

#### Chips group `[55750:5485]` — 2 вариантов
**Описание и рекомендации по применению:**
Группа чипов — набор фильтров или выбранных значений в один ряд с переносом на новую строку.  
Берите группу, чтобы зазоры и перенос были одинаковыми; при большом числе чипов сворачивайте лишние в «ещё N».  

Как выбрать вариант: по размеру чипов в группе.
- **Size** (VARIANT): M, S
- Прочие свойства: Slot#60220:1 (SLOT)
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-chips-gap-group, 8px)`
- Модификаторы (что меняет каждый):
    - `--s`: ширина `var(--ds-size-4x)`, высота `var(--ds-size-4x)`
- Разметка:

```html
<div class="ds-chips-group ds-chips-group--s">
  <span class="ds-chips-group__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-chips-group__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-chips-group {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-chips-gap-group, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-group__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-chips-text-color, #333333);
  white-space: nowrap;
}
.ds-chips-group__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-group__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-group__icon svg path {
  fill: currentColor;
}
.ds-chips-group--s .ds-chips-group__icon {
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
}
```
</details>

#### Chips Input `[52916:14622]` — 16 вариантов
**Описание и рекомендации по применению:**
Поле ввода тегов — несколько значений в одном поле, каждое становится чипом: список товаров, получатели, метки.  
Берите его, когда значений несколько и их набирают вручную; для одного значения из справочника — Autocomplete, для выбора из списка — Select.  

Как выбрать вариант:  
Size=M — основной; S — плотные формы и панели.  
Состояния: Default, Hover, Focus, Focus+Placeholder, Focus+Value, Error, Error+Hover, Disable.
- **Size** (VARIANT): M, S
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Focus+Value, Hover
- Прочие свойства: Support text#55693:0 (BOOLEAN), Element right#55751:38 (BOOLEAN), Support#59392:7 (BOOLEAN), Hint text#59430:0 (BOOLEAN), Label text value#59432:1 (TEXT), Support text value#59437:20 (TEXT), Hint text value#59437:40 (TEXT), Action text#59437:60 (BOOLEAN), Action text value#59437:80 (TEXT), Placeholder value#59507:0 (TEXT), Text value#59507:16 (TEXT), Slot#60231:21 (SLOT)
- Размеры и параметры:
    - ширина: `280px` (фикс.)
    - промежуток между элементами: `var(--ds-size-1x)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--s`: промежуток между элементами `var(--ds-form-field-gap-input-support, 4px)`, ширина `var(--ds-size-5x)`, высота `var(--ds-size-5x)`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-chips-input ds-chips-input--disabled">
  <div class="ds-chips-input__content"></div>
  <div class="ds-chips-input__frame"></div>
  <span class="ds-chips-input__hint">Текст</span>
  <span class="ds-chips-input__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-chips-input__label">Текст</span>
  <span class="ds-chips-input__support">Текст</span>
  <span class="ds-chips-input__text">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-chips-input {
  width: 280px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-1x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-input__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-chips-input__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-input__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-input__icon svg path {
  fill: currentColor;
}
.ds-chips-input__frame {
  display: flex;
  flex-direction: column;
  gap: var(--ds-chips-input-gap-chips-input-frame, 4px);
  padding: var(--ds-chips-input-m-size-pad-top, 4px) var(--ds-size-3x) var(--ds-chips-input-m-size-pad-bottom, 8px) var(--ds-size-3x);
  border-radius: var(--ds-size-3x);
  background: #f8f9fc;
  border: 1px solid #e0e0e0;
}
.ds-chips-input__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
}
.ds-chips-input__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-1x);
}
.ds-chips-input__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-size-3x) 0 var(--ds-size-3x);
}
.ds-chips-input__hint {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-size-3x) 0 var(--ds-size-3x);
}
.ds-chips-input--s {
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-chips-input--s .ds-chips-input__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-chips-input:hover {
  background: #f5f5f5;
  border: 1px solid #9e9e9e;
}
.ds-chips-input:focus-visible {
  color: #448aff;
}
.ds-chips-input:disabled {
  color: #9e9e9e;
}
.ds-chips-input.ds-chips-input--disabled {
  color: #9e9e9e;
}
.ds-chips-input--disabled {
  pointer-events: none;
}
```
</details>

#### Chips Input `[61382:55775]` — 16 вариантов
_Описание компонента в Figma отсутствует._
- **Size** (VARIANT): M, S
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Focus+Value, Hover
- Прочие свойства: Support text#55693:0 (BOOLEAN), Element right#55751:38 (BOOLEAN), Support#59392:7 (BOOLEAN), Hint text#59430:0 (BOOLEAN), Label text value#59432:1 (TEXT), Support text value#59437:20 (TEXT), Hint text value#59437:40 (TEXT), Action text#59437:60 (BOOLEAN), Action text value#59437:80 (TEXT), Placeholder value#59507:0 (TEXT), Text value#59507:16 (TEXT), Slot#60231:21 (SLOT)
- Размеры и параметры:
    - ширина: `280px` (фикс.)
    - промежуток между элементами: `var(--ds-form-field-gap-input-support, 4px)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--s`: ширина `var(--ds-size-5x)`, высота `var(--ds-size-5x)`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-chips-input-2 ds-chips-input-2--disabled">
  <div class="ds-chips-input-2__content"></div>
  <div class="ds-chips-input-2__frame"></div>
  <span class="ds-chips-input-2__hint">Текст</span>
  <span class="ds-chips-input-2__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-chips-input-2__label">Текст</span>
  <span class="ds-chips-input-2__support">Текст</span>
  <span class="ds-chips-input-2__text">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-chips-input-2 {
  width: 280px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-input-2__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-chips-input-2__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-input-2__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-input-2__icon svg path {
  fill: currentColor;
}
.ds-chips-input-2__frame {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-chips-input-2__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-content);
}
.ds-chips-input-2__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-chips-input-2__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-chips-input-2__hint {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-chips-input-2--s .ds-chips-input-2__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-chips-input-2:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-chips-input-2:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-chips-input-2:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-chips-input-2.ds-chips-input-2--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-chips-input-2--disabled {
  pointer-events: none;
}
```
</details>

#### Chips input cell `[60231:75648]` — 8 вариантов
**Описание и рекомендации по применению:**
Ввод тегов внутри ячейки таблицы — несколько значений прямо в строке: комплектующие, метки, склады.  
Используйте в редактируемых таблицах; вне таблицы берите Chips Input.  

Состояния: Default, Hover, Focus, Focus+Placeholder, Focus+Value, Error, Error+Hover, Disable.
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Focus+Value, Hover
- Размеры и параметры:
    - высота: минимум `var(--ds-size-10x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px)`
    - промежуток между элементами: `var(--ds-size-2x)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-chips-input-cell ds-chips-input-cell--disabled">
  <div class="ds-chips-input-cell__frame"></div>
  <span class="ds-chips-input-cell__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-chips-input-cell__label">Текст</span>
  <span class="ds-chips-input-cell__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-chips-input-cell {
  min-height: var(--ds-size-10x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-input-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-chips-input-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-input-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-input-cell__icon svg path {
  fill: currentColor;
}
.ds-chips-input-cell__frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-chips-input-gap-chips-input-frame, 4px);
  border-radius: var(--ds-size-3x);
  background: #f8f9fc;
  border: 1px solid #e0e0e0;
}
.ds-chips-input-cell__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-1x);
}
.ds-chips-input-cell:hover {
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-chips-input-cell:focus-visible {
  color: #333333;
}
.ds-chips-input-cell:disabled {
  color: #9e9e9e;
}
.ds-chips-input-cell.ds-chips-input-cell--disabled {
  color: #9e9e9e;
}
.ds-chips-input-cell--disabled {
  pointer-events: none;
}
```
</details>

#### Control arrow button `[52868:3935]` — 3 вариантов
**Описание и рекомендации по применению:**
Кнопка-стрелка — шаг по списку или календарю: предыдущий и следующий месяц, прокрутка вкладок, перелистывание.  
Используйте парой (назад и вперёд); когда шаг недоступен — блокируйте кнопку, а не убирайте её.  

Как выбрать вариант: по размеру блока, в котором стоит кнопка.
- **Size** (VARIANT): M, S, XS
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-0-5x)`
- Модификаторы (что меняет каждый):
    - `--s`: ширина `var(--ds-size-3x)`, высота `var(--ds-size-3x)`
- Разметка:

```html
<div class="ds-control-arrow-button ds-control-arrow-button--s">
  <span class="ds-control-arrow-button__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-control-arrow-button__icon-size"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-control-arrow-button {
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-0-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-control-arrow-button__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-control-arrow-button__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-control-arrow-button__icon svg path {
  fill: currentColor;
}
.ds-control-arrow-button__icon-size {
  height: var(--ds-size-3x);
  display: flex;
  flex-direction: row;
}
.ds-control-arrow-button--s .ds-control-arrow-button__icon {
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
}
```
</details>

#### Control Panel `[58501:4052]` — 3 вариантов
**Описание и рекомендации по применению:**
Панель управления календарём — переключение месяца и года, строка дней недели над сеткой.  
Служебный компонент календаря: используется внутри Datepicker.  

Как выбрать вариант: панель переключения периода, строка дней недели или заголовок сетки.
- **Type** (VARIANT): Calendar, Control, Week
- Прочие свойства: Slot Week#58546:5 (SLOT)
- Размеры и параметры:
    - ширина: `280px` (фикс.)
    - внутренние отступы: `var(--ds-size-1x) 0 var(--ds-size-1x) 0`
    - промежуток между элементами: `74px`
- Модификаторы (что меняет каждый):
    - `--calendar`: ширина `fit-content`, направление `column`, align-items `center`, фон `#ffffff`
    - `--control`: направление `row`, align-items `center`, color `var(--ds-color-text-primary, #333333)`
    - `--week`: ширина `fit-content`, направление `row`, внутренние отступы `var(--ds-size-0-5x) 0 var(--ds-size-0-5x) 0`, color `var(--ds-color-text-primary, #333333)`
- Разметка:

```html
<div class="ds-control-panel ds-control-panel--calendar">
  <div class="ds-control-panel__button-icon"></div>
  <div class="ds-control-panel__button-icon-group"></div>
  <div class="ds-control-panel__elements"></div>
  <span class="ds-control-panel__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-control-panel__label">Текст</span>
  <div class="ds-control-panel__month"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-control-panel {
  display: flex;
  width: 280px;
  padding: var(--ds-size-1x) 0 var(--ds-size-1x) 0;
  gap: 74px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-control-panel__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-control-panel__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-control-panel__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-control-panel__icon svg path {
  fill: currentColor;
}
.ds-control-panel__elements {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-control-panel__month {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-primary, #333333);
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel__button-icon-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
}
.ds-control-panel__button-icon {
  display: flex;
  flex-direction: row;
  gap: var(--ds-button-icon-gap, 8px);
  padding: var(--ds-button-icon-m-size-pad-top, 8px) var(--ds-button-icon-m-size-pad-right, 8px) var(--ds-button-icon-m-size-pad-bottom, 8px) var(--ds-button-icon-m-size-pad-left, 8px);
  border-radius: var(--ds-button-icon-border-radius, 8px);
}
.ds-control-panel--control {
  flex-direction: row;
  align-items: center;
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel--week {
  width: fit-content;
  flex-direction: row;
  padding: var(--ds-size-0-5x) 0 var(--ds-size-0-5x) 0;
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel--calendar {
  width: fit-content;
  flex-direction: column;
  align-items: center;
  background: #ffffff;
  color: var(--ds-color-text-primary, #333333);
}
```
</details>

#### Control Panel `[58982:11018]` — 2 вариантов
**Описание и рекомендации по применению:**
Панель управления выбором времени — заголовок и переключение между часами и минутами.  
Служебный компонент выбора времени: используется внутри Timepicker.  

Как выбрать вариант: панель переключения или строка со значением времени.
- **Type** (VARIANT): Control, Time
- Прочие свойства: Slot Time#58546:5 (SLOT)
- Размеры и параметры:
    - ширина: `280px` (фикс.)
    - внутренние отступы: `var(--ds-size-1x) 0 var(--ds-size-1x) 0`
    - промежуток между элементами: `74px`
- Модификаторы (что меняет каждый):
    - `--control`: align-items `center`, color `var(--ds-color-text-primary, #333333)`
    - `--time`: ширина `fit-content`, внутренние отступы `var(--ds-size-0-5x) 0 var(--ds-size-0-5x) 0`, color `var(--ds-color-text-primary, #333333)`
- Разметка:

```html
<div class="ds-control-panel-2 ds-control-panel-2--control">
  <div class="ds-control-panel-2__button-icon-group"></div>
  <div class="ds-control-panel-2__elements"></div>
  <span class="ds-control-panel-2__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-control-panel-2__label">Текст</span>
  <div class="ds-control-panel-2__month"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-control-panel-2 {
  display: flex;
  flex-direction: row;
  width: 280px;
  padding: var(--ds-size-1x) 0 var(--ds-size-1x) 0;
  gap: 74px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-control-panel-2__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-control-panel-2__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-control-panel-2__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-control-panel-2__icon svg path {
  fill: currentColor;
}
.ds-control-panel-2__elements {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-control-panel-2__month {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-primary, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel-2__button-icon-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-icon-gap, 8px);
}
.ds-control-panel-2--control {
  align-items: center;
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel-2--time {
  width: fit-content;
  padding: var(--ds-size-0-5x) 0 var(--ds-size-0-5x) 0;
  color: var(--ds-color-text-primary, #333333);
}
```
</details>

#### Datepicker `[58509:5439]` — 3 вариантов
**Описание и рекомендации по применению:**
Календарь — выбор даты или периода: дата поставки, период отчёта, срок.  
Открывается из поля даты (Input Datepicker); отдельно на экране не живёт.  

Как выбрать вариант:  
Type=Day — сетка дней месяца, основной вид.  
Type=Month — выбор месяца.  
Type=Year — выбор года.
- **Type** (VARIANT): Day, Month, Year
- Прочие свойства: Headline#53001:0 (TEXT), Supporting text#53001:4 (TEXT), Supporting text (range)#53001:8 (TEXT), Headline (range)#53001:12 (TEXT), Show clear button#54584:0 (BOOLEAN), show controls#58548:10 (BOOLEAN)
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x)`
    - скругление: `var(--ds-size-3x)`
    - рамка: `1px solid var(--ds-color-stroke-default, #e0e0e0)`
- Модификаторы (что меняет каждый):
    - `--day`: color `var(--ds-color-text-primary, #333333)`
    - `--month`: color `var(--ds-color-text-primary, #333333)`
    - `--year`: color `var(--ds-color-text-primary, #333333)`
- Разметка:

```html
<div class="ds-datepicker ds-datepicker--day">
  <div class="ds-datepicker__button-icon-group"></div>
  <div class="ds-datepicker__control-panel"></div>
  <div class="ds-datepicker__divider"></div>
  <div class="ds-datepicker__elements"></div>
  <span class="ds-datepicker__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-datepicker__label">Текст</span>
  <div class="ds-datepicker__week-6"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-datepicker {
  width: fit-content;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  border-radius: var(--ds-size-3x);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-datepicker__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-datepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-datepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-datepicker__icon svg path {
  fill: currentColor;
}
.ds-datepicker__control-panel {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 74px;
  padding: var(--ds-size-1x) 0 var(--ds-size-1x) 0;
}
.ds-datepicker__elements {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-datepicker__button-icon-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
}
.ds-datepicker__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-datepicker__week-6 {
  height: 48px;
  display: flex;
  flex-direction: row;
}
.ds-datepicker--day {
  color: var(--ds-color-text-primary, #333333);
}
.ds-datepicker--year {
  color: var(--ds-color-text-primary, #333333);
}
.ds-datepicker--month {
  color: var(--ds-color-text-primary, #333333);
}
```
</details>

#### Dialog content `[53535:1369]` — 1 вариантов
**Описание и рекомендации по применению:**
Содержимое диалога — область под шапкой: текст, форма, таблица.  
При длинном содержимом прокручивается именно эта область, шапка и подвал остаются на месте.
- **State** (VARIANT): Default
- Прочие свойства: Slot#58937:21 (SLOT), Scroll#58937:24 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `204px`, растёт по контенту
    - ширина: `500px` (фикс.)
    - фон: `var(--ds-color-dialog-background, #ffffff)`
- Разметка:

```html
<div class="ds-dialog-content">
  <div class="ds-dialog-content__background"></div>
  <span class="ds-dialog-content__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-dialog-content__label">Текст</span>
  <div class="ds-dialog-content__scroll"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-dialog-content {
  min-height: 204px;
  width: 500px;
  display: flex;
  flex-direction: row;
  background: var(--ds-color-dialog-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-content__label {
  font-size: var(--ds-font-body-m-16-normal-medium-size);
  line-height: var(--ds-font-body-m-16-normal-medium-line);
  letter-spacing: var(--ds-font-body-m-16-normal-medium-spacing);
  font-weight: var(--ds-font-body-m-16-normal-medium-weight);
  color: var(--ds-color-dialog-content-title-color, #333333);
  white-space: nowrap;
}
.ds-dialog-content__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-content__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-content__icon svg path {
  fill: currentColor;
}
.ds-dialog-content__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-dialog-content__background {
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-scroll-border-radius, 8px);
  background: var(--ds-color-scroll-default-background, #fafafa);
}
```
</details>

#### Dialog footer `[53749:638]` — 1 вариантов
**Описание и рекомендации по применению:**
Подвал диалога — кнопки действий окна: главное действие справа, отмена слева от него.  
Главное действие называйте по смыслу («Создать», «Сохранить»), а не «ОК».
- **State** (VARIANT): Default
- Прочие свойства: Divider#53749:3 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `69px`, растёт по контенту
    - ширина: `501px` (фикс.)
    - фон: `var(--ds-color-dialog-background, #ffffff)`
- Разметка:

```html
<div class="ds-dialog-footer">
  <div class="ds-dialog-footer__action"></div>
  <div class="ds-dialog-footer__button"></div>
  <div class="ds-dialog-footer__divider"></div>
  <span class="ds-dialog-footer__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-dialog-footer__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-dialog-footer {
  min-height: 69px;
  width: 501px;
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-footer__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-button-accent-filled-default-text-color, #ffffff);
  white-space: nowrap;
}
.ds-dialog-footer__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-footer__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-footer__icon svg path {
  fill: currentColor;
}
.ds-dialog-footer__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-dialog-footer__action {
  height: 68px;
  display: flex;
  flex-direction: column;
  padding: var(--ds-dialog-footer-pad-top, 16px) var(--ds-dialog-footer-pad-right, 24px) var(--ds-dialog-footer-pad-bottom, 16px) var(--ds-dialog-footer-pad-left, 24px);
}
.ds-dialog-footer__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-m-size-gap, 8px);
  padding: var(--ds-button-m-size-pad-top, 8px) var(--ds-button-m-size-pad-right, 12px) var(--ds-button-m-size-pad-bottom, 8px) var(--ds-button-m-size-pad-left, 12px);
  border-radius: var(--ds-button-border-radius, 8px);
  background: var(--ds-color-button-accent-filled-default-background, #448aff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
}
```
</details>

#### Dialog header `[53535:1322]` — 2 вариантов
**Описание и рекомендации по применению:**
Шапка диалога — заголовок окна и кнопка закрытия, при необходимости картинка над заголовком.  
Заголовок формулируйте по задаче окна («Создание накладной»), а не «Внимание».  

Как выбрать вариант: только текст или с картинкой сверху.
- **Type** (VARIANT): Picture, Text
- Прочие свойства: Divider#53619:9 (BOOLEAN), Close#59197:0 (BOOLEAN), Picture#59215:10 (SLOT), Description#59215:16 (BOOLEAN)
- Размеры и параметры:
    - ширина: `500px` (фикс.)
    - фон: `var(--ds-color-dialog-background, #ffffff)`
- Модификаторы (что меняет каждый):
    - `--text`: color `var(--ds-color-dialog-header-title-color, #333333)`
- Разметка:

```html
<div class="ds-dialog-header ds-dialog-header--text">
  <div class="ds-dialog-header__description"></div>
  <div class="ds-dialog-header__divider"></div>
  <span class="ds-dialog-header__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-dialog-header__label">Текст</span>
  <div class="ds-dialog-header__title-container"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-dialog-header {
  width: 500px;
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-header__label {
  font-size: var(--ds-font-header-s-20-normal-medium-size);
  line-height: var(--ds-font-header-s-20-normal-medium-line);
  letter-spacing: var(--ds-font-header-s-20-normal-medium-spacing);
  font-weight: var(--ds-font-header-s-20-normal-medium-weight);
  color: var(--ds-color-dialog-header-title-color, #333333);
  white-space: nowrap;
}
.ds-dialog-header__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-header__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-header__icon svg path {
  fill: currentColor;
}
.ds-dialog-header__title-container {
  display: flex;
  flex-direction: row;
  gap: var(--ds-dialog-header-gap, 8px);
}
.ds-dialog-header__description {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-dialog-header-desc-color, #616161);
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-dialog-header-desc-color, #616161);
}
.ds-dialog-header__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-dialog-header--text {
  color: var(--ds-color-dialog-header-title-color, #333333);
}
```
</details>

#### Dialog view `[52952:1285]` — 1 вариантов
**Описание и рекомендации по применению:**
Диалог целиком — модальное окно поверх экрана: подтверждение, форма создания, просмотр записи.  
Берите его как основу окна: шапка (Dialog header), содержимое (Dialog content), подвал с кнопками (Dialog footer), затемнение под окном (Backdrop).  
Закрытие — крестик в шапке и кнопка в подвале; не оставляйте окно без явного способа закрыть.
- **State** (VARIANT): Default
- Прочие свойства: Content#58947:4 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `364px`, растёт по контенту
    - ширина: `500px` (фикс.)
    - скругление: `var(--ds-dialog-border-radius, 12px)`
    - фон: `var(--ds-color-dialog-background, #ffffff)`
    - тень: `var(--ds-shadow-shadows-12-dp-m)`
- Разметка:

```html
<div class="ds-dialog-view">
  <div class="ds-dialog-view__action"></div>
  <div class="ds-dialog-view__content"></div>
  <div class="ds-dialog-view__divider"></div>
  <div class="ds-dialog-view__footer"></div>
  <div class="ds-dialog-view__header"></div>
  <span class="ds-dialog-view__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-dialog-view__label">Текст</span>
  <div class="ds-dialog-view__scroll"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-dialog-view {
  min-height: 364px;
  width: 500px;
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-dialog-border-radius, 12px);
  background: var(--ds-color-dialog-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-12-dp-m);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-view__label {
  font-size: var(--ds-font-header-s-20-normal-medium-size);
  line-height: var(--ds-font-header-s-20-normal-medium-line);
  letter-spacing: var(--ds-font-header-s-20-normal-medium-spacing);
  font-weight: var(--ds-font-header-s-20-normal-medium-weight);
  color: var(--ds-color-dialog-header-title-color, #333333);
  white-space: nowrap;
}
.ds-dialog-view__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-view__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-view__icon svg path {
  fill: currentColor;
}
.ds-dialog-view__header {
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
}
.ds-dialog-view__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-dialog-view__content {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-dialog-background, #ffffff);
}
.ds-dialog-view__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-dialog-view__footer {
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
}
.ds-dialog-view__action {
  height: 68px;
  display: flex;
  flex-direction: column;
  padding: var(--ds-dialog-footer-pad-top, 16px) var(--ds-dialog-footer-pad-right, 24px) var(--ds-dialog-footer-pad-bottom, 16px) var(--ds-dialog-footer-pad-left, 24px);
}
```
</details>

#### Divider `[58320:441]` — 16 вариантов
**Описание и рекомендации по применению:**
Разделитель с состояниями — линия между блоками, которую можно перетаскивать: граница колонок таблицы, граница панелей.  
Лежит на странице UI components (раздел «не готовы или под вопросом») — перед использованием уточните актуальность у владельца ДС. Обычная линия-разделитель — компонент Divider со страницы Divider.  

Как выбрать вариант:  
Type=Solid — сплошная; Dashed — пунктирная (граница, которую можно двигать).  
Size=M, L — по длине и толщине линии.  
Состояния: Lite, Default, Hover, Selected, Disable.
- **Size** (VARIANT): L, M
- **Type** (VARIANT): Dashed, Solid
- **State** (VARIANT): Default, Disable, Hover, Lite, Selected
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Divider `[53556:7964]` — 1 вариантов
**Описание и рекомендации по применению:**
Разделитель — тонкая линия между блоками или пунктами списка.  
Берите его вместо рамки, когда нужно только разделить содержимое; не ставьте разделители там, где хватает отступа.
- **Type** (VARIANT): Solid
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Element `[54104:20956]` — 9 вариантов
**Описание и рекомендации по применению:**
Слот элемента в пункте списка — выбирает, что стоит слева или справа от текста пункта: иконка, картинка, чекбокс, переключатель, счётчик.  
Служебный компонент списка: подставляется в List item, отдельно на экран не ставится.  

Как выбрать вариант: по тому, что показывает пункт.
- **Content** (VARIANT): Checkbox, Counter, Icon group, Icon size, Image size, Indicator, Radio button, Slide toggle, Text default
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-2-5x)`
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--checkbox`: направление `row`
    - `--counter`: направление `column`, color `var(--ds-color-badge-text-color, #ffffff)`
    - `--icon-group`: направление `row`, align-items `center`
    - `--icon-size`: направление `row`, align-items `center`
    - `--image-size`: направление `row`, align-items `center`
    - `--indicator`: ширина `var(--ds-size-6x)`, направление `row`
    - `--radio-button`: направление `row`
    - `--slide-toggle`: направление `row`, color `var(--ds-color-slide-toggle-text-color, #333333)`
    - `--text-default`: направление `row`, color `var(--ds-color-brand-neutral-super-dark, #333333)`
- Разметка:

```html
<div class="ds-element ds-element--checkbox">
  <span class="ds-element__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-element__image-size"></div>
  <span class="ds-element__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-element {
  display: flex;
  background: #ffffff;
  width: fit-content;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element__icon svg path {
  fill: currentColor;
}
.ds-element__image-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-size-circular);
}
.ds-element--image-size {
  flex-direction: row;
  align-items: center;
}
.ds-element--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element--icon-group {
  flex-direction: row;
  align-items: center;
}
.ds-element--text-default {
  flex-direction: row;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element--checkbox {
  flex-direction: row;
}
.ds-element--radio-button {
  flex-direction: row;
}
.ds-element--indicator {
  width: var(--ds-size-6x);
  flex-direction: row;
}
.ds-element--slide-toggle {
  flex-direction: row;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-element--counter {
  flex-direction: column;
  color: var(--ds-color-badge-text-color, #ffffff);
}
```
</details>

#### Element cell `[58885:32432]` — 11 вариантов
**Описание и рекомендации по применению:**
Слот содержимого ячейки таблицы — выбирает, что стоит внутри ячейки: текст, иконка, кнопка, статус, поле ввода.  
Служебный компонент таблицы: подставляется в ячейку, отдельно на экран не ставится.  

Как выбрать вариант: по тому, что показывает ячейка.
- **Variant** (VARIANT): Button, Button icon, Cell Input, Checkbox, Chips, Icon group, Icon size, Input number, Slide toggle, Status, Text UI
- CSS не требуется: это **слот-контейнер** — пустая обёртка под вложенный компонент (иконку, ячейку). Оформление задаёт вложенный компонент, а размер — контент.

#### Element Form Field `[60231:76795]` — 3 вариантов
**Описание и рекомендации по применению:**
Слот поля внутри ячейки таблицы — выбирает, какое именно поле ввода стоит в редактируемой ячейке.  
Служебный компонент таблицы: подставляется внутрь ячейки, отдельно на экран не ставится.  

Как выбрать вариант: по типу значения в ячейке — обычный ввод, выбор из списка или ввод тегов.
- **Variant** (VARIANT): Chips input cell, Input cell, Select cell
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--chips-input-cell`: color `#616161`
    - `--input-cell`: color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`
    - `--select-cell`: color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`
- Разметка:

```html
<div class="ds-element-form-field ds-element-form-field--chips-input-cell">
  <div class="ds-element-form-field__input"></div>
  <div class="ds-element-form-field__input-cell"></div>
  <span class="ds-element-form-field__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-element-form-field {
  width: fit-content;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-form-field__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-element-form-field__input-cell {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
}
.ds-element-form-field__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-element-form-field--input-cell {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-element-form-field--select-cell {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-element-form-field--chips-input-cell {
  color: #616161;
}
```
</details>

#### Element left `[59851:11313]` — 5 вариантов
**Описание и рекомендации по применению:**
Иконка слева во всплывающем сообщении — показывает характер сообщения.  
Служебный элемент Snackbar: цвет выбирайте по смыслу сообщения, отдельно на экран не ставится.
- **Style** (VARIANT): Accent, Negative, Neutral, Positive, Warning
- Размеры и параметры:
    - высота: минимум `var(--ds-size-5x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-2-5x)`
- Разметка:

```html
<div class="ds-element-left">
  <span class="ds-element-left__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-element-left__info"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-element-left {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-left__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-left__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-left__icon svg path {
  fill: currentColor;
}
.ds-element-left__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
```
</details>

#### Element menu `[56090:1611]` — 8 вариантов
**Описание и рекомендации по применению:**
Слот элемента в пункте меню — выбирает, что стоит рядом с названием пункта: иконка, картинка, чекбокс, переключатель, счётчик.  
Служебный компонент меню: подставляется в Menu item, отдельно на экран не ставится.  

Как выбрать вариант: по тому, что показывает пункт меню.
- **Content** (VARIANT): Checkbox, Counter, Icon size, Image size, Indicator, Radio button, Slide toggle, Text default
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-2-5x)`
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--checkbox`: направление `row`
    - `--counter`: направление `column`, color `var(--ds-color-badge-text-color, #ffffff)`
    - `--icon-size`: направление `row`, align-items `center`
    - `--image-size`: направление `row`, align-items `center`
    - `--indicator`: ширина `var(--ds-size-6x)`, направление `row`
    - `--radio-button`: направление `row`
    - `--slide-toggle`: направление `row`, color `var(--ds-color-slide-toggle-text-color, #333333)`
    - `--text-default`: направление `row`, color `var(--ds-color-brand-neutral-super-dark, #333333)`
- Разметка:

```html
<div class="ds-element-menu ds-element-menu--checkbox">
  <span class="ds-element-menu__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-element-menu__image-size"></div>
  <span class="ds-element-menu__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-element-menu {
  display: flex;
  background: #ffffff;
  width: fit-content;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-menu__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element-menu__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-menu__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-menu__icon svg path {
  fill: currentColor;
}
.ds-element-menu__image-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-size-circular);
}
.ds-element-menu--image-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-menu--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-menu--text-default {
  flex-direction: row;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element-menu--checkbox {
  flex-direction: row;
}
.ds-element-menu--radio-button {
  flex-direction: row;
}
.ds-element-menu--indicator {
  width: var(--ds-size-6x);
  flex-direction: row;
}
.ds-element-menu--slide-toggle {
  flex-direction: row;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-element-menu--counter {
  flex-direction: column;
  color: var(--ds-color-badge-text-color, #ffffff);
}
```
</details>

#### Element select `[57735:17972]` — 8 вариантов
**Описание и рекомендации по применению:**
Слот элемента в пункте списка выбора — выбирает, что стоит рядом со значением: иконка, картинка, чекбокс, переключатель, счётчик.  
Служебный компонент Select: подставляется в Select item, отдельно на экран не ставится.  

Как выбрать вариант: по тому, что показывает пункт списка выбора.
- **Content** (VARIANT): Checkbox, Counter, Icon size, Image size, Indicator, Radio button, Slide toggle, Text default
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-2-5x)`
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--checkbox`: направление `row`
    - `--counter`: направление `column`, color `var(--ds-color-badge-text-color, #ffffff)`
    - `--icon-size`: направление `row`, align-items `center`
    - `--image-size`: направление `row`, align-items `center`
    - `--indicator`: ширина `var(--ds-size-6x)`, направление `row`
    - `--radio-button`: направление `row`
    - `--slide-toggle`: направление `row`, color `var(--ds-color-slide-toggle-text-color, #333333)`
    - `--text-default`: направление `row`, color `var(--ds-color-brand-neutral-super-dark, #333333)`
- Разметка:

```html
<div class="ds-element-select ds-element-select--checkbox">
  <span class="ds-element-select__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-element-select__image-size"></div>
  <span class="ds-element-select__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-element-select {
  display: flex;
  background: #ffffff;
  width: fit-content;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-select__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element-select__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-select__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-select__icon svg path {
  fill: currentColor;
}
.ds-element-select__image-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-size-circular);
}
.ds-element-select--image-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-select--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-select--text-default {
  flex-direction: row;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element-select--checkbox {
  flex-direction: row;
}
.ds-element-select--radio-button {
  flex-direction: row;
}
.ds-element-select--indicator {
  width: var(--ds-size-6x);
  flex-direction: row;
}
.ds-element-select--slide-toggle {
  flex-direction: row;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-element-select--counter {
  flex-direction: column;
  color: var(--ds-color-badge-text-color, #ffffff);
}
```
</details>

#### Element sidenav `[56598:2991]` — 2 вариантов
**Описание и рекомендации по применению:**
Слот элемента бокового меню — выбирает, что стоит в строке меню: кнопка свёртывания или аватар пользователя.  
Служебный компонент бокового меню, отдельно на экран не ставится.
- **Content** (VARIANT): Avatar, Collaps icon
- Размеры и параметры:
    - высота: `var(--ds-size-5x)` (фикс.)
    - ширина: `var(--ds-size-5x)` (фикс.)
    - скругление: `var(--ds-size-1x)`
- Модификаторы (что меняет каждый):
    - `--avatar`: направление `column`, align-items `center`, промежуток между элементами `var(--ds-size-2-5x)`, внутренние отступы `3px var(--ds-size-0-5x) 3px var(--ds-size-0-5x)`
    - `--collaps-icon`: направление `row`, фон `var(--ds-color-sidenav-element-collaps-icon-background, #36474e)`
- Разметка:

```html
<div class="ds-element-sidenav ds-element-sidenav--avatar">
  <span class="ds-element-sidenav__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-element-sidenav__keyboard-arrow-left"></div>
  <span class="ds-element-sidenav__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-element-sidenav {
  height: var(--ds-size-5x);
  width: var(--ds-size-5x);
  display: flex;
  border-radius: var(--ds-size-1x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-sidenav__label {
  font-size: var(--ds-font-caption-m-10-normal-medium-size);
  line-height: var(--ds-font-caption-m-10-normal-medium-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-medium-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-medium-weight);
  text-transform: capitalize;
  color: var(--ds-color-text-accent, #448aff);
  white-space: nowrap;
}
.ds-element-sidenav__icon {
  flex-shrink: 0;
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-sidenav__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-sidenav__icon svg path {
  fill: currentColor;
}
.ds-element-sidenav__keyboard-arrow-left {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-element-sidenav--collaps-icon {
  flex-direction: row;
  background: var(--ds-color-sidenav-element-collaps-icon-background, #36474e);
}
.ds-element-sidenav--avatar {
  flex-direction: column;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: 3px var(--ds-size-0-5x) 3px var(--ds-size-0-5x);
  color: var(--ds-color-text-accent, #448aff);
}
```
</details>

#### Element step `[55403:7248]` — 12 вариантов
**Описание и рекомендации по применению:**
Маркер шага степпера — иконка или счётчик (номер) на подложке.  
Часть степпера, отдельно не используется: вставляется в шаг (Step).  

Как выбрать вариант:  
Content=Icon size — маркер с иконкой, когда смысл шага понятен по иконке.  
Content=Counter — маркер с номером шага.  

Состояния: Default, Hover, Press, Selected (текущий шаг), Error (шаг заполнен неверно), Disable (шаг недоступен).  
Фронт: https://frontend-common.iiko.ru/components/stepper
- **Content** (VARIANT): Counter, Icon size
- **State** (VARIANT): Default, Disable, Error, Hover, Press, Selected
- Прочие свойства: Text#57060:7 (TEXT)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-6x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-2-5x)`
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--counter`: направление `column`, color `var(--ds-color-brand-neutral-super-dark, #333333)`, color `var(--ds-color-brand-neutral-neutral, #9e9e9e)`
    - `--disabled`: pointer-events `none`
    - `--icon-size`: направление `row`, align-items `center`
- Состояния: `:active` (нажатие), `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-element-step ds-element-step--counter">
  <span class="ds-element-step__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-element-step__icon-size"></div>
  <div class="ds-element-step__info"></div>
  <span class="ds-element-step__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-element-step {
  min-height: var(--ds-size-6x);
  width: fit-content;
  display: flex;
  background: #ffffff;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-step__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element-step__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-step__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-step__icon svg path {
  fill: currentColor;
}
.ds-element-step__icon-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
}
.ds-element-step__info {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-element-step--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-step--counter {
  flex-direction: column;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element-step--counter:hover {
  color: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-element-step--counter:active {
  color: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-element-step--counter:disabled {
  color: var(--ds-color-brand-neutral-neutral, #9e9e9e);
}
.ds-element-step--counter.ds-element-step--disabled {
  color: var(--ds-color-brand-neutral-neutral, #9e9e9e);
}
.ds-element-step--disabled {
  pointer-events: none;
}
```
</details>

#### Elementare cell `[60220:72578]` — 10 вариантов
**Описание и рекомендации по применению:**
Слот содержимого ячейки таблицы — вложенный служебный набор того, что можно поставить в ячейку.  
Используется внутри строки таблицы; на экран отдельно не выносится.  

Как выбрать вариант: по тому, что показывает ячейка.
- **Variant** (VARIANT): Button, Button icon, Checkbox, Chips, Icon group, Icon size, Input number, Slide toggle, Status, Text UI
- CSS не требуется: это **слот-контейнер** — пустая обёртка под вложенный компонент (иконку, ячейку). Оформление задаёт вложенный компонент, а размер — контент.

#### Elements `[58501:4220]` — 30 вариантов
**Описание и рекомендации по применению:**
Ячейка календаря — день, месяц или год в сетке выбора.  
Служебный компонент календаря: используется внутри Datepicker. Недоступные даты блокируйте, а не убирайте из сетки.  

Как выбрать вариант:  
Type=Cell — день; Month — месяц; Year — год.  
Variant=Default — обычная дата; Today — сегодня; Selected — выбранная; Range — внутри выбранного периода.  
Состояния: Default, Hover, Press, Disable.
- **Type** (VARIANT): Cell, Month, Year
- **Variant** (VARIANT): Default, Range, Selected, Today
- **State** (VARIANT): Default, Disable, Hover, Press
- Прочие свойства: Back right#58506:0 (BOOLEAN), Back left#58506:1 (BOOLEAN), Start range#58506:2 (BOOLEAN), End range#58506:3 (BOOLEAN), Date#58506:4 (TEXT), Show focus indicator#58506:5 (BOOLEAN), Year#58506:84 (TEXT), Month#58506:165 (TEXT)
- Размеры и параметры:
    - высота: `var(--ds-size-10x)` (фикс.)
    - ширина: `var(--ds-size-10x)` (фикс.)
    - скругление: `var(--ds-radius-circular, 9999px)`
- Модификаторы (что меняет каждый):
    - `--cell`: фон `var(--ds-color-brand-neutral-lighter, #e0e0e0)`, color `var(--ds-color-text-disable, #9e9e9e)`, направление `row`, align-items `center`
    - `--disabled`: pointer-events `none`
    - `--month`: ширина `fit-content`, направление `row`, промежуток между элементами `var(--ds-size-2x)`, внутренние отступы `var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x)`
    - `--year`: ширина `fit-content`, направление `column`, align-items `center`, color `var(--ds-color-text-inversive, #ffffff)`
- Состояния: `:active` (нажатие), `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-elements ds-elements--cell">
  <div class="ds-elements__date"></div>
  <span class="ds-elements__label">Текст</span>
  <div class="ds-elements__range-highlight-end"></div>
  <div class="ds-elements__range-highlight-middle"></div>
  <div class="ds-elements__range-highlight-start"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-elements {
  display: flex;
  height: var(--ds-size-10x);
  width: var(--ds-size-10x);
  border-radius: var(--ds-radius-circular, 9999px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-elements__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-elements__range-highlight-start {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements__range-highlight-end {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements__range-highlight-middle {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-10, #f5f9ff);
}
.ds-elements__date {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-primary, #333333);
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--cell.ds-elements--today:disabled {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--today.ds-elements--disabled {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--default.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--range:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--range.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--selected:active {
  background: var(--ds-color-button-accent-filled-press-background, #2651b5);
}
.ds-elements--cell.ds-elements--today:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--cell.ds-elements--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--cell.ds-elements--today:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--cell.ds-elements--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--cell.ds-elements--range {
  flex-direction: row;
  align-items: center;
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--cell.ds-elements--selected {
  flex-direction: column;
  align-items: center;
  color: var(--ds-color-text-inversive, #ffffff);
}
.ds-elements--year.ds-elements--selected {
  width: fit-content;
  flex-direction: column;
  align-items: center;
  color: var(--ds-color-text-inversive, #ffffff);
}
.ds-elements--cell.ds-elements--today {
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  border: 1px solid var(--ds-color-stroke-hover, #9e9e9e);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--cell.ds-elements--default {
  flex-direction: column;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-2-5x) var(--ds-size-2x) var(--ds-size-2-5x);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--year.ds-elements--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--default.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--today:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--today.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--year.ds-elements--today:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--year.ds-elements--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--year.ds-elements--today:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--year.ds-elements--default {
  width: fit-content;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--year.ds-elements--today {
  width: fit-content;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  border: 1px solid var(--ds-color-stroke-hover, #9e9e9e);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--month.ds-elements--default {
  width: fit-content;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--month.ds-elements--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--month.ds-elements--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--month.ds-elements--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--month.ds-elements--default.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--disabled {
  pointer-events: none;
}
```
</details>

#### Elements `[58982:9594]` — 8 вариантов
**Описание и рекомендации по применению:**
Значение времени в списке — час или минута, доступные для выбора.  
Служебный компонент выбора времени: используется внутри Timepicker. Недоступное время блокируйте, а не убирайте из списка.  

Как выбрать вариант:  
Variant=Default — обычное значение; Selected — выбранное.  
Состояния: Default, Hover, Press, Range (внутри выбранного интервала), Disable.
- **Variant** (VARIANT): Default, Selected
- **State** (VARIANT): Default, Disable, Hover, Press, Range
- Прочие свойства: Start range#58506:2 (BOOLEAN), End range#58506:3 (BOOLEAN), Time#58506:84 (TEXT)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-10x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
- Модификаторы (что меняет каждый):
    - `--default`: color `var(--ds-color-text-disable, #9e9e9e)`, направление `row`, промежуток между элементами `var(--ds-size-2-5x)`, внутренние отступы `var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x)`
    - `--disabled`: pointer-events `none`
    - `--selected`: направление `column`, color `var(--ds-color-text-inversive, #ffffff)`
- Состояния: `:active` (нажатие), `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-elements-2 ds-elements-2--default">
  <div class="ds-elements-2__date"></div>
  <span class="ds-elements-2__label">Текст</span>
  <div class="ds-elements-2__range-highlight-end"></div>
  <div class="ds-elements-2__range-highlight-start"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-elements-2 {
  min-height: var(--ds-size-10x);
  width: fit-content;
  display: flex;
  align-items: center;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-elements-2__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-inversive, #ffffff);
  white-space: nowrap;
}
.ds-elements-2__range-highlight-start {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements-2__range-highlight-end {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements-2__date {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-button-accent-filled-default-background, #448aff);
}
.ds-elements-2--selected {
  flex-direction: column;
  color: var(--ds-color-text-inversive, #ffffff);
}
.ds-elements-2--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements-2--default.ds-elements-2--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements-2--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements-2--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements-2--default {
  flex-direction: row;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements-2--disabled {
  pointer-events: none;
}
```
</details>

#### Expansion content `[61361:99603]` — 2 вариантов
**Описание и рекомендации по применению:**
Содержимое раскрывающейся панели — область под заголовком, куда складывается сам блок.  
Служебный компонент панели: используется внутри Expansion panel.  

Как выбрать вариант: с внутренними отступами или без них, когда отступы задаёт вложенный блок.
- **Padding off/on** (VARIANT): False, True
- Прочие свойства: Slot#61363:19 (SLOT)
- Размеры и параметры:
    - ширина: `597px` (фикс.)
    - внутренние отступы: `var(--ds-expansion-panel-content-pad-top, 16px) var(--ds-expansion-panel-content-pad-right, 16px) var(--ds-expansion-panel-content-pad-bottom, 16px) var(--ds-expansion-panel-content-pad-left, 16px)`
- Модификаторы (что меняет каждый):
    - `--false`: color `var(--ds-color-expansion-panel-content-text-color, #333333)`
    - `--true`: color `var(--ds-color-expansion-panel-content-text-color, #333333)`
- Разметка:

```html
<div class="ds-expansion-content ds-expansion-content--false">
  <span class="ds-expansion-content__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-expansion-content {
  width: 597px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--ds-expansion-panel-content-pad-top, 16px) var(--ds-expansion-panel-content-pad-right, 16px) var(--ds-expansion-panel-content-pad-bottom, 16px) var(--ds-expansion-panel-content-pad-left, 16px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-expansion-content__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
  white-space: nowrap;
}
.ds-expansion-content--true {
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
}
.ds-expansion-content--false {
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
}
```
</details>

#### Expansion group panel `[56155:1676]` — 2 вариантов
**Описание и рекомендации по применению:**
Группа раскрывающихся панелей — несколько панелей подряд с общими разделителями.  
Берите группу, когда блоков настроек несколько; открытым держите только нужный.  

Как выбрать вариант: группа свёрнута или раскрыта.
- **Type ?** (VARIANT): Collaps, Expand
- Прочие свойства: Slot#61364:25 (SLOT)
- Размеры и параметры:
    - ширина: `597px` (фикс.)
    - промежуток между элементами: `var(--ds-expansion-panel-collaps-gap-group, 8px)`
- Модификаторы (что меняет каждый):
    - `--collaps`: color `var(--ds-color-expansion-panel-collaps-text-color, #333333)`
    - `--expand`: color `var(--ds-color-expansion-panel-collaps-text-color, #333333)`
- Разметка:

```html
<div class="ds-expansion-group-panel ds-expansion-group-panel--collaps">
  <span class="ds-expansion-group-panel__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-expansion-group-panel {
  width: 597px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-expansion-panel-collaps-gap-group, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-expansion-group-panel__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-expansion-panel-collaps-text-color, #333333);
  white-space: nowrap;
}
.ds-expansion-group-panel--collaps {
  color: var(--ds-color-expansion-panel-collaps-text-color, #333333);
}
.ds-expansion-group-panel--expand {
  color: var(--ds-color-expansion-panel-collaps-text-color, #333333);
}
```
</details>

#### Expansion panel `[52937:1329]` — 12 вариантов
**Описание и рекомендации по применению:**
Раскрывающаяся панель — блок, который сворачивается до заголовка: группы настроек, детали документа, дополнительные параметры.  
Прячьте в неё второстепенное, обязательные поля держите открытыми. По умолчанию оставляйте свёрнутой, если содержимое нужно не всем.  

Как выбрать вариант:  
Variant=Default — обычная панель; Info — панель с пояснением.  
Collaps/Expand=On — раскрыта; Off — свёрнута.  
Состояния: Default, Hover, Press, Disable.
- **Variant** (VARIANT): Default, Info
- **Collaps/Expand** (VARIANT): Off, On
- **State** (VARIANT): Default, Disable, Hover, Press
- Прочие свойства: Element left#17172:1340 (BOOLEAN), Element right#17172:1349 (BOOLEAN), Icon text#58024:0 (BOOLEAN), Expansion panel_Content#58991:0 (SLOT), Expansion panel_Content2#58991:9 (SLOT), Expansion panel_Content3#58991:18 (SLOT), Expansion panel_Content4#58991:27 (SLOT)
- CSS: выверено вручную, см. `components/Expansion-Panel_DS/expansion.css` в разделе «Полные CSS-стили всех компонентов»

#### Expansion table panel `[56217:15104]` — 0 вариантов
_Описание компонента в Figma отсутствует._
- CSS не требуется: это **слот-контейнер** — пустая обёртка под вложенный компонент (иконку, ячейку). Оформление задаёт вложенный компонент, а размер — контент.

#### Form field cell `[60220:72732]` — 1 вариантов
**Описание и рекомендации по применению:**
Обёртка редактируемой ячейки таблицы — выравнивание и отступы поля внутри ячейки.  
Служебный компонент таблицы: используется внутри строки, отдельно на экран не ставится.
- **Variant** (VARIANT): Table content cell Chips input
- Размеры и параметры:
    - высота: минимум `var(--ds-size-10x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - фон: `#ffffff`
- Разметка:

```html
<div class="ds-form-field-cell">
  <div class="ds-form-field-cell__table-content"></div>
  <div class="ds-form-field-cell__table-content-chips-input"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-form-field-cell {
  min-height: var(--ds-size-10x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-form-field-cell__table-content-chips-input {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-form-field-cell__table-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
}
```
</details>

#### Hint container `[54593:479]` — 10 вариантов
**Описание и рекомендации по применению:**
Подсказка — короткое пояснение по элементу: назначение кнопки-иконки, правило заполнения поля, расшифровка статуса.  
Появляется по наведению и не должна содержать действий, без которых нельзя обойтись. Текст — одна-две строки.  

Как выбрать вариант:  
Size=Single — короткая подсказка одной строкой; Complex — с заголовком и несколькими строками.  
Orientation — сторона, с которой подсказка выходит к элементу: Up, Down, Right, Left; Default — без хвостика.
- **Size** (VARIANT): Complex, Single
- **Orientation** (VARIANT): Default, Down, Left, Right, Up
- Прочие свойства: Header#54713:4 (BOOLEAN), Content#54713:15 (BOOLEAN), Footer#54713:26 (BOOLEAN)
- Размеры и параметры:
    - ширина: `250px` (фикс.)
    - скругление: `var(--ds-hint-border-radius, 8px)`
    - тень: `var(--ds-shadow-shadows-08-dp-s)`
- Модификаторы (что меняет каждый):
    - `--default`: направление `column`, color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--down`: направление `column`, color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--left`: направление `row`, color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--right`: направление `row`, color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--up`: направление `column`, color `var(--ds-color-hint-header-text-color, #ffffff)`
- Разметка:

```html
<div class="ds-hint-container ds-hint-container--default">
  <span class="ds-hint-container__arrow"><!-- иконка: material-icons по имени --></span>
  <div class="ds-hint-container__content"></div>
  <div class="ds-hint-container__footer"></div>
  <div class="ds-hint-container__header"></div>
  <span class="ds-hint-container__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-hint-container__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-hint-container {
  width: 250px;
  display: flex;
  align-items: center;
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  border-radius: var(--ds-hint-border-radius, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-container__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-header-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-container__icon svg path {
  fill: currentColor;
}
.ds-hint-container__arrow {
  height: var(--ds-size-1x);
  display: flex;
  flex-direction: row;
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container__header {
  display: flex;
  flex-direction: row;
  gap: var(--ds-hint-header-gap, 8px);
  padding: var(--ds-hint-header-pad-top, 8px) var(--ds-hint-header-pad-right, 12px) var(--ds-hint-header-pad-bottom, 4px) var(--ds-hint-header-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-hint-content-gap, 8px);
  padding: var(--ds-hint-content-pad-top, 8px) var(--ds-hint-content-pad-right, 12px) var(--ds-hint-content-pad-bottom, 8px) var(--ds-hint-content-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container__footer {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-hint-footer-gap, 12px);
  padding: var(--ds-hint-footer-pad-top, 16px) var(--ds-hint-footer-pad-right, 12px) var(--ds-hint-footer-pad-bottom, 12px) var(--ds-hint-footer-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container--up {
  flex-direction: column;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--down {
  flex-direction: column;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--right {
  flex-direction: row;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--left {
  flex-direction: row;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--default {
  flex-direction: column;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
```
</details>

#### Hint content `[54713:3325]` — 2 вариантов
**Описание и рекомендации по применению:**
Содержимое подсказки — текст внутри подсказки: одна строка или несколько блоков.  
Служебный компонент подсказки, отдельно на экран не ставится.
- **Content** (VARIANT): Group content, Single content
- Прочие свойства: Element right#56260:9 (BOOLEAN), Element left#56260:12 (BOOLEAN)
- Размеры и параметры:
    - ширина: `250px` (фикс.)
    - внутренние отступы: `var(--ds-hint-content-pad-top, 8px) var(--ds-hint-content-pad-right, 12px) var(--ds-hint-content-pad-bottom, 8px) var(--ds-hint-content-pad-left, 12px)`
    - промежуток между элементами: `var(--ds-hint-content-gap, 8px)`
    - фон: `var(--ds-color-hint-background-color, #424242)`
- Модификаторы (что меняет каждый):
    - `--group-content`: color `var(--ds-color-hint-content-text-color, #ffffff)`
    - `--single-content`: align-items `center`, color `var(--ds-color-hint-content-text-color, #ffffff)`
- Разметка:

```html
<div class="ds-hint-content ds-hint-content--group-content">
  <div class="ds-hint-content__block"></div>
  <div class="ds-hint-content__clear"></div>
  <div class="ds-hint-content__close"></div>
  <span class="ds-hint-content__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-hint-content__icon-size"></div>
  <div class="ds-hint-content__info"></div>
  <span class="ds-hint-content__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-hint-content {
  width: 250px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-hint-content-gap, 8px);
  padding: var(--ds-hint-content-pad-top, 8px) var(--ds-hint-content-pad-right, 12px) var(--ds-hint-content-pad-bottom, 8px) var(--ds-hint-content-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-content__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-hint-content-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-content__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-content__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-content__icon svg path {
  fill: currentColor;
}
.ds-hint-content__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-content__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-content__block {
  display: flex;
  flex-direction: column;
  gap: var(--ds-hint-content-gap-content, 4px);
}
.ds-hint-content__clear {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-content__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-content--group-content {
  color: var(--ds-color-hint-content-text-color, #ffffff);
}
.ds-hint-content--single-content {
  align-items: center;
  color: var(--ds-color-hint-content-text-color, #ffffff);
}
```
</details>

#### Hint footer `[54600:517]` — 1 вариантов
**Описание и рекомендации по применению:**
Подвал подсказки — ссылка или кнопка под текстом подсказки («Подробнее»).  
Добавляйте только когда есть куда вести; основное действие в подсказку не выносите.
- **Content** (VARIANT): Default
- Прочие свойства: Step text#54600:1 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `56px`, растёт по контенту
    - ширина: `250px` (фикс.)
    - внутренние отступы: `var(--ds-hint-footer-pad-top, 16px) var(--ds-hint-footer-pad-right, 12px) var(--ds-hint-footer-pad-bottom, 12px) var(--ds-hint-footer-pad-left, 12px)`
    - промежуток между элементами: `var(--ds-hint-footer-gap, 12px)`
    - фон: `var(--ds-color-hint-background-color, #424242)`
- Модификаторы (что меняет каждый):
    - `--default`: color `var(--ds-color-hint-footer-text-color, #ffffff)`
- Разметка:

```html
<div class="ds-hint-footer ds-hint-footer--default">
  <div class="ds-hint-footer__button-group"></div>
  <span class="ds-hint-footer__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-hint-footer__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-hint-footer {
  min-height: 56px;
  width: 250px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-hint-footer-gap, 12px);
  padding: var(--ds-hint-footer-pad-top, 16px) var(--ds-hint-footer-pad-right, 12px) var(--ds-hint-footer-pad-bottom, 12px) var(--ds-hint-footer-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-footer__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-button-accent-filled-default-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-footer__icon {
  flex-shrink: 0;
  width: var(--ds-size-7x);
  height: var(--ds-size-7x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-footer__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-footer__icon svg path {
  fill: currentColor;
}
.ds-hint-footer__цвет-и-палитра {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-hint-footer-text-color, #ffffff);
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-footer-text-color, #ffffff);
}
.ds-hint-footer__button-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
}
.ds-hint-footer--default {
  color: var(--ds-color-hint-footer-text-color, #ffffff);
}
```
</details>

#### Hint header `[54594:2219]` — 5 вариантов
**Описание и рекомендации по применению:**
Заголовок подсказки — тема пояснения и его окраска по смыслу.  
Цвет выбирайте по характеру сообщения, а не для украшения.  

Как выбрать вариант: обычное пояснение, акцентное, второстепенное, предупреждение или ошибка.
- **Style** (VARIANT): Error, Neutral, Primary, Secondary, Warning
- Прочие свойства: Element left#54594:55 (BOOLEAN), Element right#54594:56 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-8x)`, растёт по контенту
    - ширина: `250px` (фикс.)
    - внутренние отступы: `var(--ds-hint-header-pad-top, 8px) var(--ds-hint-header-pad-right, 12px) var(--ds-hint-header-pad-bottom, 4px) var(--ds-hint-header-pad-left, 12px)`
    - промежуток между элементами: `var(--ds-hint-header-gap, 8px)`
    - фон: `var(--ds-color-hint-background-color, #424242)`
- Модификаторы (что меняет каждый):
    - `--error`: color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--neutral`: color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--primary`: color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--secondary`: color `var(--ds-color-hint-header-text-color, #ffffff)`
    - `--warning`: color `var(--ds-color-hint-header-text-color, #ffffff)`
- Разметка:

```html
<div class="ds-hint-header ds-hint-header--error">
  <div class="ds-hint-header__clear"></div>
  <div class="ds-hint-header__close"></div>
  <span class="ds-hint-header__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-hint-header__icon-size"></div>
  <div class="ds-hint-header__info"></div>
  <span class="ds-hint-header__label">Текст</span>
  <span class="ds-hint-header__title">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-hint-header {
  min-height: var(--ds-size-8x);
  width: 250px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-hint-header-gap, 8px);
  padding: var(--ds-hint-header-pad-top, 8px) var(--ds-hint-header-pad-right, 12px) var(--ds-hint-header-pad-bottom, 4px) var(--ds-hint-header-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-header__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-header-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-header__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-header__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-header__icon svg path {
  fill: currentColor;
}
.ds-hint-header__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-header__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-header__title {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-hint-header-text-color, #ffffff);
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header__clear {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-header__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-header--neutral {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--primary {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--secondary {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--warning {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--error {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
```
</details>

#### Icon group `[53467:1060]` — 2 вариантов
**Описание и рекомендации по применению:**
Группа иконок — две и более иконки рядом с единым зазором: индикаторы в строке таблицы, набор статусных иконок в карточке.  
Зазор берите из варианта, вручную не раздвигайте.  

Как выбрать вариант: по нужному зазору между иконками — плотный или разряженный.
- **Size gap** (VARIANT): 2x, 4x
- Прочие свойства: Slot#60190:14 (SLOT)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-5x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-icon-size-gap-group-2x, 8px)`
- Модификаторы (что меняет каждый):
    - `--4x`: промежуток между элементами `var(--ds-icon-size-gap-group-4x, 16px)`
- Разметка:

```html
<div class="ds-icon-group ds-icon-group--4x">
  <span class="ds-icon-group__icon"><!-- иконка: material-icons по имени --></span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-icon-group {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-icon-size-gap-group-2x, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-icon-group__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-icon-group__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-icon-group__icon svg path {
  fill: currentColor;
}
.ds-icon-group--4x {
  gap: var(--ds-icon-size-gap-group-4x, 16px);
}
```
</details>

#### Icon size `[52927:6286]` — 12 вариантов
**Описание и рекомендации по применению:**
Контейнер иконки или картинки — задаёт единый размер и выравнивание всего, что вставляется как иконка: в кнопки, поля, пункты списков, ячейки таблиц.  
Вставляйте иконку внутрь этого контейнера, а не напрямую — иначе иконки в одном ряду разъезжаются по высоте.  

Как выбрать вариант:  
Content=Icon — векторная иконка; Content=Img — картинка или аватар.  
Size — под размер родителя: мелкие в строках таблиц и подписях, средние в кнопках и полях, крупные в пустых состояниях и плитках.
- **Size** (VARIANT): 16, 20, 24, 32, 36, 40
- **Content** (VARIANT): Icon, Img
- Прочие свойства: State#54063:8 (BOOLEAN), Instance#60108:34 (INSTANCE_SWAP)
- CSS не требуется: это **слот-контейнер** — пустая обёртка под вложенный компонент (иконку, ячейку). Оформление задаёт вложенный компонент, а размер — контент.

#### Input `[52670:7573]` — 29 вариантов
**Описание и рекомендации по применению:**
Поле ввода — для однострочного текста: название, сумма, телефон, адрес.  
Свойства включаются внутри компонента: Label, Element left (иконка слева), Element right (иконка/кнопка справа),  
Support text (подсказка) и Hint text. Есть режимы с лимитом символов и счётчиком (например, 10/256),  
с префиксами (телефон, e-mail) и с сообщением об ошибке.  

Как выбрать вариант:  
Variant=Empty — поле без значения, плейсхолдер или Label внутри.  
Variant=Populated — поле со значением, Label над полем.  
Variant=No label up — компактные вытянутые поля (S / XS), без Label сверху.  
Size: M (основной), S (компактный), XS (минимальный — для строк таблиц и ячеек).  

State: Default, Hover, Focus, Focus+Placeholder, Focus+Value, Error, Error+Hover, Disable.  
Фронт: https://frontend-common.iiko.ru/components/input
- **Size** (VARIANT): M, S, XS
- **Variant** (VARIANT): Empty, No label up, Populated
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Focus+Value, Hover
- Прочие свойства: Input text#52678:0 (TEXT), Label text#52678:3 (TEXT), Support text#52678:6 (TEXT), Label#56934:32 (BOOLEAN), Element left#56934:282 (BOOLEAN), Element right#56934:407 (BOOLEAN), Support text#56934:532 (BOOLEAN), Input text#56968:66 (BOOLEAN), Hint text#57893:0 (BOOLEAN), Support#57893:30 (BOOLEAN), Hint text#57893:60 (TEXT)
- CSS: выверено вручную, см. `components/Form-Field-Input_DS/input.css` в разделе «Полные CSS-стили всех компонентов»

#### Input cell `[60229:74436]` — 8 вариантов
**Описание и рекомендации по применению:**
Поле ввода внутри ячейки таблицы — правка значения прямо в строке, без отдельной формы.  
Используйте в редактируемых таблицах: количество, цена, комментарий в накладной. Вне таблицы берите обычное поле Input.  

Состояния: Default, Hover, Focus, Focus+Placeholder, Focus+Value, Error, Error+Hover, Disable.
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Hover, Vocus+Value
- Размеры и параметры:
    - высота: минимум `var(--ds-size-9x)`, растёт по контенту
    - ширина: `200px` (фикс.)
    - внутренние отступы: `var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px)`
    - промежуток между элементами: `var(--ds-size-2x)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-input-cell ds-input-cell--disabled">
  <div class="ds-input-cell__frame"></div>
  <span class="ds-input-cell__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-input-cell__label">Текст</span>
  <span class="ds-input-cell__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-input-cell {
  min-height: var(--ds-size-9x);
  width: 200px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-input-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-cell__icon svg path {
  fill: currentColor;
}
.ds-input-cell__frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-cell__support {
  display: flex;
  flex-direction: row;
}
.ds-input-cell:hover {
  background: var(--ds-palette-neutral-50, #f5f5f5);
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-input-cell:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-input-cell:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-cell.ds-input-cell--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-cell--disabled {
  pointer-events: none;
}
```
</details>

#### Input Datepicker `[58548:4764]` — 2 вариантов
**Описание и рекомендации по применению:**
Поле даты — ввод и выбор даты: дата поставки, период отчёта, срок годности.  
Дату можно ввести с клавиатуры или выбрать в календаре по иконке справа. Для времени берите Input Timepicker.  

Как выбрать вариант: Empty — дата не выбрана, Populated — дата выбрана.
- **Type** (VARIANT): Empty, Populated
- Размеры и параметры:
    - высота: минимум `48px`, растёт по контенту
    - ширина: `250px` (фикс.)
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--empty`: color `var(--ds-color-form-field-input-label-text-color, #616161)`
    - `--populated`: color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`
- Разметка:

```html
<div class="ds-input-datepicker ds-input-datepicker--empty">
  <div class="ds-input-datepicker__frame"></div>
  <span class="ds-input-datepicker__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-input-datepicker__label">Текст</span>
  <span class="ds-input-datepicker__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-input-datepicker {
  min-height: 48px;
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-datepicker__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-input-datepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-datepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-datepicker__icon svg path {
  fill: currentColor;
}
.ds-input-datepicker__frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-datepicker__support {
  display: flex;
  flex-direction: row;
}
.ds-input-datepicker--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-input-datepicker--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
```
</details>

#### Input number `[17193:84750]` — 29 вариантов
**Описание и рекомендации по применению:**
Поле числа — количество и числовые значения: количество товара, цена, процент, число дней.  
Рядом стоят кнопки шага «минус» и «плюс»; вводить можно и с клавиатуры.  
Не используйте его для текста и для дат — для дат берите Input Datepicker.  

Как выбрать вариант:  
Variant=Empty — без значения; Populated — со значением; No label up — без Label сверху (для таблиц и плотных форм).  
Size=M — основной; S и XS — плотные формы, панели, строки таблиц.  
Состояния: Default, Hover, Focus, Focus+Placeholder, Focus+Value, Error, Error+Hover, Disable.
- **Size** (VARIANT): M, S, XS
- **Variant** (VARIANT): Empty, No label up, Populated
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Focus+Value, Hover
- Прочие свойства: Close icon#57962:0 (BOOLEAN)
- Размеры и параметры:
    - ширина: `138px` (фикс.)
    - промежуток между элементами: `18px`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--empty`: align-items `center`, color `var(--ds-color-form-field-input-label-text-color, #616161)`, color `var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e)`
    - `--populated`: align-items `center`, color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`, color `var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e)`
    - `--s`: ширина `fit-content`
    - `--xs`: ширина `fit-content`, ширина `var(--ds-size-6x)`, высота `var(--ds-size-6x)`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-input-number ds-input-number--disabled">
  <div class="ds-input-number__frame"></div>
  <span class="ds-input-number__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-input-number__label">Текст</span>
  <span class="ds-input-number__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-input-number {
  display: flex;
  flex-direction: row;
  width: 138px;
  gap: 18px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-number__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-input-number__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-number__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-number__icon svg path {
  fill: currentColor;
}
.ds-input-number__frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-number__support {
  display: flex;
  flex-direction: row;
}
.ds-input-number--s {
  width: fit-content;
}
.ds-input-number--xs {
  width: fit-content;
}
.ds-input-number--xs .ds-input-number__icon {
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
}
.ds-input-number--populated {
  align-items: center;
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-input-number--empty {
  align-items: center;
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-input-number--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-input-number--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-input-number--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-input-number--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-number--populated.ds-input-number--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-number--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-input-number--empty.ds-input-number--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-input-number--disabled {
  pointer-events: none;
}
```
</details>

#### Input number_but icon `[56967:10506]` — 1 вариантов
_Описание компонента в Figma отсутствует._
- Прочие свойства: Support#57977:0 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `56px`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-1x)`
- Разметка:

```html
<div class="ds-input-number-but-icon">
  <div class="ds-input-number-but-icon__button"></div>
  <div class="ds-input-number-but-icon__container"></div>
  <span class="ds-input-number-but-icon__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-input-number-but-icon__label">Текст</span>
  <div class="ds-input-number-but-icon__support-text"></div>
  <span class="ds-input-number-but-icon__text">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-input-number-but-icon {
  min-height: 56px;
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-1x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-number-but-icon__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-input-number-but-icon__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-number-but-icon__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-number-but-icon__icon svg path {
  fill: currentColor;
}
.ds-input-number-but-icon__container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-1x);
}
.ds-input-number-but-icon__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-icon-gap, 8px);
  padding: var(--ds-button-icon-m-size-pad-top, 8px) var(--ds-button-icon-m-size-pad-right, 8px) var(--ds-button-icon-m-size-pad-bottom, 8px) var(--ds-button-icon-m-size-pad-left, 8px);
  border-radius: var(--ds-button-icon-border-radius, 8px);
  background: var(--ds-color-button-icon-neutral-filled-default-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
}
.ds-input-number-but-icon__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-input-number-but-icon__support-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-form-field-filled-default-support-text-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-support-text-color, #616161);
}
```
</details>

#### Input Timepicker `[58982:9561]` — 2 вариантов
**Описание и рекомендации по применению:**
Поле времени — ввод и выбор времени: время доставки, начало смены, время закрытия.  
Время можно ввести с клавиатуры или выбрать в списке по иконке справа. Для даты берите Input Datepicker.  

Как выбрать вариант: Empty — время не выбрано, Populated — время выбрано.
- **Type** (VARIANT): Empty, Populated
- Размеры и параметры:
    - высота: минимум `48px`, растёт по контенту
    - ширина: `250px` (фикс.)
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--empty`: color `var(--ds-color-form-field-input-label-text-color, #616161)`
    - `--populated`: color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`
- Разметка:

```html
<div class="ds-input-timepicker ds-input-timepicker--empty">
  <div class="ds-input-timepicker__frame"></div>
  <span class="ds-input-timepicker__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-input-timepicker__label">Текст</span>
  <span class="ds-input-timepicker__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-input-timepicker {
  min-height: 48px;
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-timepicker__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-input-timepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-timepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-timepicker__icon svg path {
  fill: currentColor;
}
.ds-input-timepicker__frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-timepicker__support {
  display: flex;
  flex-direction: row;
}
.ds-input-timepicker--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-input-timepicker--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
```
</details>

#### List (Сontainer) `[57604:4762]` — 1 вариантов
**Описание и рекомендации по применению:**
Контейнер списка — подложка с отступами, в которую складываются пункты List item.  
Берите его вместо своей подложки: отступы, разделители и прокрутка уже заданы.
- **Type** (VARIANT): Сontainer
- Прочие свойства: List container#57620:0 (SLOT), Scroll#57620:2 (BOOLEAN), Title#57623:6 (BOOLEAN), Divider header#57862:0 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `257px`, растёт по контенту
    - ширина: `258px` (фикс.)
    - внутренние отступы: `var(--ds-list-pad-top, 8px) 0 var(--ds-list-pad-bottom, 8px) 0`
    - скругление: `var(--ds-list-border-radius)`
    - фон: `var(--ds-color-list-background, #ffffff)`
- Модификаторы (что меняет каждый):
    - `--container`: color `var(--ds-color-list-item-text-label-color, #616161)`
- Разметка:

```html
<div class="ds-list-container ds-list-container--container">
  <div class="ds-list-container__content"></div>
  <div class="ds-list-container__divider"></div>
  <span class="ds-list-container__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-list-container__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-list-container__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-list-container__item"></div>
  <span class="ds-list-container__label">Текст</span>
  <div class="ds-list-container__scroll"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-list-container {
  min-height: 257px;
  width: 258px;
  display: flex;
  flex-direction: column;
  padding: var(--ds-list-pad-top, 8px) 0 var(--ds-list-pad-bottom, 8px) 0;
  border-radius: var(--ds-list-border-radius);
  background: var(--ds-color-list-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-list-container__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-list-item-text-color, #333333);
  white-space: nowrap;
}
.ds-list-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-list-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-list-container__icon svg path {
  fill: currentColor;
}
.ds-list-container__item {
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
  padding: var(--ds-list-item-pad-top, 8px) var(--ds-list-item-pad-right, 16px) var(--ds-list-item-pad-bottom, 8px) var(--ds-list-item-pad-left, 16px);
  background: var(--ds-color-list-item-default-background, #ffffff);
}
.ds-list-container__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-list-container__content {
  display: flex;
  flex-direction: column;
}
.ds-list-container__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-list-container__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-list-container__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-list-container--container {
  color: var(--ds-color-list-item-text-label-color, #616161);
}
```
</details>

#### List item `[54101:7922]` — 8 вариантов
**Описание и рекомендации по применению:**
Пункт списка — одна строка перечня: товар, документ, сотрудник, пункт меню действий.  
Вся строка кликабельна; действия над пунктом ставьте справа.  

Состояния: Default, Hover, Press, Selected, Back selected, Link, Negative (удаление), Disable.
- **State** (VARIANT): Back selected, Default, Disable, Hover, Link, Negative, Press, Selected
- Прочие свойства: Element left#54167:1 (BOOLEAN), Element right#54167:6 (BOOLEAN), Label up#54741:15 (BOOLEAN), Label down#54741:30 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `68px`, растёт по контенту
    - ширина: `258px` (фикс.)
    - внутренние отступы: `var(--ds-list-item-pad-top, 8px) var(--ds-list-item-pad-right, 16px) var(--ds-list-item-pad-bottom, 8px) var(--ds-list-item-pad-left, 16px)`
    - промежуток между элементами: `var(--ds-list-item-gap, 8px)`
    - фон: `var(--ds-color-list-item-default-background, #ffffff)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:active` (нажатие), `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-list-item ds-list-item--disabled">
  <div class="ds-list-item__checkbox"></div>
  <div class="ds-list-item__content"></div>
  <span class="ds-list-item__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-list-item__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-list-item__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-list-item__icon-size"></div>
  <span class="ds-list-item__label">Текст</span>
  <div class="ds-list-item__label-down"></div>
  <div class="ds-list-item__label-up"></div>
  <span class="ds-list-item__text">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-list-item {
  min-height: 68px;
  width: 258px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
  padding: var(--ds-list-item-pad-top, 8px) var(--ds-list-item-pad-right, 16px) var(--ds-list-item-pad-bottom, 8px) var(--ds-list-item-pad-left, 16px);
  background: var(--ds-color-list-item-default-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-list-item__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-list-item-text-color, #333333);
  white-space: nowrap;
}
.ds-list-item__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-list-item__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-list-item__icon svg path {
  fill: currentColor;
}
.ds-list-item__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-list-item__checkbox {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-list-item__content {
  display: flex;
  flex-direction: column;
}
.ds-list-item__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-list-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-list-item-text-label-color, #616161);
}
.ds-list-item__text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-list-item-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-list-item-text-color, #333333);
}
.ds-list-item__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-list-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-list-item-text-label-color, #616161);
}
.ds-list-item__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-list-item__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-list-item:hover {
  background: var(--ds-color-list-item-hover-background, #f5f5f5);
}
.ds-list-item:active {
  background: var(--ds-color-list-item-press-background, #e0e0e0);
}
.ds-list-item:disabled {
  background: var(--ds-color-list-item-disable-background, #ffffff);
  color: var(--ds-color-list-item-disable-label-text-color, #9e9e9e);
}
.ds-list-item.ds-list-item--disabled {
  background: var(--ds-color-list-item-disable-background, #ffffff);
  color: var(--ds-color-list-item-disable-label-text-color, #9e9e9e);
}
.ds-list-item--disabled {
  pointer-events: none;
}
```
</details>

#### Logo iiko `[55332:19892]` — 4 вариантов
**Описание и рекомендации по применению:**
Логотип iiko — знак продукта в шапке приложения, боковом меню и на экранах входа.  
Пропорции и цвета не меняйте, поверх пёстрых фонов используйте инверсный вариант.  

Как выбрать вариант:  
Size=Full — знак с названием; Small — только знак (для свёрнутого меню).  
Style=Main — основной; Inverse — инверсный для тёмного фона.
- **Size** (VARIANT): Full, Small
- **Style** (VARIANT): Inverse, Main
- Размеры и параметры:
    - высота: `72px` (фикс.)
    - ширина: по контенту (hug)
    - фон: `#ffffff`
- Разметка:

```html
<div class="ds-logo-iiko">
  <div class="ds-logo-iiko__vector"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-logo-iiko {
  height: 72px;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-logo-iiko__vector {
  height: 72px;
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-neutral-0, #ffffff);
}
```
</details>

#### Logo Syrve `[56079:771]` — 4 вариантов
**Описание и рекомендации по применению:**
Логотип Syrve — знак продукта для международной версии: шапка приложения, боковое меню, экран входа.  
Пропорции и цвета не меняйте; в макетах Syrve не смешивайте с логотипом iiko.  

Как выбрать вариант:  
Size=Full — знак с названием; Small — только знак (для свёрнутого меню).  
Style=Main — основной; Inverse — инверсный для тёмного фона.
- **Size** (VARIANT): Full, Small
- **Style** (VARIANT): Inverse, Main
- Размеры и параметры:
    - высота: `72px` (фикс.)
    - ширина: по контенту (hug)
    - фон: `#ffffff`
- Разметка:

```html
<div class="ds-logo-syrve">
  <div class="ds-logo-syrve__vector"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-logo-syrve {
  height: 72px;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-logo-syrve__vector {
  height: 70.9px;
  display: flex;
  flex-direction: row;
  background: #00062b;
}
```
</details>

#### Menu (Container) `[54163:6705]` — 1 вариантов
**Описание и рекомендации по применению:**
Контейнер меню — подложка с тенью, в которую складываются пункты Menu item.  
Берите его вместо своей подложки: отступы, тень и разделители уже заданы.
- **Type** (VARIANT): Container
- Прочие свойства: Scroll#55632:0 (BOOLEAN), Menu container#56968:88 (SLOT), Title#57636:8 (BOOLEAN), Search#57750:7 (BOOLEAN), Button#57848:0 (BOOLEAN), Divider header#57848:2 (BOOLEAN), Divider footer#57848:4 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `418px`, растёт по контенту
    - ширина: `240px` (фикс.)
    - внутренние отступы: `var(--ds-menu-pad-top, 8px) 0 var(--ds-menu-pad-bottom, 8px) 0`
    - промежуток между элементами: `var(--ds-menu-gap)`
    - скругление: `var(--ds-menu-border-radius, 8px)`
    - фон: `var(--ds-color-menu-background, #ffffff)`
    - тень: `var(--ds-shadow-shadows-08-dp-s)`
- Модификаторы (что меняет каждый):
    - `--container`: color `var(--ds-color-search-default-text-color, #d6d6d6)`
- Разметка:

```html
<div class="ds-menu-container ds-menu-container--container">
  <div class="ds-menu-container__button-group"></div>
  <div class="ds-menu-container__content"></div>
  <div class="ds-menu-container__divider"></div>
  <span class="ds-menu-container__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-menu-container__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-menu-container__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-menu-container__label">Текст</span>
  <div class="ds-menu-container__scroll"></div>
  <div class="ds-menu-container__search"></div>
  <span class="ds-menu-container__title">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-menu-container {
  min-height: 418px;
  width: 240px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-menu-gap);
  padding: var(--ds-menu-pad-top, 8px) 0 var(--ds-menu-pad-bottom, 8px) 0;
  border-radius: var(--ds-menu-border-radius, 8px);
  background: var(--ds-color-menu-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-menu-container__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
  white-space: nowrap;
}
.ds-menu-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-menu-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-menu-container__icon svg path {
  fill: currentColor;
}
.ds-menu-container__search {
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  padding: 0 var(--ds-size-4x) var(--ds-size-1x) var(--ds-size-4x);
}
.ds-menu-container__title {
  display: flex;
  flex-direction: row;
  gap: var(--ds-menu-item-gap, 8px);
  padding: var(--ds-menu-item-pad-top, 8px) var(--ds-menu-item-pad-right, 16px) var(--ds-menu-item-pad-bottom, 8px) var(--ds-menu-item-pad-left, 16px);
  background: var(--ds-color-menu-item-default-background, #ffffff);
}
.ds-menu-container__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-menu-container__content {
  display: flex;
  flex-direction: column;
}
.ds-menu-container__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-menu-container__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-menu-container__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-menu-container__button-group {
  height: 52px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
  padding: var(--ds-button-group-margins-pad-top, 8px) var(--ds-button-group-margins-pad-right, 16px) var(--ds-button-group-margins-pad-bottom, 8px) var(--ds-button-group-margins-pad-left, 16px);
}
.ds-menu-container--container {
  color: var(--ds-color-search-default-text-color, #d6d6d6);
}
```
</details>

#### Menu item `[56090:1476]` — 7 вариантов
**Описание и рекомендации по применению:**
Пункт меню — одно действие или переход в выпадающем меню: «Изменить», «Дублировать», «Удалить».  
Опасные действия ставьте последними и оформляйте вариантом Negative; недоступные — блокируйте, а не убирайте.  

Состояния: Default, Hover, Press, Selected, Back selected, Negative, Disable.
- **State** (VARIANT): Back selected, Default, Disable, Hover, Negative, Press, Selected
- Прочие свойства: Element left#54167:1 (BOOLEAN), Element right#54167:6 (BOOLEAN), Label up#54741:15 (BOOLEAN), Label down#54741:30 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `68px`, растёт по контенту
    - ширина: `258px` (фикс.)
    - внутренние отступы: `var(--ds-menu-item-pad-top, 8px) var(--ds-menu-item-pad-right, 16px) var(--ds-menu-item-pad-bottom, 8px) var(--ds-menu-item-pad-left, 16px)`
    - промежуток между элементами: `var(--ds-menu-item-gap, 8px)`
    - фон: `var(--ds-color-menu-item-default-background, #ffffff)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:active` (нажатие), `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-menu-item ds-menu-item--disabled">
  <div class="ds-menu-item__checkbox"></div>
  <div class="ds-menu-item__content"></div>
  <span class="ds-menu-item__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-menu-item__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-menu-item__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-menu-item__icon-size"></div>
  <span class="ds-menu-item__label">Текст</span>
  <div class="ds-menu-item__label-down"></div>
  <div class="ds-menu-item__label-up"></div>
  <span class="ds-menu-item__text">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-menu-item {
  min-height: 68px;
  width: 258px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-menu-item-gap, 8px);
  padding: var(--ds-menu-item-pad-top, 8px) var(--ds-menu-item-pad-right, 16px) var(--ds-menu-item-pad-bottom, 8px) var(--ds-menu-item-pad-left, 16px);
  background: var(--ds-color-menu-item-default-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-menu-item__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-menu-item-text-color, #333333);
  white-space: nowrap;
}
.ds-menu-item__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-menu-item__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-menu-item__icon svg path {
  fill: currentColor;
}
.ds-menu-item__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-menu-item__checkbox {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-menu-item__content {
  display: flex;
  flex-direction: column;
}
.ds-menu-item__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-menu-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-menu-item-text-label-color, #616161);
}
.ds-menu-item__text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-menu-item-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-menu-item-text-color, #333333);
}
.ds-menu-item__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-menu-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-menu-item-text-label-color, #616161);
}
.ds-menu-item__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-menu-item__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-menu-item:hover {
  background: var(--ds-color-menu-item-hover-background, #f5f5f5);
}
.ds-menu-item:active {
  background: var(--ds-color-menu-item-press-background, #e0e0e0);
}
.ds-menu-item:disabled {
  background: var(--ds-color-menu-item-disable-background, #ffffff);
  color: var(--ds-color-menu-item-disable-label-text-color, #9e9e9e);
}
.ds-menu-item.ds-menu-item--disabled {
  background: var(--ds-color-menu-item-disable-background, #ffffff);
  color: var(--ds-color-menu-item-disable-label-text-color, #9e9e9e);
}
.ds-menu-item--disabled {
  pointer-events: none;
}
```
</details>

#### Picture `[58937:3985]` — 1 вариантов
_Описание компонента в Figma отсутствует._
- Прочие свойства: Crop#58947:6 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `189px`, растёт по контенту
    - ширина: `446px` (фикс.)
    - внутренние отступы: `var(--ds-size-2x) var(--ds-size-2x) var(--ds-size-2x) var(--ds-size-2x)`
    - промежуток между элементами: `var(--ds-size-2-5x)`
    - скругление: `var(--ds-size-2x)`
    - фон: `var(--ds-color-brand-accent-super-lightest, #f8f9fc)`
- Разметка:

```html
<div class="ds-picture">
  <div class="ds-picture__crop"></div>
  <div class="ds-picture__frame-1000001806"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-picture {
  min-height: 189px;
  width: 446px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-2x) var(--ds-size-2x) var(--ds-size-2x);
  border-radius: var(--ds-size-2x);
  background: var(--ds-color-brand-accent-super-lightest, #f8f9fc);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-picture__crop {
  height: 173px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  border: 1px dashed var(--ds-color-stroke-hover, #9e9e9e);
}
.ds-picture__frame-1000001806 {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 440px;
}
```
</details>

#### Radio button `[54095:4263]` — 14 вариантов
**Описание и рекомендации по применению:**
Радиокнопка — выбор строго одного варианта из нескольких.  
Используйте, когда варианты взаимоисключающие: «Склад поставки». Если можно выбрать несколько — Checkbox.  

Состав: круглый индикатор без подписи. С подписью — Radio button label; набор вариантов с заголовком — Radio button group.  
Вариант по умолчанию должен быть выбран заранее — не оставляйте группу пустой.  

Как выбрать вариант:  
Type=Deselected / Selected — вариант не выбран / выбран.  
Variant=Normal / Error / Disable — обычный, с ошибкой (в группе не выбран обязательный вариант), недоступный.  

Состояния: Default, Hover, Press.
- **Variant** (VARIANT): Disable, Error, Normal
- **Type** (VARIANT): Deselected, Selected
- **State** (VARIANT): Default, Hover, Press
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Radio button group `[54095:4392]` — 2 вариантов
**Описание и рекомендации по применению:**
Группа радиокнопок — набор взаимоисключающих вариантов с общим заголовком и общим support-текстом или текстом ошибки.  
Используйте, когда варианты относятся к одному вопросу и выбрать нужно один.  

Состав: заголовок группы (Support up), варианты Radio button label, общий текст под группой (Support down) — в ошибке он становится текстом ошибки для всей группы.  

Как выбрать вариант:  
Orientation=Vertical — варианты в столбец, основной случай.  
Orientation=Horizontal — в строку, когда вариантов мало и они короткие.
- **Orientation** (VARIANT): Horizontal, Vertical
- Прочие свойства: Slot vertical#57257:12 (SLOT), Slot horizontal#57257:15 (SLOT), Support up#58199:15 (BOOLEAN), Support down#58199:18 (BOOLEAN)
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Radio button label `[54095:4306]` — 6 вариантов
**Описание и рекомендации по применению:**
Радиокнопка с подписью — основной способ показать вариант выбора: индикатор + текст, при необходимости support-текст.  
Используйте в формах и настройках, где нужен один вариант из списка.  

Состав: радиокнопка слева или справа от подписи (Icon left / Icon right), Label, Support.  
Кликабельна вся строка вместе с подписью.  

Как выбрать вариант:  
Type=Deselected / Selected — не выбран / выбран.  
Variant=Normal / Error / Disable — обычный, с ошибкой, недоступный.
- **Variant** (VARIANT): Disable, Error, Normal
- **Type** (VARIANT): Deselected, Selected
- Прочие свойства: Icon left#17172:1340 (BOOLEAN), Icon right#17172:1349 (BOOLEAN), Label#54065:0 (BOOLEAN), Support#58197:0 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-5x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-radio-button-label-gap-support, 4px)`
- Модификаторы (что меняет каждый):
    - `--disable`: color `var(--ds-color-radio-button-label-text-disable-color, #9e9e9e)`
    - `--error`: color `var(--ds-color-radio-button-label-text-color, #333333)`
    - `--normal`: color `var(--ds-color-radio-button-label-text-color, #333333)`
- Разметка:

```html
<div class="ds-radio-button-label ds-radio-button-label--disable">
  <div class="ds-radio-button-label__form"></div>
  <span class="ds-radio-button-label__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-radio-button-label__label">Текст</span>
  <div class="ds-radio-button-label__left"></div>
  <div class="ds-radio-button-label__right"></div>
  <span class="ds-radio-button-label__support">Текст</span>
  <div class="ds-radio-button-label__support-text"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-radio-button-label {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-radio-button-label-gap-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-radio-button-label__label {
  font-size: var(--ds-typography-font-size-3-5x);
  font-weight: var(--ds-typography-font-weight-regular);
  line-height: var(--ds-typography-line-height-5x);
  letter-spacing: 0.25px;
  color: var(--ds-color-radio-button-label-text-color, #333333);
  white-space: nowrap;
}
.ds-radio-button-label__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-radio-button-label__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-radio-button-label__icon svg path {
  fill: currentColor;
}
.ds-radio-button-label__form {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-radio-button-label-gap, 8px);
}
.ds-radio-button-label__left {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-radio-button-label__цвет-и-палитра {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-radio-button-label-text-color, #333333);
  font-size: var(--ds-typography-font-size-3-5x);
  font-weight: var(--ds-typography-font-weight-regular);
  line-height: var(--ds-typography-line-height-5x);
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label__right {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-radio-button-label__support {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 var(--ds-radio-button-label-pad-left-support-7x, 28px);
}
.ds-radio-button-label__support-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-radio-button-label-text-support-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-radio-button-label-text-support-color, #616161);
}
.ds-radio-button-label--normal.ds-radio-button-label--deselected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--normal.ds-radio-button-label--selected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--error.ds-radio-button-label--deselected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--error.ds-radio-button-label--selected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--disable.ds-radio-button-label--deselected {
  color: var(--ds-color-radio-button-label-text-disable-color, #9e9e9e);
}
.ds-radio-button-label--disable.ds-radio-button-label--selected {
  color: var(--ds-color-radio-button-label-text-disable-color, #9e9e9e);
}
```
</details>

#### Scroll `[53615:15339]` — 12 вариантов
**Описание и рекомендации по применению:**
Полоса прокрутки — прокрутка длинного содержимого: таблицы, списка, панели.  
Берите её для оформления прокручиваемых блоков в макете; в готовом интерфейсе полосу рисует браузер.  

Как выбрать вариант:  
Position=First — ползунок у начала; Middle — в середине; Last — в конце.  
Size=M, S — по толщине полосы под размер блока.  
Состояния: Default, Hover.
- **Size** (VARIANT): M, S
- **Position** (VARIANT): First, Last, Middle
- **State** (VARIANT): Default, Hover
- Размеры и параметры:
    - ширина: `184px` (фикс.)
    - внутренние отступы: `var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px)`
- Модификаторы (что меняет каждый):
    - `--first`
    - `--last`
    - `--middle`: align-items `center`
    - `--s`: ширина `var(--ds-size-2x)`
- Состояния: `:hover` (наведение)
- Разметка:

```html
<div class="ds-scroll ds-scroll--first">
  <div class="ds-scroll__background"></div>
  <div class="ds-scroll__knob"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-scroll {
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
  width: 184px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-scroll__background {
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-scroll-border-radius, 8px);
  background: var(--ds-color-scroll-default-background, #fafafa);
}
.ds-scroll__knob {
  height: var(--ds-size-2x);
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2-5x) var(--ds-size-2-5x) var(--ds-size-2-5x) var(--ds-size-2-5x);
  border-radius: var(--ds-scroll-knob-radius, 8px);
  background: var(--ds-color-scroll-default-knob-color, #d6d6d6);
}
.ds-scroll--s {
  width: var(--ds-size-2x);
}
.ds-scroll--first:hover {
  background: var(--ds-color-scroll-hover-background, #ebebeb);
}
.ds-scroll--middle {
  align-items: center;
}
.ds-scroll--middle:hover {
  background: var(--ds-color-scroll-hover-background, #ebebeb);
}
.ds-scroll--last:hover {
  background: var(--ds-color-scroll-hover-background, #ebebeb);
}
```
</details>

#### Scroll tabs `[59032:1821]` — 4 вариантов
**Описание и рекомендации по применению:**
Стрелка прокрутки вкладок — появляется, когда вкладки не помещаются по ширине.  
Служебный элемент вкладок: ставится по краям строки вкладок, отдельно не используется. Вкладки не переносите на вторую строку — прокручивайте.  

Как выбрать вариант: сторона прокрутки — влево или вправо.
- **Orientation** (VARIANT): Left, Right
- **State** (VARIANT): Default, Hover
- Размеры и параметры:
    - высота: минимум `var(--ds-size-7x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `0 0 0 48px`
    - промежуток между элементами: `var(--ds-size-2-5x)`
- Модификаторы (что меняет каждый):
    - `--left`: внутренние отступы `0 48px 0 0`
- Разметка:

```html
<div class="ds-scroll-tabs ds-scroll-tabs--left">
  <div class="ds-scroll-tabs__button-icon"></div>
  <span class="ds-scroll-tabs__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-scroll-tabs__icon-size"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-scroll-tabs {
  min-height: var(--ds-size-7x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: 0 0 0 48px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-scroll-tabs__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-scroll-tabs__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-scroll-tabs__icon svg path {
  fill: currentColor;
}
.ds-scroll-tabs__button-icon {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-icon-gap, 8px);
  padding: var(--ds-button-icon-s-size-pad-top, 4px) var(--ds-button-icon-s-size-pad-right, 4px) var(--ds-button-icon-s-size-pad-bottom, 4px) var(--ds-button-icon-s-size-pad-left, 4px);
  border-radius: var(--ds-button-icon-border-radius, 8px);
  background: var(--ds-color-button-icon-neutral-filled-default-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
}
.ds-scroll-tabs__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-scroll-tabs--left {
  padding: 0 48px 0 0;
}
```
</details>

#### Search `[54453:1620]` — 15 вариантов
**Описание и рекомендации по применению:**
Поле поиска — фильтрация списка или таблицы по строке: поиск товара, накладной, сотрудника.  
Показывайте результаты по мере ввода, а не по кнопке; крестик справа очищает запрос.  

Как выбрать вариант:  
Size=M — основной; S — панели и шапки блоков; XS — строки таблиц и плотные панели.  
Состояния: Default, Hover, Focus, Focus+Value, Completed, Disable.
- **Size** (VARIANT): M, S, XS
- **State** (VARIANT): Completed, Default, Disable, Focus, Focus+Value, Hover
- Прочие свойства: Left icon#54453:0 (BOOLEAN), Right icon#54459:3 (BOOLEAN)
- Размеры и параметры:
    - ширина: `243px` (фикс.)
    - внутренние отступы: `var(--ds-search-m-size-pad-top, 12px) var(--ds-search-m-size-pad-right, 12px) var(--ds-search-m-size-pad-bottom, 12px) var(--ds-search-m-size-pad-left, 12px)`
    - промежуток между элементами: `var(--ds-search-gap, 8px)`
    - скругление: `var(--ds-search-border-radius, 12px)`
    - рамка: `1px solid var(--ds-color-search-default-border-color, #e0e0e0)`
    - фон: `var(--ds-color-search-background, #f8f9fc)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--s`: внутренние отступы `var(--ds-search-s-size-pad-top, 8px) var(--ds-search-s-size-pad-right, 12px) var(--ds-search-s-size-pad-bottom, 8px) var(--ds-search-s-size-pad-left, 12px)`, ширина `var(--ds-size-5x)`, высота `var(--ds-size-5x)`
    - `--xs`: высота `var(--ds-size-9x)`, ширина `var(--ds-size-9x)`, внутренние отступы `var(--ds-size-1-5x) var(--ds-size-1-5x) var(--ds-size-1-5x) var(--ds-size-1-5x)`, скругление `var(--ds-size-circular)`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-search ds-search--disabled">
  <div class="ds-search__divider"></div>
  <span class="ds-search__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-search__icon-size"></div>
  <span class="ds-search__label">Текст</span>
  <div class="ds-search__right-icon"></div>
  <span class="ds-search__text">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-search {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-search-gap, 8px);
  width: 243px;
  padding: var(--ds-search-m-size-pad-top, 12px) var(--ds-search-m-size-pad-right, 12px) var(--ds-search-m-size-pad-bottom, 12px) var(--ds-search-m-size-pad-left, 12px);
  border-radius: var(--ds-search-border-radius, 12px);
  background: var(--ds-color-search-background, #f8f9fc);
  border: 1px solid var(--ds-color-search-default-border-color, #e0e0e0);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-search__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
  white-space: nowrap;
}
.ds-search__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-search__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-search__icon svg path {
  fill: currentColor;
}
.ds-search__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-search__text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-search-default-text-color, #d6d6d6);
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
}
.ds-search__right-icon {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
}
.ds-search__divider {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-search--s {
  padding: var(--ds-search-s-size-pad-top, 8px) var(--ds-search-s-size-pad-right, 12px) var(--ds-search-s-size-pad-bottom, 8px) var(--ds-search-s-size-pad-left, 12px);
}
.ds-search--s .ds-search__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-search--xs {
  height: var(--ds-size-9x);
  width: var(--ds-size-9x);
  padding: var(--ds-size-1-5x) var(--ds-size-1-5x) var(--ds-size-1-5x) var(--ds-size-1-5x);
  border-radius: var(--ds-size-circular);
}
.ds-search--xs .ds-search__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-search:disabled {
  background: var(--ds-color-search-disable-background, #ebebeb);
  color: var(--ds-color-search-disable-text-color, #9e9e9e);
}
.ds-search.ds-search--disabled {
  background: var(--ds-color-search-disable-background, #ebebeb);
  color: var(--ds-color-search-disable-text-color, #9e9e9e);
}
.ds-search:focus-visible {
  color: var(--ds-color-search-focusvalue-text-color, #333333);
}
.ds-search:hover {
  border: 1px solid var(--ds-color-search-hover-border-color, #9e9e9e);
}
.ds-search--disabled {
  pointer-events: none;
}
```
</details>

#### Select (Сontainer) `[57735:17612]` — 1 вариантов
**Описание и рекомендации по применению:**
Контейнер выпадающего списка — подложка с тенью, в которую складываются пункты Select item.  
Берите его для собственного списка вместо рисования своей подложки; отступы и тень уже заданы.
- **Type** (VARIANT): Сontainer
- Прочие свойства: Scroll#55632:0 (BOOLEAN), Item container#56968:88 (SLOT), Title#57636:8 (BOOLEAN), Search#57740:3 (BOOLEAN), Button#57740:5 (BOOLEAN), Divider header#57862:2 (BOOLEAN), Divider footer#57862:4 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `406px`, растёт по контенту
    - ширина: `240px` (фикс.)
    - внутренние отступы: `var(--ds-menu-pad-top, 8px) 0 var(--ds-menu-pad-bottom, 8px) 0`
    - промежуток между элементами: `var(--ds-space-0)`
    - скругление: `var(--ds-radius-3x, 12px)`
    - фон: `var(--ds-color-menu-background, #ffffff)`
    - тень: `var(--ds-shadow-shadows-08-dp-s)`
- Модификаторы (что меняет каждый):
    - `--container`: color `var(--ds-color-search-default-text-color, #d6d6d6)`
- Разметка:

```html
<div class="ds-select-container ds-select-container--container">
  <div class="ds-select-container__button"></div>
  <div class="ds-select-container__button-group"></div>
  <div class="ds-select-container__content"></div>
  <div class="ds-select-container__divider"></div>
  <span class="ds-select-container__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-select-container__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-select-container__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-select-container__label">Текст</span>
  <div class="ds-select-container__scroll"></div>
  <div class="ds-select-container__search"></div>
  <span class="ds-select-container__title">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-select-container {
  min-height: 406px;
  width: 240px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-space-0);
  padding: var(--ds-menu-pad-top, 8px) 0 var(--ds-menu-pad-bottom, 8px) 0;
  border-radius: var(--ds-radius-3x, 12px);
  background: var(--ds-color-menu-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-container__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
  white-space: nowrap;
}
.ds-select-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-container__icon svg path {
  fill: currentColor;
}
.ds-select-container__search {
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  padding: 0 var(--ds-size-2x) 0 var(--ds-size-2x);
}
.ds-select-container__title {
  display: flex;
  flex-direction: row;
  gap: var(--ds-select-item-gap, 8px);
  padding: var(--ds-select-item-pad-top, 8px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom, 8px) var(--ds-select-item-pad-left, 16px);
  background: var(--ds-color-menu-item-default-background, #ffffff);
}
.ds-select-container__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-select-container__content {
  display: flex;
  flex-direction: column;
}
.ds-select-container__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-select-container__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-select-container__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-select-container__button-group {
  height: 44px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
  padding: var(--ds-button-group-margins-pad-top, 8px) var(--ds-button-group-margins-pad-right, 16px) var(--ds-button-group-margins-pad-bottom, 8px) var(--ds-button-group-margins-pad-left, 16px);
}
.ds-select-container__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-s-size-gap, 4px);
  padding: var(--ds-button-s-size-pad-top, 4px) var(--ds-button-s-size-pad-right, 8px) var(--ds-button-s-size-pad-bottom, 4px) var(--ds-button-s-size-pad-left, 8px);
  border-radius: var(--ds-button-border-radius, 8px);
  border: 1px solid var(--ds-color-button-neutral-outlined-default-border-color, #e0e0e0);
}
.ds-select-container--container {
  color: var(--ds-color-search-default-text-color, #d6d6d6);
}
```
</details>

#### Select cell `[60231:74976]` — 7 вариантов
**Описание и рекомендации по применению:**
Список выбора внутри ячейки таблицы — выбор значения прямо в строке: склад, статус, единица измерения.  
Используйте в редактируемых таблицах; вне таблицы берите Select form.  

Состояния: Default, Hover, Focus, Focus+Value, Error, Error+Hover, Disable.
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Value, Hover
- Размеры и параметры:
    - высота: минимум `var(--ds-size-9x)`, растёт по контенту
    - ширина: `200px` (фикс.)
    - внутренние отступы: `var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px)`
    - промежуток между элементами: `var(--ds-size-2x)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-select-cell ds-select-cell--disabled">
  <span class="ds-select-cell__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-select-cell__input"></div>
  <div class="ds-select-cell__input-frame"></div>
  <span class="ds-select-cell__label">Текст</span>
  <span class="ds-select-cell__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-select-cell {
  min-height: var(--ds-size-9x);
  width: 200px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-select-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-cell__icon svg path {
  fill: currentColor;
}
.ds-select-cell__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-select-cell__input-frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-select-cell__support {
  display: flex;
  flex-direction: row;
}
.ds-select-cell:hover {
  background: var(--ds-palette-neutral-50, #f5f5f5);
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-select-cell:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-select-cell:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-cell.ds-select-cell--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-cell--disabled {
  pointer-events: none;
}
```
</details>

#### Select form `[57862:17226]` — 22 вариантов
**Описание и рекомендации по применению:**
Список выбора — выбор значения из готового набора: склад, поставщик, тип оплаты.  
Берите его, когда вариантов много и они известны заранее; для 2–3 вариантов на виду используйте Radio button или Toggle buttons, для поиска по большому справочнику — Autocomplete.  

Состав: Label, поле со значением и стрелкой, выпадающий список (Select item внутри контейнера), support-текст под полем.  

Как выбрать вариант:  
Variant=Empty — значение не выбрано; Populated — значение выбрано.  
Size=M — основной; S и XS — плотные формы и таблицы.  
Состояния: Default, Hover, Focus, Focus+Value, Error, Disable.
- **Size** (VARIANT): M, S, XS
- **Variant** (VARIANT): Empty, Populated
- **State** (VARIANT): Default, Disable, Error, Focus, Focus+Value, Hover
- Размеры и параметры:
    - ширина: `250px` (фикс.)
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--empty`: color `var(--ds-color-form-field-input-label-text-color, #616161)`, color `var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e)`
    - `--populated`: color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`, color `var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e)`
    - `--s`: ширина `var(--ds-size-5x)`, высота `var(--ds-size-5x)`
    - `--xs`: ширина `var(--ds-size-5x)`, высота `var(--ds-size-5x)`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-select-form ds-select-form--disabled">
  <span class="ds-select-form__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-select-form__input"></div>
  <div class="ds-select-form__input-frame"></div>
  <span class="ds-select-form__label">Текст</span>
  <span class="ds-select-form__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-select-form {
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-form__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-select-form__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-form__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-form__icon svg path {
  fill: currentColor;
}
.ds-select-form__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-select-form__input-frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-select-form__support {
  display: flex;
  flex-direction: row;
}
.ds-select-form--s .ds-select-form__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-select-form--xs .ds-select-form__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-select-form--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-select-form--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-select-form--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-select-form--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-select-form--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-select-form--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-select-form--empty.ds-select-form--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-select-form--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-form--populated.ds-select-form--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-form--disabled {
  pointer-events: none;
}
```
</details>

#### Select item `[57735:17872]` — 8 вариантов
**Описание и рекомендации по применению:**
Пункт выпадающего списка — одна строка выбора внутри Select: значение, при необходимости с подзаголовком и иконкой.  
Подзаголовок используйте, когда одного названия недостаточно (артикул, склад, комментарий).  

Состояния: Default, Hover, Press, Selected, Back selected, Error, Disable.
- **State** (VARIANT): Back selected, Default, Disable, Error, Hover, Press, Selected
- **Subtitle** (VARIANT): False, True
- Прочие свойства: Element left#54167:1 (BOOLEAN), Element right#54167:6 (BOOLEAN), Label up#54741:15 (BOOLEAN), Label down#54741:30 (BOOLEAN), Left#60868:0 (BOOLEAN), Right#60868:1 (BOOLEAN)
- Размеры и параметры:
    - ширина: `258px` (фикс.)
    - внутренние отступы: `var(--ds-select-item-pad-top-sub, 12px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom-sub, 6px) var(--ds-select-item-pad-left, 16px)`
    - промежуток между элементами: `var(--ds-select-item-gap, 8px)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--false`: внутренние отступы `var(--ds-select-item-pad-top, 8px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom, 8px) var(--ds-select-item-pad-left, 16px)`, фон `var(--ds-color-select-item-default-background, #ffffff)`, color `var(--ds-color-select-item-text-label-color, #616161)`, фон `var(--ds-color-select-item-disable-background, #ffffff)`
    - `--true`: align-items `center`, фон `var(--ds-color-select-item-default-background, #ffffff)`, color `var(--ds-color-select-item-text-label-color, #616161)`
- Состояния: `:active` (нажатие), `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-select-item ds-select-item--disabled">
  <div class="ds-select-item__content"></div>
  <span class="ds-select-item__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-select-item__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-select-item__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-select-item__icon-size"></div>
  <span class="ds-select-item__label">Текст</span>
  <div class="ds-select-item__label-down"></div>
  <div class="ds-select-item__label-up"></div>
  <div class="ds-select-item__subtitle"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-select-item {
  width: 258px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-select-item-gap, 8px);
  padding: var(--ds-select-item-pad-top-sub, 12px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom-sub, 6px) var(--ds-select-item-pad-left, 16px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-item__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-select-item-text-label-color, #616161);
  white-space: nowrap;
}
.ds-select-item__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-item__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-item__icon svg path {
  fill: currentColor;
}
.ds-select-item__element-left {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-select-item__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-select-item__content {
  display: flex;
  flex-direction: column;
}
.ds-select-item__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-select-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item__subtitle {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-select-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-m-10-normal-medium-size);
  line-height: var(--ds-font-caption-m-10-normal-medium-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-medium-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-medium-weight);
  text-transform: capitalize;
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-select-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-select-item--true {
  align-items: center;
  background: var(--ds-color-select-item-default-background, #ffffff);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item--false {
  padding: var(--ds-select-item-pad-top, 8px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom, 8px) var(--ds-select-item-pad-left, 16px);
  background: var(--ds-color-select-item-default-background, #ffffff);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item--false:hover {
  background: var(--ds-color-select-item-hover-background, #f5f5f5);
}
.ds-select-item--false:active {
  background: var(--ds-color-select-item-press-background, #e0e0e0);
}
.ds-select-item--false:disabled {
  background: var(--ds-color-select-item-disable-background, #ffffff);
  color: var(--ds-color-select-item-disable-label-text-color, #9e9e9e);
}
.ds-select-item--false.ds-select-item--disabled {
  background: var(--ds-color-select-item-disable-background, #ffffff);
  color: var(--ds-color-select-item-disable-label-text-color, #9e9e9e);
}
.ds-select-item--disabled {
  pointer-events: none;
}
```
</details>

#### Sidenav control `[55142:1734]` — 6 вариантов
**Описание и рекомендации по применению:**
Кнопка свёртывания бокового меню — переключает меню между раскрытым и свёрнутым видом.  
Стоит на границе меню; в макете показывайте её в том же состоянии, что и само меню.  

Состояния: Default, Hover, Press.
- **Mode** (VARIANT): Collapsed, Expanded
- **State** (VARIANT): Default, Hover, Press
- Прочие свойства: Divider#55147:0 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `41px`, растёт по контенту
    - ширина: `200px` (фикс.)
    - промежуток между элементами: `var(--ds-sidenav-control-expanded-gap)`
- Модификаторы (что меняет каждый):
    - `--collapsed`: ширина `fit-content`, промежуток между элементами `var(--ds-sidenav-control-collapsed-gap)`
    - `--expanded`: фон `var(--ds-color-sidenav-control-background, #263136)`, color `var(--ds-color-sidenav-control-text-color, #ffffff)`
- Состояния: `:active` (нажатие), `:hover` (наведение)
- Разметка:

```html
<div class="ds-sidenav-control ds-sidenav-control--collapsed">
  <div class="ds-sidenav-control__content"></div>
  <div class="ds-sidenav-control__divider"></div>
  <span class="ds-sidenav-control__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-sidenav-control__icon-size"></div>
  <span class="ds-sidenav-control__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-sidenav-control {
  min-height: 41px;
  display: flex;
  flex-direction: column;
  width: 200px;
  gap: var(--ds-sidenav-control-expanded-gap);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-control__label {
  font-size: var(--ds-font-caption-m-10-normal-regular-size);
  line-height: var(--ds-font-caption-m-10-normal-regular-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-regular-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-regular-weight);
  color: var(--ds-color-sidenav-control-text-color, #ffffff);
  white-space: nowrap;
}
.ds-sidenav-control__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-sidenav-control__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-sidenav-control__icon svg path {
  fill: currentColor;
}
.ds-sidenav-control__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-sidenav-control-expanded-gap-content, 8px);
  padding: var(--ds-sidenav-control-pad-top, 8px) var(--ds-sidenav-control-pad-right, 16px) var(--ds-sidenav-control-pad-bottom, 12px) var(--ds-sidenav-control-pad-left, 16px);
  background: var(--ds-color-sidenav-control-background, #263136);
}
.ds-sidenav-control__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-sidenav-control__свернуть-меню {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-control-text-color, #ffffff);
  font-size: var(--ds-font-caption-m-10-normal-regular-size);
  line-height: var(--ds-font-caption-m-10-normal-regular-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-regular-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-regular-weight);
  color: var(--ds-color-sidenav-control-text-color, #ffffff);
}
.ds-sidenav-control__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-sidenav-control--collapsed:hover {
  background: var(--ds-color-sidenav-control-background-hover, #36474e);
}
.ds-sidenav-control--collapsed:active {
  background: var(--ds-color-sidenav-control-background-press, #36474e);
}
.ds-sidenav-control--expanded {
  background: var(--ds-color-sidenav-control-background, #263136);
  color: var(--ds-color-sidenav-control-text-color, #ffffff);
}
.ds-sidenav-control--expanded:hover {
  background: var(--ds-color-sidenav-control-background-hover, #36474e);
}
.ds-sidenav-control--expanded:active {
  background: var(--ds-color-sidenav-control-background-press, #36474e);
}
.ds-sidenav-control--collapsed {
  width: fit-content;
  gap: var(--ds-sidenav-control-collapsed-gap);
}
```
</details>

#### Sidenav Footer `[55111:1056]` — 3 вариантов
**Описание и рекомендации по применению:**
Подвал бокового меню — пользователь, помощь и выход под списком разделов.  
В свёрнутом меню остаются только иконки.  

Как выбрать вариант: уровень меню (основное или вложенное) и раскрыто ли меню.
- **Type** (VARIANT): L1, L2
- **Mode** (VARIANT): Collapsed, Expanded
- Прочие свойства: Divider#55147:10 (BOOLEAN), Container#59128:17 (SLOT), Container#59128:25 (SLOT)
- Размеры и параметры:
    - ширина: `260px` (фикс.)
    - внутренние отступы: `var(--ds-sidenav-footer-l2-pad-top, 12px) var(--ds-sidenav-footer-l2-pad-right, 16px) var(--ds-sidenav-footer-l2-pad-bottom, 12px) var(--ds-sidenav-footer-l2-pad-left, 16px)`
    - промежуток между элементами: `var(--ds-sidenav-footer-l2-gap, 12px)`
- Модификаторы (что меняет каждый):
    - `--l1`: ширина `200px`, направление `column`, color `var(--ds-color-sidenav-item-l1-text-color, #ffffff)`, ширина `52px`
    - `--l2`: направление `row`, align-items `center`, фон `var(--ds-color-sidenav-footer-l2-background, #ffffff)`, color `var(--ds-color-sidenav-footer-l2-text-color, #616161)`
- Разметка:

```html
<div class="ds-sidenav-footer ds-sidenav-footer--l1">
  <div class="ds-sidenav-footer__divider"></div>
  <span class="ds-sidenav-footer__label">Текст</span>
  <div class="ds-sidenav-footer__logo-iiko"></div>
  <div class="ds-sidenav-footer__vector"></div>
  <div class="ds-sidenav-footer__ver-7-8-6-29440"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-sidenav-footer {
  display: flex;
  width: 260px;
  padding: var(--ds-sidenav-footer-l2-pad-top, 12px) var(--ds-sidenav-footer-l2-pad-right, 16px) var(--ds-sidenav-footer-l2-pad-bottom, 12px) var(--ds-sidenav-footer-l2-pad-left, 16px);
  gap: var(--ds-sidenav-footer-l2-gap, 12px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-footer__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-footer-l2-text-color, #616161);
  white-space: nowrap;
}
.ds-sidenav-footer__logo-iiko {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-sidenav-footer__vector {
  height: 9.8px;
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-footer-l2-logo, #ff5252);
}
.ds-sidenav-footer__divider {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-sidenav-footer__ver-7-8-6-29440 {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-footer-l2-text-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-footer-l2-text-color, #616161);
}
.ds-sidenav-footer--l2.ds-sidenav-footer--expanded {
  flex-direction: row;
  align-items: center;
  background: var(--ds-color-sidenav-footer-l2-background, #ffffff);
  color: var(--ds-color-sidenav-footer-l2-text-color, #616161);
}
.ds-sidenav-footer--l1.ds-sidenav-footer--expanded {
  width: 200px;
  flex-direction: column;
  color: var(--ds-color-sidenav-item-l1-text-color, #ffffff);
}
.ds-sidenav-footer--l1.ds-sidenav-footer--collapsed {
  width: 52px;
  flex-direction: column;
  color: var(--ds-color-text-accent, #448aff);
}
```
</details>

#### Sidenav header `[55045:637]` — 3 вариантов
**Описание и рекомендации по применению:**
Шапка бокового меню — логотип и название заведения или раздела над списком пунктов.  
В свёрнутом меню остаётся только знак логотипа.  

Как выбрать вариант: уровень меню (основное или вложенное) и раскрыто ли меню.
- **Type** (VARIANT): L1, L2
- **Mode** (VARIANT): Collapsed, Expanded
- Прочие свойства: Element right#55074:0 (BOOLEAN), Element left#55661:0 (BOOLEAN), Divider#59107:0 (BOOLEAN), Informer#59128:5 (BOOLEAN)
- Размеры и параметры:
    - ширина: `200px` (фикс.)
    - внутренние отступы: `var(--ds-sidenav-header-pad-top, 12px) var(--ds-sidenav-header-l1-expanded-pad-right, 16px) var(--ds-sidenav-header-pad-bottom, 12px) var(--ds-sidenav-header-l1-expanded-pad-left, 16px)`
    - промежуток между элементами: `var(--ds-sidenav-header-l1-expanded-gap, 92px)`
- Модификаторы (что меняет каждый):
    - `--l1`: направление `row`, фон `var(--ds-color-sidenav-header-l1-background, #263136)`, ширина `52px`, направление `column`
    - `--l2`: высота `48px`, ширина `260px`, направление `row`, промежуток между элементами `var(--ds-sidenav-header-l2-gap, 8px)`
- Разметка:

```html
<div class="ds-sidenav-header ds-sidenav-header--l1">
  <div class="ds-sidenav-header__close"></div>
  <span class="ds-sidenav-header__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-sidenav-header__icon-size"></div>
  <span class="ds-sidenav-header__label">Текст</span>
  <div class="ds-sidenav-header__logo-iiko"></div>
  <div class="ds-sidenav-header__vector"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-sidenav-header {
  display: flex;
  align-items: center;
  width: 200px;
  padding: var(--ds-sidenav-header-pad-top, 12px) var(--ds-sidenav-header-l1-expanded-pad-right, 16px) var(--ds-sidenav-header-pad-bottom, 12px) var(--ds-sidenav-header-l1-expanded-pad-left, 16px);
  gap: var(--ds-sidenav-header-l1-expanded-gap, 92px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-header__label {
  font-size: var(--ds-font-body-m-16-normal-medium-size);
  line-height: var(--ds-font-body-m-16-normal-medium-line);
  letter-spacing: var(--ds-font-body-m-16-normal-medium-spacing);
  font-weight: var(--ds-font-body-m-16-normal-medium-weight);
  color: var(--ds-color-sidenav-header-l2-text-color, #333333);
  white-space: nowrap;
}
.ds-sidenav-header__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-sidenav-header__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-sidenav-header__icon svg path {
  fill: currentColor;
}
.ds-sidenav-header__logo-iiko {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
}
.ds-sidenav-header__vector {
  height: 14.7px;
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-header-l1-expanded-logo, #ffffff);
}
.ds-sidenav-header__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-sidenav-header__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-sidenav-header--l1.ds-sidenav-header--expanded {
  flex-direction: row;
  background: var(--ds-color-sidenav-header-l1-background, #263136);
}
.ds-sidenav-header--l2.ds-sidenav-header--expanded {
  height: 48px;
  width: 260px;
  flex-direction: row;
  gap: var(--ds-sidenav-header-l2-gap, 8px);
  padding: var(--ds-sidenav-header-pad-top, 12px) var(--ds-sidenav-header-l2-pad-right, 16px) var(--ds-sidenav-header-pad-bottom, 12px) var(--ds-sidenav-header-l2-pad-left, 16px);
  background: var(--ds-color-sidenav-header-l2-background, #ffffff);
  color: var(--ds-color-sidenav-header-l2-text-color, #333333);
}
.ds-sidenav-header--l1.ds-sidenav-header--collapsed {
  width: 52px;
  flex-direction: column;
  padding: var(--ds-sidenav-header-pad-top, 12px) var(--ds-sidenav-header-l1-collapsed-pad-right, 14px) var(--ds-sidenav-header-pad-bottom, 12px) var(--ds-sidenav-header-l1-collapsed-pad-left, 14px);
  background: var(--ds-color-sidenav-header-l1-background, #263136);
}
```
</details>

#### Sidenav item `[55070:3734]` — 13 вариантов
**Описание и рекомендации по применению:**
Пункт бокового меню — раздел приложения в левой навигации: «Заказы», «Склады», «Отчёты».  
Три уровня вложенности: раздел, подраздел, пункт подраздела. В свёрнутом меню видна только иконка, название показывайте тултипом.  

Как выбрать вариант:  
Type=L1, L2, L3 — уровень вложенности пункта.  
Mode=Expanded — меню раскрыто (иконка + название); Collapsed — свёрнуто (только иконка).  
Состояния: Default, Hover, Active (текущий раздел), Selected (выбран).
- **Type** (VARIANT): L1, L2, L3
- **Mode** (VARIANT): Collapsed, Expanded
- **State** (VARIANT): Active, Default, Hover, Selected
- Прочие свойства: Element right#55070:0 (BOOLEAN), Badge#55083:0 (BOOLEAN), Divider#55219:13 (BOOLEAN), Indicator#59087:0 (BOOLEAN)
- Размеры и параметры:
    - ширина: `260px` (фикс.)
    - внутренние отступы: `var(--ds-sidenav-item-l3-pad-top, 8px) var(--ds-sidenav-item-l3-pad-right, 16px) var(--ds-sidenav-item-l3-pad-bottom, 8px) var(--ds-sidenav-item-l3-pad-left, 32px)`
    - промежуток между элементами: `var(--ds-sidenav-item-l3-gap, 8px)`
- Модификаторы (что меняет каждый):
    - `--l1`: ширина `200px`, направление `row`, align-items `center`, промежуток между элементами `var(--ds-sidenav-item-l1-gap-container, 8px)`
    - `--l2`: направление `column`, фон `var(--ds-color-sidenav-item-l2-background, #ffffff)`, color `var(--ds-color-sidenav-item-l2-text-color, #333333)`
    - `--l3`: направление `row`, align-items `center`, фон `var(--ds-color-sidenav-item-l3-background, #ffffff)`, color `var(--ds-color-sidenav-item-l3-text-color, #333333)`
- Состояния: `:hover` (наведение)
- Разметка:

```html
<div class="ds-sidenav-item ds-sidenav-item--l1">
  <div class="ds-sidenav-item__l3"></div>
  <span class="ds-sidenav-item__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-sidenav-item {
  display: flex;
  width: 260px;
  padding: var(--ds-sidenav-item-l3-pad-top, 8px) var(--ds-sidenav-item-l3-pad-right, 16px) var(--ds-sidenav-item-l3-pad-bottom, 8px) var(--ds-sidenav-item-l3-pad-left, 32px);
  gap: var(--ds-sidenav-item-l3-gap, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-item__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-item-l3-text-color, #333333);
  white-space: nowrap;
}
.ds-sidenav-item__l3 {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-item-l3-text-color, #333333);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-item-l3-text-color, #333333);
}
.ds-sidenav-item--l3.ds-sidenav-item--expanded:hover {
  background: var(--ds-color-sidenav-item-l3-background-hover, #f8f9fc);
}
.ds-sidenav-item--l3.ds-sidenav-item--expanded {
  flex-direction: row;
  align-items: center;
  background: var(--ds-color-sidenav-item-l3-background, #ffffff);
  color: var(--ds-color-sidenav-item-l3-text-color, #333333);
}
.ds-sidenav-item--l2.ds-sidenav-item--expanded {
  flex-direction: column;
  background: var(--ds-color-sidenav-item-l2-background, #ffffff);
  color: var(--ds-color-sidenav-item-l2-text-color, #333333);
}
.ds-sidenav-item--l2.ds-sidenav-item--expanded:hover {
  background: var(--ds-color-sidenav-item-l2-background-hover, #f8f9fc);
}
.ds-sidenav-item--l1.ds-sidenav-item--expanded:hover {
  background: var(--ds-color-sidenav-item-l1-background-hover, #36474e);
}
.ds-sidenav-item--l1.ds-sidenav-item--expanded {
  width: 200px;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-sidenav-item-l1-gap-container, 8px);
  padding: var(--ds-sidenav-item-l1-pad-top, 12px) var(--ds-sidenav-item-l1-pad-right, 16px) var(--ds-sidenav-item-l1-pad-bottom, 12px) var(--ds-sidenav-item-l1-pad-left, 16px);
  background: var(--ds-color-sidenav-item-l1-background, #263136);
  color: var(--ds-color-sidenav-item-l1-text-color, #ffffff);
}
.ds-sidenav-item--l1.ds-sidenav-item--collapsed:hover {
  background: var(--ds-color-sidenav-item-l1-background-hover, #36474e);
}
.ds-sidenav-item--l1.ds-sidenav-item--collapsed {
  width: fit-content;
  flex-direction: row;
  padding: var(--ds-sidenav-item-l1-pad-top, 12px) var(--ds-sidenav-item-l1-pad-right, 16px) var(--ds-sidenav-item-l1-pad-bottom, 12px) var(--ds-sidenav-item-l1-pad-left, 16px);
  background: var(--ds-color-sidenav-item-l1-background, #263136);
}
```
</details>

#### Sidenav View `[55074:393]` — 3 вариантов
**Описание и рекомендации по применению:**
Боковое меню целиком — готовая левая навигация: шапка, пункты, подвал.  
Берите её как основу экрана и подставляйте свои пункты; ширину раскрытого и свёрнутого меню не меняйте.  

Как выбрать вариант: уровень меню и его состояние — раскрыто или свёрнуто.
- **Type** (VARIANT): L1, L2
- **State** (VARIANT): Collapsed, Expanded
- Прочие свойства: Scroll#55227:26 (BOOLEAN), Container#59137:0 (SLOT), Container#59137:4 (SLOT), Container#59137:8 (SLOT), Container#59137:12 (SLOT), Info#59160:3 (BOOLEAN), More Pannel#59214:0 (BOOLEAN)
- CSS не требуется: собственного оформления нет — компонент задаёт только структуру/поведение, вид приходит от вложенных элементов.

#### Slide toggle `[52887:2592]` — 6 вариантов
**Описание и рекомендации по применению:**
Переключатель — включение и выключение настройки, действие применяется сразу, без кнопки «Сохранить».  
Используйте для режимов и правил: «Требуется подтверждение», «Стоимость товаров в заказе видна сотруднику ресторана». Если выбор нужно подтвердить кнопкой или пунктов несколько — Checkbox.  

Состав: переключатель, Title, support-текст под заголовком (Support down), элемент справа (Element right) — например иконка-подсказка.  
Подпись формулируйте утверждением, а не вопросом; не дублируйте в ней слово «включить».  

Как выбрать вариант:  
Active=On / Off — настройка включена / выключена.  
State=Default, Hover, Disable — обычное состояние, курсор над переключателем, недоступен.
- **Active** (VARIANT): Off, On
- **State** (VARIANT): Default, Disable, Hover
- Прочие свойства: Title#53326:0 (BOOLEAN), Support down#58203:7 (BOOLEAN), Element right#58364:0 (BOOLEAN)
- CSS: выверено вручную, см. `components/Slide-Toggle_DS/slide-toggle.css` в разделе «Полные CSS-стили всех компонентов»

#### Snackbar `[54373:10303]` — 4 вариантов
**Описание и рекомендации по применению:**
Всплывающее сообщение о результате действия: «Изменения сохранены», «Товары добавлены», «Не удалось сохранить изменения», «Сервер временно недоступен».  
Появляется на короткое время внизу экрана и не требует ответа; если решение обязательно — берите диалог.  
Действие внутри допускается одно («Обновить», «Открыть», «Отменить»).  

Как выбрать вариант:  
Type=Single — одна строка сообщения; Complex — с заголовком, описанием и действием.  
Mode=Dark — на светлых экранах; Light — на тёмных.
- **Type** (VARIANT): Complex, Single
- **Mode** (VARIANT): Dark, Light
- Прочие свойства: Element left#54373:16 (BOOLEAN), Element right#54426:0 (BOOLEAN), Progress#58768:0 (BOOLEAN), Content#58768:6 (BOOLEAN), Bottom actions#58768:12 (BOOLEAN)
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - скругление: `var(--ds-snackbar-border-radius, 8px)`
    - тень: `var(--ds-shadow-shadows-08-dp-s)`
- Модификаторы (что меняет каждый):
    - `--complex`: ширина `232px`, фон `var(--ds-color-snackbar-complex-dark-background, #424242)`, color `var(--ds-color-snackbar-complex-dark-text-color, #ffffff)`, ширина `370px`
    - `--single`: фон `var(--ds-color-snackbar-complex-dark-background, #424242)`, color `var(--ds-color-snackbar-complex-dark-text-color, #ffffff)`, ширина `370px`, фон `var(--ds-color-snackbar-complex-light-background, #ffffff)`
- Разметка:

```html
<div class="ds-snackbar ds-snackbar--complex">
  <div class="ds-snackbar__body"></div>
  <div class="ds-snackbar__button"></div>
  <div class="ds-snackbar__content"></div>
  <span class="ds-snackbar__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-snackbar__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-snackbar__label">Текст</span>
  <div class="ds-snackbar__progress"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-snackbar {
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-snackbar-border-radius, 8px);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  width: fit-content;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-snackbar__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-snackbar-complex-dark-text-color, #ffffff);
  white-space: nowrap;
}
.ds-snackbar__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-snackbar__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-snackbar__icon svg path {
  fill: currentColor;
}
.ds-snackbar__body {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-snackbar-gap, 8px);
  padding: var(--ds-snackbar-pad-top, 12px) var(--ds-snackbar-pad-right, 12px) var(--ds-snackbar-pad-bottom, 12px) var(--ds-snackbar-pad-left, 12px);
}
.ds-snackbar__content {
  display: flex;
  flex-direction: row;
  gap: var(--ds-snackbar-gap, 8px);
  padding: var(--ds-space-0) var(--ds-space-0) var(--ds-space-0) var(--ds-space-0);
  border-radius: var(--ds-radius-0);
}
.ds-snackbar__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-s-size-gap, 4px);
  padding: var(--ds-button-s-size-pad-top, 4px) var(--ds-button-s-size-pad-right, 8px) var(--ds-button-s-size-pad-bottom, 4px) var(--ds-button-s-size-pad-left, 8px);
  border-radius: var(--ds-button-border-radius, 8px);
}
.ds-snackbar__element-right {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-snackbar__progress {
  height: var(--ds-size-1x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-snackbar-border-radius, 8px);
  background: var(--ds-color-snackbar-progress-color, #448aff);
}
.ds-snackbar--single.ds-snackbar--dark {
  background: var(--ds-color-snackbar-complex-dark-background, #424242);
  color: var(--ds-color-snackbar-complex-dark-text-color, #ffffff);
}
.ds-snackbar--single.ds-snackbar--light {
  width: 370px;
  background: var(--ds-color-snackbar-complex-light-background, #ffffff);
  color: var(--ds-color-snackbar-complex-light-text-color, #333333);
}
.ds-snackbar--complex.ds-snackbar--dark {
  width: 232px;
  background: var(--ds-color-snackbar-complex-dark-background, #424242);
  color: var(--ds-color-snackbar-complex-dark-text-color, #ffffff);
}
.ds-snackbar--complex.ds-snackbar--light {
  width: 370px;
  background: var(--ds-color-snackbar-complex-light-background, #ffffff);
  color: var(--ds-color-snackbar-complex-light-text-color, #333333);
}
```
</details>

#### State `[54063:12395]` — 2 вариантов
**Описание и рекомендации по применению:**
Подложка состояния под иконкой — круглая или квадратная подсветка при наведении и нажатии.  
Служебный элемент кнопок-иконок и пунктов: подставляется под иконку, отдельно на экран не ставится.
- **State** (VARIANT): Hover, Press
- Размеры и параметры:
    - высота: `var(--ds-size-6x)` (фикс.)
    - ширина: `var(--ds-size-6x)` (фикс.)
- Состояния: `:active` (нажатие), `:hover` (наведение)
<details><summary>CSS компонента</summary>

```css

.ds-state {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-state:hover {
  background: #ebebeb;
}
.ds-state:active {
  background: #e0e0e0;
}
```
</details>

#### Status `[52928:6588]` — 18 вариантов
**Описание и рекомендации по применению:**
Статус — короткая метка состояния объекта: «Новый», «В работе», «Оплачен», «Закрыт».  
Показывайте в таблицах, списках и карточках рядом с названием или в колонке «Статус».  

Как выбрать вариант:  
Accent — активное состояние, действие сейчас выполняется.  
Positive — успех, подтверждение.  
Warning — требуется внимание, просрочено.  
Negative — ошибка, блокирующее состояние.  
Neutral — нейтральное, без акцента.  
Contrast-1 … 4 — дополнительные цвета, когда основных недостаточно.  

Type=Filled — с подложкой, заметный. Type=Text — только текст, не перетягивает внимание.  
Фронт: https://frontend-common.iiko.ru/components/status
- **Style** (VARIANT): Accent, Contrast-1, Contrast-2, Contrast-3, Contrast-4, Negative, Neutral, Positive, Warning
- **Type** (VARIANT): Filled, Text
- Прочие свойства: Element left#17172:1340 (BOOLEAN), Element right#17172:1349 (BOOLEAN)
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-status-pad-top, 4px) var(--ds-status-pad-right, 6px) var(--ds-status-pad-bottom, 4px) var(--ds-status-pad-left, 6px)`
    - промежуток между элементами: `var(--ds-status-gap, 4px)`
    - скругление: `var(--ds-status-border-radius, 8px)`
- Модификаторы (что меняет каждый):
    - `--accent`: фон `var(--ds-color-status-accent-filled-background, #f5f9ff)`, color `var(--ds-color-status-accent-filled-text-color, #448aff)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-accent-text-text-color, #448aff)`
    - `--contrast-1`: фон `var(--ds-color-status-contrast-1-filled-background, #fcf6fd)`, color `var(--ds-color-status-contrast-1-filled-text-color, #9c27b0)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-contrast-1-text-text-color, #9c27b0)`
    - `--contrast-2`: фон `var(--ds-color-status-contrast-2-filled-background, #fcf8f6)`, color `var(--ds-color-status-contrast-2-filled-text-color, #3e261e)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-contrast-2-text-text-color, #3e261e)`
    - `--contrast-3`: фон `var(--ds-color-status-contrast-3-filled-background, #f8fafc)`, color `var(--ds-color-status-contrast-3-filled-text-color, #263136)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-contrast-3-text-text-color, #263136)`
    - `--contrast-4`: фон `var(--ds-color-status-contrast-4-filled-background, #f9fbea)`, color `var(--ds-color-status-contrast-4-filled-text-color, #4f5412)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-contrast-4-text-text-color, #4f5412)`
    - `--negative`: фон `var(--ds-color-status-negative-filled-background, #fff8f8)`, color `var(--ds-color-status-negative-filled-text-color, #ff5252)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-negative-text-text-color, #ff5252)`
    - `--neutral`: фон `var(--ds-color-status-neutral-filled-background, #fafafa)`, color `var(--ds-color-status-neutral-filled-text-color, #616161)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-neutral-text-text-color, #616161)`
    - `--positive`: фон `var(--ds-color-status-positive-filled-background, #f3fcf7)`, color `var(--ds-color-status-positive-filled-text-color, #14b456)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-positive-text-text-color, #14b456)`
    - `--warning`: фон `var(--ds-color-status-warning-filled-background, #fffcf8)`, color `var(--ds-color-status-warning-filled-text-color, #ea7806)`, внутренние отступы `var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text)`, color `var(--ds-color-status-warning-text-text-color, #ea7806)`
- Разметка:

```html
<div class="ds-status ds-status--accent">
  <div class="ds-status__content"></div>
  <span class="ds-status__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-status__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-status__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-status__info"></div>
  <span class="ds-status__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-status {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-status-gap, 4px);
  border-radius: var(--ds-status-border-radius, 8px);
  padding: var(--ds-status-pad-top, 4px) var(--ds-status-pad-right, 6px) var(--ds-status-pad-bottom, 4px) var(--ds-status-pad-left, 6px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-status__label {
  font-size: var(--ds-font-caption-l-12-normal-medium-size);
  line-height: var(--ds-font-caption-l-12-normal-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-medium-weight);
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
  white-space: nowrap;
}
.ds-status__icon {
  flex-shrink: 0;
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-status-icon-color);
}
.ds-status__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-status__icon svg path {
  fill: currentColor;
}
.ds-status__element-left {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-status__info {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-status__content {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-status-neutral-filled-text-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-medium-size);
  line-height: var(--ds-font-caption-l-12-normal-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-medium-weight);
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
}
.ds-status__element-right {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-status--neutral.ds-status--filled {
  background: var(--ds-color-status-neutral-filled-background, #fafafa);
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
}
.ds-status--accent.ds-status--filled {
  background: var(--ds-color-status-accent-filled-background, #f5f9ff);
  color: var(--ds-color-status-accent-filled-text-color, #448aff);
}
.ds-status--positive.ds-status--filled {
  background: var(--ds-color-status-positive-filled-background, #f3fcf7);
  color: var(--ds-color-status-positive-filled-text-color, #14b456);
}
.ds-status--warning.ds-status--filled {
  background: var(--ds-color-status-warning-filled-background, #fffcf8);
  color: var(--ds-color-status-warning-filled-text-color, #ea7806);
}
.ds-status--negative.ds-status--filled {
  background: var(--ds-color-status-negative-filled-background, #fff8f8);
  color: var(--ds-color-status-negative-filled-text-color, #ff5252);
}
.ds-status--contrast-1.ds-status--filled {
  background: var(--ds-color-status-contrast-1-filled-background, #fcf6fd);
  color: var(--ds-color-status-contrast-1-filled-text-color, #9c27b0);
}
.ds-status--contrast-2.ds-status--filled {
  background: var(--ds-color-status-contrast-2-filled-background, #fcf8f6);
  color: var(--ds-color-status-contrast-2-filled-text-color, #3e261e);
}
.ds-status--contrast-3.ds-status--filled {
  background: var(--ds-color-status-contrast-3-filled-background, #f8fafc);
  color: var(--ds-color-status-contrast-3-filled-text-color, #263136);
}
.ds-status--contrast-4.ds-status--filled {
  background: var(--ds-color-status-contrast-4-filled-background, #f9fbea);
  color: var(--ds-color-status-contrast-4-filled-text-color, #4f5412);
}
.ds-status--neutral.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-neutral-text-text-color, #616161);
}
.ds-status--accent.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-accent-text-text-color, #448aff);
}
.ds-status--positive.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-positive-text-text-color, #14b456);
}
.ds-status--warning.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-warning-text-text-color, #ea7806);
}
.ds-status--negative.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-negative-text-text-color, #ff5252);
}
.ds-status--contrast-1.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-1-text-text-color, #9c27b0);
}
.ds-status--contrast-2.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-2-text-text-color, #3e261e);
}
.ds-status--contrast-3.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-3-text-text-color, #263136);
}
.ds-status--contrast-4.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-4-text-text-color, #4f5412);
}
```
</details>

#### Step `[54800:3659]` — 12 вариантов
**Описание и рекомендации по применению:**
Степпер — шаги многошагового процесса: мастер настройки, онбординг, оформление заказа.  
Показывает текущее положение и сколько шагов осталось. Внизу — панель с кнопками «Назад» и «Далее».  
Не сочетайте степпер с крестиком закрытия — если нужно закрыть, используйте кнопку внизу.  

Состав степпера:  
Step — кликабельный шаг (иконка + название).  
Element step — маркер шага: иконка или счётчик на подложке.  
Stepper line — контейнер, строка со всеми маркерами.  
Stepper button — кнопка «Назад» / «Далее» в панели внизу.  
Фронт: https://frontend-common.iiko.ru/components/stepper
- **Background** (VARIANT): Off, On
- **State** (VARIANT): Default, Disable, Error, Hover, Press, Selected
- Прочие свойства: Element left#55771:0 (BOOLEAN), Element right#55771:13 (BOOLEAN), Text#57060:20 (TEXT)
- CSS: выверено вручную, см. `components/Stepper_DS/stepper.css` в разделе «Полные CSS-стили всех компонентов»

#### Stepper button `[55419:7330]` — 12 вариантов
**Описание и рекомендации по применению:**
Кнопка навигации степпера — «Назад» и «Далее» в панели внизу многошагового процесса.  
Используется только вместе со степпером; для обычных действий берите Button.  

Как выбрать вариант:  
Type=Filled — акцентная (обычно «Далее»); Type=Outlined — второстепенная (обычно «Назад»).  
Position=First / Middle / Last — место в группе: First — «Назад» слева, Last — «Далее» справа.  
Content=Icon — только иконка; Content=Text — с текстом.  
Фронт: https://frontend-common.iiko.ru/components/stepper
- **Type** (VARIANT): Filled, Outlined
- **Position** (VARIANT): First, Last, Middle
- **Content** (VARIANT): Icon, Text
- Прочие свойства: Text#55442:0 (BOOLEAN)
- CSS: выверено вручную, см. `components/Stepper_DS/stepper.css` в разделе «Полные CSS-стили всех компонентов»

#### Stepper line `[54689:3072]` — 4 вариантов
**Описание и рекомендации по применению:**
Строка степпера — контейнер со всеми маркерами шагов в один ряд.  
Ставится вверху экрана или диалога многошагового процесса; внутрь вкладываются шаги Step.  

Как выбрать вариант:  
Step=On — с маркерами шагов; Step=Off — контейнер без маркеров, только подложка.  
Background=On — с подложкой под шагами; Background=Off — без подложки, по контенту.  
Фронт: https://frontend-common.iiko.ru/components/stepper
- **Step** (VARIANT): Off, On
- **Background** (VARIANT): Off, On
- Прочие свойства: Content step#59393:0 (SLOT), Content step background#59393:5 (SLOT), Content#59393:10 (SLOT), Content background#59393:15 (SLOT), Scroll left#59393:20 (BOOLEAN), Scroll right#59393:25 (BOOLEAN)
- CSS: выверено вручную, см. `components/Stepper_DS/stepper.css` в разделе «Полные CSS-стили всех компонентов»

#### Tab element `[54404:200]` — 16 вариантов
**Описание и рекомендации по применению:**
Вкладка — один раздел в строке вкладок: название, при необходимости иконка и счётчик.  
Счётчик показывает количество записей в разделе; активная вкладка всегда одна.  

Как выбрать вариант:  
Active=On — текущий раздел; Off — остальные разделы.  
Lvl=1 — основной уровень; Lvl=2 — вложенный.  
Состояния: Default, Hover, Press, Disable.
- **Lvl** (VARIANT): 1, 2
- **State** (VARIANT): Default, Disable, Hover, Press
- **Active** (VARIANT): Off, On
- Прочие свойства: Element left#54447:8 (BOOLEAN), Counter#54447:13 (BOOLEAN), Text#54876:8 (BOOLEAN), Element right#59422:0 (BOOLEAN)
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Table 2 lvl `[60074:44684]` — 2 вариантов
**Описание и рекомендации по применению:**
Вложенный уровень таблицы — подстрока и подъячейка внутри строки: состав блюда, позиции в документе, разбивка по складам.  
Берите его, когда запись раскрывается в детали; для отдельной таблицы уровень не нужен.  

Как выбрать вариант: подстрока целиком или отдельная ячейка второго уровня.
- **Type** (VARIANT): Table cell 2 lvl, Table row 2 lvl
- Прочие свойства: Header 2 lvl#60074:0 (SLOT)
- Размеры и параметры:
    - высота: минимум `72px`, растёт по контенту
    - ширина: `162px` (фикс.)
- Модификаторы (что меняет каждый):
    - `--table-cell-2-lvl`: направление `column`, рамка `1px solid var(--ds-color-stroke-default, #e0e0e0)`
    - `--table-row-2-lvl`: ширина `fit-content`, направление `row`, align-items `center`
- Разметка:

```html
<div class="ds-table-2-lvl ds-table-2-lvl--table-cell-2-lvl">
  <div class="ds-table-2-lvl__header-row"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-table-2-lvl {
  min-height: 72px;
  display: flex;
  width: 162px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-2-lvl__header-row {
  display: flex;
  flex-direction: column;
  background: var(--ds-color-table-row-header-background-header, #f0f5ff);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
}
.ds-table-2-lvl--table-cell-2-lvl {
  flex-direction: column;
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
}
.ds-table-2-lvl--table-row-2-lvl {
  width: fit-content;
  flex-direction: row;
  align-items: center;
}
```
</details>

#### Table Chips Input `[60220:70978]` — 8 вариантов
**Описание и рекомендации по применению:**
Ячейка таблицы с вводом тегов — готовая ячейка вместе с полем тегов и отступами строки.  
Служебный компонент таблицы: ставится в строку, отдельно на экран не выносится.  

Состояния: Default, Hover, Focus, Focus+Placeholder, Focus+Value, Error, Error+Hover, Disable.
- **Style** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Hover, Vocus+Value
- Размеры и параметры:
    - высота: минимум `var(--ds-size-6x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - фон: `#ffffff`
- Модификаторы (что меняет каждый):
    - `--default`: color `#616161`
    - `--disable`: color `#9e9e9e`
    - `--error`: color `#616161`
    - `--error-hover`: color `#616161`
    - `--focus`: color `#333333`
    - `--focus-placeholder`: color `#333333`
    - `--hover`: color `#616161`
    - `--vocus-value`: color `#333333`
- Разметка:

```html
<div class="ds-table-chips-input ds-table-chips-input--default">
  <div class="ds-table-chips-input__frame"></div>
  <span class="ds-table-chips-input__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-table-chips-input__label">Текст</span>
  <span class="ds-table-chips-input__support">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-table-chips-input {
  min-height: var(--ds-size-6x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-chips-input__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-table-chips-input__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-table-chips-input__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-table-chips-input__icon svg path {
  fill: currentColor;
}
.ds-table-chips-input__frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-chips-input-gap-chips-input-frame, 4px);
  border-radius: var(--ds-size-3x);
  background: #f8f9fc;
  border: 1px solid #e0e0e0;
}
.ds-table-chips-input__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-1x);
}
.ds-table-chips-input--default {
  color: #616161;
}
.ds-table-chips-input--hover {
  color: #616161;
}
.ds-table-chips-input--focus {
  color: #333333;
}
.ds-table-chips-input--focus-placeholder {
  color: #333333;
}
.ds-table-chips-input--vocus-value {
  color: #333333;
}
.ds-table-chips-input--error {
  color: #616161;
}
.ds-table-chips-input--error-hover {
  color: #616161;
}
.ds-table-chips-input--disable {
  color: #9e9e9e;
}
```
</details>

#### Table content cell `[52954:1253]` — 8 вариантов
**Описание и рекомендации по применению:**
Ячейка таблицы — одно значение в строке данных: название товара, количество, цена, ссылка на документ.  
Выравнивание берите по типу данных: текст влево, числа вправо. Пустое значение показывайте прочерком, а не пустотой.  

Состояния: Default, Null (нет значения), Link, Hover, Focus, Edit (правка значения), Error, Disable.
- **State** (VARIANT): Default, Disable, Edit, Error, Focus, Hover, Link, Null
- Размеры и параметры:
    - высота: минимум `var(--ds-size-9x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px)`
    - промежуток между элементами: `var(--ds-size-2x)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-table-content-cell ds-table-content-cell--disabled">
  <div class="ds-table-content-cell__element"></div>
  <span class="ds-table-content-cell__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-table-content-cell__label">Текст</span>
  <div class="ds-table-content-cell__text-ui"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-table-content-cell {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-content-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-table-content-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-table-content-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-table-content-cell__icon svg path {
  fill: currentColor;
}
.ds-table-content-cell__element {
  display: flex;
  flex-direction: row;
}
.ds-table-content-cell__text-ui {
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
}
.ds-table-content-cell:disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-cell.ds-table-content-cell--disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-cell:hover {
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-table-content-cell--disabled {
  pointer-events: none;
}
```
</details>

#### Table content row `[60105:56764]` — 5 вариантов
**Описание и рекомендации по применению:**
Строка таблицы — набор ячеек одной записи: позиция накладной, товар, документ.  
Выделение строки используйте для действий над записью; чередование фона включайте только в длинных таблицах.  

Состояния: Default, Zebra (чередование фона), Hover, Selected, Disable.
- **State** (VARIANT): Default, Disable, Hover, Selected, Zebra
- Прочие свойства: Content#60036:0 (SLOT)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-9x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - рамка: `1px solid var(--ds-color-stroke-default, #e0e0e0)`
    - фон: `var(--ds-color-table-row-content-default-background, #ffffff)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-table-content-row ds-table-content-row--disabled">
  <span class="ds-table-content-row__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-table-content-row {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  background: var(--ds-color-table-row-content-default-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-content-row__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-table-content-row:disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-row.ds-table-content-row--disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-row:hover {
  background: var(--ds-color-table-row-content-hover-background, #f5f5f5);
}
.ds-table-content-row--disabled {
  pointer-events: none;
}
```
</details>

#### Table footer `[59207:20759]` — 1 вариантов
**Описание и рекомендации по применению:**
Подвал таблицы — итоги по колонкам и постраничная навигация.  
Итоги показывайте по тем же колонкам, что и в строках; если итогов нет — подвал не добавляйте.
- **Type** (VARIANT): Default
- Прочие свойства: Slot Content#59249:0 (SLOT)
- Размеры и параметры:
    - высота: `65px` (фикс.)
    - ширина: `980px` (фикс.)
    - фон: `var(--ds-color-table-footer-background, #ffffff)`
    - тень: `var(--ds-shadow-shadows-01-dp-sl)`
- Модификаторы (что меняет каждый):
    - `--default`: color `var(--ds-color-expansion-panel-content-text-color, #333333)`
- Разметка:

```html
<div class="ds-table-footer ds-table-footer--default">
  <div class="ds-table-footer__content"></div>
  <div class="ds-table-footer__divider"></div>
  <span class="ds-table-footer__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-table-footer {
  height: 65px;
  width: 980px;
  display: flex;
  flex-direction: column;
  background: var(--ds-color-table-footer-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-footer__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
  white-space: nowrap;
}
.ds-table-footer__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-table-footer__content {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-table-footer-pad-top, 12px) var(--ds-table-footer-pad-right, 32px) var(--ds-table-footer-pad-bottom, 12px) var(--ds-table-footer-pad-left, 32px);
  background: #ffffff;
}
.ds-table-footer--default {
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
}
```
</details>

#### Table header cell `[60098:45424]` — 3 вариантов
**Описание и рекомендации по применению:**
Ячейка шапки таблицы — название колонки и сортировка по ней.  
Название колонки пишите коротко, единицы измерения выносите в название, а не в каждую ячейку.  

Состояния: Default, Hover, Disable (сортировка недоступна).
- **State** (VARIANT): Default, Disable, Hover
- Размеры и параметры:
    - высота: минимум `var(--ds-size-9x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px)`
    - промежуток между элементами: `var(--ds-size-2x)`
    - рамка: `1px solid var(--ds-color-stroke-default, #e0e0e0)`
    - фон: `var(--ds-color-table-cell-header-default-background, #f0f5ff)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:disabled` (неактивно), `:hover` (наведение)
- Разметка:

```html
<div class="ds-table-header-cell ds-table-header-cell--disabled">
  <div class="ds-table-header-cell__element"></div>
  <span class="ds-table-header-cell__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-table-header-cell__label">Текст</span>
  <div class="ds-table-header-cell__text-ui"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-table-header-cell {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  background: var(--ds-color-table-cell-header-default-background, #f0f5ff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-header-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-table-header-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-table-header-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-table-header-cell__icon svg path {
  fill: currentColor;
}
.ds-table-header-cell__element {
  display: flex;
  flex-direction: row;
}
.ds-table-header-cell__text-ui {
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
}
.ds-table-header-cell:hover {
  background: var(--ds-color-table-cell-header-hover-background, #f8f9fc);
}
.ds-table-header-cell:disabled {
  background: var(--ds-color-table-cell-header-disable-background, #f0f5ff);
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-header-cell.ds-table-header-cell--disabled {
  background: var(--ds-color-table-cell-header-disable-background, #f0f5ff);
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-header-cell--disabled {
  pointer-events: none;
}
```
</details>

#### Table header row `[53556:3571]` — 1 вариантов
**Описание и рекомендации по применению:**
Шапка таблицы — строка с названиями колонок, закреплена при прокрутке.  
Собирается из ячеек Table header cell; порядок колонок должен совпадать с порядком в строках данных.
- **State** (VARIANT): Default
- Прочие свойства: Header#59320:28 (SLOT)
- Размеры и параметры:
    - высота: минимум `var(--ds-size-9x)`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - скругление: `var(--ds-table-row-header-border-radius-top-left)`
    - рамка: `1px solid var(--ds-color-stroke-default, #e0e0e0)`
    - фон: `var(--ds-color-table-row-header-background-header, #f0f5ff)`
- Разметка:

```html
<div class="ds-table-header-row">
  <span class="ds-table-header-row__label">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-table-header-row {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-table-row-header-border-radius-top-left);
  background: var(--ds-color-table-row-header-background-header, #f0f5ff);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-header-row__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
```
</details>

#### Tabs `[54854:3052]` — 4 вариантов
**Описание и рекомендации по применению:**
Вкладки — переключение разделов одного экрана без перезагрузки: «Общие», «Товары», «История».  
Берите их, когда разделов 2–7 и они равнозначны; для вложенной навигации — второй уровень вкладок.  
Активная вкладка подчёркнута; названия пишите коротко, без многоточий.  

Состав: строка вкладок из Tab element, при нехватке места — стрелки прокрутки (Scroll tabs).  

Как выбрать вариант:  
Lvl=1 — основные разделы экрана; Lvl=2 — вложенные разделы внутри раздела.  
Content=Text — с текстом; Icon — только иконки, когда раздел понятен по иконке.
- **Lvl** (VARIANT): 1, 2
- **Content** (VARIANT): Icon, Text
- Прочие свойства: Content text m#58420:0 (SLOT), Content icon m#58420:5 (SLOT), Content text s#58420:10 (SLOT), Content icon s#58420:15 (SLOT), Scroll left#59422:17 (BOOLEAN), Scroll right#59422:22 (BOOLEAN)
- CSS: выверено вручную, см. `components/index.css` в разделе «Полные CSS-стили всех компонентов»

#### Text UI `[57938:18290]` — 7 вариантов
**Описание и рекомендации по применению:**
Текст интерфейса — подпись, значение или ссылка в ячейках, списках и карточках.  
Берите его, чтобы текст в однотипных местах совпадал по размеру и цвету; заголовки страниц и блоков набирайте стилями типографики.  
Лежит на странице UI components (раздел «не готовы или под вопросом») — перед использованием уточните актуальность у владельца ДС.  

Состояния: Default, Link, Hover, Press, Selected, Negative, Disable.
- **State** (VARIANT): Default, Disable, Hover, Link, Negative, Press, Selected
- Прочие свойства: Element left#54167:1 (BOOLEAN), Element right#54167:6 (BOOLEAN), Label up#54741:15 (BOOLEAN), Label down#54741:30 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `52px`, растёт по контенту
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-list-item-gap, 8px)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
- Состояния: `:disabled` (неактивно)
- Разметка:

```html
<div class="ds-text-ui ds-text-ui--disabled">
  <div class="ds-text-ui__checkbox"></div>
  <div class="ds-text-ui__content"></div>
  <span class="ds-text-ui__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-text-ui__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-text-ui__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-text-ui__icon-size"></div>
  <span class="ds-text-ui__label">Текст</span>
  <div class="ds-text-ui__label-down"></div>
  <div class="ds-text-ui__label-up"></div>
  <div class="ds-text-ui__list-item"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-text-ui {
  min-height: 52px;
  width: fit-content;
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-text-ui__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-text-ui__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-text-ui__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-text-ui__icon svg path {
  fill: currentColor;
}
.ds-text-ui__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-text-ui__checkbox {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-text-ui__content {
  display: flex;
  flex-direction: column;
}
.ds-text-ui__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-ui-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-text-ui-text-label-color, #616161);
}
.ds-text-ui__list-item {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-ui-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
}
.ds-text-ui__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-ui-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-text-ui-text-label-color, #616161);
}
.ds-text-ui__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-text-ui__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-text-ui:disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-text-ui.ds-text-ui--disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-text-ui--disabled {
  pointer-events: none;
}
```
</details>

#### Textarea `[57916:9023]` — 13 вариантов
**Описание и рекомендации по применению:**
Многострочное поле — длинный текст: комментарий к заказу, примечание к накладной, описание позиции.  
Берите его, когда ответ не помещается в одну строку; для короткого значения используйте Input.  

Состав: Label над полем, само поле с прокруткой, support-текст под полем (подсказка или ошибка).  
Высоту задавайте под ожидаемый текст, растягивать вручную не нужно.  

Как выбрать вариант:  
Variant=Empty — поле без текста; Populated — с введённым текстом.  
Состояния: Default, Hover, Focus, Focus+Placeholder, Focus+Value, Error, Error+Hover, Disable.
- **Size** (VARIANT): M
- **Variant** (VARIANT): Empty, Populated
- **State** (VARIANT): Default, Disable, Error, Error+Hover, Focus, Focus+Placeholder, Focus+Value, Hover
- Прочие свойства: Input text#52678:0 (TEXT), Label text#52678:3 (TEXT), Support text#52678:6 (TEXT), Label#56934:32 (BOOLEAN), Element left#56934:282 (BOOLEAN), Element right#56934:407 (BOOLEAN), Support text#56934:532 (BOOLEAN), Input text#56968:66 (BOOLEAN), Hint text#57893:0 (BOOLEAN), Support#57893:30 (BOOLEAN), Hint text#57893:60 (TEXT), Scroll#57994:0 (BOOLEAN)
- Размеры и параметры:
    - высота: минимум `96px`, растёт по контенту
    - ширина: `250px` (фикс.)
    - промежуток между элементами: `var(--ds-form-field-gap-input-support, 4px)`
- Модификаторы (что меняет каждый):
    - `--disabled`: pointer-events `none`
    - `--empty`: color `var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e)`, color `var(--ds-color-form-field-input-label-text-color, #616161)`
    - `--populated`: color `var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e)`, color `var(--ds-color-form-field-filled-default-label-text-color, #616161)`
- Состояния: `:disabled` (неактивно), `:focus-visible`, `:hover` (наведение)
- Разметка:

```html
<div class="ds-textarea ds-textarea--disabled">
  <span class="ds-textarea__element-left"><!-- иконка: material-icons по имени --></span>
  <span class="ds-textarea__element-right"><!-- иконка: material-icons по имени --></span>
  <span class="ds-textarea__hint">Текст</span>
  <span class="ds-textarea__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-textarea__input-content"></div>
  <div class="ds-textarea__input-frame"></div>
  <span class="ds-textarea__label">Текст</span>
  <div class="ds-textarea__scroll"></div>
  <span class="ds-textarea__support">Текст</span>
  <span class="ds-textarea__text">Текст</span>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-textarea {
  min-height: 96px;
  width: 250px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-textarea__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-textarea__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-textarea__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-textarea__icon svg path {
  fill: currentColor;
}
.ds-textarea__input-frame {
  height: 76px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-pad-textarea-top, 4px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-textarea__element-left {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-textarea__input-content {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-content);
}
.ds-textarea__element-right {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-textarea__scroll {
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-textarea__support {
  display: flex;
  flex-direction: row;
}
.ds-textarea__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-textarea__hint {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-textarea--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-textarea--populated.ds-textarea--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-textarea--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-textarea--empty.ds-textarea--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-textarea--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-textarea--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-textarea--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-textarea--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-textarea--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-textarea--disabled {
  pointer-events: none;
}
```
</details>

#### Timepicker `[58982:9858]` — 2 вариантов
**Описание и рекомендации по применению:**
Выбор времени — список или сетка часов и минут: время доставки, начало смены.  
Открывается из поля времени (Input Timepicker); отдельно на экране не живёт.  

Как выбрать вариант:  
Type=Time line — список времени одной колонкой, прокруткой.  
Type=Time grid — сетка значений, когда нужен быстрый выбор круглых значений.
- **Type** (VARIANT): Time grid, Time line
- Прочие свойства: Slot Time#58983:4 (SLOT), Control Panel#58983:7 (SLOT), Scroll#58983:10 (BOOLEAN)
- Размеры и параметры:
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `var(--ds-size-2x) 0 var(--ds-size-2x) 0`
    - скругление: `var(--ds-size-3x)`
    - рамка: `1px solid var(--ds-color-stroke-default, #e0e0e0)`
    - фон: `var(--ds-color-brand-neutral-default, #ffffff)`
    - тень: `var(--ds-shadow-shadows-08-dp-s)`
- Модификаторы (что меняет каждый):
    - `--time-grid`: направление `column`, align-items `center`, color `var(--ds-color-text-primary, #333333)`
    - `--time-line`: направление `row`, color `var(--ds-color-text-primary, #333333)`
- Разметка:

```html
<div class="ds-timepicker ds-timepicker--time-grid">
  <div class="ds-timepicker__control-panel"></div>
  <span class="ds-timepicker__icon"><!-- иконка: material-icons по имени --></span>
  <span class="ds-timepicker__label">Текст</span>
  <div class="ds-timepicker__scroll"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-timepicker {
  width: fit-content;
  display: flex;
  padding: var(--ds-size-2x) 0 var(--ds-size-2x) 0;
  border-radius: var(--ds-size-3x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-timepicker__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-timepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-timepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-timepicker__icon svg path {
  fill: currentColor;
}
.ds-timepicker__control-panel {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-timepicker__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-timepicker--time-grid {
  flex-direction: column;
  align-items: center;
  color: var(--ds-color-text-primary, #333333);
}
.ds-timepicker--time-line {
  flex-direction: row;
  color: var(--ds-color-text-primary, #333333);
}
```
</details>

#### Tree `[59564:1473]` — 8 вариантов
**Описание и рекомендации по применению:**
Дерево — иерархический список с раскрытием: группы товаров, склады, оргструктура.  
Берите его, когда у записей есть вложенность; для плоского перечня используйте List.  

Как выбрать вариант:  
Level — уровень вложенности ветки.  
Mode=Middle — ветка в середине уровня; End — последняя ветка уровня.  
For icon=On — с местом под иконку у ветки; Off — без него.
- **Level** (VARIANT): 2, 3
- **Mode** (VARIANT): End, Middle
- **For icon** (VARIANT): Off, On
- Размеры и параметры:
    - высота: `44px` (фикс.)
    - ширина: `fit-content` (фикс.)
    - промежуток между элементами: `var(--ds-size-2-5x)`
- Модификаторы (что меняет каждый):
    - `--2`: направление `row`, направление `column`, align-items `center`
    - `--3`: направление `row`, align-items `center`
- Разметка:

```html
<div class="ds-tree ds-tree--2">
  <span class="ds-tree__icon"><!-- иконка: material-icons по имени --></span>
  <div class="ds-tree__item"></div>
  <div class="ds-tree__separator-stroke"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-tree {
  height: 44px;
  width: fit-content;
  display: flex;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-tree__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-tree__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-tree__icon svg path {
  fill: currentColor;
}
.ds-tree__item {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: 0 0 var(--ds-size-5x) 11px;
}
.ds-tree__separator-stroke {
  height: 100%;
  display: flex;
  flex-direction: row;
  background: #d7d8d9;
}
.ds-tree--2.ds-tree--end.ds-tree--on {
  flex-direction: row;
}
.ds-tree--2.ds-tree--end.ds-tree--off {
  flex-direction: column;
}
.ds-tree--3.ds-tree--end.ds-tree--on {
  flex-direction: row;
}
.ds-tree--3.ds-tree--end.ds-tree--off {
  flex-direction: row;
}
.ds-tree--2.ds-tree--middle.ds-tree--on {
  flex-direction: row;
  align-items: center;
}
.ds-tree--2.ds-tree--middle.ds-tree--off {
  flex-direction: row;
  align-items: center;
}
.ds-tree--3.ds-tree--middle.ds-tree--on {
  flex-direction: row;
  align-items: center;
}
.ds-tree--3.ds-tree--middle.ds-tree--off {
  flex-direction: row;
  align-items: center;
}
```
</details>

#### Tree item `[59564:1504]` — 5 вариантов
**Описание и рекомендации по применению:**
Линия связи в дереве — соединяет ветку с родителем и показывает, продолжается ли уровень.  
Служебный элемент дерева: ставится внутрь ветки, отдельно на экран не выносится.  

Как выбрать вариант: по месту ветки в уровне и длине связи.
- **Mode** (VARIANT): End, End-long, Middle, Middle-long, Start
- Размеры и параметры:
    - высота: `44px` (фикс.)
    - ширина: `fit-content` (фикс.)
    - внутренние отступы: `0 0 var(--ds-size-5x) 11px`
    - промежуток между элементами: `var(--ds-size-2-5x)`
- Модификаторы (что меняет каждый):
    - `--end`: направление `row`, align-items `center`, ширина `48px`, направление `column`
    - `--end-long`: ширина `48px`, направление `column`, внутренние отступы `0 0 21px 11px`
    - `--middle`: направление `row`, align-items `center`, внутренние отступы `0 0 0 11px`, ширина `48px`
    - `--middle-long`: ширина `48px`, направление `row`, align-items `center`, внутренние отступы `0 0 0 11px`
    - `--start`: ширина `var(--ds-size-6x)`, направление `row`, align-items `center`, внутренние отступы `0 var(--ds-size-3x) 0 11px`
- Разметка:

```html
<div class="ds-tree-item ds-tree-item--end">
  <div class="ds-tree-item__separator-stroke"></div>
</div>
```
<details><summary>CSS компонента</summary>

```css

.ds-tree-item {
  height: 44px;
  display: flex;
  width: fit-content;
  padding: 0 0 var(--ds-size-5x) 11px;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-tree-item__separator-stroke {
  height: 100%;
  display: flex;
  flex-direction: row;
  background: #d7d8d9;
}
.ds-tree-item--end {
  flex-direction: row;
  align-items: center;
}
.ds-tree-item--end-long {
  width: 48px;
  flex-direction: column;
  padding: 0 0 21px 11px;
}
.ds-tree-item--middle {
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 11px;
}
.ds-tree-item--middle-long {
  width: 48px;
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 11px;
}
.ds-tree-item--start {
  width: var(--ds-size-6x);
  flex-direction: row;
  align-items: center;
  padding: 0 var(--ds-size-3x) 0 11px;
}
```
</details>

### Карта классов CSS-библиотеки

Готовые стили для **всех компонентов** ДС лежат в `components/index.css` (сгенерировано из Figma, все значения — токены). Паттерн: контейнер `.ds-<компонент>` + модификаторы вариантов `--<значение>` + элементы `__label` / `__icon`.

**✓ выверено по узлам Figma вручную** (размеры, шрифты, состояния сняты поштучно): Button, Input, Checkbox, Radio button, Badge, Tabs (Lvl 1/2), Divider, Banners, Card view (+header/content/footer), Expansion panel (+content), Stepper (+Step), Slide toggle. Остальные — сгенерированы автоматически: цвета/размеры/радиусы на токенах верные, структура упрощённая (при первом использовании стоит сверить с макетом).

**Весь нужный CSS уже в этом файле** — ничего скачивать не нужно. Если собираете прототип в отдельной странице на GitHub Pages, подключите CSS по прямой ссылке (или возьмите из раздела «Полные CSS-стили всех компонентов»):\n
```html
<link rel="stylesheet" href="https://anders7rusk.github.io/iiko-ds-web/tokens.css">
<link rel="stylesheet" href="https://anders7rusk.github.io/iiko-ds-web/components/Button_DS/button.css">
<link rel="stylesheet" href="https://anders7rusk.github.io/iiko-ds-web/components/Form-Field-Input_DS/input.css">
<link rel="stylesheet" href="https://anders7rusk.github.io/iiko-ds-web/components/index.css">
```

| Компонент | Класс | Модификаторы |
|---|---|---|
| Arrow | `.ds-arrow` |
| Arrow list | `.ds-arrow-list` |
| Arrow menu | `.ds-arrow-menu` |
| Arrow select | `.ds-arrow-select` |
| Autocomplete form | `.ds-autocomplete-form` · `--empty` `--populated` `--empty` `--populated` `--populated` `--empty` `--empty` `--populated` `--populated` `--disabled` · :disabled, :focus, :hover |
| Backdrop | `.ds-backdrop` |
| Button toggle | `.ds-button-toggle` · `--s` `--xs` `--filled` `--outlined` `--outlined` `--filled` |
| Checkbox label | `.ds-checkbox-label` · `--normal` `--normal` `--normal` `--error` `--error` `--error` `--disable` `--disable` `--disable` |
| Chips | `.ds-chips` · `--s` `--s` `--outlined` `--outlined` `--outlined` `--outlined` `--outlined` `--outlined` `--filled` `--filled` `--filled` `--filled` `--filled` `--disabled` · :active, :disabled, :focus, :hover |
| Chips group | `.ds-chips-group` · `--s` |
| Chips Input | `.ds-chips-input` · `--s` `--s` `--disabled` · :disabled, :focus, :hover |
| Chips Input | `.ds-chips-input-2` · `--s` `--disabled` · :disabled, :focus, :hover |
| Chips input cell | `.ds-chips-input-cell` · `--disabled` · :disabled, :focus, :hover |
| Control arrow button | `.ds-control-arrow-button` · `--s` |
| Control Panel | `.ds-control-panel` · `--control` `--week` `--calendar` |
| Control Panel | `.ds-control-panel-2` · `--control` `--time` |
| Datepicker | `.ds-datepicker` · `--day` `--year` `--month` |
| Dialog content | `.ds-dialog-content` |
| Dialog footer | `.ds-dialog-footer` |
| Dialog header | `.ds-dialog-header` · `--text` |
| Dialog view | `.ds-dialog-view` |
| Element | `.ds-element` · `--image-size` `--icon-size` `--icon-group` `--text-default` `--checkbox` `--radio-button` `--indicator` `--slide-toggle` `--counter` |
| Element cell | `.ds-element-cell` · `--icon-size` `--icon-group` `--button` `--button-icon` `--status` `--text-ui` `--input-number` `--checkbox` `--slide-toggle` `--chips` `--cell-input` |
| Element Form Field | `.ds-element-form-field` · `--input-cell` `--select-cell` `--chips-input-cell` |
| Element left | `.ds-element-left` |
| Element menu | `.ds-element-menu` · `--image-size` `--icon-size` `--text-default` `--checkbox` `--radio-button` `--indicator` `--slide-toggle` `--counter` |
| Element select | `.ds-element-select` · `--image-size` `--icon-size` `--text-default` `--checkbox` `--radio-button` `--indicator` `--slide-toggle` `--counter` |
| Element sidenav | `.ds-element-sidenav` · `--collaps-icon` `--avatar` |
| Element step | `.ds-element-step` · `--icon-size` `--counter` `--counter` `--counter` `--counter` `--counter` `--disabled` · :active, :disabled, :hover |
| Elementare cell | `.ds-elementare-cell` · `--icon-size` `--icon-group` `--button` `--button-icon` `--status` `--text-ui` `--input-number` `--checkbox` `--slide-toggle` `--chips` |
| Elements | `.ds-elements` · `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--cell` `--year` `--cell` `--cell` `--year` `--year` `--year` `--year` `--year` `--year` `--year` `--year` `--year` `--year` `--month` `--month` `--month` `--month` `--month` `--disabled` · :active, :disabled, :hover |
| Elements | `.ds-elements-2` · `--selected` `--default` `--default` `--default` `--default` `--default` `--disabled` · :active, :disabled, :hover |
| Expansion content | `.ds-expansion-content` · `--true` `--false` |
| Expansion group panel | `.ds-expansion-group-panel` · `--collaps` `--expand` |
| Form field cell | `.ds-form-field-cell` |
| Hint container | `.ds-hint-container` · `--up` `--down` `--right` `--left` `--default` |
| Hint content | `.ds-hint-content` · `--group-content` `--single-content` |
| Hint footer | `.ds-hint-footer` · `--default` |
| Hint header | `.ds-hint-header` · `--neutral` `--primary` `--secondary` `--warning` `--error` |
| Icon group | `.ds-icon-group` · `--4x` |
| Input cell | `.ds-input-cell` · `--disabled` · :disabled, :focus, :hover |
| Input Datepicker | `.ds-input-datepicker` · `--empty` `--populated` |
| Input number | `.ds-input-number` · `--s` `--xs` `--xs` `--populated` `--empty` `--populated` `--populated` `--empty` `--populated` `--populated` `--empty` `--empty` `--disabled` · :disabled, :focus, :hover |
| Input number_but icon | `.ds-input-number-but-icon` |
| Input Timepicker | `.ds-input-timepicker` · `--empty` `--populated` |
| List (Сontainer) | `.ds-list-container` · `--container` |
| List item | `.ds-list-item` · `--disabled` · :active, :disabled, :hover |
| Logo iiko | `.ds-logo-iiko` |
| Logo Syrve | `.ds-logo-syrve` |
| Menu (Container) | `.ds-menu-container` · `--container` |
| Menu item | `.ds-menu-item` · `--disabled` · :active, :disabled, :hover |
| Picture | `.ds-picture` |
| Radio button label | `.ds-radio-button-label` · `--normal` `--normal` `--error` `--error` `--disable` `--disable` |
| Scroll | `.ds-scroll` · `--s` `--first` `--middle` `--middle` `--last` · :hover |
| Scroll tabs | `.ds-scroll-tabs` · `--left` |
| Search | `.ds-search` · `--s` `--s` `--xs` `--xs` `--disabled` · :disabled, :focus, :hover |
| Select (Сontainer) | `.ds-select-container` · `--container` |
| Select cell | `.ds-select-cell` · `--disabled` · :disabled, :focus, :hover |
| Select form | `.ds-select-form` · `--s` `--xs` `--empty` `--populated` `--empty` `--populated` `--populated` `--empty` `--empty` `--populated` `--populated` `--disabled` · :disabled, :focus, :hover |
| Select item | `.ds-select-item` · `--true` `--false` `--false` `--false` `--false` `--false` `--disabled` · :active, :disabled, :hover |
| Sidenav control | `.ds-sidenav-control` · `--collapsed` `--collapsed` `--expanded` `--expanded` `--expanded` `--collapsed` · :active, :hover |
| Sidenav Footer | `.ds-sidenav-footer` · `--l2` `--l1` `--l1` |
| Sidenav header | `.ds-sidenav-header` · `--l1` `--l2` `--l1` |
| Sidenav item | `.ds-sidenav-item` · `--l3` `--l3` `--l2` `--l2` `--l1` `--l1` `--l1` `--l1` · :hover |
| Sidenav View | `.ds-sidenav-view` |
| Snackbar | `.ds-snackbar` · `--single` `--single` `--complex` `--complex` |
| State | `.ds-state` · :active, :hover |
| Status | `.ds-status` · `--neutral` `--accent` `--positive` `--warning` `--negative` `--contrast-1` `--contrast-2` `--contrast-3` `--contrast-4` `--neutral` `--accent` `--positive` `--warning` `--negative` `--contrast-1` `--contrast-2` `--contrast-3` `--contrast-4` |
| Table 2 lvl | `.ds-table-2-lvl` · `--table-cell-2-lvl` `--table-row-2-lvl` |
| Table Chips Input | `.ds-table-chips-input` · `--default` `--hover` `--focus` `--focus-placeholder` `--vocus-value` `--error` `--error-hover` `--disable` |
| Table content cell | `.ds-table-content-cell` · `--disabled` · :disabled, :hover |
| Table content row | `.ds-table-content-row` · `--disabled` · :disabled, :hover |
| Table footer | `.ds-table-footer` · `--default` |
| Table header cell | `.ds-table-header-cell` · `--disabled` · :disabled, :hover |
| Table header row | `.ds-table-header-row` |
| Text UI | `.ds-text-ui` · `--disabled` · :disabled |
| Textarea | `.ds-textarea` · `--populated` `--populated` `--empty` `--empty` `--populated` `--populated` `--empty` `--populated` `--empty` `--disabled` · :disabled, :focus, :hover |
| Timepicker | `.ds-timepicker` · `--time-grid` `--time-line` |
| Tree | `.ds-tree` · `--2` `--2` `--3` `--3` `--2` `--2` `--3` `--3` |
| Tree item | `.ds-tree-item` · `--end` `--end-long` `--middle` `--middle-long` `--start` |

#### Ручные (выверенные по Figma) файлы — их классы

Эти компоненты сняты с узлов Figma поштучно и живут в отдельных файлах (`button, input, selection, selection-icons, badge, navigation, card, expansion, stepper, toggle`). Имена классов КОРОЧЕ имени компонента в Figma — писать в разметке именно их.

| Класс | Модификаторы | Элементы |
|---|---|---|
| `.ds-btn` | `--accent` `--disabled` `--filled` `--m` `--negative` `--neutral` `--outlined` `--positive` `--s` `--text` `--warning` `--xs` | `__icon` `__label` |
| `.ds-btn-group` | `--horizontal` `--margins` `--vertical` | — |
| `.ds-btn-icon` | `--accent` `--disabled` `--m` `--negative` `--neutral` `--outlined` `--positive` `--s` `--text` `--warning` `--xs` | `__icon` |
| `.ds-btn-icon-group` | `--vertically` | — |
| `.ds-input` | `--disabled` `--error` `--m` `--s` `--xs` | `__content` `__field` `__frame` `__hint` `__icon` `__label` `__stepper` `__support` `__support-row` |
| `.ds-checkbox` | `--disabled` `--error` | `__box` `__input` `__label` `__support` |
| `.ds-radio` | `--disabled` `--error` | `__box` `__input` `__label` `__state` `__support` |
| `.ds-checkbox-wrap` | — | — |
| `.ds-checkbox-group` | `--horizontal` `--vertical` | — |
| `.ds-radio-group` | `--horizontal` `--vertical` | — |
| `.ds-badge` | `--accent` `--counter` `--negative` `--point` `--positive` `--warning` | — |
| `.ds-tabs` | `--lvl2` | — |
| `.ds-tab` | `--active` `--disabled` | `__counter` `__icon` |
| `.ds-divider` | `--dashed` `--disable` `--l` `--lite` `--m` `--selected` | — |
| `.ds-divider-line` | `--dashed` `--disable` `--lite` `--selected` | — |
| `.ds-banner` | `--accent` `--horizontal` `--negative` `--neutral` `--positive` `--vertical` `--warning` | `__buttons` `__icon` `__row` `__text` |
| `.ds-field-label` | — | — |
| `.ds-card` | `--custom` `--filled` `--outlined` `--shadow` | `__content` `__divider` `__footer` `__footer--right` `__footer__action` `__header` `__label-down` `__label-up` `__title` |
| `.ds-expansion` | `--disabled` `--info` `--open` | `__actions` `__arrow` `__content` `__content--no-padding` `__header` `__icon` `__title` |
| `.ds-stepper` | — | `__divider` |
| `.ds-step` | `--bg` `--disabled` `--error` `--selected` | `__icon` `__num` |
| `.ds-stepper-button` | — | `__counter` `__group` |
| `.ds-slide-toggle` | `--disabled` `--error` | `__icon` `__input` `__row` `__support` `__title` `__track` |

### Иконки (Google Material Icons)

Иконки — **Google Material Icons**, вставляются **по имени** (а не SVG-кодом), поэтому разметка компактная, а иконки одинаковые у всех прототипов. Пришли из файла иконок ДС (Figma `skjpVJUl8ir0JazrrPAMOW`), имена совпадают с набором Google Material.

**Подключение** (один раз в `<head>` прототипа):
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
```

**Вставка по имени**, цвет наследуется от текста (`currentColor`):
```html
<span class="material-icons">add</span>
```
Иконку вставляйте туда, где ей место: внутрь `.ds-btn__icon` / `.ds-btn-icon__icon` / `.ds-input__icon`.

Иконки берём **любые из Google Material Icons** — обязательного списка имён нет.
Каталог с именами (отсюда подставляем имя): https://fonts.google.com/icons
Как устроены иконки в Material: https://m3.material.io/styles/icons/overview

Имена в файле иконок ДС совпадают с Google Material (например `schedule_time` → `schedule`, `arrow_left/right` → `arrow_back/forward`) — подбираем подходящее имя из каталога. Размер иконки — как у иконочного слота компонента: обычно 20 px (`Icon size/Size 5x`); где слот задаёт 16 (например Button icon XS) — оставляем 16 по токену компонента.

### Бренд-иконка iiko (SVG, не Material)

Логотип iiko — **не Material**, вставляется SVG-кодом (цвет `currentColor`):

```html
<svg width="20" height="20" viewBox="0 0 169 72" fill="none" xmlns="http://www.w3.org/2000/svg"> <g clip-path="url(#clip0_55332_22289)"> <path d="M142.121 27.4503C125.935 27.4503 115.721 35.7723 115.721 49.5734C115.721 63.3744 125.935 71.6712 142.121 71.6712C158.308 71.6712 168.521 63.3491 168.521 49.5734C168.521 35.7976 158.282 27.4503 142.121 27.4503ZM142.121 59.5548C137.728 59.5548 137.626 53.9089 137.626 49.5734C137.626 45.2378 137.723 39.5666 142.121 39.5666C146.519 39.5666 146.58 45.2125 146.58 49.5734C146.58 53.9342 146.514 59.5548 142.121 59.5548Z" fill="currentColor"/> <path d="M20.0802 28.4165H1.73282C1.14173 28.4165 0.662552 28.8922 0.662552 29.4789V69.6324C0.662552 70.2191 1.14173 70.6948 1.73282 70.6948H20.0802C20.6713 70.6948 21.1505 70.2191 21.1505 69.6324V29.4789C21.1505 28.8922 20.6713 28.4165 20.0802 28.4165Z" fill="currentColor"/> <path d="M20.0802 9.87015H1.73282C1.14173 9.87015 0.662552 10.3458 0.662552 10.9325V22.9325C0.662552 23.5193 1.14173 23.9949 1.73282 23.9949H20.0802C20.6713 23.9949 21.1505 23.5193 21.1505 22.9325V10.9325C21.1505 10.3458 20.6713 9.87015 20.0802 9.87015Z" fill="currentColor"/> <path d="M48.6869 28.4165H30.3395C29.7484 28.4165 29.2692 28.8922 29.2692 29.4789V69.6324C29.2692 70.2191 29.7484 70.6948 30.3395 70.6948H48.6869C49.278 70.6948 49.7571 70.2191 49.7571 69.6324V29.4789C49.7571 28.8922 49.278 28.4165 48.6869 28.4165Z" fill="currentColor"/> <path d="M48.6869 9.87015H30.3395C29.7484 9.87015 29.2692 10.3458 29.2692 10.9325V22.9325C29.2692 23.5193 29.7484 23.9949 30.3395 23.9949H48.6869C49.278 23.9949 49.7571 23.5193 49.7571 22.9325V10.9325C49.7571 10.3458 49.278 9.87015 48.6869 9.87015Z" fill="currentColor"/> <path d="M99.6825 48.0506C99.3002 47.4536 99.341 46.6897 99.7691 46.1282L111.338 31.1332C112.199 30.0253 111.394 28.4216 109.988 28.4216H91.1815C90.626 28.4216 90.096 28.6948 89.7851 29.1551L78.69 45.2175H78.3434V11.5599C78.3434 10.629 77.584 9.87521 76.6463 9.87521H59.5832C58.6454 9.87521 57.8861 10.629 57.8861 11.5599V69.0051C57.8861 69.9359 58.6454 70.6897 59.5832 70.6897H76.6463C77.584 70.6897 78.3434 69.9359 78.3434 69.0051V50.2007H78.69L89.6475 69.8246C89.9431 70.3609 90.519 70.6897 91.1356 70.6897H110.925C112.256 70.6897 113.071 69.2277 112.363 68.1045L99.6723 48.0455H99.6774L99.6825 48.0506Z" fill="currentColor"/> <path d="M133.595 11.2766C134.456 12.4098 135.618 13.2293 136.668 14.1956C137.876 15.3288 139.134 16.8364 139.038 18.5565C138.971 19.3457 138.691 20.0337 138.243 20.6863C137.636 21.597 136.933 22.371 136.184 23.1096C135.46 23.8128 135.48 24.9815 136.224 25.6644H136.209L137.31 26.6813C138.003 27.3187 139.094 27.3035 139.766 26.6408C140.169 26.2412 140.567 25.8213 140.944 25.4014C141.015 25.4975 141.097 25.5936 141.193 25.6745H141.188L142.305 26.6863C143.008 27.3238 144.088 27.2985 144.761 26.6358C145.164 26.2361 145.561 25.8263 145.938 25.4064C146.005 25.5025 146.081 25.5936 146.173 25.6695H146.168L147.258 26.6712C147.962 27.3086 149.042 27.2884 149.725 26.6206C150.388 25.968 151.035 25.3002 151.611 24.5818C152.182 23.8584 152.589 22.973 152.849 22.1332C153.068 21.511 153.043 20.7572 152.977 20.0944C152.91 19.5329 152.661 18.8752 152.375 18.3693C151.774 17.2361 150.79 16.2041 149.847 15.3187C148.522 14.0894 147.156 13.1231 146.428 11.3676C146.208 10.8668 146.045 10.2041 146.045 9.67286C146.015 9.01518 146.142 8.44351 146.392 7.85161C146.896 6.59191 147.702 5.63576 148.655 4.79596C149.419 4.10793 149.429 2.90894 148.67 2.20574L147.615 1.21417C146.953 0.596972 145.923 0.576736 145.24 1.15852C144.807 1.52783 144.379 1.91232 143.997 2.35751C143.976 2.37775 143.956 2.41316 143.93 2.43846C143.864 2.35751 143.803 2.27151 143.721 2.19562L142.666 1.20405C142.009 0.586854 140.995 0.566618 140.296 1.13829C139.843 1.51771 139.41 1.90726 139.012 2.35245C138.992 2.37269 138.961 2.4081 138.941 2.43846C138.875 2.35245 138.803 2.27151 138.722 2.19056L137.667 1.199C137.004 0.581795 135.975 0.561559 135.292 1.14335C134.859 1.51265 134.43 1.89714 134.048 2.34233C132.754 3.7538 131.734 5.79259 132.091 7.77572C132.31 9.03542 132.82 10.2243 133.61 11.2563L133.595 11.2664V11.2766ZM141.397 7.86679C141.555 7.4823 141.759 7.12817 141.968 6.78921C141.953 7.12817 141.968 7.46206 142.019 7.80102C142.238 9.06072 142.748 10.2496 143.538 11.2816C144.399 12.4148 145.561 13.2344 146.601 14.2007C147.809 15.3339 149.068 16.8415 148.976 18.5616C148.91 19.3508 148.629 20.0388 148.181 20.6914C148.13 20.7724 148.074 20.8331 148.023 20.914C148.023 20.6358 148.023 20.3626 148.002 20.0944C147.936 19.5329 147.686 18.8752 147.401 18.3693C146.8 17.2361 145.78 16.2041 144.873 15.3187C143.512 14.0894 142.182 13.1231 141.433 11.3676C141.244 10.8668 141.086 10.2041 141.051 9.67286C141.02 9.01518 141.148 8.44351 141.397 7.85161V7.86173V7.86679ZM136.433 7.85667C136.591 7.46206 136.79 7.11299 136.999 6.76392C136.984 7.10793 136.984 7.45195 137.04 7.79596C137.259 9.05566 137.799 10.2445 138.559 11.2766C139.445 12.4098 140.582 13.2293 141.632 14.1956C142.84 15.3288 144.098 16.8364 144.002 18.5565C143.971 19.3457 143.655 20.0337 143.242 20.6863C143.176 20.7723 143.115 20.8533 143.054 20.9444C143.054 20.656 143.038 20.3575 143.013 20.0843C142.947 19.5228 142.697 18.8651 142.412 18.3592C141.81 17.226 140.827 16.1939 139.884 15.3086C138.559 14.0793 137.193 13.113 136.464 11.3575C136.245 10.8567 136.082 10.1939 136.082 9.66274C136.051 9.00507 136.179 8.4334 136.428 7.84149V7.85161L136.433 7.85667Z" fill="currentColor"/> </g> <defs> <clipPath id="clip0_55332_22289"> <rect width="169" height="72" fill="white"/> </clipPath> </defs> </svg>
```
## Полные CSS-стили всех компонентов

Весь CSS дизайн-системы в одном месте: токены задаются через `tokens.css`, стили компонентов — ниже. При сборке прототипа **скопируйте этот CSS в `<style>` своего прототипа** (или сохраните как `components.css` и подключите `<link rel="stylesheet" href="components.css">`).

### Шрифт Roboto — из Google Fonts (онлайн)

Все прототипы работают онлайн — офлайн-подключения шрифта нет. Roboto 400/500 берём из **Google Fonts**:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
```

В прототипах можно и одним файлом ДС: `iiko-ds-web/font.css` — он делает тот же `@import` Google Fonts.

Подключать первым — иначе метрики (14/20, 16/24) поедут на системном шрифте. `font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif`.

### tokens.css (токены)

```css

:root {

  
  --ds-size-0: 0px;   
  --ds-size-0-5x: 2px;   
  --ds-size-1x: 4px;   
  --ds-size-1-5x: 6px;   
  --ds-size-2x: 8px;   
  --ds-size-2-5x: 10px;   
  --ds-size-3x: 12px;   
  --ds-size-3-5x: 14px;   
  --ds-size-4x: 16px;   
  --ds-size-5x: 20px;   
  --ds-size-6x: 24px;   
  --ds-size-7x: 28px;   
  --ds-size-8x: 32px;   
  --ds-size-circular: 9999px;   
  --ds-size-0-25x: 1px;   
  --ds-size-8-5x: 34px;   
  --ds-size-9x: 36px;   
  --ds-size-10x: 40px;   

  
  --ds-palette-neutral-0: #ffffff;   
  --ds-palette-neutral-100: #ebebeb;   
  --ds-palette-neutral-200: #e0e0e0;   
  --ds-palette-neutral-300: #d6d6d6;   
  --ds-palette-neutral-400: #bdbdbd;   
  --ds-palette-neutral-500: #9e9e9e;   
  --ds-palette-neutral-600: #757575;   
  --ds-palette-neutral-700: #616161;   
  --ds-palette-neutral-800: #424242;   
  --ds-palette-neutral-900: #333333;   
  --ds-palette-negative-5: #fbf8f8;   
  --ds-palette-negative-200: #ffcccc;   
  --ds-palette-negative-300: #ffb8b8;   
  --ds-palette-negative-500: #ff5252;   
  --ds-palette-negative-700: #de1a12;   
  --ds-palette-negative-900: #7f0f0a;   
  --ds-palette-warning-5: #fdfcfa;   
  --ds-palette-warning-200: #ffe9cc;   
  --ds-palette-warning-300: #ffd9a8;   
  --ds-palette-warning-500: #ffab40;   
  --ds-palette-warning-700: #ea7806;   
  --ds-palette-warning-900: #994000;   
  --ds-palette-positive-5: #f8fbfa;   
  --ds-palette-positive-200: #c1f1d5;   
  --ds-palette-positive-300: #97e8b9;   
  --ds-palette-positive-500: #14b456;   
  --ds-palette-positive-700: #0f852c;   
  --ds-palette-positive-900: #0a571a;   
  --ds-palette-accent-5: #f8f9fc;   
  --ds-palette-accent-200: #ccdfff;   
  --ds-palette-accent-300: #a8c9ff;   
  --ds-palette-accent-500: #448aff;   
  --ds-palette-accent-700: #2651b5;   
  --ds-palette-accent-900: #162a69;   
  --ds-palette-contrast-1-5: #fbf7fc;   
  --ds-palette-contrast-1-700: #9c27b0;   
  --ds-palette-contrast-2-990: #291a14;   
  --ds-palette-contrast-3-5: #f9fafb;   
  --ds-palette-contrast-3-990: #142229;   
  --ds-palette-accent-100: #e8f0ff;   
  --ds-palette-neutral-transparent: rgba(255, 255, 255, 0);   
  --ds-palette-accent-990: #0d111c;   
  --ds-palette-accent-950: #151d37;   
  --ds-palette-accent-800: #123da1;   
  --ds-palette-accent-600: #3969d5;   
  --ds-palette-accent-400: #75a9ff;   
  --ds-palette-accent-50: #f0f5ff;   
  --ds-palette-accent-10: #f5f9ff;   
  --ds-palette-positive-990: #04250b;   
  --ds-palette-positive-950: #074013;   
  --ds-palette-positive-800: #0c6e21;   
  --ds-palette-positive-600: #119c34;   
  --ds-palette-positive-400: #50d889;   
  --ds-palette-positive-100: #e0f8ea;   
  --ds-palette-positive-50: #ebfbf2;   
  --ds-palette-positive-10: #f3fcf7;   
  --ds-palette-warning-950: #662a00;   
  --ds-palette-warning-990: #331500;   
  --ds-palette-warning-800: #cc5f00;   
  --ds-palette-warning-600: #fe8c06;   
  --ds-palette-warning-400: #ffc375;   
  --ds-palette-warning-100: #fff4e5;   
  --ds-palette-warning-50: #fff9f0;   
  --ds-palette-warning-10: #fffcf8;   
  --ds-palette-negative-950: #500907;   
  --ds-palette-negative-990: #300403;   
  --ds-palette-negative-800: #af150e;   
  --ds-palette-negative-600: #f4372f;   
  --ds-palette-negative-400: #ff8585;   
  --ds-palette-negative-100: #ffe5e5;   
  --ds-palette-negative-50: #fff2f2;   
  --ds-palette-negative-10: #fff8f8;   
  --ds-palette-neutral-990: #121212;   
  --ds-palette-neutral-950: #212121;   
  --ds-palette-neutral-10: #fafafa;   
  --ds-palette-neutral-50: #f5f5f5;   
  --ds-palette-contrast-1-50: #faf2fc;   
  --ds-palette-contrast-1-100: #f4e2f9;   
  --ds-palette-contrast-1-200: #efd5f6;   
  --ds-palette-contrast-1-300: #e4b8ef;   
  --ds-palette-contrast-1-400: #d58ee6;   
  --ds-palette-contrast-1-500: #c564dd;   
  --ds-palette-contrast-1-600: #b53ad4;   
  --ds-palette-contrast-1-800: #761e86;   
  --ds-palette-contrast-1-990: #2c0b32;   
  --ds-palette-contrast-1-950: #3f1047;   
  --ds-palette-contrast-1-900: #641971;   
  --ds-palette-contrast-1-10: #fcf6fd;   
  --ds-palette-contrast-2-5: #faf8f8;   
  --ds-palette-contrast-2-950: #3e261e;   
  --ds-palette-contrast-2-900: #5a3f35;   
  --ds-palette-contrast-2-800: #795548;   
  --ds-palette-contrast-2-700: #896152;   
  --ds-palette-contrast-2-600: #a57969;   
  --ds-palette-contrast-2-500: #c29180;   
  --ds-palette-contrast-2-400: #d9ac9b;   
  --ds-palette-contrast-2-300: #ebc9bc;   
  --ds-palette-contrast-2-200: #f1d9d0;   
  --ds-palette-contrast-2-100: #f7e9e3;   
  --ds-palette-contrast-2-50: #fcf5f3;   
  --ds-palette-contrast-2-10: #fcf8f6;   
  --ds-palette-contrast-3-950: #263136;   
  --ds-palette-contrast-3-900: #36474e;   
  --ds-palette-contrast-3-800: #4b626d;   
  --ds-palette-contrast-3-700: #607d8b;   
  --ds-palette-contrast-3-600: #728f9d;   
  --ds-palette-contrast-3-500: #90a7b2;   
  --ds-palette-contrast-3-400: #a9c0cb;   
  --ds-palette-contrast-3-300: #c9d7de;   
  --ds-palette-contrast-3-200: #d9e3e8;   
  --ds-palette-contrast-3-100: #e7eff3;   
  --ds-palette-contrast-3-50: #f4f9fb;   
  --ds-palette-contrast-3-10: #f8fafc;   
  --ds-palette-contrast-4-5: #f9fbea;   
  --ds-palette-contrast-4-10: #f6f8dd;   
  --ds-palette-contrast-4-50: #f3f6d5;   
  --ds-palette-contrast-4-100: #edf2c0;   
  --ds-palette-contrast-4-200: #e8edab;   
  --ds-palette-contrast-4-300: #e2e996;   
  --ds-palette-contrast-4-400: #dce481;   
  --ds-palette-contrast-4-500: #d6e06c;   
  --ds-palette-contrast-4-600: #cad742;   
  --ds-palette-contrast-4-700: #b1bd28;   
  --ds-palette-contrast-4-800: #8a931f;   
  --ds-palette-contrast-4-900: #626916;   
  --ds-palette-contrast-4-950: #4f5412;   
  --ds-palette-contrast-4-990: #272a09;   

  
  --ds-space-4x: var(--ds-size-4x);   
  --ds-space-3x: var(--ds-size-3x);   
  --ds-space-6x: var(--ds-size-6x);   
  --ds-space-2-5x: var(--ds-size-2-5x);   
  --ds-space-1-5x: var(--ds-size-1-5x);   
  --ds-space-5x: var(--ds-size-5x);   
  --ds-space-8x: var(--ds-size-8x);   
  --ds-space-3-5x: var(--ds-size-3-5x);   
  --ds-space-0: var(--ds-size-0);   
  --ds-space-2x: var(--ds-size-2x);   
  --ds-space-7x: var(--ds-size-7x);   
  --ds-space-1x: var(--ds-size-1x);   
  --ds-space-0-5x: var(--ds-size-0-5x);   

  
  --ds-radius-4x: var(--ds-size-4x);   
  --ds-radius-2x: var(--ds-size-2x);   
  --ds-radius-6x: var(--ds-size-6x);   
  --ds-radius-0: var(--ds-size-0);   
  --ds-radius-1-5x: var(--ds-size-1-5x);   
  --ds-radius-circular: var(--ds-size-circular);   
  --ds-radius-1x: var(--ds-size-1x);   
  --ds-radius-3x: var(--ds-size-3x);   
  --ds-radius-0-5x: var(--ds-size-0-5x);   

  
  --ds-stroke-pad: 1px;   
  --ds-stroke-1x: 4px;   
  --ds-stroke-0-5x: 2px;   
  --ds-stroke-0-25x: 1px;   
  --ds-stroke-dash: 1px;   

  
  --ds-shadow-shadows-none-blur: var(--ds-size-0);   
  --ds-shadow-shadows-none-spread: var(--ds-size-0);   
  --ds-shadow-shadows-none-color: var(--ds-palette-neutral-0);   
  --ds-shadow-shadows-s-1-x: var(--ds-size-0);   
  --ds-shadow-shadows-s-1-y: var(--ds-size-1x);   
  --ds-shadow-shadows-s-1-blur: var(--ds-size-1-5x);   
  --ds-shadow-shadows-s-1-spread: var(--ds-size-0);   
  --ds-shadow-shadows-s-1-color: rgba(33, 33, 33, 0.1);   
  --ds-shadow-shadows-s-2-x: var(--ds-size-0);   
  --ds-shadow-shadows-s-2-y: var(--ds-size-0);   
  --ds-shadow-shadows-s-2-blur: var(--ds-size-4x);   
  --ds-shadow-shadows-s-2-spread: var(--ds-size-0);   
  --ds-shadow-shadows-s-2-color: rgba(33, 33, 33, 0.12);   
  --ds-shadow-shadows-m-1-x: var(--ds-size-0);   
  --ds-shadow-shadows-m-1-y: var(--ds-size-2-5x);   
  --ds-shadow-shadows-m-1-blur: var(--ds-size-6x);   
  --ds-shadow-shadows-m-1-spread: var(--ds-size-0);   
  --ds-shadow-shadows-m-1-color: rgba(33, 33, 33, 0.12);   
  --ds-shadow-shadows-m-2-x: var(--ds-size-0);   
  --ds-shadow-shadows-m-2-y: var(--ds-size-0);   
  --ds-shadow-shadows-m-2-blur: var(--ds-size-7x);   
  --ds-shadow-shadows-m-2-spread: var(--ds-size-0);   
  --ds-shadow-shadows-m-2-color: rgba(33, 33, 33, 0.12);   
  --ds-shadow-shadows-xl-1-x: var(--ds-size-0);   
  --ds-shadow-shadows-xl-1-y: var(--ds-size-3x);   
  --ds-shadow-shadows-xl-1-blur: var(--ds-size-4x);   
  --ds-shadow-shadows-xl-1-spread: var(--ds-size-0);   
  --ds-shadow-shadows-xl-1-color: rgba(33, 33, 33, 0.16);   
  --ds-shadow-shadows-xl-2-x: var(--ds-size-0);   
  --ds-shadow-shadows-xl-2-y: var(--ds-size-0);   
  --ds-shadow-shadows-xl-2-blur: var(--ds-size-8x);   
  --ds-shadow-shadows-xl-2-spread: var(--ds-size-0);   
  --ds-shadow-shadows-xl-2-color: rgba(33, 33, 33, 0.16);   
  --ds-shadow-shadows-none-y: var(--ds-size-0-5x);   
  --ds-shadow-shadows-none-x: var(--ds-size-0);   
  --ds-shadow-shadows-sl-1-x: var(--ds-size-0);   
  --ds-shadow-shadows-sl-1-y: var(--ds-size-0-5x);   
  --ds-shadow-shadows-sl-1-blur: var(--ds-size-0-5x);   
  --ds-shadow-shadows-sl-1-spread: var(--ds-size-0);   
  --ds-shadow-shadows-sl-1-color: rgba(33, 33, 33, 0.04);   
  --ds-shadow-shadows-sl-2-x: var(--ds-size-0);   
  --ds-shadow-shadows-sl-2-y: var(--ds-size-0);   
  --ds-shadow-shadows-sl-2-blur: var(--ds-size-1x);   
  --ds-shadow-shadows-sl-2-spread: var(--ds-size-0);   
  --ds-shadow-shadows-sl-2-color: rgba(33, 33, 33, 0.12);   

  
  --ds-typography-font-family-family: Roboto;   
  --ds-typography-font-weight-regular: 400;   
  --ds-typography-font-weight-medium: 500;   
  --ds-typography-font-variant-normal: Normal;   
  --ds-typography-font-variant-caps: Caps;   
  --ds-typography-font-size-3x: 12px;   
  --ds-typography-font-size-2-5x: 10px;   
  --ds-typography-font-size-2x: 8px;   
  --ds-typography-line-height-4x: 16px;   
  --ds-typography-line-height-2-5x: 10px;   
  --ds-typography-line-height-3x: 12px;   
  --ds-typography-font-size-3-5x: 14px;   
  --ds-typography-font-size-4x: 16px;   
  --ds-typography-font-size-5x: 20px;   
  --ds-typography-font-size-6x: 24px;   
  --ds-typography-font-size-8-5x: 34px;   
  --ds-typography-line-height-6x: 24px;   
  --ds-typography-line-height-5x: 20px;   
  --ds-typography-line-height-8x: 32px;   
  --ds-typography-letter-spacing-0-25x: 1px;   
  --ds-typography-letter-spacing-0-125x: 0.5px;   
  --ds-typography-letter-spacing-none: 0px;   
  --ds-typography-font-family-family-variant: Helvetica;   
  --ds-typography-line-height-7x: 28px;   
  --ds-typography-line-height-10x: 40px;   
  --ds-typography-font-size-4-5x: 18px;   

  
  --ds-typography-caption-font-size-s: var(--ds-typography-font-size-2x);   
  --ds-typography-caption-line-height-s: var(--ds-typography-line-height-2-5x);   
  --ds-typography-caption-font-size-m: var(--ds-typography-font-size-2-5x);   
  --ds-typography-caption-font-size-l: var(--ds-typography-font-size-3x);   
  --ds-typography-caption-line-height-m: var(--ds-typography-line-height-3x);   
  --ds-typography-caption-line-height-l: var(--ds-typography-line-height-4x);   
  --ds-typography-body-font-size-s: var(--ds-typography-font-size-3-5x);   
  --ds-typography-body-font-size-l: var(--ds-typography-font-size-4-5x);   
  --ds-typography-body-line-height-l: var(--ds-typography-line-height-6x);   
  --ds-typography-body-line-height-s: var(--ds-typography-line-height-5x);   
  --ds-typography-header-font-size-s: var(--ds-typography-font-size-5x);   
  --ds-typography-header-font-size-m: var(--ds-typography-font-size-6x);   
  --ds-typography-header-line-height-l: var(--ds-typography-line-height-10x);   
  --ds-typography-header-line-height-m: var(--ds-typography-line-height-8x);   
  --ds-typography-letter-spacing-s: var(--ds-typography-letter-spacing-0-125x);   
  --ds-typography-letter-spacing-m: var(--ds-typography-letter-spacing-0-25x);   
  --ds-typography-header-font-size-l: var(--ds-typography-font-size-8-5x);   
  --ds-typography-letter-spacing-none: var(--ds-typography-letter-spacing-none);   
  --ds-typography-header-line-height-s: var(--ds-typography-line-height-7x);   
  --ds-typography-body-font-size-m: var(--ds-typography-font-size-4x);   
  --ds-typography-body-line-height-m: var(--ds-typography-line-height-6x);   

  
  --ds-color-brand-accent-super-lightest: var(--ds-palette-accent-5);   
  --ds-color-brand-accent-lighter: var(--ds-palette-accent-50);   
  --ds-color-brand-accent-light: var(--ds-palette-accent-300);   
  --ds-color-brand-accent-default: var(--ds-palette-accent-500);   
  --ds-color-brand-accent-dark: var(--ds-palette-accent-600);   
  --ds-color-brand-accent-darker: var(--ds-palette-accent-700);   
  --ds-color-brand-positive-lightest: var(--ds-palette-positive-10);   
  --ds-color-brand-positive-lighter: var(--ds-palette-positive-50);   
  --ds-color-brand-positive-light: var(--ds-palette-positive-300);   
  --ds-color-brand-positive-default: var(--ds-palette-positive-500);   
  --ds-color-brand-positive-dark: var(--ds-palette-positive-700);   
  --ds-color-brand-positive-darker: var(--ds-palette-positive-900);   
  --ds-color-brand-warning-lightest: var(--ds-palette-warning-10);   
  --ds-color-brand-warning-lighter: var(--ds-palette-warning-50);   
  --ds-color-brand-warning-light: var(--ds-palette-warning-300);   
  --ds-color-brand-warning-default: var(--ds-palette-warning-500);   
  --ds-color-brand-warning-dark: var(--ds-palette-warning-700);   
  --ds-color-brand-warning-darker: var(--ds-palette-warning-900);   
  --ds-color-brand-negative-lightest: var(--ds-palette-negative-10);   
  --ds-color-brand-negative-lighter: var(--ds-palette-negative-50);   
  --ds-color-brand-negative-light: var(--ds-palette-negative-300);   
  --ds-color-brand-negative-default: var(--ds-palette-negative-500);   
  --ds-color-brand-negative-dark: var(--ds-palette-negative-700);   
  --ds-color-brand-negative-darker: var(--ds-palette-negative-900);   
  --ds-color-brand-neutral-default: var(--ds-palette-neutral-0);   
  --ds-color-brand-neutral-super-light: var(--ds-palette-neutral-50);   
  --ds-color-brand-neutral-lightest: var(--ds-palette-neutral-100);   
  --ds-color-brand-neutral-lighter: var(--ds-palette-neutral-200);   
  --ds-color-brand-neutral-light: var(--ds-palette-neutral-300);   
  --ds-color-brand-neutral-neutral: var(--ds-palette-neutral-500);   
  --ds-color-brand-neutral-dark: var(--ds-palette-neutral-600);   
  --ds-color-brand-neutral-darker: var(--ds-palette-neutral-700);   
  --ds-color-brand-neutral-darkest: var(--ds-palette-neutral-800);   
  --ds-color-brand-neutral-super-dark: var(--ds-palette-neutral-900);   
  --ds-color-brand-contrast-1-lightest: var(--ds-palette-contrast-1-5);   
  --ds-color-brand-contrast-1-dark: var(--ds-palette-contrast-1-700);   
  --ds-color-brand-contrast-2-lightest: var(--ds-palette-contrast-2-100);   
  --ds-color-brand-contrast-2-dark: var(--ds-palette-contrast-2-950);   
  --ds-color-brand-contrast-3-lightest: var(--ds-palette-contrast-3-5);   
  --ds-color-brand-contrast-3-dark: var(--ds-palette-contrast-3-950);   
  --ds-color-surface-default: var(--ds-color-brand-neutral-default);   
  --ds-color-surface-hover: var(--ds-color-brand-neutral-super-light);   
  --ds-color-surface-selected: var(--ds-color-brand-neutral-super-light);   
  --ds-color-surface-press: var(--ds-color-brand-neutral-lighter);   
  --ds-color-surface-snack-tooltip: var(--ds-color-brand-neutral-darkest);   
  --ds-color-surface-sidebar-selected: var(--ds-color-brand-accent-lighter);   
  --ds-color-surface-sidebar-active: var(--ds-color-brand-accent-light);   
  --ds-color-table-surfase-default: var(--ds-color-brand-neutral-default);   
  --ds-color-table-surfase-hover: var(--ds-color-brand-neutral-super-light);   
  --ds-color-table-surfase-selected: var(--ds-color-brand-neutral-lightest);   
  --ds-color-table-surfase-head: var(--ds-palette-accent-50);   
  --ds-color-table-surfase-head-group: var(--ds-palette-accent-100);   
  --ds-color-text-primary: var(--ds-color-brand-neutral-super-dark);   
  --ds-color-text-inversive: var(--ds-color-brand-neutral-default);   
  --ds-color-text-secondary: var(--ds-color-brand-neutral-darker);   
  --ds-color-text-placeholder: var(--ds-color-brand-neutral-light);   
  --ds-color-text-disable: var(--ds-color-brand-neutral-neutral);   
  --ds-color-text-accent: var(--ds-color-brand-accent-default);   
  --ds-color-text-positive: var(--ds-color-brand-positive-default);   
  --ds-color-text-warning: var(--ds-color-brand-warning-dark);   
  --ds-color-text-negative: var(--ds-color-brand-negative-default);   
  --ds-color-shapes-lighter-pr: var(--ds-color-brand-accent-lighter);   
  --ds-color-shapes-lighter-sc: var(--ds-color-brand-positive-lighter);   
  --ds-color-shapes-lighter-wr: var(--ds-color-brand-warning-lighter);   
  --ds-color-shapes-lighter-er: var(--ds-color-brand-negative-lighter);   
  --ds-color-shapes-lightest-mg: var(--ds-color-brand-contrast-1-lightest);   
  --ds-color-shapes-lightest-br: var(--ds-color-brand-contrast-2-lightest);   
  --ds-color-shapes-lightest-db: var(--ds-color-brand-contrast-3-lightest);   
  --ds-color-shapes-default: var(--ds-color-brand-neutral-default);   
  --ds-color-shapes-hover: var(--ds-color-brand-neutral-super-light);   
  --ds-color-shapes-press: var(--ds-color-brand-neutral-lighter);   
  --ds-color-icon-primary: var(--ds-color-brand-neutral-darker);   
  --ds-color-icon-inversive: var(--ds-color-brand-neutral-default);   
  --ds-color-icon-disable: var(--ds-color-brand-neutral-neutral);   
  --ds-color-icon-accent: var(--ds-color-brand-accent-default);   
  --ds-color-icon-positive: var(--ds-color-brand-positive-default);   
  --ds-color-icon-warning: var(--ds-color-brand-warning-dark);   
  --ds-color-icon-negative: var(--ds-color-brand-negative-default);   
  --ds-color-stroke-default: var(--ds-color-brand-neutral-lighter);   
  --ds-color-stroke-hover: var(--ds-color-brand-neutral-neutral);   
  --ds-color-stroke-disable: var(--ds-color-brand-neutral-lightest);   
  --ds-color-stroke-accent: var(--ds-color-brand-accent-default);   
  --ds-color-stroke-positive: var(--ds-color-brand-positive-default);   
  --ds-color-stroke-warning: var(--ds-color-brand-warning-default);   
  --ds-color-stroke-negative: var(--ds-color-brand-negative-default);   
  --ds-color-surface-disable: var(--ds-color-brand-neutral-super-light);   
  --ds-color-table-surfase-group: var(--ds-color-brand-neutral-lightest);   
  --ds-color-button-accent-default: var(--ds-palette-accent-500);   
  --ds-color-button-accent-hover: var(--ds-palette-accent-600);   
  --ds-color-button-accent-press: var(--ds-palette-accent-700);   
  --ds-color-button-positive-default: var(--ds-palette-positive-500);   
  --ds-color-button-positive-hover: var(--ds-palette-positive-600);   
  --ds-color-button-positive-press: var(--ds-palette-positive-700);   
  --ds-color-button-warning-default: var(--ds-palette-warning-500);   
  --ds-color-button-warning-hover: var(--ds-palette-warning-600);   
  --ds-color-button-warning-press: var(--ds-palette-warning-700);   
  --ds-color-button-negative-default: var(--ds-palette-negative-500);   
  --ds-color-button-negative-hover: var(--ds-palette-negative-600);   
  --ds-color-button-negative-press: var(--ds-palette-negative-700);   
  --ds-color-button-neutral-default: var(--ds-palette-neutral-0);   
  --ds-color-button-neutral-hover: var(--ds-palette-neutral-10);   
  --ds-color-button-neutral-press: var(--ds-palette-neutral-100);   
  --ds-color-button-neutral-disable: var(--ds-palette-neutral-100);   
  --ds-color-button-accent-lite-default: var(--ds-palette-neutral-0);   
  --ds-color-button-accent-lite-hover: var(--ds-palette-accent-10);   
  --ds-color-button-accent-lite-press: var(--ds-palette-accent-100);   
  --ds-color-button-positive-lite-default: var(--ds-palette-neutral-0);   
  --ds-color-button-positive-lite-hover: var(--ds-palette-positive-10);   
  --ds-color-button-positive-lite-press: var(--ds-palette-positive-100);   
  --ds-color-button-warning-lite-default: var(--ds-palette-neutral-0);   
  --ds-color-button-warning-lite-hover: var(--ds-palette-warning-10);   
  --ds-color-button-warning-lite-press: var(--ds-palette-warning-100);   
  --ds-color-button-negative-lite-default: var(--ds-palette-neutral-0);   
  --ds-color-button-negative-lite-hover: var(--ds-palette-negative-10);   
  --ds-color-button-negative-lite-press: var(--ds-palette-negative-100);   
  --ds-color-surface-default-variant: var(--ds-color-brand-accent-super-lightest);   
  --ds-color-brand-accent-lightest: var(--ds-palette-accent-10);   
  --ds-color-shapes-default-variant: var(--ds-color-brand-accent-super-lightest);   
  --ds-color-shapes-disable: var(--ds-color-brand-neutral-lightest);   
  --ds-color-brand-neutral-default-transparent: var(--ds-palette-neutral-transparent);   
  --ds-color-button-neutral-default-transparent: var(--ds-palette-neutral-transparent);   
  --ds-color-button-accent-lite-default-transparent: var(--ds-palette-neutral-transparent);   
  --ds-color-button-positive-lite-default-transparent: var(--ds-palette-neutral-transparent);   
  --ds-color-button-warning-lite-default-transparent: var(--ds-palette-neutral-transparent);   
  --ds-color-button-negative-lite-default-transparent: var(--ds-palette-neutral-transparent);   
  --ds-color-shapes-default-transparent: var(--ds-color-brand-neutral-default-transparent);   
  --ds-color-table-surfase-default-transparent: var(--ds-color-brand-neutral-default-transparent);   
  --ds-color-table-surfase-zebra: var(--ds-palette-neutral-50);   
  --ds-color-surface-default-transparent: var(--ds-color-brand-neutral-default-transparent);   
  --ds-color-brand-accent-default-transparent: var(--ds-palette-neutral-transparent);   
  --ds-color-brand-contrast-4-lightest: var(--ds-palette-contrast-4-5);   
  --ds-color-brand-contrast-4-dark: var(--ds-palette-contrast-4-950);   
  --ds-color-icon-primary-light: var(--ds-color-brand-neutral-neutral);   

  
  --ds-color-button-accent-filled-default-background: var(--ds-color-button-accent-default);   
  --ds-color-button-accent-filled-default-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-accent-filled-default-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-accent-filled-hover-background: var(--ds-color-button-accent-hover);   
  --ds-color-button-accent-filled-hover-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-accent-filled-hover-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-accent-filled-press-background: var(--ds-color-button-accent-press);   
  --ds-color-button-accent-filled-press-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-accent-filled-press-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-accent-outlined-default-background: var(--ds-color-button-accent-lite-default-transparent);   
  --ds-color-button-accent-outlined-default-text-color: var(--ds-color-text-accent);   
  --ds-color-button-accent-outlined-default-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-accent-outlined-hover-background: var(--ds-color-button-accent-lite-hover);   
  --ds-color-button-accent-outlined-hover-text-color: var(--ds-color-text-accent);   
  --ds-color-button-accent-outlined-hover-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-accent-outlined-press-background: var(--ds-color-button-accent-lite-press);   
  --ds-color-button-accent-outlined-press-text-color: var(--ds-color-text-accent);   
  --ds-color-button-accent-outlined-press-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-accent-outlined-default-border-color: var(--ds-color-stroke-accent);   
  --ds-color-button-neutral-filled-default-background: var(--ds-color-button-neutral-default);   
  --ds-color-button-neutral-outlined-default-background: var(--ds-color-button-neutral-default-transparent);   
  --ds-color-button-neutral-outlined-default-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-outlined-default-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-neutral-outlined-default-border-color: var(--ds-color-stroke-default);   
  --ds-color-button-neutral-filled-default-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-filled-default-icon-color: var(--ds-color-icon-primary);   
  --ds-button-m-size-icon-size: var(--ds-icon-size-size-5x);   
  --ds-button-border-radius: var(--ds-radius-2x);   
  --ds-button-m-size-gap: var(--ds-space-2x);   
  --ds-button-m-size-pad-left: var(--ds-space-3x);   
  --ds-button-m-size-pad-top: var(--ds-space-2x);   
  --ds-button-m-size-pad-right: var(--ds-space-3x);   
  --ds-button-m-size-pad-bottom: var(--ds-space-2x);   
  --ds-color-button-neutral-filled-hover-background: var(--ds-color-button-neutral-hover);   
  --ds-color-button-neutral-filled-hover-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-filled-hover-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-neutral-filled-press-background: var(--ds-color-button-neutral-press);   
  --ds-color-button-neutral-filled-press-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-filled-press-icon-color: var(--ds-color-icon-primary);   
  --ds-button-s-size-icon-size: var(--ds-icon-size-size-5x);   
  --ds-button-s-size-gap: var(--ds-space-1x);   
  --ds-button-s-size-pad-right: var(--ds-space-2x);   
  --ds-button-s-size-pad-bottom: var(--ds-space-1x);   
  --ds-button-s-size-pad-left: var(--ds-space-2x);   
  --ds-button-s-size-pad-top: var(--ds-space-1x);   
  --ds-color-button-accent-outlined-hover-border-color: var(--ds-color-stroke-accent);   
  --ds-color-button-accent-outlined-press-border-color: var(--ds-color-stroke-accent);   
  --ds-color-button-neutral-outlined-hover-background: var(--ds-color-button-neutral-hover);   
  --ds-color-button-neutral-outlined-hover-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-outlined-hover-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-neutral-outlined-hover-border-color: var(--ds-color-stroke-default);   
  --ds-color-button-neutral-outlined-press-background: var(--ds-color-button-neutral-press);   
  --ds-color-button-neutral-outlined-press-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-outlined-press-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-neutral-outlined-press-border-color: var(--ds-color-stroke-default);   
  --ds-color-button-neutral-text-default-background: var(--ds-color-button-neutral-default-transparent);   
  --ds-color-button-neutral-text-default-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-text-default-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-neutral-text-hover-background: var(--ds-color-button-neutral-hover);   
  --ds-color-button-neutral-text-hover-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-text-hover-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-neutral-text-press-background: var(--ds-color-button-neutral-press);   
  --ds-color-button-neutral-text-press-text-color: var(--ds-color-text-primary);   
  --ds-color-button-neutral-text-press-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-accent-text-default-background: var(--ds-color-button-accent-lite-default-transparent);   
  --ds-color-button-accent-text-hover-background: var(--ds-color-button-accent-lite-hover);   
  --ds-color-button-accent-text-press-background: var(--ds-color-button-accent-lite-press);   
  --ds-color-button-accent-text-press-text-color: var(--ds-color-text-accent);   
  --ds-color-button-accent-text-press-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-accent-text-hover-text-color: var(--ds-color-text-accent);   
  --ds-color-button-accent-text-hover-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-accent-text-default-text-color: var(--ds-color-text-accent);   
  --ds-color-button-accent-text-default-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-positive-filled-default-background: var(--ds-color-button-positive-default);   
  --ds-color-button-positive-filled-default-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-positive-filled-default-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-positive-filled-hover-background: var(--ds-color-button-positive-hover);   
  --ds-color-button-positive-filled-hover-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-positive-filled-hover-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-positive-filled-press-background: var(--ds-color-button-positive-press);   
  --ds-color-button-positive-filled-press-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-positive-filled-press-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-positive-outlined-default-background: var(--ds-color-button-neutral-default-transparent);   
  --ds-color-button-positive-text-default-background: var(--ds-color-button-positive-lite-default-transparent);   
  --ds-color-button-positive-text-default-text-color: var(--ds-color-text-positive);   
  --ds-color-button-positive-text-default-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-positive-text-hover-background: var(--ds-color-button-positive-lite-hover);   
  --ds-color-button-positive-text-hover-text-color: var(--ds-color-text-positive);   
  --ds-color-button-positive-text-hover-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-positive-text-press-background: var(--ds-color-button-positive-lite-press);   
  --ds-color-button-positive-text-press-text-color: var(--ds-color-text-positive);   
  --ds-color-button-positive-text-press-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-positive-outlined-default-text-color: var(--ds-color-text-positive);   
  --ds-color-button-positive-outlined-default-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-positive-outlined-default-border-color: var(--ds-color-stroke-positive);   
  --ds-color-button-positive-outlined-hover-background: var(--ds-color-button-positive-lite-hover);   
  --ds-color-button-positive-outlined-hover-text-color: var(--ds-color-text-positive);   
  --ds-color-button-positive-outlined-hover-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-positive-outlined-hover-border-color: var(--ds-color-stroke-positive);   
  --ds-color-button-positive-outlined-press-background: var(--ds-color-button-positive-lite-press);   
  --ds-color-button-positive-outlined-press-text-color: var(--ds-color-text-positive);   
  --ds-color-button-positive-outlined-press-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-positive-outlined-press-border-color: var(--ds-color-stroke-positive);   
  --ds-color-button-warning-filled-default-background: var(--ds-color-button-warning-default);   
  --ds-color-button-warning-filled-default-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-warning-filled-default-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-warning-filled-hover-background: var(--ds-color-button-warning-hover);   
  --ds-color-button-warning-filled-hover-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-warning-filled-hover-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-warning-filled-press-background: var(--ds-color-button-warning-press);   
  --ds-color-button-warning-filled-press-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-warning-filled-press-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-warning-outlined-default-background: var(--ds-color-button-warning-lite-default-transparent);   
  --ds-color-button-warning-text-default-background: var(--ds-color-button-warning-lite-default-transparent);   
  --ds-color-button-warning-text-default-text-color: var(--ds-color-text-warning);   
  --ds-color-button-warning-text-default-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-warning-text-hover-background: var(--ds-color-button-warning-lite-hover);   
  --ds-color-button-warning-text-hover-text-color: var(--ds-color-text-warning);   
  --ds-color-button-warning-text-hover-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-warning-text-press-background: var(--ds-color-button-warning-lite-press);   
  --ds-color-button-warning-text-press-text-color: var(--ds-color-text-warning);   
  --ds-color-button-warning-text-press-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-warning-outlined-default-text-color: var(--ds-color-text-warning);   
  --ds-color-button-warning-outlined-default-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-warning-outlined-default-border-color: var(--ds-color-stroke-warning);   
  --ds-color-button-warning-outlined-hover-background: var(--ds-color-button-warning-lite-hover);   
  --ds-color-button-warning-outlined-hover-text-color: var(--ds-color-text-warning);   
  --ds-color-button-warning-outlined-hover-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-warning-outlined-hover-border-color: var(--ds-color-stroke-warning);   
  --ds-color-button-warning-outlined-press-background: var(--ds-color-button-warning-lite-press);   
  --ds-color-button-warning-outlined-press-text-color: var(--ds-color-text-warning);   
  --ds-color-button-warning-outlined-press-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-warning-outlined-press-border-color: var(--ds-color-stroke-warning);   
  --ds-color-button-negative-filled-default-background: var(--ds-color-button-negative-default);   
  --ds-color-button-negative-filled-default-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-negative-filled-default-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-negative-filled-hover-background: var(--ds-color-button-negative-hover);   
  --ds-color-button-negative-filled-hover-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-negative-filled-hover-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-negative-filled-press-background: var(--ds-color-button-negative-press);   
  --ds-color-button-negative-filled-press-text-color: var(--ds-color-text-inversive);   
  --ds-color-button-negative-filled-press-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-negative-outlined-default-background: var(--ds-color-button-negative-lite-default-transparent);   
  --ds-color-button-negative-text-default-background: var(--ds-color-button-negative-lite-default-transparent);   
  --ds-color-button-negative-text-default-text-color: var(--ds-color-text-negative);   
  --ds-color-button-negative-text-default-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-negative-text-hover-background: var(--ds-color-button-negative-lite-hover);   
  --ds-color-button-negative-text-hover-text-color: var(--ds-color-text-negative);   
  --ds-color-button-negative-text-hover-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-negative-text-press-background: var(--ds-color-button-negative-lite-press);   
  --ds-color-button-negative-text-press-text-color: var(--ds-color-text-negative);   
  --ds-color-button-negative-text-press-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-negative-outlined-default-text-color: var(--ds-color-text-negative);   
  --ds-color-button-negative-outlined-default-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-negative-outlined-default-border-color: var(--ds-color-stroke-negative);   
  --ds-color-button-negative-outlined-hover-background: var(--ds-color-button-negative-lite-hover);   
  --ds-color-button-negative-outlined-hover-text-color: var(--ds-color-text-negative);   
  --ds-color-button-negative-outlined-hover-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-negative-outlined-hover-border-color: var(--ds-color-stroke-negative);   
  --ds-color-button-negative-outlined-press-background: var(--ds-color-button-negative-lite-press);   
  --ds-color-button-negative-outlined-press-text-color: var(--ds-color-text-negative);   
  --ds-color-button-negative-outlined-press-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-negative-outlined-press-border-color: var(--ds-color-stroke-negative);   
  --ds-color-button-icon-neutral-filled-default-background: var(--ds-color-button-neutral-default);   
  --ds-color-button-icon-neutral-filled-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-icon-neutral-filled-hover-background: var(--ds-color-button-neutral-hover);   
  --ds-color-button-icon-neutral-filled-press-background: var(--ds-color-button-neutral-press);   
  --ds-color-button-icon-neutral-outlined-default-background: var(--ds-color-button-neutral-default);   
  --ds-color-button-icon-neutral-outlined-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-icon-neutral-outlined-border-color: var(--ds-color-stroke-default);   
  --ds-color-button-icon-neutral-text-default-background: var(--ds-color-button-neutral-default-transparent);   
  --ds-color-button-icon-neutral-text-hover-background: var(--ds-color-button-neutral-hover);   
  --ds-color-button-icon-neutral-text-press-background: var(--ds-color-button-neutral-press);   
  --ds-color-button-icon-neutral-text-icon-color: var(--ds-color-icon-primary);   
  --ds-color-button-icon-accent-filled-default-background: var(--ds-color-button-accent-default);   
  --ds-color-button-icon-accent-filled-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-icon-accent-filled-hover-background: var(--ds-color-button-accent-hover);   
  --ds-color-button-icon-accent-filled-press-background: var(--ds-color-button-accent-press);   
  --ds-color-button-icon-accent-outlined-default-background: var(--ds-color-button-accent-lite-default);   
  --ds-color-button-icon-accent-text-default-background: var(--ds-color-button-accent-lite-default-transparent);   
  --ds-color-button-icon-accent-text-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-icon-accent-text-hover-background: var(--ds-color-button-accent-lite-hover);   
  --ds-color-button-icon-accent-text-press-background: var(--ds-color-button-accent-lite-press);   
  --ds-color-button-icon-accent-outlined-icon-color: var(--ds-color-icon-accent);   
  --ds-color-button-icon-accent-outlined-border-color: var(--ds-color-stroke-accent);   
  --ds-color-button-icon-accent-outlined-hover-background: var(--ds-color-button-accent-lite-hover);   
  --ds-color-button-icon-accent-outlined-press-background: var(--ds-color-button-accent-lite-press);   
  --ds-button-icon-m-size-icon-size: var(--ds-icon-size-size-5x);   
  --ds-button-icon-border-radius: var(--ds-radius-2x);   
  --ds-button-icon-m-size-pad-left: var(--ds-space-2x);   
  --ds-button-icon-m-size-pad-right: var(--ds-space-2x);   
  --ds-button-icon-m-size-pad-top: var(--ds-space-2x);   
  --ds-button-icon-m-size-pad-bottom: var(--ds-space-2x);   
  --ds-button-icon-s-size-pad-left: var(--ds-space-1x);   
  --ds-button-icon-s-size-pad-right: var(--ds-space-1x);   
  --ds-button-icon-s-size-pad-top: var(--ds-space-1x);   
  --ds-button-icon-s-size-pad-bottom: var(--ds-space-1x);   
  --ds-color-button-icon-neutral-outlined-hover-background: var(--ds-color-button-neutral-hover);   
  --ds-color-button-icon-neutral-outlined-press-background: var(--ds-color-button-neutral-press);   
  --ds-color-button-icon-positive-filled-default-background: var(--ds-color-button-positive-default);   
  --ds-color-button-icon-positive-filled-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-icon-positive-filled-hover-background: var(--ds-color-button-positive-hover);   
  --ds-color-button-icon-positive-filled-press-background: var(--ds-color-button-positive-press);   
  --ds-color-button-icon-positive-outlined-default-background: var(--ds-color-button-positive-lite-default);   
  --ds-color-button-icon-positive-text-default-background: var(--ds-color-button-positive-lite-default-transparent);   
  --ds-color-button-icon-positive-text-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-icon-positive-text-hover-background: var(--ds-color-button-positive-lite-hover);   
  --ds-color-button-icon-positive-text-press-background: var(--ds-color-button-positive-lite-press);   
  --ds-color-button-icon-positive-outlined-icon-color: var(--ds-color-icon-positive);   
  --ds-color-button-icon-positive-outlined-border-color: var(--ds-color-stroke-positive);   
  --ds-color-button-icon-positive-outlined-hover-background: var(--ds-color-button-positive-lite-hover);   
  --ds-color-button-icon-positive-outlined-press-background: var(--ds-color-button-positive-lite-press);   
  --ds-color-button-icon-warning-filled-default-background: var(--ds-color-button-warning-default);   
  --ds-color-button-icon-warning-filled-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-icon-warning-filled-hover-background: var(--ds-color-button-warning-hover);   
  --ds-color-button-icon-warning-filled-press-background: var(--ds-color-button-warning-press);   
  --ds-color-button-icon-warning-outlined-default-background: var(--ds-color-button-warning-lite-default);   
  --ds-color-button-icon-warning-text-default-background: var(--ds-color-button-warning-lite-default-transparent);   
  --ds-color-button-icon-warning-text-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-icon-warning-text-hover-background: var(--ds-color-button-warning-lite-hover);   
  --ds-color-button-icon-warning-text-press-background: var(--ds-color-button-warning-lite-press);   
  --ds-color-button-icon-warning-outlined-icon-color: var(--ds-color-icon-warning);   
  --ds-color-button-icon-warning-outlined-border-color: var(--ds-color-stroke-warning);   
  --ds-color-button-icon-warning-outlined-hover-background: var(--ds-color-button-warning-lite-hover);   
  --ds-color-button-icon-warning-outlined-press-background: var(--ds-color-button-warning-lite-press);   
  --ds-color-button-icon-negative-filled-default-background: var(--ds-color-button-negative-default);   
  --ds-color-button-icon-negative-filled-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-button-icon-negative-filled-hover-background: var(--ds-color-button-negative-hover);   
  --ds-color-button-icon-negative-filled-press-background: var(--ds-color-button-negative-press);   
  --ds-color-button-icon-negative-outlined-default-background: var(--ds-color-button-negative-lite-default);   
  --ds-color-button-icon-negative-text-default-background: var(--ds-color-button-negative-lite-default-transparent);   
  --ds-color-button-icon-negative-text-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-icon-negative-text-hover-background: var(--ds-color-button-negative-lite-hover);   
  --ds-color-button-icon-negative-text-press-background: var(--ds-color-button-negative-lite-press);   
  --ds-color-button-icon-negative-outlined-icon-color: var(--ds-color-icon-negative);   
  --ds-color-button-icon-negative-outlined-border-color: var(--ds-color-stroke-negative);   
  --ds-color-button-icon-negative-outlined-hover-background: var(--ds-color-button-negative-lite-hover);   
  --ds-color-button-icon-negative-outlined-press-background: var(--ds-color-button-negative-lite-press);   
  --ds-button-toggle-border-radius: var(--ds-radius-3x);   
  --ds-button-toggle-pad-left: var(--ds-space-1x);   
  --ds-button-toggle-pad-right: var(--ds-space-1x);   
  --ds-button-toggle-pad-top: var(--ds-space-1x);   
  --ds-button-toggle-pad-bottom: var(--ds-space-1x);   
  --ds-color-button-toggle-filled-background: var(--ds-color-shapes-default);   
  --ds-button-toggle-gap: var(--ds-space-1x);   
  --ds-color-chips-filled-default-background: var(--ds-color-shapes-default-variant);   
  --ds-color-chips-text-color: var(--ds-color-text-primary);   
  --ds-color-chips-icon-color: var(--ds-color-icon-primary);   
  --ds-color-chips-filled-hover-background: var(--ds-color-shapes-hover);   
  --ds-color-chips-filled-press-background: var(--ds-color-shapes-press);   
  --ds-color-chips-outlined-default-background: var(--ds-color-shapes-default);   
  --ds-color-chips-outlined-default-border-color: var(--ds-color-stroke-default);   
  --ds-chips-border-size: var(--ds-stroke-0-25x);   
  --ds-chips-m-size-text-size: var(--ds-typography-body-font-size-s);   
  --ds-chips-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-chips-m-size-icon-size: var(--ds-icon-size-size-5x);   
  --ds-chips-m-size-border-radius: var(--ds-radius-3x);   
  --ds-chips-m-size-gap: var(--ds-space-2x);   
  --ds-chips-m-size-pad-left: var(--ds-space-2x);   
  --ds-chips-m-size-pad-right: var(--ds-space-2x);   
  --ds-chips-m-size-pad-top: var(--ds-space-1-5x);   
  --ds-chips-m-size-pad-bottom: var(--ds-space-1-5x);   
  --ds-chips-s-size-pad-left: var(--ds-space-1-5x);   
  --ds-chips-s-size-pad-right: var(--ds-space-1-5x);   
  --ds-chips-s-size-pad-top: var(--ds-space-1x);   
  --ds-chips-s-size-pad-bottom: var(--ds-space-1x);   
  --ds-color-chips-outlined-hover-background: var(--ds-color-shapes-default);   
  --ds-color-chips-outlined-hover-border-color: var(--ds-color-stroke-hover);   
  --ds-color-chips-outlined-press-background: var(--ds-color-shapes-press);   
  --ds-color-chips-outlined-press-border-color: var(--ds-color-stroke-default);   
  --ds-chips-s-size-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-button-disable-background-filled: var(--ds-color-button-neutral-disable);   
  --ds-color-button-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-button-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-button-disable-background-text: var(--ds-color-button-neutral-default-transparent);   
  --ds-color-button-disable-background-outlined: var(--ds-color-button-neutral-default-transparent);   
  --ds-color-button-disable-border-color: var(--ds-color-stroke-disable);   
  --ds-color-button-icon-disable-background-filled: var(--ds-color-button-neutral-disable);   
  --ds-color-button-icon-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-button-icon-disable-background-text: var(--ds-color-button-neutral-default-transparent);   
  --ds-color-button-icon-disable-background-outlined: var(--ds-color-button-neutral-disable);   
  --ds-color-button-icon-disable-border-color: var(--ds-color-stroke-disable);   
  --ds-color-chips-disable-background-filled: var(--ds-color-shapes-disable);   
  --ds-color-chips-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-chips-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-chips-disable-background-outlined: var(--ds-color-shapes-default);   
  --ds-color-chips-disable-border-color: var(--ds-color-stroke-disable);   
  --ds-button-icon-gap: var(--ds-space-2x);   
  --ds-button-icon-border-size: var(--ds-stroke-0-25x);   
  --ds-button-border-size: var(--ds-stroke-0-25x);   
  --ds-color-form-field-filled-default-input-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-filled-default-icon-color-default: var(--ds-color-icon-primary);   
  --ds-color-form-field-outlined-default-background: var(--ds-color-shapes-default);   
  --ds-color-form-field-outlined-default-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-outlined-default-icon-color: var(--ds-color-icon-primary);   
  --ds-color-form-field-outlined-default-border-color: var(--ds-color-stroke-default);   
  --ds-form-field-m-size-text: var(--ds-typography-body-font-size-m);   
  --ds-form-field-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-form-field-border-size: var(--ds-stroke-0-25x);   
  --ds-form-field-border-radius: var(--ds-radius-3x);   
  --ds-form-field-m-size-icon: var(--ds-icon-size-size-6x);   
  --ds-form-field-s-size-icon: var(--ds-icon-size-size-6x);   
  --ds-color-form-field-outlined-hover-background: var(--ds-color-button-neutral-hover);   
  --ds-color-form-field-outlined-hover-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-outlined-hover-icon-color: var(--ds-color-icon-primary);   
  --ds-color-form-field-outlined-hover-border-color: var(--ds-color-stroke-default);   
  --ds-color-form-field-outlined-focus-background: var(--ds-color-button-neutral-press);   
  --ds-color-form-field-outlined-focus-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-outlined-focus-icon-color: var(--ds-color-icon-primary);   
  --ds-color-form-field-outlined-focus-border-color: var(--ds-color-stroke-default);   
  --ds-form-field-m-size-text-label: var(--ds-typography-caption-font-size-l);   
  --ds-form-field-s-size-text: var(--ds-typography-body-font-size-m);   
  --ds-form-field-s-size-text-label: var(--ds-typography-caption-font-size-l);   
  --ds-form-field-gap-input-support: var(--ds-space-1x);   
  --ds-form-field-gap-input-frame: var(--ds-space-2x);   
  --ds-form-field-gap-input-content: var(--ds-space-0);   
  --ds-form-field-m-size-text-support: var(--ds-typography-caption-font-size-l);   
  --ds-form-field-s-size-text-support: var(--ds-typography-caption-font-size-l);   
  --ds-form-field-pad-support-left: var(--ds-space-3x);   
  --ds-form-field-pad-support-right: var(--ds-space-3x);   
  --ds-form-field-m-size-pad-input-right: var(--ds-space-3x);   
  --ds-form-field-m-size-pad-input-left: var(--ds-space-3x);   
  --ds-form-field-m-size-pad-input-bottom: var(--ds-space-3x);   
  --ds-form-field-m-size-pad-input-top: var(--ds-space-3x);   
  --ds-color-form-field-background-support: var(--ds-color-shapes-default-transparent);   
  --ds-color-form-field-outlined-error-background: var(--ds-color-button-neutral-press);   
  --ds-color-form-field-outlined-error-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-outlined-error-icon-color: var(--ds-color-icon-primary);   
  --ds-color-form-field-outlined-error-border-color: var(--ds-color-stroke-default);   
  --ds-color-form-field-filled-default-label-text-color: var(--ds-color-text-secondary);   
  --ds-color-form-field-filled-default-support-text-color: var(--ds-color-text-secondary);   
  --ds-color-form-field-filled-default-border-color: var(--ds-color-stroke-default);   
  --ds-color-form-field-filled-default-icon-color-warning: var(--ds-color-icon-warning);   
  --ds-color-form-field-input-filled-background: var(--ds-color-shapes-default-variant);   
  --ds-color-form-field-filled-hover-input-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-filled-hover-label-text-color: var(--ds-color-text-secondary);   
  --ds-color-form-field-filled-hover-text-support-color: var(--ds-color-text-secondary);   
  --ds-color-form-field-filled-hover-icon-color-default: var(--ds-color-icon-primary);   
  --ds-color-form-field-filled-hover-icon-color-warning: var(--ds-color-icon-warning);   
  --ds-color-form-field-filled-hover-border-color: var(--ds-color-stroke-hover);   
  --ds-color-form-field-filled-focus-input-cursor-color: var(--ds-color-text-primary);   
  --ds-color-form-field-filled-focus-label-text-color: var(--ds-color-text-accent);   
  --ds-color-form-field-filled-focus-support-text-color: var(--ds-color-text-secondary);   
  --ds-color-form-field-filled-focus-icon-color-default: var(--ds-color-icon-primary);   
  --ds-color-form-field-filled-focus-icon-color-warning: var(--ds-color-icon-warning);   
  --ds-color-form-field-filled-focus-border-color: var(--ds-color-stroke-accent);   
  --ds-color-form-field-filled-focus-input-text-placeholder-color: var(--ds-color-text-placeholder);   
  --ds-color-form-field-filled-focus-input-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-filled-error-input-text-color: var(--ds-color-text-primary);   
  --ds-color-form-field-filled-error-input-text-placeholder-color: var(--ds-color-text-placeholder);   
  --ds-color-form-field-filled-error-input-cursor-color: var(--ds-color-text-primary);   
  --ds-color-form-field-filled-error-label-text-color: var(--ds-color-text-negative);   
  --ds-color-form-field-filled-error-text-support-color: var(--ds-color-text-negative);   
  --ds-color-form-field-filled-error-icon-color-default: var(--ds-color-icon-primary);   
  --ds-color-form-field-filled-error-icon-color-warning: var(--ds-color-icon-warning);   
  --ds-color-form-field-filled-error-border-color: var(--ds-color-stroke-negative);   
  --ds-color-form-field-filled-error-icon-color-error: var(--ds-color-icon-negative);   
  --ds-form-field-filled-focus-border-size-focus: var(--ds-stroke-0-25x);   
  --ds-form-field-filled-error-border-size-focus: var(--ds-stroke-0-5x);   
  --ds-color-form-field-filled-hover-input-background-hover: var(--ds-color-shapes-hover);   
  --ds-color-form-field-filled-error-input-background-hover: var(--ds-color-shapes-hover);   
  --ds-color-form-field-filled-disable-input-text-color: var(--ds-color-text-disable);   
  --ds-color-form-field-filled-disable-label-text-color: var(--ds-color-text-disable);   
  --ds-color-form-field-filled-disable-support-text-color: var(--ds-color-text-disable);   
  --ds-color-form-field-filled-disable-icon-color-disable: var(--ds-color-icon-disable);   
  --ds-color-form-field-filled-disable-icon-color-warning: var(--ds-color-icon-warning);   
  --ds-color-form-field-filled-disable-border-color: var(--ds-color-stroke-disable);   
  --ds-color-form-field-filled-disable-input-background: var(--ds-color-surface-disable);   
  --ds-color-form-field-input-outlined-background: var(--ds-color-shapes-default);   
  --ds-chips-input-m-size-pad-top: var(--ds-size-1x);   
  --ds-chips-input-m-size-pad-bottom: var(--ds-size-2x);   
  --ds-form-field-s-size-pad-input-left: var(--ds-space-3x);   
  --ds-form-field-s-size-pad-input-bottom: var(--ds-space-1-5x);   
  --ds-form-field-s-size-pad-input-top: var(--ds-space-1-5x);   
  --ds-form-field-s-size-pad-input-right: var(--ds-space-3x);   
  --ds-color-button-toggle-outlined-background: var(--ds-color-shapes-default);   
  --ds-button-toggle-outlined-border-size: var(--ds-stroke-0-25x);   
  --ds-color-button-toggle-outlined-border-color: var(--ds-color-stroke-default);   
  --ds-form-field-xs-size-text: var(--ds-typography-body-font-size-s);   
  --ds-form-field-xs-size-text-label: var(--ds-typography-caption-font-size-l);   
  --ds-form-field-xs-size-text-support: var(--ds-typography-caption-font-size-l);   
  --ds-form-field-xs-size-icon: var(--ds-icon-size-size-5x);   
  --ds-form-field-xs-size-pad-input-left: var(--ds-space-2x);   
  --ds-form-field-xs-size-pad-input-right: var(--ds-space-2x);   
  --ds-form-field-xs-size-pad-input-top: var(--ds-space-1x);   
  --ds-form-field-xs-size-pad-input-bottom: var(--ds-space-1x);   
  --ds-color-input-number-input-background: var(--ds-color-shapes-default);   
  --ds-color-input-number-input-default-border-color: var(--ds-color-stroke-default);   
  --ds-input-number-input-border-size: var(--ds-stroke-0-25x);   
  --ds-color-slide-toggle-selected-default-background: var(--ds-color-brand-accent-default);   
  --ds-slide-toggle-border-radius-knob: var(--ds-radius-circular);   
  --ds-slide-toggle-knob-width: var(--ds-size-4x);   
  --ds-slide-toggle-knob-height: var(--ds-size-4x);   
  --ds-slide-toggle-border-radius: var(--ds-radius-3x);   
  --ds-slide-toggle-selected-pad-right: var(--ds-space-0-5x);   
  --ds-slide-toggle-selected-pad-left: var(--ds-space-4x);   
  --ds-slide-toggle-pad-top: var(--ds-space-0-5x);   
  --ds-slide-toggle-pad-bottom: var(--ds-space-0-5x);   
  --ds-slide-toggle-deselected-pad-right: var(--ds-space-4x);   
  --ds-slide-toggle-deselected-pad-left: var(--ds-space-0-5x);   
  --ds-icon-size-size-4x: var(--ds-size-4x);   
  --ds-icon-size-size-9x: var(--ds-size-9x);   
  --ds-icon-size-size-8x: var(--ds-size-8x);   
  --ds-icon-size-size-6x: var(--ds-size-6x);   
  --ds-icon-size-size-5x: var(--ds-size-5x);   
  --ds-icon-size-size-10x: var(--ds-size-10x);   
  --ds-status-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-status-pad-left: var(--ds-space-1-5x);   
  --ds-status-pad-right: var(--ds-space-1-5x);   
  --ds-status-pad-top: var(--ds-space-1x);   
  --ds-status-pad-bottom: var(--ds-space-1x);   
  --ds-color-status-neutral-filled-background: var(--ds-palette-neutral-10);   
  --ds-color-status-neutral-filled-text-color: var(--ds-color-text-secondary);   
  --ds-status-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-status-gap: var(--ds-space-1x);   
  --ds-status-icon-size: var(--ds-icon-size-size-4x);   
  --ds-status-border-radius: var(--ds-radius-2x);   
  --ds-color-status-neutral-text-text-color: var(--ds-color-text-secondary);   
  --ds-color-status-icon-color: var(--ds-color-icon-primary);   
  --ds-color-status-accent-filled-background: var(--ds-palette-accent-10);   
  --ds-color-status-accent-filled-text-color: var(--ds-color-text-accent);   
  --ds-color-status-accent-text-text-color: var(--ds-color-text-accent);   
  --ds-color-status-positive-filled-background: var(--ds-palette-positive-10);   
  --ds-color-status-positive-filled-text-color: var(--ds-color-text-positive);   
  --ds-color-status-positive-text-text-color: var(--ds-color-text-positive);   
  --ds-color-status-warning-filled-background: var(--ds-palette-warning-10);   
  --ds-color-status-warning-filled-text-color: var(--ds-color-text-warning);   
  --ds-color-status-warning-text-text-color: var(--ds-color-text-warning);   
  --ds-color-status-negative-filled-background: var(--ds-palette-negative-10);   
  --ds-color-status-negative-filled-text-color: var(--ds-color-text-negative);   
  --ds-color-status-negative-text-text-color: var(--ds-color-text-negative);   
  --ds-color-status-contrast-1-filled-background: var(--ds-palette-contrast-1-10);   
  --ds-color-status-contrast-1-filled-text-color: var(--ds-palette-contrast-1-700);   
  --ds-color-status-contrast-1-text-text-color: var(--ds-color-brand-contrast-1-dark);   
  --ds-color-status-contrast-2-filled-background: var(--ds-palette-contrast-2-10);   
  --ds-color-status-contrast-2-filled-text-color: var(--ds-palette-contrast-2-950);   
  --ds-color-status-contrast-2-text-text-color: var(--ds-color-brand-contrast-2-dark);   
  --ds-color-status-contrast-3-filled-background: var(--ds-palette-contrast-3-10);   
  --ds-color-status-contrast-3-filled-text-color: var(--ds-palette-contrast-3-950);   
  --ds-color-status-contrast-3-text-text-color: var(--ds-color-brand-contrast-3-dark);   
  --ds-expansion-panel-collaps-text-size: var(--ds-typography-body-font-size-s);   
  --ds-expansion-panel-collaps-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-expansion-panel-collaps-gap: var(--ds-space-2x);   
  --ds-expansion-panel-collaps-border-radius: var(--ds-radius-3x);   
  --ds-expansion-panel-collaps-pad-left: var(--ds-space-4x);   
  --ds-expansion-panel-collaps-pad-right: var(--ds-space-4x);   
  --ds-expansion-panel-collaps-pad-top: var(--ds-space-3x);   
  --ds-expansion-panel-collaps-pad-bottom: var(--ds-space-3x);   
  --ds-expansion-panel-collaps-gap-icon-group: var(--ds-space-2x);   
  --ds-color-expansion-panel-collaps-text-color: var(--ds-color-text-primary);   
  --ds-expansion-panel-collaps-border-size: var(--ds-stroke-0-25x);   
  --ds-color-expansion-panel-collaps-border-color: var(--ds-color-stroke-default);   
  --ds-expansion-panel-content-pad-left: var(--ds-space-4x);   
  --ds-expansion-panel-content-pad-right: var(--ds-space-4x);   
  --ds-expansion-panel-content-pad-top: var(--ds-space-4x);   
  --ds-expansion-panel-content-pad-bottom: var(--ds-space-4x);   
  --ds-expansion-panel-expand-border-radius: var(--ds-radius-3x);   
  --ds-expansion-panel-expand-border-size: var(--ds-stroke-0-25x);   
  --ds-color-expansion-panel-expand-border-color: var(--ds-color-stroke-default);   
  --ds-expansion-panel-content-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-expansion-panel-content-text-color: var(--ds-color-text-primary);   
  --ds-expansion-panel-content-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-dialog-background: var(--ds-color-surface-default);   
  --ds-dialog-border-radius: var(--ds-radius-3x);   
  --ds-dialog-header-gap: var(--ds-space-2x);   
  --ds-dialog-header-pad-top: var(--ds-space-6x);   
  --ds-dialog-header-title-size: var(--ds-typography-font-size-5x);   
  --ds-dialog-header-title-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-dialog-header-title-color: var(--ds-color-text-primary);   
  --ds-dialog-header-desc-size: var(--ds-typography-font-size-4x);   
  --ds-dialog-header-desc-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-dialog-header-desc-color: var(--ds-color-text-secondary);   
  --ds-color-table-cell-text-color: var(--ds-color-text-primary);   
  --ds-color-table-cell-background: var(--ds-color-table-surfase-default-transparent);   
  --ds-table-cell-pad-left: var(--ds-space-2x);   
  --ds-table-cell-pad-right: var(--ds-space-2x);   
  --ds-table-cell-pad-top: var(--ds-space-2x);   
  --ds-table-cell-pad-bottom: var(--ds-space-2x);   
  --ds-color-table-row-header-background-header: var(--ds-color-table-surfase-head);   
  --ds-table-row-header-border-radius-top-left: var(--ds-radius-2x);   
  --ds-table-row-header-border-radius-top-right: var(--ds-radius-2x);   
  --ds-color-table-row-content-default-background: var(--ds-color-table-surfase-default);   
  --ds-table-row-content-border-bottom-size: var(--ds-stroke-0-25x);   
  --ds-color-table-row-content-border-color: var(--ds-color-stroke-default);   
  --ds-color-expansion-panel-collaps-hover-background: var(--ds-color-surface-hover);   
  --ds-color-expansion-panel-collaps-default-background: var(--ds-color-surface-default-variant);   
  --ds-slide-toggle-gap: var(--ds-space-2x);   
  --ds-slide-toggle-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-slide-toggle-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-slide-toggle-selected-hover-background: var(--ds-color-brand-accent-dark);   
  --ds-color-slide-toggle-deselected-default-background: var(--ds-color-brand-neutral-neutral);   
  --ds-color-slide-toggle-deselected-hover-background: var(--ds-color-brand-neutral-dark);   
  --ds-color-slide-toggle-deselected-disable-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-slide-toggle-selected-disable-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-slide-toggle-deselected-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-slide-toggle-selected-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-slide-toggle-text-color: var(--ds-color-text-primary);   
  --ds-color-slide-toggle-knob-color: var(--ds-color-brand-neutral-default);   
  --ds-table-cell-header-hover-border-size: var(--ds-stroke-0-25x);   
  --ds-color-table-cell-header-default-background: var(--ds-color-table-surfase-head);   
  --ds-color-table-row-content-hover-background: var(--ds-color-table-surfase-hover);   
  --ds-color-table-cell-header-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-table-row-content-zebra-background: var(--ds-color-table-surfase-zebra);   
  --ds-dialog-content-title-size: var(--ds-typography-font-size-4x);   
  --ds-dialog-content-gap: var(--ds-space-4x);   
  --ds-color-dialog-content-title-color: var(--ds-color-text-primary);   
  --ds-dialog-footer-pad-bottom: var(--ds-space-4x);   
  --ds-dialog-footer-pad-top: var(--ds-space-4x);   
  --ds-dialog-content-title-weight: var(--ds-typography-font-weight-medium);   
  --ds-dialog-content-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-dialog-content-text-size: var(--ds-typography-font-size-3-5x);   
  --ds-color-dialog-content-text-color: var(--ds-color-text-secondary);   
  --ds-table-cell-text-size: var(--ds-typography-body-font-size-s);   
  --ds-table-cell-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-divider-size-m: var(--ds-stroke-0-25x);   
  --ds-color-table-cell-header-background: var(--ds-color-table-surfase-default-transparent);   
  --ds-color-table-cell-content-default-background: var(--ds-color-table-surfase-default-transparent);   
  --ds-color-table-cell-content-hover-border-color: var(--ds-color-stroke-hover);   
  --ds-table-cell-content-hover-border-size: var(--ds-stroke-0-25x);   
  --ds-color-table-cell-content-focus-border-color: var(--ds-color-stroke-accent);   
  --ds-table-cell-content-focus-border-size: var(--ds-stroke-0-25x);   
  --ds-color-table-cell-content-edit-border-color: var(--ds-color-stroke-accent);   
  --ds-table-cell-content-edit-border-size: var(--ds-stroke-0-25x);   
  --ds-color-table-cell-content-error-border-color: var(--ds-color-stroke-negative);   
  --ds-table-cell-content-error-border-size: var(--ds-stroke-0-25x);   
  --ds-color-table-cell-content-background: var(--ds-color-table-surfase-default-transparent);   
  --ds-color-table-cell-content-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-table-cell-header-hover-background: var(--ds-palette-accent-5);   
  --ds-color-table-cell-header-disable-background: var(--ds-color-table-surfase-head);   
  --ds-color-divider-solid-lite-color: var(--ds-color-stroke-default);   
  --ds-color-divider-solid-default-color: var(--ds-color-stroke-default);   
  --ds-color-divider-solid-hover-color: var(--ds-color-stroke-accent);   
  --ds-color-divider-dashed-default-color: var(--ds-color-stroke-default);   
  --ds-color-table-cell-header-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-table-row-content-selected-background: var(--ds-color-table-surfase-selected);   
  --ds-color-table-cell-content-hover-background: var(--ds-color-table-surfase-hover);   
  --ds-dialog-content-pad-top: var(--ds-space-2x);   
  --ds-color-scroll-default-background: var(--ds-palette-neutral-10);   
  --ds-color-scroll-default-knob-color: var(--ds-palette-neutral-300);   
  --ds-scroll-knob-radius: var(--ds-radius-2x);   
  --ds-scroll-border-radius: var(--ds-radius-2x);   
  --ds-color-scroll-hover-knob-color: var(--ds-palette-neutral-500);   
  --ds-color-scroll-hover-background: var(--ds-palette-neutral-100);   
  --ds-dialog-header-pad-bottom: var(--ds-space-2x);   
  --ds-dialog-content-pad-bottom: var(--ds-space-2x);   
  --ds-button-group-gap: var(--ds-space-2x);   
  --ds-color-backdrop-background: var(--ds-palette-neutral-900);   
  --ds-card-header-pad-top: var(--ds-space-6x);   
  --ds-card-header-pad-bottom: var(--ds-space-2x);   
  --ds-card-header-gap: var(--ds-space-2x);   
  --ds-card-header-title-size: var(--ds-typography-font-size-5x);   
  --ds-card-header-title-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-card-header-title-color: var(--ds-color-text-primary);   
  --ds-card-header-desc-size: var(--ds-typography-font-size-4x);   
  --ds-card-header-desc-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-card-header-desc-color: var(--ds-color-text-secondary);   
  --ds-card-content-gap: var(--ds-space-2x);   
  --ds-card-content-pad-top: var(--ds-space-2x);   
  --ds-card-content-pad-bottom: var(--ds-space-2x);   
  --ds-card-content-title-size: var(--ds-typography-font-size-4x);   
  --ds-card-content-title-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-card-content-title-color: var(--ds-color-text-primary);   
  --ds-card-content-text-size: var(--ds-typography-font-size-4x);   
  --ds-card-content-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-card-content-text-color: var(--ds-color-text-secondary);   
  --ds-card-footer-pad-top: var(--ds-space-4x);   
  --ds-card-footer-pad-bottom: var(--ds-space-4x);   
  --ds-card-pad-left: var(--ds-space-6x);   
  --ds-card-pad-right: var(--ds-space-6x);   
  --ds-card-border-radius: var(--ds-radius-2x);   
  --ds-color-card-background: var(--ds-color-shapes-default);   
  --ds-checkbox-icon-size: var(--ds-icon-size-size-5x);   
  --ds-color-checkbox-normal-deselected-press-background: var(--ds-palette-neutral-200);   
  --ds-color-checkbox-normal-deselected-hover-background: var(--ds-palette-neutral-100);   
  --ds-color-checkbox-normal-deselected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-checkbox-normal-selected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-checkbox-normal-selected-hover-background: var(--ds-palette-accent-100);   
  --ds-color-checkbox-normal-selected-press-background: var(--ds-palette-accent-200);   
  --ds-color-checkbox-normal-selected-icon-color: var(--ds-color-icon-accent);   
  --ds-color-checkbox-normal-inderterminate-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-checkbox-normal-inderterminate-hover-background: var(--ds-palette-accent-100);   
  --ds-color-checkbox-normal-inderterminate-press-background: var(--ds-palette-accent-200);   
  --ds-color-checkbox-normal-inderterminate-icon-color: var(--ds-color-icon-accent);   
  --ds-color-checkbox-error-icon-color: var(--ds-color-icon-negative);   
  --ds-color-checkbox-error-deselected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-checkbox-error-deselected-hover-background: var(--ds-palette-negative-100);   
  --ds-color-checkbox-error-deselected-press-background: var(--ds-palette-negative-200);   
  --ds-color-checkbox-error-selected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-checkbox-error-selected-hover-background: var(--ds-palette-negative-100);   
  --ds-color-checkbox-error-selected-press-background: var(--ds-palette-negative-200);   
  --ds-color-checkbox-error-inderterminate-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-checkbox-error-inderterminate-hover-background: var(--ds-palette-negative-100);   
  --ds-color-checkbox-error-inderterminate-press-background: var(--ds-palette-negative-200);   
  --ds-color-checkbox-disable-deselected-icon-color: var(--ds-color-icon-disable);   
  --ds-color-checkbox-disable-selected-icon-color: var(--ds-color-icon-disable);   
  --ds-color-checkbox-disable-inderterminate-icon-color: var(--ds-color-icon-disable);   
  --ds-color-checkbox-normal-deselected-icon-color: var(--ds-color-icon-primary);   
  --ds-color-checkbox-disable-background: var(--ds-color-shapes-default-transparent);   
  --ds-checkbox-label-gap: var(--ds-space-2x);   
  --ds-checkbox-label-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-checkbox-label-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-checkbox-label-text-color: var(--ds-color-text-primary);   
  --ds-color-checkbox-label-text-disable-color: var(--ds-color-text-disable);   
  --ds-checkbox-group-vertical-gap: var(--ds-space-2x);   
  --ds-checkbox-group-text-size: var(--ds-typography-body-font-size-s);   
  --ds-checkbox-group-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-checkbox-group-text-color: var(--ds-color-text-primary);   
  --ds-color-checkbox-group-text-disable: var(--ds-color-text-disable);   
  --ds-checkbox-group-horizontal-gap: var(--ds-space-8x);   
  --ds-checkbox-group-group-gap: var(--ds-space-2x);   
  --ds-checkbox-group-group-pad-left-0: var(--ds-space-0);   
  --ds-checkbox-group-group-pad-left-4x: var(--ds-space-4x);   
  --ds-color-radio-button-normal-deselected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-radio-button-normal-deselected-icon-color: var(--ds-color-icon-primary);   
  --ds-color-radio-button-normal-deselected-hover-background: var(--ds-palette-neutral-100);   
  --ds-color-radio-button-normal-deselected-press-background: var(--ds-palette-neutral-200);   
  --ds-color-radio-button-normal-selected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-radio-button-normal-selected-icon-color: var(--ds-color-icon-accent);   
  --ds-color-radio-button-normal-selected-hover-background: var(--ds-palette-accent-100);   
  --ds-color-radio-button-normal-selected-press-background: var(--ds-palette-accent-200);   
  --ds-radio-button-icon-size: var(--ds-icon-size-size-5x);   
  --ds-color-radio-button-error-deselected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-radio-button-error-deselected-hover-background: var(--ds-palette-negative-100);   
  --ds-color-radio-button-error-deselected-press-background: var(--ds-palette-negative-200);   
  --ds-color-radio-button-error-selected-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-radio-button-error-selected-hover-background: var(--ds-palette-negative-100);   
  --ds-color-radio-button-error-selected-press-background: var(--ds-palette-negative-200);   
  --ds-color-radio-button-error-icon-color: var(--ds-color-icon-negative);   
  --ds-color-radio-button-disable-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-radio-button-disable-deselected-icon-color: var(--ds-color-icon-disable);   
  --ds-color-radio-button-disable-selected-icon-color: var(--ds-color-icon-disable);   
  --ds-radio-button-label-gap: var(--ds-space-2x);   
  --ds-radio-button-label-text-size: var(--ds-typography-body-font-size-s);   
  --ds-radio-button-label-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-radio-button-label-text-color: var(--ds-color-text-primary);   
  --ds-color-radio-button-label-text-disable-color: var(--ds-color-text-disable);   
  --ds-radio-button-group-vertical-gap: var(--ds-space-2x);   
  --ds-radio-button-group-text-size: var(--ds-typography-body-font-size-s);   
  --ds-radio-button-group-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-radio-button-group-text-color: var(--ds-color-text-primary);   
  --ds-color-radio-button-group-text-disable-color: var(--ds-color-text-disable);   
  --ds-radio-button-group-horizontal-gap: var(--ds-space-8x);   
  --ds-color-input-number-input-icon-color: var(--ds-color-icon-primary);   
  --ds-input-number-input-pad-top: var(--ds-space-2x);   
  --ds-input-number-input-pad-right: var(--ds-space-2x);   
  --ds-input-number-input-pad-bottom: var(--ds-space-2x);   
  --ds-input-number-input-pad-left: var(--ds-space-2x);   
  --ds-input-number-input-border-radius: var(--ds-radius-2x);   
  --ds-input-number-input-gap: var(--ds-space-1x);   
  --ds-input-number-input-text-size: var(--ds-typography-body-font-size-s);   
  --ds-input-number-input-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-input-number-input-text-color: var(--ds-color-text-primary);   
  --ds-color-input-number-input-hover-border-color: var(--ds-color-stroke-hover);   
  --ds-color-input-number-input-focus-border-color: var(--ds-color-stroke-accent);   
  --ds-color-input-number-input-error-border-color: var(--ds-color-stroke-negative);   
  --ds-color-input-number-input-disable-border-color: var(--ds-color-stroke-disable);   
  --ds-color-input-number-input-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-input-number-input-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-input-number-input-error-icon-color: var(--ds-color-icon-negative);   
  --ds-banners-pad-left: var(--ds-space-4x);   
  --ds-banners-pad-right: var(--ds-space-4x);   
  --ds-banners-pad-top: var(--ds-space-3x);   
  --ds-banners-pad-bottom: var(--ds-space-3x);   
  --ds-banners-border-radius: var(--ds-radius-3x);   
  --ds-banners-text-size: var(--ds-typography-body-font-size-s);   
  --ds-banners-text-weight-r: var(--ds-typography-font-weight-regular);   
  --ds-color-banners-neutral-icon-color: var(--ds-color-icon-primary);   
  --ds-color-banners-text-color: var(--ds-color-text-primary);   
  --ds-banners-horizontal-gap: var(--ds-space-2x);   
  --ds-snackbar-pad-left: var(--ds-space-3x);   
  --ds-snackbar-pad-right: var(--ds-space-3x);   
  --ds-snackbar-pad-top: var(--ds-space-3x);   
  --ds-snackbar-pad-bottom: var(--ds-space-3x);   
  --ds-snackbar-border-radius: var(--ds-space-2x);   
  --ds-snackbar-title-size: var(--ds-typography-body-font-size-s);   
  --ds-snackbar-title-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-snackbar-complex-dark-background: var(--ds-color-surface-snack-tooltip);   
  --ds-color-snackbar-complex-dark-text-color: var(--ds-color-text-inversive);   
  --ds-snackbar-gap: var(--ds-space-2x);   
  --ds-color-banners-neutral-background: var(--ds-color-shapes-default);   
  --ds-color-tab-inactive-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-tab-lvl-1-pad-left: var(--ds-space-6x);   
  --ds-tab-lvl-1-pad-right: var(--ds-space-6x);   
  --ds-tab-lvl-1-text-size: var(--ds-typography-body-font-size-m);   
  --ds-tab-lvl-1-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-tab-inactive-icon-color: var(--ds-color-icon-primary);   
  --ds-color-tab-inactive-text-color: var(--ds-color-text-primary);   
  --ds-color-tab-active-icon-color: var(--ds-color-icon-accent);   
  --ds-color-tab-active-text-color: var(--ds-color-text-accent);   
  --ds-badge-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-badge-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-banners-accent-background: var(--ds-color-shapes-lighter-pr);   
  --ds-color-banners-warning-background: var(--ds-color-shapes-lighter-wr);   
  --ds-color-banners-negative-background: var(--ds-color-shapes-lighter-er);   
  --ds-color-banners-positive-background: var(--ds-color-shapes-lighter-sc);   
  --ds-color-banners-accent-icon-color: var(--ds-color-icon-accent);   
  --ds-color-banners-warning-icon-color: var(--ds-color-icon-warning);   
  --ds-color-banners-negative-icon-color: var(--ds-color-icon-negative);   
  --ds-color-banners-positive-icon-color: var(--ds-color-icon-positive);   
  --ds-search-m-size-pad-left: var(--ds-space-3x);   
  --ds-search-m-size-pad-right: var(--ds-space-3x);   
  --ds-search-m-size-pad-top: var(--ds-space-3x);   
  --ds-search-m-size-pad-bottom: var(--ds-space-3x);   
  --ds-search-gap: var(--ds-space-2x);   
  --ds-search-border-radius: var(--ds-space-3x);   
  --ds-search-text-size: var(--ds-typography-body-font-size-m);   
  --ds-search-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-search-focusvalue-text-color: var(--ds-color-text-primary);   
  --ds-color-search-background: var(--ds-color-shapes-default-variant);   
  --ds-color-search-focusvalue-border-color: var(--ds-color-stroke-accent);   
  --ds-form-field-filled-focus-border-size-focus-2: var(--ds-stroke-0-5x);   
  --ds-tab-lvl-1-pad-top: var(--ds-space-1x);   
  --ds-tab-gap: var(--ds-space-2x);   
  --ds-color-badge-text-color: var(--ds-color-text-inversive);   
  --ds-badge-border-radius: var(--ds-radius-circular);   
  --ds-badge-counter-pad-left: var(--ds-space-1-5x);   
  --ds-badge-counter-pad-right: var(--ds-space-1-5x);   
  --ds-color-search-focus-border-color: var(--ds-color-stroke-accent);   
  --ds-color-search-focus-text-color: var(--ds-color-text-placeholder);   
  --ds-color-search-focus-cursor-color: var(--ds-color-text-primary);   
  --ds-color-search-default-border-color: var(--ds-color-stroke-default);   
  --ds-search-border-size: var(--ds-stroke-0-25x);   
  --ds-color-search-default-text-color: var(--ds-color-text-placeholder);   
  --ds-color-search-hover-border-color: var(--ds-color-stroke-hover);   
  --ds-color-search-hover-text-color: var(--ds-color-text-placeholder);   
  --ds-color-search-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-search-disable-background: var(--ds-color-shapes-disable);   
  --ds-color-search-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-tab-active-text-color-counter: var(--ds-color-text-accent);   
  --ds-color-tab-inactive-text-color-counter: var(--ds-color-text-primary);   
  --ds-color-search-completed-border-color: var(--ds-color-stroke-default);   
  --ds-color-search-completed-text-color: var(--ds-color-text-primary);   
  --ds-color-tab-inactive-hover-background: var(--ds-color-shapes-hover);   
  --ds-color-tab-inactive-press-background: var(--ds-color-shapes-press);   
  --ds-color-tab-disable-background: var(--ds-color-shapes-default-transparent);   
  --ds-color-tab-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-tab-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-input-number-control-background: var(--ds-color-shapes-default);   
  --ds-input-number-control-pad-left: var(--ds-space-2x);   
  --ds-input-number-control-pad-right: var(--ds-space-2x);   
  --ds-input-number-control-pad-top: var(--ds-space-2x);   
  --ds-input-number-control-pad-bottom: var(--ds-space-2x);   
  --ds-input-number-control-border-size: var(--ds-stroke-0-25x);   
  --ds-input-number-control-border-radius: var(--ds-radius-2x);   
  --ds-input-number-control-gap: var(--ds-space-0-5x);   
  --ds-input-number-control-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-input-number-control-text-color: var(--ds-color-text-primary);   
  --ds-input-number-control-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-input-number-control-icon-color: var(--ds-color-icon-primary);   
  --ds-color-input-number-control-default-border-color: var(--ds-color-stroke-default);   
  --ds-color-input-number-control-hover-border-color: var(--ds-color-stroke-hover);   
  --ds-color-input-number-control-focus-border-color: var(--ds-color-stroke-accent);   
  --ds-color-input-number-control-error-border-color: var(--ds-color-stroke-negative);   
  --ds-color-input-number-control-error-icon-color: var(--ds-color-icon-negative);   
  --ds-color-input-number-control-disable-border-color: var(--ds-color-stroke-disable);   
  --ds-color-input-number-control-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-input-number-control-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-tab-active-hover-background: var(--ds-color-shapes-hover);   
  --ds-color-tab-active-press-background: var(--ds-color-shapes-press);   
  --ds-divider-size-l: var(--ds-stroke-0-5x);   
  --ds-color-tab-active-default-background: var(--ds-color-shapes-default-transparent);   
  --ds-hint-header-pad-left: var(--ds-space-3x);   
  --ds-hint-header-pad-right: var(--ds-space-3x);   
  --ds-hint-header-pad-top: var(--ds-space-2x);   
  --ds-hint-header-pad-bottom: var(--ds-space-1x);   
  --ds-hint-header-gap: var(--ds-space-2x);   
  --ds-hint-border-radius: var(--ds-space-2x);   
  --ds-hint-header-text-size: var(--ds-typography-body-font-size-s);   
  --ds-hint-header-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-color-hint-header-text-color: var(--ds-color-text-inversive);   
  --ds-color-hint-header-neutral-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-hint-header-accent-icon-color: var(--ds-color-icon-accent);   
  --ds-color-hint-header-positive-icon-color: var(--ds-color-icon-positive);   
  --ds-color-hint-header-warning-icon-color: var(--ds-color-icon-warning);   
  --ds-color-hint-header-negative-icon-color: var(--ds-color-icon-negative);   
  --ds-color-hint-background-color: var(--ds-color-surface-snack-tooltip);   
  --ds-color-hint-header-icon-color: var(--ds-color-icon-inversive);   
  --ds-color-hint-content-text-color: var(--ds-color-text-inversive);   
  --ds-color-hint-content-icon-color: var(--ds-color-icon-inversive);   
  --ds-hint-content-gap: var(--ds-space-2x);   
  --ds-hint-content-pad-top: var(--ds-space-2x);   
  --ds-hint-content-pad-right: var(--ds-space-3x);   
  --ds-hint-content-pad-bottom: var(--ds-space-2x);   
  --ds-hint-content-pad-left: var(--ds-space-3x);   
  --ds-hint-content-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-hint-content-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-hint-footer-pad-left: var(--ds-space-3x);   
  --ds-hint-footer-pad-right: var(--ds-space-3x);   
  --ds-hint-footer-pad-top: var(--ds-space-4x);   
  --ds-hint-footer-pad-bottom: var(--ds-space-3x);   
  --ds-hint-footer-gap: var(--ds-space-3x);   
  --ds-color-hint-footer-text-color: var(--ds-color-text-inversive);   
  --ds-hint-footer-title-size: var(--ds-typography-body-font-size-s);   
  --ds-hint-footer-title-weight: var(--ds-typography-font-weight-medium);   
  --ds-list-item-pad-left: var(--ds-space-4x);   
  --ds-list-item-pad-right: var(--ds-space-4x);   
  --ds-list-item-pad-top: var(--ds-space-2x);   
  --ds-list-item-pad-bottom: var(--ds-space-2x);   
  --ds-color-list-item-text-color: var(--ds-color-text-primary);   
  --ds-list-item-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-list-item-gap: var(--ds-space-2x);   
  --ds-color-list-item-icon-color: var(--ds-color-icon-primary);   
  --ds-color-list-item-default-background: var(--ds-color-surface-default);   
  --ds-color-list-item-hover-background: var(--ds-color-surface-hover);   
  --ds-color-list-item-press-background: var(--ds-color-surface-press);   
  --ds-color-list-item-selected-background: var(--ds-color-surface-default);   
  --ds-color-list-item-negative-background: var(--ds-color-shapes-default);   
  --ds-color-list-item-disable-background: var(--ds-color-surface-default);   
  --ds-color-list-item-text-label-color: var(--ds-color-text-secondary);   
  --ds-color-list-item-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-list-item-disable-label-text-color: var(--ds-color-text-disable);   
  --ds-color-list-item-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-list-item-negative-icon-color: var(--ds-color-icon-negative);   
  --ds-color-list-item-negative-label-text-color: var(--ds-color-text-negative);   
  --ds-color-list-item-negative-text-color: var(--ds-color-text-negative);   
  --ds-color-list-item-selected-icon-color: var(--ds-color-icon-accent);   
  --ds-color-divider-solid-selected-color: var(--ds-color-stroke-accent);   
  --ds-color-tab-disable-divider: var(--ds-color-stroke-disable);   
  --ds-color-divider-solid-disable-color: var(--ds-color-stroke-disable);   
  --ds-tabs-gap: var(--ds-space-0);   
  --ds-search-s-size-pad-left: var(--ds-space-3x);   
  --ds-search-s-size-pad-right: var(--ds-space-3x);   
  --ds-search-s-size-pad-top: var(--ds-space-2x);   
  --ds-search-s-size-pad-bottom: var(--ds-space-2x);   
  --ds-banners-vertical-gap: var(--ds-space-2x);   
  --ds-banners-vertical-gap-container: var(--ds-space-2x);   
  --ds-menu-pad-top: var(--ds-space-2x);   
  --ds-menu-pad-bottom: var(--ds-space-2x);   
  --ds-menu-border-radius: var(--ds-radius-2x);   
  --ds-color-menu-background: var(--ds-color-shapes-default);   
  --ds-icon-size-gap-group-2x: var(--ds-space-2x);   
  --ds-icon-size-gap-group-4x: var(--ds-space-4x);   
  --ds-scroll-pad-bottom: var(--ds-space-0-5x);   
  --ds-scroll-pad-top: var(--ds-space-0-5x);   
  --ds-color-scroll-background: var(--ds-palette-neutral-transparent);   
  --ds-menu-gap: var(--ds-space-0);   
  --ds-menu-gap-list: var(--ds-space-0);   
  --ds-button-group-default-pad-bottom: var(--ds-space-0);   
  --ds-button-group-default-pad-top: var(--ds-space-0);   
  --ds-button-group-default-pad-right: var(--ds-space-0);   
  --ds-button-group-default-pad-left: var(--ds-space-0);   
  --ds-button-group-margins-pad-bottom: var(--ds-space-2x);   
  --ds-button-group-margins-pad-top: var(--ds-space-2x);   
  --ds-button-group-margins-pad-right: var(--ds-space-4x);   
  --ds-button-group-margins-pad-left: var(--ds-space-4x);   
  --ds-color-stepper-background: var(--ds-color-surface-default-transparent);   
  --ds-color-stepper-default-background: var(--ds-palette-neutral-10);   
  --ds-color-stepper-hover-background: var(--ds-palette-accent-10);   
  --ds-color-stepper-hover-text-color: var(--ds-color-text-accent);   
  --ds-color-stepper-hover-icon-color: var(--ds-color-icon-accent);   
  --ds-color-stepper-press-background: var(--ds-palette-accent-50);   
  --ds-color-stepper-press-text-color: var(--ds-color-brand-accent-dark);   
  --ds-color-stepper-press-icon-color: var(--ds-color-icon-accent);   
  --ds-color-stepper-selected-background: var(--ds-palette-accent-10);   
  --ds-color-stepper-selected-text-color: var(--ds-color-text-accent);   
  --ds-color-stepper-selected-icon-color: var(--ds-color-icon-accent);   
  --ds-color-stepper-error-background: var(--ds-palette-negative-10);   
  --ds-color-stepper-error-text-color: var(--ds-color-text-negative);   
  --ds-color-stepper-error-icon-color: var(--ds-color-icon-negative);   
  --ds-color-stepper-disable-background: var(--ds-palette-neutral-10);   
  --ds-color-stepper-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-stepper-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-color-stepper-default-text-color: var(--ds-color-text-primary);   
  --ds-stepper-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-stepper-gap: var(--ds-space-2x);   
  --ds-color-stepper-default-icon-color: var(--ds-color-icon-primary);   
  --ds-stepper-selected-border-size: var(--ds-stroke-0-25x);   
  --ds-stepper-pad-left: var(--ds-space-2x);   
  --ds-stepper-pad-right: var(--ds-space-2x);   
  --ds-stepper-pad-bottom: var(--ds-space-1x);   
  --ds-stepper-pad-top: var(--ds-space-1x);   
  --ds-stepper-border-radius: var(--ds-radius-2x);   
  --ds-color-stepper-text-color: var(--ds-color-text-primary);   
  --ds-stepper-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-stepper-icon-color: var(--ds-color-icon-primary);   
  --ds-color-stepper-selected-border-color: var(--ds-color-stroke-accent);   
  --ds-status-pad-bottom-text: var(--ds-space-0);   
  --ds-status-pad-top-text: var(--ds-space-0);   
  --ds-status-pad-right-text: var(--ds-space-0);   
  --ds-status-pad-left-text: var(--ds-space-0);   
  --ds-chips-s-size-icon-size: var(--ds-icon-size-size-4x);   
  --ds-list-item-text-size: var(--ds-typography-body-font-size-s);   
  --ds-list-item-text-size-label: var(--ds-typography-caption-font-size-l);   
  --ds-menu-item-pad-left: var(--ds-space-4x);   
  --ds-menu-item-pad-right: var(--ds-space-4x);   
  --ds-menu-item-pad-top: var(--ds-space-2x);   
  --ds-menu-item-pad-bottom: var(--ds-space-2x);   
  --ds-color-menu-item-default-background: var(--ds-color-surface-default);   
  --ds-color-menu-item-hover-background: var(--ds-color-surface-hover);   
  --ds-color-menu-item-press-background: var(--ds-color-surface-press);   
  --ds-color-menu-item-selected-background: var(--ds-color-shapes-default);   
  --ds-color-menu-item-selected-icon-color: var(--ds-color-icon-accent);   
  --ds-color-menu-item-negative-background: var(--ds-color-shapes-default);   
  --ds-color-menu-item-negative-text-color: var(--ds-color-text-negative);   
  --ds-color-menu-item-negative-label-text-color: var(--ds-color-text-negative);   
  --ds-color-menu-item-negative-icon-color: var(--ds-color-icon-negative);   
  --ds-color-menu-item-disable-background: var(--ds-color-surface-default);   
  --ds-color-menu-item-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-menu-item-disable-label-text-color: var(--ds-color-text-disable);   
  --ds-color-menu-item-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-menu-item-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-menu-item-text-color: var(--ds-color-text-primary);   
  --ds-menu-item-text-size-label: var(--ds-typography-caption-font-size-l);   
  --ds-color-menu-item-text-label-color: var(--ds-color-text-secondary);   
  --ds-menu-item-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-menu-item-gap: var(--ds-space-2x);   
  --ds-color-menu-item-icon-color: var(--ds-color-icon-primary);   
  --ds-color-expansion-panel-collaps-press-background: var(--ds-color-surface-press);   
  --ds-color-expansion-panel-collaps-disable-background: var(--ds-color-surface-disable);   
  --ds-color-expansion-panel-collaps-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-expansion-panel-collaps-disable-border-color: var(--ds-color-stroke-disable);   
  --ds-color-expansion-panel-content-background: var(--ds-color-surface-default);   
  --ds-expansion-panel-collaps-gap-group: var(--ds-space-2x);   
  --ds-hint-content-gap-content: var(--ds-space-1x);   
  --ds-search-xs-size-pad-left: var(--ds-space-3x);   
  --ds-search-xs-size-pad-right: var(--ds-space-3x);   
  --ds-search-xs-size-pad-top: var(--ds-space-2x);   
  --ds-search-xs-size-pad-bottom: var(--ds-space-2x);   
  --ds-sidenav-footer-l1-collapsed-gap: var(--ds-space-0);   
  --ds-sidenav-header-l2-gap: var(--ds-space-2x);   
  --ds-color-sidenav-header-l1-background: var(--ds-palette-contrast-3-950);   
  --ds-color-sidenav-header-l2-background: var(--ds-color-surface-default);   
  --ds-stepper-gap-line: var(--ds-space-2x);   
  --ds-stepper-divider-width: var(--ds-size-2x);   
  --ds-color-stepper-divider-color: var(--ds-palette-neutral-700);   
  --ds-stepper-text-weight-button: var(--ds-typography-font-weight-medium);   
  --ds-stepper-gap-button: var(--ds-space-4x);   
  --ds-color-search-hover-background-xs: var(--ds-palette-accent-100);   
  --ds-color-search-default-background-xs: var(--ds-palette-accent-50);   
  --ds-hint-arrow-width: var(--ds-space-2x);   
  --ds-hint-arrow-height: var(--ds-space-1x);   
  --ds-tab-lvv-2-pad-left: var(--ds-space-3x);   
  --ds-tab-lvv-2-pad-right: var(--ds-space-3x);   
  --ds-tab-lvv-2-pad-top: var(--ds-space-1x);   
  --ds-color-divider-dashed-selected-color: var(--ds-color-stroke-accent);   
  --ds-color-divider-dashed-disable-color: var(--ds-color-stroke-disable);   
  --ds-tab-lvv-2-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-sidenav-header-pad-bottom: var(--ds-space-3x);   
  --ds-sidenav-header-pad-top: var(--ds-space-3x);   
  --ds-sidenav-header-l1-collapsed-pad-right: var(--ds-space-3-5x);   
  --ds-sidenav-header-l1-collapsed-pad-left: var(--ds-space-3-5x);   
  --ds-sidenav-header-l1-expanded-pad-right: var(--ds-space-4x);   
  --ds-sidenav-header-l1-expanded-pad-left: var(--ds-space-4x);   
  --ds-sidenav-header-l2-gap-content: var(--ds-space-2x);   
  --ds-sidenav-header-l2-pad-right: var(--ds-space-4x);   
  --ds-sidenav-header-l2-pad-left: var(--ds-space-4x);   
  --ds-sidenav-control-pad-top: var(--ds-space-2x);   
  --ds-sidenav-control-pad-bottom: var(--ds-space-3x);   
  --ds-color-sidenav-control-background: var(--ds-palette-contrast-3-950);   
  --ds-color-sidenav-control-background-hover: var(--ds-palette-contrast-3-900);   
  --ds-color-sidenav-control-background-press: var(--ds-palette-contrast-3-900);   
  --ds-sidenav-control-pad-left: var(--ds-space-4x);   
  --ds-sidenav-control-pad-right: var(--ds-space-4x);   
  --ds-sidenav-header-l2-text-size: var(--ds-typography-body-font-size-m);   
  --ds-color-sidenav-header-l2-text-color: var(--ds-color-text-primary);   
  --ds-sidenav-header-l2-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-sidenav-element-gap: var(--ds-space-0);   
  --ds-color-sidenav-element-collaps-icon-background: var(--ds-palette-contrast-3-900);   
  --ds-sidenav-control-collapsed-gap: var(--ds-space-0);   
  --ds-sidenav-control-expanded-gap: var(--ds-space-0);   
  --ds-sidenav-control-expanded-gap-content: var(--ds-space-2x);   
  --ds-color-sidenav-item-l1-background: var(--ds-palette-contrast-3-950);   
  --ds-color-sidenav-item-l1-background-hover: var(--ds-palette-contrast-3-900);   
  --ds-color-sidenav-item-l1-background-selected: var(--ds-palette-contrast-3-800);   
  --ds-sidenav-item-l1-pad-left: var(--ds-space-4x);   
  --ds-sidenav-item-l1-pad-right: var(--ds-space-4x);   
  --ds-sidenav-item-l2-gap-container: var(--ds-space-2x);   
  --ds-sidenav-item-l2-gap-content: var(--ds-space-2x);   
  --ds-sidenav-item-l2-pad-left: var(--ds-space-4x);   
  --ds-sidenav-item-l2-pad-right: var(--ds-space-4x);   
  --ds-color-sidenav-item-l2-background: var(--ds-color-surface-default);   
  --ds-color-sidenav-item-l2-text-color: var(--ds-color-text-primary);   
  --ds-sidenav-item-l2-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-sidenav-item-l2-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-sidenav-item-l1-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-sidenav-item-l1-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-sidenav-item-l1-text-color: var(--ds-color-text-inversive);   
  --ds-color-sidenav-item-l2-background-selected: var(--ds-color-brand-accent-lighter);   
  --ds-color-sidenav-item-l2-background-hover: var(--ds-color-brand-accent-super-lightest);   
  --ds-sidenav-item-l2-pad-bottom: var(--ds-space-2-5x);   
  --ds-sidenav-item-l2-pad-top: var(--ds-space-2-5x);   
  --ds-sidenav-item-l3-gap: var(--ds-space-2x);   
  --ds-sidenav-item-l3-pad-left: var(--ds-space-8x);   
  --ds-sidenav-item-l3-pad-right: var(--ds-space-4x);   
  --ds-sidenav-item-l3-pad-top: var(--ds-space-2x);   
  --ds-sidenav-item-l3-pad-bottom: var(--ds-space-2x);   
  --ds-color-sidenav-item-l3-text-color: var(--ds-color-text-primary);   
  --ds-sidenav-item-l3-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-sidenav-item-l3-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-sidenav-item-l3-background: var(--ds-color-surface-default);   
  --ds-color-sidenav-item-l3-background-hover: var(--ds-color-brand-accent-super-lightest);   
  --ds-color-sidenav-item-l3-background-selected: var(--ds-color-brand-accent-lighter);   
  --ds-color-sidenav-item-l3-text-color-selected: var(--ds-color-text-accent);   
  --ds-sidenav-footer-l1-expanded-gap: var(--ds-space-0);   
  --ds-sidenav-footer-l2-gap: var(--ds-space-3x);   
  --ds-sidenav-footer-l2-pad-bottom: var(--ds-space-3x);   
  --ds-sidenav-footer-l2-pad-right: var(--ds-space-4x);   
  --ds-sidenav-footer-l2-pad-top: var(--ds-space-3x);   
  --ds-sidenav-footer-l2-pad-left: var(--ds-space-4x);   
  --ds-color-sidenav-footer-l2-background: var(--ds-color-surface-default);   
  --ds-sidenav-footer-l2-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-sidenav-footer-l2-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-sidenav-footer-l2-text-color: var(--ds-color-text-secondary);   
  --ds-sidenav-footer-l2-logo-width: 38px;   
  --ds-sidenav-footer-l2-logo-height: 16px;   
  --ds-sidenav-sidebar-l1-gap: var(--ds-space-0);   
  --ds-sidenav-sidebar-l2-gap: var(--ds-space-0);   
  --ds-sidenav-sidebar-pad-top: var(--ds-space-2x);   
  --ds-sidenav-sidebar-pad-bottom: var(--ds-space-2x);   
  --ds-color-sidenav-sidebar-l1-background: var(--ds-palette-contrast-3-950);   
  --ds-chips-s-size-border-radius: var(--ds-radius-2x);   
  --ds-form-field-xs-size-border-radius: var(--ds-radius-0);   
  --ds-button-xs-size-icon-size: var(--ds-icon-size-size-4x);   
  --ds-button-xs-size-gap: var(--ds-space-1x);   
  --ds-button-xs-size-pad-left: var(--ds-space-1-5x);   
  --ds-button-xs-size-pad-right: var(--ds-space-1-5x);   
  --ds-button-xs-size-pad-top: var(--ds-space-1x);   
  --ds-button-xs-size-pad-bottom: var(--ds-space-1x);   
  --ds-button-xs-size-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-button-xs-size-text-size: var(--ds-typography-caption-font-size-l);   
  --ds-button-icon-xs-size-pad-left: var(--ds-space-1x);   
  --ds-button-icon-xs-size-pad-right: var(--ds-space-1x);   
  --ds-button-icon-xs-size-pad-top: var(--ds-space-1x);   
  --ds-button-icon-xs-size-pad-bottom: var(--ds-space-1x);   
  --ds-list-gap: var(--ds-space-0);   
  --ds-list-gap-list: var(--ds-space-0);   
  --ds-list-pad-top: var(--ds-space-2x);   
  --ds-list-pad-bottom: var(--ds-space-2x);   
  --ds-list-border-radius: var(--ds-radius-0);   
  --ds-color-list-background: var(--ds-color-shapes-default);   
  --ds-scroll-pad-right: var(--ds-space-0-5x);   
  --ds-scroll-pad-left: var(--ds-space-0-5x);   
  --ds-color-menu-item-selected-back-selected: var(--ds-palette-accent-10);   
  --ds-menu-item-pad-left-s: 32px;   
  --ds-menu-item-pad-left-m: 48px;   
  --ds-color-list-item-selected-back-selected: var(--ds-palette-accent-10);   
  --ds-color-form-field-input-label-text-color: var(--ds-color-text-secondary);   
  --ds-form-field-pad-textarea-top: var(--ds-space-1x);   
  --ds-form-field-pad-textarea-bottom: var(--ds-space-2x);   
  --ds-color-status-contrast-4-filled-background: var(--ds-palette-contrast-4-5);   
  --ds-color-status-contrast-4-filled-text-color: var(--ds-palette-contrast-4-950);   
  --ds-color-status-contrast-4-text-text-color: var(--ds-color-brand-contrast-4-dark);   
  --ds-snackbar-cont-size: var(--ds-typography-caption-font-size-l);   
  --ds-snackbar-cont-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-snackbar-complex-light-background: var(--ds-color-surface-default);   
  --ds-snackbar-max-width: 370px;   
  --ds-color-snackbar-complex-light-text-color: var(--ds-color-text-primary);   
  --ds-color-snackbar-progress-color: var(--ds-color-icon-accent);   
  --ds-dialog-header-pad-right: var(--ds-space-6x);   
  --ds-dialog-header-pad-left: var(--ds-space-6x);   
  --ds-dialog-content-pad-left: var(--ds-space-6x);   
  --ds-dialog-content-pad-right: var(--ds-space-6x);   
  --ds-dialog-footer-pad-right: var(--ds-space-6x);   
  --ds-dialog-footer-pad-left: var(--ds-space-6x);   
  --ds-sidenav-item-l1-pad-bottom: var(--ds-space-3x);   
  --ds-sidenav-item-l1-pad-top: var(--ds-space-3x);   
  --ds-color-sidenav-item-l1-indicator: var(--ds-color-icon-inversive);   
  --ds-color-sidenav-item-l1-element-left: var(--ds-color-icon-inversive);   
  --ds-sidenav-item-l1-gap-container: var(--ds-space-2x);   
  --ds-color-sidenav-item-l1-element-right: var(--ds-color-icon-inversive);   
  --ds-sidenav-item-l1-gap-content: var(--ds-space-2x);   
  --ds-color-sidenav-item-l3-indicator: var(--ds-color-icon-accent);   
  --ds-sidenav-control-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-sidenav-control-text-size: var(--ds-typography-caption-font-size-m);   
  --ds-color-sidenav-control-text-color: var(--ds-color-text-inversive);   
  --ds-color-sidenav-control-divider: var(--ds-palette-contrast-3-900);   
  --ds-sidenav-header-l1-expanded-gap: 92px;   
  --ds-color-sidenav-header-l1-expanded-logo: var(--ds-color-shapes-default);   
  --ds-color-sidenav-header-l1-collapsed-logo: var(--ds-color-shapes-default);   
  --ds-color-sidenav-header-l1-collapsed-logo-element: var(--ds-palette-negative-500);   
  --ds-color-sidenav-footer-l2-logo: var(--ds-palette-negative-500);   
  --ds-sidenav-header-l1-expanded-logo-width: 56px;   
  --ds-sidenav-header-l1-expanded-logo-height: 24px;   
  --ds-color-sidenav-sidebar-l2-background: var(--ds-color-surface-default);   
  --ds-sidenav-sidebar-info-pad-top: var(--ds-space-4x);   
  --ds-color-sidenav-sidebar-info-background-container: var(--ds-color-surface-default-variant);   
  --ds-sidenav-sidebar-info-pad-bottom: var(--ds-space-4x);   
  --ds-sidenav-sidebar-info-pad-left: var(--ds-space-2x);   
  --ds-sidenav-sidebar-info-pad-right: var(--ds-space-2x);   
  --ds-color-sidenav-item-l3-background-active: var(--ds-color-brand-accent-lighter);   
  --ds-sidenav-sidebar-info-pad-left-container: var(--ds-space-3x);   
  --ds-sidenav-sidebar-info-pad-right-container: var(--ds-space-3x);   
  --ds-sidenav-sidebar-info-pad-top-container: var(--ds-space-3x);   
  --ds-sidenav-sidebar-info-pad-bottom-container: var(--ds-space-3x);   
  --ds-sidenav-sidebar-info-gap-container: var(--ds-space-4x);   
  --ds-table-pad-top: var(--ds-space-3x);   
  --ds-table-pad-left: var(--ds-space-8x);   
  --ds-table-pad-right: var(--ds-space-8x);   
  --ds-table-pad-bottom: var(--ds-space-3x);   
  --ds-table-footer-pad-bottom: var(--ds-space-3x);   
  --ds-table-footer-pad-top: var(--ds-space-3x);   
  --ds-table-footer-pad-right: var(--ds-space-8x);   
  --ds-table-footer-pad-left: var(--ds-space-8x);   
  --ds-color-table-footer-background: var(--ds-color-table-surfase-default);   
  --ds-chips-input-gap-chips-input-frame: var(--ds-size-1x);   
  --ds-color-status-background: var(--ds-color-shapes-default-transparent);   
  --ds-chips-gap-group: var(--ds-space-2x);   
  --ds-button-m-size-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-button-m-size-text-size: var(--ds-typography-body-font-size-s);   
  --ds-button-s-size-text-weight: var(--ds-typography-font-weight-medium);   
  --ds-button-s-size-text-size: var(--ds-typography-body-font-size-s);   
  --ds-button-icon-s-size-icon-size: var(--ds-icon-size-size-5x);   
  --ds-button-icon-xs-size-icon-size: var(--ds-icon-size-size-4x);   
  --ds-color-list-item-link-background: var(--ds-color-surface-default);   
  --ds-color-list-item-link-text-color: var(--ds-color-text-accent);   
  --ds-checkbox-label-gap-support: var(--ds-space-1x);   
  --ds-checkbox-label-pad-left-support-0: var(--ds-space-0);   
  --ds-checkbox-label-pad-left-support-7x: var(--ds-space-7x);   
  --ds-radio-button-label-gap-support: var(--ds-space-1x);   
  --ds-checkbox-group-vertical-gap-support: var(--ds-space-2x);   
  --ds-checkbox-group-group-gap-support: var(--ds-space-2x);   
  --ds-checkbox-group-horizontal-gap-support: var(--ds-space-2x);   
  --ds-radio-button-group-vertical-gap-support: var(--ds-space-2x);   
  --ds-radio-button-group-horizontal-gap-support: var(--ds-space-2x);   
  --ds-radio-button-label-pad-left-support-7x: var(--ds-space-7x);   
  --ds-radio-button-label-pad-left-support-0: var(--ds-space-0);   
  --ds-slide-toggle-gap-support: var(--ds-space-1x);   
  --ds-slide-toggle-pad-left-support-10-5x: 42px;   
  --ds-slide-toggle-pad-left-support-0: var(--ds-space-0);   
  --ds-chips-s-size-gap: var(--ds-space-1x);   
  --ds-color-slide-toggle-text-support-color: var(--ds-color-text-secondary);   
  --ds-slide-toggle-text-support-weight: var(--ds-typography-font-weight-regular);   
  --ds-slide-toggle-text-support-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-checkbox-label-text-support-color: var(--ds-color-text-secondary);   
  --ds-checkbox-label-text-support-weight: var(--ds-typography-font-weight-regular);   
  --ds-checkbox-label-text-support-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-checkbox-group-text-support-color: var(--ds-color-text-secondary);   
  --ds-checkbox-group-text-support-weight: var(--ds-typography-font-weight-regular);   
  --ds-checkbox-group-text-support-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-slide-toggle-text-error-color: var(--ds-color-text-negative);   
  --ds-color-radio-button-label-text-support-color: var(--ds-color-text-secondary);   
  --ds-radio-button-label-text-support-weight: var(--ds-typography-font-weight-regular);   
  --ds-radio-button-label-text-support-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-radio-button-label-text-error-color: var(--ds-color-text-negative);   
  --ds-radio-button-group-text-support-weight: var(--ds-typography-font-weight-regular);   
  --ds-radio-button-group-text-support-size: var(--ds-typography-caption-font-size-l);   
  --ds-color-radio-button-group-text-support-color: var(--ds-color-text-secondary);   
  --ds-color-radio-button-group-text-support-error-color: var(--ds-color-text-negative);   
  --ds-color-checkbox-label-text-support-error-color: var(--ds-color-text-negative);   
  --ds-color-checkbox-group-text-support-error-color: var(--ds-color-text-negative);   
  --ds-color-badge-accent-background: var(--ds-color-brand-accent-default);   
  --ds-color-badge-negative-background: var(--ds-color-brand-negative-default);   
  --ds-color-badge-positive-background: var(--ds-color-brand-positive-default);   
  --ds-color-badge-warning-background: var(--ds-color-brand-warning-default);   
  --ds-badge-point-height: var(--ds-size-2x);   
  --ds-badge-point-width: var(--ds-size-2x);   
  --ds-banners-border-dash-size: var(--ds-stroke-dash);   
  --ds-color-banners-border-color: var(--ds-color-stroke-accent);   
  --ds-banners-text-weight-m: var(--ds-typography-font-weight-medium);   
  --ds-color-text-ui-default-background: var(--ds-color-surface-default);   
  --ds-color-text-ui-hover-background: var(--ds-color-surface-hover);   
  --ds-color-text-ui-press-background: var(--ds-color-surface-press);   
  --ds-color-text-ui-selected-background: var(--ds-color-surface-default);   
  --ds-color-text-ui-link-background: var(--ds-color-surface-default);   
  --ds-color-text-ui-link-text-color: var(--ds-color-text-accent);   
  --ds-color-text-ui-selected-back-selected: var(--ds-palette-accent-10);   
  --ds-color-text-ui-selected-icon-color: var(--ds-color-icon-accent);   
  --ds-color-text-ui-negative-background: var(--ds-color-shapes-default);   
  --ds-color-text-ui-negative-text-color: var(--ds-color-text-negative);   
  --ds-color-text-ui-negative-label-text-color: var(--ds-color-text-negative);   
  --ds-color-text-ui-negative-icon-color: var(--ds-color-icon-negative);   
  --ds-color-text-ui-disable-background: var(--ds-color-surface-default);   
  --ds-color-text-ui-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-text-ui-disable-label-text-color: var(--ds-color-text-disable);   
  --ds-color-text-ui-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-text-ui-gap: var(--ds-space-2x);   
  --ds-text-ui-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-text-ui-text-color: var(--ds-color-text-primary);   
  --ds-text-ui-text-size-label: var(--ds-typography-caption-font-size-l);   
  --ds-color-text-ui-text-label-color: var(--ds-color-text-secondary);   
  --ds-text-ui-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-text-ui-icon-color: var(--ds-color-icon-primary);   
  --ds-text-ui-pad-top: var(--ds-space-2x);   
  --ds-text-ui-pad-bottom: var(--ds-space-2x);   
  --ds-text-ui-pad-left: var(--ds-space-4x);   
  --ds-text-ui-pad-right: var(--ds-space-4x);   
  --ds-table-cell-pad-left-2x: 36px;   
  --ds-color-text-ui-text-placeholder: var(--ds-color-text-placeholder);   
  --ds-badge-counter-pad-bottom: var(--ds-size-0-25x);   
  --ds-badge-counter-pad-top: var(--ds-size-0-25x);   
  --ds-color-chips-outlined-focus-background: var(--ds-color-shapes-default);   
  --ds-color-chips-outlined-focus-border-color: var(--ds-color-stroke-accent);   
  --ds-color-banners-accent-background-tip: var(--ds-color-brand-accent-lightest);   
  --ds-banners-text-size-tip: var(--ds-typography-caption-font-size-l);   
  --ds-dialog-shadows: 12 dp M;   
  --ds-snackbar-gap-group: var(--ds-space-2x);   
  --ds-color-snackbar-single-dark-background: var(--ds-color-surface-snack-tooltip);   
  --ds-color-snackbar-single-dark-text-color: var(--ds-color-text-inversive);   
  --ds-color-snackbar-single-light-background: var(--ds-color-surface-default);   
  --ds-color-snackbar-single-light-text-color: var(--ds-color-text-primary);   
  --ds-select-item-gap: var(--ds-space-2x);   
  --ds-select-item-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-select-item-text-color: var(--ds-color-text-primary);   
  --ds-select-item-text-size-label: var(--ds-typography-caption-font-size-l);   
  --ds-color-select-item-text-label-color: var(--ds-color-text-secondary);   
  --ds-select-item-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-color-select-item-icon-color: var(--ds-color-icon-primary);   
  --ds-select-item-pad-left-s: 32px;   
  --ds-select-item-pad-left-m: 48px;   
  --ds-select-item-pad-left: var(--ds-space-4x);   
  --ds-select-item-pad-right: var(--ds-space-4x);   
  --ds-select-item-pad-top: var(--ds-space-2x);   
  --ds-select-item-pad-bottom: var(--ds-space-2x);   
  --ds-color-select-item-default-background: var(--ds-color-surface-default);   
  --ds-color-select-item-hover-background: var(--ds-color-surface-hover);   
  --ds-color-select-item-press-background: var(--ds-color-surface-press);   
  --ds-color-select-item-selected-background: var(--ds-color-shapes-default);   
  --ds-color-select-item-selected-back-selected: var(--ds-palette-accent-10);   
  --ds-color-select-item-selected-icon-color: var(--ds-color-icon-accent);   
  --ds-color-select-item-negative-background: var(--ds-color-shapes-default);   
  --ds-color-select-item-negative-text-color: var(--ds-color-text-negative);   
  --ds-color-select-item-negative-label-text-color: var(--ds-color-text-negative);   
  --ds-color-select-item-negative-icon-color: var(--ds-color-icon-negative);   
  --ds-color-select-item-disable-background: var(--ds-color-surface-default);   
  --ds-color-select-item-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-select-item-disable-label-text-color: var(--ds-color-text-disable);   
  --ds-color-select-item-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-select-item-text-size-sub: var(--ds-typography-caption-font-size-m);   
  --ds-select-item-text-weight-sub: var(--ds-typography-font-weight-medium);   
  --ds-select-item-pad-top-sub: var(--ds-space-3x);   
  --ds-select-item-pad-bottom-sub: var(--ds-space-1-5x);   
  --ds-dialog-content-gap-text: var(--ds-space-2x);   
  --ds-card-border-size: var(--ds-stroke-0-25x);   
  --ds-color-card-border-color: var(--ds-color-stroke-default);   
  --ds-card-shadows: 01 dp Sl;   
  --ds-tab-lvl-1-pad-bottom: var(--ds-space-1x);   
  --ds-tab-lvv-2-pad-bottom: var(--ds-space-1x);   
  --ds-tab-lvv-2-text-size: var(--ds-typography-body-font-size-s);   
  --ds-color-tab-icon-color-negative: var(--ds-color-icon-negative);   
  --ds-color-expansion-panel-collaps-default-background-info: var(--ds-color-brand-accent-lightest);   
  --ds-color-expansion-panel-content-background-info: var(--ds-color-brand-accent-lightest);   
  --ds-color-expansion-panel-collaps-hover-background-info: var(--ds-color-brand-accent-lighter);   
  --ds-color-expansion-panel-collaps-press-background-info: var(--ds-palette-accent-100);   
  --ds-color-expansion-panel-collaps-disable-background-info: var(--ds-color-brand-accent-lightest);   
  --ds-color-expansion-panel-content-text-color-disable: var(--ds-color-text-disable);   
  --ds-color-expansion-panel-expand-background: var(--ds-color-surface-default);   
  --ds-elements-datepicker-border-radius: var(--ds-radius-circular);   
  --ds-elements-datepicker-border-size: var(--ds-stroke-0-25x);   
  --ds-elements-datepicker-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-elements-datepicker-cell-pad-left: var(--ds-space-2-5x);   
  --ds-elements-datepicker-cell-pad-right: var(--ds-space-2-5x);   
  --ds-elements-datepicker-cell-pad-top: var(--ds-space-2x);   
  --ds-elements-datepicker-cell-pad-bottom: var(--ds-space-2x);   
  --ds-elements-datepicker-cell-text-size: var(--ds-typography-body-font-size-m);   
  --ds-elements-datepicker-year-pad-left: var(--ds-space-4x);   
  --ds-elements-datepicker-year-pad-right: var(--ds-space-4x);   
  --ds-elements-datepicker-year-pad-top: var(--ds-space-2x);   
  --ds-elements-datepicker-year-pad-bottom: var(--ds-space-2x);   
  --ds-elements-datepicker-year-text-size: var(--ds-typography-body-font-size-m);   
  --ds-elements-datepicker-month-pad-left: var(--ds-space-2x);   
  --ds-elements-datepicker-month-pad-right: var(--ds-space-1x);   
  --ds-elements-datepicker-month-pad-top: var(--ds-space-2-5x);   
  --ds-elements-datepicker-month-pad-bottom: var(--ds-space-2-5x);   
  --ds-elements-datepicker-month-gap: var(--ds-space-2x);   
  --ds-elements-datepicker-month-text-size: var(--ds-typography-body-font-size-s);   
  --ds-elements-datepicker-month-icon-size: var(--ds-icon-size-size-5x);   
  --ds-color-elements-datepicker-cell-text-color: var(--ds-color-text-primary);   
  --ds-color-elements-datepicker-cell-default-default-background: var(--ds-palette-neutral-transparent);   
  --ds-color-elements-datepicker-cell-default-hover-background: var(--ds-color-brand-neutral-super-light);   
  --ds-color-elements-datepicker-cell-default-press-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-datepicker-cell-default-disable-background: var(--ds-palette-neutral-transparent);   
  --ds-color-elements-datepicker-cell-default-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-elements-datepicker-cell-today-border-color: var(--ds-color-stroke-hover);   
  --ds-color-elements-datepicker-cell-today-default-background: var(--ds-color-brand-neutral-default);   
  --ds-color-elements-datepicker-cell-today-hover-background: var(--ds-color-brand-neutral-super-light);   
  --ds-color-elements-datepicker-cell-today-press-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-datepicker-cell-today-disable-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-datepicker-cell-today-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-elements-datepicker-cell-selected-text-color: var(--ds-color-text-inversive);   
  --ds-color-elements-datepicker-cell-selected-default-background: var(--ds-color-button-accent-filled-default-background);   
  --ds-color-elements-datepicker-cell-selected-hover-background: var(--ds-color-button-accent-filled-hover-background);   
  --ds-color-elements-datepicker-cell-selected-press-background: var(--ds-color-button-accent-filled-press-background);   
  --ds-color-elements-datepicker-cell-range-default-background: var(--ds-color-brand-neutral-default);   
  --ds-color-elements-datepicker-cell-range-press-state-layer: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-datepicker-cell-range-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-elements-datepicker-year-default-text-color: var(--ds-color-text-primary);   
  --ds-color-elements-datepicker-year-default-default-background: var(--ds-color-brand-neutral-default);   
  --ds-color-elements-datepicker-year-default-hover-background: var(--ds-color-brand-neutral-super-light);   
  --ds-color-elements-datepicker-year-default-press-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-datepicker-year-default-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-elements-datepicker-year-today-border-color: var(--ds-color-stroke-hover);   
  --ds-color-elements-datepicker-year-today-text-color: var(--ds-color-text-primary);   
  --ds-color-elements-datepicker-year-today-default-background: var(--ds-color-brand-neutral-default);   
  --ds-color-elements-datepicker-year-today-hover-background: var(--ds-color-brand-neutral-super-light);   
  --ds-color-elements-datepicker-year-today-press-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-datepicker-year-today-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-elements-datepicker-year-selected-text-color: var(--ds-color-text-inversive);   
  --ds-color-elements-datepicker-year-selected-default-background: var(--ds-color-button-accent-filled-default-background);   
  --ds-color-elements-datepicker-year-selected-hover-background: var(--ds-color-button-accent-filled-hover-background);   
  --ds-color-elements-datepicker-year-selected-press-background: var(--ds-color-button-accent-filled-press-background);   
  --ds-color-elements-datepicker-month-text-color: var(--ds-color-text-primary);   
  --ds-color-elements-datepicker-month-icon-color: var(--ds-color-icon-primary);   
  --ds-color-elements-datepicker-month-default-default-background: var(--ds-color-brand-neutral-default);   
  --ds-color-elements-datepicker-month-default-hover-background: var(--ds-color-brand-neutral-super-light);   
  --ds-color-elements-datepicker-month-default-press-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-datepicker-month-default-disable-text-color: var(--ds-color-text-disable);   
  --ds-color-elements-datepicker-month-default-disable-icon-color: var(--ds-color-icon-disable);   
  --ds-elements-datepicker-year-selected-gap: var(--ds-space-2x);   
  --ds-input-datepicker-icon: date_range;   
  --ds-input-datepicker-empty-placeholder-text: ДД.ММ.ГГГГ;   
  --ds-input-datepicker-populated-label-text: Дата;   
  --ds-input-datepicker-populated-placeholder-text: ДД.ММ.ГГГГ;   
  --ds-control-panel-datepicker-pad-top: var(--ds-space-1x);   
  --ds-control-panel-datepicker-pad-bottom: var(--ds-space-1x);   
  --ds-control-panel-datepicker-control-gap: Auto;   
  --ds-control-panel-datepicker-week-pad-top: var(--ds-space-0-5x);   
  --ds-control-panel-datepicker-week-pad-bottom: var(--ds-space-0-5x);   
  --ds-datepicker-pad-top: var(--ds-space-2x);   
  --ds-datepicker-pad-bottom: var(--ds-space-2x);   
  --ds-datepicker-pad-left: var(--ds-space-4x);   
  --ds-datepicker-pad-right: var(--ds-space-4x);   
  --ds-datepicker-border-radius: var(--ds-radius-3x);   
  --ds-datepicker-border-size: var(--ds-stroke-0-25x);   
  --ds-color-datepicker-border-color: var(--ds-color-stroke-default);   
  --ds-input-timepicker-icon: schedule_time;   
  --ds-input-timepicker-empty-placeholder-text: ЧЧ.ММ;   
  --ds-input-timepicker-populated-label-text: Время;   
  --ds-input-timepicker-populated-placeholder-text: ЧЧ.ММ;   
  --ds-elements-timepicker-border-radius: var(--ds-radius-circular);   
  --ds-elements-timepicker-text-weight: var(--ds-typography-font-weight-regular);   
  --ds-elements-timepicker-pad-left: var(--ds-space-4x);   
  --ds-elements-timepicker-pad-right: var(--ds-space-4x);   
  --ds-elements-timepicker-pad-top: var(--ds-space-2x);   
  --ds-elements-timepicker-pad-bottom: var(--ds-space-2x);   
  --ds-elements-timepicker-text-size: var(--ds-typography-body-font-size-m);   
  --ds-color-elements-timepicker-selected-text-color: var(--ds-color-text-inversive);   
  --ds-color-elements-timepicker-selected-default-background: var(--ds-color-button-accent-filled-default-background);   
  --ds-color-elements-timepicker-selected-hover-background: var(--ds-color-button-accent-filled-hover-background);   
  --ds-color-elements-timepicker-selected-press-background: var(--ds-color-button-accent-filled-press-background);   
  --ds-color-elements-timepicker-default-text-color: var(--ds-color-text-primary);   
  --ds-color-elements-timepicker-default-default-background: var(--ds-color-brand-neutral-default);   
  --ds-color-elements-timepicker-default-hover-background: var(--ds-color-brand-neutral-super-light);   
  --ds-color-elements-timepicker-default-press-background: var(--ds-color-brand-neutral-lighter);   
  --ds-color-elements-timepicker-default-range-background: var(--ds-palette-accent-50);   
  --ds-color-elements-timepicker-default-disable-text-color: var(--ds-color-text-disable);   
  --ds-control-panel-timepicker-pad-top: var(--ds-space-1x);   
  --ds-control-panel-timepicker-pad-bottom: var(--ds-space-1x);   
  --ds-control-panel-timepicker-control-gap: Auto;   
  --ds-control-panel-timepicker-time-pad-top: var(--ds-space-0-5x);   
  --ds-control-panel-timepicker-time-pad-bottom: var(--ds-space-0-5x);   
  --ds-timepicker-time-grid-pad-top: var(--ds-space-2x);   
  --ds-timepicker-time-grid-pad-bottom: var(--ds-space-2x);   
  --ds-timepicker-time-grid-border-radius: var(--ds-radius-3x);   
  --ds-timepicker-time-grid-border-size: var(--ds-stroke-0-25x);   
  --ds-color-timepicker-time-grid-border-color: var(--ds-color-stroke-default);   
  --ds-timepicker-time-line-component: Select (Container);   

  
  --ds-color-chips-input-background-support: rgba(255, 255, 255, 0.0);
  --ds-color-chips-input-default-action-text-color: #616161;
  --ds-color-chips-input-default-background: #f8f9fc;
  --ds-color-chips-input-default-border-color: #e0e0e0;
  --ds-color-chips-input-default-label-text-color: #616161;
  --ds-color-chips-input-default-support-text-color: #616161;
  --ds-color-chips-input-disable-action-text-color: #9e9e9e;
  --ds-color-chips-input-disable-background: #f5f5f5;
  --ds-color-chips-input-disable-border-color: #ebebeb;
  --ds-color-chips-input-disable-icon-color: #9e9e9e;
  --ds-color-chips-input-disable-label-text-color: #9e9e9e;
  --ds-color-chips-input-disable-support-text-color: #9e9e9e;
  --ds-color-chips-input-error-action-text-color: #616161;
  --ds-color-chips-input-error-background: #f8f9fc;
  --ds-color-chips-input-error-background-hover: #f5f5f5;
  --ds-color-chips-input-error-border-color: #ff5252;
  --ds-color-chips-input-error-cursor-color: #333333;
  --ds-color-chips-input-error-icon-color: #ff5252;
  --ds-color-chips-input-error-label-text-color: #ff5252;
  --ds-color-chips-input-error-support-text-color: #ff5252;
  --ds-color-chips-input-error-text-placeholder-color: #d6d6d6;
  --ds-color-chips-input-focus-background: #f8f9fc;
  --ds-color-chips-input-focus-border-color: #448aff;
  --ds-color-chips-input-focus-label-text-color: #448aff;
  --ds-color-chips-input-focus-support-text-color: #616161;
  --ds-color-chips-input-focus-text-color: #333333;
  --ds-color-chips-input-focus-text-placeholder-color: #d6d6d6;
  --ds-color-chips-input-hover-action-text-color: #616161;
  --ds-color-chips-input-hover-background: #f5f5f5;
  --ds-color-chips-input-hover-border-color: #9e9e9e;
  --ds-color-chips-input-hover-label-text-color: #616161;
  --ds-color-chips-input-hover-support-text-color: #616161;
  --ds-color-expansion-panel-block-collaps-border-color: #e0e0e0;
  --ds-color-expansion-panel-block-collaps-content-background: #ffffff;
  --ds-color-expansion-panel-block-collaps-content-text-color: #333333;
  --ds-color-expansion-panel-block-expand-header-border-color: #e0e0e0;
  --ds-color-expansion-panel-block-expand-header-icon-color: #616161;
  --ds-color-expansion-panel-block-expand-header-text-color: #333333;
  --ds-color-expansion-panel-block-expand-header-default-background: #f8f9fc;
  --ds-color-expansion-panel-block-expand-header-disable-background: #f5f5f5;
  --ds-color-expansion-panel-block-expand-header-disable-border-color: #ebebeb;
  --ds-color-expansion-panel-block-expand-header-disable-text-color: #9e9e9e;
  --ds-color-expansion-panel-block-expand-header-hover-background: #f5f5f5;
  --ds-color-expansion-panel-block-expand-header-press-background: #e0e0e0;
  --ds-color-input-background-support: rgba(255, 255, 255, 0.0);
  --ds-color-input-input-filled-background: #f8f9fc;
  --ds-color-input-input-label-text-color: #616161;
  --ds-color-input-input-outlined-background: #ffffff;
  --ds-color-input-filled-default-border-color: #e0e0e0;
  --ds-color-input-filled-default-icon-color-default: #616161;
  --ds-color-input-filled-default-icon-color-warning: #ea7806;
  --ds-color-input-filled-default-input-text-color: #333333;
  --ds-color-input-filled-default-label-text-color: #616161;
  --ds-color-input-filled-default-support-text-color: #616161;
  --ds-color-input-filled-disable-border-color: #ebebeb;
  --ds-color-input-filled-disable-icon-color-disable: #9e9e9e;
  --ds-color-input-filled-disable-icon-color-warning: #ea7806;
  --ds-color-input-filled-disable-input-background: #f5f5f5;
  --ds-color-input-filled-disable-input-text-color: #9e9e9e;
  --ds-color-input-filled-disable-label-text-color: #9e9e9e;
  --ds-color-input-filled-disable-support-text-color: #9e9e9e;
  --ds-color-input-filled-error-border-color: #ff5252;
  --ds-color-input-filled-error-icon-color-default: #616161;
  --ds-color-input-filled-error-icon-color-error: #ff5252;
  --ds-color-input-filled-error-icon-color-warning: #ea7806;
  --ds-color-input-filled-error-input-background-hover: #f5f5f5;
  --ds-color-input-filled-error-input-cursor-color: #333333;
  --ds-color-input-filled-error-input-text-color: #333333;
  --ds-color-input-filled-error-input-text-placeholder-color: #d6d6d6;
  --ds-color-input-filled-error-label-text-color: #ff5252;
  --ds-color-input-filled-error-text-support-color: #ff5252;
  --ds-color-input-filled-focus-border-color: #448aff;
  --ds-color-input-filled-focus-icon-color-default: #616161;
  --ds-color-input-filled-focus-icon-color-warning: #ea7806;
  --ds-color-input-filled-focus-input-cursor-color: #333333;
  --ds-color-input-filled-focus-input-text-color: #333333;
  --ds-color-input-filled-focus-input-text-placeholder-color: #d6d6d6;
  --ds-color-input-filled-focus-label-text-color: #448aff;
  --ds-color-input-filled-focus-support-text-color: #616161;
  --ds-color-input-filled-hover-border-color: #9e9e9e;
  --ds-color-input-filled-hover-icon-color-default: #616161;
  --ds-color-input-filled-hover-icon-color-warning: #ea7806;
  --ds-color-input-filled-hover-input-background-hover: #f5f5f5;
  --ds-color-input-filled-hover-input-text-color: #333333;
  --ds-color-input-filled-hover-label-text-color: #616161;
  --ds-color-input-filled-hover-text-support-color: #616161;
  --ds-color-input-outlined-default-background: #ffffff;
  --ds-color-input-outlined-default-border-color: #e0e0e0;
  --ds-color-input-outlined-default-icon-color: #616161;
  --ds-color-input-outlined-default-text-color: #333333;
  --ds-color-input-outlined-error-background: #ebebeb;
  --ds-color-input-outlined-error-border-color: #e0e0e0;
  --ds-color-input-outlined-error-icon-color: #616161;
  --ds-color-input-outlined-error-text-color: #333333;
  --ds-color-input-outlined-focus-background: #ebebeb;
  --ds-color-input-outlined-focus-border-color: #e0e0e0;
  --ds-color-input-outlined-focus-icon-color: #616161;
  --ds-color-input-outlined-focus-text-color: #333333;
  --ds-color-input-outlined-hover-background: #fafafa;
  --ds-color-input-outlined-hover-border-color: #e0e0e0;
  --ds-color-input-outlined-hover-icon-color: #616161;
  --ds-color-input-outlined-hover-text-color: #333333;
  --ds-color-search-focus-value-border-color: #448aff;
  --ds-color-search-focus-value-text-color: #333333;
  --ds-color-snackbar-dark-background: #424242;
  --ds-color-snackbar-dark-text-color: #ffffff;
  --ds-color-snackbar-dark-complex-accent-icon-color: #448aff;
  --ds-color-snackbar-dark-complex-negative-icon-color: #ff5252;
  --ds-color-snackbar-dark-complex-neutral-icon-color: #ffffff;
  --ds-color-snackbar-dark-complex-positive-icon-color: #14b456;
  --ds-color-snackbar-dark-complex-warning-icon-color: #ea7806;
  --ds-color-snackbar-dark-single-accent-icon-color: #448aff;
  --ds-color-snackbar-dark-single-negative-icon-color: #ff5252;
  --ds-color-snackbar-dark-single-neutral-icon-color: #ffffff;
  --ds-color-snackbar-dark-single-positive-icon-color: #14b456;
  --ds-color-snackbar-dark-single-warning-icon-color: #ea7806;
  --ds-color-snackbar-light-background: #ffffff;
  --ds-color-snackbar-light-text-color: #333333;
  --ds-color-snackbar-light-complex-accent-icon-color: #448aff;
  --ds-color-snackbar-light-complex-negative-icon-color: #ff5252;
  --ds-color-snackbar-light-complex-neutral-icon-color: #616161;
  --ds-color-snackbar-light-complex-positive-icon-color: #14b456;
  --ds-color-snackbar-light-complex-warning-icon-color: #ea7806;
  --ds-color-snackbar-light-single-accent-icon-color: #448aff;
  --ds-color-snackbar-light-single-negative-icon-color: #ff5252;
  --ds-color-snackbar-light-single-neutral-icon-color: #616161;
  --ds-color-snackbar-light-single-positive-icon-color: #14b456;
  --ds-color-snackbar-light-single-warning-icon-color: #ea7806;
  --ds-color-tab-active-counter-text-color: #448aff;
  --ds-color-tab-active-divider: #448aff;
  --ds-color-tab-innactive-counter-text-color: #333333;
  --ds-color-tab-innactive-icon-color: #616161;
  --ds-color-tab-innactive-text-color: #333333;
  --ds-color-tab-innactive-default-background: rgba(255, 255, 255, 0.0);
  --ds-color-tab-innactive-hover-background: #f5f5f5;
  --ds-color-tab-innactive-press-background: #e0e0e0;
  --ds-shadow-sl: 0px 2px 2px 0px rgba(33, 33, 33, 0.039), 0px 0px 4px 0px rgba(33, 33, 33, 0.122);
  --ds-shadow-s: 0px 4px 6px 0px rgba(33, 33, 33, 0.102), 0px 0px 16px 0px rgba(33, 33, 33, 0.122);
  --ds-shadow-m: 0px 10px 24px 0px rgba(33, 33, 33, 0.122), 0px 0px 28px 0px rgba(33, 33, 33, 0.122);
  --ds-shadow-xl: 0px 12px 16px 0px rgba(33, 33, 33, 0.161), 0px 0px 32px 0px rgba(33, 33, 33, 0.161);
}

:root {
  
  --ds-font-header-l-34-normal-regular: 400 34px/40px "Roboto";
  --ds-font-header-l-34-normal-regular-size: 34px;
  --ds-font-header-l-34-normal-regular-line: 40px;
  --ds-font-header-l-34-normal-regular-spacing: 0px;
  --ds-font-header-l-34-normal-regular-weight: 400;
  --ds-font-header-l-34-normal-medium: 500 34px/40px "Roboto";
  --ds-font-header-l-34-normal-medium-size: 34px;
  --ds-font-header-l-34-normal-medium-line: 40px;
  --ds-font-header-l-34-normal-medium-spacing: 0px;
  --ds-font-header-l-34-normal-medium-weight: 500;
  --ds-font-header-l-34-caps-regular: 400 34px/40px "Roboto";
  --ds-font-header-l-34-caps-regular-size: 34px;
  --ds-font-header-l-34-caps-regular-line: 40px;
  --ds-font-header-l-34-caps-regular-spacing: 0px;
  --ds-font-header-l-34-caps-regular-weight: 400;
  --ds-font-header-l-34-caps-medium: 500 34px/40px "Roboto";
  --ds-font-header-l-34-caps-medium-size: 34px;
  --ds-font-header-l-34-caps-medium-line: 40px;
  --ds-font-header-l-34-caps-medium-spacing: 0px;
  --ds-font-header-l-34-caps-medium-weight: 500;
  --ds-font-header-m-24-normal-regular: 400 24px/32px "Roboto";
  --ds-font-header-m-24-normal-regular-size: 24px;
  --ds-font-header-m-24-normal-regular-line: 32px;
  --ds-font-header-m-24-normal-regular-spacing: 0.5px;
  --ds-font-header-m-24-normal-regular-weight: 400;
  --ds-font-header-m-24-normal-medium: 500 24px/32px "Roboto";
  --ds-font-header-m-24-normal-medium-size: 24px;
  --ds-font-header-m-24-normal-medium-line: 32px;
  --ds-font-header-m-24-normal-medium-spacing: 0.5px;
  --ds-font-header-m-24-normal-medium-weight: 500;
  --ds-font-header-m-24-caps-regular: 400 24px/32px "Roboto";
  --ds-font-header-m-24-caps-regular-size: 24px;
  --ds-font-header-m-24-caps-regular-line: 32px;
  --ds-font-header-m-24-caps-regular-spacing: 0.5px;
  --ds-font-header-m-24-caps-regular-weight: 400;
  --ds-font-header-m-24-caps-medium: 500 24px/32px "Roboto";
  --ds-font-header-m-24-caps-medium-size: 24px;
  --ds-font-header-m-24-caps-medium-line: 32px;
  --ds-font-header-m-24-caps-medium-spacing: 0.5px;
  --ds-font-header-m-24-caps-medium-weight: 500;
  --ds-font-header-s-20-normal-regular: 400 20px/28px "Roboto";
  --ds-font-header-s-20-normal-regular-size: 20px;
  --ds-font-header-s-20-normal-regular-line: 28px;
  --ds-font-header-s-20-normal-regular-spacing: 0.5px;
  --ds-font-header-s-20-normal-regular-weight: 400;
  --ds-font-header-s-20-normal-medium: 500 20px/28px "Roboto";
  --ds-font-header-s-20-normal-medium-size: 20px;
  --ds-font-header-s-20-normal-medium-line: 28px;
  --ds-font-header-s-20-normal-medium-spacing: 0.5px;
  --ds-font-header-s-20-normal-medium-weight: 500;
  --ds-font-header-s-20-caps-regular: 400 20px/28px "Roboto";
  --ds-font-header-s-20-caps-regular-size: 20px;
  --ds-font-header-s-20-caps-regular-line: 28px;
  --ds-font-header-s-20-caps-regular-spacing: 0.5px;
  --ds-font-header-s-20-caps-regular-weight: 400;
  --ds-font-header-s-20-caps-medium: 500 20px/28px "Roboto";
  --ds-font-header-s-20-caps-medium-size: 20px;
  --ds-font-header-s-20-caps-medium-line: 28px;
  --ds-font-header-s-20-caps-medium-spacing: 0.5px;
  --ds-font-header-s-20-caps-medium-weight: 500;
  --ds-font-body-l-18-normal-regular: 400 18px/24px "Roboto";
  --ds-font-body-l-18-normal-regular-size: 18px;
  --ds-font-body-l-18-normal-regular-line: 24px;
  --ds-font-body-l-18-normal-regular-spacing: 0.5px;
  --ds-font-body-l-18-normal-regular-weight: 400;
  --ds-font-body-l-18-normal-medium: 500 18px/24px "Roboto";
  --ds-font-body-l-18-normal-medium-size: 18px;
  --ds-font-body-l-18-normal-medium-line: 24px;
  --ds-font-body-l-18-normal-medium-spacing: 0.5px;
  --ds-font-body-l-18-normal-medium-weight: 500;
  --ds-font-body-l-18-caps-regular: 400 18px/24px "Roboto";
  --ds-font-body-l-18-caps-regular-size: 18px;
  --ds-font-body-l-18-caps-regular-line: 24px;
  --ds-font-body-l-18-caps-regular-spacing: 0.5px;
  --ds-font-body-l-18-caps-regular-weight: 400;
  --ds-font-body-l-18-caps-medium: 500 18px/24px "Roboto";
  --ds-font-body-l-18-caps-medium-size: 18px;
  --ds-font-body-l-18-caps-medium-line: 24px;
  --ds-font-body-l-18-caps-medium-spacing: 0.5px;
  --ds-font-body-l-18-caps-medium-weight: 500;
  --ds-font-body-m-16-normal-regular: 400 16px/24px "Roboto";
  --ds-font-body-m-16-normal-regular-size: 16px;
  --ds-font-body-m-16-normal-regular-line: 24px;
  --ds-font-body-m-16-normal-regular-spacing: 0.5px;
  --ds-font-body-m-16-normal-regular-weight: 400;
  --ds-font-body-m-16-normal-medium: 500 16px/24px "Roboto";
  --ds-font-body-m-16-normal-medium-size: 16px;
  --ds-font-body-m-16-normal-medium-line: 24px;
  --ds-font-body-m-16-normal-medium-spacing: 0.5px;
  --ds-font-body-m-16-normal-medium-weight: 500;
  --ds-font-body-m-16-caps-regular: 400 16px/24px "Roboto";
  --ds-font-body-m-16-caps-regular-size: 16px;
  --ds-font-body-m-16-caps-regular-line: 24px;
  --ds-font-body-m-16-caps-regular-spacing: 0.5px;
  --ds-font-body-m-16-caps-regular-weight: 400;
  --ds-font-body-m-16-caps-medium: 500 16px/24px "Roboto";
  --ds-font-body-m-16-caps-medium-size: 16px;
  --ds-font-body-m-16-caps-medium-line: 24px;
  --ds-font-body-m-16-caps-medium-spacing: 0.5px;
  --ds-font-body-m-16-caps-medium-weight: 500;
  --ds-font-body-s-14-normal-regular: 400 14px/20px "Roboto";
  --ds-font-body-s-14-normal-regular-size: 14px;
  --ds-font-body-s-14-normal-regular-line: 20px;
  --ds-font-body-s-14-normal-regular-spacing: 0.5px;
  --ds-font-body-s-14-normal-regular-weight: 400;
  --ds-font-body-s-14-normal-medium: 500 14px/20px "Roboto";
  --ds-font-body-s-14-normal-medium-size: 14px;
  --ds-font-body-s-14-normal-medium-line: 20px;
  --ds-font-body-s-14-normal-medium-spacing: 0.5px;
  --ds-font-body-s-14-normal-medium-weight: 500;
  --ds-font-body-s-14-caps-regular: 400 14px/20px "Roboto";
  --ds-font-body-s-14-caps-regular-size: 14px;
  --ds-font-body-s-14-caps-regular-line: 20px;
  --ds-font-body-s-14-caps-regular-spacing: 0.5px;
  --ds-font-body-s-14-caps-regular-weight: 400;
  --ds-font-body-s-14-caps-medium: 500 14px/20px "Roboto";
  --ds-font-body-s-14-caps-medium-size: 14px;
  --ds-font-body-s-14-caps-medium-line: 20px;
  --ds-font-body-s-14-caps-medium-spacing: 0.5px;
  --ds-font-body-s-14-caps-medium-weight: 500;
  --ds-font-caption-l-12-normal-regular: 400 12px/16px "Roboto";
  --ds-font-caption-l-12-normal-regular-size: 12px;
  --ds-font-caption-l-12-normal-regular-line: 16px;
  --ds-font-caption-l-12-normal-regular-spacing: 0.5px;
  --ds-font-caption-l-12-normal-regular-weight: 400;
  --ds-font-caption-l-12-normal-medium: 500 12px/16px "Roboto";
  --ds-font-caption-l-12-normal-medium-size: 12px;
  --ds-font-caption-l-12-normal-medium-line: 16px;
  --ds-font-caption-l-12-normal-medium-spacing: 0.5px;
  --ds-font-caption-l-12-normal-medium-weight: 500;
  --ds-font-caption-l-12-caps-regular: 400 12px/16px "Roboto";
  --ds-font-caption-l-12-caps-regular-size: 12px;
  --ds-font-caption-l-12-caps-regular-line: 16px;
  --ds-font-caption-l-12-caps-regular-spacing: 0.5px;
  --ds-font-caption-l-12-caps-regular-weight: 400;
  --ds-font-caption-l-12-caps-medium: 500 12px/16px "Roboto";
  --ds-font-caption-l-12-caps-medium-size: 12px;
  --ds-font-caption-l-12-caps-medium-line: 16px;
  --ds-font-caption-l-12-caps-medium-spacing: 0.5px;
  --ds-font-caption-l-12-caps-medium-weight: 500;
  --ds-font-caption-m-10-normal-regular: 400 10px/12px "Roboto";
  --ds-font-caption-m-10-normal-regular-size: 10px;
  --ds-font-caption-m-10-normal-regular-line: 12px;
  --ds-font-caption-m-10-normal-regular-spacing: 0.5px;
  --ds-font-caption-m-10-normal-regular-weight: 400;
  --ds-font-caption-m-10-normal-medium: 500 10px/12px "Roboto";
  --ds-font-caption-m-10-normal-medium-size: 10px;
  --ds-font-caption-m-10-normal-medium-line: 12px;
  --ds-font-caption-m-10-normal-medium-spacing: 0.5px;
  --ds-font-caption-m-10-normal-medium-weight: 500;
  --ds-font-caption-m-10-caps-regular: 400 10px/12px "Roboto";
  --ds-font-caption-m-10-caps-regular-size: 10px;
  --ds-font-caption-m-10-caps-regular-line: 12px;
  --ds-font-caption-m-10-caps-regular-spacing: 0.5px;
  --ds-font-caption-m-10-caps-regular-weight: 400;
  --ds-font-caption-m-10-caps-medium: 500 10px/12px "Roboto";
  --ds-font-caption-m-10-caps-medium-size: 10px;
  --ds-font-caption-m-10-caps-medium-line: 12px;
  --ds-font-caption-m-10-caps-medium-spacing: 0.5px;
  --ds-font-caption-m-10-caps-medium-weight: 500;
  --ds-font-caption-s-8-normal-regular: 400 8px/10px "Roboto";
  --ds-font-caption-s-8-normal-regular-size: 8px;
  --ds-font-caption-s-8-normal-regular-line: 10px;
  --ds-font-caption-s-8-normal-regular-spacing: 0.5px;
  --ds-font-caption-s-8-normal-regular-weight: 400;
  --ds-font-caption-s-8-normal-medium: 500 8px/10px "Roboto";
  --ds-font-caption-s-8-normal-medium-size: 8px;
  --ds-font-caption-s-8-normal-medium-line: 10px;
  --ds-font-caption-s-8-normal-medium-spacing: 0.5px;
  --ds-font-caption-s-8-normal-medium-weight: 500;
  --ds-font-caption-s-8-caps-regular: 400 8px/10px "Roboto";
  --ds-font-caption-s-8-caps-regular-size: 8px;
  --ds-font-caption-s-8-caps-regular-line: 10px;
  --ds-font-caption-s-8-caps-regular-spacing: 0.5px;
  --ds-font-caption-s-8-caps-regular-weight: 400;
  --ds-font-caption-s-8-caps-medium: 500 8px/10px "Roboto";
  --ds-font-caption-s-8-caps-medium-size: 8px;
  --ds-font-caption-s-8-caps-medium-line: 10px;
  --ds-font-caption-s-8-caps-medium-spacing: 0.5px;
  --ds-font-caption-s-8-caps-medium-weight: 500;
  
  --ds-shadow-shadows-none: 0px 2px 0px 0px #ffffff;
  --ds-shadow-shadows-01-dp-sl: 0px 0px 4px 0px rgba(33, 33, 33, 0.12), 0px 2px 2px 0px rgba(33, 33, 33, 0.04);
  --ds-shadow-shadows-08-dp-s: 0px 0px 16px 0px rgba(33, 33, 33, 0.12), 0px 4px 6px 0px rgba(33, 33, 33, 0.1);
  --ds-shadow-shadows-12-dp-m: 0px 0px 28px 0px rgba(33, 33, 33, 0.12), 0px 10px 24px 0px rgba(33, 33, 33, 0.12);
  --ds-shadow-shadows-24-dp-xl: 0px 0px 32px 0px rgba(33, 33, 33, 0.16), 0px 12px 16px 0px rgba(33, 33, 33, 0.16);
  
  --ds-paint-surface-default: #ffffff;
  --ds-paint-surface-default-v2: #f8f9fc;
  --ds-paint-surface-hover: #f5f5f5;
  --ds-paint-surface-selected: #ebebeb;
  --ds-paint-surface-press: #e0e0e0;
  --ds-paint-surface-disable: #e0e0e0;
  --ds-paint-surface-snacktooltip: #424242;
  --ds-paint-surface-sidebar: #f8f9fc;
  --ds-paint-surface-sidebar-selected: #f0f5ff;
  --ds-paint-surface-sidebar-active: #a8c9ff;
  --ds-paint-table-surfase-default: #ffffff;
  --ds-paint-table-surfase-hover: #f5f5f5;
  --ds-paint-table-surfase-selected: #ebebeb;
  --ds-paint-table-surfase-group: #ebebeb;
  --ds-paint-table-surfase-head: #f0f5ff;
  --ds-paint-table-surfase-head-group: #a8c9ff;
  --ds-paint-text-primary: #333333;
  --ds-paint-text-inversive: #ffffff;
  --ds-paint-text-caption: #616161;
  --ds-paint-text-placeholder: #d6d6d6;
  --ds-paint-text-disable: #9e9e9e;
  --ds-paint-text-accent: #448aff;
  --ds-paint-text-positive: #14b456;
  --ds-paint-text-warning: #ffab40;
  --ds-paint-text-negative: #ff5252;
  --ds-paint-button-neutral-default: #ffffff;
  --ds-paint-button-neutral-hover: #f5f5f5;
  --ds-paint-button-neutral-press: #ebebeb;
  --ds-paint-button-neutral-disable: #ebebeb;
  --ds-paint-button-accent-default: #448aff;
  --ds-paint-button-accent-hover: #3969d5;
  --ds-paint-button-accent-press: #2651b5;
  --ds-paint-button-positive-default: #14b456;
  --ds-paint-button-positive-hover: #0f852c;
  --ds-paint-button-positive-press: #0a571a;
  --ds-paint-button-warning-default: #ffab40;
  --ds-paint-button-warning-hover: #ea7806;
  --ds-paint-button-warning-press: #994000;
  --ds-paint-button-negative-default: #ff5252;
  --ds-paint-button-negative-hover: #de1a12;
  --ds-paint-button-negative-press: #7f0f0a;
  --ds-paint-icon-primary: #616161;
  --ds-paint-icon-inversive: #ffffff;
  --ds-paint-icon-disable: #9e9e9e;
  --ds-paint-icon-accent: #448aff;
  --ds-paint-icon-positive: #14b456;
  --ds-paint-icon-warning: #ea7806;
  --ds-paint-icon-negative: #ff5252;
  --ds-paint-shapes-default: #ffffff;
  --ds-paint-shapes-superlight-nt: #f5f5f5;
  --ds-paint-shapes-lightest-nt: #ebebeb;
  --ds-paint-shapes-lighter-nt: #e0e0e0;
  --ds-paint-shapes-lighter-pr: #f8f9fc;
  --ds-paint-shapes-lighter-sc: #ebfbf2;
  --ds-paint-shapes-lighter-wr: #fff9f0;
  --ds-paint-shapes-lighter-er: #fff2f2;
  --ds-paint-shapes-lightest-mg: #fbf7fc;
  --ds-paint-shapes-lightest-br: #f7e9e3;
  --ds-paint-shapes-lightest-db: #f9fafb;
  --ds-paint-stroke-default: #e0e0e0;
  --ds-paint-stroke-hover: #9e9e9e;
  --ds-paint-stroke-disable: #ebebeb;
  --ds-paint-stroke-primary: #448aff;
  --ds-paint-stroke-secondary: #14b456;
  --ds-paint-stroke-warning: #ffab40;
  --ds-paint-stroke-error: #ff5252;
}

.ds-text-header-l-34-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-l-34-normal-regular-size);
  line-height: var(--ds-font-header-l-34-normal-regular-line);
  letter-spacing: var(--ds-font-header-l-34-normal-regular-spacing);
  font-weight: var(--ds-font-header-l-34-normal-regular-weight);
}
.ds-text-header-l-34-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-l-34-normal-medium-size);
  line-height: var(--ds-font-header-l-34-normal-medium-line);
  letter-spacing: var(--ds-font-header-l-34-normal-medium-spacing);
  font-weight: var(--ds-font-header-l-34-normal-medium-weight);
}
.ds-text-header-l-34-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-l-34-caps-regular-size);
  line-height: var(--ds-font-header-l-34-caps-regular-line);
  letter-spacing: var(--ds-font-header-l-34-caps-regular-spacing);
  font-weight: var(--ds-font-header-l-34-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-header-l-34-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-l-34-caps-medium-size);
  line-height: var(--ds-font-header-l-34-caps-medium-line);
  letter-spacing: var(--ds-font-header-l-34-caps-medium-spacing);
  font-weight: var(--ds-font-header-l-34-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-header-m-24-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-m-24-normal-regular-size);
  line-height: var(--ds-font-header-m-24-normal-regular-line);
  letter-spacing: var(--ds-font-header-m-24-normal-regular-spacing);
  font-weight: var(--ds-font-header-m-24-normal-regular-weight);
}
.ds-text-header-m-24-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-m-24-normal-medium-size);
  line-height: var(--ds-font-header-m-24-normal-medium-line);
  letter-spacing: var(--ds-font-header-m-24-normal-medium-spacing);
  font-weight: var(--ds-font-header-m-24-normal-medium-weight);
}
.ds-text-header-m-24-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-m-24-caps-regular-size);
  line-height: var(--ds-font-header-m-24-caps-regular-line);
  letter-spacing: var(--ds-font-header-m-24-caps-regular-spacing);
  font-weight: var(--ds-font-header-m-24-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-header-m-24-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-m-24-caps-medium-size);
  line-height: var(--ds-font-header-m-24-caps-medium-line);
  letter-spacing: var(--ds-font-header-m-24-caps-medium-spacing);
  font-weight: var(--ds-font-header-m-24-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-header-s-20-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-s-20-normal-regular-size);
  line-height: var(--ds-font-header-s-20-normal-regular-line);
  letter-spacing: var(--ds-font-header-s-20-normal-regular-spacing);
  font-weight: var(--ds-font-header-s-20-normal-regular-weight);
}
.ds-text-header-s-20-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-s-20-normal-medium-size);
  line-height: var(--ds-font-header-s-20-normal-medium-line);
  letter-spacing: var(--ds-font-header-s-20-normal-medium-spacing);
  font-weight: var(--ds-font-header-s-20-normal-medium-weight);
}
.ds-text-header-s-20-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-s-20-caps-regular-size);
  line-height: var(--ds-font-header-s-20-caps-regular-line);
  letter-spacing: var(--ds-font-header-s-20-caps-regular-spacing);
  font-weight: var(--ds-font-header-s-20-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-header-s-20-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-header-s-20-caps-medium-size);
  line-height: var(--ds-font-header-s-20-caps-medium-line);
  letter-spacing: var(--ds-font-header-s-20-caps-medium-spacing);
  font-weight: var(--ds-font-header-s-20-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-body-l-18-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-l-18-normal-regular-size);
  line-height: var(--ds-font-body-l-18-normal-regular-line);
  letter-spacing: var(--ds-font-body-l-18-normal-regular-spacing);
  font-weight: var(--ds-font-body-l-18-normal-regular-weight);
}
.ds-text-body-l-18-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-l-18-normal-medium-size);
  line-height: var(--ds-font-body-l-18-normal-medium-line);
  letter-spacing: var(--ds-font-body-l-18-normal-medium-spacing);
  font-weight: var(--ds-font-body-l-18-normal-medium-weight);
}
.ds-text-body-l-18-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-l-18-caps-regular-size);
  line-height: var(--ds-font-body-l-18-caps-regular-line);
  letter-spacing: var(--ds-font-body-l-18-caps-regular-spacing);
  font-weight: var(--ds-font-body-l-18-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-body-l-18-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-l-18-caps-medium-size);
  line-height: var(--ds-font-body-l-18-caps-medium-line);
  letter-spacing: var(--ds-font-body-l-18-caps-medium-spacing);
  font-weight: var(--ds-font-body-l-18-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-body-m-16-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
}
.ds-text-body-m-16-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-m-16-normal-medium-size);
  line-height: var(--ds-font-body-m-16-normal-medium-line);
  letter-spacing: var(--ds-font-body-m-16-normal-medium-spacing);
  font-weight: var(--ds-font-body-m-16-normal-medium-weight);
}
.ds-text-body-m-16-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-m-16-caps-regular-size);
  line-height: var(--ds-font-body-m-16-caps-regular-line);
  letter-spacing: var(--ds-font-body-m-16-caps-regular-spacing);
  font-weight: var(--ds-font-body-m-16-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-body-m-16-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-m-16-caps-medium-size);
  line-height: var(--ds-font-body-m-16-caps-medium-line);
  letter-spacing: var(--ds-font-body-m-16-caps-medium-spacing);
  font-weight: var(--ds-font-body-m-16-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-body-s-14-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
}
.ds-text-body-s-14-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
}
.ds-text-body-s-14-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-s-14-caps-regular-size);
  line-height: var(--ds-font-body-s-14-caps-regular-line);
  letter-spacing: var(--ds-font-body-s-14-caps-regular-spacing);
  font-weight: var(--ds-font-body-s-14-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-body-s-14-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-body-s-14-caps-medium-size);
  line-height: var(--ds-font-body-s-14-caps-medium-line);
  letter-spacing: var(--ds-font-body-s-14-caps-medium-spacing);
  font-weight: var(--ds-font-body-s-14-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-caption-l-12-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
}
.ds-text-caption-l-12-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-l-12-normal-medium-size);
  line-height: var(--ds-font-caption-l-12-normal-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-medium-weight);
}
.ds-text-caption-l-12-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-l-12-caps-regular-size);
  line-height: var(--ds-font-caption-l-12-caps-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-caps-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-caption-l-12-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-l-12-caps-medium-size);
  line-height: var(--ds-font-caption-l-12-caps-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-caps-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-caption-m-10-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-m-10-normal-regular-size);
  line-height: var(--ds-font-caption-m-10-normal-regular-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-regular-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-regular-weight);
}
.ds-text-caption-m-10-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-m-10-normal-medium-size);
  line-height: var(--ds-font-caption-m-10-normal-medium-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-medium-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-medium-weight);
  text-transform: capitalize;
}
.ds-text-caption-m-10-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-m-10-caps-regular-size);
  line-height: var(--ds-font-caption-m-10-caps-regular-line);
  letter-spacing: var(--ds-font-caption-m-10-caps-regular-spacing);
  font-weight: var(--ds-font-caption-m-10-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-caption-m-10-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-m-10-caps-medium-size);
  line-height: var(--ds-font-caption-m-10-caps-medium-line);
  letter-spacing: var(--ds-font-caption-m-10-caps-medium-spacing);
  font-weight: var(--ds-font-caption-m-10-caps-medium-weight);
  text-transform: uppercase;
}
.ds-text-caption-s-8-normal-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-s-8-normal-regular-size);
  line-height: var(--ds-font-caption-s-8-normal-regular-line);
  letter-spacing: var(--ds-font-caption-s-8-normal-regular-spacing);
  font-weight: var(--ds-font-caption-s-8-normal-regular-weight);
}
.ds-text-caption-s-8-normal-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-s-8-normal-medium-size);
  line-height: var(--ds-font-caption-s-8-normal-medium-line);
  letter-spacing: var(--ds-font-caption-s-8-normal-medium-spacing);
  font-weight: var(--ds-font-caption-s-8-normal-medium-weight);
}
.ds-text-caption-s-8-caps-regular {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-s-8-caps-regular-size);
  line-height: var(--ds-font-caption-s-8-caps-regular-line);
  letter-spacing: var(--ds-font-caption-s-8-caps-regular-spacing);
  font-weight: var(--ds-font-caption-s-8-caps-regular-weight);
  text-transform: uppercase;
}
.ds-text-caption-s-8-caps-medium {
  font-family: "Roboto", sans-serif;
  font-size: var(--ds-font-caption-s-8-caps-medium-size);
  line-height: var(--ds-font-caption-s-8-caps-medium-line);
  letter-spacing: var(--ds-font-caption-s-8-caps-medium-spacing);
  font-weight: var(--ds-font-caption-s-8-caps-medium-weight);
  text-transform: uppercase;
}

```

### Стили компонентов

Порядок важен: сначала автоген всех компонентов, затем ВЫВЕРЕННЫЕ вручную файлы — они должны перекрывать автоген, а не наоборот.

```css

.ds-arrow {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow__icon svg path {
  fill: currentColor;
}
.ds-arrow__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}

.ds-arrow-list {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow-list__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow-list__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow-list__icon svg path {
  fill: currentColor;
}
.ds-arrow-list__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}

.ds-arrow-menu {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow-menu__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow-menu__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow-menu__icon svg path {
  fill: currentColor;
}
.ds-arrow-menu__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}

.ds-arrow-select {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-arrow-select__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-arrow-select__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-arrow-select__icon svg path {
  fill: currentColor;
}
.ds-arrow-select__drop-down {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}

.ds-autocomplete-form {
  min-height: 48px;
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-autocomplete-form__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-autocomplete-form__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-autocomplete-form__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-autocomplete-form__icon svg path {
  fill: currentColor;
}
.ds-autocomplete-form__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-autocomplete-form__input-frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-autocomplete-form__support {
  display: flex;
  flex-direction: row;
}
.ds-autocomplete-form--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-autocomplete-form--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-autocomplete-form--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-autocomplete-form--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-autocomplete-form--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-autocomplete-form--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-autocomplete-form--empty.ds-autocomplete-form--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-autocomplete-form--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-autocomplete-form--populated.ds-autocomplete-form--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-autocomplete-form--disabled {
  pointer-events: none;
}

.ds-backdrop {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-backdrop-background, #333333);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-button-toggle {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-toggle-gap, 4px);
  padding: var(--ds-button-toggle-pad-top, 4px) var(--ds-button-toggle-pad-right, 4px) var(--ds-button-toggle-pad-bottom, 4px) var(--ds-button-toggle-pad-left, 4px);
  border-radius: var(--ds-button-toggle-border-radius, 12px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-button-toggle__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-button-accent-outlined-default-text-color, #448aff);
  white-space: nowrap;
}
.ds-button-toggle__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-button-toggle__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-button-toggle__icon svg path {
  fill: currentColor;
}
.ds-button-toggle--s .ds-button-toggle__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-button-toggle--xs .ds-button-toggle__icon {
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
}
.ds-button-toggle--filled.ds-button-toggle--text {
  background: var(--ds-color-button-toggle-filled-background, #ffffff);
  color: var(--ds-color-button-accent-outlined-default-text-color, #448aff);
  border: none;
  box-shadow: none;
}
.ds-button-toggle--outlined.ds-button-toggle--text {
  background: var(--ds-color-button-toggle-outlined-background, #ffffff);
  border: 1px solid var(--ds-color-button-toggle-outlined-border-color, #e0e0e0);
  color: var(--ds-color-button-accent-filled-default-text-color, #ffffff);
  box-shadow: none;
}
.ds-button-toggle--outlined.ds-button-toggle--icon {
  background: var(--ds-color-button-toggle-outlined-background, #ffffff);
  border: 1px solid var(--ds-color-button-toggle-outlined-border-color, #e0e0e0);
}
.ds-button-toggle--filled.ds-button-toggle--icon {
  background: var(--ds-color-button-toggle-filled-background, #ffffff);
}

.ds-checkbox-label {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-checkbox-label-gap-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-checkbox-label__label {
  font-size: var(--ds-typography-font-size-3-5x);
  font-weight: var(--ds-typography-font-weight-regular);
  line-height: var(--ds-typography-line-height-5x);
  letter-spacing: 0.25px;
  color: var(--ds-color-checkbox-label-text-color, #333333);
  white-space: nowrap;
}
.ds-checkbox-label__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-checkbox-label__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-checkbox-label__icon svg path {
  fill: currentColor;
}
.ds-checkbox-label__form {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-checkbox-label-gap, 8px);
}
.ds-checkbox-label__left {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-checkbox-label__right {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-checkbox-label__support {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 var(--ds-checkbox-label-pad-left-support-7x, 28px);
}
.ds-checkbox-label__support-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-checkbox-label-text-support-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-checkbox-label-text-support-color, #616161);
}
.ds-checkbox-label--normal.ds-checkbox-label--deselected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--normal.ds-checkbox-label--selected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--normal.ds-checkbox-label--inderterminate {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--error.ds-checkbox-label--deselected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--error.ds-checkbox-label--selected {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--error.ds-checkbox-label--inderterminate {
  color: var(--ds-color-checkbox-label-text-color, #333333);
}
.ds-checkbox-label--disable.ds-checkbox-label--deselected {
  color: var(--ds-color-checkbox-label-text-disable-color, #9e9e9e);
}
.ds-checkbox-label--disable.ds-checkbox-label--selected {
  color: var(--ds-color-checkbox-label-text-disable-color, #9e9e9e);
}
.ds-checkbox-label--disable.ds-checkbox-label--inderterminate {
  color: var(--ds-color-checkbox-label-text-disable-color, #9e9e9e);
}

.ds-chips {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  height: var(--ds-size-8x);
  padding: var(--ds-chips-m-size-pad-top, 6px) var(--ds-chips-m-size-pad-right, 8px) var(--ds-chips-m-size-pad-bottom, 6px) var(--ds-chips-m-size-pad-left, 8px);
  gap: var(--ds-chips-m-size-gap, 8px);
  border-radius: var(--ds-chips-m-size-border-radius, 12px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-chips-text-color, #333333);
  white-space: nowrap;
}
.ds-chips__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips__icon svg path {
  fill: currentColor;
}
.ds-chips__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-chips__add {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-chips__chip-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
}
.ds-chips__chip-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-chips-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-chips-text-color, #333333);
}
.ds-chips__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-chips--s {
  gap: var(--ds-chips-s-size-gap, 4px);
  padding: var(--ds-chips-s-size-pad-top, 4px) var(--ds-chips-s-size-pad-right, 6px) var(--ds-chips-s-size-pad-bottom, 4px) var(--ds-chips-s-size-pad-left, 6px);
  border-radius: var(--ds-chips-s-size-border-radius, 8px);
}
.ds-chips--s .ds-chips__icon {
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
}
.ds-chips--outlined {
  background: var(--ds-color-chips-outlined-default-background, #ffffff);
  border: 1px solid var(--ds-color-chips-outlined-default-border-color, #e0e0e0);
  color: var(--ds-color-chips-text-color, #333333);
}
.ds-chips--outlined:hover {
  background: var(--ds-color-chips-outlined-hover-background, #ffffff);
  border: 1px solid var(--ds-color-chips-outlined-hover-border-color, #9e9e9e);
}
.ds-chips--outlined:focus-visible {
  background: var(--ds-color-chips-outlined-focus-background, #ffffff);
}
.ds-chips--outlined:active {
  background: var(--ds-color-chips-outlined-press-background, #e0e0e0);
  border: 1px solid var(--ds-color-chips-outlined-press-border-color, #e0e0e0);
}
.ds-chips--outlined:disabled {
  background: var(--ds-color-chips-disable-background-outlined, #ffffff);
  border: 1px solid var(--ds-color-chips-disable-border-color, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--outlined.ds-chips--disabled {
  background: var(--ds-color-chips-disable-background-outlined, #ffffff);
  border: 1px solid var(--ds-color-chips-disable-border-color, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--filled {
  background: var(--ds-color-chips-filled-default-background, #f8f9fc);
  color: var(--ds-color-chips-text-color, #333333);
}
.ds-chips--filled:hover {
  background: var(--ds-color-chips-filled-hover-background, #f5f5f5);
}
.ds-chips--filled:active {
  background: var(--ds-color-chips-filled-press-background, #e0e0e0);
}
.ds-chips--filled:disabled {
  background: var(--ds-color-chips-disable-background-filled, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--filled.ds-chips--disabled {
  background: var(--ds-color-chips-disable-background-filled, #ebebeb);
  color: var(--ds-color-chips-disable-text-color, #9e9e9e);
}
.ds-chips--disabled {
  pointer-events: none;
}

.ds-chips-group {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-chips-gap-group, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-group__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-chips-text-color, #333333);
  white-space: nowrap;
}
.ds-chips-group__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-group__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-group__icon svg path {
  fill: currentColor;
}
.ds-chips-group--s .ds-chips-group__icon {
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
}

.ds-chips-input {
  width: 280px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-1x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-input__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-chips-input__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-input__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-input__icon svg path {
  fill: currentColor;
}
.ds-chips-input__frame {
  display: flex;
  flex-direction: column;
  gap: var(--ds-chips-input-gap-chips-input-frame, 4px);
  padding: var(--ds-chips-input-m-size-pad-top, 4px) var(--ds-size-3x) var(--ds-chips-input-m-size-pad-bottom, 8px) var(--ds-size-3x);
  border-radius: var(--ds-size-3x);
  background: #f8f9fc;
  border: 1px solid #e0e0e0;
}
.ds-chips-input__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
}
.ds-chips-input__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-1x);
}
.ds-chips-input__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-size-3x) 0 var(--ds-size-3x);
}
.ds-chips-input__hint {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-size-3x) 0 var(--ds-size-3x);
}
.ds-chips-input--s {
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-chips-input--s .ds-chips-input__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-chips-input:hover {
  background: #f5f5f5;
  border: 1px solid #9e9e9e;
}
.ds-chips-input:focus-visible {
  color: #448aff;
}
.ds-chips-input:disabled {
  color: #9e9e9e;
}
.ds-chips-input.ds-chips-input--disabled {
  color: #9e9e9e;
}
.ds-chips-input--disabled {
  pointer-events: none;
}

.ds-chips-input-2 {
  width: 280px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-input-2__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-chips-input-2__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-input-2__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-input-2__icon svg path {
  fill: currentColor;
}
.ds-chips-input-2__frame {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-chips-input-2__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-content);
}
.ds-chips-input-2__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-chips-input-2__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-chips-input-2__hint {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-chips-input-2--s .ds-chips-input-2__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-chips-input-2:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-chips-input-2:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-chips-input-2:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-chips-input-2.ds-chips-input-2--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-chips-input-2--disabled {
  pointer-events: none;
}

.ds-chips-input-cell {
  min-height: var(--ds-size-10x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-chips-input-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-chips-input-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-chips-input-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-chips-input-cell__icon svg path {
  fill: currentColor;
}
.ds-chips-input-cell__frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-chips-input-gap-chips-input-frame, 4px);
  border-radius: var(--ds-size-3x);
  background: #f8f9fc;
  border: 1px solid #e0e0e0;
}
.ds-chips-input-cell__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-1x);
}
.ds-chips-input-cell:hover {
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-chips-input-cell:focus-visible {
  color: #333333;
}
.ds-chips-input-cell:disabled {
  color: #9e9e9e;
}
.ds-chips-input-cell.ds-chips-input-cell--disabled {
  color: #9e9e9e;
}
.ds-chips-input-cell--disabled {
  pointer-events: none;
}

.ds-control-arrow-button {
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-0-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-control-arrow-button__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-control-arrow-button__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-control-arrow-button__icon svg path {
  fill: currentColor;
}
.ds-control-arrow-button__icon-size {
  height: var(--ds-size-3x);
  display: flex;
  flex-direction: row;
}
.ds-control-arrow-button--s .ds-control-arrow-button__icon {
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
}

.ds-control-panel {
  display: flex;
  width: 280px;
  padding: var(--ds-size-1x) 0 var(--ds-size-1x) 0;
  gap: 74px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-control-panel__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-control-panel__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-control-panel__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-control-panel__icon svg path {
  fill: currentColor;
}
.ds-control-panel__elements {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-control-panel__month {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-primary, #333333);
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel__button-icon-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
}
.ds-control-panel__button-icon {
  display: flex;
  flex-direction: row;
  gap: var(--ds-button-icon-gap, 8px);
  padding: var(--ds-button-icon-m-size-pad-top, 8px) var(--ds-button-icon-m-size-pad-right, 8px) var(--ds-button-icon-m-size-pad-bottom, 8px) var(--ds-button-icon-m-size-pad-left, 8px);
  border-radius: var(--ds-button-icon-border-radius, 8px);
}
.ds-control-panel--control {
  flex-direction: row;
  align-items: center;
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel--week {
  width: fit-content;
  flex-direction: row;
  padding: var(--ds-size-0-5x) 0 var(--ds-size-0-5x) 0;
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel--calendar {
  width: fit-content;
  flex-direction: column;
  align-items: center;
  background: #ffffff;
  color: var(--ds-color-text-primary, #333333);
}

.ds-control-panel-2 {
  display: flex;
  flex-direction: row;
  width: 280px;
  padding: var(--ds-size-1x) 0 var(--ds-size-1x) 0;
  gap: 74px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-control-panel-2__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-control-panel-2__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-control-panel-2__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-control-panel-2__icon svg path {
  fill: currentColor;
}
.ds-control-panel-2__elements {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-control-panel-2__month {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-primary, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel-2__button-icon-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-icon-gap, 8px);
}
.ds-control-panel-2--control {
  align-items: center;
  color: var(--ds-color-text-primary, #333333);
}
.ds-control-panel-2--time {
  width: fit-content;
  padding: var(--ds-size-0-5x) 0 var(--ds-size-0-5x) 0;
  color: var(--ds-color-text-primary, #333333);
}

.ds-datepicker {
  width: fit-content;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  border-radius: var(--ds-size-3x);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-datepicker__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-datepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-datepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-datepicker__icon svg path {
  fill: currentColor;
}
.ds-datepicker__control-panel {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 74px;
  padding: var(--ds-size-1x) 0 var(--ds-size-1x) 0;
}
.ds-datepicker__elements {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-datepicker__button-icon-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
}
.ds-datepicker__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-datepicker__week-6 {
  height: 48px;
  display: flex;
  flex-direction: row;
}
.ds-datepicker--day {
  color: var(--ds-color-text-primary, #333333);
}
.ds-datepicker--year {
  color: var(--ds-color-text-primary, #333333);
}
.ds-datepicker--month {
  color: var(--ds-color-text-primary, #333333);
}

.ds-dialog-content {
  min-height: 204px;
  width: 500px;
  display: flex;
  flex-direction: row;
  background: var(--ds-color-dialog-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-content__label {
  font-size: var(--ds-font-body-m-16-normal-medium-size);
  line-height: var(--ds-font-body-m-16-normal-medium-line);
  letter-spacing: var(--ds-font-body-m-16-normal-medium-spacing);
  font-weight: var(--ds-font-body-m-16-normal-medium-weight);
  color: var(--ds-color-dialog-content-title-color, #333333);
  white-space: nowrap;
}
.ds-dialog-content__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-content__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-content__icon svg path {
  fill: currentColor;
}
.ds-dialog-content__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-dialog-content__background {
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-scroll-border-radius, 8px);
  background: var(--ds-color-scroll-default-background, #fafafa);
}

.ds-dialog-footer {
  min-height: 69px;
  width: 501px;
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-footer__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-button-accent-filled-default-text-color, #ffffff);
  white-space: nowrap;
}
.ds-dialog-footer__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-footer__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-footer__icon svg path {
  fill: currentColor;
}
.ds-dialog-footer__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-dialog-footer__action {
  height: 68px;
  display: flex;
  flex-direction: column;
  padding: var(--ds-dialog-footer-pad-top, 16px) var(--ds-dialog-footer-pad-right, 24px) var(--ds-dialog-footer-pad-bottom, 16px) var(--ds-dialog-footer-pad-left, 24px);
}
.ds-dialog-footer__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-m-size-gap, 8px);
  padding: var(--ds-button-m-size-pad-top, 8px) var(--ds-button-m-size-pad-right, 12px) var(--ds-button-m-size-pad-bottom, 8px) var(--ds-button-m-size-pad-left, 12px);
  border-radius: var(--ds-button-border-radius, 8px);
  background: var(--ds-color-button-accent-filled-default-background, #448aff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
}

.ds-dialog-header {
  width: 500px;
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-header__label {
  font-size: var(--ds-font-header-s-20-normal-medium-size);
  line-height: var(--ds-font-header-s-20-normal-medium-line);
  letter-spacing: var(--ds-font-header-s-20-normal-medium-spacing);
  font-weight: var(--ds-font-header-s-20-normal-medium-weight);
  color: var(--ds-color-dialog-header-title-color, #333333);
  white-space: nowrap;
}
.ds-dialog-header__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-header__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-header__icon svg path {
  fill: currentColor;
}
.ds-dialog-header__title-container {
  display: flex;
  flex-direction: row;
  gap: var(--ds-dialog-header-gap, 8px);
}
.ds-dialog-header__description {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-dialog-header-desc-color, #616161);
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-dialog-header-desc-color, #616161);
}
.ds-dialog-header__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-dialog-header--text {
  color: var(--ds-color-dialog-header-title-color, #333333);
}

.ds-dialog-view {
  min-height: 364px;
  width: 500px;
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-dialog-border-radius, 12px);
  background: var(--ds-color-dialog-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-12-dp-m);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-dialog-view__label {
  font-size: var(--ds-font-header-s-20-normal-medium-size);
  line-height: var(--ds-font-header-s-20-normal-medium-line);
  letter-spacing: var(--ds-font-header-s-20-normal-medium-spacing);
  font-weight: var(--ds-font-header-s-20-normal-medium-weight);
  color: var(--ds-color-dialog-header-title-color, #333333);
  white-space: nowrap;
}
.ds-dialog-view__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-dialog-view__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-dialog-view__icon svg path {
  fill: currentColor;
}
.ds-dialog-view__header {
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
}
.ds-dialog-view__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-dialog-view__content {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-dialog-background, #ffffff);
}
.ds-dialog-view__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-dialog-view__footer {
  display: flex;
  flex-direction: column;
  background: var(--ds-color-dialog-background, #ffffff);
}
.ds-dialog-view__action {
  height: 68px;
  display: flex;
  flex-direction: column;
  padding: var(--ds-dialog-footer-pad-top, 16px) var(--ds-dialog-footer-pad-right, 24px) var(--ds-dialog-footer-pad-bottom, 16px) var(--ds-dialog-footer-pad-left, 24px);
}

.ds-element {
  display: flex;
  background: #ffffff;
  width: fit-content;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element__icon svg path {
  fill: currentColor;
}
.ds-element__image-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-size-circular);
}
.ds-element--image-size {
  flex-direction: row;
  align-items: center;
}
.ds-element--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element--icon-group {
  flex-direction: row;
  align-items: center;
}
.ds-element--text-default {
  flex-direction: row;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element--checkbox {
  flex-direction: row;
}
.ds-element--radio-button {
  flex-direction: row;
}
.ds-element--indicator {
  width: var(--ds-size-6x);
  flex-direction: row;
}
.ds-element--slide-toggle {
  flex-direction: row;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-element--counter {
  flex-direction: column;
  color: var(--ds-color-badge-text-color, #ffffff);
}

.ds-element-cell {
  width: fit-content;
  display: flex;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-cell__label {
  font-size: var(--ds-font-caption-l-12-normal-medium-size);
  line-height: var(--ds-font-caption-l-12-normal-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-medium-weight);
  color: var(--ds-color-button-neutral-filled-default-text-color, #333333);
  white-space: nowrap;
}
.ds-element-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-cell__icon svg path {
  fill: currentColor;
}
.ds-element-cell__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-element-cell__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-element-cell--icon-size {
  flex-direction: row;
  align-items: center;
  background: #ffffff;
}
.ds-element-cell--icon-group {
  flex-direction: row;
  align-items: center;
  background: #ffffff;
}
.ds-element-cell--button {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-button-neutral-filled-default-text-color, #333333);
}
.ds-element-cell--button-icon {
  flex-direction: row;
  background: #ffffff;
}
.ds-element-cell--status {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
}
.ds-element-cell--text-ui {
  flex-direction: row;
  color: var(--ds-color-text-ui-text-label-color, #616161);
}
.ds-element-cell--input-number {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-form-field-filled-default-support-text-color, #616161);
}
.ds-element-cell--checkbox {
  flex-direction: row;
  background: #ffffff;
}
.ds-element-cell--slide-toggle {
  flex-direction: column;
  background: #ffffff;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-element-cell--chips {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-chips-text-color, #333333);
}
.ds-element-cell--cell-input {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}

.ds-element-form-field {
  width: fit-content;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-form-field__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-element-form-field__input-cell {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
}
.ds-element-form-field__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-element-form-field--input-cell {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-element-form-field--select-cell {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-element-form-field--chips-input-cell {
  color: #616161;
}

.ds-element-left {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-left__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-left__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-left__icon svg path {
  fill: currentColor;
}
.ds-element-left__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}

.ds-element-menu {
  display: flex;
  background: #ffffff;
  width: fit-content;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-menu__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element-menu__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-menu__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-menu__icon svg path {
  fill: currentColor;
}
.ds-element-menu__image-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-size-circular);
}
.ds-element-menu--image-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-menu--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-menu--text-default {
  flex-direction: row;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element-menu--checkbox {
  flex-direction: row;
}
.ds-element-menu--radio-button {
  flex-direction: row;
}
.ds-element-menu--indicator {
  width: var(--ds-size-6x);
  flex-direction: row;
}
.ds-element-menu--slide-toggle {
  flex-direction: row;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-element-menu--counter {
  flex-direction: column;
  color: var(--ds-color-badge-text-color, #ffffff);
}

.ds-element-select {
  display: flex;
  background: #ffffff;
  width: fit-content;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-select__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element-select__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-select__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-select__icon svg path {
  fill: currentColor;
}
.ds-element-select__image-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-size-circular);
}
.ds-element-select--image-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-select--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-select--text-default {
  flex-direction: row;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element-select--checkbox {
  flex-direction: row;
}
.ds-element-select--radio-button {
  flex-direction: row;
}
.ds-element-select--indicator {
  width: var(--ds-size-6x);
  flex-direction: row;
}
.ds-element-select--slide-toggle {
  flex-direction: row;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-element-select--counter {
  flex-direction: column;
  color: var(--ds-color-badge-text-color, #ffffff);
}

.ds-element-sidenav {
  height: var(--ds-size-5x);
  width: var(--ds-size-5x);
  display: flex;
  border-radius: var(--ds-size-1x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-sidenav__label {
  font-size: var(--ds-font-caption-m-10-normal-medium-size);
  line-height: var(--ds-font-caption-m-10-normal-medium-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-medium-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-medium-weight);
  text-transform: capitalize;
  color: var(--ds-color-text-accent, #448aff);
  white-space: nowrap;
}
.ds-element-sidenav__icon {
  flex-shrink: 0;
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-sidenav__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-sidenav__icon svg path {
  fill: currentColor;
}
.ds-element-sidenav__keyboard-arrow-left {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-element-sidenav--collaps-icon {
  flex-direction: row;
  background: var(--ds-color-sidenav-element-collaps-icon-background, #36474e);
}
.ds-element-sidenav--avatar {
  flex-direction: column;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: 3px var(--ds-size-0-5x) 3px var(--ds-size-0-5x);
  color: var(--ds-color-text-accent, #448aff);
}

.ds-element-step {
  min-height: var(--ds-size-6x);
  width: fit-content;
  display: flex;
  background: #ffffff;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-element-step__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-brand-neutral-super-dark, #333333);
  white-space: nowrap;
}
.ds-element-step__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-element-step__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-element-step__icon svg path {
  fill: currentColor;
}
.ds-element-step__icon-size {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
}
.ds-element-step__info {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-element-step--icon-size {
  flex-direction: row;
  align-items: center;
}
.ds-element-step--counter {
  flex-direction: column;
  color: var(--ds-color-brand-neutral-super-dark, #333333);
}
.ds-element-step--counter:hover {
  color: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-element-step--counter:active {
  color: var(--ds-color-brand-neutral-default, #ffffff);
}
.ds-element-step--counter:disabled {
  color: var(--ds-color-brand-neutral-neutral, #9e9e9e);
}
.ds-element-step--counter.ds-element-step--disabled {
  color: var(--ds-color-brand-neutral-neutral, #9e9e9e);
}
.ds-element-step--disabled {
  pointer-events: none;
}

.ds-elementare-cell {
  width: fit-content;
  display: flex;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-elementare-cell__label {
  font-size: var(--ds-font-caption-l-12-normal-medium-size);
  line-height: var(--ds-font-caption-l-12-normal-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-medium-weight);
  color: var(--ds-color-button-neutral-filled-default-text-color, #333333);
  white-space: nowrap;
}
.ds-elementare-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-elementare-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-elementare-cell__icon svg path {
  fill: currentColor;
}
.ds-elementare-cell__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-elementare-cell__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-elementare-cell--icon-size {
  flex-direction: row;
  align-items: center;
  background: #ffffff;
}
.ds-elementare-cell--icon-group {
  flex-direction: row;
  align-items: center;
  background: #ffffff;
}
.ds-elementare-cell--button {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-button-neutral-filled-default-text-color, #333333);
}
.ds-elementare-cell--button-icon {
  flex-direction: row;
  background: #ffffff;
}
.ds-elementare-cell--status {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
}
.ds-elementare-cell--text-ui {
  flex-direction: row;
  color: var(--ds-color-text-ui-text-label-color, #616161);
}
.ds-elementare-cell--input-number {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-form-field-filled-default-support-text-color, #616161);
}
.ds-elementare-cell--checkbox {
  flex-direction: row;
  background: #ffffff;
}
.ds-elementare-cell--slide-toggle {
  flex-direction: column;
  background: #ffffff;
  color: var(--ds-color-slide-toggle-text-color, #333333);
}
.ds-elementare-cell--chips {
  flex-direction: row;
  background: #ffffff;
  color: var(--ds-color-chips-text-color, #333333);
}

.ds-elements {
  display: flex;
  height: var(--ds-size-10x);
  width: var(--ds-size-10x);
  border-radius: var(--ds-radius-circular, 9999px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-elements__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-elements__range-highlight-start {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements__range-highlight-end {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements__range-highlight-middle {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-10, #f5f9ff);
}
.ds-elements__date {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-primary, #333333);
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--cell.ds-elements--today:disabled {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--today.ds-elements--disabled {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--default.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--range:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--range.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--cell.ds-elements--selected:active {
  background: var(--ds-color-button-accent-filled-press-background, #2651b5);
}
.ds-elements--cell.ds-elements--today:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--cell.ds-elements--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--cell.ds-elements--today:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--cell.ds-elements--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--cell.ds-elements--range {
  flex-direction: row;
  align-items: center;
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--cell.ds-elements--selected {
  flex-direction: column;
  align-items: center;
  color: var(--ds-color-text-inversive, #ffffff);
}
.ds-elements--year.ds-elements--selected {
  width: fit-content;
  flex-direction: column;
  align-items: center;
  color: var(--ds-color-text-inversive, #ffffff);
}
.ds-elements--cell.ds-elements--today {
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  border: 1px solid var(--ds-color-stroke-hover, #9e9e9e);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--cell.ds-elements--default {
  flex-direction: column;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-2-5x) var(--ds-size-2x) var(--ds-size-2-5x);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--year.ds-elements--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--default.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--today:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--today.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--year.ds-elements--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--year.ds-elements--today:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--year.ds-elements--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--year.ds-elements--today:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--year.ds-elements--default {
  width: fit-content;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--year.ds-elements--today {
  width: fit-content;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  border: 1px solid var(--ds-color-stroke-hover, #9e9e9e);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--month.ds-elements--default {
  width: fit-content;
  flex-direction: row;
  gap: var(--ds-size-2x);
  padding: var(--ds-size-2-5x) var(--ds-size-1x) var(--ds-size-2-5x) var(--ds-size-2x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements--month.ds-elements--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements--month.ds-elements--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements--month.ds-elements--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--month.ds-elements--default.ds-elements--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements--disabled {
  pointer-events: none;
}

.ds-elements-2 {
  min-height: var(--ds-size-10x);
  width: fit-content;
  display: flex;
  align-items: center;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-elements-2__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-inversive, #ffffff);
  white-space: nowrap;
}
.ds-elements-2__range-highlight-start {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements-2__range-highlight-end {
  height: var(--ds-size-10x);
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-accent-50, #f0f5ff);
}
.ds-elements-2__date {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-button-accent-filled-default-background, #448aff);
}
.ds-elements-2--selected {
  flex-direction: column;
  color: var(--ds-color-text-inversive, #ffffff);
}
.ds-elements-2--default:disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements-2--default.ds-elements-2--disabled {
  color: var(--ds-color-text-disable, #9e9e9e);
}
.ds-elements-2--default:active {
  background: var(--ds-color-brand-neutral-lighter, #e0e0e0);
}
.ds-elements-2--default:hover {
  background: var(--ds-color-brand-neutral-super-light, #f5f5f5);
}
.ds-elements-2--default {
  flex-direction: row;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-4x) var(--ds-size-2x) var(--ds-size-4x);
  border-radius: var(--ds-radius-circular, 9999px);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  color: var(--ds-color-text-primary, #333333);
}
.ds-elements-2--disabled {
  pointer-events: none;
}

.ds-expansion-content {
  width: 597px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--ds-expansion-panel-content-pad-top, 16px) var(--ds-expansion-panel-content-pad-right, 16px) var(--ds-expansion-panel-content-pad-bottom, 16px) var(--ds-expansion-panel-content-pad-left, 16px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-expansion-content__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
  white-space: nowrap;
}
.ds-expansion-content--true {
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
}
.ds-expansion-content--false {
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
}

.ds-expansion-group-panel {
  width: 597px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-expansion-panel-collaps-gap-group, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-expansion-group-panel__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-expansion-panel-collaps-text-color, #333333);
  white-space: nowrap;
}
.ds-expansion-group-panel--collaps {
  color: var(--ds-color-expansion-panel-collaps-text-color, #333333);
}
.ds-expansion-group-panel--expand {
  color: var(--ds-color-expansion-panel-collaps-text-color, #333333);
}

.ds-form-field-cell {
  min-height: var(--ds-size-10x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-form-field-cell__table-content-chips-input {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-form-field-cell__table-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
}

.ds-hint-container {
  width: 250px;
  display: flex;
  align-items: center;
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  border-radius: var(--ds-hint-border-radius, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-container__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-header-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-container__icon svg path {
  fill: currentColor;
}
.ds-hint-container__arrow {
  height: var(--ds-size-1x);
  display: flex;
  flex-direction: row;
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container__header {
  display: flex;
  flex-direction: row;
  gap: var(--ds-hint-header-gap, 8px);
  padding: var(--ds-hint-header-pad-top, 8px) var(--ds-hint-header-pad-right, 12px) var(--ds-hint-header-pad-bottom, 4px) var(--ds-hint-header-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-hint-content-gap, 8px);
  padding: var(--ds-hint-content-pad-top, 8px) var(--ds-hint-content-pad-right, 12px) var(--ds-hint-content-pad-bottom, 8px) var(--ds-hint-content-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container__footer {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-hint-footer-gap, 12px);
  padding: var(--ds-hint-footer-pad-top, 16px) var(--ds-hint-footer-pad-right, 12px) var(--ds-hint-footer-pad-bottom, 12px) var(--ds-hint-footer-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
}
.ds-hint-container--up {
  flex-direction: column;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--down {
  flex-direction: column;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--right {
  flex-direction: row;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--left {
  flex-direction: row;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-container--default {
  flex-direction: column;
  color: var(--ds-color-hint-header-text-color, #ffffff);
}

.ds-hint-content {
  width: 250px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-hint-content-gap, 8px);
  padding: var(--ds-hint-content-pad-top, 8px) var(--ds-hint-content-pad-right, 12px) var(--ds-hint-content-pad-bottom, 8px) var(--ds-hint-content-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-content__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-hint-content-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-content__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-content__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-content__icon svg path {
  fill: currentColor;
}
.ds-hint-content__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-content__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-content__block {
  display: flex;
  flex-direction: column;
  gap: var(--ds-hint-content-gap-content, 4px);
}
.ds-hint-content__clear {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-content__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-content--group-content {
  color: var(--ds-color-hint-content-text-color, #ffffff);
}
.ds-hint-content--single-content {
  align-items: center;
  color: var(--ds-color-hint-content-text-color, #ffffff);
}

.ds-hint-footer {
  min-height: 56px;
  width: 250px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-hint-footer-gap, 12px);
  padding: var(--ds-hint-footer-pad-top, 16px) var(--ds-hint-footer-pad-right, 12px) var(--ds-hint-footer-pad-bottom, 12px) var(--ds-hint-footer-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-footer__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-button-accent-filled-default-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-footer__icon {
  flex-shrink: 0;
  width: var(--ds-size-7x);
  height: var(--ds-size-7x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-footer__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-footer__icon svg path {
  fill: currentColor;
}
.ds-hint-footer__цвет-и-палитра {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-hint-footer-text-color, #ffffff);
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-footer-text-color, #ffffff);
}
.ds-hint-footer__button-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
}
.ds-hint-footer--default {
  color: var(--ds-color-hint-footer-text-color, #ffffff);
}

.ds-hint-header {
  min-height: var(--ds-size-8x);
  width: 250px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-hint-header-gap, 8px);
  padding: var(--ds-hint-header-pad-top, 8px) var(--ds-hint-header-pad-right, 12px) var(--ds-hint-header-pad-bottom, 4px) var(--ds-hint-header-pad-left, 12px);
  background: var(--ds-color-hint-background-color, #424242);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-hint-header__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-header-text-color, #ffffff);
  white-space: nowrap;
}
.ds-hint-header__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-hint-header__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-hint-header__icon svg path {
  fill: currentColor;
}
.ds-hint-header__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-header__info {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-header__title {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-hint-header-text-color, #ffffff);
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header__clear {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-hint-header__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-hint-header--neutral {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--primary {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--secondary {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--warning {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}
.ds-hint-header--error {
  color: var(--ds-color-hint-header-text-color, #ffffff);
}

.ds-icon-group {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-icon-size-gap-group-2x, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-icon-group__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-icon-group__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-icon-group__icon svg path {
  fill: currentColor;
}
.ds-icon-group--4x {
  gap: var(--ds-icon-size-gap-group-4x, 16px);
}

.ds-input-cell {
  min-height: var(--ds-size-9x);
  width: 200px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-input-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-cell__icon svg path {
  fill: currentColor;
}
.ds-input-cell__frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-cell__support {
  display: flex;
  flex-direction: row;
}
.ds-input-cell:hover {
  background: var(--ds-palette-neutral-50, #f5f5f5);
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-input-cell:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-input-cell:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-cell.ds-input-cell--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-cell--disabled {
  pointer-events: none;
}

.ds-input-datepicker {
  min-height: 48px;
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-datepicker__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-input-datepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-datepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-datepicker__icon svg path {
  fill: currentColor;
}
.ds-input-datepicker__frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-datepicker__support {
  display: flex;
  flex-direction: row;
}
.ds-input-datepicker--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-input-datepicker--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}

.ds-input-number {
  display: flex;
  flex-direction: row;
  width: 138px;
  gap: 18px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-number__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-input-number__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-number__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-number__icon svg path {
  fill: currentColor;
}
.ds-input-number__frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-number__support {
  display: flex;
  flex-direction: row;
}
.ds-input-number--s {
  width: fit-content;
}
.ds-input-number--xs {
  width: fit-content;
}
.ds-input-number--xs .ds-input-number__icon {
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
}
.ds-input-number--populated {
  align-items: center;
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-input-number--empty {
  align-items: center;
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-input-number--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-input-number--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-input-number--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-input-number--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-number--populated.ds-input-number--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-input-number--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-input-number--empty.ds-input-number--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-input-number--disabled {
  pointer-events: none;
}

.ds-input-number-but-icon {
  min-height: 56px;
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-1x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-number-but-icon__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-input-number-but-icon__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-number-but-icon__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-number-but-icon__icon svg path {
  fill: currentColor;
}
.ds-input-number-but-icon__container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-1x);
}
.ds-input-number-but-icon__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-icon-gap, 8px);
  padding: var(--ds-button-icon-m-size-pad-top, 8px) var(--ds-button-icon-m-size-pad-right, 8px) var(--ds-button-icon-m-size-pad-bottom, 8px) var(--ds-button-icon-m-size-pad-left, 8px);
  border-radius: var(--ds-button-icon-border-radius, 8px);
  background: var(--ds-color-button-icon-neutral-filled-default-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
}
.ds-input-number-but-icon__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-input-number-but-icon__support-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-form-field-filled-default-support-text-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-support-text-color, #616161);
}

.ds-input-timepicker {
  min-height: 48px;
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-input-timepicker__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-input-timepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-input-timepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-input-timepicker__icon svg path {
  fill: currentColor;
}
.ds-input-timepicker__frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-input-timepicker__support {
  display: flex;
  flex-direction: row;
}
.ds-input-timepicker--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-input-timepicker--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}

.ds-list-container {
  min-height: 257px;
  width: 258px;
  display: flex;
  flex-direction: column;
  padding: var(--ds-list-pad-top, 8px) 0 var(--ds-list-pad-bottom, 8px) 0;
  border-radius: var(--ds-list-border-radius);
  background: var(--ds-color-list-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-list-container__label {
  font-size: var(--ds-font-body-s-14-normal-medium-size);
  line-height: var(--ds-font-body-s-14-normal-medium-line);
  letter-spacing: var(--ds-font-body-s-14-normal-medium-spacing);
  font-weight: var(--ds-font-body-s-14-normal-medium-weight);
  color: var(--ds-color-list-item-text-color, #333333);
  white-space: nowrap;
}
.ds-list-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-list-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-list-container__icon svg path {
  fill: currentColor;
}
.ds-list-container__item {
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
  padding: var(--ds-list-item-pad-top, 8px) var(--ds-list-item-pad-right, 16px) var(--ds-list-item-pad-bottom, 8px) var(--ds-list-item-pad-left, 16px);
  background: var(--ds-color-list-item-default-background, #ffffff);
}
.ds-list-container__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-list-container__content {
  display: flex;
  flex-direction: column;
}
.ds-list-container__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-list-container__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-list-container__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-list-container--container {
  color: var(--ds-color-list-item-text-label-color, #616161);
}

.ds-list-item {
  min-height: 68px;
  width: 258px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
  padding: var(--ds-list-item-pad-top, 8px) var(--ds-list-item-pad-right, 16px) var(--ds-list-item-pad-bottom, 8px) var(--ds-list-item-pad-left, 16px);
  background: var(--ds-color-list-item-default-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-list-item__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-list-item-text-color, #333333);
  white-space: nowrap;
}
.ds-list-item__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-list-item__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-list-item__icon svg path {
  fill: currentColor;
}
.ds-list-item__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-list-item__checkbox {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-list-item__content {
  display: flex;
  flex-direction: column;
}
.ds-list-item__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-list-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-list-item-text-label-color, #616161);
}
.ds-list-item__text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-list-item-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-list-item-text-color, #333333);
}
.ds-list-item__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-list-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-list-item-text-label-color, #616161);
}
.ds-list-item__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-list-item__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-list-item:hover {
  background: var(--ds-color-list-item-hover-background, #f5f5f5);
}
.ds-list-item:active {
  background: var(--ds-color-list-item-press-background, #e0e0e0);
}
.ds-list-item:disabled {
  background: var(--ds-color-list-item-disable-background, #ffffff);
  color: var(--ds-color-list-item-disable-label-text-color, #9e9e9e);
}
.ds-list-item.ds-list-item--disabled {
  background: var(--ds-color-list-item-disable-background, #ffffff);
  color: var(--ds-color-list-item-disable-label-text-color, #9e9e9e);
}
.ds-list-item--disabled {
  pointer-events: none;
}

.ds-logo-iiko {
  height: 72px;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-logo-iiko__vector {
  height: 72px;
  display: flex;
  flex-direction: row;
  background: var(--ds-palette-neutral-0, #ffffff);
}

.ds-logo-syrve {
  height: 72px;
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-logo-syrve__vector {
  height: 70.9px;
  display: flex;
  flex-direction: row;
  background: #00062b;
}

.ds-menu-container {
  min-height: 418px;
  width: 240px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-menu-gap);
  padding: var(--ds-menu-pad-top, 8px) 0 var(--ds-menu-pad-bottom, 8px) 0;
  border-radius: var(--ds-menu-border-radius, 8px);
  background: var(--ds-color-menu-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-menu-container__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
  white-space: nowrap;
}
.ds-menu-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-menu-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-menu-container__icon svg path {
  fill: currentColor;
}
.ds-menu-container__search {
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  padding: 0 var(--ds-size-4x) var(--ds-size-1x) var(--ds-size-4x);
}
.ds-menu-container__title {
  display: flex;
  flex-direction: row;
  gap: var(--ds-menu-item-gap, 8px);
  padding: var(--ds-menu-item-pad-top, 8px) var(--ds-menu-item-pad-right, 16px) var(--ds-menu-item-pad-bottom, 8px) var(--ds-menu-item-pad-left, 16px);
  background: var(--ds-color-menu-item-default-background, #ffffff);
}
.ds-menu-container__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-menu-container__content {
  display: flex;
  flex-direction: column;
}
.ds-menu-container__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-menu-container__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-menu-container__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-menu-container__button-group {
  height: 52px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
  padding: var(--ds-button-group-margins-pad-top, 8px) var(--ds-button-group-margins-pad-right, 16px) var(--ds-button-group-margins-pad-bottom, 8px) var(--ds-button-group-margins-pad-left, 16px);
}
.ds-menu-container--container {
  color: var(--ds-color-search-default-text-color, #d6d6d6);
}

.ds-menu-item {
  min-height: 68px;
  width: 258px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-menu-item-gap, 8px);
  padding: var(--ds-menu-item-pad-top, 8px) var(--ds-menu-item-pad-right, 16px) var(--ds-menu-item-pad-bottom, 8px) var(--ds-menu-item-pad-left, 16px);
  background: var(--ds-color-menu-item-default-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-menu-item__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-menu-item-text-color, #333333);
  white-space: nowrap;
}
.ds-menu-item__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-menu-item__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-menu-item__icon svg path {
  fill: currentColor;
}
.ds-menu-item__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-menu-item__checkbox {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-menu-item__content {
  display: flex;
  flex-direction: column;
}
.ds-menu-item__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-menu-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-menu-item-text-label-color, #616161);
}
.ds-menu-item__text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-menu-item-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-menu-item-text-color, #333333);
}
.ds-menu-item__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-menu-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-menu-item-text-label-color, #616161);
}
.ds-menu-item__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-menu-item__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-menu-item:hover {
  background: var(--ds-color-menu-item-hover-background, #f5f5f5);
}
.ds-menu-item:active {
  background: var(--ds-color-menu-item-press-background, #e0e0e0);
}
.ds-menu-item:disabled {
  background: var(--ds-color-menu-item-disable-background, #ffffff);
  color: var(--ds-color-menu-item-disable-label-text-color, #9e9e9e);
}
.ds-menu-item.ds-menu-item--disabled {
  background: var(--ds-color-menu-item-disable-background, #ffffff);
  color: var(--ds-color-menu-item-disable-label-text-color, #9e9e9e);
}
.ds-menu-item--disabled {
  pointer-events: none;
}

.ds-picture {
  min-height: 189px;
  width: 446px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2x) var(--ds-size-2x) var(--ds-size-2x) var(--ds-size-2x);
  border-radius: var(--ds-size-2x);
  background: var(--ds-color-brand-accent-super-lightest, #f8f9fc);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-picture__crop {
  height: 173px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  border: 1px dashed var(--ds-color-stroke-hover, #9e9e9e);
}
.ds-picture__frame-1000001806 {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 440px;
}

.ds-radio-button-label {
  min-height: var(--ds-size-5x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  gap: var(--ds-radio-button-label-gap-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-radio-button-label__label {
  font-size: var(--ds-typography-font-size-3-5x);
  font-weight: var(--ds-typography-font-weight-regular);
  line-height: var(--ds-typography-line-height-5x);
  letter-spacing: 0.25px;
  color: var(--ds-color-radio-button-label-text-color, #333333);
  white-space: nowrap;
}
.ds-radio-button-label__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-radio-button-label__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-radio-button-label__icon svg path {
  fill: currentColor;
}
.ds-radio-button-label__form {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-radio-button-label-gap, 8px);
}
.ds-radio-button-label__left {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-radio-button-label__цвет-и-палитра {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-radio-button-label-text-color, #333333);
  font-size: var(--ds-typography-font-size-3-5x);
  font-weight: var(--ds-typography-font-weight-regular);
  line-height: var(--ds-typography-line-height-5x);
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label__right {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-radio-button-label__support {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 var(--ds-radio-button-label-pad-left-support-7x, 28px);
}
.ds-radio-button-label__support-text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-radio-button-label-text-support-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-radio-button-label-text-support-color, #616161);
}
.ds-radio-button-label--normal.ds-radio-button-label--deselected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--normal.ds-radio-button-label--selected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--error.ds-radio-button-label--deselected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--error.ds-radio-button-label--selected {
  color: var(--ds-color-radio-button-label-text-color, #333333);
}
.ds-radio-button-label--disable.ds-radio-button-label--deselected {
  color: var(--ds-color-radio-button-label-text-disable-color, #9e9e9e);
}
.ds-radio-button-label--disable.ds-radio-button-label--selected {
  color: var(--ds-color-radio-button-label-text-disable-color, #9e9e9e);
}

.ds-scroll {
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
  width: 184px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-scroll__background {
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-scroll-border-radius, 8px);
  background: var(--ds-color-scroll-default-background, #fafafa);
}
.ds-scroll__knob {
  height: var(--ds-size-2x);
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-size-2-5x) var(--ds-size-2-5x) var(--ds-size-2-5x) var(--ds-size-2-5x);
  border-radius: var(--ds-scroll-knob-radius, 8px);
  background: var(--ds-color-scroll-default-knob-color, #d6d6d6);
}
.ds-scroll--s {
  width: var(--ds-size-2x);
}
.ds-scroll--first:hover {
  background: var(--ds-color-scroll-hover-background, #ebebeb);
}
.ds-scroll--middle {
  align-items: center;
}
.ds-scroll--middle:hover {
  background: var(--ds-color-scroll-hover-background, #ebebeb);
}
.ds-scroll--last:hover {
  background: var(--ds-color-scroll-hover-background, #ebebeb);
}

.ds-scroll-tabs {
  min-height: var(--ds-size-7x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: 0 0 0 48px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-scroll-tabs__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-scroll-tabs__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-scroll-tabs__icon svg path {
  fill: currentColor;
}
.ds-scroll-tabs__button-icon {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-icon-gap, 8px);
  padding: var(--ds-button-icon-s-size-pad-top, 4px) var(--ds-button-icon-s-size-pad-right, 4px) var(--ds-button-icon-s-size-pad-bottom, 4px) var(--ds-button-icon-s-size-pad-left, 4px);
  border-radius: var(--ds-button-icon-border-radius, 8px);
  background: var(--ds-color-button-icon-neutral-filled-default-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
}
.ds-scroll-tabs__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-scroll-tabs--left {
  padding: 0 48px 0 0;
}

.ds-search {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-search-gap, 8px);
  width: 243px;
  padding: var(--ds-search-m-size-pad-top, 12px) var(--ds-search-m-size-pad-right, 12px) var(--ds-search-m-size-pad-bottom, 12px) var(--ds-search-m-size-pad-left, 12px);
  border-radius: var(--ds-search-border-radius, 12px);
  background: var(--ds-color-search-background, #f8f9fc);
  border: 1px solid var(--ds-color-search-default-border-color, #e0e0e0);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-search__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
  white-space: nowrap;
}
.ds-search__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-search__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-search__icon svg path {
  fill: currentColor;
}
.ds-search__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-search__text {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-search-default-text-color, #d6d6d6);
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
}
.ds-search__right-icon {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
}
.ds-search__divider {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-search--s {
  padding: var(--ds-search-s-size-pad-top, 8px) var(--ds-search-s-size-pad-right, 12px) var(--ds-search-s-size-pad-bottom, 8px) var(--ds-search-s-size-pad-left, 12px);
}
.ds-search--s .ds-search__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-search--xs {
  height: var(--ds-size-9x);
  width: var(--ds-size-9x);
  padding: var(--ds-size-1-5x) var(--ds-size-1-5x) var(--ds-size-1-5x) var(--ds-size-1-5x);
  border-radius: var(--ds-size-circular);
}
.ds-search--xs .ds-search__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-search:disabled {
  background: var(--ds-color-search-disable-background, #ebebeb);
  color: var(--ds-color-search-disable-text-color, #9e9e9e);
}
.ds-search.ds-search--disabled {
  background: var(--ds-color-search-disable-background, #ebebeb);
  color: var(--ds-color-search-disable-text-color, #9e9e9e);
}
.ds-search:focus-visible {
  color: var(--ds-color-search-focusvalue-text-color, #333333);
}
.ds-search:hover {
  border: 1px solid var(--ds-color-search-hover-border-color, #9e9e9e);
}
.ds-search--disabled {
  pointer-events: none;
}

.ds-select-container {
  min-height: 406px;
  width: 240px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-space-0);
  padding: var(--ds-menu-pad-top, 8px) 0 var(--ds-menu-pad-bottom, 8px) 0;
  border-radius: var(--ds-radius-3x, 12px);
  background: var(--ds-color-menu-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-container__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-search-default-text-color, #d6d6d6);
  white-space: nowrap;
}
.ds-select-container__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-container__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-container__icon svg path {
  fill: currentColor;
}
.ds-select-container__search {
  display: flex;
  flex-direction: column;
  gap: var(--ds-size-2-5x);
  padding: 0 var(--ds-size-2x) 0 var(--ds-size-2x);
}
.ds-select-container__title {
  display: flex;
  flex-direction: row;
  gap: var(--ds-select-item-gap, 8px);
  padding: var(--ds-select-item-pad-top, 8px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom, 8px) var(--ds-select-item-pad-left, 16px);
  background: var(--ds-color-menu-item-default-background, #ffffff);
}
.ds-select-container__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-select-container__content {
  display: flex;
  flex-direction: column;
}
.ds-select-container__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-select-container__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-select-container__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-select-container__button-group {
  height: 44px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-group-gap, 8px);
  padding: var(--ds-button-group-margins-pad-top, 8px) var(--ds-button-group-margins-pad-right, 16px) var(--ds-button-group-margins-pad-bottom, 8px) var(--ds-button-group-margins-pad-left, 16px);
}
.ds-select-container__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-s-size-gap, 4px);
  padding: var(--ds-button-s-size-pad-top, 4px) var(--ds-button-s-size-pad-right, 8px) var(--ds-button-s-size-pad-bottom, 4px) var(--ds-button-s-size-pad-left, 8px);
  border-radius: var(--ds-button-border-radius, 8px);
  border: 1px solid var(--ds-color-button-neutral-outlined-default-border-color, #e0e0e0);
}
.ds-select-container--container {
  color: var(--ds-color-search-default-text-color, #d6d6d6);
}

.ds-select-cell {
  min-height: var(--ds-size-9x);
  width: 200px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-select-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-cell__icon svg path {
  fill: currentColor;
}
.ds-select-cell__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-select-cell__input-frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-select-cell__support {
  display: flex;
  flex-direction: row;
}
.ds-select-cell:hover {
  background: var(--ds-palette-neutral-50, #f5f5f5);
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-select-cell:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-select-cell:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-cell.ds-select-cell--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-cell--disabled {
  pointer-events: none;
}

.ds-select-form {
  width: 250px;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-form__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-input-label-text-color, #616161);
  white-space: nowrap;
}
.ds-select-form__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-form__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-form__icon svg path {
  fill: currentColor;
}
.ds-select-form__input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
}
.ds-select-form__input-frame {
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-m-size-pad-input-top, 12px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-select-form__support {
  display: flex;
  flex-direction: row;
}
.ds-select-form--s .ds-select-form__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-select-form--xs .ds-select-form__icon {
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
}
.ds-select-form--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-select-form--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-select-form--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-select-form--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-select-form--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-select-form--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-select-form--empty.ds-select-form--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-select-form--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-form--populated.ds-select-form--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-select-form--disabled {
  pointer-events: none;
}

.ds-select-item {
  width: 258px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-select-item-gap, 8px);
  padding: var(--ds-select-item-pad-top-sub, 12px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom-sub, 6px) var(--ds-select-item-pad-left, 16px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-select-item__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-select-item-text-label-color, #616161);
  white-space: nowrap;
}
.ds-select-item__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-select-item__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-select-item__icon svg path {
  fill: currentColor;
}
.ds-select-item__element-left {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-select-item__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-select-item__content {
  display: flex;
  flex-direction: column;
}
.ds-select-item__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-select-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item__subtitle {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-select-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-m-10-normal-medium-size);
  line-height: var(--ds-font-caption-m-10-normal-medium-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-medium-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-medium-weight);
  text-transform: capitalize;
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-select-item-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-select-item--true {
  align-items: center;
  background: var(--ds-color-select-item-default-background, #ffffff);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item--false {
  padding: var(--ds-select-item-pad-top, 8px) var(--ds-select-item-pad-right, 16px) var(--ds-select-item-pad-bottom, 8px) var(--ds-select-item-pad-left, 16px);
  background: var(--ds-color-select-item-default-background, #ffffff);
  color: var(--ds-color-select-item-text-label-color, #616161);
}
.ds-select-item--false:hover {
  background: var(--ds-color-select-item-hover-background, #f5f5f5);
}
.ds-select-item--false:active {
  background: var(--ds-color-select-item-press-background, #e0e0e0);
}
.ds-select-item--false:disabled {
  background: var(--ds-color-select-item-disable-background, #ffffff);
  color: var(--ds-color-select-item-disable-label-text-color, #9e9e9e);
}
.ds-select-item--false.ds-select-item--disabled {
  background: var(--ds-color-select-item-disable-background, #ffffff);
  color: var(--ds-color-select-item-disable-label-text-color, #9e9e9e);
}
.ds-select-item--disabled {
  pointer-events: none;
}

.ds-sidenav-control {
  min-height: 41px;
  display: flex;
  flex-direction: column;
  width: 200px;
  gap: var(--ds-sidenav-control-expanded-gap);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-control__label {
  font-size: var(--ds-font-caption-m-10-normal-regular-size);
  line-height: var(--ds-font-caption-m-10-normal-regular-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-regular-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-regular-weight);
  color: var(--ds-color-sidenav-control-text-color, #ffffff);
  white-space: nowrap;
}
.ds-sidenav-control__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-sidenav-control__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-sidenav-control__icon svg path {
  fill: currentColor;
}
.ds-sidenav-control__content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-sidenav-control-expanded-gap-content, 8px);
  padding: var(--ds-sidenav-control-pad-top, 8px) var(--ds-sidenav-control-pad-right, 16px) var(--ds-sidenav-control-pad-bottom, 12px) var(--ds-sidenav-control-pad-left, 16px);
  background: var(--ds-color-sidenav-control-background, #263136);
}
.ds-sidenav-control__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-sidenav-control__свернуть-меню {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-control-text-color, #ffffff);
  font-size: var(--ds-font-caption-m-10-normal-regular-size);
  line-height: var(--ds-font-caption-m-10-normal-regular-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-regular-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-regular-weight);
  color: var(--ds-color-sidenav-control-text-color, #ffffff);
}
.ds-sidenav-control__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-sidenav-control--collapsed:hover {
  background: var(--ds-color-sidenav-control-background-hover, #36474e);
}
.ds-sidenav-control--collapsed:active {
  background: var(--ds-color-sidenav-control-background-press, #36474e);
}
.ds-sidenav-control--expanded {
  background: var(--ds-color-sidenav-control-background, #263136);
  color: var(--ds-color-sidenav-control-text-color, #ffffff);
}
.ds-sidenav-control--expanded:hover {
  background: var(--ds-color-sidenav-control-background-hover, #36474e);
}
.ds-sidenav-control--expanded:active {
  background: var(--ds-color-sidenav-control-background-press, #36474e);
}
.ds-sidenav-control--collapsed {
  width: fit-content;
  gap: var(--ds-sidenav-control-collapsed-gap);
}

.ds-sidenav-footer {
  display: flex;
  width: 260px;
  padding: var(--ds-sidenav-footer-l2-pad-top, 12px) var(--ds-sidenav-footer-l2-pad-right, 16px) var(--ds-sidenav-footer-l2-pad-bottom, 12px) var(--ds-sidenav-footer-l2-pad-left, 16px);
  gap: var(--ds-sidenav-footer-l2-gap, 12px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-footer__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-footer-l2-text-color, #616161);
  white-space: nowrap;
}
.ds-sidenav-footer__logo-iiko {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-sidenav-footer__vector {
  height: 9.8px;
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-footer-l2-logo, #ff5252);
}
.ds-sidenav-footer__divider {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-sidenav-footer__ver-7-8-6-29440 {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-footer-l2-text-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-footer-l2-text-color, #616161);
}
.ds-sidenav-footer--l2.ds-sidenav-footer--expanded {
  flex-direction: row;
  align-items: center;
  background: var(--ds-color-sidenav-footer-l2-background, #ffffff);
  color: var(--ds-color-sidenav-footer-l2-text-color, #616161);
}
.ds-sidenav-footer--l1.ds-sidenav-footer--expanded {
  width: 200px;
  flex-direction: column;
  color: var(--ds-color-sidenav-item-l1-text-color, #ffffff);
}
.ds-sidenav-footer--l1.ds-sidenav-footer--collapsed {
  width: 52px;
  flex-direction: column;
  color: var(--ds-color-text-accent, #448aff);
}

.ds-sidenav-header {
  display: flex;
  align-items: center;
  width: 200px;
  padding: var(--ds-sidenav-header-pad-top, 12px) var(--ds-sidenav-header-l1-expanded-pad-right, 16px) var(--ds-sidenav-header-pad-bottom, 12px) var(--ds-sidenav-header-l1-expanded-pad-left, 16px);
  gap: var(--ds-sidenav-header-l1-expanded-gap, 92px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-header__label {
  font-size: var(--ds-font-body-m-16-normal-medium-size);
  line-height: var(--ds-font-body-m-16-normal-medium-line);
  letter-spacing: var(--ds-font-body-m-16-normal-medium-spacing);
  font-weight: var(--ds-font-body-m-16-normal-medium-weight);
  color: var(--ds-color-sidenav-header-l2-text-color, #333333);
  white-space: nowrap;
}
.ds-sidenav-header__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-sidenav-header__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-sidenav-header__icon svg path {
  fill: currentColor;
}
.ds-sidenav-header__logo-iiko {
  height: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
}
.ds-sidenav-header__vector {
  height: 14.7px;
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-header-l1-expanded-logo, #ffffff);
}
.ds-sidenav-header__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-sidenav-header__close {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-sidenav-header--l1.ds-sidenav-header--expanded {
  flex-direction: row;
  background: var(--ds-color-sidenav-header-l1-background, #263136);
}
.ds-sidenav-header--l2.ds-sidenav-header--expanded {
  height: 48px;
  width: 260px;
  flex-direction: row;
  gap: var(--ds-sidenav-header-l2-gap, 8px);
  padding: var(--ds-sidenav-header-pad-top, 12px) var(--ds-sidenav-header-l2-pad-right, 16px) var(--ds-sidenav-header-pad-bottom, 12px) var(--ds-sidenav-header-l2-pad-left, 16px);
  background: var(--ds-color-sidenav-header-l2-background, #ffffff);
  color: var(--ds-color-sidenav-header-l2-text-color, #333333);
}
.ds-sidenav-header--l1.ds-sidenav-header--collapsed {
  width: 52px;
  flex-direction: column;
  padding: var(--ds-sidenav-header-pad-top, 12px) var(--ds-sidenav-header-l1-collapsed-pad-right, 14px) var(--ds-sidenav-header-pad-bottom, 12px) var(--ds-sidenav-header-l1-collapsed-pad-left, 14px);
  background: var(--ds-color-sidenav-header-l1-background, #263136);
}

.ds-sidenav-item {
  display: flex;
  width: 260px;
  padding: var(--ds-sidenav-item-l3-pad-top, 8px) var(--ds-sidenav-item-l3-pad-right, 16px) var(--ds-sidenav-item-l3-pad-bottom, 8px) var(--ds-sidenav-item-l3-pad-left, 32px);
  gap: var(--ds-sidenav-item-l3-gap, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-item__label {
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-item-l3-text-color, #333333);
  white-space: nowrap;
}
.ds-sidenav-item__l3 {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-sidenav-item-l3-text-color, #333333);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-sidenav-item-l3-text-color, #333333);
}
.ds-sidenav-item--l3.ds-sidenav-item--expanded:hover {
  background: var(--ds-color-sidenav-item-l3-background-hover, #f8f9fc);
}
.ds-sidenav-item--l3.ds-sidenav-item--expanded {
  flex-direction: row;
  align-items: center;
  background: var(--ds-color-sidenav-item-l3-background, #ffffff);
  color: var(--ds-color-sidenav-item-l3-text-color, #333333);
}
.ds-sidenav-item--l2.ds-sidenav-item--expanded {
  flex-direction: column;
  background: var(--ds-color-sidenav-item-l2-background, #ffffff);
  color: var(--ds-color-sidenav-item-l2-text-color, #333333);
}
.ds-sidenav-item--l2.ds-sidenav-item--expanded:hover {
  background: var(--ds-color-sidenav-item-l2-background-hover, #f8f9fc);
}
.ds-sidenav-item--l1.ds-sidenav-item--expanded:hover {
  background: var(--ds-color-sidenav-item-l1-background-hover, #36474e);
}
.ds-sidenav-item--l1.ds-sidenav-item--expanded {
  width: 200px;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-sidenav-item-l1-gap-container, 8px);
  padding: var(--ds-sidenav-item-l1-pad-top, 12px) var(--ds-sidenav-item-l1-pad-right, 16px) var(--ds-sidenav-item-l1-pad-bottom, 12px) var(--ds-sidenav-item-l1-pad-left, 16px);
  background: var(--ds-color-sidenav-item-l1-background, #263136);
  color: var(--ds-color-sidenav-item-l1-text-color, #ffffff);
}
.ds-sidenav-item--l1.ds-sidenav-item--collapsed:hover {
  background: var(--ds-color-sidenav-item-l1-background-hover, #36474e);
}
.ds-sidenav-item--l1.ds-sidenav-item--collapsed {
  width: fit-content;
  flex-direction: row;
  padding: var(--ds-sidenav-item-l1-pad-top, 12px) var(--ds-sidenav-item-l1-pad-right, 16px) var(--ds-sidenav-item-l1-pad-bottom, 12px) var(--ds-sidenav-item-l1-pad-left, 16px);
  background: var(--ds-color-sidenav-item-l1-background, #263136);
}

.ds-sidenav-view {
  display: flex;
  flex-direction: column;
  padding: var(--ds-sidenav-sidebar-pad-top, 8px) 0 var(--ds-sidenav-sidebar-pad-bottom, 8px) 0;
  width: fit-content;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-sidenav-view__label {
  font-size: var(--ds-font-caption-m-10-normal-regular-size);
  line-height: var(--ds-font-caption-m-10-normal-regular-line);
  letter-spacing: var(--ds-font-caption-m-10-normal-regular-spacing);
  font-weight: var(--ds-font-caption-m-10-normal-regular-weight);
  color: var(--ds-color-sidenav-control-text-color, #ffffff);
  white-space: nowrap;
}
.ds-sidenav-view__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-sidenav-view__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-sidenav-view__icon svg path {
  fill: currentColor;
}
.ds-sidenav-view__container {
  display: flex;
  flex-direction: column;
}
.ds-sidenav-view__header {
  display: flex;
  flex-direction: column;
}
.ds-sidenav-view__body {
  display: flex;
  flex-direction: row;
}
.ds-sidenav-view__footer {
  display: flex;
  flex-direction: column;
}
.ds-sidenav-view__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}

.ds-snackbar {
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-snackbar-border-radius, 8px);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  width: fit-content;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-snackbar__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-snackbar-complex-dark-text-color, #ffffff);
  white-space: nowrap;
}
.ds-snackbar__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-snackbar__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-snackbar__icon svg path {
  fill: currentColor;
}
.ds-snackbar__body {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-snackbar-gap, 8px);
  padding: var(--ds-snackbar-pad-top, 12px) var(--ds-snackbar-pad-right, 12px) var(--ds-snackbar-pad-bottom, 12px) var(--ds-snackbar-pad-left, 12px);
}
.ds-snackbar__content {
  display: flex;
  flex-direction: row;
  gap: var(--ds-snackbar-gap, 8px);
  padding: var(--ds-space-0) var(--ds-space-0) var(--ds-space-0) var(--ds-space-0);
  border-radius: var(--ds-radius-0);
}
.ds-snackbar__button {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-button-s-size-gap, 4px);
  padding: var(--ds-button-s-size-pad-top, 4px) var(--ds-button-s-size-pad-right, 8px) var(--ds-button-s-size-pad-bottom, 4px) var(--ds-button-s-size-pad-left, 8px);
  border-radius: var(--ds-button-border-radius, 8px);
}
.ds-snackbar__element-right {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-snackbar__progress {
  height: var(--ds-size-1x);
  display: flex;
  flex-direction: row;
  border-radius: var(--ds-snackbar-border-radius, 8px);
  background: var(--ds-color-snackbar-progress-color, #448aff);
}
.ds-snackbar--single.ds-snackbar--dark {
  background: var(--ds-color-snackbar-complex-dark-background, #424242);
  color: var(--ds-color-snackbar-complex-dark-text-color, #ffffff);
}
.ds-snackbar--single.ds-snackbar--light {
  width: 370px;
  background: var(--ds-color-snackbar-complex-light-background, #ffffff);
  color: var(--ds-color-snackbar-complex-light-text-color, #333333);
}
.ds-snackbar--complex.ds-snackbar--dark {
  width: 232px;
  background: var(--ds-color-snackbar-complex-dark-background, #424242);
  color: var(--ds-color-snackbar-complex-dark-text-color, #ffffff);
}
.ds-snackbar--complex.ds-snackbar--light {
  width: 370px;
  background: var(--ds-color-snackbar-complex-light-background, #ffffff);
  color: var(--ds-color-snackbar-complex-light-text-color, #333333);
}

.ds-state {
  height: var(--ds-size-6x);
  width: var(--ds-size-6x);
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-state:hover {
  background: #ebebeb;
}
.ds-state:active {
  background: #e0e0e0;
}

.ds-status {
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-status-gap, 4px);
  border-radius: var(--ds-status-border-radius, 8px);
  padding: var(--ds-status-pad-top, 4px) var(--ds-status-pad-right, 6px) var(--ds-status-pad-bottom, 4px) var(--ds-status-pad-left, 6px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-status__label {
  font-size: var(--ds-font-caption-l-12-normal-medium-size);
  line-height: var(--ds-font-caption-l-12-normal-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-medium-weight);
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
  white-space: nowrap;
}
.ds-status__icon {
  flex-shrink: 0;
  width: var(--ds-size-4x);
  height: var(--ds-size-4x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-status-icon-color);
}
.ds-status__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-status__icon svg path {
  fill: currentColor;
}
.ds-status__element-left {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-status__info {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-status__content {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-status-neutral-filled-text-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-medium-size);
  line-height: var(--ds-font-caption-l-12-normal-medium-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-medium-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-medium-weight);
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
}
.ds-status__element-right {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
}
.ds-status--neutral.ds-status--filled {
  background: var(--ds-color-status-neutral-filled-background, #fafafa);
  color: var(--ds-color-status-neutral-filled-text-color, #616161);
}
.ds-status--accent.ds-status--filled {
  background: var(--ds-color-status-accent-filled-background, #f5f9ff);
  color: var(--ds-color-status-accent-filled-text-color, #448aff);
}
.ds-status--positive.ds-status--filled {
  background: var(--ds-color-status-positive-filled-background, #f3fcf7);
  color: var(--ds-color-status-positive-filled-text-color, #14b456);
}
.ds-status--warning.ds-status--filled {
  background: var(--ds-color-status-warning-filled-background, #fffcf8);
  color: var(--ds-color-status-warning-filled-text-color, #ea7806);
}
.ds-status--negative.ds-status--filled {
  background: var(--ds-color-status-negative-filled-background, #fff8f8);
  color: var(--ds-color-status-negative-filled-text-color, #ff5252);
}
.ds-status--contrast-1.ds-status--filled {
  background: var(--ds-color-status-contrast-1-filled-background, #fcf6fd);
  color: var(--ds-color-status-contrast-1-filled-text-color, #9c27b0);
}
.ds-status--contrast-2.ds-status--filled {
  background: var(--ds-color-status-contrast-2-filled-background, #fcf8f6);
  color: var(--ds-color-status-contrast-2-filled-text-color, #3e261e);
}
.ds-status--contrast-3.ds-status--filled {
  background: var(--ds-color-status-contrast-3-filled-background, #f8fafc);
  color: var(--ds-color-status-contrast-3-filled-text-color, #263136);
}
.ds-status--contrast-4.ds-status--filled {
  background: var(--ds-color-status-contrast-4-filled-background, #f9fbea);
  color: var(--ds-color-status-contrast-4-filled-text-color, #4f5412);
}
.ds-status--neutral.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-neutral-text-text-color, #616161);
}
.ds-status--accent.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-accent-text-text-color, #448aff);
}
.ds-status--positive.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-positive-text-text-color, #14b456);
}
.ds-status--warning.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-warning-text-text-color, #ea7806);
}
.ds-status--negative.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-negative-text-text-color, #ff5252);
}
.ds-status--contrast-1.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-1-text-text-color, #9c27b0);
}
.ds-status--contrast-2.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-2-text-text-color, #3e261e);
}
.ds-status--contrast-3.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-3-text-text-color, #263136);
}
.ds-status--contrast-4.ds-status--text {
  padding: var(--ds-status-pad-top-text) var(--ds-status-pad-right-text) var(--ds-status-pad-bottom-text) var(--ds-status-pad-left-text);
  color: var(--ds-color-status-contrast-4-text-text-color, #4f5412);
}

.ds-table-2-lvl {
  min-height: 72px;
  display: flex;
  width: 162px;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-2-lvl__header-row {
  display: flex;
  flex-direction: column;
  background: var(--ds-color-table-row-header-background-header, #f0f5ff);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
}
.ds-table-2-lvl--table-cell-2-lvl {
  flex-direction: column;
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
}
.ds-table-2-lvl--table-row-2-lvl {
  width: fit-content;
  flex-direction: row;
  align-items: center;
}

.ds-table-chips-input {
  min-height: var(--ds-size-6x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-chips-input__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: #616161;
  white-space: nowrap;
}
.ds-table-chips-input__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-chips-icon-color);
}
.ds-table-chips-input__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-table-chips-input__icon svg path {
  fill: currentColor;
}
.ds-table-chips-input__frame {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-chips-input-gap-chips-input-frame, 4px);
  border-radius: var(--ds-size-3x);
  background: #f8f9fc;
  border: 1px solid #e0e0e0;
}
.ds-table-chips-input__support {
  display: flex;
  flex-direction: row;
  gap: var(--ds-size-1x);
}
.ds-table-chips-input--default {
  color: #616161;
}
.ds-table-chips-input--hover {
  color: #616161;
}
.ds-table-chips-input--focus {
  color: #333333;
}
.ds-table-chips-input--focus-placeholder {
  color: #333333;
}
.ds-table-chips-input--vocus-value {
  color: #333333;
}
.ds-table-chips-input--error {
  color: #616161;
}
.ds-table-chips-input--error-hover {
  color: #616161;
}
.ds-table-chips-input--disable {
  color: #9e9e9e;
}

.ds-table-content-cell {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-content-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-table-content-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-table-content-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-table-content-cell__icon svg path {
  fill: currentColor;
}
.ds-table-content-cell__element {
  display: flex;
  flex-direction: row;
}
.ds-table-content-cell__text-ui {
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
}
.ds-table-content-cell:disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-cell.ds-table-content-cell--disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-cell:hover {
  border: 1px solid var(--ds-color-table-cell-content-hover-border-color, #9e9e9e);
}
.ds-table-content-cell--disabled {
  pointer-events: none;
}

.ds-table-content-row {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  background: var(--ds-color-table-row-content-default-background, #ffffff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-content-row__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-table-content-row:disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-row.ds-table-content-row--disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-content-row:hover {
  background: var(--ds-color-table-row-content-hover-background, #f5f5f5);
}
.ds-table-content-row--disabled {
  pointer-events: none;
}

.ds-table-footer {
  height: 65px;
  width: 980px;
  display: flex;
  flex-direction: column;
  background: var(--ds-color-table-footer-background, #ffffff);
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-footer__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
  white-space: nowrap;
}
.ds-table-footer__divider {
  height: var(--ds-size-0-25x);
  display: flex;
  flex-direction: column;
  background: #ffffff;
}
.ds-table-footer__content {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: var(--ds-table-footer-pad-top, 12px) var(--ds-table-footer-pad-right, 32px) var(--ds-table-footer-pad-bottom, 12px) var(--ds-table-footer-pad-left, 32px);
  background: #ffffff;
}
.ds-table-footer--default {
  color: var(--ds-color-expansion-panel-content-text-color, #333333);
}

.ds-table-header-cell {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2x);
  padding: var(--ds-table-cell-pad-top, 8px) var(--ds-table-cell-pad-right, 8px) var(--ds-table-cell-pad-bottom, 8px) var(--ds-table-cell-pad-left, 8px);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  background: var(--ds-color-table-cell-header-default-background, #f0f5ff);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-header-cell__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-table-header-cell__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-table-header-cell__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-table-header-cell__icon svg path {
  fill: currentColor;
}
.ds-table-header-cell__element {
  display: flex;
  flex-direction: row;
}
.ds-table-header-cell__text-ui {
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
}
.ds-table-header-cell:hover {
  background: var(--ds-color-table-cell-header-hover-background, #f8f9fc);
}
.ds-table-header-cell:disabled {
  background: var(--ds-color-table-cell-header-disable-background, #f0f5ff);
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-header-cell.ds-table-header-cell--disabled {
  background: var(--ds-color-table-cell-header-disable-background, #f0f5ff);
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-table-header-cell--disabled {
  pointer-events: none;
}

.ds-table-header-row {
  min-height: var(--ds-size-9x);
  width: fit-content;
  display: flex;
  flex-direction: column;
  border-radius: var(--ds-table-row-header-border-radius-top-left);
  background: var(--ds-color-table-row-header-background-header, #f0f5ff);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-table-header-row__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}

.ds-text-ui {
  min-height: 52px;
  width: fit-content;
  display: flex;
  flex-direction: row;
  gap: var(--ds-list-item-gap, 8px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-text-ui__label {
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
  white-space: nowrap;
}
.ds-text-ui__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-text-ui__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-text-ui__icon svg path {
  fill: currentColor;
}
.ds-text-ui__element-left {
  display: flex;
  flex-direction: row;
  background: #ffffff;
}
.ds-text-ui__checkbox {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-text-ui__content {
  display: flex;
  flex-direction: column;
}
.ds-text-ui__label-up {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-ui-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-text-ui-text-label-color, #616161);
}
.ds-text-ui__list-item {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-ui-text-color, #333333);
  font-size: var(--ds-font-body-s-14-normal-regular-size);
  line-height: var(--ds-font-body-s-14-normal-regular-line);
  letter-spacing: var(--ds-font-body-s-14-normal-regular-spacing);
  font-weight: var(--ds-font-body-s-14-normal-regular-weight);
  color: var(--ds-color-text-ui-text-color, #333333);
}
.ds-text-ui__label-down {
  display: flex;
  flex-direction: row;
  background: var(--ds-color-text-ui-text-label-color, #616161);
  font-size: var(--ds-font-caption-l-12-normal-regular-size);
  line-height: var(--ds-font-caption-l-12-normal-regular-line);
  letter-spacing: var(--ds-font-caption-l-12-normal-regular-spacing);
  font-weight: var(--ds-font-caption-l-12-normal-regular-weight);
  color: var(--ds-color-text-ui-text-label-color, #616161);
}
.ds-text-ui__element-right {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  background: #ffffff;
}
.ds-text-ui__icon-size {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-text-ui:disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-text-ui.ds-text-ui--disabled {
  color: var(--ds-color-text-ui-disable-label-text-color, #9e9e9e);
}
.ds-text-ui--disabled {
  pointer-events: none;
}

.ds-textarea {
  min-height: 96px;
  width: 250px;
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-support, 4px);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-textarea__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-form-field-filled-default-input-text-color, #333333);
  white-space: nowrap;
}
.ds-textarea__icon {
  flex-shrink: 0;
  width: var(--ds-size-5x);
  height: var(--ds-size-5x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-textarea__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-textarea__icon svg path {
  fill: currentColor;
}
.ds-textarea__input-frame {
  height: 76px;
  display: flex;
  flex-direction: row;
  gap: var(--ds-form-field-gap-input-frame, 8px);
  padding: var(--ds-form-field-pad-textarea-top, 4px) var(--ds-form-field-m-size-pad-input-right, 12px) var(--ds-form-field-m-size-pad-input-bottom, 12px) var(--ds-form-field-m-size-pad-input-left, 12px);
  border-radius: var(--ds-form-field-border-radius, 12px);
  background: var(--ds-color-form-field-input-filled-background, #f8f9fc);
  border: 1px solid var(--ds-color-form-field-filled-default-border-color, #e0e0e0);
}
.ds-textarea__element-left {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-textarea__input-content {
  display: flex;
  flex-direction: column;
  gap: var(--ds-form-field-gap-input-content);
}
.ds-textarea__element-right {
  height: var(--ds-size-5x);
  display: flex;
  flex-direction: row;
}
.ds-textarea__scroll {
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-textarea__support {
  display: flex;
  flex-direction: row;
}
.ds-textarea__text {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-textarea__hint {
  height: var(--ds-size-4x);
  display: flex;
  flex-direction: row;
  padding: 0 var(--ds-form-field-pad-support-right, 12px) 0 var(--ds-form-field-pad-support-left, 12px);
}
.ds-textarea--populated:disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-textarea--populated.ds-textarea--disabled {
  color: var(--ds-color-form-field-filled-disable-label-text-color, #9e9e9e);
}
.ds-textarea--empty:disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-textarea--empty.ds-textarea--disabled {
  color: var(--ds-color-form-field-filled-disable-input-text-color, #9e9e9e);
}
.ds-textarea--populated:focus-visible {
  color: var(--ds-color-form-field-filled-focus-label-text-color, #448aff);
}
.ds-textarea--populated {
  color: var(--ds-color-form-field-filled-default-label-text-color, #616161);
}
.ds-textarea--empty {
  color: var(--ds-color-form-field-input-label-text-color, #616161);
}
.ds-textarea--populated:hover {
  color: var(--ds-color-form-field-filled-hover-label-text-color, #616161);
}
.ds-textarea--empty:hover {
  background: var(--ds-color-form-field-filled-hover-input-background-hover, #f5f5f5);
  border: 1px solid var(--ds-color-form-field-filled-hover-border-color, #9e9e9e);
}
.ds-textarea--disabled {
  pointer-events: none;
}

.ds-timepicker {
  width: fit-content;
  display: flex;
  padding: var(--ds-size-2x) 0 var(--ds-size-2x) 0;
  border-radius: var(--ds-size-3x);
  background: var(--ds-color-brand-neutral-default, #ffffff);
  border: 1px solid var(--ds-color-stroke-default, #e0e0e0);
  box-shadow: var(--ds-shadow-shadows-08-dp-s);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-timepicker__label {
  font-size: var(--ds-font-body-m-16-normal-regular-size);
  line-height: var(--ds-font-body-m-16-normal-regular-line);
  letter-spacing: var(--ds-font-body-m-16-normal-regular-spacing);
  font-weight: var(--ds-font-body-m-16-normal-regular-weight);
  color: var(--ds-color-text-primary, #333333);
  white-space: nowrap;
}
.ds-timepicker__icon {
  flex-shrink: 0;
  width: var(--ds-size-3x);
  height: var(--ds-size-3x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-timepicker__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-timepicker__icon svg path {
  fill: currentColor;
}
.ds-timepicker__control-panel {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.ds-timepicker__scroll {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: var(--ds-scroll-pad-top, 2px) var(--ds-scroll-pad-right, 2px) var(--ds-scroll-pad-bottom, 2px) var(--ds-scroll-pad-left, 2px);
}
.ds-timepicker--time-grid {
  flex-direction: column;
  align-items: center;
  color: var(--ds-color-text-primary, #333333);
}
.ds-timepicker--time-line {
  flex-direction: row;
  color: var(--ds-color-text-primary, #333333);
}

.ds-tree {
  height: 44px;
  width: fit-content;
  display: flex;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-tree__icon {
  flex-shrink: 0;
  width: var(--ds-size-6x);
  height: var(--ds-size-6x);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.ds-tree__icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ds-tree__icon svg path {
  fill: currentColor;
}
.ds-tree__item {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-size-2-5x);
  padding: 0 0 var(--ds-size-5x) 11px;
}
.ds-tree__separator-stroke {
  height: 100%;
  display: flex;
  flex-direction: row;
  background: #d7d8d9;
}
.ds-tree--2.ds-tree--end.ds-tree--on {
  flex-direction: row;
}
.ds-tree--2.ds-tree--end.ds-tree--off {
  flex-direction: column;
}
.ds-tree--3.ds-tree--end.ds-tree--on {
  flex-direction: row;
}
.ds-tree--3.ds-tree--end.ds-tree--off {
  flex-direction: row;
}
.ds-tree--2.ds-tree--middle.ds-tree--on {
  flex-direction: row;
  align-items: center;
}
.ds-tree--2.ds-tree--middle.ds-tree--off {
  flex-direction: row;
  align-items: center;
}
.ds-tree--3.ds-tree--middle.ds-tree--on {
  flex-direction: row;
  align-items: center;
}
.ds-tree--3.ds-tree--middle.ds-tree--off {
  flex-direction: row;
  align-items: center;
}

.ds-tree-item {
  height: 44px;
  display: flex;
  width: fit-content;
  padding: 0 0 var(--ds-size-5x) 11px;
  gap: var(--ds-size-2-5x);
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}
.ds-tree-item__separator-stroke {
  height: 100%;
  display: flex;
  flex-direction: row;
  background: #d7d8d9;
}
.ds-tree-item--end {
  flex-direction: row;
  align-items: center;
}
.ds-tree-item--end-long {
  width: 48px;
  flex-direction: column;
  padding: 0 0 21px 11px;
}
.ds-tree-item--middle {
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 11px;
}
.ds-tree-item--middle-long {
  width: 48px;
  flex-direction: row;
  align-items: center;
  padding: 0 0 0 11px;
}
.ds-tree-item--start {
  width: var(--ds-size-6x);
  flex-direction: row;
  align-items: center;
  padding: 0 var(--ds-size-3x) 0 11px;
}

.ds-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  border: 1px solid transparent;
  border-radius: var(--ds-radius-2x);            
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  font-size: var(--ds-typography-font-size-3-5x); 
  font-weight: var(--ds-typography-font-weight-medium); 
  letter-spacing: var(--ds-typography-letter-spacing-s); 
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  user-select: none;
  transition: background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease;
}

.ds-btn:focus-visible {
  outline: 2px solid var(--ds-palette-accent-300);
  outline-offset: 2px;
}

.ds-btn:disabled,
.ds-btn--disabled {
  pointer-events: none;
}

.ds-btn--xs {
  height: 24px;
  padding: 4px 6px;
  gap: var(--ds-space-1x);                        
  font-size: var(--ds-typography-font-size-3x);   
}
.ds-btn--xs 
.ds-btn__label {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.ds-btn__icon { font-size: 16px; }

.ds-btn--s {
  height: 28px;
  padding: 4px 8px;
  gap: var(--ds-space-1x);
}
.ds-btn--s .ds-btn__icon { font-size: 20px; }

.ds-btn--m {
  height: 36px;
  padding: 8px 12px;
  gap: var(--ds-space-2x);                        
}
.ds-btn--m .ds-btn__icon { font-size: 20px; }

.ds-btn-group {
  display: flex;
}
.ds-btn-group--horizontal { flex-direction: row; gap: var(--ds-button-group-gap); }    
.ds-btn-group--vertical   { flex-direction: column; gap: var(--ds-button-group-gap); } 
.ds-btn-group--margins {
  padding: var(--ds-button-group-margins-pad-top) var(--ds-button-group-margins-pad-right); 
}

.ds-btn__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-size: 20px;
  line-height: 1;
}

.ds-btn--accent.ds-btn--filled {
  background: var(--ds-color-button-accent-default);   
  color: var(--ds-color-text-inversive);               
}
.ds-btn--accent.ds-btn--filled:hover  { background: var(--ds-color-button-accent-hover); }   
.ds-btn--accent.ds-btn--filled:active { background: var(--ds-color-button-accent-press); }   

.ds-btn--accent.ds-btn--outlined {
  background: var(--ds-color-button-accent-lite-default); 
  border-color: var(--ds-color-button-accent-default);
  color: var(--ds-color-button-accent-default);
}
.ds-btn--accent.ds-btn--outlined:hover  { background: var(--ds-color-button-accent-lite-hover); } 
.ds-btn--accent.ds-btn--outlined:active { background: var(--ds-color-button-accent-lite-press); } 

.ds-btn--accent.ds-btn--text {
  background: var(--ds-color-button-accent-lite-default);
  color: var(--ds-color-button-accent-default);
}
.ds-btn--accent.ds-btn--text:hover  { background: var(--ds-color-button-accent-lite-hover); }
.ds-btn--accent.ds-btn--text:active { background: var(--ds-color-button-accent-lite-press); }

.ds-btn--neutral.ds-btn--filled {
  background: var(--ds-color-button-neutral-default); 
  color: var(--ds-color-text-primary);                
}
.ds-btn--neutral.ds-btn--filled:hover  { background: var(--ds-color-button-neutral-hover); } 
.ds-btn--neutral.ds-btn--filled:active { background: var(--ds-color-button-neutral-press); } 

.ds-btn--neutral.ds-btn--outlined {
  background: var(--ds-color-button-neutral-default);
  border-color: var(--ds-color-stroke-default);      
  color: var(--ds-color-text-primary);
}
.ds-btn--neutral.ds-btn--outlined:hover  { background: var(--ds-color-button-neutral-hover); }
.ds-btn--neutral.ds-btn--outlined:active { background: var(--ds-color-button-neutral-press); }

.ds-btn--neutral.ds-btn--text {
  background: var(--ds-color-button-neutral-default);
  color: var(--ds-color-text-primary);
}
.ds-btn--neutral.ds-btn--text:hover  { background: var(--ds-color-button-neutral-hover); }
.ds-btn--neutral.ds-btn--text:active { background: var(--ds-color-button-neutral-press); }

.ds-btn--positive.ds-btn--filled {
  background: var(--ds-color-button-positive-default); 
  color: var(--ds-color-text-inversive);
}
.ds-btn--positive.ds-btn--filled:hover  { background: var(--ds-color-button-positive-hover); } 
.ds-btn--positive.ds-btn--filled:active { background: var(--ds-color-button-positive-press); } 

.ds-btn--positive.ds-btn--outlined {
  background: var(--ds-color-button-positive-lite-default);
  border-color: var(--ds-color-button-positive-default);
  color: var(--ds-color-button-positive-default);
}
.ds-btn--positive.ds-btn--outlined:hover  { background: var(--ds-color-button-positive-lite-hover); } 
.ds-btn--positive.ds-btn--outlined:active { background: var(--ds-color-button-positive-lite-press); } 

.ds-btn--positive.ds-btn--text {
  background: var(--ds-color-button-positive-lite-default);
  color: var(--ds-color-button-positive-default);
}
.ds-btn--positive.ds-btn--text:hover  { background: var(--ds-color-button-positive-lite-hover); }
.ds-btn--positive.ds-btn--text:active { background: var(--ds-color-button-positive-lite-press); }

.ds-btn--negative.ds-btn--filled {
  background: var(--ds-color-button-negative-default); 
  color: var(--ds-color-text-inversive);
}
.ds-btn--negative.ds-btn--filled:hover  { background: var(--ds-color-button-negative-hover); } 
.ds-btn--negative.ds-btn--filled:active { background: var(--ds-color-button-negative-press); } 

.ds-btn--negative.ds-btn--outlined {
  background: var(--ds-color-button-negative-lite-default);
  border-color: var(--ds-color-button-negative-default);
  color: var(--ds-color-button-negative-default);
}
.ds-btn--negative.ds-btn--outlined:hover  { background: var(--ds-color-button-negative-lite-hover); } 
.ds-btn--negative.ds-btn--outlined:active { background: var(--ds-color-button-negative-lite-press); } 

.ds-btn--negative.ds-btn--text {
  background: var(--ds-color-button-negative-lite-default);
  color: var(--ds-color-button-negative-default);
}
.ds-btn--negative.ds-btn--text:hover  { background: var(--ds-color-button-negative-lite-hover); }
.ds-btn--negative.ds-btn--text:active { background: var(--ds-color-button-negative-lite-press); }

.ds-btn--warning.ds-btn--filled {
  background: var(--ds-color-button-warning-default); 
  color: var(--ds-color-text-inversive);
}
.ds-btn--warning.ds-btn--filled:hover  { background: var(--ds-color-button-warning-hover); } 
.ds-btn--warning.ds-btn--filled:active { background: var(--ds-color-button-warning-press); } 

.ds-btn--warning.ds-btn--outlined {
  background: var(--ds-color-button-warning-lite-default);
  border-color: var(--ds-color-button-warning-default);
  color: var(--ds-color-button-warning-press);      
}
.ds-btn--warning.ds-btn--outlined:hover  { background: var(--ds-color-button-warning-lite-hover); } 
.ds-btn--warning.ds-btn--outlined:active { background: var(--ds-color-button-warning-lite-press); } 

.ds-btn--warning.ds-btn--text {
  background: var(--ds-color-button-warning-lite-default);
  color: var(--ds-color-button-warning-press);
}
.ds-btn--warning.ds-btn--text:hover  { background: var(--ds-color-button-warning-lite-hover); }
.ds-btn--warning.ds-btn--text:active { background: var(--ds-color-button-warning-lite-press); }

.ds-btn--filled:disabled,
.ds-btn--filled.ds-btn--disabled {
  background: var(--ds-color-button-neutral-disable); 
  color: var(--ds-color-text-disable);                
}

.ds-btn--outlined:disabled,
.ds-btn--outlined.ds-btn--disabled {
  background: var(--ds-color-button-neutral-default);
  border-color: var(--ds-color-button-neutral-disable);
  color: var(--ds-color-text-disable);
}

.ds-btn--text:disabled,
.ds-btn--text.ds-btn--disabled {
  background: var(--ds-color-button-neutral-default);
  color: var(--ds-color-text-disable);
}

.ds-btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  flex-shrink: 0;
  width: var(--ds-size-9x);                    
  height: var(--ds-size-9x);
  padding: var(--ds-space-2x);                 
  border: 1px solid transparent;
  border-radius: var(--ds-radius-2x);          
  background: none;
  cursor: pointer;
  transition: background-color .12s ease, border-color .12s ease;
}

.ds-btn-icon__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--ds-size-5x);                    
  height: var(--ds-size-5x);
  flex-shrink: 0;                              
}
.ds-btn-icon__icon svg { width: 100%; height: 100%; display: block; }
.ds-btn-icon__icon svg path { fill: currentColor; }

.ds-btn-icon--m {
  width: var(--ds-size-9x);                    
  height: var(--ds-size-9x);
  padding: var(--ds-space-2x);                 
}
.ds-btn-icon--s {
  width: var(--ds-size-7x);                    
  height: var(--ds-size-7x);
  padding: var(--ds-space-1x);                 
}
.ds-btn-icon--xs {
  width: var(--ds-size-6x);                    
  height: var(--ds-size-6x);
  padding: var(--ds-space-1x);                 
}
.ds-btn-icon--xs .ds-btn-icon__icon {
  width: var(--ds-size-4x);                    
  height: var(--ds-size-4x);
  flex-shrink: 0;                              
}

.ds-btn-icon:disabled,
.ds-btn-icon--disabled {
  pointer-events: none;
  background: var(--ds-color-button-icon-disable-background-filled);
  border-color: var(--ds-color-button-icon-disable-border-color);
  color: var(--ds-color-button-icon-disable-icon-color);
}
.ds-btn-icon--outlined:disabled,
.ds-btn-icon--outlined.ds-btn-icon--disabled {
  background: var(--ds-color-button-icon-disable-background-outlined);
}
.ds-btn-icon--text:disabled,
.ds-btn-icon--text.ds-btn-icon--disabled {
  background: var(--ds-color-button-icon-disable-background-text);
  border-color: transparent;
}

.ds-btn-icon-group {
  display: inline-flex;
  flex-direction: row;
  align-items: center;
  gap: var(--ds-space-2x);                     
}
.ds-btn-icon-group--vertically {
  flex-direction: column;
}

.ds-btn-icon--accent.ds-btn-icon--filled {
  background: var(--ds-color-button-icon-accent-filled-default-background);
  color: var(--ds-color-button-icon-accent-filled-icon-color);
}
.ds-btn-icon--accent.ds-btn-icon--filled:hover {
  background: var(--ds-color-button-icon-accent-filled-hover-background);
}
.ds-btn-icon--accent.ds-btn-icon--filled:active {
  background: var(--ds-color-button-icon-accent-filled-press-background);
}
.ds-btn-icon--accent.ds-btn-icon--outlined {
  background: var(--ds-color-button-icon-accent-outlined-default-background);
  color: var(--ds-color-button-icon-accent-outlined-icon-color);
  border-color: var(--ds-color-button-icon-accent-outlined-border-color);
}
.ds-btn-icon--accent.ds-btn-icon--outlined:hover {
  background: var(--ds-color-button-icon-accent-outlined-hover-background);
}
.ds-btn-icon--accent.ds-btn-icon--outlined:active {
  background: var(--ds-color-button-icon-accent-outlined-press-background);
}
.ds-btn-icon--accent.ds-btn-icon--text {
  background: var(--ds-color-button-icon-accent-text-default-background);
  color: var(--ds-color-button-icon-accent-text-icon-color);
}
.ds-btn-icon--accent.ds-btn-icon--text:hover {
  background: var(--ds-color-button-icon-accent-text-hover-background);
}
.ds-btn-icon--accent.ds-btn-icon--text:active {
  background: var(--ds-color-button-icon-accent-text-press-background);
}
.ds-btn-icon--negative.ds-btn-icon--filled {
  background: var(--ds-color-button-icon-negative-filled-default-background);
  color: var(--ds-color-button-icon-negative-filled-icon-color);
}
.ds-btn-icon--negative.ds-btn-icon--filled:hover {
  background: var(--ds-color-button-icon-negative-filled-hover-background);
}
.ds-btn-icon--negative.ds-btn-icon--filled:active {
  background: var(--ds-color-button-icon-negative-filled-press-background);
}
.ds-btn-icon--negative.ds-btn-icon--outlined {
  background: var(--ds-color-button-icon-negative-outlined-default-background);
  color: var(--ds-color-button-icon-negative-outlined-icon-color);
  border-color: var(--ds-color-button-icon-negative-outlined-border-color);
}
.ds-btn-icon--negative.ds-btn-icon--outlined:hover {
  background: var(--ds-color-button-icon-negative-outlined-hover-background);
}
.ds-btn-icon--negative.ds-btn-icon--outlined:active {
  background: var(--ds-color-button-icon-negative-outlined-press-background);
}
.ds-btn-icon--negative.ds-btn-icon--text {
  background: var(--ds-color-button-icon-negative-text-default-background);
  color: var(--ds-color-button-icon-negative-text-icon-color);
}
.ds-btn-icon--negative.ds-btn-icon--text:hover {
  background: var(--ds-color-button-icon-negative-text-hover-background);
}
.ds-btn-icon--negative.ds-btn-icon--text:active {
  background: var(--ds-color-button-icon-negative-text-press-background);
}
.ds-btn-icon--neutral.ds-btn-icon--filled {
  background: var(--ds-color-button-icon-neutral-filled-default-background);
  color: var(--ds-color-button-icon-neutral-filled-icon-color);
}
.ds-btn-icon--neutral.ds-btn-icon--filled:hover {
  background: var(--ds-color-button-icon-neutral-filled-hover-background);
}
.ds-btn-icon--neutral.ds-btn-icon--filled:active {
  background: var(--ds-color-button-icon-neutral-filled-press-background);
}
.ds-btn-icon--neutral.ds-btn-icon--outlined {
  background: var(--ds-color-button-icon-neutral-outlined-default-background);
  color: var(--ds-color-button-icon-neutral-outlined-icon-color);
  border-color: var(--ds-color-button-icon-neutral-outlined-border-color);
}
.ds-btn-icon--neutral.ds-btn-icon--outlined:hover {
  background: var(--ds-color-button-icon-neutral-outlined-hover-background);
}
.ds-btn-icon--neutral.ds-btn-icon--outlined:active {
  background: var(--ds-color-button-icon-neutral-outlined-press-background);
}
.ds-btn-icon--neutral.ds-btn-icon--text {
  background: var(--ds-color-button-icon-neutral-text-default-background);
  color: var(--ds-color-button-icon-neutral-text-icon-color);
}
.ds-btn-icon--neutral.ds-btn-icon--text:hover {
  background: var(--ds-color-button-icon-neutral-text-hover-background);
}
.ds-btn-icon--neutral.ds-btn-icon--text:active {
  background: var(--ds-color-button-icon-neutral-text-press-background);
}
.ds-btn-icon--positive.ds-btn-icon--filled {
  background: var(--ds-color-button-icon-positive-filled-default-background);
  color: var(--ds-color-button-icon-positive-filled-icon-color);
}
.ds-btn-icon--positive.ds-btn-icon--filled:hover {
  background: var(--ds-color-button-icon-positive-filled-hover-background);
}
.ds-btn-icon--positive.ds-btn-icon--filled:active {
  background: var(--ds-color-button-icon-positive-filled-press-background);
}
.ds-btn-icon--positive.ds-btn-icon--outlined {
  background: var(--ds-color-button-icon-positive-outlined-default-background);
  color: var(--ds-color-button-icon-positive-outlined-icon-color);
  border-color: var(--ds-color-button-icon-positive-outlined-border-color);
}
.ds-btn-icon--positive.ds-btn-icon--outlined:hover {
  background: var(--ds-color-button-icon-positive-outlined-hover-background);
}
.ds-btn-icon--positive.ds-btn-icon--outlined:active {
  background: var(--ds-color-button-icon-positive-outlined-press-background);
}
.ds-btn-icon--positive.ds-btn-icon--text {
  background: var(--ds-color-button-icon-positive-text-default-background);
  color: var(--ds-color-button-icon-positive-text-icon-color);
}
.ds-btn-icon--positive.ds-btn-icon--text:hover {
  background: var(--ds-color-button-icon-positive-text-hover-background);
}
.ds-btn-icon--positive.ds-btn-icon--text:active {
  background: var(--ds-color-button-icon-positive-text-press-background);
}
.ds-btn-icon--warning.ds-btn-icon--filled {
  background: var(--ds-color-button-icon-warning-filled-default-background);
  color: var(--ds-color-button-icon-warning-filled-icon-color);
}
.ds-btn-icon--warning.ds-btn-icon--filled:hover {
  background: var(--ds-color-button-icon-warning-filled-hover-background);
}
.ds-btn-icon--warning.ds-btn-icon--filled:active {
  background: var(--ds-color-button-icon-warning-filled-press-background);
}
.ds-btn-icon--warning.ds-btn-icon--outlined {
  background: var(--ds-color-button-icon-warning-outlined-default-background);
  color: var(--ds-color-button-icon-warning-outlined-icon-color);
  border-color: var(--ds-color-button-icon-warning-outlined-border-color);
}
.ds-btn-icon--warning.ds-btn-icon--outlined:hover {
  background: var(--ds-color-button-icon-warning-outlined-hover-background);
}
.ds-btn-icon--warning.ds-btn-icon--outlined:active {
  background: var(--ds-color-button-icon-warning-outlined-press-background);
}
.ds-btn-icon--warning.ds-btn-icon--text {
  background: var(--ds-color-button-icon-warning-text-default-background);
  color: var(--ds-color-button-icon-warning-text-icon-color);
}
.ds-btn-icon--warning.ds-btn-icon--text:hover {
  background: var(--ds-color-button-icon-warning-text-hover-background);
}
.ds-btn-icon--warning.ds-btn-icon--text:active {
  background: var(--ds-color-button-icon-warning-text-press-background);
}

.ds-input {
  display: flex;
  flex-direction: column;
  gap: var(--ds-space-1x);            
  width: 100%;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-input__frame {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);            
  box-sizing: border-box;
  border: 1px solid var(--ds-color-stroke-default);   
  border-radius: var(--ds-radius-3x);                 
  background: var(--ds-color-shapes-default-variant); 
  transition: background-color 0.15s ease, border-color 0.15s ease;
}

.ds-input--m .ds-input__frame { height: 48px; padding: 12px; }               
.ds-input--s .ds-input__frame { height: 36px; padding: 6px 12px; }           
.ds-input--xs .ds-input__frame {
  height: 28px;
  padding: 4px 8px;                 
  border-radius: var(--ds-radius-0);   
  background: transparent;             
}

.ds-input__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-size: 20px;                   
  color: var(--ds-color-icon-primary);  
}

.ds-input__content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
  min-width: 0;
}

.ds-input__label {
  font-size: var(--ds-typography-font-size-3x);    
  font-weight: var(--ds-typography-font-weight-regular);
  letter-spacing: var(--ds-typography-letter-spacing-s);
  line-height: 16px;
  color: var(--ds-color-text-secondary);           
  transition: color 0.15s ease;
}

.ds-input__field {
  width: 100%;
  box-sizing: border-box;
  border: none;
  outline: none;
  background: transparent;
  padding: 0;
  font-family: inherit;
  font-size: var(--ds-typography-font-size-4x);    
  font-weight: var(--ds-typography-font-weight-regular);
  letter-spacing: var(--ds-typography-letter-spacing-s);
  line-height: 24px;
  color: var(--ds-color-text-primary);             
}

.ds-input--xs .ds-input__field {
  font-size: var(--ds-typography-font-size-3-5x);  
  line-height: 20px;
}
.ds-input--xs .ds-input__label,
.ds-input--s  .ds-input__label { display: none; }  

.ds-input__field::placeholder {
  color: var(--ds-color-text-placeholder);         
  opacity: 1;
}

.ds-input__support-row {
  display: flex;
  align-items: center;
  justify-content: space-between;   
}

.ds-input__support,
.ds-input__hint {
  font-size: var(--ds-typography-font-size-3x);    
  font-weight: var(--ds-typography-font-weight-regular);
  letter-spacing: var(--ds-typography-letter-spacing-s);
  line-height: 16px;
  color: var(--ds-color-text-secondary);           
  transition: color 0.15s ease;
}

.ds-input__frame:hover {
  background: var(--ds-color-shapes-hover);        
  border-color: var(--ds-color-stroke-hover);      
}

.ds-input__frame:focus-within {
  background: var(--ds-color-shapes-default-variant); 
  border-color: var(--ds-color-stroke-accent);        
}
.ds-input__frame:focus-within .ds-input__label { color: var(--ds-color-text-accent); }

.ds-input--error .ds-input__frame {
  border-color: var(--ds-color-stroke-negative);   
  background: var(--ds-color-shapes-default-variant);
}
.ds-input--error .ds-input__frame:hover {
  background: var(--ds-color-shapes-hover);        
}
.ds-input--error .ds-input__label,
.ds-input--error .ds-input__support {
  color: var(--ds-color-text-negative);            
}

.ds-input--disabled .ds-input__frame,
.ds-input--disabled .ds-input__frame:hover {
  background: var(--ds-color-surface-disable);     
  border-color: var(--ds-color-stroke-disable);    
}
.ds-input--disabled .ds-input__label,
.ds-input--disabled .ds-input__field,
.ds-input--disabled .ds-input__support,
.ds-input--disabled .ds-input__hint,
.ds-input--disabled .ds-input__icon {
  color: var(--ds-color-text-disable);             
}
.ds-input--disabled .ds-input__field { cursor: not-allowed; }

.ds-checkbox,
.ds-radio {
  display: inline-flex;
  align-items: center;
  gap: var(--ds-space-2x);              
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  cursor: pointer;
  user-select: none;
}

.ds-checkbox__input,
.ds-radio__input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
  pointer-events: none;
}

.ds-checkbox__box,
.ds-radio__box {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  font-size: 20px;
  line-height: 1;
  color: var(--ds-color-icon-primary);            
  transition: color 0.15s ease;
}

.ds-checkbox__box::before { content: 'check_box_outline_blank'; }

.ds-checkbox__label,
.ds-radio__label {
  font-size: var(--ds-typography-font-size-3-5x); 
  font-weight: var(--ds-typography-font-weight-regular);
  letter-spacing: 0.25px;
  line-height: 20px;
  color: var(--ds-color-text-primary);            
}
.ds-checkbox__label { color: var(--ds-color-checkbox-label-text-color); }
.ds-radio__label { color: var(--ds-color-radio-button-label-text-color); }

.ds-checkbox__box { color: var(--ds-color-checkbox-normal-deselected-icon-color); }
.ds-checkbox__input:checked ~ .ds-checkbox__box {
  color: var(--ds-color-checkbox-normal-selected-icon-color);             
}
.ds-checkbox__input:indeterminate ~ .ds-checkbox__box {
  color: var(--ds-color-checkbox-normal-inderterminate-icon-color);       
}
.ds-checkbox__input:checked ~ .ds-checkbox__box::before { content: 'check_box'; }
.ds-checkbox__input:indeterminate ~ .ds-checkbox__box::before { content: 'indeterminate_check_box'; }

.ds-checkbox-wrap {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
}
.ds-checkbox-wrap .ds-checkbox { align-self: flex-start; }

.ds-radio__box { color: var(--ds-color-radio-button-normal-deselected-icon-color); }  
.ds-radio__input:checked + .ds-radio__box {
  color: var(--ds-color-radio-button-normal-selected-icon-color);             
}

.ds-checkbox--error .ds-checkbox__box,
.ds-checkbox--error .ds-checkbox__input:checked ~ .ds-checkbox__box,
.ds-checkbox--error .ds-checkbox__input:indeterminate ~ .ds-checkbox__box {
  color: var(--ds-color-checkbox-error-icon-color);           
}
.ds-radio--error .ds-radio__box,
.ds-radio--error .ds-radio__input:checked + .ds-radio__box {
  color: var(--ds-color-radio-button-error-icon-color);       
}
.ds-checkbox--error .ds-checkbox__label,
.ds-radio--error .ds-radio__label {
  color: var(--ds-color-text-primary);  
}

.ds-checkbox--disabled,
.ds-radio--disabled {
  cursor: not-allowed;
}
.ds-checkbox--disabled .ds-checkbox__box { color: var(--ds-color-checkbox-disable-deselected-icon-color); }
.ds-checkbox--disabled .ds-checkbox__input:checked ~ .ds-checkbox__box { color: var(--ds-color-checkbox-disable-selected-icon-color); }
.ds-checkbox--disabled .ds-checkbox__input:indeterminate ~ .ds-checkbox__box { color: var(--ds-color-checkbox-disable-inderterminate-icon-color); }
.ds-checkbox--disabled .ds-checkbox__label { color: var(--ds-color-checkbox-label-text-disable-color); }
.ds-radio--disabled .ds-radio__box,
.ds-radio--disabled .ds-radio__input:checked + .ds-radio__box {
  color: var(--ds-color-radio-button-disable-deselected-icon-color);          
}
.ds-radio--disabled .ds-radio__label {
  color: var(--ds-color-radio-button-label-text-disable-color);               
}

.ds-checkbox-group,
.ds-radio-group {
  display: flex;
}
.ds-checkbox-group--vertical,
.ds-radio-group--vertical { flex-direction: column; gap: var(--ds-space-2x); }  
.ds-checkbox-group--horizontal,
.ds-radio-group--horizontal { flex-direction: row; gap: var(--ds-space-8x); }  

.ds-checkbox__support,
.ds-radio__support {
  display: block;
  margin-top: var(--ds-space-1x);                 
  margin-left: 28px;                              
  font-size: var(--ds-typography-font-size-3x);   
  line-height: 16px;
}
.ds-checkbox__support { color: var(--ds-color-checkbox-label-text-support-color); }  
.ds-radio__support { color: var(--ds-color-radio-button-label-text-support-color); } 
.ds-checkbox--error ~ .ds-checkbox__support,
.ds-radio--error .ds-radio__support {
  color: var(--ds-color-text-negative);           
}

.ds-radio__box {
  position: relative;
}
.ds-radio__box svg {
  position: relative;
  z-index: 1;
  width: 20px;
  height: 20px;
  display: block;
}
.ds-radio__state {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 28px;
  height: 28px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
}

.ds-checkbox__box::before, .ds-radio__box::before { content: none !important; }
.ds-checkbox__box, .ds-radio__box { background-repeat: no-repeat; background-position: center; background-size: 20px 20px; }

.ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%23616161%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox__input:checked ~ .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M10.6%2016.2L17.65%209.15L16.25%207.75L10.6%2013.4L7.75%2010.55L6.35%2011.95L10.6%2016.2ZM5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%23448aff%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox__input:indeterminate ~ .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M7%2013H17V11H7V13ZM5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%23448aff%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox--error .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%23ff5252%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox--error .ds-checkbox__input:checked ~ .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M10.6%2016.2L17.65%209.15L16.25%207.75L10.6%2013.4L7.75%2010.55L6.35%2011.95L10.6%2016.2ZM5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%23ff5252%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox--error .ds-checkbox__input:indeterminate ~ .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M7%2013H17V11H7V13ZM5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%23ff5252%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox--disabled .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%239e9e9e%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox--disabled .ds-checkbox__input:checked ~ .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M10.6%2016.2L17.65%209.15L16.25%207.75L10.6%2013.4L7.75%2010.55L6.35%2011.95L10.6%2016.2ZM5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%239e9e9e%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-checkbox--disabled .ds-checkbox__input:indeterminate ~ .ds-checkbox__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M7%2013H17V11H7V13ZM5%2021C4.45%2021%203.97917%2020.8042%203.5875%2020.4125C3.19583%2020.0208%203%2019.55%203%2019V5C3%204.45%203.19583%203.97917%203.5875%203.5875C3.97917%203.19583%204.45%203%205%203H19C19.55%203%2020.0208%203.19583%2020.4125%203.5875C20.8042%203.97917%2021%204.45%2021%205V19C21%2019.55%2020.8042%2020.0208%2020.4125%2020.4125C20.0208%2020.8042%2019.55%2021%2019%2021H5ZM5%2019H19V5H5V19Z%22%20fill%3D%22%239e9e9e%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-radio__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C10.6167%2022%209.31667%2021.7375%208.1%2021.2125C6.88333%2020.6875%205.825%2019.975%204.925%2019.075C4.025%2018.175%203.3125%2017.1167%202.7875%2015.9C2.2625%2014.6833%202%2013.3833%202%2012C2%2010.6167%202.2625%209.31667%202.7875%208.1C3.3125%206.88333%204.025%205.825%204.925%204.925C5.825%204.025%206.88333%203.3125%208.1%202.7875C9.31667%202.2625%2010.6167%202%2012%202C13.3833%202%2014.6833%202.2625%2015.9%202.7875C17.1167%203.3125%2018.175%204.025%2019.075%204.925C19.975%205.825%2020.6875%206.88333%2021.2125%208.1C21.7375%209.31667%2022%2010.6167%2022%2012C22%2013.3833%2021.7375%2014.6833%2021.2125%2015.9C20.6875%2017.1167%2019.975%2018.175%2019.075%2019.075C18.175%2019.975%2017.1167%2020.6875%2015.9%2021.2125C14.6833%2021.7375%2013.3833%2022%2012%2022ZM12%2020C14.2333%2020%2016.125%2019.225%2017.675%2017.675C19.225%2016.125%2020%2014.2333%2020%2012C20%209.76667%2019.225%207.875%2017.675%206.325C16.125%204.775%2014.2333%204%2012%204C9.76667%204%207.875%204.775%206.325%206.325C4.775%207.875%204%209.76667%204%2012C4%2014.2333%204.775%2016.125%206.325%2017.675C7.875%2019.225%209.76667%2020%2012%2020Z%22%20fill%3D%22%23616161%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-radio__input:checked + .ds-radio__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2017C13.3833%2017%2014.5625%2016.5125%2015.5375%2015.5375C16.5125%2014.5625%2017%2013.3833%2017%2012C17%2010.6167%2016.5125%209.4375%2015.5375%208.4625C14.5625%207.4875%2013.3833%207%2012%207C10.6167%207%209.4375%207.4875%208.4625%208.4625C7.4875%209.4375%207%2010.6167%207%2012C7%2013.3833%207.4875%2014.5625%208.4625%2015.5375C9.4375%2016.5125%2010.6167%2017%2012%2017ZM12%2022C10.6167%2022%209.31667%2021.7375%208.1%2021.2125C6.88333%2020.6875%205.825%2019.975%204.925%2019.075C4.025%2018.175%203.3125%2017.1167%202.7875%2015.9C2.2625%2014.6833%202%2013.3833%202%2012C2%2010.6167%202.2625%209.31667%202.7875%208.1C3.3125%206.88333%204.025%205.825%204.925%204.925C5.825%204.025%206.88333%203.3125%208.1%202.7875C9.31667%202.2625%2010.6167%202%2012%202C13.3833%202%2014.6833%202.2625%2015.9%202.7875C17.1167%203.3125%2018.175%204.025%2019.075%204.925C19.975%205.825%2020.6875%206.88333%2021.2125%208.1C21.7375%209.31667%2022%2010.6167%2022%2012C22%2013.3833%2021.7375%2014.6833%2021.2125%2015.9C20.6875%2017.1167%2019.975%2018.175%2019.075%2019.075C18.175%2019.975%2017.1167%2020.6875%2015.9%2021.2125C14.6833%2021.7375%2013.3833%2022%2012%2022ZM12%2020C14.2333%2020%2016.125%2019.225%2017.675%2017.675C19.225%2016.125%2020%2014.2333%2020%2012C20%209.76667%2019.225%207.875%2017.675%206.325C16.125%204.775%2014.2333%204%2012%204C9.76667%204%207.875%204.775%206.325%206.325C4.775%207.875%204%209.76667%204%2012C4%2014.2333%204.775%2016.125%206.325%2017.675C7.875%2019.225%209.76667%2020%2012%2020Z%22%20fill%3D%22%23448aff%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-radio--error .ds-radio__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C10.6167%2022%209.31667%2021.7375%208.1%2021.2125C6.88333%2020.6875%205.825%2019.975%204.925%2019.075C4.025%2018.175%203.3125%2017.1167%202.7875%2015.9C2.2625%2014.6833%202%2013.3833%202%2012C2%2010.6167%202.2625%209.31667%202.7875%208.1C3.3125%206.88333%204.025%205.825%204.925%204.925C5.825%204.025%206.88333%203.3125%208.1%202.7875C9.31667%202.2625%2010.6167%202%2012%202C13.3833%202%2014.6833%202.2625%2015.9%202.7875C17.1167%203.3125%2018.175%204.025%2019.075%204.925C19.975%205.825%2020.6875%206.88333%2021.2125%208.1C21.7375%209.31667%2022%2010.6167%2022%2012C22%2013.3833%2021.7375%2014.6833%2021.2125%2015.9C20.6875%2017.1167%2019.975%2018.175%2019.075%2019.075C18.175%2019.975%2017.1167%2020.6875%2015.9%2021.2125C14.6833%2021.7375%2013.3833%2022%2012%2022ZM12%2020C14.2333%2020%2016.125%2019.225%2017.675%2017.675C19.225%2016.125%2020%2014.2333%2020%2012C20%209.76667%2019.225%207.875%2017.675%206.325C16.125%204.775%2014.2333%204%2012%204C9.76667%204%207.875%204.775%206.325%206.325C4.775%207.875%204%209.76667%204%2012C4%2014.2333%204.775%2016.125%206.325%2017.675C7.875%2019.225%209.76667%2020%2012%2020Z%22%20fill%3D%22%23ff5252%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-radio--error .ds-radio__input:checked + .ds-radio__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2017C13.3833%2017%2014.5625%2016.5125%2015.5375%2015.5375C16.5125%2014.5625%2017%2013.3833%2017%2012C17%2010.6167%2016.5125%209.4375%2015.5375%208.4625C14.5625%207.4875%2013.3833%207%2012%207C10.6167%207%209.4375%207.4875%208.4625%208.4625C7.4875%209.4375%207%2010.6167%207%2012C7%2013.3833%207.4875%2014.5625%208.4625%2015.5375C9.4375%2016.5125%2010.6167%2017%2012%2017ZM12%2022C10.6167%2022%209.31667%2021.7375%208.1%2021.2125C6.88333%2020.6875%205.825%2019.975%204.925%2019.075C4.025%2018.175%203.3125%2017.1167%202.7875%2015.9C2.2625%2014.6833%202%2013.3833%202%2012C2%2010.6167%202.2625%209.31667%202.7875%208.1C3.3125%206.88333%204.025%205.825%204.925%204.925C5.825%204.025%206.88333%203.3125%208.1%202.7875C9.31667%202.2625%2010.6167%202%2012%202C13.3833%202%2014.6833%202.2625%2015.9%202.7875C17.1167%203.3125%2018.175%204.025%2019.075%204.925C19.975%205.825%2020.6875%206.88333%2021.2125%208.1C21.7375%209.31667%2022%2010.6167%2022%2012C22%2013.3833%2021.7375%2014.6833%2021.2125%2015.9C20.6875%2017.1167%2019.975%2018.175%2019.075%2019.075C18.175%2019.975%2017.1167%2020.6875%2015.9%2021.2125C14.6833%2021.7375%2013.3833%2022%2012%2022ZM12%2020C14.2333%2020%2016.125%2019.225%2017.675%2017.675C19.225%2016.125%2020%2014.2333%2020%2012C20%209.76667%2019.225%207.875%2017.675%206.325C16.125%204.775%2014.2333%204%2012%204C9.76667%204%207.875%204.775%206.325%206.325C4.775%207.875%204%209.76667%204%2012C4%2014.2333%204.775%2016.125%206.325%2017.675C7.875%2019.225%209.76667%2020%2012%2020Z%22%20fill%3D%22%23ff5252%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-radio--disabled .ds-radio__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C10.6167%2022%209.31667%2021.7375%208.1%2021.2125C6.88333%2020.6875%205.825%2019.975%204.925%2019.075C4.025%2018.175%203.3125%2017.1167%202.7875%2015.9C2.2625%2014.6833%202%2013.3833%202%2012C2%2010.6167%202.2625%209.31667%202.7875%208.1C3.3125%206.88333%204.025%205.825%204.925%204.925C5.825%204.025%206.88333%203.3125%208.1%202.7875C9.31667%202.2625%2010.6167%202%2012%202C13.3833%202%2014.6833%202.2625%2015.9%202.7875C17.1167%203.3125%2018.175%204.025%2019.075%204.925C19.975%205.825%2020.6875%206.88333%2021.2125%208.1C21.7375%209.31667%2022%2010.6167%2022%2012C22%2013.3833%2021.7375%2014.6833%2021.2125%2015.9C20.6875%2017.1167%2019.975%2018.175%2019.075%2019.075C18.175%2019.975%2017.1167%2020.6875%2015.9%2021.2125C14.6833%2021.7375%2013.3833%2022%2012%2022ZM12%2020C14.2333%2020%2016.125%2019.225%2017.675%2017.675C19.225%2016.125%2020%2014.2333%2020%2012C20%209.76667%2019.225%207.875%2017.675%206.325C16.125%204.775%2014.2333%204%2012%204C9.76667%204%207.875%204.775%206.325%206.325C4.775%207.875%204%209.76667%204%2012C4%2014.2333%204.775%2016.125%206.325%2017.675C7.875%2019.225%209.76667%2020%2012%2020Z%22%20fill%3D%22%239e9e9e%22%2F%3E%3C%2Fsvg%3E");   
}
.ds-radio--disabled .ds-radio__input:checked + .ds-radio__box {
  background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2017C13.3833%2017%2014.5625%2016.5125%2015.5375%2015.5375C16.5125%2014.5625%2017%2013.3833%2017%2012C17%2010.6167%2016.5125%209.4375%2015.5375%208.4625C14.5625%207.4875%2013.3833%207%2012%207C10.6167%207%209.4375%207.4875%208.4625%208.4625C7.4875%209.4375%207%2010.6167%207%2012C7%2013.3833%207.4875%2014.5625%208.4625%2015.5375C9.4375%2016.5125%2010.6167%2017%2012%2017ZM12%2022C10.6167%2022%209.31667%2021.7375%208.1%2021.2125C6.88333%2020.6875%205.825%2019.975%204.925%2019.075C4.025%2018.175%203.3125%2017.1167%202.7875%2015.9C2.2625%2014.6833%202%2013.3833%202%2012C2%2010.6167%202.2625%209.31667%202.7875%208.1C3.3125%206.88333%204.025%205.825%204.925%204.925C5.825%204.025%206.88333%203.3125%208.1%202.7875C9.31667%202.2625%2010.6167%202%2012%202C13.3833%202%2014.6833%202.2625%2015.9%202.7875C17.1167%203.3125%2018.175%204.025%2019.075%204.925C19.975%205.825%2020.6875%206.88333%2021.2125%208.1C21.7375%209.31667%2022%2010.6167%2022%2012C22%2013.3833%2021.7375%2014.6833%2021.2125%2015.9C20.6875%2017.1167%2019.975%2018.175%2019.075%2019.075C18.175%2019.975%2017.1167%2020.6875%2015.9%2021.2125C14.6833%2021.7375%2013.3833%2022%2012%2022ZM12%2020C14.2333%2020%2016.125%2019.225%2017.675%2017.675C19.225%2016.125%2020%2014.2333%2020%2012C20%209.76667%2019.225%207.875%2017.675%206.325C16.125%204.775%2014.2333%204%2012%204C9.76667%204%207.875%204.775%206.325%206.325C4.775%207.875%204%209.76667%204%2012C4%2014.2333%204.775%2016.125%206.325%2017.675C7.875%2019.225%209.76667%2020%2012%2020Z%22%20fill%3D%22%239e9e9e%22%2F%3E%3C%2Fsvg%3E");   
}

.ds-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-sizing: border-box;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  font-size: var(--ds-typography-font-size-3x);      
  font-weight: var(--ds-typography-font-weight-medium); 
  line-height: var(--ds-typography-caption-line-height-l); 
  color: var(--ds-color-text-inversive);             
  vertical-align: middle;
}

.ds-badge--counter {
  height: 18px;
  min-width: 19px;
  padding: var(--ds-size-0-25x) var(--ds-space-1-5x); 
  border-radius: var(--ds-radius-circular);          
}

.ds-badge--point {
  width: 8px;
  height: 8px;
  border-radius: var(--ds-radius-circular);          
}

.ds-badge--accent   { background: var(--ds-color-badge-accent-background); }   
.ds-badge--positive { background: var(--ds-color-badge-positive-background); } 
.ds-badge--warning  { background: var(--ds-color-badge-warning-background); }  
.ds-badge--negative { background: var(--ds-color-badge-negative-background); } 

.page-badge #matrix-root .matrix-types { padding-top: 16px; }
.page-badge #matrix-root .matrix-row { grid-template-columns: repeat(2, 1fr); }

.ds-tabs {
  display: flex;
  align-items: stretch;
  gap: var(--ds-space-0);
  border-bottom: 1px solid var(--ds-color-divider-solid-default-color); 
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-tab {
  display: inline-flex;
  align-items: center;
  gap: var(--ds-space-2x);                                
  box-sizing: border-box;
  height: 32px;                                           
  padding: var(--ds-space-1x) var(--ds-space-6x);          
  border: none;
  border-bottom: 2px solid transparent;
  margin-bottom: -1px;
  background: var(--ds-color-tab-innactive-default-background);
  color: var(--ds-color-tab-innactive-text-color);        
  font-family: inherit;
  font-size: var(--ds-typography-body-font-size-m);       
  font-weight: var(--ds-typography-font-weight-medium);   
  letter-spacing: var(--ds-typography-letter-spacing-s);
  line-height: var(--ds-typography-body-line-height-m);   
  white-space: nowrap;
  cursor: pointer;
  transition: background-color .15s ease, color .15s ease, border-color .15s ease;
}

.ds-tab:hover  { background: var(--ds-color-tab-innactive-hover-background); }  
.ds-tab:active { background: var(--ds-color-tab-innactive-press-background); }  

.ds-tab__icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-tab-innactive-icon-color);        
}

.ds-tab--active {
  color: var(--ds-color-tab-active-text-color);           
  border-bottom-color: var(--ds-color-tab-active-divider);
}
.ds-tab--active .ds-tab__icon { color: var(--ds-color-tab-active-icon-color); }
.ds-tab--active:hover  { background: var(--ds-color-tab-active-hover-background); }
.ds-tab--active:active { background: var(--ds-color-tab-active-press-background); }

.ds-tab--disabled,
.ds-tab:disabled {
  color: var(--ds-color-tab-disable-text-color);          
  pointer-events: none;
}
.ds-tab--disabled .ds-tab__icon { color: var(--ds-color-tab-disable-icon-color); }

.ds-tabs--lvl2 .ds-tab {
  height: 28px;
  padding: var(--ds-space-1x) var(--ds-space-3x);
  font-size: var(--ds-typography-body-font-size-s);       
  font-weight: var(--ds-typography-font-weight-regular);  
  line-height: var(--ds-typography-body-line-height-s);   
}

.ds-tab__counter {
  color: var(--ds-color-tab-innactive-counter-text-color);
  font-size: var(--ds-typography-font-size-3x);
}
.ds-tab--active .ds-tab__counter { color: var(--ds-color-tab-active-counter-text-color); }

.ds-divider {
  height: 1px;                                              
  border: none;
  margin: 0;
  background: var(--ds-color-divider-solid-default-color);  
}
.ds-divider--m            { height: 1px; }
.ds-divider--l            { height: 2px; }                  
.ds-divider--lite         { background: var(--ds-color-divider-solid-lite-color); }
.ds-divider:hover         { background: var(--ds-color-divider-solid-hover-color); }     
.ds-divider--selected     { background: var(--ds-color-divider-solid-selected-color); }  
.ds-divider--disable      { background: var(--ds-color-divider-solid-disable-color); }   
.ds-divider--dashed {
  height: 0;
  background: none;
  border-top: 1px dashed var(--ds-color-divider-dashed-default-color);
}
.ds-divider--dashed.ds-divider--l        { border-top-width: 2px; }
.ds-divider--dashed.ds-divider--selected { border-top-color: var(--ds-color-divider-dashed-selected-color); }
.ds-divider--dashed.ds-divider--disable  { border-top-color: var(--ds-color-divider-dashed-disable-color); }

.ds-divider-line {
  height: 1px;
  border: none;
  margin: 0;
  background: var(--ds-color-divider-solid-default-color);  
}
.ds-divider-line--lite     { background: var(--ds-color-divider-solid-lite-color); }
.ds-divider-line--selected { background: var(--ds-color-divider-solid-selected-color); } 
.ds-divider-line--disable  { background: var(--ds-color-divider-solid-disable-color); }
.ds-divider-line--dashed {
  height: 0;
  background: none;
  border-top: 1px dashed var(--ds-color-divider-dashed-default-color);
}

.ds-banner {
  display: flex;
  gap: var(--ds-space-2x);                                
  box-sizing: border-box;
  padding: var(--ds-space-3x) var(--ds-space-4x);          
  border-radius: var(--ds-radius-3x);                     
  background: var(--ds-color-banners-accent-background);  
  color: var(--ds-color-banners-text-color);              
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  font-size: var(--ds-typography-body-font-size-s);       
  line-height: var(--ds-typography-body-line-height-s);   
  letter-spacing: var(--ds-typography-letter-spacing-s);
}

.ds-banner--horizontal { flex-direction: row; align-items: center; }
.ds-banner--vertical   { flex-direction: column; }

.ds-banner--accent   { background: var(--ds-color-banners-accent-background); }
.ds-banner--positive { background: var(--ds-color-banners-positive-background); }
.ds-banner--warning  { background: var(--ds-color-banners-warning-background); }
.ds-banner--negative { background: var(--ds-color-banners-negative-background); }
.ds-banner--neutral  {
  background: var(--ds-color-banners-neutral-background);
  border: 1px solid var(--ds-color-banners-border-color);
}

.ds-banner__icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-banners-accent-icon-color);       
}
.ds-banner--positive .ds-banner__icon { color: var(--ds-color-banners-positive-icon-color); }
.ds-banner--warning  .ds-banner__icon { color: var(--ds-color-banners-warning-icon-color); }
.ds-banner--negative .ds-banner__icon { color: var(--ds-color-banners-negative-icon-color); }
.ds-banner--neutral  .ds-banner__icon { color: var(--ds-color-banners-neutral-icon-color); }

.ds-banner__row {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);
  width: 100%;
}

.ds-banner__text { flex: 1; }

.ds-banner__buttons {
  display: flex;
  gap: var(--ds-space-2x);
}

.ds-input__icon svg { width: 20px; height: 20px; display: block; }
.ds-input__icon svg path { fill: currentColor; }

.ds-input__stepper {
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  color: var(--ds-color-icon-primary);                     
}
.ds-input__stepper svg { width: 20px; height: 12px; display: block; }
.ds-input__stepper svg path { fill: currentColor; }
.ds-input__stepper button {
  border: none; background: none; padding: 0; margin: 0;
  display: flex; cursor: pointer; color: inherit;
}

.ds-field-label {
  display: block;
  color: var(--ds-color-text-primary);                    
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  font-size: var(--ds-typography-font-size-3-5x);         
  font-weight: var(--ds-typography-font-weight-medium);   
  letter-spacing: var(--ds-typography-letter-spacing-s);
  line-height: 20px;
}

.ds-card {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  border-radius: var(--ds-radius-2x);                 
  background: var(--ds-color-surface-default);        
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-card--filled { }

.ds-card--outlined {
  border: 1px solid var(--ds-color-stroke-default);   
}

.ds-card--shadow {
  box-shadow: var(--ds-shadow-shadows-01-dp-sl);
}

.ds-card--custom {
  padding: 16px;
}

.ds-card__header {
  display: flex;
  flex-direction: column;
  gap: var(--ds-space-2x);                            
  padding: 16px 16px 4px;                            
}

.ds-card__label-up,
.ds-card__label-down {
  color: var(--ds-color-text-secondary);              
  font-size: var(--ds-typography-body-font-size-m);   
  font-weight: var(--ds-typography-font-weight-regular); 
  line-height: var(--ds-typography-body-line-height-m); 
  letter-spacing: var(--ds-typography-letter-spacing-none);
}

.ds-card__title {
  margin: 0;
  color: var(--ds-color-text-primary);                
  font-size: var(--ds-typography-header-font-size-s); 
  font-weight: var(--ds-typography-font-weight-medium);
  line-height: var(--ds-typography-header-line-height-s); 
  letter-spacing: var(--ds-typography-letter-spacing-none);
}

.ds-card__content {
  display: flex;
  flex-direction: column;
  padding: 16px;                                      
}

.ds-card__footer {
  display: flex;
  flex-direction: column;
}
.ds-card__divider {
  height: 1px;
  background: var(--ds-color-stroke-default);         
  border: none;
}
.ds-card__footer__action {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);                            
  padding: 4px 16px 16px;                             
}
.ds-card__footer--right .ds-card__footer__action { justify-content: flex-end; }

.ds-expansion {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  border-radius: var(--ds-radius-3x);                    
  border: 1px solid var(--ds-color-stroke-default);      
  background: var(--ds-color-surface-default);           
  overflow: hidden;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-expansion--info {
  border: 1px dashed var(--ds-color-stroke-accent);      
  background: var(--ds-palette-accent-10);               
}

.ds-expansion__header {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);                               
  box-sizing: border-box;
  min-height: 44px;
  padding: var(--ds-space-3x) var(--ds-space-4x);         
  background: transparent;
  cursor: pointer;
  transition: background-color .15s ease;
}

.ds-expansion__header:hover  { background: var(--ds-color-shapes-hover); }   
.ds-expansion__header:active { background: var(--ds-color-shapes-press); }   

.ds-expansion--disabled {
  border-color: var(--ds-color-stroke-disable);          
  background: var(--ds-color-surface-disable);           
}
.ds-expansion--disabled .ds-expansion__header {
  color: var(--ds-color-text-disable);
  pointer-events: none;
}

.ds-expansion__icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-icon-primary);                   
}
.ds-expansion--info .ds-expansion__icon { color: var(--ds-color-icon-accent); }  

.ds-expansion__arrow {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ds-color-icon-primary);
  transition: transform .15s ease;
}
.ds-expansion--open .ds-expansion__arrow { transform: rotate(180deg); }

.ds-expansion__title {
  flex: 1;
  color: var(--ds-color-text-primary);                   
  font-size: var(--ds-typography-body-font-size-s);      
  font-weight: var(--ds-typography-font-weight-medium);  
  line-height: var(--ds-typography-body-line-height-s);  
  letter-spacing: var(--ds-typography-letter-spacing-s);
}

.ds-expansion__actions {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);
  flex-shrink: 0;
}

.ds-expansion__content {
  display: flex;
  flex-direction: column;
  padding: var(--ds-space-4x);                           
  color: var(--ds-color-text-primary);
  font-size: var(--ds-typography-body-font-size-s);      
  line-height: var(--ds-typography-body-line-height-s);  
  letter-spacing: var(--ds-typography-letter-spacing-s);
}
.ds-expansion__content--no-padding { padding: 0; }

.ds-expansion__icon svg path,
.ds-expansion__arrow svg path { fill: currentColor; }
.ds-expansion:not(.ds-expansion--open) .ds-expansion__content { display: none; }

.ds-stepper {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);                                  
  background: var(--ds-color-stepper-background);
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-step {
  display: inline-flex;
  align-items: center;
  gap: var(--ds-space-2x);                                  
  box-sizing: border-box;
  min-height: 24px;
  border: none;
  background: none;
  padding: 0;
  color: var(--ds-color-stepper-default-text-color);        
  font-family: inherit;
  font-size: var(--ds-typography-body-font-size-s);         
  font-weight: var(--ds-typography-font-weight-regular);    
  line-height: var(--ds-typography-body-line-height-s);     
  letter-spacing: var(--ds-typography-letter-spacing-s);
  white-space: nowrap;
  cursor: pointer;
}

.ds-step--bg {
  min-height: 32px;
  padding: var(--ds-space-1x) var(--ds-space-2x);
  border-radius: var(--ds-radius-2x);                       
  background: var(--ds-color-stepper-default-background);   
}

.ds-step:hover {
  color: var(--ds-color-stepper-hover-text-color);          
}
.ds-step--bg:hover { background: var(--ds-color-stepper-hover-background); }

.ds-step--selected {
  color: var(--ds-color-stepper-selected-text-color);       
}
.ds-step--bg.ds-step--selected {
  background: var(--ds-color-stepper-selected-background);  
  border: 1px solid var(--ds-color-stepper-selected-border-color);
}

.ds-step--disabled,
.ds-step:disabled {
  color: var(--ds-color-stepper-disable-text-color);        
  pointer-events: none;
}

.ds-step--error { color: var(--ds-color-stepper-error-text-color); }

.ds-step__num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  border-radius: var(--ds-radius-circular);                 
  color: var(--ds-color-stepper-default-icon-color);        
  font-size: var(--ds-typography-body-font-size-s);         
  line-height: 20px;
}

.ds-step--selected .ds-step__num {
  background: var(--ds-color-brand-accent-default);         
  color: var(--ds-color-text-inversive);                    
}
.ds-step--disabled .ds-step__num { color: var(--ds-color-stepper-disable-icon-color); }
.ds-step--error .ds-step__num    { color: var(--ds-color-stepper-error-icon-color); }

.ds-step__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  color: var(--ds-color-stepper-icon-color);
}
.ds-step__icon svg { width: 24px; height: 24px; display: block; }
.ds-step__icon svg path { fill: currentColor; }

.ds-stepper__divider {
  flex-shrink: 0;
  width: 8px;
  height: 1px;
  background: var(--ds-color-stepper-divider-color);         
}

.ds-stepper-button {
  display: flex;
  align-items: center;
  gap: var(--ds-space-4x);                                  
  min-height: 36px;
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-stepper-button__counter {
  flex-shrink: 0;
  color: var(--ds-color-text-primary);                      
  font-size: var(--ds-typography-body-font-size-s);         
  font-weight: var(--ds-typography-font-weight-medium);     
  line-height: var(--ds-typography-body-line-height-s);     
  white-space: nowrap;
}

.ds-stepper-button__group {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);                                  
}

.ds-slide-toggle {
  display: inline-flex;
  flex-direction: column;
  gap: var(--ds-space-1x);                                    
  font-family: 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

.ds-slide-toggle__row {
  display: flex;
  align-items: center;
  gap: var(--ds-space-2x);                                    
  cursor: pointer;
}

.ds-slide-toggle__input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
  pointer-events: none;
}

.ds-slide-toggle__track {
  position: relative;
  flex-shrink: 0;
  width: 34px;
  height: 20px;
  border-radius: var(--ds-radius-3x);                         
  background: var(--ds-color-slide-toggle-deselected-default-background); 
  transition: background-color .15s ease;
}

.ds-slide-toggle__track::after {
  content: '';
  position: absolute;
  top: 2px;
  left: 2px;
  width: 16px;
  height: 16px;
  border-radius: var(--ds-radius-circular);                   
  background: var(--ds-color-slide-toggle-knob-color);        
  transition: transform .15s ease;
}

.ds-slide-toggle__row:hover .ds-slide-toggle__track {
  background: var(--ds-color-slide-toggle-deselected-hover-background);   
}

.ds-slide-toggle__input:checked + .ds-slide-toggle__track {
  background: var(--ds-color-slide-toggle-selected-default-background);   
}
.ds-slide-toggle__input:checked + .ds-slide-toggle__track::after {
  transform: translateX(14px);
}
.ds-slide-toggle__row:hover .ds-slide-toggle__input:checked + .ds-slide-toggle__track {
  background: var(--ds-color-slide-toggle-selected-hover-background);     
}

.ds-slide-toggle__input:disabled + .ds-slide-toggle__track {
  background: var(--ds-color-slide-toggle-deselected-disable-background); 
}
.ds-slide-toggle__input:checked:disabled + .ds-slide-toggle__track {
  background: var(--ds-color-slide-toggle-selected-disable-background);
}
.ds-slide-toggle--disabled { pointer-events: none; }
.ds-slide-toggle--disabled .ds-slide-toggle__title {
  color: var(--ds-color-slide-toggle-deselected-disable-text-color);      
}

.ds-slide-toggle__title {
  color: var(--ds-color-slide-toggle-text-color);             
  font-size: var(--ds-typography-body-font-size-s);           
  font-weight: var(--ds-typography-font-weight-regular);      
  line-height: var(--ds-typography-body-line-height-s);       
  letter-spacing: var(--ds-typography-letter-spacing-s);
}

.ds-slide-toggle__support {
  color: var(--ds-color-slide-toggle-text-support-color);      
  font-size: var(--ds-typography-caption-font-size-l);         
  line-height: var(--ds-typography-caption-line-height-l);     
  letter-spacing: var(--ds-typography-letter-spacing-s);
  padding-left: 42px;                                          
}
.ds-slide-toggle--error .ds-slide-toggle__support {
  color: var(--ds-color-slide-toggle-text-error-color);        
}

.ds-slide-toggle__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  color: var(--ds-color-icon-primary);                         
}
.ds-slide-toggle__icon svg { width: 20px; height: 20px; display: block; }
.ds-slide-toggle__icon svg path { fill: currentColor; }

```

### Чек-лист соответствия ДС

- [ ] Все цвета, размеры, радиусы — только `var(--ds-*)`, без хардкода
- [ ] Кнопки: класс `ds-btn` + размер (`--xs/--s/--m`) + стиль (`--accent/--neutral/--positive/--negative/--warning`) + тип (`--filled/--outlined/--text`)
- [ ] Одна accent-кнопка на область, negative — экономно
- [ ] Иконки — Material Icons по имени внутри `.ds-btn__icon` / `.ds-btn-icon__icon` / `.ds-input__icon`, цвет через `currentColor`
- [ ] Input: размер из набора M/S/XS, лейбл только у M
- [ ] Checkbox/Radio: иконки-глифы 20×20, цвета из компонентных токенов
- [ ] Badge: Counter или Point, стиль из 4 вариантов
- [ ] Шрифт Roboto 400/500, размеры из токенов типографики