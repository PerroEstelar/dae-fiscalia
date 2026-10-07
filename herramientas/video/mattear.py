#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta a la persona de un video con Robust Video Matting, en CPU.

Por que RVM y no un recortador por imagen: lleva estado recurrente entre
cuadros, asi que el borde no parpadea. Es lo que mata a los modelos tipo U2Net
cuando se usan cuadro a cuadro sobre pelo.

Sale un ProRes 4444 con alfa recto (sin premultiplicar), que es lo que Resolve
espera. El `fgr` que devuelve el modelo ya viene con el derrame de color del
fondo viejo descontado, asi que no hay que despillar aparte.
"""
import subprocess, sys, numpy as np, onnxruntime as ort, time, os

SRC = sys.argv[1]
OUT = sys.argv[2]
W, H, N = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
FPS = sys.argv[6]
# cuanto se reduce la imagen para el paso neuronal. RVM pide que el lado largo
# del reducido quede cerca de 512: aqui 832 * 0.6 = 499.
RATIO = float(sys.argv[7]) if len(sys.argv) > 7 else 0.6

ses = ort.InferenceSession("/home/claude/rvm/rvm.onnx", providers=["CPUExecutionProvider"])
rec = [np.zeros([1,1,1,1], dtype=np.float32)] * 4
dsr = np.array([RATIO], dtype=np.float32)

lee = subprocess.Popen(["ffmpeg","-v","error","-i",SRC,"-f","rawvideo","-pix_fmt","rgb24","-"],
                       stdout=subprocess.PIPE)
esc = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgba",
                        "-s","%dx%d"%(W,H),"-r",FPS,"-i","-",
                        "-c:v","prores_ks","-profile:v","4444","-pix_fmt","yuva444p10le",
                        "-alpha_bits","16","-vendor","apl0", OUT], stdin=subprocess.PIPE)

t0 = time.time()
for i in range(N):
    crudo = lee.stdout.read(W*H*3)
    if len(crudo) < W*H*3: break
    src = (np.frombuffer(crudo, np.uint8).reshape(H,W,3).astype(np.float32)/255.0
           ).transpose(2,0,1)[None]
    fgr, pha, *rec = ses.run([], {"src":src, "r1i":rec[0], "r2i":rec[1],
                                  "r3i":rec[2], "r4i":rec[3], "downsample_ratio":dsr})
    rgb = np.clip(fgr[0].transpose(1,2,0), 0, 1)
    a   = np.clip(pha[0,0], 0, 1)
    esc.stdin.write((np.dstack([rgb, a[...,None]])*255).astype(np.uint8).tobytes())
    if i % 100 == 0:
        v = (i+1)/max(time.time()-t0, 1e-6)
        print("  %4d/%d  %.1f cuadros/s  faltan ~%.0f s" % (i, N, v, (N-i)/max(v,1e-6)), flush=True)

esc.stdin.close(); esc.wait(); lee.wait()
print("listo: %s  %.1f MB  en %.0f s" % (os.path.basename(OUT), os.path.getsize(OUT)/1e6, time.time()-t0))
