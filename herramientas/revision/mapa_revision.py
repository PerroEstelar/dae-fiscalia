# -*- coding: utf-8 -*-
"""Arma la copia del mapa de virtualización con la hoja de revisión (flujo «revisión»).

    python3 mapa_revision.py <mapa.xlsx> <comentarios.json> <carpeta_png> <salida.xlsx>

- Copia la hoja indicada en el json («Unidad 1») como «<hoja> - revisión», justo al lado y con pestaña coral.
  La original no se toca. La copia conserva encabezados (fila 1) y la columna A (# diapositiva); se vacían
  las celdas de contenido B2:E<última> y en su lugar va el comentario (texto enriquecido) con la miniatura
  anclada dentro de la misma celda, debajo del texto.
- Las filas extra (Generales, Convenciones) van debajo de la grilla, sin mover filas ni columnas existentes.
- Se ensancha la columna revisada y se agrandan las filas para que quepan texto y miniatura.
"""
import json
import math
import os
import sys
from copy import copy

import openpyxl
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.drawing.image import Image as XLImage
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, OneCellAnchor
from openpyxl.drawing.xdr import XDRPositiveSize2D
from openpyxl.styles import Alignment, Font
from openpyxl.utils import column_index_from_string, get_column_letter
from openpyxl.utils.units import pixels_to_EMU

MARINO, TEAL, OXIDO = 'FF002F46', 'FF396B83', 'FFA75260'
ANCHO_COL = 54            # caracteres
MINI_W, MINI_H = 360, 153  # px (proporción 400×170)
CHARS_LINEA = 56          # estimado conservador para Arial 9 en ese ancho (LibreOffice/Excel)
PT_LINEA = 12.5


def color_tag(t):
    t = t.upper()
    if t.startswith('BIEN'):
        return TEAL
    if t.startswith('OJO') or t.startswith('ERROR'):
        return OXIDO
    return MARINO


def rico(lineas):
    partes, n = [], 0
    for i, (tag, txt) in enumerate(lineas):
        sep = '' if i == 0 else '\n'
        if i == 0 and not tag:
            partes.append(TextBlock(InlineFont(rFont='Arial', sz=10, b=True, color=MARINO), txt))
            n += 1
            continue
        if tag:
            partes.append(TextBlock(InlineFont(rFont='Arial', sz=9, b=True, color=color_tag(tag)), sep + tag + ': '))
            partes.append(TextBlock(InlineFont(rFont='Arial', sz=9, color='FF222222'), txt))
        else:
            partes.append(TextBlock(InlineFont(rFont='Arial', sz=9, color='FF222222'), sep + txt))
        n += max(1, math.ceil((len(tag) + 2 + len(txt)) / CHARS_LINEA))
    return CellRichText(*partes), n


def a_compartidas(ruta):
    """Este openpyxl guarda todo el texto como inlineStr, y LibreOffice ignora el formato (negrita, color) del
    texto enriquecido inline. Se pasa todo a xl/sharedStrings.xml, que leen bien Excel, Sheets y LibreOffice."""
    import re
    import shutil
    import zipfile
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
    ct = salida['[Content_Types].xml'].decode('utf-8')
    ct = ct.replace('</Types>', '<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.'
                    'openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/></Types>')
    salida['[Content_Types].xml'] = ct.encode('utf-8')
    rl = salida['xl/_rels/workbook.xml.rels'].decode('utf-8')
    rl = rl.replace('</Relationships>', '<Relationship Id="rIdSST" Type="http://schemas.openxmlformats.org/'
                    'officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"/></Relationships>')
    salida['xl/_rels/workbook.xml.rels'] = rl.encode('utf-8')
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for n in [i.filename for i in zin.infolist()] + ['xl/sharedStrings.xml']:
            zout.writestr(n, salida[n])
    zin.close()
    shutil.move(tmp, ruta)
    print('textos a sharedStrings:', len(sis))


def main():
    mapa, cj, carpeta, salida = sys.argv[1:5]
    com = json.load(open(cj, encoding='utf-8'))
    wb = openpyxl.load_workbook(mapa)
    base = wb[com['hoja']]
    ws = wb.copy_worksheet(base)
    ws.title = (com['hoja'] + ' - revisión')[:31]
    wb.move_sheet(ws, offset=wb.sheetnames.index(com['hoja']) + 1 - wb.sheetnames.index(ws.title))
    ws.sheet_properties.tabColor = 'EE616B'
    ultima = base.max_row
    for fila in ws.iter_rows(min_row=2, max_row=ultima, min_col=2, max_col=base.max_column):
        for c in fila:
            c.value = None
    col = com['columna']
    ci = column_index_from_string(col)
    ws.column_dimensions[col].width = ANCHO_COL
    for ref, d in com['celdas'].items():
        c = ws[ref]
        r = c.row
        if r > ultima:  # filas nuevas bajo la grilla: copiar estilo de la última fila
            for k in range(1, base.max_column + 1):
                o, n = ws.cell(ultima, k), ws.cell(r, k)
                n.font, n.border, n.fill, n.alignment = copy(o.font), copy(o.border), copy(o.fill), copy(o.alignment)
            a = ws.cell(r, 1)
            a.value = d.get('rotulo', '')
            a.font = copy(ws['A1'].font)
        texto, n = rico(d['texto'])
        c.value = texto
        c.alignment = Alignment(wrap_text=True, vertical='top', horizontal='left')
        c.font = Font(name='Arial', size=9, color='FF222222')  # base, por si un visor ignora los formatos del texto
        alto_txt = (n + 1) * PT_LINEA + 6
        alto = max(alto_txt + (MINI_H * 0.75 + 12 if d.get('mini') else 4), 91.5)
        ws.row_dimensions[r].height = alto
        if d.get('mini'):
            png = os.path.join(carpeta, '%s%s.png' % (com.get('prefijo_png', ''), d['mini']))
            im = XLImage(png)
            im.width, im.height = MINI_W, MINI_H
            off = int(alto * 4 / 3) - MINI_H - 8   # pegada al fondo de la celda: si sobra alto, sobra arriba
            im.anchor = OneCellAnchor(_from=AnchorMarker(col=ci - 1, colOff=pixels_to_EMU(8), row=r - 1,
                                                         rowOff=pixels_to_EMU(off)),
                                      ext=XDRPositiveSize2D(pixels_to_EMU(MINI_W), pixels_to_EMU(MINI_H)))
            ws.add_image(im)
    wb.active = wb.sheetnames.index(ws.title)
    if not wb.views:
        from openpyxl.workbook.views import BookView
        wb.views.append(BookView())
    wb.views[0].activeTab = wb.sheetnames.index(ws.title)
    for h in wb.worksheets:
        h.sheet_view.tabSelected = h is ws
    wb.save(salida)
    a_compartidas(salida)
    print('hojas:', wb.sheetnames)
    print('filas:', {k: round(v.height, 1) for k, v in ws.row_dimensions.items() if v.height})


if __name__ == '__main__':
    main()
