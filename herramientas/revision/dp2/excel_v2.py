# -*- coding: utf-8 -*-
"""Excel de revisión de Derecho de petición, v2: el mismo Excel del 23 nov (hojas «Unidad N - revisión» y «Generales -
revisión», el comentario de una frase y el boceto de cada celda) más la PROPUESTA ya hecha, como en el de Terminaciones
anticipadas: «Propuesta:» en coral fuera de la miniatura, el título de la pantalla corregida y su miniatura real (la
escena tal como queda en el Genially: marco + mediación), y debajo el boceto de la revisión.

python3 excel_v2.py <mapa.xlsx> <revision_dp.json> <carpeta bocetos> <salida.xlsx>
Las miniaturas reales salen de capturas_prop.py (out/prop/L<u>.<l>_E<nn>.png).
"""
import json, math, os, sys
from copy import copy
sys.path.insert(0, '/home/claude/repo/herramientas/revision')
import mapa_revision as MR
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.drawing.image import Image as XLImage
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, OneCellAnchor
from openpyxl.drawing.xdr import XDRPositiveSize2D
from openpyxl.styles import Alignment
from openpyxl.utils.units import pixels_to_EMU
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
PROP = os.path.join(AQUI, 'out', 'prop')
COMP = os.path.join(AQUI, 'out', 'excel_v2_png')
ESC = json.load(open(os.path.join(AQUI, 'out', 'escenas_dp.json'), encoding='utf-8'))
F_PROP = InlineFont(rFont='Arial', sz=20, b=True, color='FFEE616B')
F_TIT = InlineFont(rFont='Arial', sz=20, b=True, color='FF002F46')
F_COM = InlineFont(rFont='Arial', sz=20, color='FF222222')
ANCHO = 560                 # px en la hoja (como el Excel de TA); el PNG va a 800
ESCALA = 800 / ANCHO
CHARS_LINEA = 35
PT_LINEA = 26.5

# Celda de la revisión (fila del mapa) -> escenas de la lección revisada. Salió de cruzar el comentario de cada celda
# (y el E de su boceto) con las escenas de la revisión: donde el mapa tiene menos filas que el Genially, una celda
# cubre dos escenas (E04-E05 de la 2.3, el caso 1 de la 4.4…) y las pantallas nuevas (4.4 de la 2.3, cierre de la
# 3.3, caso práctico y cuadro de la 4.3) caen en la celda que pedía la omisión.
def seguidas(a, b, d=1):
    return {r: [r - d] for r in range(a, b + 1)}


MAPA = {
    '1.1': seguidas(2, 12), '1.2': {2: [1, 2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7], 8: [8]}, '1.3': seguidas(2, 8),
    '1.4': seguidas(2, 3), '2.1': seguidas(2, 10), '2.2': seguidas(2, 10),
    '2.3': {2: [1], 3: [2], 4: [3], 5: [4, 5], 6: [6], 7: [7], 8: [8], 9: [9], 10: [10], 11: [11]},
    '2.4': seguidas(2, 7), '3.1': {2: [1], 3: [2], 4: [3], 5: [5], 6: [6], 7: [7], 8: [8]}, '3.2': seguidas(2, 10),
    '3.3': {2: [1], 3: [2], 4: [3], 5: [4, 5], 6: [6], 7: [7], 8: [8], 9: [9], 10: [10]}, '3.4': seguidas(2, 13),
    '4.1': seguidas(2, 11), '4.2': {2: [1], 3: [2], 4: [3], 5: [4], 6: [5], 7: [6, 7], 8: [8], 9: [9], 10: [10]},
    '4.3': seguidas(2, 14),
    '4.4': {2: [1], 3: [2], 4: [3], 5: [4, 5], 6: [6], 7: [7], 8: [8], 9: [9], 10: [10, 11], 11: [12], 12: [13],
            13: [14], 14: [15], 15: [16]},
}
COL = {'B': 1, 'C': 2, 'D': 3, 'E': 4}


def fuente(tam, negrita=False):
    for f in ('/usr/share/fonts/truetype/liberation/LiberationSans-%s.ttf' % ('Bold' if negrita else 'Regular'),
              '/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf' % ('-Bold' if negrita else '')):
        if os.path.exists(f):
            return ImageFont.truetype(f, tam)
    return ImageFont.load_default()


