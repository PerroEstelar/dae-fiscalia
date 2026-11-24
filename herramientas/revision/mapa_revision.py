# -*- coding: utf-8 -*-
"""Arma la copia del mapa de virtualización con las hojas de revisión (flujo «revisión»).

    python3 mapa_revision.py <mapa.xlsx> <revision.json> <carpeta_png> <salida.xlsx>

revision.json:
  {"hojas": [{"hoja": "Unidad 1", "celdas": {"B2": {"t": "una frase", "mini": "clave_png"?}, ...}}, ...],
   "generales": [{"t": "una frase", "mini": "clave_png"?}, ...]}

- Por cada hoja del json se duplica la original como «<hoja> - revisión» (pestaña coral, al lado de la
  original, que no se toca). Quedan la fila 1 (títulos de lección) y la columna A (# diapositiva); se vacían las
  celdas de contenido y en su lugar va **una sola frase** (propuesta y errores) con la miniatura debajo, pegada
  al fondo de la celda (si sobra alto, sobra aire; nunca tapa el texto).
- «Generales - revisión»: una fila por asunto que se repite en todo el curso.
- Las columnas de lección se ensanchan y las filas crecen para que quepan frase y miniatura.

Pedido de Sebastián (24 nov 2026): poco texto, una frase por celda; las miniaturas se quedan; letra más grande
(11, y después 14); y en las celdas sin diapositiva en el mapa, una nota que lo diga.
"""
import json
import math
import os
import re
import shutil
import sys
import zipfile
from copy import copy

import openpyxl
from openpyxl.drawing.image import Image as XLImage
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, OneCellAnchor
from openpyxl.drawing.xdr import XDRPositiveSize2D
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from openpyxl.utils.units import pixels_to_EMU

ANCHO_COL = 80             # caracteres
MINI_W, MINI_H = 420, 178  # px (proporción 400×170)
CHARS_LINEA = 38           # estimado conservador para Arial 16 en ese ancho
PT_LINEA = 21.5
# Sebastián: «la letra está muy chiquita» (9,5 → 11), «más grande la letra» (11 → 14) y «más grande el tamaño de la
# letra del texto de cada celda» (14 → 16), 24 nov. Los títulos de lección y el número de diapositiva van a 14.
FUENTE = Font(name='Arial', size=16, color='FF222222')
TITULO_PT = 14
FUENTE_VACIA = Font(name='Arial', size=13, italic=True, color='FF8A9BA3')


def a_compartidas(ruta):
    """Este openpyxl guarda el texto como inlineStr; se pasa a sharedStrings, que leen bien Excel, Sheets y
    LibreOffice (LibreOffice ignora el formato del texto inline)."""
    tmp = ruta + '.tmp'
    zin = zipfile.ZipFile(ruta)
    sis, salida = [], {}
    patron = re.compile(r'<c r="([A-Z]+[0-9]+)"((?: s="[0-9]+")?) t="inlineStr"><is>(.*?)</is></c>', re.S)
    for n in zin.namelist():
        d = zin.read(n)
        if n.startswith('xl/worksheets/sheet') and n.endswith('.xml'):
            def cambio(m):
                sis.append(m.group(3))
                return '<c r="%s"%s t="s"><v>%d</v></c>' % (m.group(1), m.group(2), len(sis) - 1)
            d = patron.sub(cambio, d.decode('utf-8')).encode('utf-8')
        salida[n] = d
    assert 'xl/sharedStrings.xml' not in salida
    salida['xl/sharedStrings.xml'] = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<sst xmlns='
                                      '"http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="%d" '
                                      'uniqueCount="%d">%s</sst>' % (len(sis), len(sis),
                                                                     ''.join('<si>%s</si>' % t for t in sis))
                                      ).encode('utf-8')
    ct = salida['[Content_Types].xml'].decode('utf-8').replace(
        '</Types>', '<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-'
        'officedocument.spreadsheetml.sharedStrings+xml"/></Types>')
    salida['[Content_Types].xml'] = ct.encode('utf-8')
    rl = salida['xl/_rels/workbook.xml.rels'].decode('utf-8').replace(
        '</Relationships>', '<Relationship Id="rIdSST" Type="http://schemas.openxmlformats.org/officeDocument/'
        '2006/relationships/sharedStrings" Target="sharedStrings.xml"/></Relationships>')
    salida['xl/_rels/workbook.xml.rels'] = rl.encode('utf-8')
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for n in [i.filename for i in zin.infolist()] + ['xl/sharedStrings.xml']:
            zout.writestr(n, salida[n])
    zin.close()
    shutil.move(tmp, ruta)


def alto_texto(t):
    return (math.ceil(len(t) / CHARS_LINEA) + 1) * PT_LINEA + 6


def poner(ws, ref, d, carpeta, altos):
    c = ws[ref]
    c.value = d['t']
    c.font = copy(FUENTE)
    c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='left')
    h = alto_texto(d['t']) + (MINI_H * 0.75 + 12 if d.get('mini') else 0)
    altos[c.row] = max(altos.get(c.row, 91.5), h)
    if d.get('mini'):
        return (c.row, c.column, os.path.join(carpeta, d['mini'] + '.png'))


def anclar(ws, pendientes, altos):
    for fila, col, png in pendientes:
        im = XLImage(png)
        im.width, im.height = MINI_W, MINI_H
        off = int(altos[fila] * 4 / 3) - MINI_H - 8
        im.anchor = OneCellAnchor(_from=AnchorMarker(col=col - 1, colOff=pixels_to_EMU(8), row=fila - 1,
                                                     rowOff=pixels_to_EMU(off)),
                                  ext=XDRPositiveSize2D(pixels_to_EMU(MINI_W), pixels_to_EMU(MINI_H)))
        ws.add_image(im)
    for fila, h in altos.items():
        ws.row_dimensions[fila].height = h


