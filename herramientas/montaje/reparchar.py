# -*- coding: utf-8 -*-
r"""Cambia uno o varios cartones del cuerpo de un video de profe ya entregado, sin volver a rendir
ni a codificar el resto (17 nov 2026). Es `retitular.py` para tramos de adentro.

**Para qué.** Sebastián, con los 12 videos de Enfoque diferencial entregados: «en vez de "unas
lentes" que diga "unos lentes"… revisa los guiones antes de entregar el paquete entero». La
revisión dio seis cartones en cinco videos, cuatro de ellos de 22 a 28 minutos. Cada cartón dura
de 9 a 15 segundos.

**Qué hace**, para un plan que ya trae el texto corregido y `VERSIONES = {clave: n}`, con el
cartón nuevo rendido (`ic_pieza.py cartones <clave>` lo deja como «<PREFIJO>_<clave> v<n>.mov»):

1. En Resolve, `ReplaceClip` del medio del cartón viejo por el nuevo. Comprueba que el ítem
   sigue en su cuadro, con su largo, y que la línea mide lo mismo.
2. Busca en la entrega vieja los cuadros clave (IDR) que encierran cada cartón: el último antes
   de que entre y el primero después de que salga (`keyint=48`: hay uno cada 2 s como mucho). Los
   tramos que se tocan se funden.
3. Rinde en Resolve solo esos tramos (ajustes del máster de `mp4_entrega`) y los codifica con la
   receta de entrega (`mp4_entrega.VIDEO`).
4. Copia de la entrega vieja, sin recodificar, todo lo demás; pega las partes con el demuxer
   `concat` (`-auto_convert 0`) y le pone el audio de la entrega vieja, tal cual.
5. Verifica: cuadros = línea; SPS/PPS iguales en todas las partes; todo lo que no es tramo nuevo,
   idéntico a la entrega vieja paquete a paquete; pts seguidos y en la rejilla; cuadro clave en
   cada empalme; audio idéntico; decodificación completa sin errores; PSNR de cada tramo contra
   lo que rindió Resolve, y contra la entrega vieja cuadro a cuadro (fuera del cartón tiene que
   ser la misma imagen: si baja, cambió algo más que el cartón).
6. Deja una hoja con el cartón viejo y el nuevo a media pantalla y los cuadros de los empalmes, y
   vuelve a exportar el `.drt` (el anterior va a `_descartes`).

    python reparchar.py plan_ed00 <versión vieja> <versión nueva> c02_lentes [otra clave…]

Log: `<P.TMP>/reparchar.log`, que termina en «REPARCHADO» o en «FALLO: …». Hoja:
`<P.TMP>/reparchar_hoja.jpg`. No borra nada: la entrega vieja y los cartones viejos quedan donde
están.

Solo cartones y lower thirds (V2 y V4). Una lista de After Effects se cambia igual a mano
(rendirla con otro nombre y agregarla aquí), pero hoy no hizo falta.
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
PISTA = {'carton': 2, 'lt': 4}

plan, V_OLD, V_NEW, CLAVES = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4:]
for _r, _d, _f in os.walk(os.path.join(AQUI, '..', '..', 'cursos')):
    if plan + '.py' in _f:
        sys.path.insert(0, _r)
        break
P = importlib.import_module(plan)
T = P.TMP + '/reparchar/'
os.makedirs(T, exist_ok=True)
log = open(P.TMP + '/reparchar.log', 'w', encoding='utf-8')


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
    rejilla de 23,976)."""
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
    """md5 de cada paquete de video, sin decodificar: {cuadro: (bytes, md5)}."""
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


def md5_audio(f):
    return run([FF, '-v', 'error', '-i', f, '-map', '0:a', '-c', 'copy', '-f', 'md5', '-']).stdout.strip()


def cuadro_de(f, k, w, h):
    raw = subprocess.run([FF, '-v', 'error', '-ss', '%.4f' % (k / FPS - 0.004), '-i', f, '-frames:v', '1', '-vf', 'scale=%d:%d' % (w, h),
                          '-pix_fmt', 'rgb24', '-f', 'rawvideo', '-'], capture_output=True).stdout
    return Image.frombytes('RGB', (w, h), raw) if len(raw) == w * h * 3 else Image.new('RGB', (w, h), (90, 0, 0))


vieja = '%s/05 EXPORTS/%s.mp4' % (P.R, P.EXPORT % V_OLD)
nueva = '%s/05 EXPORTS/%s.mp4' % (P.R, P.EXPORT % V_NEW)
if os.path.exists(nueva):
    falla('ya existe ' + nueva)
if not os.path.exists(vieja):
    falla('no está ' + vieja)
if not CLAVES:
    falla('faltan las claves de los cartones')
