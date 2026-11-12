# -*- coding: utf-8 -*-
r"""Línea de Resolve de la introducción al curso de Delitos ambientales (dentro de run_inline).

    exec(open(r'D:\DAE\_repo\herramientas\montaje\ic_linea.py', encoding='utf-8').read())
    construir(); drt(); exportar(1)

Es `te_linea.py` con el plan `plan_ic` (el esqueleto de `srpa_linea.py`):
- V1: intro FGN 0–194, el clip desde el 409, el cartón de título de cierre y el
  outro, todo a 1:1;
- V2: el cartón de título 194–409 y los cartones de caja;
- V3: los motion graphics;
- V4: los lower thirds;
- A1: el audio.
"""
import os
import sys
import importlib

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\introduccion_curso')
import plan_ic as P  # noqa: E402
importlib.reload(P)

TIT_INI, TIT_DUR, INTRO_DUR = 194, 215, 194
PISTA = {'carton': 2, 'mg_act': 3, 'mg_lista': 3, 'lt': 4}
NOMBRES_V = {1: 'VIDEO', 2: 'CARTONES', 3: 'MOTION GRAPHICS', 4: 'LOWER THIRD'}


def carpeta_pool(*partes):
    f = mp.GetRootFolder()
    for p in tuple(P.BIN) + partes:
        nxt = [s for s in f.GetSubFolderList() if s.GetName().strip() == p]
        f = nxt[0] if nxt else mp.AddSubFolder(f, p)
    return f


def por_ruta(folder, ruta):
    for c in folder.GetClipList() or []:
        if os.path.normcase(c.GetClipProperty('File Path') or '') == os.path.normcase(os.path.normpath(ruta)):
            return c
    return None


def linea(n):
    for i in range(1, project.GetTimelineCount() + 1):
        t = project.GetTimelineByIndex(i)
        if t.GetName() == n:
            return t
    return None


def archivo(clave, tipo):
    if tipo in ('mg_act', 'mg_lista'):
        return '%s/09 MOTION GRAPHICS/%s_%s.mov' % (P.R, P.PREFIJO, clave)
    return '%s/02 CARTONES/%s_%s.mov' % (P.R, P.PREFIJO, clave)


def importar():
    lotes = {'01 VIDEO': [P.COMPUESTO], '02 CARTONES': [P.TITULO], '09 MOTION GRAPHICS': []}
    for clave, tipo, *_ in P.ITEMS:
        lotes['09 MOTION GRAPHICS' if tipo.startswith('mg') else '02 CARTONES'].append(archivo(clave, tipo))
    pool = {}
    for b, rutas in lotes.items():
        f = carpeta_pool(b)
        faltan = [r for r in rutas if por_ruta(f, r) is None]
        for r in faltan:
            if not os.path.exists(r):
                raise SystemExit('FALTA EN DISCO: ' + r)
        if faltan:
            mp.SetCurrentFolder(f)
            mp.ImportMedia([os.path.normpath(r) for r in faltan])
        for r in rutas:
            c = por_ruta(f, r)
            if c is None:
                raise SystemExit('NO ENTRÓ AL POOL: ' + r)
            if b == '09 MOTION GRAPHICS':
                c.SetClipProperty('Alpha mode', 'Premultiplied')
            pool[r] = c
    return pool


def poner(tl, mpi, pista, cuadro, tipo=None, src_fin=None):
    info = {'mediaPoolItem': mpi, 'startFrame': 0, 'trackIndex': pista, 'recordFrame': tl.GetStartFrame() + cuadro}
    if src_fin is not None:
        info['endFrame'] = src_fin
    if tipo:
        info['mediaType'] = tipo
    r = mp.AppendToTimeline([info])
    if not r or r[0] is None:
        raise SystemExit('NO SE PUDO PONER %s en V%d %d' % (mpi.GetName(), pista, cuadro))
    return r[0]


