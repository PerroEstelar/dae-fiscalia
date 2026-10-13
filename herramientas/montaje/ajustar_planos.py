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
                  congelado hasta completar N. Para cuando la ranura es más
                  larga que el loop y el gesto ya terminó.
    camara        una imagen fija con la cámara horneada: empuje o retroceso
                  lento (zoom dinámico) más una vibración de pulso muy baja.
                  Para los planos que NO llevan video generado.

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
      vibra     excursión de la vibración, en px de salida (2.0)
      fase      corrimiento de la vibración en segundos; sirve para que el
                mismo plano en dos ranuras distintas no respire igual

    La vibración son tres senos de frecuencias sin razón entera sumados, así
    que no se repite a la vista. Y además resuelve el escalón de zoompan: los
    recortes se redondean a entero, y un paneo lento sin vibración salta cada
    cuatro o cinco cuadros. Con la vibración encima, x e y cambian en todos
    los cuadros y el escalón se disuelve.
"""
import json
import os
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
PICO_SENOS = 1.9             # el pico de la suma de los tres senos


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


def _vf_camara(t, an, al, n):
    enc = float(t.get("encuadre", 0.88))
    emp = float(t.get("empuje", 0.0))
    dx, dy = t.get("deriva", [0.0, 0.0])
    cx, cy = t.get("centro", [0.5, 0.5])
    vib = float(t.get("vibra", 2.0)) / PICO_SENOS
    fase = float(t.get("fase", 0.0))

    # la ventana no puede salirse del rango util en ningun punto del barrido
    piso = SALIDA_AN / float(an) * MARGEN
    for w in (enc, enc * (1 - emp)):
        if w > 1.0 or w < piso:
            raise ValueError("ventana fuera de riel: %.3f (riel %.3f-1.0)"
                             % (w, piso))

    f = "(on/%d)" % max(n - 1, 1)
    wf = "(%.6f*(1-%.6f*%s))" % (enc, emp, f)
    cw = "(%d*%s)" % (an, wf)
    ch = "(%d*%s)" % (al, wf)
    esc = "(%s/%d)" % (cw, SALIDA_AN)          # px de salida -> px de fuente
    tt = "(on/%.6f+%.4f)" % (FPS_N, fase)
    sx = ("(%.5f*%s*(sin(2*PI*0.37*%s)+0.6*sin(2*PI*0.61*%s+1.1)"
          "+0.3*sin(2*PI*1.27*%s+2.3)))" % (vib, esc, tt, tt, tt))
    sy = ("(%.5f*%s*(sin(2*PI*0.29*%s+0.7)+0.6*sin(2*PI*0.53*%s+2.6)"
          "+0.3*sin(2*PI*1.09*%s+0.4)))" % (vib, esc, tt, tt, tt))

    bx = "%.6f*%d-%s/2+%.6f*%s*%s+%s" % (cx, an, cw, dx, cw, f, sx)
    by = "%.6f*%d-%s/2+%.6f*%s*%s+%s" % (cy, al, ch, dy, ch, f, sy)
    x = "max(0,min(%d-%s,%s))" % (an, cw, bx)
    y = "max(0,min(%d-%s,%s))" % (al, ch, by)
    z = "1/%s" % wf

    return ("zoompan=z='%s':x='%s':y='%s':d=1:s=%dx%d:fps=%s"
            % (z, x, y, SALIDA_AN, SALIDA_AL, FPS))


def ajustar(t):
    src, n, salida = t["fuente"], t["frames"], t["salida"]
    modo, ini = t.get("modo", "loop"), t.get("inicio", 0)
    os.makedirs(os.path.dirname(salida), exist_ok=True)

    if modo == "camara":
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
            # el loop completo y después su último cuadro quieto
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
