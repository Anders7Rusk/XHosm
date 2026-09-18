# -*- coding: utf-8 -*-
"""xHOSM: совмещение процесса разработки (приложенный PDF) с нашими материалами."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, HRFlowable)
from reportlab.graphics.shapes import Drawing, Rect as _Rect, String as _String

OUT = '/opt/data/xhosm-redesign'
FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DVS', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVS-B', FD + 'DejaVuSans-Bold.ttf'))
registerFontFamily('DVS', normal='DVS', bold='DVS-B', italic='DVS', boldItalic='DVS-B')

ACCENT = colors.HexColor('#448AFF'); DARK = colors.HexColor('#263238')
GRAY = colors.HexColor('#616161'); LINE = colors.HexColor('#D9E2EC')
BG = colors.HexColor('#F2F6FB')

S = {}
S['title'] = ParagraphStyle('t', fontName='DVS-B', fontSize=20, leading=24, textColor=DARK, spaceAfter=2)
S['subtitle'] = ParagraphStyle('st', fontName='DVS', fontSize=10.5, leading=14, textColor=GRAY)
S['meta'] = ParagraphStyle('m', fontName='DVS', fontSize=8.5, leading=12, textColor=GRAY)
S['h1'] = ParagraphStyle('h1', fontName='DVS-B', fontSize=14, leading=17, textColor=colors.HexColor('#1A4E8A'), spaceBefore=12, spaceAfter=5)
S['h2'] = ParagraphStyle('h2', fontName='DVS-B', fontSize=11.6, leading=14.5, textColor=colors.HexColor('#21456E'), spaceBefore=10, spaceAfter=3)
S['h3'] = ParagraphStyle('h3', fontName='DVS-B', fontSize=10.0, leading=12.5, textColor=DARK, spaceBefore=9, spaceAfter=2)
S['body'] = ParagraphStyle('b', fontName='DVS', fontSize=9.3, leading=12.8, textColor=DARK, spaceAfter=3)
S['step'] = ParagraphStyle('s', parent=S['body'], leftIndent=14, bulletIndent=2, spaceAfter=1.5)
S['card'] = ParagraphStyle('c', fontName='DVS', fontSize=9.0, leading=12.4, textColor=DARK, leftIndent=6, spaceAfter=2)
S['small'] = ParagraphStyle('sm', fontName='DVS', fontSize=8, leading=11, textColor=GRAY, spaceAfter=2)
S['th'] = ParagraphStyle('th', fontName='DVS-B', fontSize=8.2, leading=10.6, textColor=colors.HexColor('#12365B'))
S['td'] = ParagraphStyle('td', fontName='DVS', fontSize=8.2, leading=10.6, textColor=DARK)


def P(t, st='body'):
    return Paragraph(t, S[st])


def TBL(header, rows, widths):
    data = [[Paragraph(h, S['th']) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c), S['td']) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BG), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.45, LINE), ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3), ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FAFCFE')])]))
    return t


def make_pdf(path, footer_text, story):
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=1.6*cm, rightMargin=1.6*cm,
                          topMargin=1.5*cm, bottomMargin=1.5*cm, title=footer_text, author='Hermes Agent (iiko)')
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='n')

    def on_page(cv, d):
        cv.saveState(); cv.setFont('DVS', 7); cv.setFillColor(GRAY)
        cv.drawString(doc.leftMargin, 0.85*cm, footer_text)
        cv.drawRightString(A4[0]-doc.rightMargin, 0.85*cm, 'стр. %d' % d.page)
        cv.setStrokeColor(LINE); cv.setLineWidth(0.5)
        cv.line(doc.leftMargin, 1.05*cm, A4[0]-doc.rightMargin, 1.05*cm); cv.restoreState()

    doc.addPageTemplates([PageTemplate(id='all', frames=[frame], onPage=on_page)])
    doc.build(story)


def stages_strip():
    d = Drawing(504, 72)
    stages = [
        ('1. Понять,', 'что болит', 'done', 'пройден'),
        ('2. Решить,', 'что проверяем', 'done', 'пройден условно'),
        ('3. Описать до', 'рисования', 'next', 'сейчас здесь'),
        ('4. Дизайн', '', 'later', 'дальше'),
        ('5. Разработка,', 'запуск', 'later', 'с командой'),
    ]
    x = 0; w = 96; gap = 6
    for l1, l2, st, sub in stages:
        if st == 'done':
            fill, edge = colors.HexColor('#E9F7EF'), colors.HexColor('#3DAA6D')
        elif st == 'next':
            fill, edge = colors.HexColor('#E8F1FF'), ACCENT
        else:
            fill, edge = colors.HexColor('#F1F3F5'), colors.HexColor('#B0BEC5')
        d.add(_Rect(x, 26, w, 38, rx=5, ry=5, fillColor=fill, strokeColor=edge, strokeWidth=1))
        cx = x + w / 2
        d.add(_String(cx, 52, l1, fontName='DVS-B', fontSize=8.0, textAnchor='middle', fillColor=DARK))
        if l2:
            d.add(_String(cx, 42, l2, fontName='DVS-B', fontSize=8.0, textAnchor='middle', fillColor=DARK))
        d.add(_String(cx, 12, sub, fontName='DVS', fontSize=7.2, textAnchor='middle', fillColor=GRAY))
        x += w + gap
    d.hAlign = 'CENTER'
    return d


doc = []
doc += [P('xHOSM — процесс разработки × наши материалы', 'title'),
        P('Как пять этапов процесса (из приложенного PDF) ложатся на собранные документы — и что делаем дальше в режиме «один дизайнер + Hermes»', 'subtitle'),
        Spacer(1, 4), HRFlowable(width='100%', thickness=1.2, color=ACCENT, spaceAfter=6),
        P('18.09.2026 · Hermes Agent · Основа: «Процесс разработки продукта: упрощённый вариант» (приложение) + пакет xHOSM (файлы 1–5 в /opt/data/xhosm-redesign)', 'meta'),
        Spacer(1, 6)]

doc.append(P('1. Где мы в процессе', 'h1'))
doc.append(stages_strip())
doc.append(Spacer(1, 3))
doc.append(P('Этапы 1–2 процесса фактически пройдены на нашем пакете документов (этап 2 — с условным вердиктом, см. раздел 4). Сейчас мы стоим на входе в <b>этап 3 «Описать до того, как рисовать»</b>: у нас уже есть сценарии и блок-схемы «как сейчас» — осталось превратить две выбранные гипотезы в Story по шаблону и затем перейти к дизайну.', 'body'))
doc.append(P('Отличия режима «один дизайнер»: часть шагов процесса упрощаю или пропускаю осознанно (RICE-приоритизацию, полные гейты, замеры продукта) — компенсирую тем, что каждый артефакт собирается на фактуре этапа 1 и проверяется на небольшой группе коллег. Hermes в процессе указан как сборщик брифов и черновиков — эту роль он у нас и выполняет.', 'body'))

doc.append(P('2. Карта: этап процесса → наши файлы → статус → следующий шаг', 'h1'))
doc.append(TBL(['Этап процесса', 'Выход по процессу', 'Наши материалы', 'Статус', 'Следующий шаг'], [
 ['1. Понять, что болит', 'Проблема с источником и бизнес-контекстом + решение по трём исходам', 'Файл 2 «Боли и замечания» (Jira/вики/интервью); файл 1 «Материалы» (контекст системы)', 'Пройден: решение — «подтверждена»', 'Зафиксировать формулировку проблемы (раздел 3)'],
 ['2. Решить, что проверяем', 'Гипотеза по шаблону + вердикт по проверке', 'Файл 5 «Гипотезы улучшений» (H1–H16)', 'Пройден условно: «подтвердились»', 'Выбрать 1–2 гипотезы, заполнить шаблоны (раздел 4)'],
 ['3. Описать до рисования', 'Story с обязательными полями (+ схема as is/to be)', 'Файлы 3–4 «Сценарии» и «Клик-пути + блок-схемы» (= готовые сценарии и схемы as is)', 'Сейчас здесь', 'Собрать Story для выбранных гипотез + схемы to be (раздел 5)'],
 ['4. Дизайн', 'Макет + ревью по гайдам ДС + саммари', 'Файл 1 (текущее состояние) и файл 4 (сценарии) как вход', 'Дальше', 'Макеты 2 экранов-лидеров по ДС + саммари (раздел 6)'],
 ['5. Разработка, запуск, наблюдение', 'Работающий запуск с метрикой и решением по наблюдению', '—', 'Позже (с командой)', 'Пилот на L3, метрика «до/после», пост-мониторинг'],
], [3.1 * cm, 4.4 * cm, 5.0 * cm, 2.6 * cm, 2.4 * cm]))
doc.append(Spacer(1, 2))
doc.append(P('Приятное совпадение: <b>блок-схемы клик-путей из файла 4 — это уже готовые «схемы as is»</b>, которые процесс требует на этапе 3/4. Их не нужно рисовать заново — только дополнить схемами «to be» по выбранным гипотезам.', 'body'))

doc.append(P('3. Этап 1 в нашей редакции (формализация выхода)', 'h1'))
doc.append(P('<b>Проблема (словами заказчика):</b> «Поддержке больно работать в xHOSM: статусы, которым нельзя верить; операции по одной штуке; данные разбросаны по CRM/Postman/логам; многие экраны не объясняют, что происходит и почему нельзя».', 'body'))
doc.append(P('<b>Источники:</b> Jira (DO-969, DO-1225, DO-427, DO-1329, DO-1431, DO-586, DO-1218…), вики (регламенты L3, протоколы партнёрской поддержки, черновик «Анализ зависаний»), интервью 10 сотрудников 2026.', 'body'))
doc.append(P('<b>Бизнес-контекст:</b> ~85 000 активных серверов; xHOSM — ежедневный инструмент смены L3; обходные SQL-скрипты, ложные тикеты, повторные проверки, онбординг новичков через «посвящённых».', 'body'))
doc.append(P('<b>Решение по правилу выхода:</b> ✅ <b>подтверждена</b> — болит не у одного, повторяется годами (DO-969 с 2021, DO-427 с 2019), источники фиксируются. Идём дальше.', 'body'))

doc.append(P('4. Этап 2: гипотезы и шаблон', 'h1'))
doc.append(P('По правилу процесса в «спринт» берутся 1–2 гипотезы. Рекомендация для первого цикла: <b>H2 «Единый умный поиск» + H4 «Доказательный статус»</b> — самые частотные точки входа и доверия; H7 (массовые смены) и H3 (центр задач) — следующие в очереди. Ниже — шаблоны по процессу, заполненные для этих двух.', 'body'))
doc.append(P('H2 — шаблон гипотезы', 'h3'))
doc.append(TBL(['Поле', 'Что пишем'], [
 ['Проблема', 'Поддержке трудно находить клиента: WHERE вручную, фильтры только после поиска, связи Chain↔RMS ищутся глазами. Источник: интервью 10 сотрудников (2026), комментарий на вики (WHERE/геокодинг), DO-899 (ориентирование)'],
 ['Метрика', 'Время «тикет → найден нужный сервер»; доля поисков без ручного WHERE'],
 ['Как проверяем', 'Кликабельный черновой прототип + 5–7 коротких интервью с L3 (тип: понятность)'],
 ['Критерий успеха', 'Время поиска −30% и более; 4 из 5 участников находят сервер без подсказки коллеги'],
 ['Срок', '2 недели (один «спринт»), вердикт до конца'],
 ['Тип проверки', 'Понятность → прототип (по матрице «тип → способ проверки»)'],
 ['Владелец', 'Дизайнер (+ Hermes: черновик прототипа и текстов)'],
], [3.0 * cm, 14.5 * cm]))
doc.append(Spacer(1, 2))
doc.append(P('H4 — шаблон гипотезы', 'h3'))
doc.append(TBL(['Поле', 'Что пишем'], [
 ['Проблема', 'Статусы недостоверны и не объяснены: «Auto» против «STOPPED» при фокусе (DO-1225), «статусу доверять нельзя» (черновик зависаний) — ложные тикеты и ручные перепроверки. Источник: Jira + интервью L3'],
 ['Метрика', 'Число ручных перепроверок на разбор; число ложных тикетов от партнёров (база — замер до)'],
 ['Как проверяем', 'Прототип статус-бейджа и карточки + интервью L3 и партнёрской поддержки; сверка с историей тикетов'],
 ['Критерий успеха', '4 из 5 говорят «статусу верю и понимаю, откуда он»; перепроверки по причине «не верю статусу» → к нулю'],
 ['Срок', 'тот же «спринт»'],
 ['Тип проверки', 'Боль → интервью; понятность → прототип'],
 ['Владелец', 'Дизайнер'],
], [3.0 * cm, 14.5 * cm]))
doc.append(Spacer(1, 2))
doc.append(P('Вердикт «условно подтверждены»: сейчас он опирается на фактуру этапа 1 (боли) и экспертную оценку. Чтобы соблюсти процесс, мини-проверка стоит один день: прототип на 5 человек из поддержки — и вердикт становится настоящим.', 'body'))

doc.append(P('5. Этап 3 (сейчас): что уже есть и что собрать', 'h1'))
doc.append(P('По процессу выход этапа — Story с обязательными полями, для комплексных историй — схема as is/to be. Порядок: конкуренты → схема → прототип → описание.', 'body'))
doc.append(P('<b>У нас уже есть:</b> клик-пути и блок-схемы «как сейчас» (файл 4) = сценарии и as is; карта модулей и элементов (файл 1) = контекст для макета текущего состояния.', 'body'))
doc.append(P('<b>Осталось собрать:</b> Story по шаблону для H2 и H4, схемы «to be» (по гипотезам), критерии приёмки Given/When/Then. Эскиз Story для H2 — ниже (полный пакет соберу после твоего «ок»).', 'body'))
doc.append(P('H2 — эскиз Story', 'h3'))
doc.append(TBL(['Поле', 'Что пишем'], [
 ['Источник обращения', 'Интервью 10 сотрудников (2026); DO-899 (ориентирование в системе); комментарий вики про WHERE-запросы'],
 ['Бизнес-контекст', 'Поиск — вход во все операции; ~85 тыс. активных серверов; L3 работает с ним ежедневно десятки раз'],
 ['Бизнес-эффект', 'Разборы быстрее и с меньшим числом ошибок выбора сервера; меньше времени клиента в ожидании; уходит обходной WHERE'],
 ['Что делаем', 'Единый умный поиск: подсказка типа ввода, чипсы фильтров (кластер/статус/версия/бренд), сохранённые выборки, связи Chain↔RMS, массовые действия из результатов'],
 ['Критерии приёмки (Given/When/Then)', 'Given: вставлен список 40 CRM ID; When: Ctrl+Enter; Then: все найдены, виден счётчик и чипсы. · Given: введён UID; Then: подсказка «это UID» и поиск по UID. · Given: найден Chain; When: «связанные»; Then: показаны его RMS (и наоборот)'],
 ['Схема as is/to be', 'as is — блок-схема UI-01 из файла 4; to be — собрать (по гипотезе)'],
 ['Макет', '(слот: заполнится на этапе 4)'],
 ['Саммари от дизайнера', '(слот: грабли и граничные случаи при передаче в разработку)'],
], [4.0 * cm, 13.5 * cm]))

doc.append(P('6. Этап 4: дизайн — что делаем мы', 'h1'))
for r in [
 '<b>Вход:</b> Story + текущее состояние (файл 1) + гайды ДС. Ничего не переписываем заново — задача на дизайн «генерируется» из Story.',
 '<b>Работа:</b> макет по гайдам ДС (компоненты, UX-паттерны: навигация, фильтры, таблицы, пустые состояния; тексты) — 1–2 дня на макет; ревью по гайдам, лимит 3 итерации.',
 '<b>Выход:</b> макет + саммари для разработки (состояния и грабли: «что легко упустить при реализации»).',
 '<b>Наш план:</b> два макета-лидера — «Поиск» (H2) и «Статус + диагностика сервера» (H4) на базе сценариев файла 4; затем H7/H3.',
]:
    doc.append(Paragraph(r, S['step'], bulletText='•'))

doc.append(P('7. Этап 5: когда подключится команда', 'h1'))
for r in [
 '<b>Метрика «до»:</b> зафиксировать базу на первом замере (время поиска, число шагов в операциях, число обходных скриптов) — иначе будет не с чем сравнивать.',
 '<b>Пилот на L3:</b> показ макетов на груминге, промежуточная приёмка, гейт «готово к проду» с чек-листом; продуктовая метрика по формуле из гипотез.',
 '<b>Наблюдение:</b> пост-мониторинг ≥2 недель по той же метрике, стоп-условия, короткое ретро с одним принятым улучшением.',
 '<b>Правило спринтов:</b> дизайн живёт на спринт раньше разработки (макет до груминга); мелкие правки — внутри спринта.',
]:
    doc.append(Paragraph(r, S['step'], bulletText='•'))

doc.append(P('8. Чек-лист «что делаем прямо сейчас»', 'h1'))
for r in [
 '1. Подтвердить выбор гипотез первого цикла: H2 (поиск) + H4 (статус) — или заменить на H7/H3.',
 '2. Собрать полный пакет этапа 3: Story для H2 и H4, схемы «to be», критерии приёмки (сделаю по команде).',
 '3. Мини-проверка вердикта: прототип → 5 человек из поддержки (один день).',
 '4. Макеты по ДС для H2 и H4 + саммари для разработки (этап 4).',
 '5. Отдать пакет команде: груминг, реализуемость, пилотные метрики (этап 5).',
]:
    doc.append(Paragraph(r, S['step'], bulletText='•'))
doc.append(Spacer(1, 3))
doc.append(P('Что осознанно пропускаем в одиночном режиме: RICE-приоритизацию (выбор по частоте боли), полный гейт «берём в работу» (заменяет наш факт-пакет этапа 1) и замеры продукта (нужны на пилоте с командой). Компенсация — каждый артефакт опирается на фактуру и проверяется на мини-группе.', 'small'))

make_pdf(os.path.join(OUT, 'xHOSM_совмещение_с_процессом_v1.pdf'),
         'xHOSM · процесс разработки × наши материалы · 18.09.2026', doc)
print('OK')
for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(os.path.join(OUT, f)))
