# -*- coding: utf-8 -*-
"""Quita «Tarea del foro» de los casos ya entregados de Bienes U1, Bienes U2 y SRPA U5C1 (23 nov 2026).

El pedido llegó con el C5U3 («esto no es un foro, quitar toda la línea que dice Tarea del foro») y se extendió
a todos los casos entregados que tienen ese antetítulo. Para cada caso:

- Se **duplica** la línea entregada; la vieja no se toca.
- En V3, el cartón de la pausa (`…_p2_foro….mov`) cambia por su `… v2.mov`, en el mismo cuadro y con la misma
  duración. Los cartones v2 salen de `herramientas/cartones/foros_v2.py`: primero se rinde la especificación vieja
  con el `cartones_ta` de hoy y tiene que dar los mismos cuadros que el cartón entregado (framemd5, 0 distintos);
  después se rinde sin el `ante`.
- El intro y el outro FGN (V1 y A1) habían quedado sin medio en el pool: se quitan y se vuelven a poner desde
  ` 00 COMUNES/INTRO` (`FGN_intro_version7.mp4`) en los mismos cuadros. En U5C1 el bumper dura 194 cuadros (los
  primeros 194 de 222), igual que en la línea vieja.
- Se comparan las dos líneas ítem por ítem: la única diferencia debe ser el cartón.
- Se exporta el `.drt` a `10 TIMELINE SEBASTIAN`.

Se corre desde el puente (run_inline, `resolve` ya enlazado), un caso por llamada:

    exec(open('D:/DAE/_repo/herramientas/montaje/foros_v2_lineas.py', encoding='utf-8').read()); correr('c5u1')

Idempotente: si la línea nueva ya existe, no la vuelve a crear y solo arregla lo que falte.
"""
import os

INTRO = r'E:\DAE MASTER\00 COMUNES\INTRO\FGN_intro_version7.mp4'
B5 = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/'
CASOS = {
    'c5u1': dict(vieja='C5U1 LOGISTICA CMR - a la voz', nueva='C5U1 LOGISTICA CMR - a la voz v2',
                 carton='C5U1_p2_foro_v264.mov', rango=(4610, 4874), outro=4993, bumper=222,
                 caso=B5 + 'UNIDAD 1/CASO 01 - logistica CMR del norte'),
    'c5u2': dict(vieja='C5U2 SINIESTRO VIAL - a la voz v2', nueva='C5U2 SINIESTRO VIAL - a la voz v3',
                 carton='C5U2_p2_foro.mov', rango=(5122, 5418), outro=5537, bumper=222,
                 caso=B5 + 'UNIDAD 2/CASO 02 - el siniestro vial'),
    'u5c1': dict(vieja='U5C1 LOS CHAPULINES - a la voz', nueva='U5C1 LOS CHAPULINES - a la voz v2',
                 carton='U5C1_p2_foro.mov', rango=(4070, 4262), outro=4381, bumper=194,
                 caso='E:/DAE MASTER/CURSO 1 - SRPA/UNIDAD 1 - PROFE CARLOS HUMBERTO/UNIDAD 5/cASO 1'),
}


def _n(p):
    return os.path.normcase(os.path.abspath(p or ''))


def lineas(pr):
    return {pr.GetTimelineByIndex(i).GetName(): pr.GetTimelineByIndex(i)
            for i in range(1, pr.GetTimelineCount() + 1)}


def en_pool(mp, ruta):
    """(carpeta, clip) del clip del pool cuyo archivo es `ruta`; (None, None) si no está."""
    q = _n(ruta)

    def rec(f):
        for c in f.GetClipList() or []:
            if _n(c.GetClipProperty('File Path')) == q:
                return f, c
        for s in f.GetSubFolderList() or []:
            r = rec(s)
            if r[1]:
                return r
        return None, None
    return rec(mp.GetRootFolder())


def mapa(tl):
    t0, out = tl.GetStartFrame(), []
    for k in ('video', 'audio'):
        for n in range(1, tl.GetTrackCount(k) + 1):
            for it in tl.GetItemListInTrack(k, n) or []:
                out.append((k[0] + str(n), it.GetName(), it.GetStart() - t0, it.GetEnd() - t0,
                            it.GetLeftOffset(), it.GetRightOffset()))
    return out


def poner(mp, tl, clip, ini, n, pista, tipo):
    """Pone `n` cuadros de `clip` (desde su cuadro 0) en `ini`. Comprueba la duración que quedó: si el extremo
    resultó inclusivo, lo quita y lo vuelve a poner un cuadro más corto."""
    t0 = tl.GetStartFrame()
    k = 'video' if tipo == 1 else 'audio'
    for fin in (n, n - 1):
        r = mp.AppendToTimeline([{'mediaPoolItem': clip, 'startFrame': 0, 'endFrame': fin,
                                  'trackIndex': pista, 'recordFrame': t0 + ini, 'mediaType': tipo}])
        it = [x for x in tl.GetItemListInTrack(k, pista) or [] if x.GetStart() - t0 == ini]
        if r and it and it[0].GetEnd() - it[0].GetStart() == n:
            return it[0]
        if it:
            tl.DeleteClips(it, False)
    raise SystemExit('no quedó %s en %s%d %d (+%d)' % (clip.GetName(), k[0], pista, ini, n))


