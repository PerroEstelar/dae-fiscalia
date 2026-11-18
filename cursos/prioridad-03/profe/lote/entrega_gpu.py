# -*- coding: utf-8 -*-
"""Trata, videos de profe (17-18 nov 2026): linea de Resolve y entrega MP4 directo de Resolve por la placa NVIDIA
(H.264, unos 5 Mb/s reales), sin master de 32 Mb/s (no hay disco). Un plan tras otro, segun cola.txt (se puede
alargar; termina con FIN). Espera el compuesto de cada plan. Despues de cada entrega: cuenta de cuadros contra la
linea, sonido, hoja de revision y copia a la carpeta de paso de Drive SI HAY CUPO (el Drive de Sebastian estaba
casi lleno); lo que no entra queda en pendientes.txt y se reintenta en cada vuelta. Log: lote_entrega.log"""
import importlib, os, shutil, subprocess, sys, time
PY = sys.executable
M = 'D:/DAE/_repo/herramientas/montaje/'
sys.path.insert(0, M)
sys.path.insert(0, 'D:/DAE/_repo/cursos/prioridad-03/profe')
sys.path.insert(0, 'D:/DAE/_repo/herramientas/entrega')
os.environ.setdefault('DAE_PRESET', 'slow')
from subir_exclusivo import copiar_exclusivo
import mp4_entrega as E
import DaVinciResolveScript as dvr
T = 'D:/DAE/_tmp/tr_p/'
PASO = 'G:/My Drive/_MA subidas/'
log = open(T + 'lote_entrega.log', 'a', encoding='utf-8')
META = 5000.0      # kb/s reales que se buscan
MARGEN = 0.35e9    # cupo de Drive que se deja libre


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def cola():
    try:
        return [l.strip() for l in open(T + 'cola.txt', encoding='utf-8') if l.strip()]
    except OSError:
        return []


def proyecto():
    resolve = dvr.scriptapp('Resolve')
    return resolve, resolve.GetProjectManager().GetCurrentProject()


def linea(pr, nombre):
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre:
            tl = t
    return tl


def moov_adelante(f):
    with open(f, 'rb') as fh:
        return b'moov' in fh.read(1 << 16)


def rinde(P, nombre, kbps, tmp, tramo=None):
    resolve, pr = proyecto()
    while pr.IsRenderingInProgress():
        time.sleep(2)
    tl = linea(pr, P.NOMBRE_LINEA)
    if tl is None:
        return None, 0, None
    largo = tl.GetEndFrame() - tl.GetStartFrame()
    os.makedirs(tmp, exist_ok=True)
    out = '%s/%s.mp4' % (tmp, nombre)
    if os.path.exists(out):
        shutil.move(out, '%s.%d.viejo' % (out, int(time.time())))
    pr.SetCurrentTimeline(tl)
    resolve.OpenPage('deliver')
    pr.DeleteAllRenderJobs()
    pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    aj = {'SelectAllFrames': True, 'TargetDir': os.path.normpath(tmp), 'CustomName': nombre,
          'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': 23.976,
          'VideoQuality': int(kbps), 'AudioCodec': 'aac', 'AudioSampleRate': 48000,
          'NetworkOptimization': True, 'ExportVideo': True, 'ExportAudio': True}
    if tramo:
        aj.update({'SelectAllFrames': False, 'MarkIn': tl.GetStartFrame() + tramo[0],
                   'MarkOut': tl.GetStartFrame() + tramo[1] - 1})
    pr.SetRenderSettings(aj)
    job = pr.AddRenderJob()
    pr.StartRendering([job])
    while pr.IsRenderingInProgress():
        time.sleep(2)
    st = pr.GetRenderJobStatus(job)
    time.sleep(6 if tramo else 15)       # el archivo recien terminado puede no tener todavia el moov
    if tramo:                            # los ajustes son del proyecto: se devuelven
        pr.SetRenderSettings({'SelectAllFrames': True})
    return (out if os.path.exists(out) else None), (largo if not tramo else tramo[1] - tramo[0]), st


def kbps_real(f, cuadros):
    return os.path.getsize(f) * 8 / 1000.0 / (cuadros / (24000 / 1001.0))


def calibra(P):
    k = 5000.0
    for paso in (1, 2):
        try:
            r = rinde(P, 'calibra%d' % paso, k, P.TMP + '/gpu', tramo=(1000, 1480))
            if not r[0]:
                break
            real = kbps_real(r[0], 480)
            w('calibra', paso, 'pedido %d' % k, 'real %.0f kb/s' % real, 'moov adelante', moov_adelante(r[0]))
            if 0.9 * META <= real <= 1.1 * META:
                break
            k = max(3000.0, min(80000.0, k * META / real))
        except Exception as e:
            w('CALIBRA EXCEPCION', repr(e)[:300]); break
    return k


def subir(f):
    """Copia a la carpeta de paso si hay cupo. Devuelve True si quedo copiado."""
    libre = shutil.disk_usage('G:/').free
    n = os.path.getsize(f)
    if libre < n + MARGEN:
        return False
    nb, md5 = copiar_exclusivo(f, PASO + os.path.basename(f))
    w('copiado|%s|%d|%s' % (os.path.basename(f), nb, md5))
    return True


def pendientes(agrega=None, quita=None):
    p = T + 'pendientes.txt'
    ls = [l.strip() for l in open(p, encoding='utf-8')] if os.path.exists(p) else []
    ls = [l for l in ls if l and l != quita]
    if agrega and agrega not in ls:
        ls.append(agrega)
    open(p, 'w', encoding='utf-8').write('\n'.join(ls) + ('\n' if ls else ''))
    return ls


