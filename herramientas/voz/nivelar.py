#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iguala el nivel PERCIBIDO de varios bloques de voz y comprueba el escalon.

EL PROBLEMA QUE RESUELVE
    Cuando la pieza alterna entre dos locutores, el oido sigue el nivel
    DURANTE el habla. Igualar los LUFS integrados no basta: el integrado
    promedia los silencios y castiga al bloque que calla mas, asi que dos
    bloques con el mismo integrado pueden sonar distinto, y al reves.

    Aqui se iguala la MEDIANA del short-term contando solo las ventanas con
    voz, que es lo que predice el nivel percibido, y despues se MIDE el salto
    entre bloque y bloque para comprobar que no quedo escalon.

EL TECHO
    Subir diez decibeles a una voz puede reventar el pico. Se aplica un
    limitador suave solo cuando hace falta, y se verifica el pico real
    sobremuestreando por cuatro: un pico entre muestras no se ve en el
    maximo de la senal.
"""
import os, subprocess, sys
import numpy as np
from medir import carga, perfil, _k, SR

OBJETIVO = -19.0      # LUFS de habla, el de la serie
TECHO_TP = -1.0       # dBTP


def mediana_habla(x):
    st = perfil(x)
    vivas = st[st > st.max() - 20]
    return float(np.median(vivas))


def true_peak(x, oversample=4):
    from scipy.signal import resample_poly
    return 20 * np.log10(np.abs(resample_poly(x, oversample, 1)).max() + 1e-12)


def limitar(x, techo_db):
    techo = 10 ** (techo_db / 20.0)
    tp = 10 ** (true_peak(x) / 20.0)
    if tp <= techo:
        return x, 0.0
    # reduccion suave: se baja todo lo justo y se redondean los picos
    k = techo / tp
    y = np.tanh(x / techo * 0.98) * techo
    # mezcla: solo donde el original pasaba del techo
    m = np.abs(x) > techo * 0.9
    out = x.copy()
    out[m] = y[m]
    return out, 20 * np.log10(k)


def escribir(ruta, x):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le',
                          '-ar', str(SR), '-ac', '1', '-i', '-',
                          '-c:a', 'libmp3lame', '-b:a', '192k', ruta],
                         stdin=subprocess.PIPE)
    p.stdin.write(np.clip(x, -1, 1).astype(np.float32).tobytes())
    p.stdin.close(); p.wait()


if __name__ == '__main__':
    salida = sys.argv[1]
    os.makedirs(salida, exist_ok=True)
    fuentes = sorted(sys.argv[2:])
    print('%-20s %7s %7s %7s %7s' % ('bloque', 'antes', 'ganancia', 'despues', 'picoTP'))
    niveles = []
    for f in fuentes:
        x = carga(f)
        antes = mediana_habla(x)
        g = OBJETIVO - antes
        y = x * (10 ** (g / 20.0))
        y, extra = limitar(y, TECHO_TP)
        d = os.path.join(salida, os.path.basename(f))
        escribir(d, y)
        z = carga(d)
        desp = mediana_habla(z)
        tp = true_peak(z)
        niveles.append((os.path.basename(f), desp))
        print('%-20s %7.1f %+7.1f %7.1f %7.1f' % (
            os.path.basename(f).replace('C5U1_', '').replace('.mp3', ''),
            antes, g, desp, tp))
    print()
    print('ESCALON ENTRE BLOQUES CONSECUTIVOS')
    peor = 0.0
    for i in range(1, len(niveles)):
        d = niveles[i][1] - niveles[i - 1][1]
        peor = max(peor, abs(d))
        print('   %-14s -> %-14s %+5.2f LU' % (
            niveles[i - 1][0].replace('C5U1_', '').replace('.mp3', '')[:14],
            niveles[i][0].replace('C5U1_', '').replace('.mp3', '')[:14], d))
    print('   peor salto: %.2f LU  (bajo 1,0 LU no se percibe)' % peor)