def construir():
    resolve.OpenPage('edit')
    if linea(P.NOMBRE_LINEA) is not None:
        raise SystemExit('ya existe la línea ' + P.NOMBRE_LINEA)
    pool = importar()
    intro = linea('MA - U1 - INTRODUCCION').GetItemListInTrack('video', 1)[0].GetMediaPoolItem()
    mp.SetCurrentFolder(carpeta_pool('10 TIMELINE SEBASTIAN'))
    tl = mp.CreateEmptyTimeline(P.NOMBRE_LINEA)
    project.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < 4:
        tl.AddTrack('video')
    for i, n in NOMBRES_V.items():
        tl.SetTrackName('video', i, n)
    tl.SetTrackName('audio', 1, 'VIDEO')
    poner(tl, intro, 1, 0, tipo=1, src_fin=INTRO_DUR)
    poner(tl, intro, 1, 0, tipo=2, src_fin=INTRO_DUR)
    poner(tl, pool[P.TITULO], 2, TIT_INI, tipo=1)
    clip = poner(tl, pool[P.COMPUESTO], 1, P.CLIP0, tipo=1)
    poner(tl, pool[P.COMPUESTO], 1, P.CLIP0, tipo=2)
    fin = clip.GetEnd() - tl.GetStartFrame()
    poner(tl, pool[P.TITULO], 1, fin, tipo=1)
    poner(tl, intro, 1, fin + TIT_DUR, tipo=1, src_fin=INTRO_DUR)
    poner(tl, intro, 1, fin + TIT_DUR, tipo=2, src_fin=INTRO_DUR)
    for clave, tipo, t0, t1, _c in P.ITEMS:
        poner(tl, pool[archivo(clave, tipo)], PISTA[tipo], P.cuadro(t0), tipo=1)
    return revisar()


def revisar():
    tl = linea(P.NOMBRE_LINEA)
    t0 = tl.GetStartFrame()
    malos = []
    for k in ('video', 'audio'):
        for n in range(1, tl.GetTrackCount(k) + 1):
            its = tl.GetItemListInTrack(k, n) or []
            print('%s%d %-16s %3d ítems' % (k[0].upper(), n, tl.GetTrackName(k, n), len(its)))
            for it in its:
                mpi = it.GetMediaPoolItem()
                if k == 'video' and n > 1 and 'titulo' not in it.GetName():
                    if it.GetEnd() - it.GetStart() != int(mpi.GetClipProperty('Frames')):
                        malos.append(it.GetName())
                if k == 'video' and n == 1 and (it.GetProperty('ZoomX') != 1.0 or it.GetProperty('Pan') != 0.0):
                    malos.append('zoom ' + it.GetName())
    print('fin de la línea %d  problemas %s' % (tl.GetEndFrame() - t0, malos or 'ninguno'))
    return tl


def drt():
    tl = linea(P.NOMBRE_LINEA)
    out = '%s/10 TIMELINE SEBASTIAN/%s.drt' % (P.R, P.NOMBRE_LINEA)
    print('drt', tl.Export(os.path.normpath(out), resolve.EXPORT_DRT), out)


def exportar(n=1):
    tl = linea(P.NOMBRE_LINEA)
    project.SetCurrentTimeline(tl)
    resolve.OpenPage('deliver')
    dst = '%s/05 EXPORTS' % P.R
    nombre = P.EXPORT % n
    if os.path.exists('%s/%s.mov' % (dst, nombre)):
        raise SystemExit('ya existe ' + nombre)
    project.LoadRenderPreset('H.264 Master')
    project.SetCurrentRenderFormatAndCodec('mov', 'H264')
    project.SetRenderSettings({
        'TargetDir': os.path.normpath(dst), 'CustomName': nombre,
        'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': 23.976,
        'VideoQuality': 6000, 'EncodingProfile': 'High', 'AudioCodec': 'aac', 'AudioSampleRate': 48000,
        'ExportVideo': True, 'ExportAudio': True, 'SelectAllFrames': True})
    job = project.AddRenderJob()
    print('job', job, nombre, project.StartRendering([job]))
    return job