ITEMS = {it[0]: it for it in P.ITEMS}
VERS = getattr(P, 'VERSIONES', {})
cambios = []      # (clave, pista, cuadro, ruta nueva)
for c in CLAVES:
    if c not in ITEMS or ITEMS[c][1] not in PISTA:
        falla('%s no es un cartón ni un lower third del plan' % c)
    if not VERS.get(c):
        falla('%s no está en VERSIONES del plan' % c)
    ruta = '%s/02 CARTONES/%s_%s v%d.mov' % (P.R, P.PREFIJO, c, VERS[c])
    if not os.path.exists(ruta):
        falla('no está ' + ruta)
    cambios.append((c, PISTA[ITEMS[c][1]], P.cuadro(ITEMS[c][2]), ruta))

# ---------- 1. Resolve: los cartones nuevos en la línea
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


def item_en(pista, cuadro):
    for it in tl.GetItemListInTrack('video', pista) or []:
        if it.GetStart() - t0 == cuadro:
            return it
    return None


tramos = []       # (clave, a, b): cuadros de la línea que ocupa cada cartón
for c, pista, k, ruta in cambios:
    it = item_en(pista, k)
    if it is None:
        falla('no hay un ítem en V%d que empiece en el cuadro %d (%s)' % (pista, k, c))
    m = it.GetMediaPoolItem()
    actual = m.GetClipProperty('File Path') or ''
    dur = it.GetEnd() - it.GetStart()
    if not os.path.basename(actual).startswith('%s_%s' % (P.PREFIJO, c)):
        falla('el ítem del cuadro %d en V%d es %s y no %s' % (k, pista, os.path.basename(actual), c))
    if M.cuadros(ruta) != dur:
        falla('%s mide %d cuadros y el ítem de la línea %d' % (os.path.basename(ruta), M.cuadros(ruta), dur))
    if norm(actual) != norm(ruta):
        p('ReplaceClip', c, os.path.basename(actual), '->', os.path.basename(ruta), m.ReplaceClip(os.path.normpath(ruta)))
    it = item_en(pista, k)
    m = it.GetMediaPoolItem() if it else None
    if it is None or it.GetEnd() - it.GetStart() != dur or norm(m.GetClipProperty('File Path') or '') != norm(ruta) \
            or tl.GetEndFrame() - t0 != largo:
        falla('la línea cambió al reemplazar %s' % c)
    tramos.append((c, k, k + dur))
p('línea', P.NOMBRE_LINEA, 'largo', largo, 'cartones', tramos)

# ---------- 2. la entrega vieja: cuadros clave alrededor de cada cartón
pk = paquetes(vieja)
if len(pk) != largo:
    falla('la entrega vieja mide %d y la línea %d' % (len(pk), largo))
idr = sorted(int(round(a)) for a, b in pk if b)
segs = []         # [k_a, k_b, [claves]]
for c, a, b in sorted(tramos, key=lambda x: x[1]):
    k_a = max(k for k in idr if k <= a)
    k_b = min([k for k in idr if k >= b] + [largo])
    if a - k_a > 96 or k_b - b > 96:
        falla('cuadros clave raros alrededor de %s: %d–%d para %d–%d' % (c, k_a, k_b, a, b))
    if segs and k_a <= segs[-1][1]:
        segs[-1][1] = max(segs[-1][1], k_b)
        segs[-1][2].append(c)
    else:
        segs.append([k_a, k_b, [c]])
p('entrega vieja', os.path.basename(vieja), 'cuadros', len(pk), '| tramos nuevos', [(a, b, b - a, cs) for a, b, cs in segs])

# ---------- 3. los tramos: Resolve y x264
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
    for i, (a, b, _cs) in enumerate(segs):
        rinde('tramo%d_master' % i, a, b)
finally:
    # los ajustes de render son del proyecto: se devuelven en el acto
    pr.DeleteAllRenderJobs()
    pr.SetRenderSettings({'SelectAllFrames': True, 'ExportVideo': True, 'ExportAudio': True})
    resolve.OpenPage('edit')
