# -*- coding: utf-8 -*-
r"""Línea de Resolve del conversatorio «Articulación DEMA y DECOC» (dentro de run_inline).

    exec(open(r'D:\DAE\_repo\herramientas\montaje\dema_linea.py', encoding='utf-8').read())
    construir()     # importa los medios y arma la línea
    revisar()       # lista las pistas

El esqueleto es el de las introducciones MA:
- V1 VIDEO: intro FGN 0–194, la composición desde el 409, el cartón de título
  de cierre al final del clip (zoom 1,16, pan 145) y el outro FGN (zoom 1,16,
  pan 145).
- V2 CARTONES: el cartón de título 194–409 y los cartones de caja.
- V3 MOTION GRAPHICS: las composiciones de After Effects.
- V4 LOWER THIRD: los cuatro lower thirds.
- A1 VIDEO: el audio del intro, de la composición (con el nivel ya ajustado) y
  del outro.

La línea va en el bin `10 TIMELINE SEBASTIAN` del conversatorio, y el `.drt` en
la misma carpeta del disco.
"""
import os
import sys
import importlib

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\conversatorio_dema')
import plan_dema as P  # noqa: E402
importlib.reload(P)

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
R = CURSO + '/UNIDAD 1/CONVERSATORIO - Articulacion DEMA y DECOC'
BIN = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE', 'UNIDAD 1', 'CONVERSATORIO - Articulacion DEMA y DECOC']
NOMBRE = 'MA - U1 - CONVERSATORIO DEMA Y DECOC'
COMPOSICION = R + '/01 VIDEO/DEMA_DECOC_composicion_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo conversatorio DEMA y DECOC.mp4'
ZOOM, PAN = 1.16, 145.0
TIT_INI, TIT_DUR, INTRO_DUR = 194, 215, 194
PISTA = {'carton': 2, 'mg_act': 3, 'mg_lista': 3, 'lt': 4}
NOMBRES_V = {1: 'VIDEO', 2: 'CARTONES', 3: 'MOTION GRAPHICS', 4: 'LOWER THIRD'}


def carpeta(*partes):
    f = mp.GetRootFolder()
    for p in tuple(BIN) + partes:
        nxt = [s for s in f.GetSubFolderList() if s.GetName().strip() == p]
        f = nxt[0] if nxt else mp.AddSubFolder(f, p)
    return f


def por_nombre(folder, n):
    for c in folder.GetClipList() or []:
        if c.GetName() == n:
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
        return '%s/09 MOTION GRAPHICS/DEMA_%s.mov' % (R, clave)
    return '%s/02 CARTONES/DEMA_%s.mov' % (R, clave)


def importar():
    lotes = {'01 VIDEO': [COMPOSICION], '02 CARTONES': [TITULO], '09 MOTION GRAPHICS': []}
    for clave, tipo, *_ in P.ITEMS:
        lotes['09 MOTION GRAPHICS' if tipo.startswith('mg') else '02 CARTONES'].append(archivo(clave, tipo))
    pool = {}
    for b, rutas in lotes.items():
        f = carpeta(b)
        faltan = [r for r in rutas if por_nombre(f, os.path.basename(r)) is None]
        for r in faltan:
            if not os.path.exists(r):
                raise SystemExit('FALTA EN DISCO: ' + r)
        if faltan:
            mp.SetCurrentFolder(f)
            mp.ImportMedia([r.replace('/', '\\') for r in faltan])
        for r in rutas:
            c = por_nombre(f, os.path.basename(r))
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


def construir():
    resolve.OpenPage('edit')
    pool = importar()
    intro = linea('MA - U1 - INTRODUCCION').GetItemListInTrack('video', 1)[0].GetMediaPoolItem()
    if linea(NOMBRE) is not None:
        raise SystemExit('ya existe la línea ' + NOMBRE)
    mp.SetCurrentFolder(carpeta('10 TIMELINE SEBASTIAN'))
    tl = mp.CreateEmptyTimeline(NOMBRE)
    project.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < 4:
        tl.AddTrack('video')
    for i, n in NOMBRES_V.items():
        tl.SetTrackName('video', i, n)
    tl.SetTrackName('audio', 1, 'VIDEO')

    poner(tl, intro, 1, 0, tipo=1, src_fin=INTRO_DUR)
    poner(tl, intro, 1, 0, tipo=2, src_fin=INTRO_DUR)
    titulo = pool[TITULO]
    poner(tl, titulo, 2, TIT_INI, tipo=1)
    clip = poner(tl, pool[COMPOSICION], 1, P.CLIP0)
    if not [x for x in tl.GetItemListInTrack('audio', 1) if x.GetName() == clip.GetName()]:
        poner(tl, pool[COMPOSICION], 1, P.CLIP0, tipo=2)
    fin = clip.GetEnd() - tl.GetStartFrame()
    encuadre(poner(tl, titulo, 1, fin, tipo=1))
    encuadre(poner(tl, intro, 1, fin + TIT_DUR, tipo=1, src_fin=INTRO_DUR))
    poner(tl, intro, 1, fin + TIT_DUR, tipo=2, src_fin=INTRO_DUR)

    for clave, tipo, lado, t0, t1, _c in P.ITEMS:
        poner(tl, pool[archivo(clave, tipo)], PISTA[tipo], P.cuadro(t0), tipo=1)
    return revisar()


def revisar():
    tl = linea(NOMBRE)
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
    print('fin de la línea', tl.GetEndFrame() - t0, 'problemas', malos or 'ninguno')
    return tl
