# -*- coding: utf-8 -*-
r"""Cirugia sobre una linea que Sebastian ya toco: cambios puntuales de items,
SIN remontar (31 oct, la revision del C2). Complementa a
`reemplazar_en_sitio_jr.py` (que solo cambia el MEDIO de un clip).

    python cirugia_jr.py C2 v4                   rehace la pista CARTONES (V4)
                                                 completa segun el plan actual
    python cirugia_jr.py C2 quitar V3 <archivo> [pos]
                                                 quita el item de esa pista que
                                                 usa ese archivo (y esa posicion
                                                 relativa, si se da)
    python cirugia_jr.py C2 poner V8 <ruta> <pos> <largo>
                                                 pone un clip nuevo en esa pista
                                                 en el cuadro `pos` de la linea
    python cirugia_jr.py C2 relink <ruta> [...]  relee archivos reescritos en
                                                 su sitio (ReplaceClip)
    python cirugia_jr.py C2 retrato              imprime el retrato de la linea
                                                 contra el plan (que cambio)

Antes y despues se toma el RETRATO (pista, archivo, entrada, salida,
desplazamiento) y se imprime exactamente lo que cambio: nada mas que lo
pedido puede cambiar, y si cambia, se dice y NO se guarda el proyecto.
Las posiciones son cuadros desde el inicio de la linea (como en `plan`).
"""
import os
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import jr_pieza as SP                                     # noqa: E402
import reemplazar_en_sitio_jr as RS                       # noqa: E402

PISTA = {'V1': ('video', 1), 'V2': ('video', 2), 'V3': ('video', 3), 'V4': ('video', 4),
         'V6': ('video', 6), 'V8': ('video', 8), 'A1': ('audio', 1), 'A4': ('audio', 4),
         'A5': ('audio', 5)}


def w(*a):
    print(*a, flush=True)


def linea(L):
    resolve = SP._resolve()
    pr = resolve.GetProjectManager().GetCurrentProject()
    nl = SP.nombre_linea(L)
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t and t.GetName() == nl:
            pr.SetCurrentTimeline(t)
            return resolve, pr, t
    raise SystemExit('no hay linea %s' % nl)


def retrato_rel(tl):
    s0 = tl.GetStartFrame()
    return [(tipo, tr, st - s0, en - st, off, nm) for tipo, tr, st, en, off, nm in RS.retrato(tl)]


def diferencias(antes, despues):
    a, b = set(antes), set(despues)
    return sorted(a - b), sorted(b - a)


def item_de(tl, tipo, tr, archivo, pos=None):
    s0 = tl.GetStartFrame()
    for it in tl.GetItemListInTrack(tipo, tr) or []:
        mpi = it.GetMediaPoolItem()
        fp = mpi.GetClipProperty('File Path') if mpi else ''
        if os.path.basename((fp or it.GetName()).replace('/', os.sep)) == os.path.basename(archivo):
            if pos is None or it.GetStart() - s0 == pos:
                return it
    return None


def pool_item(pr, ruta):
    mp = pr.GetMediaPool()
    quiero = RS.norm(ruta)
    out = RS.items_de(mp.GetRootFolder(), {quiero}, [])
    if out:
        return out[0]
    # no esta en el pool: se importa al bin de la ranura (10 TIMELINE SEBASTIAN...)
    import rutas_jr as R
    L = os.path.basename(ruta).split('_')[1]
    raiz = mp.GetRootFolder()
    rel = os.path.relpath(os.path.dirname(ruta), r'E:\DAE MASTER').split(os.sep)
    f = raiz
    for q in rel:
        f = next((x for x in f.GetSubFolderList() if x.GetName() == q), None) or mp.AddSubFolder(f, q)
    mp.SetCurrentFolder(f)
    mp.ImportMedia([ruta])
    out = RS.items_de(mp.GetRootFolder(), {quiero}, [])
    assert out, 'no entro al pool: %s' % ruta
    return out[0]


def poner(pr, tl, pista, ruta, pos, largo):
    tipo, tr = PISTA[pista]
    it = pool_item(pr, ruta)
    r = pr.GetMediaPool().AppendToTimeline([{
        'mediaPoolItem': it, 'startFrame': 0, 'endFrame': largo,
        'trackIndex': tr, 'recordFrame': tl.GetStartFrame() + pos,
        'mediaType': 1 if tipo == 'video' else 2}])
    assert r, 'no entro %s en %s %d' % (os.path.basename(ruta), pista, pos)


