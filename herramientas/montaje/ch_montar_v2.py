# -*- coding: utf-8 -*-
r"""Arma en Resolve la linea V2 de un caso del profe Carlos Humberto a partir de
un montaje .json hecho afuera (cuadros exactos), la deja en el bin
`<caso>\10 TIMELINE SEBASTIAN`, exporta la .drt a esa carpeta y lanza el
render del master.

El montaje:
  {"caso": 6, "linea": "CH U1 CASO 06 - Lenin v2", "largo": 2252,
   "video": [{"archivo": ..., "ini": 0, "fin": 2252, "pista": 1, "en": 0}, ...],
   "audio": [{"archivo": ..., "pista": 1, "en": 0}, ...]}
`ini`/`fin` son cuadros del archivo (fin excluido); `en` es el cuadro de la
linea contado desde su inicio. Pista 1 de video = la base (la V1 tal cual o
sus tramos); las de arriba = piezas nuevas. Audio: A1 voz v2, A2 fondo v2.

    pasos: preparar (copia piezas y audio a la carpeta del caso),
           armar, drt, render, entrega
"""
import json
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch_migrar as CM      # noqa: E402

RAIZ = r'E:\DAE MASTER\PRIORIDAD 1\PROFE CARLOS HUMBERTO'
TMP = r'D:\DAE\_tmp\ch\v2'


def w(*a):
    print(*a, flush=True)


def cargar(n):
    return json.load(open(os.path.join(TMP, 'montaje_c%02d.json' % n), encoding='utf-8'))


def preparar(n):
    r"""Lleva lo que vino de afuera (D:\DAE\_tmp\ch\v2\c0N) a la carpeta del caso:
    piezas de video a 02 CARTONES\v2, audio (flac) a 03 VOCES\v2 como wav 24."""
    src = os.path.join(TMP, 'c%02d' % n)
    caso = CM.carpeta(n)
    hechos = []
    for f in sorted(os.listdir(src)):
        p = os.path.join(src, f)
        if f.endswith('.flac'):
            d = os.path.join(caso, '03 VOCES', 'v2')
            os.makedirs(d, exist_ok=True)
            o = os.path.join(d, f[:-5] + '.wav')
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-c:a', 'pcm_s24le', o], check=True)
        elif f.endswith(('.mp4', '.mov')):
            d = os.path.join(caso, '02 CARTONES', 'v2')
            os.makedirs(d, exist_ok=True)
            o = os.path.join(d, f)
            shutil.copy2(p, o)
        else:
            continue
        hechos.append(o)
    return hechos


def _mpi(mp, path, cache):
    if path in cache:
        return cache[path]
    rel = os.path.relpath(os.path.dirname(path), r'E:\DAE MASTER').split(os.sep)
    b = CM.bin_de(mp, rel)
    for c in b.GetClipList() or []:
        if (c.GetClipProperty('File Path') or '').lower() == path.lower():
            cache[path] = c
            return c
    mp.SetCurrentFolder(b)
    r = mp.ImportMedia([path]) or []
    if not r:
        raise RuntimeError('no importa ' + path)
    cache[path] = r[0]
    return r[0]


def armar(pr, n):
    m = cargar(n)
    mp = pr.GetMediaPool()
    nombre = m['linea']
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre:
            # no se borra: se aparta con sufijo y se arma de nuevo
            t.SetName(nombre + ' (anterior %s)' % time.strftime('%H%M%S'))
    rel = os.path.relpath(CM.carpeta(n), r'E:\DAE MASTER').split(os.sep)
    b_tl = CM.bin_de(mp, rel + ['10 TIMELINE SEBASTIAN'])
    cache = {}
    for it in m['video'] + m['audio']:
        _mpi(mp, it['archivo'], cache)
    mp.SetCurrentFolder(b_tl)
    tl = mp.CreateEmptyTimeline(nombre)
    pr.SetCurrentTimeline(tl)
    st = tl.GetStartFrame()
    nv = max(x['pista'] for x in m['video'])
    na = max(x['pista'] for x in m['audio'])
    while tl.GetTrackCount('video') < nv:
        tl.AddTrack('video')
    # pistas de audio estereo (un mono en pista estereo suena solo a la izquierda)
    for k in range(1, int(tl.GetTrackCount('audio')) + 1):
        pass
    while tl.GetTrackCount('audio') < na:
        tl.AddTrack('audio', 'stereo')
    tipos = [tl.GetTrackSubType('audio', k) if hasattr(tl, 'GetTrackSubType') else '?'
             for k in range(1, int(tl.GetTrackCount('audio')) + 1)]
    infos = []
    for it in sorted(m['video'], key=lambda x: (x['pista'], x['en'])):
        infos.append({'mediaPoolItem': cache[it['archivo']], 'startFrame': it['ini'],
                      'endFrame': it['fin'], 'trackIndex': it['pista'], 'recordFrame': st + it['en'],
                      'mediaType': 1})
    for it in m['audio']:
        mpi = cache[it['archivo']]
        fin = it.get('fin') or int(mpi.GetClipProperty('Frames') or 0) or m['largo']
        infos.append({'mediaPoolItem': mpi, 'startFrame': it.get('ini', 0), 'endFrame': fin,
                      'trackIndex': it['pista'], 'recordFrame': st + it['en'], 'mediaType': 2})
    # de a uno: AppendToTimeline con varios a veces corre los vecinos un cuadro
    res = []
    for ci in infos:
        r = mp.AppendToTimeline([ci])
        res.append(bool(r))
    # verificacion
    mal = []
    for it in m['video']:
        hit = [x for x in tl.GetItemListInTrack('video', it['pista']) or []
               if x.GetStart() - st == it['en']]
        if not hit or hit[0].GetEnd() - hit[0].GetStart() != it['fin'] - it['ini']:
            mal.append((it['pista'], it['en'], [(x.GetStart() - st, x.GetEnd() - st)
                                                for x in tl.GetItemListInTrack('video', it['pista'])]))
    w('linea', nombre, 'items', sum(res), '/', len(res), 'tipos audio', tipos, 'mal', mal)
    return tl, mal