def compuesto(clave, escenas, boceto):
    """PNG de 800 px: la(s) miniatura(s) real(es) y, debajo, el boceto de la revisión con su rótulo gris."""
    W = 800
    partes = []
    for k, n in enumerate(escenas):
        im = Image.open(os.path.join(PROP, 'L%s_E%02d.png' % (clave[0], n))).convert('RGB').resize((W, 450), Image.LANCZOS)
        partes.append(im)
        if k < len(escenas) - 1:
            partes.append(Image.new('RGB', (W, 12), 'white'))
    if boceto:
        rot = Image.new('RGB', (W, 56), 'white')
        ImageDraw.Draw(rot).text((2, 22), 'Boceto de la revisión del 23 de noviembre', font=fuente(22), fill=(120, 136, 145))
        partes.append(rot)
        b = Image.open(boceto).convert('RGB')
        bw = int(460 * ESCALA)
        partes.append(b.resize((bw, round(b.height * bw / b.width)), Image.LANCZOS))
    H = sum(p.height for p in partes)
    lienzo = Image.new('RGB', (W, H), 'white')
    y = 0
    for p in partes:
        lienzo.paste(p, (0, y))
        y += p.height
    lienzo.paste(Image.new('RGB', (W, 1), (190, 200, 205)), (0, 0))
    os.makedirs(COMP, exist_ok=True)
    ruta = os.path.join(COMP, clave[1] + '.png')
    lienzo.quantize(colors=256, method=Image.MEDIANCUT).save(ruta, optimize=True)
    return ruta, ANCHO, round(H / ESCALA)


def lineas(t):
    return sum(max(1, math.ceil(len(p) / CHARS_LINEA)) for p in t.split('\n'))


PEND = []


def poner(ws, ref, d, carpeta, altos):
    c = ws[ref]
    clave = d.get('_leccion')
    if not clave or ref[1:] == '1':
        return MR._poner_v1(ws, ref, d, carpeta, altos)
    escenas = MAPA.get(clave, {}).get(int(ref[1:]))
    if not escenas:
        return MR._poner_v1(ws, ref, d, carpeta, altos)
    tit = ' + '.join(ESC[clave][n - 1]['titulo'] for n in escenas)
    c.value = CellRichText(TextBlock(F_COM, d['t']), TextBlock(F_PROP, '\nPropuesta: '), TextBlock(F_TIT, tit))
    c.font = copy(MR.FUENTE)
    c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='left')
    boceto = os.path.join(carpeta, d['mini'] + '.png') if d.get('mini') else None
    png, w, h = compuesto((clave, 'V2_%s_%s' % (ws.title.split()[1], ref)), escenas, boceto)
    alto = (lineas(d['t'] + '\nPropuesta: ' + tit) + 1) * PT_LINEA + 6 + h * 0.75 + 12
    altos[c.row] = max(altos.get(c.row, 91.5), alto)
    PEND.append((ws.title, c.row, c.column, png, w, h))
    return None


def anclar(ws, pendientes, altos):
    MR._anclar_v1(ws, pendientes, altos)
    for hoja, fila, col, png, w, h in [p for p in PEND if p[0] == ws.title]:
        im = XLImage(png)
        im.width, im.height = w, h
        off = int(altos[fila] * 4 / 3) - h - 8
        im.anchor = OneCellAnchor(_from=AnchorMarker(col=col - 1, colOff=pixels_to_EMU(8), row=fila - 1,
                                                     rowOff=pixels_to_EMU(off)),
                                  ext=XDRPositiveSize2D(pixels_to_EMU(w), pixels_to_EMU(h)))
        ws.add_image(im)
    for fila, hh in altos.items():
        ws.row_dimensions[fila].height = hh
    if os.environ.get('VERIFICAR'):   # copia de control: todo el ancho en una página, para revisarla en PDF
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth, ws.page_setup.fitToHeight, ws.page_setup.orientation = 1, 0, 'landscape'


def main():
    mapa, rj, carpeta, salida = sys.argv[1:5]
    rev = json.load(open(rj, encoding='utf-8'))
    for h in rev['hojas']:
        u = int(h['hoja'].split()[-1])
        for ref, d in h['celdas'].items():
            d['_leccion'] = '%d.%d' % (u, COL[ref[0]])
    tmp = salida + '.rev.json'
    json.dump(rev, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False)
    MR._poner_v1, MR._anclar_v1 = MR.poner, MR.anclar
    MR.poner, MR.anclar = poner, anclar
    sys.argv = [sys.argv[0], mapa, tmp, carpeta, salida]
    MR.main()
    os.remove(tmp)
    print('celdas con propuesta:', len(PEND))


if __name__ == '__main__':
    main()