time.sleep(12)                  # el mp4 recién terminado puede no tener todavía el moov
ok_img = True
for i, (a, b, cs) in enumerate(segs):
    m, x = T + 'tramo%d_master.mp4' % i, T + 'tramo%d.mp4' % i
    if M.cuadros(m) != b - a:
        falla('tramo%d_master mide %d y tenía que medir %d' % (i, M.cuadros(m), b - a))
    if os.path.exists(x):
        os.remove(x)
    run([FF, '-y', '-v', 'error', '-i', m] + M.VIDEO + ['-an', '-f', 'mp4', x])
    r = run([FF, '-hide_banner', '-nostats', '-i', x, '-i', m, '-lavfi', '[0:v][1:v]psnr', '-f', 'null', '-']).stderr
    p('tramo%d' % i, cs, 'cuadros', M.cuadros(x), 'psnr contra Resolve', (re.findall(r'average:[\d.]+ min:[\d.]+', r) or ['?'])[-1])
    # contra la entrega vieja, cuadro a cuadro: fuera del cartón es la misma imagen
    st = T + 'tramo%d_psnr.txt' % i
    if os.path.exists(st):
        os.remove(st)
    # el archivo de estadísticas va con nombre relativo y `cwd=T`: así no hay que escapar «D:» en el filtro
    run([FF, '-hide_banner', '-nostats', '-ss', '%.4f' % (a / FPS - 0.004), '-i', vieja, '-i', m, '-frames:v', str(b - a),
         '-lavfi', '[0:v][1:v]psnr=stats_file=tramo%d_psnr.txt' % i, '-f', 'null', '-'], cwd=T)
    ps = [float(x_) if x_ != 'inf' else 99.0 for x_ in re.findall(r'psnr_avg:(inf|[\d.]+)', open(st).read())] if os.path.exists(st) else []
    dentro = set()
    for c, ta, tb in tramos:
        if c in cs:
            dentro |= set(range(ta - a, tb - a))
    fuera = [v for j, v in enumerate(ps) if j not in dentro]
    den = [v for j, v in enumerate(ps) if j in dentro]
    p('tramo%d contra la entrega vieja: %d cuadros | fuera del cartón mín %.1f dB (%d) | dentro mín %.1f media %.1f (%d)' % (
        i, len(ps), min(fuera) if fuera else 99, len(fuera), min(den) if den else 99, sum(den) / max(1, len(den)), len(den)))
    # dentro del cartón la imagen cambia lo que cambie el texto (si la caja gana un renglón, bastante):
    # se informa y no se juzga; fuera tiene que ser la entrega vieja vuelta a rendir (45 dB o más)
    if len(ps) != b - a or (fuera and min(fuera) < 38):
        ok_img = False
if not ok_img:
    falla('un tramo no se parece a la entrega vieja: cambió algo más que el cartón')

# ---------- 4. lo demás, copiado; y todo pegado
partes, cur = [], 0     # (archivo, cuadros, primer cuadro, es nuevo)
for i, (a, b, _cs) in enumerate(segs):
    if a > cur:
        partes.append((T + 'copia%d.mp4' % len(partes), a - cur, cur, False))
    partes.append((T + 'tramo%d.mp4' % i, b - a, a, True))
    cur = b
if cur < largo:
    partes.append((T + 'copia%d.mp4' % len(partes), largo - cur, cur, False))
for f, n, k, es_nuevo in partes:
    if es_nuevo:
        continue
    if os.path.exists(f):
        os.remove(f)
    if k == 0:
        run([FF, '-y', '-v', 'error', '-i', vieja, '-an', '-c:v', 'copy', '-frames:v', str(n), '-f', 'mp4', f])
    else:
        # `-ss` un pelo después del cuadro clave (la búsqueda cae en él) y `setts` para que la copia
        # arranque en pts 0 (ver `retitular.py`)
        run([FF, '-y', '-v', 'error', '-ss', '%.6f' % (k / FPS + 0.004), '-i', vieja, '-an', '-c:v', 'copy',
             '-frames:v', str(n), '-bsf:v', 'setts=pts=PTS-STARTPTS:dts=DTS-STARTPTS', '-f', 'mp4', f])
    if M.cuadros(f) != n:
        falla('%s mide %d y tenía que medir %d' % (os.path.basename(f), M.cuadros(f), n))
ex = [extradata(f) for f, _n, _k, _e in partes]
p('partes', [(os.path.basename(f), k, n) for f, n, k, _e in partes])
p('SPS/PPS', sorted({e.get('extradata_hash') for e in ex}), ex[0].get('profile'), ex[0].get('level'), ex[0].get('has_b_frames'),
  ex[0].get('r_frame_rate'))
if len({json.dumps(e, sort_keys=True) for e in ex}) != 1:
    falla('las partes no tienen los mismos parámetros: %s' % ex)
with open(T + 'lista.txt', 'w', encoding='utf-8') as fl:
    for j, (f, n, _k, _e) in enumerate(partes):
        fl.write("file '%s'\n" % f)
        if j < len(partes) - 1:
            fl.write('duration %.6f\n' % (n / FPS))
run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-auto_convert', '0', '-i', T + 'lista.txt', '-c', 'copy', '-f', 'mp4',
     T + 'imagen.mp4'])
tmp = nueva + '.parcial'
run([FF, '-y', '-v', 'error', '-i', T + 'imagen.mp4', '-i', vieja, '-map', '0:v', '-map', '1:a', '-c', 'copy',
     '-movflags', '+faststart', '-f', 'mp4', tmp])

