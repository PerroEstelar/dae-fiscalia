#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Silencios reales de una locucion, con ventana corta.

LA VENTANA IMPORTA MAS QUE EL UMBRAL
    Con la ventana de 3 s del short-term, una pausa de 0,8 s no baja el nivel
    lo suficiente y el detector devuelve cero silencios aunque esten ahi. Para
    encontrar PAUSAS hace falta una ventana del orden de la pausa: 50 ms de
    RMS, y el umbral relativo al nivel de habla del propio bloque.
"""
import json, subprocess, sys
import numpy as np
from medir import carga, SR

VENT = 0.050
UMBRAL_DB = -30.0     # por debajo del nivel de habla
MIN = 0.22            # una pausa util para cortar


def rms_corto(x, vent=VENT):
    n = int(vent * SR)
    m = (len(x) // n) * n
    return np.sqrt((x[:m].reshape(-1, n) ** 2).mean(axis=1) + 1e-12), n / SR


def buscar(x, umbral_db=UMBRAL_DB, minimo=MIN):
    r, paso = rms_corto(x)
    db = 20 * np.log10(r)
    habla = np.percentile(db[db > db.max() - 40], 60)
    quieto = db < habla + umbral_db
    out, i = [], 0
    while i < len(quieto):
        if quieto[i]:
            j = i
            while j < len(quieto) and quieto[j]:
                j += 1
            if (j - i) * paso >= minimo:
                out.append((round(i * paso, 2), round(j * paso, 2),
                            round((j - i) * paso, 2)))
            i = j
        else:
            i += 1
    return out, habla


if __name__ == '__main__':
    x = carga(sys.argv[1])
    sil, habla = buscar(x)
    print('%s  %.1f s  nivel de habla %.1f dB' % (sys.argv[1].split('/')[-1], len(x) / SR, habla))
    print('%d pausas de %.2f s o mas' % (len(sil), MIN))
    for a, b, d in sil:
        print('   %7.2f -> %7.2f   %.2f s' % (a, b, d))
    if len(sys.argv) > 2:
        json.dump([{'ini': a, 'fin': b, 'dur': d} for a, b, d in sil],
                  open(sys.argv[2], 'w'), indent=1)
