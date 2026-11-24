# -*- coding: utf-8 -*-
"""Excel «REVISION COMENTARIOS - <CURSO>»: solo comentarios, sin miniaturas.

Hojas «Unidad N - revisión»: fila 1 = lecciones, columna A = número de diapositiva tal como sale en los
pantallazos («U1 L1 - 03.png» es la fila 3 de la columna de la lección 1.1). Cada celda, una frase breve.
«Bien así.» va en gris, para que se vean de un golpe las que piden cambio. Hoja «Generales - revisión».

python3 excel_rev.py DA|DP <salida.xlsx>
"""
import glob, json, math, os, sys
import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/home/claude/repo/herramientas/revision')
import aplicar
from mapa_revision import a_compartidas

AQUI = os.path.dirname(os.path.abspath(__file__))
CURSOS = {'DA': 'Investigación y judicialización de delitos contra el medio ambiente y los recursos naturales',
          'DP': 'Derecho de petición y acción de tutela'}
F_COM = Font(name='Arial', size=20, color='FF222222')
F_BIEN = Font(name='Arial', size=20, color='FF7F8C8A')
F_TIT = Font(name='Arial', size=16, bold=True, color='FF002F46')
F_NUM = Font(name='Arial', size=16, bold=True, color='FF002F46')
CORAL = 'FFEE616B'
FONDO_TIT = PatternFill('solid', fgColor='FFF2CC')
FINO = Side(style='thin', color='FF999999')
BORDE = Border(left=FINO, right=FINO, top=FINO, bottom=FINO)
ANCHO = 62          # ancho de columna de lección (unidades de Excel)
CHARS = 38          # caracteres por renglón a Arial 20 en ese ancho
PT = 26.5           # alto de renglón a Arial 20


def titulo_leccion(cur, lec):
    """Título de la lección como lo muestra la cabecera del Genially (texto junto al chip «Lección N»)."""
    for f in sorted(glob.glob(os.path.join(AQUI, 'cap', cur, lec, '*.json')))[3:]:
        js = json.load(open(f, encoding='utf-8'))
        for t in js['frames'][0].get('t', []):
            if t['y'] < 100 and t['x'] > 450 and len(t['t']) > 12 and not t['t'].startswith('Page'):
                return t['t']
    return ''


def renglones(texto, chars=CHARS):
    n = 0
    for par in texto.split('\n'):
        n += max(1, math.ceil(len(par) / chars))
    return n


def generales(cur):
    return json.load(open(os.path.join(AQUI, 'generales_%s.json' % cur.lower()), encoding='utf-8'))


def main():
    cur, salida = sys.argv[1], sys.argv[2]
    S = aplicar.specs(cur)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    unidades = sorted({int(l.split()[0][1:]) for l in S})
    for u in unidades:
        ws = wb.create_sheet('Unidad %d - revisión' % u)
        ws.sheet_properties.tabColor = CORAL[2:]
        lecs = sorted([l for l in S if l.startswith('U%d ' % u)], key=lambda l: int(l.split()[1][1:]))
        ws.column_dimensions['A'].width = 16
        c = ws.cell(1, 1, 'Diapositiva')
        c.font, c.alignment, c.border, c.fill = F_TIT, Alignment(horizontal='center', vertical='center',
                                                                 wrap_text=True), BORDE, FONDO_TIT
        maxn = max(max(S[l]) for l in lecs)
        alto_tit = 0
        for j, lec in enumerate(lecs):
            col = j + 2
            ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = ANCHO
            l = int(lec.split()[1][1:])
            tit = 'Lección %d.%d\n%s' % (u, l, titulo_leccion(cur, lec))
            c = ws.cell(1, col, tit)
            c.font, c.border, c.fill = F_TIT, BORDE, FONDO_TIT
            c.alignment = Alignment(wrap_text=True, vertical='top')
            alto_tit = max(alto_tit, renglones(tit, 50) * 21 + 10)
        ws.row_dimensions[1].height = min(409, alto_tit)
        for n in range(1, maxn + 1):
            fila = n + 1
            c = ws.cell(fila, 1, n)
            c.font, c.border = F_NUM, BORDE
            c.alignment = Alignment(horizontal='center', vertical='top')
            alto = 1
            for j, lec in enumerate(lecs):
                c = ws.cell(fila, j + 2)
                c.border = BORDE
                if n not in S[lec]:
                    continue
                com = S[lec][n][0]
                c.value = com
                c.font = F_BIEN if com.startswith('Bien así') and not S[lec][n][1] else F_COM
                c.alignment = Alignment(wrap_text=True, vertical='top')
                alto = max(alto, renglones(com))
            ws.row_dimensions[fila].height = min(409, alto * PT + 8)
        ws.freeze_panes = 'B2'
    ws = wb.create_sheet('Generales - revisión')
    ws.sheet_properties.tabColor = CORAL[2:]
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 150
    c = ws.cell(1, 2, 'Generales: lo que se repite en todo el curso')
    c.font, c.fill, c.border = F_TIT, FONDO_TIT, BORDE
    ws.cell(1, 1).fill, ws.cell(1, 1).border = FONDO_TIT, BORDE
    ws.row_dimensions[1].height = 30
    for i, g in enumerate(generales(cur)):
        fila = i + 2
        a = ws.cell(fila, 1, i + 1)
        a.font, a.border = F_NUM, BORDE
        a.alignment = Alignment(horizontal='center', vertical='top')
        b = ws.cell(fila, 2, g)
        b.font, b.border = F_COM, BORDE
        b.alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[fila].height = min(409, renglones(g, 95) * PT + 8)
    wb.save(salida)
    a_compartidas(salida)
    print('ok', salida, [w.title for w in wb.worksheets])


if __name__ == '__main__':
    main()
