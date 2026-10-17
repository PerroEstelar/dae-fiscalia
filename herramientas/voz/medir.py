#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mide el nivel PERCIBIDO de un bloque de voz, que no es el LUFS integrado.

POR QUE NO SIRVE EL INTEGRADO
    El integrado promedia toda la pista, silencios incluidos, y los penaliza
    segun cuanto callen. Un bloque con frases cortas y pausas largas integra
    mas bajo que uno corrido aunque las dos voces suenen igual de fuertes. Si
    se igualan los integrados, al cambiar de voz se oye el escalon.

    Lo que el oido sigue es el nivel DURANTE el habla. Por eso aqui se mide la
    MEDIANA del short-term (ventana de 3 s, paso de 0,1 s) contando solo las
    ventanas donde hay voz, y se descarta el resto.
"""
import subprocess, sys
import numpy as np

SR = 48000
VENT = 3.0
PASO = 0.1


def carga(ruta):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', ruta, '-ac', '1',
                          '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64)


def _k(x):
    """Ponderacion K de la BS.1770, en dos filtros biquad."""
    from scipy.signal import lfilter
    # shelving de cabeza
    b1 = [1.53512485958697, -2.69169618940638, 1.19839281085285]
    a1 = [1.0, -1.69065929318241, 0.73248077421585]
    # paso alto
    b2 = [1.0, -2.0, 1.0]
    a2 = [1.0, -1.99004745483398, 0.99007225036621]
    return lfilter(b2, a2, lfilter(b1, a1, x))


def perfil(x):
    """Short-term LUFS cada PASO segundos."""
    y = _k(x) ** 2
    L, p = int(VENT * SR), int(PASO * SR)
    n = (len(y) - L) // p + 1
    if n < 1:
        return np.array([])
    acum = np.cumsum(np.insert(y, 0, 0.0))
    idx = np.arange(n) * p
    ms = (acum[idx + L] - acum[idx]) / L
    return -0.691 + 10 * np.log10(ms + 1e-12)


def nivel_de_habla(ruta):
    x = carga(ruta)
    st = perfil(x)
    if not len(st):
        return None
    # se queda con las ventanas con voz: las que estan dentro de 20 LU del pico
    vivas = st[st > st.max() - 20]
    rms = np.sqrt((x ** 2).mean())
    return {
        'dur': len(x) / SR,
        'mediana_habla': float(np.median(vivas)),
        'p10': float(np.percentile(vivas, 10)),
        'p90': float(np.percentile(vivas, 90)),
        'integrado_aprox': float(-0.691 + 10 * np.log10((_k(x) ** 2).mean() + 1e-12)),
        'pico': float(20 * np.log10(np.abs(x).max() + 1e-12)),
        'silencio_pct': float(100 * (st <= st.max() - 20).mean()),
    }


if __name__ == '__main__':
    print('%-22s %6s %9s %9s %7s %7s %8s' % (
        'bloque', 'dur', 'habla', 'integrado', 'p10', 'p90', 'silencio'))
    for r in sys.argv[1:]:
        m = nivel_de_habla(r)
        print('%-22s %6.1f %9.1f %9.1f %7.1f %7.1f %7.0f%%' % (
            r.split('/')[-1].replace('C5U1_', '').replace('.mp3', ''),
            m['dur'], m['mediana_habla'], m['integrado_aprox'],
            m['p10'], m['p90'], m['silencio_pct']))
