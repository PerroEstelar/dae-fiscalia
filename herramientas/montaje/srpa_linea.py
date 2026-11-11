# -*- coding: utf-8 -*-
r"""Líneas de Resolve de los videos de profes del curso SRPA y justicia
restaurativa (dentro de run_inline).

    exec(open(r'D:\DAE\_repo\herramientas\montaje\srpa_linea.py', encoding='utf-8').read())
    construir('u3c')     # importa los medios y arma la línea
    revisar('u3c')       # duración de cada ítem contra su archivo
    drt('u3c')           # exporta el .drt a 10 TIMELINE SEBASTIAN
    exportar('u3c')      # encola y arranca el render de entrega en 05 EXPORTS

El esqueleto es el de las introducciones de Delitos ambientales y el del
conversatorio DEMA y DECOC (`dema_linea.py`):
- V1 VIDEO: intro FGN 0–194, el clip compuesto desde el 409, el cartón de título
  de cierre al final del clip (zoom 1,16, pan 145) y el outro FGN (igual).
- V2 CARTONES: el cartón de título 194–409 y los cartones de caja.
- V3 MOTION GRAPHICS: las composiciones de After Effects (alfa premultiplicado).
- V4 LOWER THIRD.
- A1 VIDEO: el audio del intro, del clip (ya a −19 LUFS) y del outro.
"""
import os
import sys
import importlib

sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
import srpa as S  # noqa: E402
import plan_srpa as P  # noqa: E402
importlib.reload(S)
importlib.reload(P)

ZOOM, PAN = 1.16, 145.0
TIT_INI, TIT_DUR, INTRO_DUR = 194, 215, 194
PISTA = {'carton': 2, 'mg_act': 3, 'mg_lista': 3, 'lt': 4}
NOMBRES_V = {1: 'VIDEO', 2: 'CARTONES', 3: 'MOTION GRAPHICS', 4: 'LOWER THIRD'}


def bin_video(clave):
    return [S.BIN_RAIZ] + S.VIDEOS[clave]['carpeta'].split('/')


def carpeta_pool(clave, *partes):
    f = mp.GetRootFolder()
    for p in tuple(bin_video(clave)) + partes:
        nxt = [s for s in f.GetSubFolderList() if s.GetName().strip() == p]
        f = nxt[0] if nxt else mp.AddSubFolder(f, p)
        if f is None:
            raise SystemExit('no se pudo crear el bin ' + p)
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


def archivo(clave, item, tipo):
    if tipo in ('mg_act', 'mg_lista'):
        return '%s/09 MOTION GRAPHICS/SRPA_%s_%s.mov' % (S.carpeta(clave), clave, item)
    return '%s/02 CARTONES/SRPA_%s_%s.mov' % (S.carpeta(clave), clave, item)


def importar(clave):
    lotes = {'01 VIDEO': [S.compuesto(clave)], '02 CARTONES': [S.titulo_carton(clave)], '09 MOTION GRAPHICS': []}
    for item, tipo, *_ in P.ITEMS[clave]:
        lotes['09 MOTION GRAPHICS' if tipo.startswith('mg') else '02 CARTONES'].append(archivo(clave, item, tipo))
    pool = {}
    for b, rutas in lotes.items():
        f = carpeta_pool(clave, b)
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
    info = {'mediaPoolItem': mpi, 'startFrame': 0, 'trackIndex': pista,
            'recordFrame': tl.GetStartFrame() + cuadro}
    if src_fin is not None:
        info['endFrame'] = src_fin
    if tipo:
        info['mediaType'] = tipo
    r = mp.AppendToTimeline([info])
    if not r or r[0] is None:
        raise SystemExit('NO SE PUDO PONER %s en V%d %d' % (mpi.GetName(), pista, cuadro))
    return r[0]


def encuadre(it):
    it.SetProperty('ZoomX', ZOOM)
    it.SetProperty('ZoomY', ZOOM)
    it.SetProperty('Pan', PAN)