# ---------- 5. verificación
pn = paquetes(tmp)
ok_n = len(pn) == largo
orden = sorted(a for a, _b in pn)
k0 = min(a for a, _b in pk)
ok_pts = bool(orden) and all(abs(a - (k0 + i)) < 1e-3 for i, a in enumerate(orden))
claves_n = {int(round(a)) for a, b in pn if b}
empalmes = sorted({k for a, b, _cs in segs for k in (a, b) if k < largo})
ok_emp = all(k in claves_n for k in empalmes)
p('cuadros', len(pn), '/ línea', largo, 'OK' if ok_n else 'FALLA', '| pts seguidos y en la rejilla', ok_pts,
  '| cuadro clave en los empalmes', ok_emp, empalmes)
a_, b_ = md5_paquetes(vieja), md5_paquetes(tmp)
nuevos = set()
for a, b, _cs in segs:
    nuevos |= set(range(a, b))
ok_copia = len(a_) == len(b_) == largo and all(k in a_ and a_.get(k) == b_.get(k) for k in range(largo) if k not in nuevos)
p('lo copiado, idéntico paquete a paquete (%d cuadros):' % (largo - len(nuevos)), ok_copia,
  '| paquetes que cambian en los tramos nuevos', sum(1 for k in nuevos if a_.get(k) != b_.get(k)), 'de', len(nuevos))
ma, mb = md5_audio(vieja), md5_audio(tmp)
p('audio idéntico:', ma == mb and bool(ma), ma)
r = subprocess.run([FF, '-v', 'error', '-xerror', '-i', tmp, '-f', 'null', '-'], capture_output=True, text=True, errors='replace')
ok_dec = r.returncode == 0 and not r.stderr.strip()
p('decodificación completa: rc', r.returncode, 'errores', len(r.stderr.strip().splitlines()), r.stderr[-200:])
if not (ok_n and ok_pts and ok_emp and ok_copia and ma == mb and ma and ok_dec):
    falla('la verificación no pasó; queda ' + tmp)
os.replace(tmp, nueva)
j = json.loads(run([FP, '-v', 'error', '-show_streams', '-of', 'json', nueva]).stdout)
v_ = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
p('entrega', os.path.basename(nueva), v_['codec_name'], v_.get('profile'), 'L%s' % v_.get('level'), '%dx%d' % (v_['width'], v_['height']),
  v_.get('color_space'), v_.get('r_frame_rate'), '%d MB' % (os.path.getsize(nueva) >> 20), 'sonido', M.medir(nueva))

# hoja: por cartón, el viejo y el nuevo a media pantalla, y los cuadros de los empalmes
hoja = Image.new('RGB', (1920, 850 * len(tramos)), (20, 20, 20))
dr = ImageDraw.Draw(hoja)
for i, (c, ta, tb) in enumerate(sorted(tramos, key=lambda x: x[1])):
    y, mid = 850 * i, (ta + tb) // 2
    a, b = [(sa, sb) for sa, sb, cs in segs if c in cs][0]
    hoja.paste(cuadro_de(vieja, mid, 960, 540), (0, y))
    hoja.paste(cuadro_de(nueva, mid, 960, 540), (960, y))
    dr.text((6, y + 542), '%s  ANTES (v%d), cuadro %d' % (c, V_OLD, mid), fill=(255, 255, 0))
    dr.text((966, y + 542), '%s  AHORA (v%d), cuadro %d' % (c, V_NEW, mid), fill=(255, 255, 0))
    for jx, (nom, k) in enumerate([('empalme -1', a - 1), ('empalme', a), ('empalme -1', b - 1), ('empalme', b)]):
        if 0 <= k < largo:
            hoja.paste(cuadro_de(nueva, k, 480, 270), (480 * jx, y + 560))
        dr.text((480 * jx + 4, y + 832), '%s %d' % (nom, k), fill=(255, 255, 0))
hoja.save(P.TMP + '/reparchar_hoja.jpg', quality=90)

# ---------- 6. el .drt
drt = '%s/10 TIMELINE SEBASTIAN/%s.drt' % (P.R, P.NOMBRE_LINEA)
if os.path.exists(drt):
    d = os.path.dirname(drt) + '/_descartes'
    os.makedirs(d, exist_ok=True)
    dst, n_ = '%s/%s (antes de la v%d).drt' % (d, P.NOMBRE_LINEA, V_NEW), 1
    while os.path.exists(dst):          # no se pisa ni se borra nada
        n_ += 1
        dst = '%s/%s (antes de la v%d) %d.drt' % (d, P.NOMBRE_LINEA, V_NEW, n_)
    shutil.move(drt, dst)
p('drt', tl.Export(os.path.normpath(drt), resolve.EXPORT_DRT))
pm.SaveProject()
p('REPARCHADO')
