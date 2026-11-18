# -*- coding: utf-8 -*-
r"""Quita un tramo de un video de profe YA ENTREGADO sin volver a componer ni a codificar el resto (18 nov 2026).
Es el método de `reparchar.py` (copiar todo lo que no cambia, codificar solo lo que toca) aplicado a un corte.

**Para qué.** Al leer las transcripciones para los subtítulos aparecieron tomas repetidas sin cortar en tres videos
de unidad de Terminaciones anticipadas («ah, voy a volver a empezar»). Sebastián: «solo corta esas partes… para
evitar reprocesar todo».

    python recortar_entrega.py <plan> <versión vieja> <versión nueva> <a> <b> [lt=<clave>] [limpios=<n>]

Quita los cuadros [a, b) de la entrega vieja (cuadros de la línea, 23,976). Lo que queda:

- **Imagen.** Todo lo que está antes del último cuadro clave ≤ a y después del primer cuadro clave ≥ b se COPIA.
  Los bordes que no caen en un cuadro clave se vuelven a codificar con la receta de la entrega (mismo preset: mismos
  SPS/PPS), tomando los cuadros de la propia entrega vieja (el compuesto de estos videos va a 30 fps y no casa cuadro
  a cuadro con la línea).
- **`lt=<clave>`**: el corte se lleva el lower third (corte al principio del clip). El tramo que sigue al corte se
  codifica de nuevo con el lower third encima, en el mismo lugar relativo al arranque del clip, hasta el primer
  cuadro clave después de que sale.
- **`limpios=<n>`**: los primeros n cuadros después del corte traen en la entrega vieja la cola del lower third
  viejo. Se toman del compuesto, que no lo tiene: para cada uno se busca el cuadro del compuesto que más se parece
  (fuera de la zona del rótulo) y se informa el parecido.
- **Sonido.** Intro y outro salen de la entrega vieja; el tramo del clip, del compuesto (que es lo que suena en la
  línea), con los mismos cuadros quitados y un fundido de 12 ms en cada borde. AAC a 320 kb/s.

Verifica: cuadros = viejos − (b − a); SPS/PPS iguales en todas las partes; lo copiado, idéntico paquete a paquete;
pts seguidos; cuadro clave en cada empalme; decodificación completa; sonido (LUFS y pico) y sincronía contra el
compuesto. Deja una hoja con los cuadros de los empalmes. No borra nada: la entrega vieja queda donde está.

Log: `<P.TMP>/recortar.log`, que termina en «RECORTADO» o en «FALLO: …». Hoja: `<P.TMP>/recortar_hoja.jpg`.

NO toca Resolve: la línea sigue con la toma entera. El plan se corrige aparte (TRAMOS) para que la versión con
gráficos salga ya cortada.
"""
import glob
import importlib
import json
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
plan, V_OLD, V_NEW, A, B = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
OPC = dict(x.split('=', 1) for x in sys.argv[6:])
os.environ['DAE_PLAN'] = plan            # mp4_entrega toma de ahí el preset de la entrega
import mp4_entrega as M  # noqa: E402

for _r, _d, _f in os.walk(os.path.join(AQUI, '..', '..', 'cursos')):
    if plan + '.py' in _f:
        sys.path.insert(0, _r)
        break
P = importlib.import_module(plan)
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
FF, FP = FB + '/ffmpeg.exe', FB + '/ffprobe.exe'
FPS = 24000 / 1001.0
FR = '24000/1001'
SIN_PERDIDA = ['-c:v', 'libx264', '-qp', '0', '-preset', 'ultrafast', '-pix_fmt', 'yuv420p'] + M.COLOR
T = os.environ.get('DAE_TMP_RECORTE', P.TMP + '/recortar').rstrip('/') + '/'      # los tramos sin pérdida pesan: D: suele estar lleno
os.makedirs(T, exist_ok=True)
log = open(P.TMP + '/recortar.log', 'w', encoding='utf-8')


def p(*a):
    print(*a, file=log, flush=True)


def falla(m):
    p('FALLO: ' + m)
    raise SystemExit(1)


def run(c, **k):
    r = subprocess.run(c, capture_output=True, text=True, errors='replace', **k)
    if r.returncode:
        p('ERR', ' '.join(c)[:300], r.stderr[-600:])
    return r


