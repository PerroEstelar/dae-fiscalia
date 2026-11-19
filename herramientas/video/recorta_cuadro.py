# -*- coding: utf-8 -*-
r"""Recorta a la persona de un video horizontal (Robust Video Matting, ONNX) y la compone sobre un fondo fijo.

Es `recorta_persona.py` sin el cuadrado: toma un rectángulo cualquiera de la fuente (por defecto, el cuadro
entero), lo escala y lo coloca donde se le diga. Nació con los videos de profe del curso de la Ley 1826 (19
nov 2026): un profe de frente, grabado en 1920×1080 con un fondo virtual de biblioteca, que Sebastián pidió
pasar al fondo de la Fiscalía. Con el cuadro entero las manos no se cortan en un cuadrado angosto: el único
borde recto que puede verse es el del propio cuadro de la fuente.

    python recorta_cuadro.py <fuente> <fondo> <salida.mp4> [--x 0 --y 0 --ancho 1920 --alto 1080]
                             [--escala 1.0] [--cx 1250] [--base 1080] [--modelo resnet50|mobilenetv3]
                             [--ratio 0.25] [--cpu] [--desde s] [--cuadros N] [--muestra t.jpg]

- El rectángulo (`--x --y --ancho --alto`) se escala por `--escala` y se le pasa al modelo a ese tamaño.
- Queda con su centro horizontal en `--cx` y su borde de abajo en `--base` (1080: apoyado en el piso del
  cuadro). Lo que cae fuera de 1920×1080 se pierde.
- Salen dos archivos, como en `recorta_persona.py`: `<salida>` (1920×1080, H.264 CRF 14, BT.709, con el audio
  de la fuente copiado y sin `-shortest`) y `<salida sin .mp4>_mate.mp4` (el alfa del rectángulo escalado).
- La fuente se lee como BT.709 de rango limitado (un 1080p sin etiqueta).
- `--ratio`: 0,25 para 1080p (lo que recomienda el modelo para HD); 0,4 para recortes de menos de 1080 de alto.

Los modelos y onnxruntime-directml están en `D:\DAE\_herramientas\matting` (instalados con permiso de
Sebastián el 17 nov 2026). Log por salida estándar: una línea cada 500 cuadros y `LISTO <cuadros> <fps>`."""
import argparse, glob, os, subprocess, time
import numpy as np

H = 'D:/DAE/_herramientas/matting/'
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
FF, FP = FB + '/ffmpeg.exe', FB + '/ffprobe.exe'
CW, CH = 1920, 1080

ap = argparse.ArgumentParser()
ap.add_argument('fuente'); ap.add_argument('fondo'); ap.add_argument('salida')
ap.add_argument('--x', type=int, default=0); ap.add_argument('--y', type=int, default=0)
ap.add_argument('--ancho', type=int, default=1920); ap.add_argument('--alto', type=int, default=1080)
ap.add_argument('--escala', type=float, default=1.0); ap.add_argument('--cx', type=int, default=1250)
ap.add_argument('--base', type=int, default=1080)
ap.add_argument('--modelo', default='resnet50'); ap.add_argument('--ratio', type=float, default=0.25)
ap.add_argument('--cpu', action='store_true'); ap.add_argument('--cuadros', type=int, default=0)
ap.add_argument('--desde', type=float, default=0.0); ap.add_argument('--muestra', default='')
a = ap.parse_args()

import onnxruntime as ort
from PIL import Image

W = int(round(a.ancho * a.escala / 2)) * 2
Hh = int(round(a.alto * a.escala / 2)) * 2
x0 = a.cx - W // 2                    # esquina del rectángulo escalado dentro del cuadro de salida
y0 = a.base - Hh
ax, bx = max(x0, 0), min(x0 + W, CW)  # la parte que cae dentro del cuadro
ay, by = max(y0, 0), min(y0 + Hh, CH)
if ax >= bx or ay >= by:
    raise SystemExit('el rectangulo cae fuera del cuadro')
print('modelo a %dx%d; en el cuadro: x %d-%d, y %d-%d' % (W, Hh, ax, bx, ay, by), flush=True)

so = ort.SessionOptions()
prov = ['CPUExecutionProvider'] if a.cpu else ['DmlExecutionProvider', 'CPUExecutionProvider']
if not a.cpu:
    so.enable_mem_pattern = False
    so.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
ses = ort.InferenceSession(H + 'rvm_%s_fp32.onnx' % a.modelo, so, providers=prov)
print('proveedores', ses.get_providers(), flush=True)

fps = subprocess.run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', a.fuente],
                     capture_output=True, text=True).stdout.strip().split()[0].strip(',')
fondo = np.asarray(Image.open(a.fondo).convert('RGB').resize((CW, CH), Image.LANCZOS), dtype=np.uint8)
bg = fondo[ay:by, ax:bx].astype(np.float32) / 255.0
sy, sx = slice(ay - y0, by - y0), slice(ax - x0, bx - x0)      # la misma parte, en el rectángulo escalado

esc = ',scale=%d:%d:flags=lanczos' % (W, Hh) if (W, Hh) != (a.ancho, a.alto) else ''
dec = subprocess.Popen([FF, '-v', 'error'] + (['-ss', '%.3f' % a.desde] if a.desde else []) + ['-i', a.fuente, '-vf',
                        'crop=%d:%d:%d:%d%s,scale=in_color_matrix=bt709:in_range=tv:out_range=pc,format=rgb24' % (a.ancho, a.alto, a.x, a.y, esc),
                        '-f', 'rawvideo', '-'], stdout=subprocess.PIPE)
tmp = a.salida + '.parcial.mp4'
mate = os.path.splitext(a.salida)[0] + '_mate.mp4'
audio = ['-ss', '%.3f' % a.desde] if a.desde else []
enc = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % (CW, CH), '-r', fps, '-i', '-'] + audio +
                       ['-i', a.fuente, '-map', '0:v', '-map', '1:a?', '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p',
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-colorspace', 'bt709', '-color_primaries', 'bt709',
                        '-color_trc', 'bt709', '-c:a', 'copy', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
encm = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'gray', '-s', '%dx%d' % (W, Hh), '-r', fps, '-i', '-',
                         '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-color_range', 'pc',
                         mate + '.parcial.mp4'], stdin=subprocess.PIPE)
rec = [np.zeros([1, 1, 1, 1], dtype=np.float32)] * 4
ratio = np.array([a.ratio], dtype=np.float32)
n, t0, t_inf = 0, time.time(), 0.0
cuadro = fondo.copy()
tam = W * Hh * 3
while True:
    b = dec.stdout.read(tam)
    if len(b) < tam:
        break
    src = np.frombuffer(b, np.uint8).reshape(Hh, W, 3)
    t = time.time()
    fgr, pha, *rec = ses.run(None, {'src': np.ascontiguousarray(src.transpose(2, 0, 1)[None].astype(np.float32) / 255.0),
                                    'r1i': rec[0], 'r2i': rec[1], 'r3i': rec[2], 'r4i': rec[3], 'downsample_ratio': ratio})
    t_inf += time.time() - t
    al = pha[0, 0][sy, sx][..., None]
    com = fgr[0].transpose(1, 2, 0)[sy, sx] * al + bg * (1.0 - al)
    cuadro[ay:by, ax:bx] = np.clip(com * 255.0 + 0.5, 0, 255).astype(np.uint8)
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
