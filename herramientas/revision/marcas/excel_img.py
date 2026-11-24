# -*- coding: utf-8 -*-
"""Excel «REVISION COMENTARIOS - <CURSO>» con el pantallazo marcado dentro de cada celda.

Sebastián (24 nov): «en cada celda iban los screenshots intervenidos tipo paint», y «estás contrastando tres
elementos: diseño instruccional, mapa de curso y Genially como nos lo enviaron».

Hojas «Unidad N - revisión»: fila 1 = lecciones; columna A = número de diapositiva del Genially (el mismo del
archivo del pantallazo). En cada celda, de arriba abajo:
  · en gris, qué pide el mapa para esa diapositiva (o que no está en el mapa);
  · el comentario, una frase (contraste con el DI y el mapa);
  · el pantallazo de la diapositiva tal como está en el Genially enviado, con las marcas a mano.
«Generales - revisión» al final. Texto en sharedStrings (LibreOffice y Sheets leen así la negrita y el color).

python3 excel_img.py DP <mapa.xlsx> <salida.xlsx>
"""
import glob, io, json, math, os, re, sys, unicodedata
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
sys.path.insert(0, '/home/claude/repo/herramientas/revision')
import aplicar, marcas
from mapa_revision import a_compartidas

AQUI = os.path.dirname(os.path.abspath(__file__))
IMG_W, IMG_H = 600, 338          # px del pantallazo en la celda
ANCHO_COL = 92                   # caracteres: ~650 px
CHARS = 38                       # Arial 20 en ese ancho (conservador)
CHARS_MAPA = 72                  # Arial 13
PT20, PT13 = 26.5, 17.5
MAX_PT = 409
F_COM = InlineFont(rFont='Arial', sz=20, color='FF222222')
F_BIEN = InlineFont(rFont='Arial', sz=20, color='FF7F8C8A')
F_MAPA = InlineFont(rFont='Arial', sz=13, i=True, color='FF5B6B73')
F_TIT = Font(name='Arial', size=16, bold=True, color='FF002F46')
FONDO_TIT = PatternFill('solid', fgColor='FFF2CC')
FINO = Side(style='thin', color='FF999999')
BORDE = Border(left=FINO, right=FINO, top=FINO, bottom=FINO)
CLAVES = ('mapa conceptual', 'grid', 'scroll', 'audio', 'tabla', 'línea de tiempo', 'linea de tiempo', 'pop',
          'pestaña', 'botones', 'botón', 'escenario', 'lista', 'html', 'tarjeta', 'imágenes', 'imagenes', 'persona',
          'cajas', 'ruta', 'texto plano', 'descarga', 'giran', 'ilustr', 'despliega', 'flip')


SINON = {'aplicacion': 'analisis', 'onjetivo': 'objetivo'}


def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'^\s*[\d\.]+\s*', '', s)
    return set(SINON.get(w, w) for w in re.findall(r'[a-z]{3,}', s)
               if w not in ('del', 'las', 'los', 'para', 'con', 'que', 'por', 'una', 'nueva'))


def recurso(texto):
    """Lo que el mapa pide como recurso para la fila (párrafos en mayúsculas o con palabras de recurso)."""
    pars = [p.strip() for p in re.split(r'\n+', texto or '') if p.strip()][1:]
    out = []
    for p in pars:
        letras = [c for c in p if c.isalpha()]
        mayus = letras and sum(c.isupper() for c in letras) / len(letras) > 0.6
        if mayus or any(k in p.lower() for k in CLAVES):
            p = re.sub(r'\b[A-ZÁÉÍÓÚÑ]{2,}(?:\s+[A-ZÁÉÍÓÚÑ]{2,})*\b', lambda m: m.group(0).lower(), p)
            out.append(p.rstrip('. '))
    r = '; '.join(out)
    r = r[:1].upper() + r[1:]
    r = re.sub(r'\bhtml\b', 'HTML', r, flags=re.I)
    if not r:
        t = re.sub(r'^\s*[\d\.]+\s*', '', (texto or '').strip().split('\n')[0]).replace('Onjetivo', 'Objetivo')
        r = '«%s», sin recurso indicado' % t.rstrip('. ')[:70]
    if len(r) > 110:
        r = r[:110].rsplit(' ', 1)[0] + '…'
    return r