def paquetes(f):
    r = run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=time_base', '-of', 'csv=p=0', f]).stdout.split()
    num, den = (int(x) for x in r[0].split('/'))
    r = run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'packet=pts,flags', '-of', 'csv=p=0', f]).stdout
    out = []
    for ln in r.split():
        c = ln.split(',')
        if len(c) >= 2 and c[0].lstrip('-').isdigit():
            out.append((int(c[0]) * num * 24000 / (den * 1001.0), 'K' in c[1]))
    return out


def md5_paquetes(f):
    r = run([FF, '-v', 'error', '-i', f, '-map', '0:v:0', '-c', 'copy', '-f', 'framemd5', '-']).stdout
    den, out = 24000, {}
    for ln in r.splitlines():
        if ln.startswith('#tb'):
            den = int(ln.split('/')[-1])
        elif ln and not ln.startswith('#'):
            c = [x.strip() for x in ln.split(',')]
            out[int(round(int(c[2]) * 24000 / (den * 1001.0)))] = (c[4], c[5])
    return out


def extradata(f):
    r = run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries',
             'stream=profile,level,pix_fmt,r_frame_rate,has_b_frames,color_space,extradata_hash', '-show_data_hash', 'md5',
             '-of', 'json', f]).stdout
    return json.loads(r)['streams'][0]


def grises(f, sel, w=480, h=270):
    """Cuadros elegidos (expresión de `select`), en gris y chicos, para comparar."""
    raw = subprocess.run([FF, '-v', 'error', '-i', f, '-an', '-vf', "select='%s',scale=%d:%d,format=gray" % (sel, w, h),
                          '-fps_mode', 'passthrough', '-f', 'rawvideo', '-'], capture_output=True).stdout
    n = len(raw) // (w * h)
    return np.frombuffer(raw[:n * w * h], dtype=np.uint8).reshape(n, h, w).astype(np.float32)


def cuadro_de(f, k, w, h):
    raw = subprocess.run([FF, '-v', 'error', '-ss', '%.4f' % (k / FPS - 0.004), '-i', f, '-frames:v', '1', '-vf', 'scale=%d:%d' % (w, h),
                          '-pix_fmt', 'rgb24', '-f', 'rawvideo', '-'], capture_output=True).stdout
    return Image.frombytes('RGB', (w, h), raw) if len(raw) == w * h * 3 else Image.new('RGB', (w, h), (90, 0, 0))