def drt(pr, n):
    m = cargar(n)
    tl = [pr.GetTimelineByIndex(i) for i in range(1, int(pr.GetTimelineCount()) + 1)
          if pr.GetTimelineByIndex(i).GetName() == m['linea']][0]
    d = os.path.join(CM.carpeta(n), '10 TIMELINE SEBASTIAN')
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, m['linea'] + '.drt')
    pr.SetCurrentTimeline(tl)
    import DaVinciResolveScript as dvr
    r = tl.Export(p, dvr.scriptapp('Resolve').EXPORT_DRT)
    return p, r


def nombre_salida(n):
    return 'CH U1 CASO %02d - %s V2' % (n, CM.carpeta(n).split(' - ', 1)[1])


def kick_master(pr, n):
    """Master de archivo: MP4 H.264 NVIDIA a 80000 (~32 Mbps), AAC. Vuelve sin
    esperar; el estado se mira con ch_render1.estado()."""
    m = cargar(n)
    tl = [pr.GetTimelineByIndex(i) for i in range(1, int(pr.GetTimelineCount()) + 1)
          if pr.GetTimelineByIndex(i).GetName() == m['linea']][0]
    pr.SetCurrentTimeline(tl)
    st = tl.GetStartFrame()
    dest = os.path.join(CM.carpeta(n), '05 EXPORTS', '_master v2')
    os.makedirs(dest, exist_ok=True)
    nm = nombre_salida(n) + ' master'
    if any(f.startswith(nm + '.') for f in os.listdir(dest)):
        return 'YA EXISTE ' + nm
    pr.DeleteAllRenderJobs()
    pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    s = {'SelectAllFrames': False, 'MarkIn': st, 'MarkOut': st + m['largo'] - 1, 'TargetDir': dest,
         'CustomName': nm, 'ExportVideo': True, 'ExportAudio': True, 'FormatWidth': 1920,
         'FormatHeight': 1080, 'VideoQuality': 80000, 'AudioCodec': 'aac', 'AudioSampleRate': 48000}
    for _ in range(5):
        if pr.SetRenderSettings(s):
            break
        [pr.SetRenderSettings({k: v}) for k, v in s.items()]
        time.sleep(1)
    else:
        return 'AJUSTES'
    job = pr.AddRenderJob()
    pr.StartRendering([job], False)
    return 'ANDANDO ' + nm


def entrega(n):
    """Paso 2 de la receta Fiscalia: x264 CRF 18 slow, tune animation. El audio
    sale de la mezcla v2 (voz + fondo, -18 LUFS, techo -1 dBTP) en una sola
    pasada AAC 196k; el master de Resolve queda de archivo."""
    caso = CM.carpeta(n)
    nm = nombre_salida(n)
    master = os.path.join(caso, '05 EXPORTS', '_master v2', nm + ' master.mp4')
    mezcla = os.path.join(caso, '03 VOCES', 'v2', 'CH_U1_C%02d_mezcla_v2.wav' % n)
    out = os.path.join(caso, '05 EXPORTS', nm + '.mp4')
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', master, '-i', mezcla, '-map', '0:v:0', '-map', '1:a:0',
           '-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-tune', 'animation',
           '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
           '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
           '-c:a', 'aac', '-b:a', '196k', '-ar', '48000', '-shortest', '-movflags', '+faststart', out]
    subprocess.run(cmd, check=True)
    return out


if __name__ == '__main__':
    # uso suelto (proceso aparte): python ch_montar_v2.py entrega 6
    if sys.argv[1] == 'entrega':
        for x in sys.argv[2:]:
            w(entrega(int(x)))
    w('LISTO')
