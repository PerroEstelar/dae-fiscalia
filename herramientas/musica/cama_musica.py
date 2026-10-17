#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la cama de música de una pieza, con el ducking ya horneado.

POR QUÉ HORNEADO Y NO AUTOMATIZADO EN RESOLVE
    La API de Resolve de este build no deja escribir niveles ni keyframes de
    audio. Entonces el archivo sale con la envolvente ya aplicada y entra a la
    línea con la ganancia en cero. Si hay que cambiar el balance, se vuelve a
    correr esto, no se toca el fader.

LOS NIVELES DE LA SERIE
    voz           −19 LUFS
    música        −32 LUFS bajo la narración   (13 dB por debajo de la voz)
    música        −26 LUFS en los huecos y bajo el bloque de preguntas
    Se normaliza a −26 y se baja 6 dB donde hay narración, con rampas de 1 s.
"""
import json, math, os, subprocess, sys
import numpy as np

SR = 48000
RAMPA = 1.0          # segundos de subida y bajada del ducking
ENTRADA = 1.5        # fade in
SALIDA = 2.5         # fade out
DUCK_DB = -6.0


def _decodificar(ruta, dur, costura=None):
    cmd = ["ffmpeg", "-v", "error", "-i", ruta, "-t", f"{dur:.3f}",
           "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    crudo = subprocess.run(cmd, capture_output=True, check=True).stdout
    a = np.frombuffer(crudo, dtype=np.float32).reshape(-1, 2).copy()
    n = int(round(dur * SR))
    if costura:
        return _armar_con_costura(a, n, costura)
    if len(a) < n:                      # la pista es más corta: se repite con cruce
        cruce = int(1.5 * SR)
        salida = np.zeros((n, 2), dtype=np.float32)
        pos = 0
        while pos < n:
            tramo = a if pos == 0 else a[cruce:]
            fin = min(pos + len(tramo), n)
            trozo = tramo[: fin - pos].copy()
            if pos > 0:
                k = min(cruce, len(trozo))
                f = np.linspace(0, 1, k, dtype=np.float32)[:, None]
                salida[pos:pos + k] = salida[pos:pos + k] * (1 - f) + trozo[:k] * f
                salida[pos + k:fin] = trozo[k:]
            else:
                salida[pos:fin] = trozo
            pos = fin - (cruce if fin < n else 0)
        a = salida
    return a[:n]


def _armar_con_costura(a, n, costura, cruce_s=2.5):
    """Cabeza + el bucle del cuerpo las veces que haga falta + cola.

    POR QUE EXISTE
        Una pieza compuesta -intro, cuerpo y cierre- no da la vuelta: el final
        no se parece al principio porque nunca se penso para eso, y da igual
        donde se corte. La pista del Curso 5 mide -16 dB al empezar, sube a -7
        en el cuerpo y cae a -34 en el ultimo compas; ninguna costura de vuelta
        completa pasa de 0,50 de correlacion.

        Con costura=(salida, retorno) se repite SOLO el tramo del cuerpo: la
        cabeza entra una vez, el tramo entre retorno y salida se repite las
        veces que hagan falta, y la cola -con el final real- cierra. La pieza
        entra con la entrada de la musica y termina con su cadencia.

    EL FINAL CAE SIEMPRE EN EL ULTIMO CUADRO
        Si sobra o falta material se ajusta el BUCLE, nunca la cola. Rellenar
        con silencio seria tirar a la basura el final que se queria conservar.

    Los dos puntos salen de costura.py, que los busca por correlacion
    normalizada en vez de a ojo.
    """
    sal, ret = [int(x * SR) for x in costura]
    cr = int(cruce_s * SR)
    cabeza, bucle, cola = a[:ret], a[ret:sal], a[sal:]
    if len(bucle) <= cr * 2:
        raise ValueError("el bucle es mas corto que dos cruces")

    falta = n - len(cabeza) - len(cola) + cr * 2
    if falta < len(bucle):
        vueltas, recorte = 1, len(bucle) - max(falta, cr * 2 + 1)
    else:
        paso = len(bucle) - cr
        vueltas = int(math.ceil((falta - len(bucle)) / float(paso))) + 1
        recorte = len(bucle) + paso * (vueltas - 1) - falta

    def cruzar(x, y):
        k = min(cr, len(x), len(y))
        f = np.linspace(0, 1, k, dtype=np.float32)[:, None]
        m = x[-k:] * np.cos(f * np.pi / 2) + y[:k] * np.sin(f * np.pi / 2)
        return np.concatenate([x[:-k], m, y[k:]])

    res = cabeza
    for v in range(vueltas):
        tramo = bucle if v < vueltas - 1 else bucle[:len(bucle) - recorte]
        res = cruzar(res, tramo)
    res = cruzar(res, cola)

    print("   cabeza %.1f s + %d vuelta(s) de %.1f s + cola %.1f s = %.1f s (pedidos %.1f)"
          % (ret / SR, vueltas, (sal - ret) / SR, (len(a) - sal) / SR,
             len(res) / SR, n / SR))
    if len(res) < n:
        res = np.concatenate([res, np.zeros((n - len(res), 2), dtype=np.float32)])
    return res[:n]


def _envolvente(dur, tramos_voz):
    """1.0 en los huecos, DUCK_DB donde hay voz, con rampas lineales."""
    n = int(round(dur * SR))
    g = np.ones(n, dtype=np.float32)
    duck = float(10 ** (DUCK_DB / 20))
    r = int(RAMPA * SR)
    for a, b in tramos_voz:
        ia, ib = int(a * SR), int(b * SR)
        i0, i1 = max(0, ia - r), min(n, ib + r)
        if ia > i0:
            g[i0:ia] = np.minimum(g[i0:ia], np.linspace(1.0, duck, ia - i0, dtype=np.float32))
        g[max(0, ia):min(n, ib)] = np.minimum(g[max(0, ia):min(n, ib)], duck)
        if i1 > ib:
            g[ib:i1] = np.minimum(g[ib:i1], np.linspace(duck, 1.0, i1 - ib, dtype=np.float32))
    ne, ns = int(ENTRADA * SR), int(SALIDA * SR)
    g[:ne] *= np.linspace(0, 1, ne, dtype=np.float32)
    g[-ns:] *= np.linspace(1, 0, ns, dtype=np.float32)
    return g[:, None]


def _lufs(ruta):
    out = subprocess.run(["ffmpeg", "-nostats", "-i", ruta, "-af", "ebur128=peak=true",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    for i, l in enumerate(out.splitlines()):
        if "Integrated loudness" in l:
            for s in out.splitlines()[i:i + 3]:
                if s.strip().startswith("I:"):
                    return float(s.split()[1])
    return None


def cama(pista, salida, dur, tramos_voz, objetivo=-26.0, costura=None):
    a = _decodificar(pista, dur, costura)

    tmp = salida + ".plano.wav"
    _escribir(tmp, a)
    actual = _lufs(tmp)
    a *= float(10 ** ((objetivo - actual) / 20))        # al nivel de hueco
    os.remove(tmp)

    a *= _envolvente(dur, tramos_voz)
    pico = float(np.abs(a).max())
    if pico > 0.89:                                      # techo a −1 dBTP con aire
        a *= 0.89 / pico
    _escribir(salida, a)
    print(f"{os.path.basename(salida)}  {dur:.1f}s  hueco {objetivo} LUFS  "
          f"bajo voz {objetivo + DUCK_DB} LUFS  medido {_lufs(salida):.1f} LUFS integrado")


def _escribir(ruta, a):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR),
                          "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", ruta],
                         stdin=subprocess.PIPE)
    p.stdin.write(np.clip(a, -1, 1).astype(np.float32).tobytes())
    p.stdin.close()
    p.wait()


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    for c in spec:
        cama(c["pista"], c["salida"], c["dur"], [tuple(t) for t in c["voz"]],
             c.get("objetivo", -26.0), c.get("costura"))
