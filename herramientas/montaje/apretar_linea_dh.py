# -*- coding: utf-8 -*-
r"""La linea de una pieza APRETADA, hecha desde la linea de Sebastian.

    python apretar_linea_dh.py U3 <linea_apretada.json>

DH U3, 1 nov. La voz se apreto (`voz/apretar_dh.py`) y todo lo demas se
corre con el mismo mapa de tiempo. NO se remonta desde el plan (eso borraria
sus cambios a mano: en la U3 quito el respiro final, recorto el carton p03 y
dejo la musica terminando donde empieza el outro); se toma SU linea item por
item y se pone cada uno donde el mapa dice, con su medio nuevo cuando lo
hay (ranura corta, carton requemado, voz y cama nuevas, Kling reconformado)
o con el mismo item del pool cuando no cambia (intro, cartones blancos,
marca de agua, rotulo, sonido del intro).

    json = {"linea": nombre, "pieza": cuadros, "items": [
        {"t": "v"|"a", "k": pista, "viejo": archivo en su linea o null,
         "s_viejo": su cuadro de entrada, "ns": entrada nueva, "nl": largo,
         "sf": cuadro de origen, ["sub": carpeta de la unidad, "f": archivo]}]}

Su linea NO se toca: se renombra «… (antes de apretar)» y la nueva toma el
nombre. Nada se borra del pool: lo nuevo entra con otro nombre de archivo.
Al final: retrato de la nueva contra el plan (pista, entrada, largo, archivo),
huecos en V1, largo total, .drt nuevo (el anterior a _descartes) y vuelta a
la linea y la pagina en que estaba Sebastian.
"""
import json
import os
import sys
import time

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import dh_pieza as SP                                   # noqa: E402
import rutas_dh as R                                    # noqa: E402


def norm(p):
    return os.path.normcase(os.path.normpath((p or '').replace('/', os.sep)))


