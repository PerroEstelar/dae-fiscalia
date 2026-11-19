# -*- coding: utf-8 -*-
"""Arma el Excel del inventario de videos de profe a partir de datos.py."""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import datos as D
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

AR = 'Arial'
hf = Font(name=AR, bold=True, color='FFFFFF', size=10); hfill = PatternFill('solid', fgColor='1F3864')
thin = Side(style='thin', color='BFBFBF'); bd = Border(left=thin, right=thin, top=thin, bottom=thin)
nf = Font(name=AR, size=10); link = Font(name=AR, size=10, color='0563C1', underline='single')

def seg(d):
    if not d: return 0
    a = [int(x) for x in d.split(':')]
    return a[0] * 60 + a[1] if len(a) == 2 else a[0] * 3600 + a[1] * 60 + a[2]

wb = Workbook(); ws = wb.active; ws.title = 'Videos de profe'
COLS = [('Prioridad', 9), ('Curso', 34), ('Unidad', 10), ('Pieza', 30), ('Profesor o profesores', 30), ('Estado', 18),
        ('Duración', 9), ('Minutos', 9), ('Video (enlace)', 44), ('Subtítulos .srt (enlace)', 24), ('Carpeta de Drive (enlace)', 16),
        ('Gráfica', 20), ('Entregado', 11), ('Observaciones', 60)]
for j, (h, w) in enumerate(COLS, 1):
    c = ws.cell(row=1, column=j, value=h); c.font = hf; c.fill = hfill; c.border = bd
    c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    ws.column_dimensions[get_column_letter(j)].width = w