def correr(clave):
    pr = resolve.GetProjectManager().GetCurrentProject()  # noqa: F821 (lo enlaza el puente)
    mp = pr.GetMediaPool()
    c = CASOS[clave]
    L = lineas(pr)
    vieja = L[c['vieja']]
    if c['nueva'] in L:
        tl = L[c['nueva']]
        print('la línea ya estaba:', c['nueva'])
    else:
        pr.SetCurrentTimeline(vieja)
        tl = vieja.DuplicateTimeline(c['nueva'])
        if not tl:
            raise SystemExit('no se pudo duplicar ' + c['vieja'])
        print('duplicada:', c['nueva'])
    pr.SetCurrentTimeline(tl)
    t0 = tl.GetStartFrame()
    ini, fin = c['rango']

    # 1. el cartón de la pausa
    base = os.path.splitext(c['carton'])[0]
    nuevo = c['caso'] + '/02 CARTONES/' + base + ' v2.mov'
    if not os.path.exists(nuevo):
        raise SystemExit('falta ' + nuevo)
    v3 = [x for x in tl.GetItemListInTrack('video', 3) or [] if x.GetName() == c['carton']]
    if v3:
        it = v3[0]
        assert (it.GetStart() - t0, it.GetEnd() - t0) == (ini, fin), (it.GetStart() - t0, it.GetEnd() - t0)
        carpeta, _ = en_pool(mp, it.GetMediaPoolItem().GetClipProperty('File Path'))
        _, clip = en_pool(mp, nuevo)
        if clip is None:
            mp.SetCurrentFolder(carpeta)
            imp = mp.ImportMedia([nuevo]) or []
            clip = imp[0] if imp else None
            if clip is None:
                raise SystemExit('no se pudo importar ' + nuevo)
            print('importado a', carpeta.GetName(), ':', clip.GetName())
        if int(clip.GetClipProperty('Frames')) != fin - ini:
            raise SystemExit('el v2 dura %s, la ranura %d' % (clip.GetClipProperty('Frames'), fin - ini))
        tl.DeleteClips([it], False)
        poner(mp, tl, clip, ini, fin - ini, 3, 1)
        print('cartón cambiado en V3 %d-%d' % (ini, fin))

    # 2. intro y outro sin medio
    _, intro = en_pool(mp, INTRO)
    if intro is None or not os.path.exists(INTRO):
        raise SystemExit('no está el intro en el pool')
    b = c['bumper']
    for k, tipo in (('video', 1), ('audio', 2)):
        malos = [x for x in tl.GetItemListInTrack(k, 1) or []
                 if x.GetMediaPoolItem() is None and x.GetName() == 'FGN_intro_version7.mp4']
        pos = sorted((x.GetStart() - t0, x.GetEnd() - t0) for x in malos)
        if not malos:
            continue
        assert pos == [(0, b), (c['outro'], c['outro'] + b)], pos
        tl.DeleteClips(malos, False)
        for a in (0, c['outro']):
            poner(mp, tl, intro, a, b, 1, tipo)
        print('intro y outro repuestos en %s1' % k[0].upper())

    # 3. las dos líneas, ítem por ítem
    mv, mn = mapa(vieja), mapa(tl)
    solo_v = [x for x in mv if x not in mn]
    solo_n = [x for x in mn if x not in mv]
    print('ítems: vieja %d, nueva %d' % (len(mv), len(mn)))
    print('solo en la vieja:', solo_v)
    print('solo en la nueva:', solo_n)
    esperado = (len(solo_v) == 1 and len(solo_n) == 1 and solo_v[0][0] == solo_n[0][0] == 'v3'
                and solo_v[0][2:] == solo_n[0][2:] and solo_n[0][1] == base + ' v2.mov')
    print('DIFERENCIA ESPERADA' if esperado else 'OJO: HAY OTRAS DIFERENCIAS')

    # 4. sin medios offline
    sin = []
    for k in ('video', 'audio'):
        for n in range(1, tl.GetTrackCount(k) + 1):
            for x in tl.GetItemListInTrack(k, n) or []:
                m = x.GetMediaPoolItem()
                r = m.GetClipProperty('File Path') if m else ''
                if m is None or (r and not os.path.exists(r)):
                    sin.append('%s%d %s %d' % (k[0], n, x.GetName(), x.GetStart() - t0))
    print('offline:', sin or 'ninguno')

    # 5. el .drt
    if esperado and not sin:
        d = c['caso'] + '/10 TIMELINE SEBASTIAN/' + c['nueva'] + '.drt'
        print('drt', tl.Export(d, resolve.EXPORT_DRT), d)  # noqa: F821
    return esperado and not sin