# Revisado a mano donde los títulos no alcanzan (lección, página del Genially) -> fila del mapa o None (no está)
OVR = {('U4 L4', 8): None, ('U4 L4', 12): 9, ('U4 L4', 14): 10, ('U4 L4', 16): 12, ('U3 L4', 14): 12,
       ('U1 L4', 5): 3, ('U2 L4', 5): 3}


def mapa_por_pagina(mapa, cur):
    """{lección: {página: (fila del mapa, recurso) | None}} por parecido entre el título de la fila del mapa y el
    rótulo de la diapositiva en el Genially."""
    wb = openpyxl.load_workbook(mapa)
    out = {}
    for f in sorted(glob.glob(os.path.join(AQUI, 'cap', cur, '*', '*.json'))):
        lec = os.path.basename(os.path.dirname(f))
        js = json.load(open(f, encoding='utf-8'))
        p, _tot, nombre = js['pagina']
        u, l = int(lec[1]), int(lec[4])
        if not re.search(r'-E\d\d$', nombre):
            out.setdefault(lec, {})[p] = None
            continue
        tex, _, _ = marcas.cajas(js)
        rot = ' '.join(t['t'] for t in tex if not t['marco'] and 108 < t['b'][1] < 165 and 90 < t['b'][0] < 140)
        ws = wb['Unidad %d' % u]
        col = l + 1
        mejor, puntos = None, 0
        a = norm(rot)
        for r in range(2, ws.max_row + 1):
            v = ws.cell(r, col).value
            if not v or not str(v).strip():
                continue
            b = norm(str(v).strip().split('\n')[0].replace('Onjetivo', 'Objetivo'))
            if not a or not b:
                continue
            s = len(a & b) / min(len(a), len(b))
            if len(a & b) < 2 and min(len(a), len(b)) > 1:
                s = min(s, 0.4)
            if s > puntos:
                mejor, puntos = (r, recurso(str(v))), s
        out.setdefault(lec, {})[p] = ('mapa', mejor) if puntos >= 0.6 else ('fuera', rot)
        if (lec, p) in OVR:
            r = OVR[(lec, p)]
            out[lec][p] = ('mapa', (r, recurso(str(ws.cell(r, col).value)))) if r else ('fuera', rot)
    return out


def png_celda(src):
    im = Image.open(src).convert('RGB').resize((IMG_W * 2, IMG_H * 2), Image.LANCZOS)
    im = im.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE)
    b = io.BytesIO()
    im.save(b, 'PNG', optimize=True)
    b.seek(0)
    return b


def titulo_leccion(cur, lec):
    for f in sorted(glob.glob(os.path.join(AQUI, 'cap', cur, lec, '*.json')))[3:]:
        js = json.load(open(f, encoding='utf-8'))
        for t in js['frames'][0].get('t', []):
            if t['y'] < 100 and t['x'] > 450 and len(t['t']) > 12 and not t['t'].startswith('Page'):
                return t['t']
    return ''


