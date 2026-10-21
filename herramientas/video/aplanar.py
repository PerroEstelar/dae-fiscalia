#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplana un clip generado hasta que se parezca, medido, a su placa quieta.

EL PROBLEMA, MEDIDO ANTES DE INVENTAR LA SOLUCION
    Sebastian marco que los clips de movimiento tenian ruido y color raros
    frente a las placas. Medido en el gradiente local horizontal: las placas
    del Caso 3 estan en 1,3 a 2,1 y los clips salen en 3,5 a 9,1. A 1:1 se ve
    lo que es: un moteado fino y parejo sobre TODAS las superficies planas,
    como grano de pelicula. La forma y los bordes son los mismos.

    No es un defecto del modelo de video que se arregle cambiando de modelo:
    medido sobre los tres casos, los clips de Kling del Caso 1 marcan 7,45 y
    los de Veo del Caso 2 marcan 9,85, o sea peor que los 3,81 de este caso.
    Es lo que pasa cuando cualquier modelo generativo vuelve a renderizar una
    ilustracion perfectamente plana.

POR QUE nlmeans Y NO hqdn3d
    Probado y medido sobre el mismo cuadro: hqdn3d, hasta 50:40:60:50, baja el
    ruido de 9,07 a 7,24 y no alcanza. nlmeans a s=7 lo deja en 2,44 contra
    2,05 de la placa. El grano es fino y de alta frecuencia y las superficies
    son planas: es exactamente el caso para el que sirve un filtro de medias
    no locales.

LA FUERZA NO SE ELIGE A OJO: SE BUSCA
    Cada clip trae su propio grano y cada placa su propia lisura, asi que un
    s fijo sobra en unos y falta en otros -s=7 deja el r11 en 1,09 contra 1,58
    de su placa, o sea MAS liso que el original, que tambien esta mal-. Se
    prueban varios sobre el cuadro 0 y se queda el que minimiza la distancia
    relativa a las dos metricas de SU placa: ruido y dureza de borde.
"""
import json
import os
import subprocess
import sys

from PIL import Image, ImageFilter

ESCALAS = (3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)
FPS = '24000/1001'


def metricas(ruta):
    """(ruido, dureza): gradiente local y energia de borde."""
    im = Image.open(ruta).convert('L')
    g = im.resize((960, 540), Image.BOX)
    a = g.tobytes()
    W = 960
    idx = [i for i in range(len(a) - 1) if (i % W) < W - 1]
    ru = sum(abs(a[i] - a[i + 1]) for i in idx) / float(len(idx))
    e = im.filter(ImageFilter.FIND_EDGES)
    du = sum(e.tobytes()) / float(len(e.tobytes()))
    return ru, du


def _cuadro(clip, vf, destino):
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-i', clip]
    if vf:
        cmd += ['-vf', vf]
    cmd += ['-frames:v', '1', destino]
    subprocess.run(cmd, check=True)


def buscar(clip, placa, tmp):
    """Devuelve (s, metricas del clip, metricas de la placa)."""
    jp = os.path.join(tmp, 'ref.png')
    Image.open(placa).convert('RGB').resize((1920, 1080)).save(jp)
    obj = metricas(jp)
    mejor = None
    for s in ESCALAS:
        j = os.path.join(tmp, 'p%d.png' % int(s))
        _cuadro(clip, 'nlmeans=s=%.1f:p=7:r=15' % s, j)
        m = metricas(j)
        d = (abs(m[0] - obj[0]) / max(obj[0], 0.01)
             + abs(m[1] - obj[1]) / max(obj[1], 0.01))
        if mejor is None or d < mejor[0]:
            mejor = (d, s, m)
    return mejor[1], mejor[2], obj


def aplanar(clip, placa, salida, tmp):
    os.makedirs(tmp, exist_ok=True)
    s, m, obj = buscar(clip, placa, tmp)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', clip,
                    '-vf', 'nlmeans=s=%.1f:p=7:r=15' % s, '-an',
                    '-c:v', 'libx264', '-preset', 'slow', '-crf', '14',
                    '-pix_fmt', 'yuv420p', '-g', '600', '-keyint_min', '600',
                    '-sc_threshold', '0', '-r', FPS, salida], check=True)
    return dict(clip=os.path.basename(clip), s=s,
                clip_ruido=round(m[0], 2), clip_dureza=round(m[1], 2),
                placa_ruido=round(obj[0], 2), placa_dureza=round(obj[1], 2))


if __name__ == '__main__':
    trabajos = json.load(open(sys.argv[1], encoding='utf-8'))
    out = []
    for t in trabajos:
        r = aplanar(t['clip'], t['placa'], t['salida'], t['tmp'])
        out.append(r)
        print('%-26s s=%.1f  clip %5.2f/%6.2f  placa %5.2f/%6.2f'
              % (r['clip'][:26], r['s'], r['clip_ruido'], r['clip_dureza'],
                 r['placa_ruido'], r['placa_dureza']))
        sys.stdout.flush()
    json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
