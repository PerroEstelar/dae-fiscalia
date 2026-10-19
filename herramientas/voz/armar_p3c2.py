#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el master de narracion del P3C2 y saca la rejilla.

LAS PAUSAS MARCAN LA FORMA DE LA PIEZA
    Este caso no es un relato continuo sino cuatro personas, cada una con su
    propuesta equivocada al lado. Entonces la pausa larga va ANTES de cada
    persona -b3 Mara, b6 Samuel, b9 Elisa, b11 Patricia- y la mas larga antes
    del cierre. El oido lee esos cuatro respiros como cuatro apartados, que es
    exactamente lo que el documento tiene.
"""
import json, os, subprocess, sys
import numpy as np
sys.path.insert(0, '/home/claude/c5/voz')
from armar import carga, SR, COLA

PREFIJO = 'P3C2_'
PAUSA = {'b3_mara': 1.0, 'b6_samuel': 1.0, 'b9_elisa': 1.0,
         'b11_patricia': 1.0, 'b12_cierre': 1.2}
PAUSA_POR_DEFECTO = 0.8


def nombre(f):
    return f.replace(PREFIJO, '').replace('.mp3', '').split('_', 1)[1]


def main(carpeta, salida):
    fs = sorted(f for f in os.listdir(carpeta) if f.endswith('.mp3'))
    tramos, piezas, t = [], [], 0.0
    for i, f in enumerate(fs):
        x = carga(os.path.join(carpeta, f))
        piezas.append(x)
        tramos.append({'bloque': nombre(f), 'entra': round(t, 3),
                       'sale': round(t + len(x) / SR, 3),
                       'dur': round(len(x) / SR, 3)})
        t += len(x) / SR
        if i < len(fs) - 1:
            p = PAUSA.get(nombre(fs[i + 1]), PAUSA_POR_DEFECTO)
            piezas.append(np.zeros(int(p * SR)))
            t += p
    piezas.append(np.zeros(int(COLA * SR)))
    y = np.concatenate(piezas)
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR),
                          '-ac', '2', '-i', '-', '-c:a', 'pcm_s24le', salida],
                         stdin=subprocess.PIPE)
    p.stdin.write(np.repeat(np.clip(y, -1, 1).astype(np.float32), 2).tobytes())
    p.stdin.close(); p.wait()
    return tramos, len(y) / SR


if __name__ == '__main__':
    tramos, dur = main(sys.argv[1], sys.argv[2])
    print('master %.2f s' % dur)
    print('%-22s %7s %7s %7s' % ('bloque', 'entra', 'sale', 'dur'))
    for t in tramos:
        print('%-22s %7.2f %7.2f %7.2f' % (t['bloque'], t['entra'], t['sale'], t['dur']))
    json.dump({'dur': dur, 'tramos': tramos},
              open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
