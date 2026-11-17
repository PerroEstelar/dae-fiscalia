# -*- coding: utf-8 -*-
r"""Cambia el cartón de título de un video de profe ya entregado, sin volver a rendir el cuerpo
(17 nov 2026).

**Para qué.** Los 12 videos de profe de Enfoque diferencial salieron con el título «Enfoque
diferencial en la práctica del fiscal» y el curso se llama «Enfoque diferencial». El título va en
dos sitios de la línea, con el mismo archivo: al principio (cuadros 194–408, V2) y en el cierre
(los 215 cuadros que siguen al cuerpo, V1). Volver a rendir y codificar los 12 son 2 h 12 min de
video a tiempo real; el cuerpo no cambia.

**Qué hace**, para un plan cuyo `TITULO` ya apunta al cartón nuevo (rendido con
`ic_pieza.py titulo`):

1. En Resolve, `ReplaceClip` del medio del cartón viejo por el nuevo: los dos ítems de la línea
   quedan con el título nuevo y todo lo demás igual. Comprueba que la línea mide lo mismo.
2. Mira en la entrega vieja que haya un cuadro clave (IDR) justo en el 409, donde empieza el
   cuerpo, y justo donde termina (largo − 409). x264 los pone ahí porque son cambios de plano.
   Si falta alguno, no sigue: ese video va por el camino largo (`profe_entrega`).
3. Rinde en Resolve solo la cabeza (cuadros 0–408: intro y título) y la cola (cierre y outro),
   con los ajustes del máster de `mp4_entrega` (H.264 NVIDIA, 80000), y las codifica con la
   receta de entrega (`mp4_entrega.VIDEO`).
4. Copia el cuerpo de la entrega vieja sin recodificar, pega cabeza + cuerpo + cola con el
   demuxer `concat` y le pone el audio de la entrega vieja, tal cual.
5. Verifica: cuadros = línea; SPS/PPS iguales en las tres partes; el cuerpo, cuadro a cuadro,
   idéntico al de la entrega vieja (`framemd5`); pts seguidos de punta a punta; audio idéntico
   (md5 de los paquetes); decodificación completa sin errores; PSNR de la cabeza y la cola
   contra lo que rindió Resolve. Deja una hoja con cuadros del título, del cierre y de los
   empalmes.
6. Vuelve a exportar el `.drt` (el anterior va a `_descartes`).

    python retitular.py plan_ed1p <ruta del cartón viejo> <versión vieja> <versión nueva>

Log: `<P.TMP>/retitular.log`, que termina en «RETITULADO» o en «FALLO: …». No borra nada: la
entrega vieja y el cartón viejo quedan donde están.
"""
import glob
import importlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mp4_entrega as M  # noqa: E402

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
FF, FP = FB + '/ffmpeg.exe', FB + '/ffprobe.exe'
FPS = 24000 / 1001.0
CLIP0, TIT_DUR, INTRO_DUR = 409, 215, 194

plan, VIEJO, V_OLD, V_NEW = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
for _r, _d, _f in os.walk(os.path.join(AQUI, '..', '..', 'cursos')):
    if plan + '.py' in _f:
        sys.path.insert(0, _r)
        break
P = importlib.import_module(plan)
T = P.TMP + '/retitular/'
os.makedirs(T, exist_ok=True)
log = open(P.TMP + '/retitular.log', 'w', encoding='utf-8')


def p(*a):
    print(*a, file=log, flush=True)


def falla(m):
    p('FALLO: ' + m)
    raise SystemExit(1)


def run(c, **k):
    r = subprocess.run(c, capture_output=True, text=True, errors='replace', **k)
    if r.returncode:
        p('ERR', ' '.join(c)[:240], r.stderr[-600:])
    return r


def norm(x):
    return os.path.normcase(os.path.normpath(x))


def paquetes(f):
    """Los paquetes de video: [(cuadro, es clave)], con el cuadro como número real (pts sobre la
    rejilla de 23,976). Si un pts no cae en la rejilla, el número no es entero."""
    r = run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=time_base', '-of', 'csv=p=0', f]).stdout.split()
    num, den = (int(x) for x in r[0].split('/'))
    r = run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'packet=pts,flags', '-of', 'csv=p=0', f]).stdout
    out = []
    for ln in r.split():
        c = ln.split(',')
        if len(c) >= 2 and c[0].lstrip('-').isdigit():
            out.append((int(c[0]) * num * 24000 / (den * 1001.0), 'K' in c[1]))
    return out


