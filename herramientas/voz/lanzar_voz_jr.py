# -*- coding: utf-8 -*-
r"""Pide las voces de las seis piezas de Justicia restaurativa.

Es `lanzar_voz_gj` apuntado a otro arbol: las dos voces de la serie, mismo
modelo, mismos ajustes (los de `elevenlabs.py`), MAS una tercera para los
parlamentos de Juana en las unidades 2 a 4. Un curso nuevo con otro
narrador se oiria como otra serie; un personaje con la voz del narrador que
lo describe no se distingue de el.

    Carlos        Y4HwpMNrBWN5dFKi5Lw8   colombian male middle_aged narrative
    Pilar         x6LHvMgpXmty838MUqHh   colombian female middle_aged narrative
    Juana         Pzocg9GZr24gNfKRHiyy   Elisa Maria, la de los casos del
                                         profe Carlos Humberto (CH U1)

A ElevenLabs va el `tts` -numeros en letras, siglas deletreadas-; el
verbatim se queda para el carton. Los .txt van a `03 VOCES/textos_tts/<voz>`
y los mp3 a `03 VOCES/crudo`, con el mismo nombre.

La llave sale de D:\DAE\_secretos\elevenlabs.txt, fuera del repositorio, y
nunca se imprime.

    python lanzar_voz_jr.py              las seis
    python lanzar_voz_jr.py U3           solo esa
    python lanzar_voz_jr.py U3 --solo b03_el_perdon   un bloque (toma nueva;
                                         la anterior va a _descartes)
"""
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_jr import VIDEOS, bloques            # noqa: E402
import rutas_jr as R                            # noqa: E402

ELEVEN = r'D:\DAE\_repo\herramientas\voz\elevenlabs.py'
VOZ = {'Carlos': 'Y4HwpMNrBWN5dFKi5Lw8', 'Pilar': 'x6LHvMgpXmty838MUqHh',
       'Juana': 'Pzocg9GZr24gNfKRHiyy'}


def nombre(clave, i, nom):
    return 'JR_%s_%02d_%s' % (clave, i, nom)


def escribir(clave, solo=None):
    tx = os.path.join(R.voces(clave), 'textos_tts')
    crudo = os.path.join(R.voces(clave), 'crudo')
    for v in VOZ:
        d = os.path.join(tx, v.lower())
        os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):          # un lote limpio por voz
            if f.endswith('.txt'):
                os.remove(os.path.join(d, f))
    os.makedirs(crudo, exist_ok=True)
    n = 0
    for i, (nom, v, _texto, tts, _p) in enumerate(bloques(clave), 1):
        if solo and nom not in solo:
            continue
        nm = nombre(clave, i, nom)
        mp3 = os.path.join(crudo, nm + '.mp3')
        if os.path.exists(mp3):
            if not solo:
                continue                 # ya existe: no se vuelve a pedir
            d = os.path.join(crudo, '_descartes')
            os.makedirs(d, exist_ok=True)
            shutil.move(mp3, os.path.join(d, '%s__toma_%s.mp3'
                                          % (nm, time.strftime('%H%M%S'))))
        p = os.path.join(tx, v.lower(), nm + '.txt')
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(tts)
        n += 1
    return n


def pedir(clave):
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    tx = os.path.join(R.voces(clave), 'textos_tts')
    crudo = os.path.join(R.voces(clave), 'crudo')
    for v, vid in VOZ.items():
        carpeta = os.path.join(tx, v.lower())
        if not [f for f in os.listdir(carpeta) if f.endswith('.txt')]:
            continue
        print('=== %s · %s' % (clave, v), flush=True)
        q = subprocess.run([sys.executable, ELEVEN, 'lote', carpeta, vid, crudo],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=env)
        s = (q.stdout or '') + (q.stderr or '')
        print(s.encode('ascii', 'replace').decode()[-1500:], flush=True)


if __name__ == '__main__':
    args = sys.argv[1:]
    solo = None
    if '--solo' in args:
        k = args.index('--solo')
        solo = set(args[k + 1:])
        args = args[:k]
    claves = [x.upper() for x in args] or VIDEOS
    for c in claves:
        print('%d textos escritos para %s' % (escribir(c, solo), c), flush=True)
    for c in claves:
        pedir(c)
    print('', flush=True)
    for c in claves:
        crudo = os.path.join(R.voces(c), 'crudo')
        fs = sorted(f for f in os.listdir(crudo) if f.endswith('.mp3'))
        falta = len(bloques(c)) - len(fs)
        print('%s: %d/%d mp3 %s' % (c, len(fs), len(bloques(c)),
                                     'OK' if falta == 0 else ('FALTAN %d' % falta)),
              flush=True)
    print('LISTO', flush=True)
