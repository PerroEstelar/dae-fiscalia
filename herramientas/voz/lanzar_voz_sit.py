# -*- coding: utf-8 -*-
r"""Pide las voces de las situaciones en video (A a E).

Es `lanzar_voz_df` apuntado a otra carpeta: mismas dos voces, mismo modelo,
mismos ajustes. Un caso del mismo curso con otro locutor se oye como otra
serie.

    Carlos   Y4HwpMNrBWN5dFKi5Lw8   colombian male middle_aged narrative
    Pilar    x6LHvMgpXmty838MUqHh   colombian female middle_aged narrative

A ElevenLabs va el `tts` -numeros en letras, siglas deletreadas-; el
verbatim se queda para el carton. Los .txt van a `textos_tts` para que nadie
los confunda con la fuente.

La llave sale de D:\DAE\_secretos\elevenlabs.txt, fuera del repositorio, y
nunca se imprime.

    python lanzar_voz_sit.py            todas las de video
    python lanzar_voz_sit.py A C        solo esas
"""
import os
import subprocess
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_sit import VIDEOS, bloques          # noqa: E402
import rutas_sit as R                          # noqa: E402

ELEVEN = r'D:\DAE\_repo\herramientas\voz\elevenlabs.py'
VOZ = {'Carlos': 'Y4HwpMNrBWN5dFKi5Lw8', 'Pilar': 'x6LHvMgpXmty838MUqHh'}


def escribir(letra):
    tx = os.path.join(R.voces(letra), 'textos_tts')
    for v in VOZ:
        os.makedirs(os.path.join(tx, v.lower()), exist_ok=True)
    os.makedirs(os.path.join(R.voces(letra), 'crudo'), exist_ok=True)
    n = 0
    for i, (nom, v, _texto, tts, _p) in enumerate(bloques(letra), 1):
        p = os.path.join(tx, v.lower(), 'SIT_%s_%02d_%s.txt' % (letra, i, nom))
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(tts)
        n += 1
    return n


def pedir(letra):
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    tx = os.path.join(R.voces(letra), 'textos_tts')
    crudo = os.path.join(R.voces(letra), 'crudo')
    for v, vid in VOZ.items():
        carpeta = os.path.join(tx, v.lower())
        if not os.listdir(carpeta):
            continue
        print('=== situacion %s · %s' % (letra, v), flush=True)
        q = subprocess.run([sys.executable, ELEVEN, 'lote', carpeta, vid, crudo],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=env)
        s = (q.stdout or '') + (q.stderr or '')
        print(s.encode('ascii', 'replace').decode(), flush=True)


if __name__ == '__main__':
    letras = [x.upper() for x in sys.argv[1:]] or VIDEOS
    for L in letras:
        print('%d textos escritos para la situacion %s' % (escribir(L), L),
              flush=True)
    for L in letras:
        pedir(L)
    print('', flush=True)
    for L in letras:
        crudo = os.path.join(R.voces(L), 'crudo')
        fs = sorted(f for f in os.listdir(crudo) if f.endswith('.mp3'))
        falta = len(bloques(L)) - len(fs)
        print('situacion %s: %d/%d mp3 %s'
              % (L, len(fs), len(bloques(L)),
                 'OK' if falta == 0 else ('FALTAN %d' % falta)), flush=True)
    print('LISTO', flush=True)
