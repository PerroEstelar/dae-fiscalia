# -*- coding: utf-8 -*-
r"""Cuando una pieza se APRIETA (`voz/apretar_dh.py`), sus ranuras horneadas y
sus detalles se acortan: este paso escribe la version corta de cada una.

    python apretar_ranuras_dh.py U3 <mapa.json>

`mapa.json` es el que deja el plan (u3_apretado.json): `ranuras` = {n: [ini
nuevo, largo nuevo, ini viejo, largo viejo]} y `det` = {nombre: {ranura,
entra, cuadros}} ya pasados por el mapa.

LO QUE HACE
    Ranura simple: la horneada vieja (RANURAS/<nm>_v<viejo>.mp4) se corta a
    sus primeros <nuevo> cuadros y se escribe RANURAS/<nm>_v<nuevo>.mp4. El
    horneado de la serie es SIN empuje (encuadre 0,88 y pulso de mano), asi
    que cortar el final no pierde nada: es el mismo plano, mas corto. Las
    REUSA con empuje (r06, r10, r11, r12, r20, r27 de la U3) terminan el
    empuje un poco antes; tampoco se nota.
    Ranura COMPUESTA (dos placas pegadas por corte, con el corte puesto en
    una palabra de la voz): NO se corta aqui; se vuelve a hornear con
    `dh_pieza construir=<n,...>` con el corte ya pasado por el mapa en
    `escenas_dh_<L>.COMPUESTAS`.
    Detalle (V3): DETALLE/<det>_v<viejo>.mp4 se corta a <nuevo>.
Lo viejo no se toca: el archivo nuevo tiene otro nombre (otro largo), que
es ademas lo que evita la cache de Resolve.
"""
import json
import os
import subprocess
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import dh_pieza as SP                                   # noqa: E402
import rutas_dh as R                                    # noqa: E402


def corta(src, dst, n):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-frames:v', str(n),
                    '-c:v', 'libx264', '-crf', '14', '-preset', 'slow',
                    '-pix_fmt', 'yuv420p', '-an', dst], check=True)
    return SP.cuadros(dst)


def main(L, mapa):
    a = json.load(open(mapa, encoding='utf-8'))
    tl = R.sub(L, '10 TIMELINE SEBASTIAN')
    comp = getattr(SP.E(L), 'COMPUESTAS', {})
    for k, (ns, nl, vs, vl) in sorted(a['ranuras'].items(), key=lambda x: int(x[0])):
        n = int(k)
        nm = SP.nombre(L, n)
        if n in comp:
            SP.w('r%02d compuesta: se rehornea con construir' % n)
            continue
        src = os.path.join(tl, 'RANURAS', '%s_v%d.mp4' % (nm, vl))
        dst = os.path.join(tl, 'RANURAS', '%s_v%d.mp4' % (nm, nl))
        if os.path.exists(dst):
            SP.w('r%02d ya estaba: %s' % (n, os.path.basename(dst)))
            continue
        got = corta(src, dst, nl)
        SP.w('r%02d %3d -> %3d  %s' % (n, vl, got, 'OK' if got == nl else 'FALLA'))
    det = SP.E(L).DET
    for (n, nm), d in sorted(det.items()):
        full = '%s_r%02d_%s_det' % ('DH_' + L, n, nm)
        viejo = [f for f in os.listdir(os.path.join(tl, 'DETALLE'))
                 if f.startswith(full + '_v') and f.endswith('.mp4')]
        nuevo = os.path.join(tl, 'DETALLE', '%s_v%d.mp4' % (full, d['cuadros']))
        if os.path.exists(nuevo):
            SP.w('%s ya estaba' % os.path.basename(nuevo))
            continue
        src = os.path.join(tl, 'DETALLE', sorted(viejo, key=len)[0])
        got = corta(src, nuevo, d['cuadros'])
        SP.w('%s %s -> %d %s' % (full, os.path.basename(src), got,
                                 'OK' if got == d['cuadros'] else 'FALLA'))
    SP.w('LISTO')


if __name__ == '__main__':
    main(sys.argv[1].upper(), sys.argv[2])
