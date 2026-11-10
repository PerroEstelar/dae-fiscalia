# -*- coding: utf-8 -*-
r"""Arma en Resolve las introducciones U2-U5 de Medio Ambiente con el molde de la U1.

Se corre dentro de `run_inline` (con `resolve`, `project`, `mp` ya ligados):

    exec(open(r'D:\DAE\_repo\herramientas\montaje\ma_intros.py', encoding='utf-8').read())
    importar(2)     # cartón de título, cartones de caja y motion graphics a sus bins
    construir(2)    # línea nueva a partir de la U1
    revisar(2)      # lista lo que quedó en cada pista

`construir` no toca la U1 ni la primera pasada: la línea vieja de la unidad pasa a
llamarse «… (primera pasada)» y la nueva es un duplicado de `MA - U1 -
INTRODUCCION` (así hereda el lower third de V4/V5 como lo dejó Sebastián), al que
se le cambian V1, V2, V3 y A1:

    V1  intro FGN 0-194 (de la U1) · clip de la unidad desde 409 · cartón de título
        de cierre al final del clip (zoom 1,16, pan 145) · outro FGN (zoom 1,16, pan 145)
    V2  CARTONES: cartón de título 194-409 + cartones de caja del plan
    V3  MOTION GRAPHICS: las composiciones de After Effects del plan
    A1  audio del intro, del clip y del outro
"""
import os
import sys

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente')
import importlib  # noqa: E402
import plan_intros as P  # noqa: E402
importlib.reload(P)

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
RAIZ = 'CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
MOLDE = 'MA - U1 - INTRODUCCION'
ZOOM, PAN = 1.16, 145.0
TIT_INI, TIT_DUR, INTRO_DUR = 194, 215, 194


def nombre(u):
    return 'MA - U%d - INTRODUCCION' % u


def carpeta(*partes):
    f = mp.GetRootFolder()
    for p in (RAIZ,) + partes:
        nxt = [s for s in f.GetSubFolderList() if s.GetName() == p]
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


def importar(u):
    """Cartón de título, cartones de caja (v3) y MG al pool; devuelve {nombre: mpi}."""
    out = {}
    bins = (('02 CARTONES', ['%s/UNIDAD %d/02 CARTONES/carton titulo ambientales u%dv3.mp4' % (CURSO, u, u)] +
             ['%s/UNIDAD %d/02 CARTONES/v3/MA_U%d_%s.mov' % (CURSO, u, u, c)
              for c, tipo, *_ in P.UNIDADES[u]['items'] if tipo == 'carton']),
            ('05 MOTION GRAPHICS', ['%s/UNIDAD %d/02 CARTONES/mg/MA_U%d_%s.mov' % (CURSO, u, u, c)
                                    for c, tipo, *_ in P.UNIDADES[u]['items'] if tipo != 'carton']))
    for b, rutas in bins:
        f = carpeta('UNIDAD %d' % u, b)
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
            if b == '05 MOTION GRAPHICS':
                c.SetClipProperty('Alpha mode', 'Premultiplied')
            out[os.path.basename(r)] = c
    return out


def poner(tl, mpi, pista, cuadro, tipo=None, src_fin=None):
    info = {'mediaPoolItem': mpi, 'startFrame': 0, 'trackIndex': pista,
            'recordFrame': tl.GetStartFrame() + cuadro}
    if src_fin is not None:
        info['endFrame'] = src_fin
    if tipo:
        info['mediaType'] = tipo
    r = mp.AppendToTimeline([info])
    if not r or r[0] is None:
        raise SystemExit('NO SE PUDO PONER %s en %s %d' % (mpi.GetName(), pista, cuadro))
    return r[0]


def encuadre(it):
    it.SetProperty('ZoomX', ZOOM)
    it.SetProperty('ZoomY', ZOOM)
    it.SetProperty('Pan', PAN)