def pcm(f):
    raw = subprocess.run([FF, '-v', 'error', '-i', f, '-vn', '-ac', '2', '-ar', '48000', '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()


vieja = '%s/05 EXPORTS/%s.mp4' % (P.R, P.EXPORT % V_OLD)
nueva = '%s/05 EXPORTS/%s.mp4' % (P.R, P.EXPORT % V_NEW)
if os.path.exists(nueva):
    falla('ya existe ' + nueva)
if not os.path.exists(vieja):
    falla('no está ' + vieja)
CLIP0 = P.CLIP0
pk = paquetes(vieja)
largo = len(pk)
idr = sorted(int(round(a)) for a, b in pk if b)
CLIPF = largo - CLIP0 - 215 - 194              # cuadros del clip en la línea (cartón de cierre 215, outro 194)
if not (CLIP0 <= A < B <= CLIP0 + CLIPF):
    falla('el corte %d–%d no está dentro del clip (%d–%d)' % (A, B, CLIP0, CLIP0 + CLIPF))
quita = B - A
p('entrega vieja', os.path.basename(vieja), 'cuadros', largo, '| clip', CLIP0, CLIP0 + CLIPF, '| se quitan', A, B, '(%d cuadros, %.2f s)' % (quita, quita / FPS),
  '| preset', M.PRESET)

# ---------- 1. qué se copia y qué se codifica
k_a = max(k for k in idr if k <= A)             # hasta aquí se copia; [k_a, A) se codifica
LT = None
if 'lt' in OPC:
    it = {i[0]: i for i in P.ITEMS}.get(OPC['lt'])
    if not it or A != CLIP0:
        falla('lt= vale para un corte al principio del clip, y la clave tiene que estar en ITEMS')
    lt_ruta = '%s/02 CARTONES/%s_%s.mov' % (P.R, P.PREFIJO, OPC['lt'])
    lt_off = P.cuadro(it[2]) - CLIP0            # cuadros desde el arranque del clip hasta que entra el rótulo
    lt_dur = M.cuadros(lt_ruta)
    LT = (lt_ruta, lt_off, lt_dur)
    k_b = min(k for k in idr if k >= B + lt_off + lt_dur)
else:
    k_b = min(k for k in idr if k >= B)
LIMPIOS = int(OPC.get('limpios', 0))
p('se copia [0, %d) y [%d, %d) | se codifica [%d, %d) y [%d, %d)' % (k_a, k_b, largo, k_a, A, B, k_b), '| lower third', LT, '| limpios', LIMPIOS)
if A - k_a > 96 or k_b - B > 400:
    falla('cuadros clave raros alrededor del corte')


def extrae(nombre, f, sel, n):
    out = T + nombre
    run([FF, '-y', '-v', 'error', '-i', f, '-an', '-vf', "select='%s',setpts=N/(%s)/TB" % (sel, FR), '-frames:v', str(n), '-r', FR]
        + SIN_PERDIDA + [out])
    if M.cuadros(out) != n:
        falla('%s mide %d y tenía que medir %d' % (nombre, M.cuadros(out), n))
    return out


segs = []       # (archivo codificado, cuadros, etiqueta)
if A > k_a:
    izq = extrae('izq.mkv', vieja, r'between(n\,%d\,%d)' % (k_a, A - 1), A - k_a)
    run([FF, '-y', '-v', 'error', '-i', izq] + M.VIDEO + ['-an', '-f', 'mp4', T + 'izq.mp4'])
    segs.append((T + 'izq.mp4', A - k_a, 'izq'))
if k_b > B:
    entradas = []
    if LIMPIOS:
        # la entrega vieja trae en esos cuadros la cola del rótulo viejo: salen del compuesto
        vj = grises(vieja, r'between(n\,%d\,%d)' % (B, B + LIMPIOS + 5))
        fc = float(P.FPS_COMPUESTO) if getattr(P, 'FPS_COMPUESTO', None) and '/' not in str(P.FPS_COMPUESTO) else 30.0
        x0 = int((B - CLIP0) * fc / FPS) - 3
        cp = grises(P.COMPUESTO, r'between(n\,%d\,%d)' % (x0, x0 + int((LIMPIOS + 6) * fc / FPS) + 7))
        elegidos = []
        for j in range(len(vj)):
            # se compara la mitad de arriba del cuadro, donde no hay rótulo
            d = [float(((vj[j][:150] - c[:150]) ** 2).mean()) for c in cp]
            m = int(np.argmin(d))
            elegidos.append((B + j, x0 + m, 10 * np.log10(255.0 ** 2 / max(d[m], 1e-6)),
                             10 * np.log10(255.0 ** 2 / max(sorted(d)[1], 1e-6))))
        p('cuadro de la línea -> cuadro del compuesto (PSNR del elegido y del segundo):',
          ' '.join('%d->%d %.1f/%.1f' % e for e in elegidos))
        idx = [e[1] for e in elegidos[:LIMPIOS]]
        if any(b_ <= a_ for a_, b_ in zip(idx, idx[1:])) or min(e[2] for e in elegidos) < 30:
            falla('los cuadros limpios no casan con el compuesto')
        entradas.append(extrae('limpios.mkv', P.COMPUESTO, '+'.join(r'eq(n\,%d)' % c for c in idx), LIMPIOS))
    entradas.append(extrae('der.mkv', vieja, r'between(n\,%d\,%d)' % (B + LIMPIOS, k_b - 1), k_b - B - LIMPIOS))
    cmd = [FF, '-y', '-v', 'error']
    for e in entradas:
        cmd += ['-i', e]
    n_in = len(entradas)
    fg = ''.join('[%d:v]' % i for i in range(n_in)) + 'concat=n=%d:v=1:a=0,setpts=N/(%s)/TB[base]' % (n_in, FR) if n_in > 1 \
        else '[0:v]setpts=N/(%s)/TB[base]' % FR
    if LT:
        cmd += ['-i', LT[0]]
        # el rótulo es RGB con alfa: se pasa a YUV con la matriz 709 (la del video) y entra en su cuadro
        fg += ';[%d:v]scale=out_color_matrix=bt709:out_range=tv,format=yuva420p,setpts=PTS+%d/(%s)/TB[lt]' % (n_in, LT[1], FR)
        fg += ';[base][lt]overlay=0:0:eof_action=pass:format=yuv420[v]'
    else:
        fg += ';[base]null[v]'
    run(cmd + ['-filter_complex', fg, '-map', '[v]', '-frames:v', str(k_b - B), '-r', FR] + M.VIDEO + ['-an', '-f', 'mp4', T + 'der.mp4'])
    segs.append((T + 'der.mp4', k_b - B, 'der'))
for f, n, _e in segs:
    if M.cuadros(f) != n:
        falla('%s mide %d y tenía que medir %d' % (os.path.basename(f), M.cuadros(f), n))

# ---------- 2. lo copiado y todo pegado
partes = []      # (archivo, cuadros, primer cuadro en la entrega vieja o None si es nuevo)
if k_a > 0:
    f = T + 'copia0.mp4'
    run([FF, '-y', '-v', 'error', '-i', vieja, '-an', '-c:v', 'copy', '-frames:v', str(k_a), '-f', 'mp4', f])
    partes.append((f, k_a, 0))
for f, n, _e in segs:
    partes.append((f, n, None))
if k_b < largo:
    f = T + 'copia1.mp4'
    run([FF, '-y', '-v', 'error', '-ss', '%.6f' % (k_b / FPS + 0.004), '-i', vieja, '-an', '-c:v', 'copy',
         '-frames:v', str(largo - k_b), '-bsf:v', 'setts=pts=PTS-STARTPTS:dts=DTS-STARTPTS', '-f', 'mp4', f])
    partes.append((f, largo - k_b, k_b))
for f, n, _k in partes:
    if M.cuadros(f) != n:
        falla('%s mide %d y tenía que medir %d' % (os.path.basename(f), M.cuadros(f), n))
ex = [extradata(f) for f, _n, _k in partes]
p('partes', [(os.path.basename(f), n, k) for f, n, k in partes])
p('SPS/PPS', sorted({e.get('extradata_hash') for e in ex}), ex[0].get('profile'), ex[0].get('level'), ex[0].get('r_frame_rate'))
if len({json.dumps(e, sort_keys=True) for e in ex}) != 1:
    falla('las partes no tienen los mismos parámetros: %s' % ex)
with open(T + 'lista.txt', 'w', encoding='utf-8') as fl:
    for j, (f, n, _k) in enumerate(partes):
        fl.write("file '%s'\n" % f)
        if j < len(partes) - 1:
            fl.write('duration %.6f\n' % (n / FPS))
run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-auto_convert', '0', '-i', T + 'lista.txt', '-c', 'copy', '-f', 'mp4',
     T + 'imagen.mp4'])
