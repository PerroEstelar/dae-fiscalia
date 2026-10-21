# -*- coding: utf-8 -*-
"""Pide las dieciocho voces del Caso 4 a ElevenLabs, por lote y por voz.

Las dos voces son las MISMAS de toda la serie, y eso no es negociable: un caso
con otro locutor se oye como otra serie.

    Carlos   Y4HwpMNrBWN5dFKi5Lw8   colombian male middle_aged narrative
    Pilar    x6LHvMgpXmty838MUqHh   colombian female middle_aged narrative

El nombre del .txt manda: `lote` escribe el mp3 con el mismo nombre, y el
armador ordena por ese nombre y le saca el bloque. Por eso van numerados.
"""
import os
import subprocess
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_p3c4 import BLOQUES

ELEVEN = r'D:\DAE\_repo\herramientas\voz\elevenlabs.py'
BASE = r'E:\DAE MASTER\PRIORIDAD 03\CASO 04 - Puerto de salida\03 VOCES'
VOZ = {'Carlos': 'Y4HwpMNrBWN5dFKi5Lw8', 'Pilar': 'x6LHvMgpXmty838MUqHh'}

TX = os.path.join(BASE, 'textos')
CRUDO = os.path.join(BASE, 'crudo')


def escribir():
    n = 0
    for v in VOZ:
        os.makedirs(os.path.join(TX, v.lower()), exist_ok=True)
    os.makedirs(CRUDO, exist_ok=True)
    for i, (nom, v, t) in enumerate(BLOQUES, 1):
        p = os.path.join(TX, v.lower(), 'P3C4_%02d_%s.txt' % (i, nom))
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(t)
        n += 1
    return n


def pedir():
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    for v, vid in VOZ.items():
        carpeta = os.path.join(TX, v.lower())
        print('=== %s (%s)' % (v, vid), flush=True)
        q = subprocess.run([sys.executable, ELEVEN, 'lote', carpeta, vid, CRUDO],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=env)
        s = ((q.stdout or '') + (q.stderr or ''))
        print(s.encode('ascii', 'replace').decode(), flush=True)


if __name__ == '__main__':
    print('%d textos escritos' % escribir(), flush=True)
    pedir()
    fs = sorted(f for f in os.listdir(CRUDO) if f.endswith('.mp3'))
    print('\n%d mp3 en crudo' % len(fs), flush=True)
    for f in fs:
        print('   %-38s %6d KB' % (f, os.path.getsize(os.path.join(CRUDO, f)) // 1024),
              flush=True)
