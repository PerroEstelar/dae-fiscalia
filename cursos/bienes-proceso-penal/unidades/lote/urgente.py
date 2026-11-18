# -*- coding: utf-8 -*-
"""Bienes unidades, cierres (17 nov 2026, «we need to have this before 10 pm»): la entrega MP4 sale directo de
Resolve por la placa NVIDIA (H.264, unos 5 Mb/s), en vez de x264 por procesador, que no llegaba. Uno tras otro:
los que ya tienen linea se rinden; el que no, espera su compuesto y arma la linea. Despues: faststart, cuenta de
cuadros, copia a Drive. Al final, los masters que falten y las hojas de revision. Log: lote_entrega.log
    python urgente.py plan_biu3c plan_biu4c plan_biu2c plan_biu1c"""
import importlib, os, shutil, subprocess, sys, time
PY = sys.executable
M = 'D:/DAE/_repo/herramientas/montaje/'
sys.path.insert(0, M)
sys.path.insert(0, 'D:/DAE/_repo/cursos/bienes-proceso-penal/unidades')
sys.path.insert(0, 'D:/DAE/_repo/herramientas/entrega')
os.environ.setdefault('DAE_PRESET', 'slow')
from subir_exclusivo import copiar_exclusivo
import mp4_entrega as E
import DaVinciResolveScript as dvr
T = 'D:/DAE/_tmp/bi_u/'
FF = E.FB + '/ffmpeg.exe'
log = open(T + 'lote_entrega.log', 'a', encoding='utf-8')
META = 5000.0      # kb/s reales que se buscan


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


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
          'ExportVideo': True, 'ExportAudio': True}
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
    return (out if os.path.exists(out) else None), (largo if not tramo else tramo[1] - tramo[0]), st


def kbps_real(f, cuadros):
    return os.path.getsize(f) * 8 / 1000.0 / (cuadros / (24000 / 1001.0))


def calibra(P):
    """Dos pruebas de 20 s para saber que numero darle a Resolve: el codificador de la placa queda muy por
    debajo del valor pedido (los masters, pedidos a 80000, salen a unos 20000)."""
    k = 16000.0
    for paso in (1, 2):
        try:
            r = rinde(P, 'calibra%d' % paso, k, P.TMP + '/gpu', tramo=(1000, 1480))
            if not r[0]:
                break
            real = kbps_real(r[0], 480)
            w('calibra', paso, 'pedido %d' % k, 'real %.0f kb/s' % real)
            if 0.85 * META <= real <= 1.2 * META:
                break
            k = max(4000.0, min(80000.0, k * META / real))
        except Exception as e:
            w('CALIBRA EXCEPCION', repr(e)[:300]); break
    return k


def entrega(p, kbps):
    P = importlib.import_module(p)
    v = getattr(P, 'VERSION', 1)
    nombre = P.EXPORT % v
    f = '%s/05 EXPORTS/%s.mp4' % (P.R, nombre)
    if os.path.exists(f):
        w('ya existe', os.path.basename(f)); return True
    t = time.time()
    out, largo, st = rinde(P, nombre, kbps, P.TMP + '/gpu')
    if not out:
        w('GPU FALLO', p, st); return False
    os.makedirs(os.path.dirname(f), exist_ok=True)
    r = subprocess.run([FF, '-y', '-v', 'error', '-i', out, '-c', 'copy', '-movflags', '+faststart', '-f', 'mp4', f + '.parcial'],
                       capture_output=True, text=True, errors='replace')
    if r.returncode:
        w('FASTSTART FALLO', p, r.stderr[-300:]); return False
    n = E.cuadros(f + '.parcial')
    if n != largo:
        w('CUADROS FALLA', p, n, largo); return False
    os.replace(f + '.parcial', f)
    w('entrega', p, 'rc 0 True', '%.0f s' % (time.time() - t), '| NVIDIA por Resolve, pedido %d kb/s, real %.0f kb/s, cuadros %d / linea %d OK, %d MB, sonido %s'
      % (kbps, kbps_real(f, largo), n, largo, os.path.getsize(f) >> 20, E.medir(f)))
    nb, md5 = copiar_exclusivo(f, 'G:/My Drive/_MA subidas/' + os.path.basename(f))
    w('copiado|%s|%s|%d|%s' % (p, os.path.basename(f), nb, md5))
    return True


planes = sys.argv[1:]
# si quedo un master a medio rendir del lote anterior, se espera a que su proceso termine
t0 = time.time()
while time.time() - t0 < 420:
    q = subprocess.run(['wmic', 'process', 'where', "name='python.exe'", 'get', 'CommandLine', '/format:list'],
                       capture_output=True, text=True, errors='replace').stdout
    if 'E.master(' not in q:
        break
    time.sleep(3)
w('urgente: arranca', planes)
kbps = None
hechos = []
for p in planes:
    try:
        P = importlib.import_module(p)
        env = dict(os.environ, DAE_PLAN=p, PYTHONUTF8='1')
        _res, pr = proyecto()
        if linea(pr, P.NOMBRE_LINEA) is None:
            cl = P.TMP + '/cadena.log'
            t0 = time.time(); s = ''
            while time.time() - t0 < 4 * 3600:
                s = open(cl, encoding='utf-8', errors='replace').read() if os.path.exists(cl) else ''
                if 'LOTE LISTO' in s or 'LOTE FALLO' in s:
                    break
                time.sleep(3)
            if 'LOTE LISTO' not in s:
                w('SIN CADENA', p); continue
            r = subprocess.run([PY, M + 'ic_linea_externa.py'], capture_output=True, text=True, env=env, errors='replace')
            open(P.TMP + '/linea.log', 'w', encoding='utf-8').write(r.stdout + ('\nERR ' + r.stderr[-2500:] if r.returncode else ''))
            bien = 'LINEA LISTA' in r.stdout and 'problemas ninguno' in r.stdout
            w('linea', p, bien, '|', ' ; '.join(l for l in r.stdout.splitlines() if 'fin de la' in l)[:200])
            if not bien:
                w('LINEA FALLO', p, (r.stdout[-400:] + r.stderr[-400:])); continue
        if kbps is None:
            kbps = calibra(P)
        if entrega(p, kbps):
            hechos.append(p)
    except Exception as e:
        w('URGENTE EXCEPCION', p, repr(e)[:400])
w('ENTREGAS URGENTES LISTAS', hechos)
# lo que no corria prisa: el master de archivo del que falte y las hojas de revision
for p in planes:
    try:
        P = importlib.import_module(p)
        v = getattr(P, 'VERSION', 1)
        env = dict(os.environ, DAE_PLAN=p, PYTHONUTF8='1')
        m, _l = E.master(P.NOMBRE_LINEA, P.R, P.EXPORT % v, P.MASTER_DIR)
        w('master', p, os.path.exists(m))
        r2 = subprocess.run([PY, M + 'ic_revision.py', str(v)], capture_output=True, text=True, env=env, errors='replace')
        w('revision', p, 'rc', r2.returncode)
    except Exception as e:
        w('MASTER/REVISION EXCEPCION', p, repr(e)[:300])
resolve, pr = proyecto()
resolve.OpenPage('edit')
w('LOTE LISTO')
open(T + 'prioridad.fin', 'w').write('fin')