ws.row_dimensions[1].height = 34
prev = None; banda = False
for i, f in enumerate(D.F, 2):
    if f['curso'] != prev: banda = not banda; prev = f['curso']
    fill = PatternFill('solid', fgColor='EEF3F9' if banda else 'FFFFFF')
    ent = f['estado'] == 'Entregado'
    vals = [f['pri'], f['curso'], f['unidad'], f['pieza'], f['profe'], f['estado'], f['dur'] or '',
            round(seg(f['dur']) / 60.0, 1) if (ent and f['dur']) else '',
            f['archivo'] + ('.mov' if 'está en .mov' in f['nota'] else ('.mp4' if ent else '')),
            ('%d subtítulos' % f['n_srt']) if f['srt'] else ('' if not ent else 'Sin subtítulos'),
            'Abrir carpeta' if f['carpeta'] else '', f['grafica'], f['fecha'], f['nota']]
    maxl = 1
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=i, column=j, value=v); c.font = nf; c.border = bd; c.fill = fill
        c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='center' if j in (1, 3, 7, 8, 13) else 'left')
        w = COLS[j - 1][1]
        if isinstance(v, str) and v: maxl = max(maxl, -(-len(v) // max(8, int(w * 1.05))))
    if f['vid']: ws.cell(row=i, column=9).hyperlink = D.V % f['vid']; ws.cell(row=i, column=9).font = link
    if f['srt']: ws.cell(row=i, column=10).hyperlink = D.V % f['srt']; ws.cell(row=i, column=10).font = link
    if f['carpeta']: ws.cell(row=i, column=11).hyperlink = D.C % f['carpeta']; ws.cell(row=i, column=11).font = link
    ws.cell(row=i, column=8).number_format = '0.0'
    ws.row_dimensions[i].height = min(120, max(28, 13.5 * maxl + 4))
n = len(D.F) + 1
ws.freeze_panes = 'E2'; ws.auto_filter.ref = 'A1:%s%d' % (get_column_letter(len(COLS)), n)

# Resumen por curso
wr = wb.create_sheet('Resumen')
H = [('Prioridad', 10), ('Curso', 70), ('Videos entregados', 12), ('Minutos entregados', 12), ('Con subtítulos', 12), ('Gráfica provisional', 12), ('Pendientes o en pausa', 13), ('Profesor o profesores', 60)]
for j, (h, w) in enumerate(H, 1):
    c = wr.cell(row=1, column=j, value=h); c.font = hf; c.fill = hfill; c.border = bd
    c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center'); wr.column_dimensions[get_column_letter(j)].width = w
wr.row_dimensions[1].height = 34
cursos = []
for f in D.F:
    if (f['pri'], f['curso']) not in cursos: cursos.append((f['pri'], f['curso']))
SIN = [(1, 'Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado', 'No hay grabaciones de profe en la carpeta del curso.'),
       (2, 'Gerencia judicial', 'No hay grabaciones de profe en la carpeta del curso.'),
       (3, 'Investigación judicial y forense de la desaparición forzada', 'No hay grabaciones de profe en la carpeta del curso.')]
R = "'Videos de profe'!"
i = 2
for p, cu in cursos:
    profs = []
    for f in D.F:
        if f['curso'] == cu and f['estado'] == 'Entregado':
            for x in f['profe'].replace(' y ', ', ').split(', '):
                x = x.strip()
                if x and x not in profs: profs.append(x)
    vals = [p, cu,
            '=COUNTIFS(%s$B$2:$B$%d,B%d,%s$F$2:$F$%d,"Entregado")' % (R, n, i, R, n),
            '=ROUND(SUMIFS(%s$H$2:$H$%d,%s$B$2:$B$%d,B%d),0)' % (R, n, R, n, i),
            '=COUNTIFS(%s$B$2:$B$%d,B%d,%s$J$2:$J$%d,"*subtítulos",%s$J$2:$J$%d,"<>Sin subtítulos")' % (R, n, i, R, n, R, n),
            '=COUNTIFS(%s$B$2:$B$%d,B%d,%s$L$2:$L$%d,"Provisional*")' % (R, n, i, R, n),
            '=COUNTIFS(%s$B$2:$B$%d,B%d,%s$F$2:$F$%d,"<>Entregado")' % (R, n, i, R, n),
            ', '.join(profs)]
    for j, v in enumerate(vals, 1):
        c = wr.cell(row=i, column=j, value=v); c.font = nf; c.border = bd
        c.alignment = Alignment(horizontal='left' if j in (2, 8) else 'center', vertical='top', wrap_text=True)
    i += 1
t = i
for j, v in enumerate(['', 'Total', '=SUM(C2:C%d)' % (t - 1), '=SUM(D2:D%d)' % (t - 1), '=SUM(E2:E%d)' % (t - 1), '=SUM(F2:F%d)' % (t - 1), '=SUM(G2:G%d)' % (t - 1), ''], 1):
    c = wr.cell(row=t, column=j, value=v); c.font = Font(name=AR, size=10, bold=True); c.border = bd
    c.alignment = Alignment(horizontal='left' if j == 2 else 'center')
i = t + 2
c = wr.cell(row=i, column=2, value='Cursos sin videos de profe'); c.font = Font(name=AR, size=10, bold=True)
for p, cu, nota in SIN:
    i += 1
    for j, v in enumerate([p, cu, '', '', '', '', '', nota], 1):
        c = wr.cell(row=i, column=j, value=v); c.font = nf; c.border = bd
        c.alignment = Alignment(horizontal='left' if j in (2, 8) else 'center', vertical='top', wrap_text=True)
wr.freeze_panes = 'A2'

# Notas
wn = wb.create_sheet('Notas'); wn.column_dimensions['A'].width = 150
import notas
for i, (tx, b) in enumerate(notas.NOTAS, 1):
    c = wn.cell(row=i, column=1, value=tx); c.font = Font(name=AR, size=11 if b else 10, bold=bool(b))
    c.alignment = Alignment(wrap_text=True, vertical='top'); wn.row_dimensions[i].height = max(16, 14 * (-(-len(tx) // 150)) + 4)
wb.move_sheet('Resumen', offset=-1)
wb.active = 0
out = sys.argv[1] if len(sys.argv) > 1 else 'videos_de_profe.xlsx'
wb.save(out)
ent = [f for f in D.F if f['estado'] == 'Entregado']
print('filas', len(D.F), 'entregados', len(ent), 'min', round(sum(seg(f['dur']) for f in ent) / 60.0), 'con srt', sum(1 for f in ent if f['srt']), out)