def quitar(tl, pista, archivo, pos=None):
    tipo, tr = PISTA[pista]
    it = item_de(tl, tipo, tr, archivo, pos)
    assert it is not None, 'no hay %s en %s (pos %s)' % (archivo, pista, pos)
    assert tl.DeleteClips([it]), 'no se pudo quitar %s' % archivo


def main():
    L, paso = sys.argv[1].upper(), sys.argv[2]
    args = sys.argv[3:]
    resolve, pr, tl = linea(L)
    antes = retrato_rel(tl)
    esperado_fuera, esperado_dentro = [], []
    if paso == 'retrato':
        v1, v4, v6, voz, mus, ini, dur, tot = SP.plan(L)
        v2, v3, v8, _ = SP.capas(L)
        plan = set()
        for tr, lst in ((1, v1), (2, v2), (3, v3), (4, v4), (6, v6), (8, v8)):
            for pos, largo, p in lst:
                plan.add(('video', tr, pos, largo, 0, os.path.basename(p)))
        hay = set(x for x in antes if x[0] == 'video')
        w('en la linea y no en el plan:', sorted(hay - plan) or 'nada')
        w('en el plan y no en la linea:', sorted(plan - hay) or 'nada')
        return
    if paso == 'v4':
        v1, v4, v6, voz, mus, ini, dur, tot = SP.plan(L)
        viejos = tl.GetItemListInTrack('video', 4) or []
        if viejos:
            assert tl.DeleteClips(viejos), 'no se pudo vaciar V4'
        for pos, largo, p in v4:
            poner(pr, tl, 'V4', p, pos, largo)
        esperado_fuera = [x for x in antes if x[0] == 'video' and x[1] == 4]
        esperado_dentro = [('video', 4, pos, largo, 0, os.path.basename(p)) for pos, largo, p in v4]
    elif paso == 'quitar':
        pista, archivo = args[0], args[1]
        pos = int(args[2]) if len(args) > 2 else None
        quitar(tl, pista, archivo, pos)
        tipo, tr = PISTA[pista]
        esperado_fuera = [x for x in antes if x[0] == tipo and x[1] == tr
                          and x[5] == os.path.basename(archivo) and (pos is None or x[2] == pos)]
        assert len(esperado_fuera) == 1, esperado_fuera
    elif paso == 'poner':
        pista, ruta, pos, largo = args[0], args[1], int(args[2]), int(args[3])
        poner(pr, tl, pista, ruta, pos, largo)
        tipo, tr = PISTA[pista]
        esperado_dentro = [(tipo, tr, pos, largo, 0, os.path.basename(ruta))]
    elif paso == 'relink':
        mp = pr.GetMediaPool()
        for ruta in args:
            items = RS.items_de(mp.GetRootFolder(), {RS.norm(ruta)}, [])
            assert items, 'no esta en el pool: %s' % ruta
            for it in items:
                assert it.ReplaceClip(ruta), 'ReplaceClip fallo: %s' % ruta
            w('   releido', os.path.basename(ruta))
    else:
        raise SystemExit('paso?')
    despues = retrato_rel(tl)
    fuera, dentro = diferencias(antes, despues)
    # un item que sale y vuelve a entrar identico (mismo archivo, misma
    # posicion) no aparece en ninguna diferencia: no falta nada
    igual = set(antes) & set(despues)
    mal = [x for x in fuera if x not in esperado_fuera] + [x for x in dentro if x not in esperado_dentro]
    falta = [x for x in esperado_fuera if x not in fuera and x not in igual] + \
            [x for x in esperado_dentro if x not in dentro and x not in igual]
    w('salieron %d, entraron %d' % (len(fuera), len(dentro)))
    if mal or falta:
        w('CAMBIO ALGO QUE NO SE PIDIO, NO SE GUARDA:', mal[:10], 'faltan:', falta[:10])
        raise SystemExit(2)
    resolve.GetProjectManager().SaveProject()
    w('guardado;', SP.nombre_linea(L), 'largo', tl.GetEndFrame() - tl.GetStartFrame())


if __name__ == '__main__':
    main()
    w('LISTO')
