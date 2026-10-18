#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el master de narracion del C5U2 y saca la rejilla.

Mismo metodo que armar.py del C5U1; cambia el prefijo de los nombres y el
mapa de pausas, porque las bisagras de este caso son otras:

    b3_patrimonio  el giro: "todo lo que lo compone es de origen licito"
    b4_inventario  arranca el inventario
    b8_cierre      entra el cierre
"""
import json, os, subprocess, sys
import numpy as np
sys.path.insert(0, '/home/claude/c5/voz')
from armar import carga, SR, COLA, silencios

PREFIJO = 'C5U2_'
PAUSA = {'b3_patrimonio': 1.2, 'b4_inventario': 1.0, 'b8_cierre': 1.4}
PAUSA_POR_DEFECTO = 0.8


def main(carpeta, salida, reparto):
    fs = sorted(f for f in os.listdir(carpeta) if f.endswith('.mp3'))
    tramos, piezas, t = [], [], 0.0
    for i, f in enumerate(fs):
        x = carga(os.path.join(carpeta, f))
        piezas.append(x)
        nombre = f.replace(PREFIJO, '').replace('.mp3', '')
        tramos.append({'bloque': nombre, 'entra': round(t, 3),
                       'sale': round(t + len(x) / SR, 3),
                       'dur': round(len(x) / SR, 3)})
        t += len(x) / SR
        if i < len(fs) - 1:
            p = PAUSA.get(fs[i + 1].replace(PREFIJO, '').replace('.mp3', ''),
                          PAUSA_POR_DEFECTO)
            piezas.append(np.zeros(int(p * SR)))
            t += p
    piezas.append(np.zeros(int(COLA * SR)))
    y = np.concatenate(piezas)

    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR),
                          '-ac', '2', '-i', '-', '-c:a', 'pcm_s24le', salida],
                         stdin=subprocess.PIPE)
    p.stdin.write(np.repeat(np.clip(y, -1, 1).astype(np.float32), 2).tobytes())
    p.stdin.close(); p.wait()

    dur = len(y) / SR
    pal = sum(r['palabras'] for r in json.load(open(reparto, encoding='utf-8')))
    print('master %.2f s | %d palabras | %.0f palabras por minuto' % (dur, pal, pal / dur * 60))
    return tramos, dur


if __name__ == '__main__':
    tramos, dur = main(sys.argv[1], sys.argv[2], sys.argv[3])
    print()
    print('%-16s %7s %7s %7s' % ('bloque', 'entra', 'sale', 'dur'))
    for t in tramos:
        print('%-16s %7.2f %7.2f %7.2f' % (t['bloque'], t['entra'], t['sale'], t['dur']))
    sil = silencios(sys.argv[2])
    print()
    print('%d silencios medidos de 0,30 s o mas' % len(sil))
    json.dump({'dur': dur, 'tramos': tramos, 'silencios': sil},
              open(sys.argv[4], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