def md5_cuadros(f):
    r = run([FF, '-v', 'error', '-i', f, '-an', '-f', 'framemd5', '-']).stdout
    return [x.split(',')[-1].strip() for x in r.splitlines() if x and not x.startswith('#')]


def extradata(f):
    r = run([FP, '-v', 'error', '-select_streams', 'v:0', '-show_entries',
             'stream=profile,level,pix_fmt,r_frame_rate,has_b_frames,color_space,extradata_hash', '-show_data_hash', 'md5',
             '-of', 'json', f]).stdout
    return json.loads(r)['streams'][0]


def md5_audio(f):
    return run([FF, '-v', 'error', '-i', f, '-map', '0:a', '-c', 'copy', '-f', 'md5', '-']).stdout.strip()


vieja = '%s/05 EXPORTS/%s.mp4' % (P.R, P.EXPORT % V_OLD)
nueva = '%s/05 EXPORTS/%s.mp4' % (P.R, P.EXPORT % V_NEW)
if os.path.exists(nueva):
    falla('ya existe ' + nueva)
for f in (vieja, P.TITULO, VIEJO):
    if not os.path.exists(f):
        falla('no está ' + f)

# ---------- 1. Resolve: el cartón nuevo en la línea
import DaVinciResolveScript as dvr  # noqa: E402

resolve = dvr.scriptapp('Resolve')
pm = resolve.GetProjectManager()
pr = pm.GetCurrentProject()
tl = None
for i in range(1, int(pr.GetTimelineCount()) + 1):
    t = pr.GetTimelineByIndex(i)
    if t.GetName() == P.NOMBRE_LINEA:
        tl = t
if tl is None:
    falla('no está la línea ' + P.NOMBRE_LINEA)
t0 = tl.GetStartFrame()
largo = tl.GetEndFrame() - t0
fin = largo - CLIP0          # primer cuadro del cierre


def titulos():
    out = []
    for n in (1, 2):
        for it in tl.GetItemListInTrack('video', n) or []:
            m = it.GetMediaPoolItem()
            ruta = norm(m.GetClipProperty('File Path') or '') if m else ''
            if ruta in (norm(VIEJO), norm(P.TITULO)):
                out.append((n, it.GetStart() - t0, it.GetEnd() - it.GetStart(), ruta, m))
    return sorted(out, key=lambda x: x[1])


antes = titulos()
p('línea', P.NOMBRE_LINEA, 'largo', largo, 'títulos', [(a, b, c, os.path.basename(d)) for a, b, c, d, _m in antes])
if [(b, c) for _a, b, c, _d, _m in antes] != [(INTRO_DUR, TIT_DUR), (fin, TIT_DUR)]:
    falla('los cartones de título no están en 194 y en %d con 215 cuadros' % fin)
for _n, _b, _c, ruta, m in antes:
    if ruta == norm(VIEJO):
        ok = m.ReplaceClip(os.path.normpath(P.TITULO))
        p('ReplaceClip', ok)
        break
despues = titulos()
if [(a, b, c) for a, b, c, _d, _m in despues] != [(a, b, c) for a, b, c, _d, _m in antes] or \
        any(d != norm(P.TITULO) for _a, _b, _c, d, _m in despues) or tl.GetEndFrame() - t0 != largo:
    falla('la línea cambió al reemplazar el cartón: %s' % [(a, b, c, os.path.basename(d)) for a, b, c, d, _m in despues])
p('cartón nuevo en la línea:', os.path.basename(P.TITULO), 'largo', tl.GetEndFrame() - t0)

# ---------- 2. la entrega vieja: cuadros y cuadros clave
pk = paquetes(vieja)
if len(pk) != largo:
    falla('la entrega vieja mide %d y la línea %d' % (len(pk), largo))
idr = sorted(int(round(a)) for a, b in pk if b)
if CLIP0 not in idr or fin not in idr:
    falla('la entrega vieja no tiene cuadro clave en %d y en %d (cerca: %s / %s)' % (
        CLIP0, fin, [k for k in idr if abs(k - CLIP0) < 60], [k for k in idr if abs(k - fin) < 60]))
p('entrega vieja', os.path.basename(vieja), 'cuadros', len(pk), 'cuadro clave en', CLIP0, 'y en', fin)

