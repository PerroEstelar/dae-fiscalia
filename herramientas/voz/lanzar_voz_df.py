# -*- coding: utf-8 -*-
r"""Pide las voces de los cinco capitulos del caso MIRIAM Y MARIANA.

Las dos voces son las MISMAS de toda la serie, y eso no es negociable: un
caso con otro locutor se oye como otra serie.

    Carlos   Y4HwpMNrBWN5dFKi5Lw8   colombian male middle_aged narrative
    Pilar    x6LHvMgpXmty838MUqHh   colombian female middle_aged narrative

SE MANDA `tts`, NO `texto`
    El guion trae dos versiones de cada bloque. A ElevenLabs va la version
    fonetica -sicosocial, treinta y seis, nueve milimetros-; el verbatim se
    queda para el carton. El .txt que se escribe aqui es el que se OYE, y
    por eso va a una carpeta que se llama `textos_tts`: para que nadie lo
    confunda con la fuente.

La llave sale de D:\DAE\_secretos\elevenlabs.txt, fuera del repositorio.
"""
import os
import subprocess
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_df import CAPITULOS, bloques          # noqa: E402

ELEVEN = r'D:\DAE\_repo\herramientas\voz\elevenlabs.py'
RAIZ = (r'E:\DAE MASTER\PRIORIDAD 03'
        '\\' r'CURSO - INVESTIGACION JUDICIAL Y FORENSE DE LA DESAPARICION FORZADA'
        '\\' r'UNIDAD DESAPARICION FORZADA' '\\' r'CASO MIRIAM Y MARIANA')
VOZ = {'Carlos': 'Y4HwpMNrBWN5dFKi5Lw8', 'Pilar': 'x6LHvMgpXmty838MUqHh'}

CAPS = {1: 'CAPITULO 1 - EL ECO EN LA PLAZA Y LA RESPUESTA DE PAPEL',
        2: 'CAPITULO 2 - RELOJES EN PAUSA Y EL CLAMOR EN LAS REDES',
        3: 'CAPITULO 3 - EL ENGRANAJE ROTO Y EL MAPA DE COMPETENCIAS',
        4: 'CAPITULO 4 - LAS VOCES QUE NO SE APAGAN Y EL DOLOR EN LA VENTANILLA',
        5: 'CAPITULO 5 - LA TIERRA HABLA Y LA MATRIZ DEL SILENCIO'}


def voces(cap):
    return os.path.join(RAIZ, CAPS[cap], '03 VOCES')


def escribir(cap):
    tx = os.path.join(voces(cap), 'textos_tts')
    n = 0
    for v in VOZ:
        os.makedirs(os.path.join(tx, v.lower()), exist_ok=True)
    os.makedirs(os.path.join(voces(cap), 'crudo'), exist_ok=True)
    for i, (nom, v, _texto, tts, _p) in enumerate(bloques(cap), 1):
        p = os.path.join(tx, v.lower(), 'DF_C%d_%02d_%s.txt' % (cap, i, nom))
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(tts)
        n += 1
    return n


def pedir(cap):
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    tx = os.path.join(voces(cap), 'textos_tts')
    crudo = os.path.join(voces(cap), 'crudo')
    for v, vid in VOZ.items():
        carpeta = os.path.join(tx, v.lower())
        if not os.listdir(carpeta):
            continue
        print('=== capitulo %d · %s' % (cap, v), flush=True)
        q = subprocess.run([sys.executable, ELEVEN, 'lote', carpeta, vid, crudo],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=env)
        s = ((q.stdout or '') + (q.stderr or ''))
        print(s.encode('ascii', 'replace').decode(), flush=True)


if __name__ == '__main__':
    caps = [int(x) for x in sys.argv[1:]] or sorted(CAPITULOS)
    for c in caps:
        print('%d textos escritos para el capitulo %d' % (escribir(c), c),
              flush=True)
    for c in caps:
        pedir(c)
    print('', flush=True)
    for c in caps:
        crudo = os.path.join(voces(c), 'crudo')
        fs = sorted(f for f in os.listdir(crudo) if f.endswith('.mp3'))
        falta = len(bloques(c)) - len(fs)
        print('capitulo %d: %d/%d mp3 %s'
              % (c, len(fs), len(bloques(c)),
                 'OK' if falta == 0 else ('FALTAN %d' % falta)), flush=True)
    print('LISTO', flush=True)