def construir(u):
    pool = importar(u)
    molde = linea(MOLDE)
    v1 = molde.GetItemListInTrack('video', 1)
    intro = v1[0].GetMediaPoolItem()
    if intro is None or v1[0].GetStart() != molde.GetStartFrame():
        raise SystemExit('el intro de la U1 no está donde se espera')

    vieja = linea(nombre(u))
    if vieja is not None:
        vieja.SetName(nombre(u) + ' (primera pasada)')
    bin_u = carpeta('UNIDAD %d' % u)
    mp.SetCurrentFolder(bin_u)
    project.SetCurrentTimeline(molde)
    tl = molde.DuplicateTimeline(nombre(u))
    if tl is None:
        raise SystemExit('DuplicateTimeline falló')
    project.SetCurrentTimeline(tl)
    t0 = tl.GetStartFrame()

    # fuera lo propio de la U1 (el intro de V1/A1 y el lower third se quedan)
    borrar = list(tl.GetItemListInTrack('video', 1)[1:]) + list(tl.GetItemListInTrack('video', 2) or []) \
        + list(tl.GetItemListInTrack('video', 3) or []) + list(tl.GetItemListInTrack('audio', 1)[1:])
    if borrar:
        tl.DeleteClips(borrar, False)
    tl.SetTrackName('video', 3, 'MOTION GRAPHICS')

    # clip de la unidad (video y audio enlazados) desde el 409
    clip = por_nombre(carpeta('UNIDAD %d' % u, '01 VIDEO INTRODUCCION'),
                      'Introduccion_delitos_ambientales_unidad-%d.mp4' % u)
    it = poner(tl, clip, 1, P.CLIP0)
    fin = it.GetEnd() - t0
    if not tl.GetItemListInTrack('audio', 1)[-1].GetName().startswith('Introduccion'):
        poner(tl, clip, 1, P.CLIP0, tipo=2)

    titulo = pool['carton titulo ambientales u%dv3.mp4' % u]
    poner(tl, titulo, 2, TIT_INI, tipo=1)
    cierre = poner(tl, titulo, 1, fin, tipo=1)
    encuadre(cierre)
    outro = poner(tl, intro, 1, fin + TIT_DUR, tipo=1, src_fin=INTRO_DUR)
    encuadre(outro)
    poner(tl, intro, 1, fin + TIT_DUR, tipo=2, src_fin=INTRO_DUR)

    for clave, tipo, ini, dur, _d in P.UNIDADES[u]['items']:
        mpi = pool['MA_U%d_%s.mov' % (u, clave)]
        poner(tl, mpi, 2 if tipo == 'carton' else 3, ini, tipo=1)

    if por_nombre(bin_u, nombre(u)) is None:
        for f in (carpeta('UNIDAD 1'), mp.GetCurrentFolder(), mp.GetRootFolder()):
            c = por_nombre(f, nombre(u))
            if c is not None:
                mp.MoveClips([c], bin_u)
                break
    return revisar(u)


def revisar(u):
    tl = linea(nombre(u))
    t0 = tl.GetStartFrame()
    filas = []
    for kind, n in (('video', 1), ('video', 2), ('video', 3), ('video', 4), ('video', 5), ('audio', 1)):
        for it in tl.GetItemListInTrack(kind, n) or []:
            z = it.GetProperty('ZoomX') if kind == 'video' else None
            filas.append('%s%d %-46s %6d-%6d%s%s' % (
                kind[0].upper(), n, it.GetName()[:46], it.GetStart() - t0, it.GetEnd() - t0,
                '' if it.GetMediaPoolItem() or it.GetName() in ('Text+', 'Text', 'Transition', 'Slide')
                else '  SIN MEDIA', '  zoom %.2f pan %.0f' % (z, it.GetProperty('Pan')) if z and z != 1 else ''))
    print('\n'.join(filas))
    print('fin de la línea', tl.GetEndFrame() - t0)
    return tl
