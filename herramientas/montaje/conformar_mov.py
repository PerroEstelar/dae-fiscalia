#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Conforma los clips generados a ranuras de la serie.

DOS COSAS QUE HAY QUE ARREGLAR EN TODO CLIP GENERADO
    1. SALE A 24,000 Y LA SERIE VA A 23,976. No es un redondeo: son 1,001
       cuadros de diferencia cada mil, y sobre doce segundos eso es medio
       cuadro de deriva contra la voz. Se reinterpreta el ritmo -no se
       remuestrea- porque el contenido es el mismo, solo cambia el reloj.

    2. NO MIDE LO QUE MIDE LA RANURA. Seedance entrega duraciones enteras en
       segundos y las ranuras salen de los silencios de la locucion, que no
       son enteros. Lo que sobra se recorta por el final; lo que falta se
       gana estirando el tiempo con `setpts`, nunca congelando el ultimo
       cuadro: una congelacion de tres cuadros en un plano donde alguien
       camina se ve, y un 1 % de camara lenta no.

Se escribe con el mismo nombre que usa `camara.py` -`..._v<cuadros>.mp4`-
para que `montar_p3c4_v2.medios()` los recoja sin saber de donde vienen.
"""
import json
import os
import subprocess
import sys

FPS = '24000/1001'
FPS_N = 24000.0 / 1001


def cuadros(p):
    o = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                        '-count_frames', '-show_entries',
                        'stream=nb_read_frames', '-of', 'default=nw=1:nk=1',
                        p], capture_output=True, text=True).stdout.strip()
    return int(o)


def conformar(origen, destino, n):
    """Deja `origen` en exactamente `n` cuadros a 23,976."""
    hay = cuadros(origen)
    # el factor de tiempo: lo que hay contra lo que se necesita
    pts = float(n) / hay
    vf = ('settb=AVTB,setpts=%.9f*PTS' % pts) if abs(pts - 1.0) > 1e-6 else 'settb=AVTB,setpts=PTS'
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', origen,
           '-vf', vf, '-r', FPS, '-frames:v', str(n),
           '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', '14',
           '-pix_fmt', 'yuv420p', '-g', '600', '-keyint_min', '600',
           '-sc_threshold', '0', destino]
    subprocess.run(cmd, check=True)
    sal = cuadros(destino)
    return hay, sal, pts


if __name__ == '__main__':
    MOV = sys.argv[1]
    RAN = sys.argv[2]
    MAPA = json.load(open(sys.argv[3], encoding='utf-8'))
    os.makedirs(RAN, exist_ok=True)
    print('%-34s %6s %6s %8s %s' % ('ranura', 'origen', 'final', 'tiempo', 'ok'))
    mal = []
    for k in sorted(MAPA, key=int):
        n, nom = MAPA[k]['cuadros'], MAPA[k]['nombre']
        o = os.path.join(MOV, 'P3C4_mov_r%02d.mp4' % int(k))
        d = os.path.join(RAN, '%s_v%d.mp4' % (nom, n))
        hay, sal, pts = conformar(o, d, n)
        ok = (sal == n)
        if not ok:
            mal.append((nom, sal, n))
        print('%-34s %6d %6d %7.3fx %s' % (nom, hay, sal, pts, 'OK' if ok else 'FALLA'))
    print('')
    print('FALLOS:', mal or 'ninguno')