def construir(clave):
    resolve.OpenPage('edit')
    nombre = S.nombre_linea(clave)
    if linea(nombre) is not None:
        raise SystemExit('ya existe la línea ' + nombre)
    pool = importar(clave)
    intro = linea('MA - U1 - INTRODUCCION').GetItemListInTrack('video', 1)[0].GetMediaPoolItem()
    mp.SetCurrentFolder(carpeta_pool(clave, '10 TIMELINE SEBASTIAN'))
    tl = mp.CreateEmptyTimeline(nombre)
    project.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < 4:
        tl.AddTrack('video')
    for i, n in NOMBRES_V.items():
        tl.SetTrackName('video', i, n)
    tl.SetTrackName('audio', 1, 'VIDEO')

    poner(tl, intro, 1, 0, tipo=1, src_fin=INTRO_DUR)
    poner(tl, intro, 1, 0, tipo=2, src_fin=INTRO_DUR)
    titulo = pool[S.titulo_carton(clave)]
    poner(tl, titulo, 2, TIT_INI, tipo=1)
    clip = poner(tl, pool[S.compuesto(clave)], 1, P.CLIP0, tipo=1)
    poner(tl, pool[S.compuesto(clave)], 1, P.CLIP0, tipo=2)
    fin = clip.GetEnd() - tl.GetStartFrame()
    encuadre(poner(tl, titulo, 1, fin, tipo=1))
    encuadre(poner(tl, intro, 1, fin + TIT_DUR, tipo=1, src_fin=INTRO_DUR))
    poner(tl, intro, 1, fin + TIT_DUR, tipo=2, src_fin=INTRO_DUR)

    for item, tipo, t0, t1, _c in P.ITEMS[clave]:
        poner(tl, pool[archivo(clave, item, tipo)], PISTA[tipo], P.cuadro(clave, t0), tipo=1)
    return revisar(clave)


def revisar(clave):
    tl = linea(S.nombre_linea(clave))
    t0 = tl.GetStartFrame()
    malos = []
    for k in ('video', 'audio'):
        for n in range(1, tl.GetTrackCount(k) + 1):
            its = tl.GetItemListInTrack(k, n) or []
            print('%s%d %-16s %3d ítems' % (k[0].upper(), n, tl.GetTrackName(k, n), len(its)))
            for it in its:
                mpi = it.GetMediaPoolItem()
                if mpi is None:
                    malos.append(('sin medio', k, n, it.GetName()))
                    continue
                dur = it.GetEnd() - it.GetStart()
                if k == 'video' and n > 1 and 'titulo' not in it.GetName():
                    esperado = int(mpi.GetClipProperty('Frames'))
                    if dur != esperado:
                        malos.append((it.GetName(), dur, esperado))
    print('%s fin de la línea %d  problemas %s' % (clave, tl.GetEndFrame() - t0, malos or 'ninguno'))
    return tl


def drt(clave):
    tl = linea(S.nombre_linea(clave))
    out = '%s/10 TIMELINE SEBASTIAN/%s.drt' % (S.carpeta(clave), S.nombre_linea(clave))
    ok = tl.Export(os.path.normpath(out), resolve.EXPORT_DRT)
    print(clave, 'drt', ok, out)


def exportar(clave, n=1):
    """Encola el render de entrega con los ajustes de la serie y lo arranca."""
    tl = linea(S.nombre_linea(clave))
    project.SetCurrentTimeline(tl)
    resolve.OpenPage('deliver')
    dst = '%s/05 EXPORTS' % S.carpeta(clave)
    nombre = S.nombre_export(clave, n)
    f = '%s/%s.mov' % (dst, nombre)
    if os.path.exists(f):
        raise SystemExit('ya existe ' + f)
    project.LoadRenderPreset('H.264 Master')
    project.SetCurrentRenderFormatAndCodec('mov', 'H264')
    project.SetRenderSettings({
        'TargetDir': os.path.normpath(dst), 'CustomName': nombre,
        'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': 23.976,
        'VideoQuality': 6000, 'EncodingProfile': 'High',
        'AudioCodec': 'aac', 'AudioSampleRate': 48000,
        'ExportVideo': True, 'ExportAudio': True, 'SelectAllFrames': True,
    })
    job = project.AddRenderJob()
    print(clave, 'job', job, nombre)
    return job