# ---------- 3. cabeza y cola: Resolve y x264
pr.SetCurrentTimeline(tl)
resolve.OpenPage('deliver')


def rinde(nombre, a, b):
    for viejo_ in glob.glob(T + nombre + '*'):
        os.remove(viejo_)
    pr.DeleteAllRenderJobs()
    okf = pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    ok = pr.SetRenderSettings({'SelectAllFrames': False, 'MarkIn': t0 + a, 'MarkOut': t0 + b - 1,
                               'TargetDir': os.path.normpath(T), 'CustomName': nombre,
                               'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': 23.976,
                               'VideoQuality': 80000, 'AudioCodec': 'aac', 'AudioSampleRate': 48000,
                               'ExportVideo': True, 'ExportAudio': True})
    job = pr.AddRenderJob()
    pr.StartRendering([job])
    while pr.IsRenderingInProgress():
        time.sleep(1)
    st = pr.GetRenderJobStatus(job)
    p('render', nombre, a, b, okf, ok, st.get('JobStatus'), st.get('CompletionPercentage'))


try:
    rinde('cabeza_master', 0, CLIP0)
    rinde('cola_master', fin, largo)
finally:
    # los ajustes de render son del proyecto: se devuelven en el acto
    pr.DeleteAllRenderJobs()
    pr.SetRenderSettings({'SelectAllFrames': True, 'ExportVideo': True, 'ExportAudio': True})
    resolve.OpenPage('edit')
time.sleep(12)                  # el mp4 recién terminado puede no tener todavía el moov
for nombre, n in (('cabeza', CLIP0), ('cola', largo - fin)):
    m = T + nombre + '_master.mp4'
    if M.cuadros(m) != n:
        falla('%s_master mide %d y tenía que medir %d' % (nombre, M.cuadros(m), n))
    if os.path.exists(T + nombre + '.mp4'):
        os.remove(T + nombre + '.mp4')
    run([FF, '-y', '-v', 'error', '-i', m] + M.VIDEO + ['-an', '-f', 'mp4', T + nombre + '.mp4'])
    r = run([FF, '-hide_banner', '-nostats', '-i', T + nombre + '.mp4', '-i', m, '-lavfi', '[0:v][1:v]psnr', '-f', 'null', '-']).stderr
    p(nombre, 'cuadros', M.cuadros(T + nombre + '.mp4'), 'psnr contra Resolve', (re.findall(r'average:[\d.]+ min:[\d.]+', r) or ['?'])[-1])

# ---------- 4. cuerpo copiado y pegado
n_cuerpo = fin - CLIP0
if os.path.exists(T + 'cuerpo.mp4'):
    os.remove(T + 'cuerpo.mp4')
run([FF, '-y', '-v', 'error', '-ss', '%.6f' % (CLIP0 / FPS + 0.004), '-i', vieja, '-an', '-c:v', 'copy',
     '-frames:v', str(n_cuerpo), '-f', 'mp4', T + 'cuerpo.mp4'])
if M.cuadros(T + 'cuerpo.mp4') != n_cuerpo:
    falla('el cuerpo copiado mide %d y tenía que medir %d' % (M.cuadros(T + 'cuerpo.mp4'), n_cuerpo))
ex = [extradata(T + x) for x in ('cabeza.mp4', 'cuerpo.mp4', 'cola.mp4')]
p('SPS/PPS', [e.get('extradata_hash') for e in ex], ex[0].get('profile'), ex[0].get('level'), ex[0].get('has_b_frames'),
  ex[0].get('r_frame_rate'))
if len({json.dumps(e, sort_keys=True) for e in ex}) != 1:
    falla('las tres partes no tienen los mismos parámetros: %s' % ex)
open(T + 'lista.txt', 'w', encoding='utf-8').write(
    "file '%scabeza.mp4'\nduration %.6f\nfile '%scuerpo.mp4'\nduration %.6f\nfile '%scola.mp4'\n"
    % (T, CLIP0 / FPS, T, n_cuerpo / FPS, T))
run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', T + 'lista.txt', '-c', 'copy', '-f', 'mp4', T + 'imagen.mp4'])
run([FF, '-y', '-v', 'error', '-i', T + 'imagen.mp4', '-i', vieja, '-map', '0:v', '-map', '1:a', '-c', 'copy',
     '-movflags', '+faststart', '-f', 'mp4', nueva + '.parcial'])