def main(L, plan_json):
    pl = json.load(open(plan_json, encoding='utf-8'))
    resolve = SP._resolve()
    pm = resolve.GetProjectManager()
    pr = pm.GetCurrentProject()
    mp = pr.GetMediaPool()
    antes = {'linea': pr.GetCurrentTimeline().GetName() if pr.GetCurrentTimeline() else None,
             'pagina': resolve.GetCurrentPage()}
    nl = pl['linea']
    suya = None
    nombres = set()
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        nombres.add(t.GetName())
        if t.GetName() == nl:
            suya = t
    assert suya is not None, 'no esta la linea %s' % nl
    T0 = suya.GetStartFrame()
    # sus items, por (tipo, pista, archivo, entrada)
    suyos = {}
    for tipo in ('video', 'audio'):
        for i in range(1, suya.GetTrackCount(tipo) + 1):
            for it in suya.GetItemListInTrack(tipo, i) or []:
                m = it.GetMediaPoolItem()
                fp = m.GetClipProperty('File Path') if m else ''
                suyos[(tipo[0], i, os.path.basename(fp or it.GetName()),
                       it.GetStart() - T0)] = m
    pistas_v = [suya.GetTrackName('video', i) for i in range(1, suya.GetTrackCount('video') + 1)]
    pistas_a = [suya.GetTrackName('audio', i) for i in range(1, suya.GetTrackCount('audio') + 1)]

    # el pool: rutas -> item, y los bins de la unidad
    raiz = mp.GetRootFolder()

    def _todos(f):
        for c in f.GetClipList() or []:
            yield c
        for sf in f.GetSubFolderList() or []:
            yield from _todos(sf)

    def _hijo(f, n):
        for x in f.GetSubFolderList() or []:
            if x.GetName() == n:
                return x
        return None

    def _baja(f, partes):
        for q in partes:
            if q:
                f = _hijo(f, q) or mp.AddSubFolder(f, q)
        return f

    unidad = R.carpeta(L)
    carp = _baja(raiz, os.path.relpath(unidad, r'E:\DAE MASTER').split(os.sep))
    pool = {norm(c.GetClipProperty('File Path')): c for c in _todos(carp)}
    nuevos = sorted({os.path.join(unidad, x['sub'].replace('/', os.sep), x['f'])
                     for x in pl['items'] if x.get('f')})
    falta = [p for p in nuevos if not os.path.exists(p)]
    if falta:
        raise SystemExit('faltan en disco: %s' % falta)
    for p in nuevos:
        if norm(p) in pool:
            continue
        b = _baja(carp, os.path.dirname(os.path.relpath(p, unidad)).split(os.sep))
        mp.SetCurrentFolder(b)
        r = mp.ImportMedia([p])
        if r:
            pool[norm(p)] = r[0]
    for _ in range(5):
        falta = [p for p in nuevos if norm(p) not in pool]
        if not falta:
            break
        time.sleep(0.8)
        pool.update({norm(c.GetClipProperty('File Path')): c for c in _todos(carp)})
    if falta:
        raise SystemExit('no entraron al pool: %s' % falta)

    # su linea queda con otro nombre; la nueva toma el suyo
    k, otro = 1, '%s (antes de apretar)' % nl
    while otro in nombres:
        k += 1
        otro = '%s (antes de apretar %d)' % (nl, k)
    suya.SetName(otro)
    mp.SetCurrentFolder(_baja(carp, ['10 TIMELINE SEBASTIAN']))
    tl = mp.CreateEmptyTimeline(nl)
    pr.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < len(pistas_v):
        tl.AddTrack('video')
    while tl.GetTrackCount('audio') < len(pistas_a):
        tl.AddTrack('audio', 'stereo')
    for i, n in enumerate(pistas_v, 1):
        tl.SetTrackName('video', i, n)
    for i, n in enumerate(pistas_a, 1):
        tl.SetTrackName('audio', i, n)
    T1 = tl.GetStartFrame()

    por_pista = {}
    for x in pl['items']:
        if x.get('f'):
            m = pool[norm(os.path.join(unidad, x['sub'].replace('/', os.sep), x['f']))]
        else:
            m = suyos[(x['t'], x['k'], x['viejo'], x['s_viejo'])]
        por_pista.setdefault((x['t'], x['k']), []).append(
            {'mediaPoolItem': m, 'startFrame': x['sf'], 'endFrame': x['sf'] + x['nl'],
             'trackIndex': x['k'], 'recordFrame': T1 + x['ns'],
             'mediaType': 1 if x['t'] == 'v' else 2})
    for (t, k), lista in sorted(por_pista.items()):
        lista.sort(key=lambda d: d['recordFrame'])
        r = mp.AppendToTimeline(lista)
        SP.w('%s%d: %d items, puestos %d' % (t.upper(), k, len(lista), len(r or [])))

    # retrato contra el plan
    hay = set()
    for tipo in ('video', 'audio'):
        for i in range(1, tl.GetTrackCount(tipo) + 1):
            for it in tl.GetItemListInTrack(tipo, i) or []:
                m = it.GetMediaPoolItem()
                fp = os.path.basename(m.GetClipProperty('File Path')) if m else it.GetName()
                hay.add((tipo[0], i, it.GetStart() - T1, it.GetEnd() - it.GetStart(), fp))
    pide = {(x['t'], x['k'], x['ns'], x['nl'], x.get('f') or x['viejo']) for x in pl['items']}
    sobra, faltan = sorted(hay - pide), sorted(pide - hay)
    largo = tl.GetEndFrame() - T1
    SP.w('retrato: %d items, %d pedidos; faltan %s; sobran %s' % (len(hay), len(pide), faltan[:6], sobra[:6]))
    SP.w('huecos V1 %s; largo %d (plan %d)' % (SP.huecos(tl), largo, pl['pieza']))
    dest = R.sub(L, '10 TIMELINE SEBASTIAN')
    drt = os.path.join(dest, '%s.drt' % nl)
    if os.path.exists(drt):
        SP.aparta(drt, 'apretada_%s' % time.strftime('%H%M%S'))
    tl.Export(drt, resolve.EXPORT_DRT)
    SP.w('.drt %s' % (os.path.getsize(drt) if os.path.exists(drt) else 'NO SE ESCRIBIO'))
    pm.SaveProject()
    resolve.OpenPage(antes['pagina'] or 'edit')
    SP.w('vuelta a %s / %s (su linea vieja: «%s»)' % (nl, antes['pagina'], otro))
    SP.w('LISTO' if not faltan and not sobra and largo == pl['pieza'] else 'REVISAR')


if __name__ == '__main__':
    main(sys.argv[1].upper(), sys.argv[2])
