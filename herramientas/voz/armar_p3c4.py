#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el master de narracion del P3C4 «Puerto de salida» y saca los tramos.

LAS PAUSAS MARCAN LA FORMA, Y AQUI LA FORMA ES OTRA
    Los tres casos anteriores eran una situacion con sus propuestas al lado, y
    la pausa larga iba antes de cada persona o antes de la bisagra. Este son
    SEIS ACTUACIONES SUCESIVAS, y dentro de cada una pasa dos veces lo mismo:
    primero el acto sustentado, despues el que no lo esta.

    Entonces hay dos jerarquias de pausa, no una:

      1,0 s  antes de cada actuacion nueva -b03, b06, b09, b11, b13, b15-.
             El oido tiene que oir seis apartados, porque son seis audiencias
             distintas y el espectador se pierde si suenan como un relato
             corrido.
      0,9 s  antes de cada propuesta o decision equivocada. Es el giro de cada
             escena y necesita un respiro propio, pero MENOR que el de la
             escena: si fuera igual, las seis escenas se oirian como doce.
      1,2 s  antes del cierre.
      0,8 s  el resto.

    Son 15,9 s de pausas sobre toda la pieza.
"""
import json
import os
import subprocess
import sys

import numpy as np

from armar import carga, SR, COLA

PREFIJO = 'P3C4_'

ACTUACION = 1.0     # empieza una audiencia nueva
GIRO = 0.9          # entra la propuesta o la decision equivocada
CIERRE = 1.2
POR_DEFECTO = 0.8

PAUSA = {
    'b03_solicitud': ACTUACION,
    'b04_prop_cuentas': GIRO,
    'b05_prop_registro': GIRO,
    'b06_captura_nora': ACTUACION,
    'b08_prop_permanente': GIRO,
    'b09_medida_nora': ACTUACION,
    'b10_decision_jueza': GIRO,
    'b11_medida_ivan': ACTUACION,
    'b12_prop_no_se_oye': GIRO,
    'b13_imputacion_lina': ACTUACION,
    'b14_prop_silencio': GIRO,
    'b15_imputacion_ivan': ACTUACION,
    'b17_prop_precisiones': GIRO,
    'b18_cierre': CIERRE,
}


def nombre(f):
    """P3C4_07_b07_recepcionista.mp3 -> b07_recepcionista"""
    return f.replace(PREFIJO, '').replace('.mp3', '').split('_', 1)[1]


def main(carpeta, salida):
    fs = sorted(f for f in os.listdir(carpeta) if f.endswith(('.mp3', '.wav')))
    tramos, piezas, t = [], [], 0.0
    for i, f in enumerate(fs):
        x = carga(os.path.join(carpeta, f))
        piezas.append(x)
        tramos.append({'bloque': nombre(f), 'entra': round(t, 3),
                       'sale': round(t + len(x) / SR, 3),
                       'dur': round(len(x) / SR, 3)})
        t += len(x) / SR
        if i < len(fs) - 1:
            p = PAUSA.get(nombre(fs[i + 1]), POR_DEFECTO)
            piezas.append(np.zeros(int(p * SR)))
            t += p
    piezas.append(np.zeros(int(COLA * SR)))
    y = np.concatenate(piezas)
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le',
                          '-ar', str(SR), '-ac', '2', '-i', '-',
                          '-c:a', 'pcm_s24le', salida], stdin=subprocess.PIPE)
    p.stdin.write(np.repeat(np.clip(y, -1, 1).astype(np.float32), 2).tobytes())
    p.stdin.close()
    p.wait()
    return tramos, len(y) / SR


if __name__ == '__main__':
    tramos, dur = main(sys.argv[1], sys.argv[2])
    print('master %.2f s  (%d:%04.1f)' % (dur, int(dur) // 60, dur % 60))
    print('%-26s %7s %7s %7s' % ('bloque', 'entra', 'sale', 'dur'))
    for t in tramos:
        print('%-26s %7.2f %7.2f %7.2f'
              % (t['bloque'], t['entra'], t['sale'], t['dur']))
    json.dump({'dur': dur, 'tramos': tramos},
              open(sys.argv[3], 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