nlargo = largo - quita

# ---------- 3. el sonido
M_ = 2002                                       # muestras por cuadro a 48 kHz
old, comp = pcm(vieja), pcm(P.COMPUESTO)
n_clip = CLIPF * M_
if len(comp) < n_clip:
    comp = np.vstack([comp, np.zeros((n_clip - len(comp), 2), dtype=np.float32)])
comp = comp[:n_clip]
fa = int(0.012 * 48000)
rampa = np.linspace(0.0, 1.0, fa, dtype=np.float32)[:, None]
izq_a = comp[:(A - CLIP0) * M_].copy()
der_a = comp[(B - CLIP0) * M_:].copy()
if len(izq_a) > fa:
    izq_a[-fa:] *= rampa[::-1]
der_a[:fa] *= rampa
nuevo = np.vstack([old[:CLIP0 * M_], izq_a, der_a, old[(CLIP0 + CLIPF) * M_:]])
if len(nuevo) < nlargo * M_:                    # el sonido mide lo mismo que la imagen, a la muestra
    nuevo = np.vstack([nuevo, np.zeros((nlargo * M_ - len(nuevo), 2), dtype=np.float32)])
nuevo = nuevo[:nlargo * M_]
p('sonido: %d muestras (%.3f s); imagen %.3f s' % (len(nuevo), len(nuevo) / 48000.0, nlargo / FPS))
enc = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'f32le', '-ar', '48000', '-ac', '2', '-i', '-', '-c:a', 'aac', '-b:a', '320k',
                        '-f', 'mp4', T + 'audio.m4a'], stdin=subprocess.PIPE)
enc.stdin.write(nuevo.tobytes())
enc.stdin.close()
if enc.wait():
    falla('no se pudo codificar el sonido')
tmp = nueva + '.parcial'
run([FF, '-y', '-v', 'error', '-i', T + 'imagen.mp4', '-i', T + 'audio.m4a', '-map', '0:v', '-map', '1:a', '-c', 'copy',
     '-movflags', '+faststart', '-f', 'mp4', tmp])

