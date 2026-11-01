# -*- coding: utf-8 -*-
r"""Pide las voces de los cinco videos de Derechos humanos.

Es `lanzar_voz_jr` con el reparto del curso: Carlos narra (la voz de la
serie) y cada personaje tiene la suya, mismo modelo y mismos ajustes (los
de `elevenlabs.py`). Las carpetas de textos van POR PERSONAJE, no por voz:
Sandra y la abogada Salgado comparten la de Milena y nunca hablan las dos
en el mismo video.

    Carlos         Y4HwpMNrBWN5dFKi5Lw8   narrador de la serie
    Carmen         Pzocg9GZr24gNfKRHiyy   Elisa Maria
    Andres         Ux2YbCNfurnKHnzlBHGX   Leo
    Entrevistador  4uvQjLPvqApx1dVzpNfM   Johan  (1 nov: se probo pasarlo voz a voz a
                                          Jerome y Sebastian lo rechazo: golpes de
                                          viento en el micro. Se queda Johan; en la
                                          U3 lleva +2 dB a 280 Hz y ~+1,5 dB de nivel.
                                          Realzar, no transformar)
    Sandra         oWSxI36XAKnfMWmzmQok   Milena
    Salgado        oWSxI36XAKnfMWmzmQok   Milena
    Quintero       x6LHvMgpXmty838MUqHh   Pilar
    Julian         Ol2UUwISo9ncUTR92kGn   Alejandro
    Juez           57D8YIbQSuE3REDPO6Vm   Horacio

Un bloque de voz SILENCIO no va a ElevenLabs: se escribe con ffmpeg un mp3
mudo de los segundos que dice su `tts` (U4 d29, «La otra silla»).

A ElevenLabs va el `tts` -numeros en letras, siglas leidas-; el verbatim
se queda para el carton. Los .txt van a `03 VOCES/textos_tts/<personaje>`
y los mp3 a `03 VOCES/crudo`, con el mismo nombre.

La llave sale de D:\DAE\_secretos\elevenlabs.txt, fuera del repositorio, y
nunca se imprime.

    python lanzar_voz_dh.py              los cinco
    python lanzar_voz_dh.py U3           solo esa
    python lanzar_voz_dh.py U3 --solo c18_tomese_su_tiempo   un bloque (toma
                                         nueva; la anterior va a _descartes)
"""
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_dh import VIDEOS, bloques            # noqa: E402
import rutas_dh as R                            # noqa: E402

ELEVEN = r'D:\DAE\_repo\herramientas\voz\elevenlabs.py'
VOZ = {'Carlos': 'Y4HwpMNrBWN5dFKi5Lw8',
       'Carmen': 'Pzocg9GZr24gNfKRHiyy',
       'Andres': 'Ux2YbCNfurnKHnzlBHGX',
       'Entrevistador': '4uvQjLPvqApx1dVzpNfM',
       'Sandra': 'oWSxI36XAKnfMWmzmQok',
       'Salgado': 'oWSxI36XAKnfMWmzmQok',
       'Quintero': 'x6LHvMgpXmty838MUqHh',
       'Julian': 'Ol2UUwISo9ncUTR92kGn',
       'Juez': '57D8YIbQSuE3REDPO6Vm'}
FF = os.environ.get('FFMPEG', 'ffmpeg')


def nombre(clave, i, nom):
    return 'DH_%s_%02d_%s' % (clave, i, nom)


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
        if v == 'SILENCIO':              # mudo, de los segundos del tts
            q = subprocess.run([FF, '-v', 'error', '-y', '-f', 'lavfi', '-i',
                                'anullsrc=r=44100:cl=mono', '-t', tts,
                                '-c:a', 'libmp3lame', '-b:a', '128k', mp3],
                               capture_output=True, text=True)
            assert q.returncode == 0, q.stderr[-400:]
            continue
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
