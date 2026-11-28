# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026): la entrega SIN el render de Resolve.

El render de Resolve quedo en 0 % ("cuMemAlloc failed 801" en el log de Resolve, la placa en mal estado despues de
horas de recortes por DirectML; reiniciar Resolve no alcanzo: en octubre se arreglo reiniciando el computador). La
linea se sigue armando en Resolve (ic_linea_externa.py, para que Sebastian la tenga y la pueda tocar), pero el MP4 sale
de ffmpeg leyendo ESA linea: cada item de video (pistas de abajo hacia arriba) se superpone en su lugar sobre negro
a 23,976, con su recorte de fuente y el cambio de cuadros por segundo; el sonido de A1 va en su lugar. Despues: techo
de -3 dBTP (alimiter a 192 kHz), cuenta de cuadros contra la linea, sonido, copia a la carpeta de paso de Drive y la
hoja de revision (ic_revision.py). Un plan tras otro, segun cola.txt (termina con FIN). Log: lote_entrega.log"""
import importlib, json, os, re, shutil, subprocess, sys, time
PY = sys.executable
M = 'D:/DAE/_repo/herramientas/montaje/'
sys.path.insert(0, M)
sys.path.insert(0, 'D:/DAE/_repo/cursos/gerencia_judicial/profe')
sys.path.insert(0, 'D:/DAE/_repo/herramientas/entrega')
from subir_exclusivo import copiar_exclusivo
os.environ.setdefault('DAE_PRESET', 'medium')   # grafica provisional: el preset rapido que ya admite mp4_entrega
import mp4_entrega as E
import DaVinciResolveScript as dvr
T = 'D:/DAE/_tmp/gj_p/'
PASO = 'G:/My Drive/_MA subidas/'
FPS = 24000 / 1001.0
log = open(T + 'lote_entrega.log', 'a', encoding='utf-8')


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
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre:
            return t
    return None


def estructura(tl):
    """Los items de la linea: (tipo, pista, inicio, fin, archivo, fuente_inicio_s, fps_fuente) en cuadros de la linea."""
    s0 = tl.GetStartFrame()
    out = []
    for tipo in ('video', 'audio'):
        for k in range(1, int(tl.GetTrackCount(tipo)) + 1):
            for it in (tl.GetItemListInTrack(tipo, k) or []):
                mp = it.GetMediaPoolItem()
                f = mp.GetClipProperty('File Path') if mp else ''
                fps = float(mp.GetClipProperty('FPS') or FPS) if mp else FPS
                out.append({'tipo': tipo, 'pista': k, 'ini': it.GetStart() - s0, 'fin': it.GetEnd() - s0, 'archivo': f,
                            'src_s': it.GetLeftOffset() / fps, 'fps': fps, 'alfa': (mp.GetClipProperty('Alpha mode') or 'None') != 'None' if mp else False})
    return out, tl.GetEndFrame() - s0


def armar(items, total, sal):
    ins, fil = [], []

    def entrada(p):
        ins.extend(['-i', p]); return len(ins) // 2 - 1
    dur = total / FPS
    fil.append('color=c=black:s=1920x1080:r=24000/1001:d=%.6f,format=yuv420p[base]' % dur)
    cur = 'base'
    vids = sorted([x for x in items if x['tipo'] == 'video'], key=lambda x: (x['pista'], x['ini']))
    for k, x in enumerate(vids):
        i = entrada(x['archivo'])
        n = x['fin'] - x['ini']
        fmt = 'yuva420p' if x['alfa'] else 'yuv420p'
        fil.append('[%d:v]trim=start=%.6f,setpts=PTS-STARTPTS,fps=24000/1001,trim=end_frame=%d,scale=1920:1080,setsar=1,format=%s,'
                   'setpts=PTS+%.6f/TB[c%d]' % (i, x['src_s'], n, fmt, x['ini'] / FPS, k))
        fil.append('[%s][c%d]overlay=eof_action=pass:format=auto[o%d]' % (cur, k, k))
        cur = 'o%d' % k
    fil.append('[%s]trim=end_frame=%d,format=yuv420p[v]' % (cur, total))
    auds = sorted([x for x in items if x['tipo'] == 'audio'], key=lambda x: x['ini'])
    etq = []
    for k, x in enumerate(auds):
        i = entrada(x['archivo'])
        n = (x['fin'] - x['ini']) / FPS
        fil.append('[%d:a]aresample=48000,aformat=channel_layouts=stereo,atrim=start=%.6f:duration=%.6f,asetpts=PTS-STARTPTS,adelay=%d:all=1[a%d]'
                   % (i, x['src_s'], n, int(round(x['ini'] / FPS * 1000)), k))
        etq.append('[a%d]' % k)
    fil.append('anullsrc=r=48000:cl=stereo,atrim=duration=%.6f[sil]' % dur)
    fil.append('[sil]%samix=inputs=%d:normalize=0:duration=first,atrim=duration=%.6f,'
               'aresample=192000,alimiter=limit=%.4f:attack=1:release=50:level=false,aresample=48000[a]' % (''.join(etq), len(etq) + 1, dur, E.LIMITE))
    fg = T + os.path.basename(sal) + '.filtro'   # el grafo de ffmpeg queda en la carpeta de trabajo, no en 05 EXPORTS
    open(fg, 'w', encoding='utf-8').write(';\n'.join(fil))
    cmd = [E.FB + '/ffmpeg.exe', '-y', '-v', 'error'] + ins + ['-/filter_complex', fg, '-map', '[v]', '-map', '[a]', '-r', '24000/1001',
           '-frames:v', str(total)] + E.VIDEO + ['-c:a', 'aac', '-b:a', '320k', sal + '.parcial.mp4']
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
    if r.returncode:
        return None, r.stderr[-800:]
    os.replace(sal + '.parcial.mp4', sal)
    return sal, '%.0f s' % (time.time() - t0)


def subir(f):
    n = os.path.getsize(f)
    if shutil.disk_usage('G:/').free < n + 0.35e9 or shutil.disk_usage('C:/').free < n + 0.4e9:
        return False
    nb, md5 = copiar_exclusivo(f, PASO + os.path.basename(f))
    w('copiado|%s|%d|%s' % (os.path.basename(f), nb, md5))
    return True


def uno(p):
    P = importlib.import_module(p)
    env = dict(os.environ, DAE_PLAN=p, PYTHONUTF8='1')
    v = getattr(P, 'VERSION', 1)
    nombre = P.EXPORT % v
    f = '%s/05 EXPORTS/%s.mp4' % (P.R, nombre)
    if os.path.exists(f):
        w('ya existe', os.path.basename(f)); return
    _res, pr = proyecto()
    if linea(pr, P.NOMBRE_LINEA) is None:
        cl = P.TMP + '/cadena.log'
        t0 = time.time(); s = ''
        while time.time() - t0 < 8 * 3600:
            s = open(cl, encoding='utf-8', errors='replace').read() if os.path.exists(cl) else ''
            if 'LOTE LISTO' in s or 'LOTE FALLO' in s:
                break
            time.sleep(5)
        if 'LOTE LISTO' not in s:
            w('SIN CADENA', p); return
        try:
            r = subprocess.run([PY, M + 'ic_linea_externa.py'], capture_output=True, text=True, env=env, errors='replace', timeout=1200)
        except subprocess.TimeoutExpired:
            w('LINEA SIN RESPUESTA (20 min)', p); return
        open(P.TMP + '/linea.log', 'w', encoding='utf-8').write(r.stdout + ('\nERR ' + r.stderr[-2500:] if r.returncode else ''))
        bien = 'LINEA LISTA' in r.stdout and 'problemas ninguno' in r.stdout
        w('linea', p, bien, '|', ' ; '.join(l for l in r.stdout.splitlines() if 'fin de la' in l)[:200])
        if not bien:
            w('LINEA FALLO', p, (r.stdout[-500:] + r.stderr[-500:])); return
    _res, pr = proyecto()
    tl = linea(pr, P.NOMBRE_LINEA)
    items, total = estructura(tl)
    json.dump({'items': items, 'total': total}, open(P.TMP + '/linea_estructura.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    falta = [x['archivo'] for x in items if not os.path.exists(x['archivo'])]
    if falta:
        w('FALTA MEDIA', p, falta); return
    os.makedirs('%s/05 EXPORTS' % P.R, exist_ok=True)
    out, nota = armar(items, total, f)
    if not out:
        w('FFMPEG FALLO', p, nota); return
    n = E.cuadros(f)
    son = E.medir(f)
    ok = n == total and float(son.get('Peak', 0)) <= E.TECHO_COPIA
    w('entrega', p, 'rc 0 %s' % ok, nota, '| ffmpeg x264 crf 18 ' + E.PRESET + ', cuadros %d / linea %d %s, %d MB, %.0f kb/s, sonido %s'
      % (n, total, 'OK' if n == total else 'FALLA', os.path.getsize(f) >> 20, os.path.getsize(f) * 8 / 1000.0 / (n / FPS), son))
    if not ok:
        os.replace(f, f + '.revisar_%d.viejo' % int(time.time())); return
    if not subir(f):
        w('SIN CUPO para copiar a Drive', os.path.basename(f))
    r2 = subprocess.run([PY, M + 'ic_revision.py', str(v)], capture_output=True, text=True, env=env, errors='replace')
    w('revision', p, 'rc', r2.returncode, r2.stderr[-200:] if r2.returncode else '')


vistos = []
w('entrega_ffmpeg: arranca')
while True:
    c = cola()
    nuevos = [p for p in c if p != 'FIN' and p not in vistos]
    if not nuevos:
        if 'FIN' in c:
            break
        time.sleep(15); continue
    vistos.append(nuevos[0])
    try:
        uno(nuevos[0])
    except Exception as e:
        w('ENTREGA EXCEPCION', nuevos[0], repr(e)[:400])
w('ENTREGAS LISTAS')