def main():
    cur, mapa, salida = sys.argv[1], sys.argv[2], sys.argv[3]
    S = aplicar.specs(cur)
    M = mapa_por_pagina(mapa, cur) if mapa != '-' else {}
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    sin_mapa = []
    for u in sorted({int(l[1]) for l in S}):
        ws = wb.create_sheet('Unidad %d - revisión' % u)
        ws.sheet_properties.tabColor = 'EE616B'
        lecs = sorted([l for l in S if l.startswith('U%d ' % u)], key=lambda l: int(l[4]))
        ws.column_dimensions['A'].width = 14
        c = ws.cell(1, 1, 'Diapositiva del Genially')
        c.font, c.border, c.fill = F_TIT, BORDE, FONDO_TIT
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        alto1 = 40
        for j, lec in enumerate(lecs):
            col = j + 2
            ws.column_dimensions[get_column_letter(col)].width = ANCHO_COL
            tit = 'Lección %d.%d · %s' % (u, int(lec[4]), titulo_leccion(cur, lec))
            c = ws.cell(1, col, tit)
            c.font, c.border, c.fill = F_TIT, BORDE, FONDO_TIT
            c.alignment = Alignment(wrap_text=True, vertical='center')
            alto1 = max(alto1, math.ceil(len(tit) / 60) * 21 + 12)
        ws.row_dimensions[1].height = alto1
        for n in range(1, max(max(S[l]) for l in lecs) + 1):
            fila = n + 1
            c = ws.cell(fila, 1, n)
            c.font, c.border = Font(name='Arial', size=16, bold=True, color='FF002F46'), BORDE
            c.alignment = Alignment(horizontal='center', vertical='top')
            alto = 30
            for j, lec in enumerate(lecs):
                col = j + 2
                c = ws.cell(fila, col)
                c.border = BORDE
                if n not in S[lec]:
                    continue
                com, mk = S[lec][n]
                m = M.get(lec, {}).get(n)
                if m is None:
                    gris = ''
                elif m[0] == 'mapa':
                    gris = 'Mapa: ' + (m[1][1] or 'texto de la fila %d' % m[1][0])
                else:
                    gris = 'Esta diapositiva no está en el mapa.'
                    sin_mapa.append('%s %02d %s' % (lec, n, m[1][:50]))
                partes = []
                if gris:
                    partes.append(TextBlock(F_MAPA, gris + '\n'))
                partes.append(TextBlock(F_BIEN if com.startswith('Bien así') and not mk else F_COM, com))
                c.value = CellRichText(partes)
                c.alignment = Alignment(wrap_text=True, vertical='top')
                h_txt = (math.ceil(len(gris) / CHARS_MAPA) * PT13 if gris else 0) + math.ceil(len(com) / CHARS) * PT20 + 10
                png = os.path.join(AQUI, 'marcados', cur, lec, '%s - %02d.png' % (lec, n))
                im = XLImage(png_celda(png))
                im.width, im.height = IMG_W, IMG_H
                off = int(h_txt * 4 / 3) + 6
                im.anchor = OneCellAnchor(_from=AnchorMarker(col=col - 1, colOff=pixels_to_EMU(8), row=fila - 1,
                                                             rowOff=pixels_to_EMU(off)),
                                          ext=XDRPositiveSize2D(pixels_to_EMU(IMG_W), pixels_to_EMU(IMG_H)))
                ws.add_image(im)
                alto = max(alto, h_txt + IMG_H * 0.75 + 14)
            if alto > MAX_PT:
                print('ALTO', u, n, round(alto))
            ws.row_dimensions[fila].height = min(MAX_PT, alto)
        ws.freeze_panes = 'B2'
    ws = wb.create_sheet('Generales - revisión')
    ws.sheet_properties.tabColor = 'EE616B'
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 150
    c = ws.cell(1, 2, 'Generales: lo que se repite en todo el curso')
    c.font, c.fill, c.border = F_TIT, FONDO_TIT, BORDE
    ws.cell(1, 1).fill, ws.cell(1, 1).border = FONDO_TIT, BORDE
    ws.row_dimensions[1].height = 30
    for i, g in enumerate(json.load(open(os.path.join(AQUI, 'generales_%s.json' % cur.lower()), encoding='utf-8'))):
        a = ws.cell(i + 2, 1, i + 1)
        a.font, a.border = Font(name='Arial', size=16, bold=True), BORDE
        a.alignment = Alignment(horizontal='center', vertical='top')
        b = ws.cell(i + 2, 2, g)
        b.font, b.border = Font(name='Arial', size=20, color='FF222222'), BORDE
        b.alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[i + 2].height = min(MAX_PT, math.ceil(len(g) / 95) * PT20 + 10)
    wb.active = 0
    wb.save(salida)
    a_compartidas(salida)
    print('ok', salida, os.path.getsize(salida) // 1024, 'KB')
    print('fuera del mapa:', len(sin_mapa))
    for s in sin_mapa:
        print('  ', s)


if __name__ == '__main__':
    main()
