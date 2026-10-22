# -*- coding: utf-8 -*-
"""Arma el prompt final de cada placa del P3C5 y lo deja en un json.

Lo armado es lo que se manda y es lo que se guarda: no hay borrador aparte.
Es la leccion del Caso 3, donde seis prompts guardados en local no coincidian
con lo que de verdad habia salido por la API.
"""
import json
import sys

sys.path.insert(0, '.')
from placas_p3c5_base import arma, TOKENS
from placas_p3c5_escenas import E, CENITALES

MODELO = {'mode': 'seedream-5-pro', 'width': 2560, 'height': 1440,
          'resolution': '2k', 'creditos': 100}

out = {}
for nom, (ranura, cuadros, rostro, acento, que, escena) in E.items():
    out[nom] = {
        'ranura': 'r%02d' % ranura,
        'n': ranura,
        'cuadros': cuadros,
        'que': que,
        'rostro': bool(rostro),
        'acento': acento or '',
        'cenital': nom in CENITALES,
        'prompt': arma(escena % TOKENS if '%(' in escena else escena,
                       con_rostro=rostro, con_acento=acento,
                       cenital=nom in CENITALES),
    }

if __name__ == '__main__':
    json.dump({'modelo': MODELO, 'placas': out},
              open('prompts_p3c5.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('%-34s %-5s %5s %6s %6s %s' % ('placa', 'ran', 'cuad', 'rostro', 'acento', 'car'))
    for n, v in sorted(out.items(), key=lambda x: x[1]['n']):
        print('%-34s %-5s %5d %6s %6s %5d'
              % (n, v['ranura'], v['cuadros'], 'si' if v['rostro'] else '-',
                 v['acento'] or '-', len(v['prompt'])))
    print('\n%d placas · %d cuadros · %d creditos'
          % (len(out), sum(v['cuadros'] for v in out.values()),
             len(out) * MODELO['creditos']))
