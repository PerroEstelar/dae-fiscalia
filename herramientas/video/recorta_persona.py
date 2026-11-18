# -*- coding: utf-8 -*-
r"""Recorta a la persona de un video (Robust Video Matting, ONNX) y la compone sobre un fondo fijo.

Nació con los videos de avatar del curso de Trata (18 nov 2026): avatares verticales (1080×1920) en una
biblioteca generada, que Sebastián pidió «iguales al resto de videos de profe hablando a cámara»: la persona
recortada sobre el fondo DAE/Fiscalía con los logos a la izquierda y sin «Aprende con la DAE»
(`FONDO 4 V2.png`, de la carpeta de Drive «FONDOS SIN APRENDE CON LA DAE»).

De la fuente se toma un cuadrado (`--x --y --lado`), se lleva a 1080×1080 y se le pasa al modelo; la persona
queda apoyada en el borde inferior del cuadro de 1920×1080, con el centro del cuadrado en `--cx`. Salen dos
archivos:
- `<salida>`: el compuesto de 1920×1080 (H.264 CRF 14, BT.709) con el audio de la fuente copiado;
- `<salida sin .mp4>_mate.mp4`: el mate (alfa) de 1080×1080 en gris, para cambiar de fondo sin volver a recortar.

El modelo y onnxruntime-directml se instalaron con permiso de Sebastián (18 nov) en `D:\DAE\_herramientas\
matting` (modelos de github.com/PeterL1n/RobustVideoMatting, v1.0.0).

    python recorta_persona.py <fuente> <fondo> <salida.mp4> --y 100 [--x 0 --lado 1080 --cx 1250]
                              [--modelo resnet50|mobilenetv3] [--ratio 0.4] [--cpu] [--cuadros N] [--muestra t.jpg]
Log por salida estándar: una línea cada 500 cuadros y `LISTO <cuadros> <fps>`."""
import argparse, glob, os, subprocess, sys, time
import numpy as np

H = 'D:/DAE/_herramientas/matting/'
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
FF, FP = FB + '/ffmpeg.exe', FB + '/ffprobe.exe'
N = 1080

ap = argparse.ArgumentParser()
ap.add_argument('fuente'); ap.add_argument('fondo'); ap.add_argument('salida')
ap.add_argument('--x', type=int, default=0); ap.add_argument('--y', type=int, required=True)
ap.add_argument('--lado', type=int, default=1080); ap.add_argument('--cx', type=int, default=1250)
ap.add_argument('--modelo', default='resnet50'); ap.add_argument('--ratio', type=float, default=0.4)
ap.add_argument('--cpu', action='store_true'); ap.add_argument('--cuadros', type=int, default=0)
ap.add_argument('--desde', type=float, default=0.0); ap.add_argument('--muestra', default='')
a = ap.parse_args()

import onnxruntime as ort
from PIL import Image

so = ort.SessionOptions()
prov = ['CPUExecutionProvider'] if a.cpu else ['DmlExecutionProvider', 'CPUExecutionProvider']
if not a.cpu:
    so.enable_mem_pattern = False
    so.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
ses = ort.InferenceSession(H + 'rvm_%s_fp32.onnx' % a.modelo, so, providers=prov)
print('proveedores', ses.get_providers(), flush=True)

fps = subprocess.run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', a.fuente],
                     capture_output=True, text=True).stdout.strip().split()[0].strip(',')
fondo = np.asarray(Image.open(a.fondo).convert('RGB').resize((1920, 1080), Image.LANCZOS), dtype=np.uint8)
x0 = a.cx - N // 2
if x0 < 0 or x0 + N > 1920:
    raise SystemExit('el cuadrado se sale del cuadro: cx=%d' % a.cx)
bg = fondo[:, x0:x0 + N].astype(np.float32) / 255.0

esc = ',scale=%d:%d:flags=lanczos' % (N, N) if a.lado != N else ''
dec = subprocess.Popen([FF, '-v', 'error'] + (['-ss', '%.3f' % a.desde] if a.desde else []) + ['-i', a.fuente, '-vf',
                        'crop=%d:%d:%d:%d%s,scale=in_color_matrix=bt709:in_range=tv:out_range=pc,format=rgb24' % (a.lado, a.lado, a.x, a.y, esc),
                        '-f', 'rawvideo', '-'], stdout=subprocess.PIPE)
tmp = a.salida + '.parcial.mp4'
mate = os.path.splitext(a.salida)[0] + '_mate.mp4'
audio = ['-ss', '%.3f' % a.desde] if a.desde else []
enc = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', fps, '-i', '-'] + audio +
                       ['-i', a.fuente, '-map', '0:v', '-map', '1:a?', '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p',
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-colorspace', 'bt709', '-color_primaries', 'bt709',
                        '-color_trc', 'bt709', '-c:a', 'copy', '-shortest', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
encm = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'gray', '-s', '%dx%d' % (N, N), '-r', fps, '-i', '-',
                         '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-color_range', 'pc',
                         mate + '.parcial.mp4'], stdin=subprocess.PIPE)
rec = [np.zeros([1, 1, 1, 1], dtype=np.float32)] * 4
ratio = np.array([a.ratio], dtype=np.float32)
n, t0, t_inf = 0, time.time(), 0.0
cuadro = fondo.copy()
while True:
    b = dec.stdout.read(N * N * 3)
    if len(b) < N * N * 3:
        break
    src = np.frombuffer(b, np.uint8).reshape(N, N, 3)
    t = time.time()
    fgr, pha, *rec = ses.run(None, {'src': np.ascontiguousarray(src.transpose(2, 0, 1)[None].astype(np.float32) / 255.0),
                                    'r1i': rec[0], 'r2i': rec[1], 'r3i': rec[2], 'r4i': rec[3], 'downsample_ratio': ratio})
    t_inf += time.time() - t
    al = pha[0, 0][..., None]
    com = fgr[0].transpose(1, 2, 0) * al + bg * (1.0 - al)
    cuadro[:, x0:x0 + N] = np.clip(com * 255.0 + 0.5, 0, 255).astype(np.uint8)
    enc.stdin.write(cuadro.tobytes())
    encm.stdin.write(np.clip(pha[0, 0] * 255.0 + 0.5, 0, 255).astype(np.uint8).tobytes())
    n += 1
    if a.muestra and n == (a.cuadros or 60) // 2:
        Image.fromarray(cuadro).save(a.muestra, quality=90)
        Image.fromarray(np.clip(pha[0, 0] * 255, 0, 255).astype(np.uint8)).save(os.path.splitext(a.muestra)[0] + '_mate.jpg', quality=90)
    if n % 500 == 0:
        print('%d cuadros  %.1f fps  (modelo %.0f ms)' % (n, n / (time.time() - t0), 1000 * t_inf / n), flush=True)
    if a.cuadros and n >= a.cuadros:
        break
dec.kill()
enc.stdin.close(); encm.stdin.close()
enc.wait(); encm.wait()
os.replace(tmp, a.salida)
os.replace(mate + '.parcial.mp4', mate)
print('LISTO %d %.1f fps (modelo %.0f ms por cuadro)' % (n, n / (time.time() - t0), 1000 * t_inf / max(n, 1)), flush=True)
