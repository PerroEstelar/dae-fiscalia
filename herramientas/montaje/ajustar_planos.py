#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajusta cada plano a la ranura que le dejó la voz.

Se corre con un manifiesto JSON: una lista de trabajos
    {"fuente": <ruta>, "modo": "loop"|"hold"|"loop_congela", "frames": N,
     "inicio": cuadro de entrada del loop, "salida": <ruta>}

LOS TRES MODOS
    hold          una imagen fija estirada a N cuadros.
    loop          una ventana de N cuadros del loop, A VELOCIDAD NATIVA desde
                  `inicio`. Es el modo por defecto: acelerar un Kling se nota
                  mucho más que frenarlo, y frenarlo se nota más que cortarlo.
    loop_congela  el loop entero a velocidad nativa y después su último cuadro
                  congelado hasta completar N. Para cuando la ranura es más
                  larga que el loop y el gesto ya terminó: en vez de arrastrar
                  el movimiento, se deja reposar.

Si la ranura pasa de los cuadros del loop y no se pide `loop_congela`, se usa
`setpts` con k = N × 1.001 / origen. El 1.001 es el paso de 24 a 23.976; sin él
se pierde un cuadro al final.

Todo sale a 1920×1080 con lanczos en el encode, no en la línea, para que Resolve
no reescale cuadro a cuadro.
"""
import json
import os
import subprocess
import sys

FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
FFPROBE = os.environ.get("FFPROBE", "ffprobe")
FPS = "24000/1001"
ESCALA = "scale=1920:1080:flags=lanczos"
COMUNES = ["-an", "-c:v", "libx264", "-preset", "fast", "-crf", "14",
           "-pix_fmt", "yuv420p", "-g", "600", "-keyint_min", "600",
           "-sc_threshold", "0", "-r", FPS]


def cuadros(ruta):
    r = subprocess.run([FFPROBE, "-v", "error", "-count_frames",
                        "-select_streams", "v:0",
                        "-show_entries", "stream=nb_read_frames",
                        "-of", "json", ruta], capture_output=True, text=True)
    return int(json.loads(r.stdout)["streams"][0]["nb_read_frames"])


def ajustar(t):
    src, n, salida = t["fuente"], t["frames"], t["salida"]
    modo, ini = t.get("modo", "loop"), t.get("inicio", 0)
    os.makedirs(os.path.dirname(salida), exist_ok=True)

    if modo == "hold":
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