# ---------- 4. verificación
pn = paquetes(tmp)
ok_n = len(pn) == nlargo
orden = sorted(a for a, _b in pn)
k0 = min(a for a, _b in pk)
ok_pts = bool(orden) and all(abs(a - (k0 + i)) < 1e-3 for i, a in enumerate(orden))
claves_n = {int(round(a)) for a, b in pn if b}
empalmes, cur = [], 0
for f, n, _k in partes:
    if cur:
        empalmes.append(cur)
    cur += n
ok_emp = all(k in claves_n for k in empalmes)
p('cuadros', len(pn), '/ esperados', nlargo, 'OK' if ok_n else 'FALLA', '| pts seguidos', ok_pts, '| cuadro clave en los empalmes', ok_emp, empalmes)
a_, b_ = md5_paquetes(vieja), md5_paquetes(tmp)
copiados = list(range(0, k_a)) + list(range(k_b, largo))
ok_copia = all(a_.get(k) == b_.get(k if k < k_a else k - quita) and a_.get(k) for k in copiados)
p('lo copiado, idéntico paquete a paquete (%d cuadros de %d):' % (len(copiados), nlargo), ok_copia)
r = subprocess.run([FF, '-v', 'error', '-xerror', '-i', tmp, '-f', 'null', '-'], capture_output=True, text=True, errors='replace')
ok_dec = r.returncode == 0 and not r.stderr.strip()
p('decodificación completa: rc', r.returncode, 'errores', len(r.stderr.strip().splitlines()), r.stderr[-200:])
son = M.medir(tmp)
ok_son = 'Peak' in son and float(son['Peak']) <= -0.5 and -17.5 <= float(son['I']) <= -14.5
# sincronía: el sonido nuevo contra el compuesto, un minuto después del corte
na = pcm(tmp)
t_n = min(B - quita + 1440, nlargo - 215 - 194 - 600)       # cuadro de la entrega nueva
t_c = t_n - CLIP0 + (quita if t_n >= A else 0)               # el mismo momento en el compuesto
x, y = na[t_n * M_:(t_n + 240) * M_, 0], comp[t_c * M_ - 4800:(t_c + 240) * M_ + 4800, 0]
N = 1 << 20
cc = np.fft.irfft(np.fft.rfft(np.pad(y, (0, N - len(y)))) * np.conj(np.fft.rfft(np.pad(x, (0, N - len(x))))))
des = int(np.argmax(cc)) - 4800
ok_sinc = abs(des) <= 480
p('sonido', son, 'OK' if ok_son else 'FALLA', '| desfase contra el compuesto %d muestras (%.1f ms)' % (des, des / 48.0), 'OK' if ok_sinc else 'FALLA')
if not (ok_n and ok_pts and ok_emp and ok_copia and ok_dec and ok_son and ok_sinc):
    falla('la verificación no pasó; queda ' + tmp)
os.replace(tmp, nueva)
j = json.loads(run([FP, '-v', 'error', '-show_streams', '-of', 'json', nueva]).stdout)
v_ = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
p('entrega', os.path.basename(nueva), v_['codec_name'], v_.get('profile'), 'L%s' % v_.get('level'), '%dx%d' % (v_['width'], v_['height']),
  v_.get('color_space'), v_.get('r_frame_rate'), '%d cuadros' % nlargo, '%d MB' % (os.path.getsize(nueva) >> 20))

# hoja: los cuadros de alrededor de cada empalme y, si hay rótulo, antes, durante y al final
ks = []
for e in empalmes:
    ks += [('empalme -2', e - 2), ('empalme -1', e - 1), ('empalme', e), ('empalme +1', e + 1)]
if LT:
    ks += [('antes del rótulo', A + LT[1] - 1), ('rótulo', A + LT[1] + 40), ('rótulo', A + LT[1] + LT[2] - 30), ('después', A + LT[1] + LT[2] + 2)]
ks += [('corte -1', A - 1), ('corte', A), ('corte +12', A + 12), ('corte +36', A + 36)]
cols = 4
hoja = Image.new('RGB', (480 * cols, 290 * ((len(ks) + cols - 1) // cols)), (20, 20, 20))
dr = ImageDraw.Draw(hoja)
for i, (nom, k) in enumerate(ks):
    x_, y_ = 480 * (i % cols), 290 * (i // cols)
    if 0 <= k < nlargo:
        hoja.paste(cuadro_de(nueva, k, 480, 270), (x_, y_))
    dr.text((x_ + 4, y_ + 273), '%s  cuadro %d (%.2f s)' % (nom, k, k / FPS), fill=(255, 255, 0))
hoja.save(P.TMP + '/recortar_hoja.jpg', quality=90)
p('RECORTADO')
