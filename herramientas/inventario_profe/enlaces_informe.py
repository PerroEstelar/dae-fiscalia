# -*- coding: utf-8 -*-
"""Enlaces a carpetas de Drive en el informe (pestaña Resumen de «Inventario_videos_17 NOV»), 19 nov 2026."""
import json
SID = 927548570
F = 'https://drive.google.com/drive/folders/%s'
AZUL = {'red': 0.06666667, 'green': 0.33333334, 'blue': 0.8}
C = {
    'SRPA': '1zfEPFp1HdoaK3f0JUCEZJAdKgsV8dcsD',
    'TA': '1H2oIsmE55wwaNYyynoZrmhJK9WXN4k_V',
    'BI': '12Wwl_Vq9CCJVTPN7Y7g7JH0j3b9cDiAT',
    'JR': '11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o',
    'DH': '1Oa_NdV5Uwl6IgMccYY-BO38RofKr7iAk',
    'DH_P': '1O1O4kbtNFGO4N7vtb-Ydph5K4PUZ3EQ1',
    'ED': '1qKmKVuwmNGKaTLbzgtm2pc5-uqf98k9u',
    'ED_P': '1LNFO7X0A15EnIifpRpEycKcGW1LIqYLA',
    'TR': '1A3rlk8CCzw0cRq2sFEAZ_H6plaFMkq_l',
}
HOJA = 'https://docs.google.com/spreadsheets/d/13wsiWOYCbAxg4IPKHJq4r63uCkDWWaub1YKMP4h_xxM/edit'


def enl(uri):
    return {'link': {'uri': uri}, 'foregroundColorStyle': {'rgbColor': AZUL}, 'underline': True}


def celda_multi(prefijo, partes, sep=' · '):
    """Una celda con varios enlaces: (etiqueta, uri) por parte."""
    txt = prefijo
    runs = []
    for i, (et, uri) in enumerate(partes):
        if i:
            txt += sep
        a = len(txt.encode('utf-16-le')) // 2
        txt += et
        b = len(txt.encode('utf-16-le')) // 2
        runs.append({'startIndex': a, 'format': enl(uri)})
        runs.append({'startIndex': b, 'format': {}})
    if runs and runs[-1]['startIndex'] >= len(txt.encode('utf-16-le')) // 2:
        runs.pop()                       # un tramo no puede empezar en el final del texto
    return {'userEnteredValue': {'stringValue': txt}, 'textFormatRuns': runs,
            'userEnteredFormat': {'textFormat': {'fontFamily': 'Calibri', 'fontSize': 11, 'bold': False},
                                  'verticalAlignment': 'TOP', 'wrapStrategy': 'OVERFLOW_CELL'}}


E7 = celda_multi('Carpetas en Drive: ', [('SRPA', F % C['SRPA']), ('Terminaciones anticipadas', F % C['TA']),
                                        ('Bienes en el proceso penal', F % C['BI']), ('Enfoque diferencial', F % C['ED_P'])])
E8 = celda_multi('Carpeta en Drive: ', [('Tráfico de migrantes y trata de personas › VIDEOS › VIDEOS FINALIZADOS', F % C['TR'])])
E9 = celda_multi('Carpetas en Drive: ', [('Justicia restaurativa', F % C['JR']), ('Terminaciones anticipadas', F % C['TA']), ('SRPA', F % C['SRPA']),
                                        ('Bienes en el proceso penal', F % C['BI']), ('Derechos humanos', F % C['DH']),
                                        ('Enfoque diferencial', F % C['ED']), ('Inventario de videos de profe (cada video y su .srt)', HOJA)])


def fila_lista(curso, etiqueta, uri):
    return {'values': [{'userEnteredValue': {'stringValue': curso}},
                       {'userEnteredValue': {'stringValue': etiqueta},
                        'userEnteredFormat': {'textFormat': {'foregroundColorStyle': {'rgbColor': AZUL}, 'link': {'uri': uri}}}}]}


LISTA = [
    ('Bienes en el proceso penal', 'VIDEOS (inicio y cierre del curso y de las unidades)', F % C['BI']),
    ('Justicia restaurativa en la práctica del fiscal', 'VIDEOS › VIDEOS FINALIZADOS', F % C['JR']),
    ('Derechos humanos aplicados a la función judicial', 'Videos (casos)', F % C['DH']),
    ('Derechos humanos aplicados a la función judicial', 'Videos › VIDEOS PROFE - Yefri Yoel Torrado Verjel', F % C['DH_P']),
    ('Enfoques diferenciales', 'VIDEOS (casos)', F % C['ED']),
    ('Enfoques diferenciales', 'VIDEOS › VIDEOS PROFE - Camilo Borrero García', F % C['ED_P']),
    ('Tráfico de migrantes y trata de personas', 'VIDEOS › VIDEOS FINALIZADOS', F % C['TR']),
    ('Todos los cursos', 'Inventario de videos de profe: enlace a cada video, a su .srt y a su carpeta', HOJA),
]
reqs = [
    {'updateCells': {'start': {'sheetId': SID, 'rowIndex': 6, 'columnIndex': 4},
                     'rows': [{'values': [E7]}, {'values': [E8]}, {'values': [E9]}],
                     'fields': 'userEnteredValue,textFormatRuns,userEnteredFormat.textFormat,userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy'}},
    # La fila 22 («Terminaciones anticipadas · VIDEOS … de JP») no tiene enlace y se dejó así: no se pudo
    # confirmar cuál es esa carpeta (en 1lmPOsRfGzN6FbMGtNy6u6bPTNptlN7uW no están las grabaciones de unidad).
    {'updateCells': {'start': {'sheetId': SID, 'rowIndex': 23, 'columnIndex': 0},
                     'rows': [fila_lista(*x) for x in LISTA],
                     'fields': 'userEnteredValue,userEnteredFormat.textFormat.foregroundColorStyle,userEnteredFormat.textFormat.link'}},
]
json.dump(reqs, open('reqs.json', 'w', encoding='utf-8'), ensure_ascii=False)
for nombre, c in (('E7', E7), ('E8', E8), ('E9', E9)):
    t = c['userEnteredValue']['stringValue']; r = c['textFormatRuns']
    print(nombre, repr(t))
    for i in range(0, len(r) - 1, 2):
        print('    ', repr(t[r[i]['startIndex']:r[i + 1]['startIndex']]), '->', r[i]['format']['link']['uri'][-34:])
    if len(r) % 2: print('    ', repr(t[r[-1]['startIndex']:]), '->', r[-1]['format']['link']['uri'][-34:])
print(json.dumps(reqs, ensure_ascii=False))
