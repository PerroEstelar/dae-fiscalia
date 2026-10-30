# -*- coding: utf-8 -*-
r"""Cruza la rejilla de cada pieza con los tiempos por palabra de Scribe.

Sale D:\DAE\_tmp\jr\cruce_jr.json = {clave: {'ranuras': <JR_<X>_ranuras.json>,
'words': [(t0, t1, palabra, bloque)], 'rejilla': <JR_<X>_rejilla.json>}}, en
segundos del master (el tiempo de cada toma corrido por el `entra` de su
bloque). Lo leen `recortar_jr.py` (cortes por palabra) y `prompts_jr.py` (que
se oye encima de cada ranura).

    python cruce_jr.py            las seis
    python cruce_jr.py U1 U3      algunas
"""
import json
import os
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_jr import VIDEOS, bloques            # noqa: E402
import rutas_jr as R                            # noqa: E402

FPS = 24000 / 1001.0
SALIDA = os.path.join(R.TMP, 'cruce_jr.json')


def cruce(clave):
    voces = R.voces(clave)
    rej = json.load(open(os.path.join(voces, 'JR_%s_rejilla.json' % clave), encoding='utf-8'))
    ran = json.load(open(os.path.join(voces, 'JR_%s_ranuras.json' % clave), encoding='utf-8'))
    entra = {t['bloque']: t['entra'] for t in rej['tramos']}
    words = []
    for i, (nom, _v, _t, _tts, _p) in enumerate(bloques(clave), 1):
        j = json.load(open(os.path.join(voces, 'stt', 'JR_%s_%02d_%s.json' % (clave, i, nom)),
                           encoding='utf-8'))
        off = entra[nom]
        for w in j.get('words', []):
            if w.get('type', 'word') != 'word':
                continue
            words.append((round(w['start'] + off, 3), round(w['end'] + off, 3),
                          w['text'], nom))
    return {'ranuras': ran, 'words': words, 'rejilla': rej}


if __name__ == '__main__':
    claves = [x.upper() for x in sys.argv[1:]] or VIDEOS
    out = json.load(open(SALIDA, encoding='utf-8')) if os.path.exists(SALIDA) else {}
    for c in claves:
        out[c] = cruce(c)
        d = out[c]
        for i, r in enumerate(d['ranuras']['ranuras'], 1):
            a, b = r['ini'] / FPS, (r['ini'] + r['dur']) / FPS
            txt = ' '.join(w[2] for w in d['words'] if a <= w[0] < b)
            print('%s r%02d %4d  %s' % (c, i, r['dur'], txt), flush=True)
    json.dump(out, open(SALIDA, 'w', encoding='utf-8'), ensure_ascii=False)
    print('LISTO', flush=True)