def main():
    mapa, rj, carpeta, salida = sys.argv[1:5]
    rev = json.load(open(rj, encoding='utf-8'))
    wb = openpyxl.load_workbook(mapa)
    primera = None
    for h in rev['hojas']:
        base = wb[h['hoja']]
        ws = wb.copy_worksheet(base)
        ws.title = (h['hoja'] + ' - revisión')[:31]
        wb.move_sheet(ws, offset=wb.sheetnames.index(h['hoja']) + 1 - wb.sheetnames.index(ws.title))
        ws.sheet_properties.tabColor = 'EE616B'
        primera = primera or ws
        for fila in ws.iter_rows(min_row=2, max_row=base.max_row, min_col=2, max_col=base.max_column):
            for c in fila:
                c.value = None
        # Las hojas traen anchos agrupados (p. ej. A:D en la Unidad 3): se parten en una entrada por columna
        # para poder ensanchar solo las de lección sin que el grupo las pise.
        anchos = {}
        for _k, v in list(ws.column_dimensions.items()):
            for i in range(v.min or 1, (v.max or v.min or 1) + 1):
                anchos[i] = v.width
        for i, wv in anchos.items():
            cd = ws.column_dimensions[get_column_letter(i)]
            cd.min, cd.max, cd.width = i, i, wv
        for i in range(2, base.max_column + 1):
            ws.column_dimensions[get_column_letter(i)].width = ANCHO_COL
        # Títulos de lección (fila 1) y número de diapositiva (columna A) al mismo tamaño que los comentarios
        alto1 = ws.row_dimensions[1].height or 15
        for i in range(1, base.max_column + 1):
            c = ws.cell(1, i)
            c.font = Font(name=c.font.name or 'Arial', size=TITULO_PT, bold=True, color=copy(c.font.color))
            c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
            if i > 1 and c.value:
                alto1 = max(alto1, math.ceil(len(str(c.value)) / 42) * 19 + 10)
        ws.row_dimensions[1].height = alto1
        for fila in range(2, base.max_row + 1):
            c = ws.cell(fila, 1)
            c.font = Font(name=c.font.name or 'Arial', size=TITULO_PT, bold=True, color=copy(c.font.color))
        altos, pend = {}, []
        for ref, d in h['celdas'].items():
            r = poner(ws, ref, d, carpeta, altos)
            if r:
                pend.append(r)
        if rev.get('vacias'):
            # Celdas de la grilla sin diapositiva en el mapa (esa lección tiene menos filas): se dice, para que no
            # parezca que falta la revisión. Solo en filas con alguna diapositiva.
            for fila in range(2, base.max_row + 1):
                cols = [get_column_letter(i) for i in range(2, base.max_column + 1)]
                if not any(base['%s%d' % (c, fila)].value not in (None, '') for c in cols):
                    continue
                for c in cols:
                    ref = '%s%d' % (c, fila)
                    if ref not in h['celdas']:
                        ws[ref].value = rev['vacias']
                        ws[ref].font = copy(FUENTE_VACIA)
                        ws[ref].alignment = Alignment(wrap_text=True, vertical='top', horizontal='left')
        anclar(ws, pend, altos)
    if rev.get('generales'):
        u1 = wb[rev['hojas'][0]['hoja']]
        fin = wb.sheetnames.index('Desplegables') if 'Desplegables' in wb.sheetnames else len(wb.sheetnames)
        ws = wb.create_sheet('Generales - revisión', index=fin)
        ws.sheet_properties.tabColor = 'EE616B'
        for k, v in (('A1', '#'), ('B1', 'Generales: lo que se repite en todo el curso')):
            ws[k].value = v
            o = u1['A1']
            ws[k].fill, ws[k].border = copy(o.fill), copy(o.border)
            ws[k].font = Font(name=o.font.name or 'Arial', size=TITULO_PT, bold=True, color=copy(o.font.color))
            ws[k].alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
        ws.column_dimensions['A'].width = 8
        ws.column_dimensions['B'].width = ANCHO_COL + 6
        ws.row_dimensions[1].height = 36
        altos, pend = {}, []
        borde = copy(u1['B2'].border)
        for i, d in enumerate(rev['generales']):
            fila = i + 2
            ws.cell(fila, 1, i + 1).alignment = Alignment(vertical='top', horizontal='center')
            ws.cell(fila, 1).font = Font(name='Arial', size=TITULO_PT, bold=True)
            ws.cell(fila, 1).border = copy(borde)
            ws.cell(fila, 2).border = copy(borde)
            r = poner(ws, 'B%d' % fila, d, carpeta, altos)
            if r:
                pend.append(r)
        anclar(ws, pend, altos)
    if rev.get('solo_revision'):
        # Sebastián (24 nov): «solo deja las hojas que sean de revisión en el Excel, quita las originales»
        for n in list(wb.sheetnames):
            if 'revisión' not in n:
                del wb[n]
    if not wb.views:
        from openpyxl.workbook.views import BookView
        wb.views.append(BookView())
    wb.active = wb.sheetnames.index(primera.title)
    wb.views[0].activeTab = wb.sheetnames.index(primera.title)
    for h in wb.worksheets:
        h.sheet_view.tabSelected = h is primera
    wb.save(salida)
    a_compartidas(salida)
    print('hojas:', wb.sheetnames)


if __name__ == '__main__':
    main()
