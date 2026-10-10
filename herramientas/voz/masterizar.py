#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Masteriza una locución al estándar de la serie.

EL ESTÁNDAR
    −19 LUFS integrados · −1,0 dBTP · 48 kHz · 24 bits · estéreo dual-mono.

EL ORDEN IMPORTA
    remuestreo → dual-mono → medir → normalizar.  Si se pasa a dual-mono
    DESPUÉS de normalizar, la medida EBU R128 sube 3 dB y la pista queda a
    −16 LUFS: ese fue el error que arrastraban las primeras piezas.

USO
    masterizar.py entrada.mp3 salida.wav [objetivo]
    masterizar.py --lote carpeta_entrada carpeta_salida
"""
import json, os, re, subprocess, sys

FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
CADENA = "aresample=48000:resampler=soxr:precision=28,pan=stereo|c0=c0|c1=c0"
OBJETIVO, TECHO, RANGO = -19.0, -1.0, 11.0


def _medir(entrada, objetivo):
    cmd = [FFMPEG, "-nostats", "-i", entrada, "-af",
           "%s,loudnorm=I=%.1f:TP=%.1f:LRA=%.1f:print_format=json"
           % (CADENA, objetivo, TECHO, RANGO), "-f", "null", "-"]
    err = subprocess.run(cmd, capture_output=True, text=True).stderr
    bloque = err[err.rindex("{"):err.rindex("}") + 1]
    return json.loads(bloque)


def _lufs(ruta):
    err = subprocess.run([FFMPEG, "-nostats", "-i", ruta, "-af", "ebur128=peak=true",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    ls = err.splitlines()
    i = max(k for k, l in enumerate(ls) if "Integrated loudness" in l)
    lufs = tp = None
    for s in ls[i:i + 12]:
        s = s.strip()
        if s.startswith("I:") and lufs is None:
            lufs = float(s.split()[1])
        if s.startswith("Peak:") and tp is None:
            tp = float(s.split()[1])
    return lufs, tp


def masterizar(entrada, salida, objetivo=OBJETIVO):
    m = _medir(entrada, objetivo)
    cmd = [FFMPEG, "-v", "error", "-y", "-i", entrada, "-af",
           "%s,loudnorm=I=%.1f:TP=%.1f:LRA=%.1f:measured_I=%s:measured_TP=%s:"
           "measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true"
           % (CADENA, objetivo, TECHO, RANGO, m["input_i"], m["input_tp"],
              m["input_lra"], m["input_thresh"], m["target_offset"]),
           "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le", salida]
    subprocess.run(cmd, check=True)
    lufs, tp = _lufs(salida)
    print("%-26s  %6.1f LUFS  %5.1f dBTP" % (os.path.basename(salida), lufs, tp))
    return lufs, tp


if __name__ == "__main__":
    if sys.argv[1] == "--lote":
        ent, sal = sys.argv[2], sys.argv[3]
        os.makedirs(sal, exist_ok=True)
        for f in sorted(os.listdir(ent)):
            if f.lower().endswith((".mp3", ".wav")):
                masterizar(os.path.join(ent, f),
                           os.path.join(sal, os.path.splitext(f)[0] + ".wav"))
    else:
        masterizar(sys.argv[1], sys.argv[2],
                   float(sys.argv[3]) if len(sys.argv) > 3 else OBJETIVO)
