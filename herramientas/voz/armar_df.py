# -*- coding: utf-8 -*-
r"""Arma el master de narracion de cada capitulo del caso MIRIAM Y MARIANA.

Es `armar_p3c5` con dos cambios y ninguno de fondo:

    1. LAS PAUSAS SALEN DEL GUION, no de un diccionario aparte. Cada bloque
       de `guion_df` ya declara la pausa que lleva delante, asi que el mapa
       de pausas y el texto no se pueden desincronizar. En el P3C5 eran dos
       archivos distintos y habia que acordarse de tocar los dos.

    2. CORRE POR CAPITULO. Son cinco piezas, no una.

Lo demas es identico y a proposito: nivelar cada bloque contra la MEDIANA
para que no haya escalon, concatenar con las pausas, y recien entonces una
ganancia al objetivo de la serie con un limitador que solo toca las puntas.
-19 LUFS, techo -1 dBTP.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'textos'))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_df import bloques, CAPITULOS          # noqa: E402

SR = 48000
COLA = 0.6
OBJETIVO = -19.0
LIMITE = -2.0

FF = os.environ.get('FFMPEG', 'ffmpeg')
FP = os.environ.get('FFPROBE', FF.replace('ffmpeg', 'ffprobe'))

RAIZ = (r'E:\DAE MASTER\PRIORIDAD 03'
        '\\' r'CURSO - INVESTIGACION JUDICIAL Y FORENSE DE LA DESAPARICION FORZADA'
        '\\' r'UNIDAD DESAPARICION FORZADA' '\\' r'CASO MIRIAM Y MARIANA')
CAPS = {1: 'CAPITULO 1 - EL ECO EN LA PLAZA Y LA RESPUESTA DE PAPEL',
        2: 'CAPITULO 2 - RELOJES EN PAUSA Y EL CLAMOR EN LAS REDES',
        3: 'CAPITULO 3 - EL ENGRANAJE ROTO Y EL MAPA DE COMPETENCIAS',
        4: 'CAPITULO 4 - LAS VOCES QUE NO SE APAGAN Y EL DOLOR EN LA VENTANILLA',
        5: 'CAPITULO 5 - LA TIERRA HABLA Y LA MATRIZ DEL SILENCIO'}


def medir(ruta):
    s = subprocess.run([FF, '-nostats', '-i', ruta, '-af', 'ebur128=peak=true',
                        '-f', 'null', '-'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace').stderr
    i = re.findall(r'I:\s+(-?\d+\.\d+) LUFS', s)
    p = re.findall(r'Peak:\s+(-?\d+\.\d+) dBFS', s)
    return (float(i[-1]) if i else None), (float(p[-1]) if p else None)


def duracion(ruta):
    s = subprocess.run([FP, '-v', 'error', '-show_entries', 'format=duration',
                        '-of', 'csv=p=0', ruta], capture_output=True,
                       text=True).stdout
    return float(s.strip())


def main(cap):
    voces = os.path.join(RAIZ, CAPS[cap], '03 VOCES')
    crudo = os.path.join(voces, 'crudo')
    salida = os.path.join(voces, 'DF_C%d_NARRADOR.wav' % cap)
    jsal = os.path.join(voces, 'DF_C%d_rejilla.json' % cap)

    orden = [b[0] for b in bloques(cap)]
    pausa = {b[0]: b[4] for b in bloques(cap)}

    fs = sorted(f for f in os.listdir(crudo) if f.endswith('.mp3'))
    # DF_C1_07_b07_nadie_la_vio.mp3 -> b07_nadie_la_vio
    def nom(f):
        return f[:-4].split('_', 3)[3]
    hay = {nom(f): f for f in fs}
    faltan = [b for b in orden if b not in hay]
    assert not faltan, 'faltan mp3: %s' % faltan
    fs = [hay[b] for b in orden]
    rutas = [os.path.join(crudo, f) for f in fs]

    niveles = [medir(r)[0] for r in rutas]
    duraciones = [duracion(r) for r in rutas]
    vivos = sorted(n for n in niveles if n is not None)
    med = (vivos[len(vivos) // 2] if len(vivos) % 2
           else (vivos[len(vivos) // 2 - 1] + vivos[len(vivos) // 2]) / 2.0)

    cmd = [FF, '-v', 'error', '-y']
    for r in rutas:
        cmd += ['-i', r]
    partes, etiquetas = [], []
    for i, (f, n) in enumerate(zip(fs, niveles)):
        g = (med - n) if n is not None else 0.0
        partes.append('[%d:a]aresample=%d,aformat=sample_fmts=fltp:'
                      'channel_layouts=mono,volume=%.4fdB[a%d]' % (i, SR, g, i))
        etiquetas.append('[a%d]' % i)
        if i < len(fs) - 1:
            p = pausa[orden[i + 1]]
            partes.append('aevalsrc=0:s=%d:d=%.4f,aformat=sample_fmts=fltp:'
                          'channel_layouts=mono[p%d]' % (SR, p, i))
            etiquetas.append('[p%d]' % i)
    partes.append('aevalsrc=0:s=%d:d=%.4f,aformat=sample_fmts=fltp:'
                  'channel_layouts=mono[cola]' % (SR, COLA))
    etiquetas.append('[cola]')
    partes.append('%sconcat=n=%d:v=0:a=1[out]'
                  % (''.join(etiquetas), len(etiquetas)))
    tmp = salida + '.tmp.wav'
    cmd += ['-filter_complex', ';'.join(partes), '-map', '[out]',
            '-c:a', 'pcm_s24le', '-ar', str(SR), '-ac', '1', tmp]
    q = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    if q.returncode:
        raise SystemExit('ffmpeg: ' + (q.stderr or '')[-1200:])

    antes, _ = medir(tmp)
    g = OBJETIVO - antes
    for intento in (1, 2):
        q = subprocess.run([FF, '-v', 'error', '-y', '-i', tmp,
                            '-af', 'volume=%.4fdB,alimiter=limit=%.4f:attack=5:'
                                   'release=50:level=disabled,'
                                   'aformat=channel_layouts=stereo'
                                   % (g, 10 ** (LIMITE / 20.0)),
                            '-c:a', 'pcm_s24le', '-ar', str(SR), salida],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace')
        if q.returncode:
            raise SystemExit('ffmpeg: ' + (q.stderr or '')[-800:])
        hecho, pico = medir(salida)
        if abs(hecho - OBJETIVO) <= 0.2:
            break
        g += (OBJETIVO - hecho)
    os.remove(tmp)

    tramos, t = [], 0.0
    for i, (b, d) in enumerate(zip(orden, duraciones)):
        tramos.append({'bloque': b, 'entra': round(t, 3),
                       'sale': round(t + d, 3), 'dur': round(d, 3)})
        t += d
        if i < len(orden) - 1:
            t += pausa[orden[i + 1]]
    t += COLA

    info = {'capitulo': cap, 'dur': round(t, 3), 'tramos': tramos,
            'lufs_crudo': antes, 'ganancia_db': round(g, 2),
            'lufs_final': hecho, 'pico_dbfs': pico}
    json.dump(info, open(jsal, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    return info


if __name__ == '__main__':
    caps = [int(x) for x in sys.argv[1:]] or sorted(CAPITULOS)
    for c in caps:
        info = main(c)
        d = info['dur']
        print('capitulo %d  master %.2f s (%d:%04.1f)  %.1f LUFS  pico %.1f dBFS'
              % (c, d, int(d) // 60, d % 60, info['lufs_final'],
                 info['pico_dbfs']), flush=True)
        for t in info['tramos']:
            print('      %-26s %7.2f %7.2f %7.2f'
                  % (t['bloque'], t['entra'], t['sale'], t['dur']), flush=True)
    print('LISTO', flush=True)