def reintenta():
    for f in pendientes():
        try:
            if os.path.exists(f) and subir(f):
                pendientes(quita=f)
        except Exception as e:
            w('SUBIDA EXCEPCION', os.path.basename(f), repr(e)[:200])


def entrega(p, kbps):
    P = importlib.import_module(p)
    v = getattr(P, 'VERSION', 1)
    nombre = P.EXPORT % v
    f = '%s/05 EXPORTS/%s.mp4' % (P.R, nombre)
    if os.path.exists(f):
        w('ya existe', os.path.basename(f)); return True
    t = time.time()
    out, largo, st = rinde(P, nombre, kbps, '%s/05 EXPORTS/_rindiendo' % P.R)
    if not out:
        w('GPU FALLO', p, st); return False
    n = E.cuadros(out)
    if n != largo:
        w('CUADROS FALLA', p, n, largo); return False
    if moov_adelante(out):
        os.replace(out, f)               # mismo disco: un cambio de nombre, sin copia
        fs = 'faststart de Resolve'
    else:
        r = subprocess.run([E.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', out, '-c', 'copy', '-movflags', '+faststart', '-f', 'mp4', f + '.parcial'],
                           capture_output=True, text=True, errors='replace')
        if r.returncode or E.cuadros(f + '.parcial') != largo:
            w('FASTSTART FALLO', p, r.stderr[-300:]); return False
        os.replace(f + '.parcial', f)
        fs = 'faststart por remux (el crudo queda en _rindiendo)'
    w('entrega', p, 'rc 0 True', '%.0f s' % (time.time() - t), '| NVIDIA por Resolve, pedido %d kb/s, real %.0f kb/s, cuadros %d / linea %d OK, %d MB, %s, sonido %s'
      % (kbps, kbps_real(f, largo), n, largo, os.path.getsize(f) >> 20, fs, E.medir(f)))
    if not subir(f):
        pendientes(agrega=f)
        w('SIN CUPO en Drive: queda pendiente', os.path.basename(f))
    env = dict(os.environ, DAE_PLAN=p, PYTHONUTF8='1')
    r2 = subprocess.run([PY, M + 'ic_revision.py', str(v)], capture_output=True, text=True, env=env, errors='replace')
    w('revision', p, 'rc', r2.returncode, r2.stderr[-200:] if r2.returncode else '')
    return True


def uno(p, kbps):
    P = importlib.import_module(p)
    env = dict(os.environ, DAE_PLAN=p, PYTHONUTF8='1')
    _res, pr = proyecto()
    if linea(pr, P.NOMBRE_LINEA) is None:
        cl = P.TMP + '/cadena.log'
        t0 = time.time(); s = ''
        while time.time() - t0 < 8 * 3600:
            s = open(cl, encoding='utf-8', errors='replace').read() if os.path.exists(cl) else ''
            if 'LOTE LISTO' in s or 'LOTE FALLO' in s:
                break
            time.sleep(4)
            if int(time.time() - t0) % 120 < 4:
                reintenta()
        if 'LOTE LISTO' not in s:
            w('SIN CADENA', p); return kbps
        # el lower third se rinde de nuevo con las medidas vigentes del plan; el anterior va a _descartes
        if any(i[0] == 'lt01' for i in P.ITEMS):
            lt = '%s/02 CARTONES/%s_lt01.mov' % (P.R, P.PREFIJO)
            if os.path.exists(lt):
                d = '%s/02 CARTONES/_descartes' % P.R
                os.makedirs(d, exist_ok=True)
                shutil.move(lt, '%s/%s_lt01_%d.mov' % (d, P.PREFIJO, int(time.time())))
            r = subprocess.run([PY, M + 'ic_pieza.py', 'cartones', 'lt01'], capture_output=True, text=True, env=env, errors='replace')
            w('lt', p, 'rc', r.returncode, os.path.exists(lt), ' '.join(r.stdout.split())[-80:], r.stderr[-300:] if r.returncode else '')
            if not os.path.exists(lt):
                w('LT FALLO', p); return kbps
        r = subprocess.run([PY, M + 'ic_linea_externa.py'], capture_output=True, text=True, env=env, errors='replace')
        open(P.TMP + '/linea.log', 'w', encoding='utf-8').write(r.stdout + ('\nERR ' + r.stderr[-2500:] if r.returncode else ''))
        bien = 'LINEA LISTA' in r.stdout and 'problemas ninguno' in r.stdout
        w('linea', p, bien, '|', ' ; '.join(l for l in r.stdout.splitlines() if 'fin de la' in l)[:200])
        if not bien:
            w('LINEA FALLO', p, (r.stdout[-500:] + r.stderr[-500:])); return kbps
    if kbps is None:
        kbps = calibra(P)
    entrega(p, kbps)
    return kbps


vistos, kbps = [], None
w('entrega_gpu: arranca')
while True:
    c = cola()
    nuevos = [p for p in c if p != 'FIN' and p not in vistos]
    if not nuevos:
        if 'FIN' in c:
            break
        reintenta()
        time.sleep(15); continue
    vistos.append(nuevos[0])
    try:
        kbps = uno(nuevos[0], kbps)
    except Exception as e:
        w('ENTREGA EXCEPCION', nuevos[0], repr(e)[:400])
    reintenta()
w('ENTREGAS LISTAS')
# lo que quedo sin cupo se sigue intentando (hasta 12 h): Sebastian tiene que vaciar la papelera de Drive
t0 = time.time()
while pendientes() and time.time() - t0 < 12 * 3600:
    reintenta()
    time.sleep(60)
resolve, pr = proyecto()
resolve.OpenPage('edit')
w('LOTE LISTO', 'pendientes de subir:', [os.path.basename(x) for x in pendientes()])
