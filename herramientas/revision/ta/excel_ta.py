# -*- coding: utf-8 -*-
"""Excel de revisión de Terminaciones anticipadas: la misma estructura que el de Derecho de petición
(hojas «Unidad N - revisión» con pestaña coral, fila 1 = lecciones, columna A = # diapositiva, una celda por
diapositiva con el letrero «Propuesta:» FUERA de la miniatura, el título y un comentario corto si hace falta,
y la miniatura pegada al fondo de la celda) más «Generales - revisión»."""
import glob, json, math, os, sys
import openpyxl
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.drawing.image import Image as XLImage
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, OneCellAnchor
from openpyxl.drawing.xdr import XDRPositiveSize2D
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.utils.units import pixels_to_EMU
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maqueta as M
sys.path.insert(0, '/home/claude/repo/herramientas/revision')
from mapa_revision import a_compartidas

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, 'out')
ANCHO_COL = 92
MINI_W, MINI_H = 560, 315
CHARS_LINEA = 36
PT_LINEA = 26.5
AMARILLO = PatternFill('solid', fgColor='FFF2CC')
FINO = Side(style='thin', color='FF999999')
BORDE = Border(left=FINO, right=FINO, top=FINO, bottom=FINO)
F_PROP = InlineFont(rFont='Arial', sz=20, b=True, color='FFEE616B')
F_TIT = InlineFont(rFont='Arial', sz=20, b=True, color='FF002F46')
F_COM = InlineFont(rFont='Arial', sz=20, color='FF222222')
GENERALES = json.load(open(os.path.join(AQUI, 'generales.json'), encoding='utf-8'))


def mini(clave):
    src = os.path.join(OUT, 'final', clave + '.png')
    # PNG de 800 px, como las miniaturas del Excel de Derecho de petición, que sí se ven en Excel, Sheets y
    # LibreOffice (la primera entrega iba en JPEG de 1120 px y Sebastián no vio las miniaturas).
    os.makedirs(os.path.join(OUT, 'mini_pal'), exist_ok=True)
    dst = os.path.join(OUT, 'mini_pal', clave + '.png')
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
        Image.open(src).convert('RGB').resize((800, 450), Image.LANCZOS).quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(dst, optimize=True)
    return dst


def lineas(t):
    return max(1, math.ceil(len(t) / CHARS_LINEA)) if t else 0


def main(salida):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    for u in (1, 2, 3, 4):
        ws = wb.create_sheet('Unidad %d - revisión' % u)
        ws.sheet_properties.tabColor = 'EE616B'
        lecs = sorted(k for k in M.HEADINGS if k.startswith('%d.' % u))
        ws['A1'] = '# diapositiva'
        ws.column_dimensions['A'].width = 16
        for j, k in enumerate(lecs, 2):
            c = ws.cell(1, j, M.HEADINGS[k])
            ws.column_dimensions[get_column_letter(j)].width = ANCHO_COL
        for c in ws[1]:
            c.font = Font(name='Arial', size=16, bold=True, color='FF002F46')
            c.fill = AMARILLO
            c.border = BORDE
            c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center' if c.column == 1 else 'left')
        ws.row_dimensions[1].height = 66
        ws.freeze_panes = 'B2'
        altos, imgs, maxn = {}, [], 0
        for j, k in enumerate(lecs, 2):
            meta = json.load(open(os.path.join(OUT, 'meta_L%s.json' % k), encoding='utf-8'))
            maxn = max(maxn, len(meta))
            for m in meta:
                fila = m['n'] + 1
                c = ws.cell(fila, j)
                partes = [TextBlock(F_PROP, 'Propuesta: '), TextBlock(F_TIT, m['titulo'])]
                if m.get('com'):
                    partes.append(TextBlock(F_COM, '\n' + m['com']))
                c.value = CellRichText(*partes)
                c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='left')
                c.border = BORDE
                n = lineas('Propuesta: ' + m['titulo']) + lineas(m.get('com', ''))
                h = (n + 0.6) * PT_LINEA + MINI_H * 0.75 + 16
                altos[fila] = max(altos.get(fila, 0), h)
                imgs.append((fila, j, mini('L%s_E%02d' % (k, m['n']))))
        for fila in range(2, maxn + 2):
            a = ws.cell(fila, 1, fila - 1)
            a.font = Font(name='Arial', size=16, bold=True)
            a.alignment = Alignment(horizontal='center', vertical='top')
            a.border = BORDE
            for j in range(2, len(lecs) + 2):
                c = ws.cell(fila, j)
                c.border = BORDE
                if c.value is None:
                    c.value = '(la lección termina antes)'
                    c.font = Font(name='Arial', size=15, italic=True, color='FF8A9BA3')
                    c.alignment = Alignment(vertical='top')
            ws.row_dimensions[fila].height = altos.get(fila, 40)
        for fila, col, png in imgs:
            im = XLImage(png)
            im.width, im.height = MINI_W, MINI_H
            off = int(altos[fila] * 4 / 3) - MINI_H - 10
            im.anchor = OneCellAnchor(_from=AnchorMarker(col=col - 1, colOff=pixels_to_EMU(10), row=fila - 1, rowOff=pixels_to_EMU(off)),
                                      ext=XDRPositiveSize2D(pixels_to_EMU(MINI_W), pixels_to_EMU(MINI_H)))
            ws.add_image(im)
    ws = wb.create_sheet('Generales - revisión')
    ws.sheet_properties.tabColor = 'EE616B'
    ws['A1'], ws['B1'] = '#', 'Generales: lo que se repite en todo el curso'
    for c in ws[1]:
        c.font = Font(name='Arial', size=16, bold=True, color='FF002F46')
        c.fill = AMARILLO
        c.border = BORDE
        c.alignment = Alignment(vertical='center', wrap_text=True)
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 130
    ws.row_dimensions[1].height = 36
    for i, t in enumerate(GENERALES, 2):
        a = ws.cell(i, 1, i - 1)
        a.font = Font(name='Arial', size=16, bold=True)
        a.alignment = Alignment(horizontal='center', vertical='top')
        b = ws.cell(i, 2, t)
        b.font = Font(name='Arial', size=18)
        b.alignment = Alignment(wrap_text=True, vertical='top')
        a.border = b.border = BORDE
        ws.row_dimensions[i].height = (math.ceil(len(t) / 105) + 0.5) * 24
    wb.save(salida)
    a_compartidas(salida)
    print(salida)


if __name__ == '__main__':
    main(sys.argv[1])
