#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Busca letra horneada en las placas y los clips de un caso.

POR QUE EXISTE
    En el Caso 2, el clip de movimiento de Elisa traia la palabra ELISA
    escrita dentro de la imagen, en 79x23 px, y parpadeando: aparecia en los
    primeros 40 cuadros de 168 y despues se iba. Eso no se ve en una hoja de
    contactos. Hay que LEER el cuadro, y hay que leer varios cuadros.

    Esta herramienta convierte esa revision en algo que se corre.

DOS COSAS QUE APRENDIO EL PRIMER BARRIDO
    1. La placa limpia no garantiza el clip limpio. `br05` salio limpia a
       2560 px y su horneado de camara dio un positivo a 1080: el encuadre
       agranda lo que en la placa era ilegible. Hay que mirar el clip.
    2. La letra horneada vive en los clips de Veo, no en las placas de
       Seedream. Las 31 placas del Caso 2 salieron limpias; los positivos,
       verdaderos y falsos, estaban todos en movimiento.

COMO SE LEE LA SALIDA
    Tesseract encuentra letras en cualquier textura: bordes de silla, patas
    de mesa, grano. El filtro util es el TAMANO: una palabra de verdad a
    1080p mide al menos 30x12 px. Por debajo de eso, es ruido. El resumen
    separa las dos cosas; los candidatos se miran recortados a 1:1, uno por
    uno, antes de decidir nada.

USO
    python barrido_letra.py "<carpeta del caso>" [prefijo]

    Espera dentro de esa carpeta `01 PLANOS` con las placas .png y, si
    existen, `07 MOVIMIENTO/CAPA V2` y `10 TIMELINE SEBASTIAN/RANURAS` con
    los clips.
"""
import csv
import io
import os
import re
import subprocess
import sys

TES = r"C:\Program Files\Tesseract-OCR\tesseract.EXE"
TMP = os.path.join(os.environ.get("TEMP", "."), "barrido_letra")
CONF = 65
MIN_ANCHO, MIN_ALTO = 30, 12     # el tamano de una palabra de verdad a 1080p
MUESTRAS_MOVIMIENTO = 12         # el parpadeo pide muchos cuadros
MUESTRAS_HORNEADO = 4            # un horneado de camara no cambia de contenido


def palabras(png):
    """Toda palabra legible del cuadro, con su caja."""
    r = subprocess.run([TES, png, 'stdout', '-l', 'spa+eng', '--psm', '11',
                        'tsv'], capture_output=True)
    out = []
    rd = csv.DictReader(io.StringIO(r.stdout.decode('utf-8', 'replace')),
                        delimiter='\t')
    for row in rd:
        try:
            c = float(row['conf'])
        except (TypeError, ValueError):
            continue
        # El campo de texto puede traer tabuladores o saltos y romper la
        # fila; se aplana antes de usarlo, que si no el informe se llena de
        # basura y tapa justo lo que se estaba buscando.
        t = re.sub(r'\s+', ' ', (row['text'] or '')).strip()
        if c >= CONF and len(t) >= 3 and sum(ch.isalpha() for ch in t) >= 3:
            out.append((t, int(c), int(row['left']), int(row['top']),
                        int(row['width']), int(row['height'])))
    return out


def cuadros(video, n):
    """n cuadros repartidos por el clip, como PNG temporales."""
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                        '-count_frames', '-show_entries',
                        'stream=nb_read_frames', '-of', 'csv=p=0', video],
                       capture_output=True)
    try:
        nf = int(r.stdout.decode().strip())
    except ValueError:
        return None
    png = os.path.join(TMP, 'f.png')
    for i in range(n):
        cu = int((i + 0.5) * nf / n)
        if os.path.exists(png):
            os.remove(png)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', video, '-vf',
                        'select=eq(n\\,%d)' % cu, '-frames:v', '1', png],
                       capture_output=True)
        if os.path.exists(png):
            yield cu, png


def barrer(caso, prefijo=''):
    os.makedirs(TMP, exist_ok=True)
    res = []

    d = os.path.join(caso, '01 PLANOS')
    placas = sorted(f for f in os.listdir(d)
                    if f.endswith('.png') and f.startswith(prefijo)
                    and not f.startswith('_')) if os.path.isdir(d) else []
    for f in placas:
        res.append((f, [(None,) + p for p in palabras(os.path.join(d, f))]))
        _linea(res[-1])

    clips = []
    for sub, n in (('07 MOVIMIENTO\\CAPA V2', MUESTRAS_MOVIMIENTO),
                   ('10 TIMELINE SEBASTIAN\\RANURAS', MUESTRAS_HORNEADO)):
        d = os.path.join(caso, sub)
        if not os.path.isdir(d):
            continue
        clips += [(os.path.join(d, f), n) for f in sorted(os.listdir(d))
                  if f.endswith('.mp4') and 'lecho' not in f]
    for p, n in clips:
        hits = []
        for cu, png in cuadros(p, n) or []:
            hits += [(cu,) + x for x in palabras(png)]
        res.append((os.path.basename(p), hits))
        _linea(res[-1])
    return res


def _linea(par):
    f, hits = par
    grandes = [h for h in hits if h[5] >= MIN_ANCHO and h[6] >= MIN_ALTO]
    print('%-46s %s' % (f, 'limpio' if not hits else
                        '%d hit(s), %d del tamano de una palabra'
                        % (len(hits), len(grandes))), flush=True)
    for cu, t, c, x, y, w, h in grandes:
        print('      %-18s conf %3d  en %4d,%4d  %dx%d%s'
              % (t[:18], c, x, y, w, h,
                 '  cuadro %d' % cu if cu is not None else ''), flush=True)


def resumen(res):
    print('')
    print('=== RESUMEN ===')
    grandes = [(f, h) for f, hits in res for h in hits
               if h[5] >= MIN_ANCHO and h[6] >= MIN_ALTO]
    print('%d archivos, %d limpios, %d con algun hit, %d candidatos de'
          ' tamano de palabra'
          % (len(res), sum(1 for _, hs in res if not hs),
             sum(1 for _, hs in res if hs), len(grandes)))
    for f, h in grandes:
        print('   %-44s %-14s %dx%d en %d,%d'
              % (f, h[1][:14], h[5], h[6], h[3], h[4]))
    print('')
    print('Los candidatos NO son hallazgos: hay que recortarlos a 1:1 y')
    print('mirarlos. En el Caso 2, de 6 candidatos 5 eran bordes de mueble.')


if __name__ == '__main__':
    r = barrer(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '')
    resumen(r)