# ---------- 5. verificación
tmp = nueva + '.parcial'
pn = paquetes(tmp)
ok_n = len(pn) == largo
orden = sorted(a for a, _b in pn)
k0 = min(a for a, _b in pk)
ok_pts = bool(orden) and all(abs(a - (k0 + i)) < 1e-3 for i, a in enumerate(orden))
p('cuadros', len(pn), '/ línea', largo, 'OK' if ok_n else 'FALLA', '| pts seguidos y en la rejilla', ok_pts, 'primero', orden[0] if orden else None,
  '| claves en los empalmes', [k for k in sorted(int(round(a)) for a, b in pn if b) if k in (0, CLIP0, fin)])
a, b = md5_cuadros(vieja), md5_cuadros(tmp)
ok_cuerpo = len(a) == len(b) == largo and a[CLIP0:fin] == b[CLIP0:fin]
dif_cab = sum(1 for x, y in zip(a[:CLIP0], b[:CLIP0]) if x != y)
dif_col = sum(1 for x, y in zip(a[fin:], b[fin:]) if x != y)
p('cuerpo idéntico cuadro a cuadro (%d cuadros):' % n_cuerpo, ok_cuerpo, '| cuadros que cambian en la cabeza', dif_cab, 'y en la cola', dif_col)
ma, mb = md5_audio(vieja), md5_audio(tmp)
p('audio idéntico:', ma == mb and bool(ma), ma)
r = subprocess.run([FF, '-v', 'error', '-xerror', '-i', tmp, '-f', 'null', '-'], capture_output=True, text=True, errors='replace')
ok_dec = r.returncode == 0 and not r.stderr.strip()
p('decodificación completa: rc', r.returncode, 'errores', len(r.stderr.strip().splitlines()), r.stderr[-200:])
if not (ok_n and ok_pts and ok_cuerpo and ma == mb and ma and ok_dec):
    falla('la verificación no pasó; queda ' + tmp)
os.replace(tmp, nueva)
j = json.loads(run([FP, '-v', 'error', '-show_streams', '-of', 'json', nueva]).stdout)
v_ = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
p('entrega', os.path.basename(nueva), v_['codec_name'], v_.get('profile'), 'L%s' % v_.get('level'), '%dx%d' % (v_['width'], v_['height']),
  v_.get('color_space'), v_.get('r_frame_rate'), '%d MB' % (os.path.getsize(nueva) >> 20), 'sonido', M.medir(nueva))

# hoja: título, cierre y los cuatro empalmes
pts = [('título', INTRO_DUR + 110), ('título fin', CLIP0 - 1), ('cuerpo', CLIP0), ('cuerpo fin', fin - 1), ('cierre', fin),
       ('cierre', fin + 110), ('outro', fin + TIT_DUR), ('outro', largo - 60)]
hoja = Image.new('RGB', (480 * 4, 290 * 2), (20, 20, 20))
dr = ImageDraw.Draw(hoja)
for i, (nom, k) in enumerate(pts):
    raw = subprocess.run([FF, '-v', 'error', '-ss', '%.4f' % (k / FPS - 0.004), '-i', nueva, '-frames:v', '1', '-vf', 'scale=480:270',
                          '-pix_fmt', 'rgb24', '-f', 'rawvideo', '-'], capture_output=True).stdout
    if len(raw) == 480 * 270 * 3:
        hoja.paste(Image.frombytes('RGB', (480, 270), raw), ((i % 4) * 480, (i // 4) * 290))
    dr.text(((i % 4) * 480 + 4, (i // 4) * 290 + 272), '%s %d' % (nom, k), fill=(255, 255, 0))
hoja.save(P.TMP + '/retitular_hoja.jpg', quality=88)

# ---------- 6. el .drt
drt = '%s/10 TIMELINE SEBASTIAN/%s.drt' % (P.R, P.NOMBRE_LINEA)
if os.path.exists(drt):
    d = os.path.dirname(drt) + '/_descartes'
    os.makedirs(d, exist_ok=True)
    shutil.move(drt, '%s/%s (titulo anterior).drt' % (d, P.NOMBRE_LINEA))
p('drt', tl.Export(os.path.normpath(drt), resolve.EXPORT_DRT))
pm.SaveProject()
p('RETITULADO')
