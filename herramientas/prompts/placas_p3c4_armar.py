# -*- coding: utf-8 -*-
"""Arma el prompt final de cada placa y lo deja en un json. Lo armado es lo
que se manda y es lo que se guarda: no hay borrador aparte."""
import json
import sys

sys.path.insert(0, '.')
from base import arma, TOKENS
from escenas import E

out = {}
for nom, (ranura, cuadros, rostro, acento, que, escena) in E.items():
    out[nom] = {
        'ranura': 'r%02d' % ranura,
        'cuadros': cuadros,
        'que': que,
        'rostro': rostro,
        'acento': acento,
        'prompt': arma(escena % TOKENS if '%(' in escena else escena,
                       con_rostro=rostro, con_acento=acento),
    }

if __name__ == '__main__':
    json.dump(out, open('prompts_p3c4.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('%-32s %-5s %5s %6s %6s %s' % ('placa', 'ran', 'cuad', 'rostro', 'acento', 'car'))
    for n, v in sorted(out.items(), key=lambda x: int(x[1]['ranura'][1:])):
        print('%-32s %-5s %5d %6s %6s %5d'
              % (n, v['ranura'], v['cuadros'], 'si' if v['rostro'] else '-',
                 'si' if v['acento'] else '-', len(v['prompt'])))
    print('\n%d placas · %d cuadros' % (len(out), sum(v['cuadros'] for v in out.values())))
