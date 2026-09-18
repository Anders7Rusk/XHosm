# -*- coding: utf-8 -*-
"""xHOSM — сценарии работы с интерфейсом (клик-пути по аудиториям), черновик v1."""
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
S['h3'] = ParagraphStyle('h3', fontName='DVS-B', fontSize=9.8, leading=12.5, textColor=DARK, spaceBefore=8, spaceAfter=2)
S['body'] = ParagraphStyle('b', fontName='DVS', fontSize=9.3, leading=12.8, textColor=DARK, spaceAfter=3)
S['step'] = ParagraphStyle('s', parent=S['body'], leftIndent=14, bulletIndent=2, spaceAfter=1.5)
S['note'] = ParagraphStyle('n', fontName='DVS', fontSize=8.8, leading=12.2, textColor=DARK, leftIndent=6, spaceAfter=2)
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



# ===== ДВИЖОК БЛОК-СХЕМ =====
import math as _math
from reportlab.graphics.shapes import Drawing, Rect as _Rect, Polygon as _Poly, Line as _Line, String as _String

DSZ = 8.2
DLH = 10.2
DPAD = 8.0
_ARR = colors.HexColor('#607D8B')


def _wrap(text, maxw):
    words = text.split(' ')
    lines, cur = [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if pdfmetrics.stringWidth(t, 'DVS', DSZ) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _txt(d, cx, yc, lines, bold=False):
    n = len(lines)
    y0 = yc + n * DLH / 2 - DLH * 0.72
    for i, ln in enumerate(lines):
        d.add(_String(cx, y0 - i * DLH, ln, fontName='DVS-B' if bold else 'DVS',
                      fontSize=DSZ, textAnchor='middle', fillColor=DARK))


def _arrow(d, x1, y1, x2, y2, color=None):
    color = color or _ARR
    d.add(_Line(x1, y1, x2, y2, strokeColor=color, strokeWidth=0.8))
    ang = _math.atan2(y2 - y1, x2 - x1)
    bx = x2 - 5.5 * _math.cos(ang)
    by = y2 - 5.5 * _math.sin(ang)
    px = -_math.sin(ang) * 2.6
    py = _math.cos(ang) * 2.6
    d.add(_Poly([x2, y2, bx + px, by + py, bx - px, by - py], fillColor=color, strokeColor=color))


def diagram(flow):
    MAIN_W, RIGHT_W, GX, MX = 214, 214, 54, 2
    has_right = any(it[0] == 'dec' and len(it) >= 3 and it[2] for it in flow)
    main_x = MX if has_right else 0
    right_x = main_x + MAIN_W + GX
    total_w = (right_x + RIGHT_W) if has_right else MAIN_W
    rows = []
    y = 0
    for it in flow:
        kind, text = it[0], it[1]
        if kind == 'dec':
            lines = _wrap(text, MAIN_W * 0.60)
            h = max(40, len(lines) * DLH + 22)
            dw = MAIN_W * 0.98
        else:
            lines = _wrap(text, MAIN_W - 2 * DPAD)
            h = max(26, len(lines) * DLH + 14)
            dw = MAIN_W
        rlines, rh, rlabel, mlabel = None, 0, 'нет', None
        if kind == 'dec' and len(it) >= 3 and it[2]:
            rlines = [_wrap(t, RIGHT_W - 2 * DPAD) for t in it[2]]
            rh = sum(max(24, len(l) * DLH + 12) + 10 for l in rlines) - 10
            if len(it) >= 4 and it[3]:
                rlabel = it[3]
            if len(it) >= 5 and it[4]:
                mlabel = it[4]
        span = max(h, rh)
        rows.append(dict(kind=kind, lines=lines, h=h, dw=dw, rh=rh, rlines=rlines,
                         rlabel=rlabel, mlabel=mlabel, span=span))
        y += span + 16
    total_h = y - 16 + 8
    d = Drawing(total_w, total_h + 4)
    ytop = total_h - 2
    for r in rows:
        r['ytop'] = ytop
        ytop -= r['span'] + 16
    cx = main_x + MAIN_W / 2
    for i, r in enumerate(rows):
        yb = r['ytop'] - r['h']
        r['yb'] = yb
        if r['kind'] in ('start', 'end'):
            fill = colors.HexColor('#E8F1FF') if r['kind'] == 'start' else colors.HexColor('#E9F7EF')
            edge = ACCENT if r['kind'] == 'start' else colors.HexColor('#3DAA6D')
            d.add(_Rect(main_x, yb, r['dw'], r['h'], rx=r['h'] / 2, ry=r['h'] / 2,
                        fillColor=fill, strokeColor=edge, strokeWidth=0.9))
            _txt(d, cx, yb + r['h'] / 2, r['lines'], bold=True)
        elif r['kind'] == 'step':
            d.add(_Rect(main_x, yb, r['dw'], r['h'], rx=3, ry=3, fillColor=colors.white,
                        strokeColor=colors.HexColor('#9FB3C8'), strokeWidth=0.8))
            _txt(d, cx, yb + r['h'] / 2, r['lines'])
        elif r['kind'] == 'dec':
            cy = yb + r['h'] / 2
            d.add(_Poly([cx, r['ytop'], cx + r['dw'] / 2, cy, cx, yb, cx - r['dw'] / 2, cy],
                        fillColor=colors.HexColor('#FFF6E0'),
                        strokeColor=colors.HexColor('#E6A700'), strokeWidth=0.9))
            _txt(d, cx, cy, r['lines'])
            if r['rlines']:
                stack_top = min(r['ytop'], cy + r['rh'] / 2)
                ry = stack_top
                first_cy = cy
                for j, rl in enumerate(r['rlines']):
                    rh_ = max(24, len(rl) * DLH + 12)
                    rybot = ry - rh_
                    d.add(_Rect(right_x, rybot, RIGHT_W, rh_, rx=3, ry=3, fillColor=colors.white,
                                strokeColor=colors.HexColor('#9FB3C8'), strokeWidth=0.8))
                    _txt(d, right_x + RIGHT_W / 2, rybot + rh_ / 2, rl)
                    if j == 0:
                        first_cy = rybot + rh_ / 2
                    ry = rybot - 10
                x1 = cx + r['dw'] / 2
                x2 = right_x - 2
                xm = x1 + (x2 - x1) * 0.5
                d.add(_Line(x1, cy, xm, cy, strokeColor=_ARR, strokeWidth=0.8))
                d.add(_Line(xm, cy, xm, first_cy, strokeColor=_ARR, strokeWidth=0.8))
                _arrow(d, xm, first_cy, x2, first_cy)
                d.add(_String(x1 + 4, cy + 3, r['rlabel'], fontName='DVS', fontSize=7, fillColor=GRAY))
                if r['mlabel'] and i + 1 < len(rows):
                    d.add(_String(cx + 5, yb - 12, r['mlabel'], fontName='DVS', fontSize=7, fillColor=GRAY))
                if i + 1 < len(rows):
                    last_bottom = ry + 10
                    nxt = rows[i + 1]
                    nxt_top = nxt['ytop']
                    ymerge = max(nxt_top + 3, last_bottom - 2)
                    rcx = right_x + RIGHT_W / 2
                    if last_bottom > ymerge:
                        d.add(_Line(rcx, last_bottom, rcx, ymerge, strokeColor=_ARR, strokeWidth=0.8))
                    d.add(_Line(rcx, ymerge, cx + 44, ymerge, strokeColor=_ARR, strokeWidth=0.8))
                    if nxt['kind'] == 'dec':
                        entry = nxt_top - (44.0 / (nxt['dw'] / 2)) * (nxt['h'] / 2.0)
                    else:
                        entry = nxt_top
                    _arrow(d, cx + 44, ymerge, cx + 44, entry)
    for i in range(len(rows) - 1):
        _arrow(d, cx, rows[i]['yb'], cx, rows[i + 1]['ytop'])
    d.hAlign = 'CENTER'
    return d


def legend():
    d = Drawing(470, 122)
    d.add(_Rect(6, 92, 150, 18, rx=9, ry=9, fillColor=colors.HexColor('#E8F1FF'), strokeColor=ACCENT, strokeWidth=0.9))
    d.add(_String(81, 98.5, 'Старт / финал', fontName='DVS-B', fontSize=8.2, textAnchor='middle', fillColor=DARK))
    d.add(_String(168, 98.5, '— начало и конец пути', fontName='DVS', fontSize=8.2, fillColor=GRAY))
    d.add(_Rect(6, 67, 150, 18, rx=3, ry=3, fillColor=colors.white, strokeColor=colors.HexColor('#9FB3C8'), strokeWidth=0.8))
    d.add(_String(81, 73.5, 'Шаг', fontName='DVS', fontSize=8.2, textAnchor='middle', fillColor=DARK))
    d.add(_String(168, 73.5, '— действие пользователя (клик, поле, кнопка)', fontName='DVS', fontSize=8.2, fillColor=GRAY))
    cxx, cy = 81, 38
    d.add(_Poly([cxx, cy + 11, cxx + 75, cy, cxx, cy - 11, cxx - 75, cy], fillColor=colors.HexColor('#FFF6E0'), strokeColor=colors.HexColor('#E6A700')))
    d.add(_String(cxx, cy - 3, 'Развилка', fontName='DVS', fontSize=8.2, textAnchor='middle', fillColor=DARK))
    d.add(_String(168, cy - 3, '— «да/продолжение» вниз, «нет/альтернатива» вправо', fontName='DVS', fontSize=8.2, fillColor=GRAY))
    _arrow(d, 8, 13, 150, 13)
    d.add(_String(168, 9.5, '— порядок шагов', fontName='DVS', fontSize=8.2, fillColor=GRAY))
    d.hAlign = 'CENTER'
    return d

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



FLOWS = {
'UI-00': [
 ('start', 'Открыть адрес контура (RU / EU / KZ)'),
 ('step', 'Ввести доменный логин и пароль'),
 ('step', 'Панель: шапка, вкладки, пустой список'),
 ('step', 'Клик по имени — история операций'),
 ('end', 'Начало работы'),
],
'UI-01': [
 ('start', 'Клик в поле поиска (левая панель)'),
 ('step', 'Вбить значения столбиком: CRM ID / UID / домен / Tomcat / SQL'),
 ('step', 'Ctrl+Enter или «Найти»'),
 ('dec', 'Результатов много?', ['«Показать все»', 'Фильтры в шапке таблицы'], 'да'),
 ('dec', 'Нужны связанные (Chain и RMS)?', ['Shift+клик по «Найти»'], 'да'),
 ('end', 'Сервер найден — к действию'),
],
'UI-02': [
 ('start', 'Флажок в строке'),
 ('step', 'Включено слежение: статус и версия (60 с)'),
 ('dec', 'Список больше 100 строк?', ['Слежение — OFF', 'Потом «выделить всё»'], 'да'),
 ('step', '«Больше информации»: память + resto.properties'),
 ('step', 'Кнопки UID / iikoUser / Контракт'),
 ('step', '«История» — 25 операций'),
 ('step', 'Ссылки: CRM / RDP / логи / SQL / бекап'),
 ('end', 'Все данные о сервере под рукой'),
],
'UI-W-01': [
 ('start', 'Поиск: CRM ID или домен'),
 ('step', 'Флажок — включить слежение'),
 ('step', '«Логи» — error / full'),
 ('step', '«V» — Victoria Logs'),
 ('dec', 'Сломан доступ (например, BCrypt)?', ['Groovy: Bcrypt part 1 и 2 (до 5 мин)'], 'да'),
 ('end', 'Проверка входа в веб-приложение'),
],
'UI-A-01': [
 ('start', 'Вкладка «SQL» — режим Statistics'),
 ('step', 'Задать фильтры и показатели'),
 ('step', 'Запуск по выборке (до 1500 серверов)'),
 ('step', 'Прогресс обновляется каждые 15 с'),
 ('end', 'Выгрузка ZIP готова'),
],
'UI-A-02': [
 ('start', 'Остановить Tomcat'),
 ('step', '«Бекап БД» — отметить «Анонимизация»'),
 ('dec', 'Отдать через FTP?', ['Выбрать euftp.syrve.online'], 'да'),
 ('step', 'Путь и доступ — в окне логов'),
 ('end', 'Бекап передан адресату'),
],
'UI-A-03': [
 ('start', 'Поиск тестового сервера'),
 ('step', '«Версия» — бета / Branch'),
 ('step', '«Обновить»'),
 ('step', 'Проверить статус и логи'),
 ('end', 'Результат — в задаче'),
],
'UI-A-04': [
 ('start', 'Вкладка «SQL»'),
 ('step', 'Написать запрос'),
 ('dec', 'Нужна запись?', ['Флаг «Разрешить изменения»'], 'да'),
 ('step', 'Результат: до 100 строк'),
 ('end', 'Выгрузка в CSV'),
],
'UI-I-01': [
 ('start', 'Поиск — отметить 1 строку (лимит 1)'),
 ('step', 'Регион и версия (тариф и «в Чейне» — авто)'),
 ('step', 'Кнопка «#» — часовой пояс и язык'),
 ('step', '«Проверить»: домен транслитом ( -co / -cc ), ответ HOSM'),
 ('dec', '«Контракт» — зелёный?', ['«Cancel» — поправить домен', '«Проверить» ещё раз'], 'нет', 'да'),
 ('step', '«OK» — создание запущено'),
 ('end', 'Очередь — по кнопке «#»'),
],
'UI-I-02': [
 ('start', 'Остановить Tomcat'),
 ('step', '«Перенос»: выбрать SQL-сервер назначения'),
 ('step', 'БД назначения (пусто — не менять имя)'),
 ('dec', 'БД уже существует?', ['Отметить «Пересоздать БД»'], 'да'),
 ('step', 'Запуск; прогресс — в правом верхнем углу'),
 ('end', 'БД перенесена'),
],
'UI-I-03': [
 ('start', 'Вкладка «Разное» — блок «Архив»'),
 ('step', 'Действие: архивация / восстановление / удаление / переименование'),
 ('step', 'Отметить серверы флажками'),
 ('step', 'Запуск; результат — в логах и ленте хосробота'),
 ('end', 'Новый статус сервера'),
],
'UI-P-01': [
 ('start', 'Поиск: CRM ID или домен'),
 ('step', 'Внешним видно: Название и CRM ID'),
 ('step', 'Кнопки UID / iikoUser / Контракт'),
 ('step', '«Контрагент» — карточка в CRM'),
 ('end', 'Клиенту дан ответ'),
],
'UI-P-02': [
 ('start', 'Выбрать сервер (цвет и статус обновятся)'),
 ('step', '«Служба» — «Остановить» — STOPPED'),
 ('dec', 'Статус не обновился?', ['Обновить страницу'], 'да', 'нет'),
 ('step', '«Разное» — «Закрыть смену»'),
 ('dec', 'Смен несколько?', ['Снять галку автозапуска Tomcat'], 'да', 'нет'),
 ('step', 'Скопировать UUID и дату — исправить — «Ок»'),
 ('end', 'Запустить Tomcat'),
],
'UI-P-03': [
 ('start', 'Заявка партнёра на данные'),
 ('step', 'Поддержка: «Бекап БД» (+ анонимизация)'),
 ('step', '«Обслуживание» — «Создание папки на FTP» — «Выполнить»'),
 ('step', 'Передать путь и доступ'),
 ('end', 'Партнёр забирает бекап'),
],
'UI-D-01': [
 ('start', 'Поиск клиента'),
 ('step', '«Логи» / «V» (Victoria)'),
 ('dec', 'Нужен пакет?', ['Скачать ZIP (с ротационными)'], 'да'),
 ('step', 'Конфигурация — просмотр параметров'),
 ('end', 'Данные для разбора собраны'),
],
'UI-D-02': [
 ('start', 'Cloud Tools — «Сборка версий» (DO-976)'),
 ('step', 'Сборки переезжают в отдельный контур'),
 ('step', 'Новое: сертификаты devPortal в xHOSM'),
 ('end', 'Процессы разделены'),
],
'UI-L3-01': [
 ('start', 'Поиск: CRM ID'),
 ('step', 'Отметить строку флажком'),
 ('step', '«Служба»: опции — лицензии / unsaveddata / аварийное'),
 ('step', 'Время: Сейчас / Очередь / Тех.окно / ЧЧ:ММ'),
 ('step', '«Остановка» (Disabled) или «Перезапуск» (Auto)'),
 ('dec', 'Статус не меняется?', ['«Аварийное прерывание»', 'Фикс статуса CONTAINERCREATING'], 'да'),
 ('end', 'Проверить статус и логи - ответ клиенту'),
],
'UI-L3-02': [
 ('start', 'Поиск — флажки на записях'),
 ('dec', 'Каким способом?', ['Б: CRM ID / UID в поле над кнопками', '(по CRM ID быстрее)'], 'или', 'А: по списку'),
 ('step', '«Отвязать» / «Удалить» / «Обновить» / «Обнов. кэш»'),
 ('step', 'Окно успеха; поле очищается'),
 ('dec', 'Всё ещё не работает?', ['Красный Cloud: upRevision + UOC', 'BCrypt: Groovy part 1 и 2'], 'да'),
 ('end', 'Лицензия в порядке'),
],
'UI-L3-03': [
 ('start', 'Проверить правила (тариф, размер, срок)'),
 ('step', 'Поиск — флажок на сервере'),
 ('step', '«Конфигурация»: db-period-length-days = N'),
 ('step', 'Галка перезапуска — «Сохранить»'),
 ('step', 'Проверить период в «больше информации»'),
 ('end', 'Клиент может редактировать'),
],
'UI-L3-04': [
 ('start', 'Диагностика: «больше информации», логи'),
 ('step', '«Конфигурация»: memory — ×1.5 или ×2'),
 ('step', '«Сохранить» + перезапуск Tomcat'),
 ('dec', 'Падения повторяются?', ['Повторить диагностику', 'Метрики и логи'], 'да'),
 ('end', 'Память изменена, статус проверен'),
],
'UI-L3-05': [
 ('start', 'Поиск — флажки (1 или несколько)'),
 ('step', '«Версия»: выбрать из списка; Front / Office'),
 ('step', 'Флаги: Downgrade / Unlock / Rapid — осознанно'),
 ('step', 'Время: сейчас / очередь / тех.окно'),
 ('step', '«Обновить» — наблюдать'),
 ('step', 'Бекапы: PgSQL — «тильда»; MSSQL — hosfiles-3'),
 ('dec', 'Ошибка?', ['Разбор по логам', 'Проверить открытые смены'], 'да'),
 ('end', 'Версия обновлена - клиенту'),
],
'UI-L3-06': [
 ('start', 'Поиск — строка сервера'),
 ('step', '«Логи»: error / full / JMS / startup'),
 ('step', '«V» — Victoria Logs'),
 ('dec', 'Нужен пакет для разбора?', ['Скачать ZIP (с ротационными)'], 'да'),
 ('step', 'Сервер остановлен? Смотреть Archive1 / Archive2'),
 ('end', 'Логи под рукой'),
],
'UI-L3-07': [
 ('start', 'Остановить Tomcat'),
 ('step', 'Отметить до 5 серверов (PGSQL — через TSQL)'),
 ('step', '«Бекап БД»: тип, папка, «архивировать после»'),
 ('dec', 'Для партнёра / разработки?', ['«На FTP» (euftp)', '«Анонимизация»'], 'да'),
 ('step', 'Запуск; стадии — в правом верхнем углу'),
 ('end', 'Запустить Tomcat после завершения'),
],
'UI-L3-08': [
 ('start', 'Остановить Tomcat'),
 ('dec', 'Что делаем?', ['Перенос (до 5 строк): SQL-сервер и БД', '«Пересоздать БД» — запуск'], 'или', 'Восстановление'),
 ('step', 'Восстановление (1 строка): файл из Быстрого обмена'),
 ('step', '«Пересоздать БД» — «Восстановить»'),
 ('step', 'После загрузки период станет 60 дней'),
 ('end', 'Запустить Tomcat'),
],
'UI-L3-09': [
 ('start', 'Остановить сервер — STOPPED'),
 ('dec', 'Статус не обновился?', ['Обновить страницу'], 'да', 'нет'),
 ('step', '«Разное» — «Закрыть смену»'),
 ('step', 'Скопировать UUID (YYYY-MM-DD HH:MM)'),
 ('step', 'Исправить время — «Ок» (документы — АЗ)'),
 ('dec', 'Ещё смены?', ['Снять галку автозапуска', 'Повторить закрытие'], 'да', 'нет'),
 ('end', 'Запустить Tomcat'),
],
'UI-L3-10': [
 ('start', 'Задача: запрос или скрипт'),
 ('dec', 'SQL или Groovy?', ['Groovy: Cloud Tools — Обслуживание', 'Groovy.jsp — скрипт (до 5 мин)'], 'или', 'SQL'),
 ('step', 'SQL: вкладка «SQL» — запрос'),
 ('dec', 'Нужна запись?', ['Флаг «Разрешить изменения»'], 'да'),
 ('step', 'Результат: до 100 строк — CSV'),
 ('end', 'Готово; результат — в задаче'),
],
'UI-L3-11': [
 ('start', 'Правила: Chain и RMS; период минус 1 год'),
 ('step', 'Ручной бекап на сервер контура'),
 ('step', 'Остановить сервер'),
 ('step', 'Конфигурация: db-shrink-no-backup=true, db-shrink-date=…'),
 ('step', 'db-shrink-exclusive-mode=true (эксклюзивный режим)'),
 ('dec', 'Complete и балансы равны?', ['По логам: восстановить бекап', 'или перезапуск (см. инструкцию)'], 'нет', 'да'),
 ('step', 'Режим = false — запуск сервера'),
 ('end', 'Пометка «i»: shrink выполнен'),
],
'UI-L3-12': [
 ('start', 'Поиск CRMID: RMS и Chain'),
 ('step', 'RMS: скрипт №1 (репликация + стоп)'),
 ('step', 'Бекап RMS: файл .dmp в папку Backups'),
 ('step', 'Chain: «Создать 1» — предпроверка'),
 ('step', 'Восстановить БД (PGSQL, пересоздать)'),
 ('step', 'Скрипт №2 — Server Instance'),
 ('dec', 'Ошибка «только для чейна»?', ['«Ревизия» на 1-й вкладке'], 'да'),
 ('step', 'Скрипт №3 — запуск'),
 ('end', 'RMS переведён в Chain'),
],
'UI-L3-13': [
 ('start', 'partners.iiko.ru — демо-кабинет'),
 ('dec', 'Галка «активировать сервер»?', ['Нет — вручную: xHOSM', 'Поиск по UID — создать'], 'нет', 'да'),
 ('step', 'Сервер создаётся в xHOSM (UID в адресе)'),
 ('step', 'Выбрать версию — развернуть'),
 ('step', 'Восстановить бекап клиента (анонимизация)'),
 ('end', 'Лицензия: боевая при более 150 тыс.'),
],
'UI-L3-14': [
 ('start', 'ЛК чейна: распределение лицензий'),
 ('step', 'Удалить лицензии с RMS — сохранить'),
 ('step', 'Распределить заново — сохранить'),
 ('dec', 'Автоматика подняла сервер?', ['xHOSM: найти сервер', '«Разное» — «Архив» — «Восстановление»'], 'нет', 'да'),
 ('end', 'Сервер поднят (10–15 мин)'),
],
}

doc = []
doc += [P('xHOSM — сценарии работы с интерфейсом', 'title'),
        P('Клик-пути по аудиториям: от авторизации до результата — что открывают, куда жмут, какие поля заполняют, что видят на выходе', 'subtitle'),
        Spacer(1, 4), HRFlowable(width='100%', thickness=1.2, color=ACCENT, spaceAfter=6),
        P('Черновик v1 · 18.09.2026 · Hermes Agent · Источники: wiki «Интерфейс системы управления XHOSM» (v139), инструкции L3S/DEVOPS, User Stories и спека «Xhosm», сводки болей. Действия и окна — из документации; где источник не покрывает детали — помечено «(уточнить)».', 'meta'),
        Spacer(1, 8)]

doc.append(P('0. Как читать', 'h1'))
doc.append(P('Карточка = один путь: <b>шаги</b> (что делает пользователь), <b>результат</b> (что видит/получает), при наличии — <b>фолбэк</b> (если не сработало) и <b>что учти в новом UI</b>. Адреса и названия кнопок — как в системе сейчас; в новом Linux-интерфейсе сверять со стендом xhosm-test.', 'body'))
doc.append(P('Аудитории: L3 Support (ядро), L3 Web, аналитики (RMS/Chain и данных), инфраструктура, партнёры и АМ, разработка. Вход и базовые механики — общие для всех.', 'body'))
doc.append(P('Легенда схем', 'h3'))
doc.append(legend())

# ---------- ОБЩЕЕ ----------
doc.append(P('1. Общее: вход и базовые механики (для всех аудиторий)', 'h1'))

doc.append(P('UI-00. Вход в систему и первый экран', 'h3'))
steps = [
 'Открыть адрес своего контура: RU — http://xhosm.resto.lan · EU — https://xhosm-eu.cloud.lan · KZ — http://xhosm-kz.resto.lan (тестовые контуры нового Linux-GUI: xhosm-test / xhosm-dev).',
 'Ввести доменный логин и пароль (авторизация под доменной учётной записью; внешним пользователям выдаётся отдельный доступ).',
 'Попасть на панель: сверху шапка (название, «?» — вики, имя пользователя, иконки-инструменты, ряд вкладок, статус подключений, кластеры по умолчанию, версия по умолчанию, «Компоненты», дата/время, счётчики «всего / в архиве»), снизу — пустая таблица до первого поиска.',
 'Клик по имени пользователя — история его операций; клик по «?» — переход в документацию.',
]
for i, s_ in enumerate(steps, 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('<b>Что учесть:</b> сессия ограничена по времени (≈4 ч) — при долгих разборах приходится логиниться заново; в интервью вход назван «неудобным аутентификатором» (US-028) → SSO/долгоживущая сессия. Новым людям непонятен состав панели — просили стартовую страницу-навигацию (DO-899).', 'note'))
doc.append(P('Схема пути: UI-00', 'small'))
doc.append(diagram(FLOWS['UI-00']))

doc.append(P('UI-01. Поиск сервера клиента (источник всех действий)', 'h3'))
for i, s_ in enumerate([
 'Кликнуть в поле поиска (левая панель, многострочное поле).',
 'Вбить значения — столбиком или через пробел, можно смешивать типы: CRM ID (точное), UID нового образца NNN-NNN-NNN (точное), домен (частичное: «zapravka», «zapravka.iiko.it», с портом/протоколом), Tomcat (точное), SQL-сервер (точное). До 1000 значений за раз.',
 'Ctrl+Enter (или кнопка «Найти»).',
 'Прочитать результат: по умолчанию 25 строк, счётчик найденного, флажок «Показать все», экспорт «.CSV».',
 'Сузить выборку фильтрами прямо в заголовке таблицы.',
 'Кнопка рядом с «Найти» (Shift+клик) — поиск «связанных»: нашли Chain — показать его RMS и наоборот.',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('<b>Что учесть:</b> WHERE-запросы и смешивание типов — барьер для нетехнических ролей; фильтры появляются только после поиска; «Поле „Статус“ в поиске не используется» (интервью).', 'note'))
doc.append(P('Схема пути: UI-01', 'small'))
doc.append(diagram(FLOWS['UI-01']))

doc.append(P('UI-02. Работа со строкой результата («швейцарский нож»)', 'h3'))
for i, s_ in enumerate([
 'Флажок в строке — кроме выбора, включает отслеживание статуса: статус и версия тянутся с сервера (getServerMonitoringInfo.jsp), период обновления по умолчанию 60 с; на больших выборках (>100 строк) перед «выделить всё» советуют ставить обновление на OFF.',
 'Опция «больше информации» — показывает память и ключевые параметры resto.properties.',
 'Кнопки UID · iikoUser · Контракт — по клику значение появляется прямо вместо кнопки.',
 '«История» — последние 25 операций по домену с подробностями.',
 'Ссылки строки: «Контрагент» → карточка в iikoCRM; «Домен» → веб-интерфейс клиента; «Томкат» → ярлык RDP-подключения; «Логи» → лог-файлы; «SQL-сервер» → запуск SQL-студии; «Имя БД» → бекап этой БД (MSSQL → \\\\hosfiles\\Быстрый_обмен\\, PGSQL → \\\\hossupport\\Backups\\).',
 'Для макросов (BackOffice, DBeaver и т.п.) — один раз настроить «параметры адаптера» (суффиксы resto.lan / cloud.lan).',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('<b>Что учесть:</b> цвет строки — главный индикатор статуса, но статус бывает недостоверным (DO-1225: «Auto», при фокусе — «STOPPED»); строка перегружена (~23 колонки из 70+ атрибутов, DO-586).', 'note'))
doc.append(P('Схема пути: UI-02', 'small'))
doc.append(diagram(FLOWS['UI-02']))

# ---------- L3 ----------
doc.append(P('2. Техподдержка L3 (ядро) — самые частые пути', 'h1'))
doc.append(P('L3 работает «от тикета»: найти сервер → оценить состояние → выполнить операцию → проверить результат и сообщить клиенту. Ниже — клик-пути ключевых операций.', 'body'))

cards = [
 ('UI-L3-01. Перезапуск / остановка сервиса (+очистка)', [
  'Поиск клиента (UI-01) → отметить строку флажком.',
  'Модуль «Служба». При необходимости отметить опции: «Удалить лицензии» (удалит HostAccess.dat, RestrictionsState.dat, опц. LicensingState.dat), «Удалить unsaveddata», «Аварийное прерывание».',
  'Выбрать время: Сейчас / Очередь / Тех.окно / Через 1–9 ч / ЧЧ:ММ; при регулярности — периодичность D/W/M/Q/Y.',
  'Нажать «Остановка» (служба → Disabled) или «Перезапуск» (→ Auto).',
  'Наблюдать: статус в строке (если включено отслеживание) и логи операции; дождаться завершения.',
 ], 'Фолбэк: не отвечает — «Аварийное прерывание»; статус «CONTAINERCREATING» застрял — отдельный инструмент исправления статуса пода (по флажкам).', 'Новому UI: прогресс и этапы долгой операции, ETA, уведомление о завершении — сейчас «процесс занимает длительное время, а никаких подробностей не предоставляется» (DO-1431).'),
 ('UI-L3-02. Лицензии: отвязать / обновить / удалить / кэш', [
  'Способ А (по списку): поиск → отметить флажками записи → модуль «Лицензии» → кнопка «Отвязать» / «Удалить» / «Обновить» / «Обнов. кэш».',
  'Способ Б (одиночный): ввести CRM ID или UID в поле над кнопками (по CRM ID быстрее; UID «старого образца» тоже принимается) → нажать соответствующую кнопку.',
  'Успех: всплывает окно с сообщением, поле очищается.',
  'Ветка «красный Cloud»: «upRevision» + «Обновить» → синхронизация UOC (Postman: execSyncWithCrm; админка веба: Synchronize → Flush UOC binding → Check credentials; облачко позеленело — ок).',
  'Ветка «не пускает в веб-приложение» (BCrypt): Cloud Tools → «Обслуживание» → Groovy.jsp → скрипты Bcrypt part 1 и part 2 (до 5 минут; part 1 перезапускает сервер).',
 ], None, 'Новому UI: один диагностический чек-лист «лицензия не работает» вместо цепочки xHOSM → Postman → админка; кнопки должны сообщать, что именно сделали.'),
 ('UI-L3-03. Период редактирования документов', [
  'По инструкции проверить допустимость (тариф, размер БД, до 180 / свыше 180 дней, согласования).',
  'Поиск → флажок на сервере.',
  'Модуль «Конфигурация»: в поле «имя параметра» — db-period-length-days, в поле значения — нужное число дней.',
  'Отметить опцию «перезапустить Tomcat» → «Сохранить».',
  'Проверить результат: «больше информации» (период отображается), статус сервера.',
 ], None, 'Новому UI: правила и лимиты — прямо у поля (подсказка по тарифу/сроку), статус согласований; сейчас правила живут на вики, а не в интерфейсе.'),
 ('UI-L3-04. Изменение памяти (Xmx)', [
  'Диагностика: «больше информации» (память), логи, метрики.',
  'Поиск → флажок → «Конфигурация» → параметр memory → новое значение (кратно: 1.5×/2×).',
  '«Сохранить» + перезапуск Tomcat.',
  'Проверить: память в «больше информации», статус; при ОЛАП — повторная диагностика.',
 ], None, 'Новому UI: подсказка рекомендуемого значения и объяснение ограничений (нельзя «на глаз»/уменьшать без причины — DO-343, DO-1106); калькулятор RAM из нового GUI убран.'),
 ('UI-L3-05. Обновление версии', [
  'Поиск → отметить один или несколько серверов флажками.',
  'Модуль «Версия»: выбрать версию из выпадающего списка (Branch, Beta, Бренд, Front/Office), при необходимости — опции выкладывания дистрибутивов Front/Office; флаги Downgrade / Unlock / Rapid — только осознанно.',
  'Выбрать время выполнения (сейчас / очередь / тех.окно).',
  '«Обновить» → наблюдать выполнение; проверить логи (PgSQL-бекапы ищутся с тильдой в имени БД на том же SQL-сервере; MSSQL-бекап — на \\\\hosfiles-3\\quick_exchange; файлы новой версии копируются с \\\\mria\\distriiko).',
  'После обновления: обновить статус/версию в строке, сообщить клиенту.',
 ], 'Нюанс: при MSSQL-БД происходит снятие с зеркалирования. Блокировка «нельзя — открытые смены» (DO-1936) — причина уточняется у разработки.', 'Новому UI: видимые этапы (файлы → бекап → рестарт → ревизия) и ETA; блокировки с объяснением и способом решения.'),
 ('UI-L3-06. Логи: посмотреть, найти, скачать', [
  'Поиск → в строке кликнуть поле «Логи» → открыть нужный файл (error / full / JMS / startup / threaddump).',
  'Кнопка «V» — переход в Victoria Logs по серверу.',
  'Нужен пакет для разбора — скачать ZIP (включая ротационные).',
  'Сервер остановлен — смотреть Archive1/Archive2 (пишутся каждые 15 минут).',
 ], None, 'Новому UI: встроенный поиск по всем логам клиента и live-режим («tail -F») — сейчас логи скачивают на свою машину, а докачка качает всё заново (DO-899).'),
 ('UI-L3-07. Бекап БД', [
  'Остановить службу Tomcat (обязательно для бекапа/восстановления/переноса).',
  'Поиск → отметить до 5 серверов флажками (ограничение из-за нагрузки; для PGSQL идёт конвертация через промежуточную MSSQL-базу).',
  'Модуль «Бекап БД»: тип файла (.bak/.dmp), папка, «Архивировать после», при необходимости «Сделать бекап на FTP» (euftp.syrve.online) и «Анонимизация».',
  'Запустить; сообщения о стадиях выводятся в правом верхнем углу окна; дождаться завершения.',
  'Отметить «запустить Tomcat после» (или запустить вручную в «Службе»).',
 ], 'Выдача партнёру: в «Обслуживании» → «Создание папки на FTP» → «Выполнить» → передать путь и доступ; логи покажут папку и креды.', 'Новому UI: мастер «сделать/найти/выдать бекап», история бекапов сервера, живые ссылки (сейчас «списки находятся, а ссылки не открываются», DO-899).'),
 ('UI-L3-08. Восстановление / перенос / копирование БД', [
  'Остановить Tomcat.',
  'Восстановление (1 строка): выбрать файл .bak из \\\\hosfiles\\Быстрый_обмен\\ → отметить «Пересоздать БД» → «Восстановить из бекапа» → по завершении запустить Tomcat (внимание: после загрузки период станет 60 дней).',
  'Перенос (до 5 строк): выбрать SQL-сервер назначения, БД назначения (пусто — не менять имя), «Пересоздать БД» → запустить; прогресс — в правом верхнем углу.',
  'Внутри: MSSQL↔PGSQL — конвертация FullConvert; PGSQL→PGSQL — pg_dump/pg_restore (временный файл на HOSSUPPORT D:\\Backups); MSSQL→MSSQL — sqlcmd через \\\\hosfiles\\Быстрый_обмен\\.',
 ], None, 'Новому UI: превью плана («что будет сделано») до запуска, этапы, безопасный откат; сейчас риск (пересоздание/удаление) прикрыт только подтверждениями.'),
 ('UI-L3-09. Кассовые смены: закрыть / удалить', [
  'Остановить сервер («Служба» → «Остановка», дождаться статуса STOPPED; иногда нужно обновить страницу для актуализации статуса).',
  'Модуль «Разное» → «Закрыть смену»: появится список открытых смен → скопировать строку UUID YYYY-MM-DD HH:MM целиком → вставить в поле → исправить дату-время закрытия → «Ок» (связанные документы переведутся в статус АЗ).',
  'Если смен несколько — снять галку автозапуска Tomcat справа от кнопки, чтобы сервер не перезапускался после каждой операции.',
  '«Удалить смену» — аналогично, по выбору из списка.',
  'После работы — запустить Tomcat.',
 ], 'Партнёрам выдают инструкцию («Закрытие смены — инструкция для партнёров» на вики).', 'Новому UI: список смен с массовыми галочками и шаблонами («закрыть до даты») — сейчас «по одной ну ооочень долго», люди пишут SQL-скрипты (DO-969).'),
 ('UI-L3-10. SQL-запрос и Groovy-скрипт', [
  'SQL: вкладка «SQL» → ввести запрос → для записи включить флаг «Разрешить изменения» → выполнить; лимит вывода 100 строк, дальше — CSV; массовый режим — до 1500 серверов (Statistics).',
  'Groovy: вкладка Cloud Tools → «Обслуживание» → Groovy.jsp → выбрать скрипт → запустить (до 5 минут; часть скриптов рестартит сервер).',
 ], None, 'Новому UI: история и общие сохранённые запросы (сейчас «избранные SQL» не прижились — пишут заново); понятные последствия записи на боевом.'),
 ('UI-L3-11. Обрезка базы (shrink) — тяжёлый путь', [
  'Правило: дата обрезки не позднее начала открытого периода минус 1 год; резать последовательно (Chain → RMS), контролируя балансы.',
  'Сделать ручной бекап на сервер контура.',
  'Остановить сервер в xHOSM.',
  '«Конфигурация»: снять галку перезапуска; прописать db-shrink-no-backup=true и db-shrink-date=YYYY-MM-DD; вернуть галку; включить db-shrink-exclusive-mode=true (эксклюзивный режим).',
  'Дождаться успеха в логах (статус Complete, «balances before = after»); при ошибке действовать по тексту в логах (инструкция описывает, когда надо восстанавливать бекап).',
  'Выключить эксклюзивный режим (false), запустить сервер; сделать пометку через значок «i» у сервера (комментарий о shrink).',
 ], None, 'Новому UI: мастер shrink с проверками и автопометкой — сейчас всё вручную, включая пометку.'),
 ('UI-L3-12. Перевод RMS → Chain (мастер-цепочка)', [
  'Поиск по CRM ID (пример: RMS 3725122, Chain 6711911).',
  'Отметить RMS → запустить скрипт №1 (репликация + остановка Tomcat).',
  'Вкладка «Бекапы»: галочка на RMS → файл .dmp PGSQL → папка назначения по контуру (например, \\\\hossupport-eu\\Backups) → «запустить Tomcat после»; дождаться, инфо — в окне логов.',
  'Отметить Chain → указать версию → «Создать 1» (предпроверка).',
  'Остановить Tomcat Chain → «Восстановить»: тип PGSQL, файл бекапа, «пересоздать БД», без автозапуска.',
  'Скрипт №2 (Server Instance) → при ошибке «операция только для чейна» — «Ревизия» на 1-й вкладке → скрипт №3 после запуска сервера.',
 ], None, 'Новому UI: превратить цепочку «кнопок №1–3» в пошаговый мастер с прогрессом и откатом.'),
 ('UI-L3-13. Демо-стенд для разбора', [
  'partners.iiko.ru → демо-кабинеты → добавить (RMS/сеть; город РФ на этапе создания для RU).',
  'Если галка «активировать сервер» не ставилась — идти в xHOSM и создать сервер вручную (поиск по UID).',
  'Выбрать версию → развернуть; восстановить бекап клиента (с анонимизацией); для EU — сменить адрес в CRM на европейский, сервер определится в евро-зону.',
  'Лицензия: боевая при объёмах >150 тыс. продаж.',
 ], None, 'Новому UI: «мои демо» и избранное (DO-1311), шаблоны, срок жизни стенда.'),
 ('UI-L3-14. Восстановление хостинга из архива', [
  'Сначала автоматика: в ЛК чейна «Распределение лицензий» → удалить лицензии с RMS → сохранить → распределить заново → сохранить (это даёт команду на автозапуск; сервера поднимаются за ~10–15 минут, worst ~1 час).',
  'Если не сработало: XHOSM → найти сервер (crmid / uid / domain) → выделить галочкой → вкладка «Разное», блок «Архив» → «Восстановление» (параметр «Авто» + галка «Запустить»).',
 ], None, 'Новому UI: показывать статус «восстанавливается из архива» с ETA, а не только менять цвет строки.'),
]
for t, steps_, fb, ui in cards:
    doc.append(P(t, 'h3'))
    for i, s_ in enumerate(steps_, 1):
        doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
    if fb:
        doc.append(P(f'<b>{fb}</b>', 'note'))
    if ui:
        doc.append(P(f'<b>{ui}</b>', 'note'))
    cid = t.split('.')[0].strip()
    if cid in FLOWS:
        doc.append(P(f'Схема пути: {cid}', 'small'))
        doc.append(diagram(FLOWS[cid]))
    doc.append(Spacer(1, 4))

# ---------- ОСТАЛЬНЫЕ ----------
doc.append(P('3. L3 Web', 'h1'))
doc.append(P('Работают по веб-модулям клиентов: смотрят логи и конфиги, чинят доступы, отслеживают состояние после операций.', 'body'))
doc.append(P('UI-W-01. Разбор веб-инцидента', 'h3'))
for i, s_ in enumerate([
 'Поиск (CRM ID/домен) → флажок на строке (включить отслеживание статуса/версии).',
 'Логи: «Логи» в строке → error/full → кнопка «V» (Victoria) для глубокого поиска.',
 'Конфигурация: просмотр/правка параметров resto.properties (например, якорные параметры веба) → «Сохранить» (+рестарт при необходимости).',
 'Фиксы доступа (например, BCrypt) — через Groovy (UI-L3-10); после — проверить вход в веб-приложение.',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('<b>Что учесть:</b> «Не хватало доки для работы с ошибками в xhosm» (ретро, 2025); зависимость от ручных Postman-шагов.', 'note'))
doc.append(P('Схема пути: UI-W-01', 'small'))
doc.append(diagram(FLOWS['UI-W-01']))

doc.append(P('4. Аналитики', 'h1'))
doc.append(P('RMS/Chain-аналитики: демо-стенды, бета-версии, сборки, массовые выгрузки. Аналитик данных: SQL и статистика.', 'body'))
doc.append(P('UI-A-01. Массовая статистика', 'h3'))
for i, s_ in enumerate([
 'Вкладка «SQL» → массовый режим «Statistics».',
 'Задать фильтры/показатели → запустить по выборке (до 1500 серверов).',
 'Прогресс обновляется каждые 15 секунд; по завершении — выгрузка ZIP.',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('Схема пути: UI-A-01', 'small'))
doc.append(diagram(FLOWS['UI-A-01']))
doc.append(P('UI-A-02. Бэкап для передачи (разработке/партнёру)', 'h3'))
for i, s_ in enumerate([
 'Остановить Tomcat → «Бекап БД» → отметить «Анонимизация» → при необходимости «Сделать бекап на FTP».',
 'Дождаться завершения, взять из логов путь и доступ; передать адресату.',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('Схема пути: UI-A-02', 'small'))
doc.append(diagram(FLOWS['UI-A-02']))
doc.append(P('UI-A-03. Бета-версия на тестовом сервере', 'h3'))
for i, s_ in enumerate([
 'Поиск сервера → «Версия» → выбрать бета-версию (Beta/Branch) → обновить.',
 'Проверить статус/логи, зафиксировать результат в задаче.',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('Схема пути: UI-A-03', 'small'))
doc.append(diagram(FLOWS['UI-A-03']))
doc.append(P('UI-A-04. SQL-выборки', 'h3'))
doc.append(P('Вкладка «SQL» → запрос → результат (до 100 строк) → CSV. Частые запросы — из базы знаний (вручную).', 'body'))
doc.append(P('Схема пути: UI-A-04', 'small'))
doc.append(diagram(FLOWS['UI-A-04']))

doc.append(P('5. Инфраструктура', 'h1'))
doc.append(P('Создание серверов, переезды между кластерами, архивы, разборы производительности.', 'body'))
doc.append(P('UI-I-01. Создание клиента (NSR)', 'h3'))
for i, s_ in enumerate([
 'Поиск → отметить ровно одну строку (ограничение: 1 строка).',
 'Задать: Регион (по умолчанию RUS), Версию, Тариф (подставится из CRM), опции «в Чейне» (авто из CRM) и «для КЦ».',
 'Кнопка «#» — при необходимости выбрать часовой пояс и язык (для RUS по умолчанию Europe/Moscow/ru-RU).',
 '«Проверить»: домен сгенерируется транслитерацией, пройдёт проверка ресурсов; к домену добавится «-co» (при лицензии Chain) или «-cc» (для КЦ); появится ответ сервиса HOSM с параметрами Tomcat/Hoscluster; слово «контракт» подсветится зелёным/красным.',
 'При необходимости «Cancel» → вручную поправить домен → «Проверить» повторно → «OK».',
 'Создание встанет в очередь — смотреть по кнопке «#» (тултип на строке покажет подробности).',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('<b>Что учесть:</b> «Показать очередь» у пользователей «всегда пуста» (интервью); нужен явный экран очереди с прогрессом.', 'note'))
doc.append(P('Схема пути: UI-I-01', 'small'))
doc.append(diagram(FLOWS['UI-I-01']))
doc.append(P('UI-I-02. Переезд между кластерами / на другой SQL', 'h3'))
doc.append(P('Как «Перенос/копирование» (UI-L3-08): SQL-сервер назначения → БД (пусто — не менять) → «Пересоздать БД» → запуск; прогресс в верхнем правом углу. Для больших миграций — порциями, в тех.окно.', 'body'))
doc.append(P('Схема пути: UI-I-02', 'small'))
doc.append(diagram(FLOWS['UI-I-02']))
doc.append(P('UI-I-03. Архивы', 'h3'))
doc.append(P('Вкладка «Разное», блок «Архив»: «Архивация» / «Восстановление» / «Удаление» / «Переименование» — по флажкам; события хосробота (domainenabled/disabled/archived/deleted) смотреть в ленте истории.', 'body'))
doc.append(P('Схема пути: UI-I-03', 'small'))
doc.append(diagram(FLOWS['UI-I-03']))

doc.append(P('6. Партнёры и аккаунт-менеджеры', 'h1'))
doc.append(P('Внешние пользователи видят урезанный функционал — это важно для дизайна и прав.', 'body'))
doc.append(P('UI-P-01. Проверка клиента', 'h3'))
for i, s_ in enumerate([
 'Для внешних клиентов в результатах выводятся Название и CRM ID; функционал ограничен просмотром UID, пароля iikoUser и контракта (без операций).',
 'Поиск (CRM ID/домен) → клик по кнопкам UID / iikoUser / Контракт → значение появится в строке.',
 'Переход в CRM по ссылке «Контрагент» (или «goCRM» из модуля лицензий).',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('Схема пути: UI-P-01', 'small'))
doc.append(diagram(FLOWS['UI-P-01']))
doc.append(P('UI-P-02. Закрытие смены (по инструкции для партнёров)', 'h3'))
for i, s_ in enumerate([
 'Выбрать сервер в xHOSM — цвет строки и статус обновятся.',
 '«Служба» → «Остановить» → дождаться STOPPED (возможно, обновить страницу).',
 '«Разное» → «Закрыть смену»: если смен несколько — снять галку автозапуска Tomcat; скопировать UUID и дату-время нужной смены, скорректировать время → «Ок».',
 'Перезапустить Tomcat после работы.',
], 1):
    doc.append(Paragraph(s_, S['step'], bulletText=f'{i}.'))
doc.append(P('Схема пути: UI-P-02', 'small'))
doc.append(diagram(FLOWS['UI-P-02']))
doc.append(P('UI-P-03. Запрос данных/бекапа', 'h3'))
doc.append(P('Запрос бекапа: поддержка готовит бекап и (при необходимости) создаёт FTP-папку → партнёр забирает по полученному пути и доступу. Пожелание интерфейса: «контракт видеть без похода в CRM» (DO-1329) и английская локализация (DO-1218).', 'body'))
doc.append(P('Схема пути: UI-P-03', 'small'))
doc.append(diagram(FLOWS['UI-P-03']))

doc.append(P('7. Разработка', 'h1'))
doc.append(P('UI-D-01. Разбор бага по клиенту', 'h3'))
doc.append(P('Поиск → «Логи» / «V» (Victoria) → при необходимости скачать ZIP или запросить анонимизированный бекап; конфигурацию смотреть в модуле «Конфигурация» (только чтение для их задач).', 'body'))
doc.append(P('Схема пути: UI-D-01', 'small'))
doc.append(diagram(FLOWS['UI-D-01']))
doc.append(P('UI-D-02. Сборки и сертификаты', 'h3'))
doc.append(P('Сборка версий Cloud Tools — сейчас запускается из xHOSM (см. DO-976), но по плану выпиливается в отдельный контур («не целевой функционал»); в новом GUI добавляется управление сертификатами devPortal.', 'body'))
doc.append(P('Схема пути: UI-D-02', 'small'))
doc.append(diagram(FLOWS['UI-D-02']))

doc.append(P('8. Сквозные выводы для нового интерфейса', 'h1'))
for r in [
 '<b>Вход:</b> убрать «неудобный аутентификатор» — SSO/долгая сессия, возврат к прерванному действию.',
 '<b>Поиск:</b> умный ввод с подсказками типов, конструктор условий вместо WHERE, связи Chain↔RMS, сохранённые выборки; фильтры — и до, и после поиска.',
 '<b>Статус:</b> достоверность и объяснимость (источник, время, история), честное «данные устарели» вместо ложных статусов.',
 '<b>Операции:</b> единый паттерн — план → подтверждение → этапы/прогресс → результат → уведомление; очередь и тех.окно — часть этого.',
 '<b>Массовость:</b> смены, лицензии, обновления, конфиги — «списком», а не «по одной штуке».',
 '<b>Один экран клиента:</b> контракт, дилер, лицензии, UID/iikoUser, память, период, история — без прыжков в CRM/Postman/админку.',
 '<b>Права:</b> урезанный режим партнёров и матрица ролей — проектировать явно, с объяснением недоступных действий.',
 '<b>Новичкам:</b> стартовая страница-навигация («что где лежит») — прямой запрос поддержки (DO-899).',
]:
    doc.append(Paragraph(r, S['step'], bulletText='•'))

doc.append(P('9. Открытые вопросы (уточнить у L3/веба)', 'h1'))
for q in [
 'Точные тексты сообщений и модальных окон в операциях (для правдоподобных макетов) — нужен проход по стенду xhosm-test или скринкаст.',
 'Частоты: какие действия реально ежедневные (для приоритетов экранов).',
 'Отдельные ветки L3 Web: чего не хватает в описанных путях.',
 'Кто и как согласует тех.окна и открытие периода (для UX планировщика).',
 'Партнёры: какие 3–5 действий должны уметь сами (самообслуживание) по мнению АМ.',
]:
    doc.append(Paragraph(q, S['step'], bulletText='•'))
doc.append(Spacer(1, 4))
doc.append(P('Черновик v1 — для проверки командой: пройдите свои любимые пути и пометьте, где шаги/названия расходятся с реальностью. После валидации это основа для прототипов.', 'small'))

make_pdf(os.path.join(OUT, 'xHOSM_сценарии_интерфейса_v1.pdf'),
         'xHOSM · сценарии работы с интерфейсом (черновик v1) · 18.09.2026', doc)
print('OK')
for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(os.path.join(OUT, f)))
