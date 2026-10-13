#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajusta cada plano a la ranura que le dejó la voz.

Se corre con un manifiesto JSON: una lista de trabajos
    {"fuente": <ruta>, "modo": "loop"|"hold"|"loop_congela"|"camara",
     "frames": N, "inicio": cuadro de entrada del loop, "salida": <ruta>}

LOS CUATRO MODOS
    hold          una imagen fija estirada a N cuadros.
    loop          una ventana de N cuadros del loop, A VELOCIDAD NATIVA desde
                  `inicio`. Es el modo por defecto para video generado:
                  acelerar un Kling se nota mucho más que frenarlo, y frenarlo
                  se nota más que cortarlo.
    loop_congela  el loop entero a velocidad nativa y después su último cuadro
                  congelado hasta completar N.
    camara        una imagen fija con la cámara horneada: empuje o retroceso
                  lento más un pulso de mano. Para los planos que NO llevan
                  video generado.

Si la ranura pasa de los cuadros del loop y no se pide `loop_congela`, se usa
`setpts` con k = N × 1.001 / origen. El 1.001 es el paso de 24 a 23.976; sin él
se pierde un cuadro al final.

EL MODO CAMARA
    El plano se genera a 2560 de ancho y la línea es de 1920: sobra un 33%.
    Ese sobrante es el riel de la cámara. La ventana nunca baja de 1920 px de
    fuente, así que nunca se amplía un pixel.

    Parámetros por trabajo, todos opcionales:
      encuadre  ancho de la ventana al entrar, en fracción del plano (0.88)
      empuje    cuánto se cierra la ventana a lo largo de la ranura; positivo
                acerca, negativo aleja (0.0)
      deriva    [dx, dy] paneo total, en fracción del cuadro de salida
      centro    [cx, cy] centro de la ventana al entrar (0.5, 0.5)
      vibra     excursión máxima del pulso, en px de salida (6.0)
      semilla   entero; dos ranuras con semillas distintas no respiran igual.
                Si no se da, sale del nombre del archivo de salida.
      fase      corrimiento en segundos, por compatibilidad

EL PULSO DE MANO
    Tres bandas por eje, cada una con sus frecuencias sacadas al azar dentro de
    su rango y con fase propia:

      deriva   0.05 a 0.16 Hz, peso 0.46 — el cuerpo que sostiene la cámara
      meceo    0.40 a 0.95 Hz, peso 0.20 — la respiración
      temblor  2.00 a 3.60 Hz, peso 0.34 — el pulso fino

    Las tres hacen falta y la de arriba es la que más se olvida. Una suma de
    senos lentos da un dibujo bonito en el papel y en pantalla se ve rígida,
    porque el movimiento entre cuadro y cuadro queda por debajo del pixel: la
    imagen se queda quieta cuatro cuadros y salta uno. El temblor es lo que
    hace que cada cuadro sea distinto del anterior. Medido: con el temblor en
    0.34, el 79% de los cuadros se mueve más de medio pixel; con el temblor en
    0.18, sólo el 45%, y eso es exactamente lo que se siente tieso.

    Encima va una envolvente lenta, de 17 a 28 segundos de periodo, que sube y
    baja la amplitud: hay tramos más calmados y tramos más vivos. Sin eso la
    amplitud es constante y se siente mecánica por más que el dibujo no se
    repita.

    El eje vertical lleva componentes propias y pesa 0.72 del horizontal, como
    en una cámara en mano de verdad.

    La señal se normaliza por su excursión REAL en la ranura, no por la suma
    teórica de los pesos: con componentes lentas, una ranura corta no alcanza a
    recorrer su máximo y el pulso saldría mucho más chico de lo pedido.
