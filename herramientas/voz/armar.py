#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Une los bloques nivelados en el master de narracion y saca la rejilla.

Las pausas entre bloques no se dejan al azar: cada frontera es un corte de
montaje. Las de dentro del inventario son cortas -un bien y el siguiente-, y
las de las bisagras son mas largas: donde empieza el inventario y donde entra
el cierre.
"""
import json, os, subprocess, sys
import numpy as np
from medir import carga, perfil, SR

PAUSA = {'b2_diligencia': 1.2,   # antes del inventario
         'b9_cierre': 1.4}       # antes del cierre
PAUSA_POR_DEFECTO = 0.8
COLA = 0.6


def main(carpeta, salida, reparto):
    fs = sorted(f for f in os.listdir(carpeta) if f.endswith('.mp3'))
    tramos, piezas, t = [], [], 0.0
    for i, f in enumerate(fs):
        x = carga(os.path.join(carpeta, f))
        piezas.append(x)
        nombre = f.replace('C5U1_', '').replace('.mp3', '')
        tramos.append({'bloque': nombre, 'entra': round(t, 3),
                       'sale': round(t + len(x) / SR, 3),
                       'dur': round(len(x) / SR, 3)})
        t += len(x) / SR
        if i < len(fs) - 1:
            p = PAUSA.get(fs[i + 1].replace('C5U1_', '').replace('.mp3', ''),
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
    pal = sum(json.load(open(reparto, encoding='utf-8'))[i]['palabras']
              for i in range(len(fs)))
    print('master %.2f s | %d palabras | %.0f palabras por minuto' % (dur, pal, pal / dur * 60))
    return tramos, dur


def silencios(ruta, umbral_lu=20, minimo=0.30):
    x = carga(ruta)
    st = perfil(x)
    techo = st.max()
    quieto = st <= techo - umbral_lu
    out, i = [], 0
    while i < len(quieto):
        if quieto[i]:
            j = i
            while j < len(quieto) and quieto[j]:
                j += 1
            a, b = i * 0.1, j * 0.1 + 3.0
            if b - a >= minimo:
                out.append((round(a, 2), round(b, 2)))
            i = j
        else:
            i += 1
    return out


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
