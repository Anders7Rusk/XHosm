# -*- coding: utf-8 -*-
"""Сборка v2 скрипта сценариев: добавляет блок-схемы ко всем 30 путям + легенду."""
import sys

P = '/opt/data/xhosm-redesign/'
src = open(P + 'build_ui_scenarios.py', encoding='utf-8').read()

ENGINE = '''
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
'''

FLOWS = '''
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
'''

REPS = []
REPS.append(('def make_pdf(path, footer_text, story):', ENGINE, 'before'))
REPS.append(('doc = []', FLOWS, 'before'))
REPS.append(("doc.append(P('Аудитории: L3 Support (ядро), L3 Web, аналитики (RMS/Chain и данных), инфраструктура, партнёры и АМ, разработка. Вход и базовые механики — общие для всех.', 'body'))",
             "doc.append(P('Легенда схем', 'h3'))\ndoc.append(legend())", 'after'))


def diag(k):
    return "doc.append(P('Схема пути: %s', 'small'))\ndoc.append(diagram(FLOWS['%s']))" % (k, k)

after_anchors = [
 ('просили стартовую страницу-навигацию (DO-899).\', \'note\'))', 'UI-00'),
 ('«Поле „Статус“ в поиске не используется» (интервью).\', \'note\'))', 'UI-01'),
 ('строка перегружена (~23 колонки из 70+ атрибутов, DO-586).\', \'note\'))', 'UI-02'),
 ('(ретро, 2025); зависимость от ручных Postman-шагов.\', \'note\'))', 'UI-W-01'),
 ('Частые запросы — из базы знаний (вручную).\', \'body\'))', 'UI-A-04'),
 ('нужен явный экран очереди с прогрессом.\', \'note\'))', 'UI-I-01'),
 ('Для больших миграций — порциями, в тех.окно.\', \'body\'))', 'UI-I-02'),
 ('смотреть в ленте истории.\', \'body\'))', 'UI-I-03'),
 ('(DO-1329) и английская локализация (DO-1218).\', \'body\'))', 'UI-P-03'),
 ('(только чтение для их задач).\', \'body\'))', 'UI-D-01'),
 ('управление сертификатами devPortal.\', \'body\'))', 'UI-D-02'),
]
before_anchors = [
 ("doc.append(P('UI-A-02. Бэкап для передачи (разработке/партнёру)', 'h3'))", 'UI-A-01'),
 ("doc.append(P('UI-A-03. Бета-версия на тестовом сервере', 'h3'))", 'UI-A-02'),
 ("doc.append(P('UI-A-04. SQL-выборки', 'h3'))", 'UI-A-03'),
 ("doc.append(P('UI-P-02. Закрытие смены (по инструкции для партнёров)', 'h3'))", 'UI-P-01'),
 ("doc.append(P('UI-P-03. Запрос данных/бекапа', 'h3'))", 'UI-P-02'),
]
for a, k in after_anchors:
    REPS.append((a, diag(k), 'after'))
for a, k in before_anchors:
    REPS.append((a, diag(k), 'before'))

# петля карточек: добавить схему после блока
loop_anchor = "    if ui:\n        doc.append(P(f'<b>{ui}</b>', 'note'))"
loop_new = """    if ui:
        doc.append(P(f'<b>{ui}</b>', 'note'))
    cid = t.split('.')[0].strip()
    if cid in FLOWS:
        doc.append(P(f'Схема пути: {cid}', 'small'))
        doc.append(diagram(FLOWS[cid]))
    doc.append(Spacer(1, 4))"""
REPS.append((loop_anchor, loop_new, 'replace'))

miss = []
for anchor, payload, mode in REPS:
    n = src.count(anchor)
    if n != 1:
        miss.append((n, anchor[:70]))
        continue
    if mode == 'before':
        src = src.replace(anchor, payload + '\n' + anchor)
    elif mode == 'after':
        src = src.replace(anchor, anchor + '\n' + payload)
    else:
        src = src.replace(anchor, payload)

if miss:
    print('ПРОБЛЕМА, вставки не найдены:')
    for n, a in miss:
        print(' ', n, '×', a)
    sys.exit(1)

# добавить схему для UI-W? уже добавлено в after_anchors
open(P + 'build_ui_scenarios_v2.py', 'w', encoding='utf-8').write(src)
print('OK: build_ui_scenarios_v2.py записан')
