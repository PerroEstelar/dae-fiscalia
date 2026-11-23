# -*- coding: utf-8 -*-
"""Rinde las tres líneas sin «Tarea del foro» (ver `foros_v2_lineas.py`) y compara cada entrega con la anterior.

Para cada caso, en orden (Resolve rinde de a uno):
1. `mp4_entrega.py <línea> <carpeta del caso> <nombre>`.
2. PSNR cuadro a cuadro contra la entrega anterior, a 480×270: fuera del cartón cambiado ningún cuadro puede
   quedar por debajo de 35 dB; el cartón es el único tramo que debe bajar.
3. Audio: la entrega nueva menos la anterior (mono, 48 kHz), pico y RMS de la diferencia.

    python foros_v2_cadena.py [log]          (log por defecto: D:/DAE/_tmp/c5u3/cadena_foros.log)

Termina con «CADENA LISTA».
"""
import glob
import os
import re
import subprocess
import sys
import time

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
FF = os.path.join(FB, 'ffmpeg.exe')
AQUI = os.path.dirname(os.path.abspath(__file__))
LOG = sys.argv[1] if len(sys.argv) > 1 else 'D:/DAE/_tmp/c5u3/cadena_foros.log'
TMP = os.path.dirname(LOG)
B5 = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/'
SRPA = 'E:/DAE MASTER/CURSO 1 - SRPA/UNIDAD 1 - PROFE CARLOS HUMBERTO/UNIDAD 5/cASO 1'
CASOS = [
    ('c5u1', 'C5U1 LOGISTICA CMR - a la voz v2', B5 + 'UNIDAD 1/CASO 01 - logistica CMR del norte',
     'C5U1 - revision v7', 'C5U1 - revision v6.mov', (4610, 4874)),
    ('c5u2', 'C5U2 SINIESTRO VIAL - a la voz v3', B5 + 'UNIDAD 2/CASO 02 - el siniestro vial',
     'C5U2 - revision v3', 'C5U2 - revision v2.mov', (5122, 5418)),
    ('u5c1', 'U5C1 LOS CHAPULINES - a la voz v2', SRPA,
     'U5C1_LOS_CHAPULINES_revision v2', 'U5C1_LOS_CHAPULINES_revision.mov', (4070, 4262)),
]


def w(*a):
    s = time.strftime('%H:%M:%S ') + ' '.join(str(x) for x in a)
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(s + '\n')


def psnr(nueva, vieja, clave, rango):
    st = os.path.join(TMP, 'psnr_%s.txt' % clave)
    subprocess.run([FF, '-v', 'error', '-i', nueva, '-i', vieja, '-filter_complex',
                    '[0:v]scale=480:270[a];[1:v]scale=480:270[b];[a][b]psnr=stats_file=' +
                    os.path.basename(st), '-f', 'null', '-'], check=True, cwd=TMP)
    fuera, dentro, bajos = [], [], []
    for ln in open(st):
        m = re.search(r'n:(\d+).*psnr_avg:(\S+)', ln)
        if not m:
            continue
        n = int(m.group(1)) - 1
        v = float('inf') if m.group(2) == 'inf' else float(m.group(2))
        (dentro if rango[0] <= n < rango[1] else fuera).append(v)
        if v < 35 and not (rango[0] <= n < rango[1]):
            bajos.append((n, round(v, 1)))
    w(clave, 'PSNR: %d cuadros; fuera del cartón mín %.1f dB; en el cartón mín %.1f dB; bajo 35 fuera: %s'
      % (len(fuera) + len(dentro), min(fuera), min(dentro), bajos[:20] or 'ninguno'))
    return not bajos


def audio(nueva, vieja, clave):
    f = ('[0:a]aresample=48000,pan=mono|c0=0.5*c0+0.5*c1[a];'
         '[1:a]aresample=48000,pan=mono|c0=0.5*c0+0.5*c1,volume=-1[b];'
         '[a][b]amix=inputs=2:normalize=0,astats=measure_overall=Peak_level+RMS_level:measure_perchannel=none')
    r = subprocess.run([FF, '-hide_banner', '-i', nueva, '-i', vieja, '-filter_complex', f, '-f', 'null', '-'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    lv = re.findall(r'(Peak level dB|RMS level dB):\s*(\S+)', r.stderr)
    w(clave, 'audio, nueva menos anterior:', lv)


def main():
    w('== cadena foros v2')
    for clave, linea, carpeta, nombre, vieja, rango in CASOS:
        w(clave, 'rindiendo', linea, '->', nombre)
        r = subprocess.run([sys.executable, os.path.join(AQUI, 'mp4_entrega.py'), linea, carpeta, nombre],
                           capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=AQUI)
        for ln in (r.stdout + r.stderr).strip().splitlines()[-12:]:
            w(clave, '|', ln)
        nueva = '%s/05 EXPORTS/%s.mp4' % (carpeta, nombre)
        if r.returncode or not os.path.exists(nueva):
            w(clave, 'FALLÓ la entrega, código', r.returncode)
            continue
        ok = psnr(nueva, '%s/05 EXPORTS/%s' % (carpeta, vieja), clave, rango)
        audio(nueva, '%s/05 EXPORTS/%s' % (carpeta, vieja), clave)
        w(clave, 'IMAGEN OK' if ok else 'IMAGEN: REVISAR')
    w('CADENA LISTA')


if __name__ == '__main__':
    main()