"""
import hashlib
import json
import math
import os
import random
import subprocess
import sys

FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
FFPROBE = os.environ.get("FFPROBE", "ffprobe")
FPS = "24000/1001"
FPS_N = 23.976023976
ESCALA = "scale=1920:1080:flags=lanczos"
COMUNES = ["-an", "-c:v", "libx264", "-preset", "fast", "-crf", "14",
           "-pix_fmt", "yuv420p", "-g", "600", "-keyint_min", "600",
           "-sc_threshold", "0", "-r", FPS]

SALIDA_AN, SALIDA_AL = 1920, 1080
MARGEN = 1.002               # un pelo mas que 1:1, para no ampliar pixel
ESCALA_FUENTE = 2            # el plano se sube x2 una vez y de ahi sale todo
INTER_AN, INTER_AL = 2880, 1620
PESO_VERTICAL = 0.72
# (f_min, f_max, peso, componentes)
BANDAS = ((0.05, 0.16, 0.46, 2),   # deriva: el cuerpo que sostiene
          (0.40, 0.95, 0.20, 2),   # meceo: la respiracion
          (2.00, 3.60, 0.34, 2))   # temblor: lo que cambia cada cuadro


def cuadros(ruta):
    r = subprocess.run([FFPROBE, "-v", "error", "-count_frames",
                        "-select_streams", "v:0",
                        "-show_entries", "stream=nb_read_frames",
                        "-of", "json", ruta], capture_output=True, text=True)
    return int(json.loads(r.stdout)["streams"][0]["nb_read_frames"])


def medida(ruta):
    r = subprocess.run([FFPROBE, "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=width,height",
                        "-of", "json", ruta], capture_output=True, text=True)
    s = json.loads(r.stdout)["streams"][0]
    return int(s["width"]), int(s["height"])


def grande(src):
    """El plano subido x2, cacheado. zoompan redondea el recorte a entero:
    sobre el plano nativo un pixel de fuente son 0.85 px de salida y el pulso
    se cuantiza a escalones; sobre el plano x2 son 0.43 y el movimiento vuelve
    a ser continuo."""
    d = os.path.join(os.path.dirname(src), "_x%d" % ESCALA_FUENTE)
    dst = os.path.join(d, os.path.splitext(os.path.basename(src))[0] + ".png")
    if os.path.exists(dst):
        return dst
    os.makedirs(d, exist_ok=True)
    an, al = medida(src)
    r = subprocess.run([FFMPEG, "-v", "error", "-y", "-i", src, "-vf",
                        "scale=%d:%d:flags=lanczos" % (an * ESCALA_FUENTE,
                                                       al * ESCALA_FUENTE),
                        "-frames:v", "1", dst], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError("no se pudo subir %s: %s" % (src, r.stderr[:200]))
    return dst


def _componentes(r):
    """Tres bandas: deriva, meceo y temblor. Cada una con sus propias senos."""
    comp = []
    for fa, fb, peso, k in BANDAS:
        for _ in range(k):
            f = r.uniform(fa, fb)
            comp.append((f, peso / k, r.uniform(0, 2 * math.pi)))
    return comp


def _evaluar(comp, fe, pe, n, t0):
    """La señal cuadro a cuadro, con la envolvente lenta encima."""
    v = []
    for i in range(n):
        t = i / FPS_N + t0
        env = 0.65 + 0.35 * math.sin(2 * math.pi * fe * t + pe)
        v.append(env * sum(a * math.sin(2 * math.pi * f * t + p)
                           for f, a, p in comp))
    return v


def _senos(comp, k, tt, fe, pe, pe_amp):
    """La misma señal, escrita como expresión de ffmpeg."""
    senos = "+".join("%.5f*sin(2*PI*%.5f*%s+%.4f)" % (a, f, tt, p)
                     for f, a, p in comp)
    env = "(0.65+0.35*sin(2*PI*%.5f*%s+%.4f))" % (fe, tt, pe)
    return "(%.5f*%s*(%s))" % (k, env, senos)


def _vf_camara(t, an, al, n):
    enc = float(t.get("encuadre", 0.88))
    emp = float(t.get("empuje", 0.0))
    dx, dy = t.get("deriva", [0.0, 0.0])
    cx, cy = t.get("centro", [0.5, 0.5])
    vib = float(t.get("vibra", 6.0))
    fase = float(t.get("fase", 0.0))
    sem = t.get("semilla")
    if sem is None:
        base = os.path.basename(t.get("salida", "")).encode("utf-8")
        sem = int(hashlib.md5(base).hexdigest()[:8], 16)
    r = random.Random(int(sem))

    piso = SALIDA_AN * ESCALA_FUENTE / float(an) * MARGEN
    for w in (enc, enc * (1 - emp)):
        if w > 1.0 or w < piso:
            raise ValueError("ventana fuera de riel: %.3f (riel %.3f-1.0)"
                             % (w, piso))

    f = "(on/%d)" % max(n - 1, 1)
    wf = "(%.6f*(1-%.6f*%s))" % (enc, emp, f)
    cw = "(%d*%s)" % (an, wf)
    ch = "(%d*%s)" % (al, wf)
    esc = "(%s/%d)" % (cw, SALIDA_AN)          # px de salida -> px de fuente
    t0 = fase + r.uniform(0, 40)
    tt = "(on/%.6f+%.4f)" % (FPS_N, t0)

    # envolvente lenta: tramos mas calmados y tramos mas vivos
    fe = r.uniform(1 / 28.0, 1 / 17.0)
    pe = r.uniform(0, 2 * math.pi)

    # se normaliza por la excursion REAL de la ranura, no por la suma teorica:
    # con componentes lentas una ranura corta no alcanza a recorrer su maximo,
    # y sin esto el pulso sale mucho mas chico de lo pedido
    cmx = _componentes(r)
    cmy = _componentes(r)
    vx = _evaluar(cmx, fe, pe, n, t0)
    vy = _evaluar(cmy, fe, pe, n, t0)
    pico = max(max(abs(a) for a in vx), max(abs(b) for b in vy)) or 1.0
    kx = vib / pico
    ky = vib * PESO_VERTICAL / pico

    sx = "(%s*%s)" % (esc, _senos(cmx, kx, tt, fe, pe, 0))
    sy = "(%s*%s)" % (esc, _senos(cmy, ky, tt, fe, pe, 0))

    bx = "%.6f*%d-%s/2+%.6f*%s*%s+%s" % (cx, an, cw, dx, cw, f, sx)
    by = "%.6f*%d-%s/2+%.6f*%s*%s+%s" % (cy, al, ch, dy, ch, f, sy)
    x = "max(0,min(%d-%s,%s))" % (an, cw, bx)
    y = "max(0,min(%d-%s,%s))" % (al, ch, by)
    z = "1/%s" % wf

    return ("zoompan=z='%s':x='%s':y='%s':d=1:s=%dx%d:fps=%s,%s"
            % (z, x, y, INTER_AN, INTER_AL, FPS, ESCALA))


def ajustar(t):
    src, n, salida = t["fuente"], t["frames"], t["salida"]
    modo, ini = t.get("modo", "loop"), t.get("inicio", 0)
    os.makedirs(os.path.dirname(salida), exist_ok=True)

    if modo == "camara":
        src = grande(src)
        an, al = medida(src)
        vf = _vf_camara(t, an, al, n)
        cmd = [FFMPEG, "-v", "error", "-y", "-loop", "1", "-i", src,
               "-vf", vf, "-frames:v", str(n)] + COMUNES + [salida]
    elif modo == "hold":
        cmd = [FFMPEG, "-v", "error", "-y", "-loop", "1", "-i", src,
               "-vf", ESCALA, "-frames:v", str(n)] + COMUNES + [salida]
    else:
        orig = cuadros(src)
        disponible = orig - ini
        if n <= disponible:
            vf = ("trim=start_frame=%d,setpts=PTS-STARTPTS,fps=%s,%s"
                  % (ini, FPS, ESCALA))
        elif modo == "loop_congela":
            vf = ("trim=start_frame=%d,setpts=PTS-STARTPTS,fps=%s,%s,"
                  "tpad=stop_mode=clone:stop=%d" % (ini, FPS, ESCALA, n - disponible))
        else:
            k = n * 1.001 / disponible
            vf = ("trim=start_frame=%d,setpts=PTS-STARTPTS,setpts=%.6f*PTS,fps=%s,%s"
                  % (ini, k, FPS, ESCALA))
        cmd = [FFMPEG, "-v", "error", "-y", "-i", src,
               "-vf", vf, "-frames:v", str(n)] + COMUNES + [salida]

    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print("FALLO %s: %s" % (os.path.basename(salida), r.stderr[:200]))
        return False
    c = cuadros(salida)
    print("%-34s %4d / %4d  %s" % (os.path.basename(salida), c, n,
                                   "OK" if c == n else "DESCUADRADO"))
    return c == n


if __name__ == "__main__":
    trabajos = json.load(open(sys.argv[1], encoding="utf-8"))
    desde = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    hasta = int(sys.argv[3]) if len(sys.argv) > 3 else len(trabajos)
    malos = sum(0 if ajustar(t) else 1 for t in trabajos[desde:hasta])
    print("--- %d trabajos, %d con problema" % (hasta - desde, malos))
