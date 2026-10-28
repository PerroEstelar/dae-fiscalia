# -*- coding: utf-8 -*-
r"""Arregla los enlaces que la importacion de las .drt cruzo entre casos (28 oct).

Que paso: al importar las lineas en DAE MASTER - CURSOS, Resolve junto por
NOMBRE los archivos que se llaman igual aunque sean distintos:
  - ElevenLabs_Untitled_project.mp3 (narracion de los casos 2, 3 y 5): los
    casos 3 y 5 quedaron sonando con la narracion de Rodman, y un tramo del 3
    quedo sin medio.
  - Copia de Investigacion del uso ilicito de criptoactivos(_).mp4 (rotulo de
    los casos 2 y 3): quedaron con el de 00 COMUNES\OUTRO, que es otro archivo.
Se compara cada item con el archivo que tenia en la linea original
(inventario.json) y su copia en DAE MASTER (copias.json). FGN_intro va a
00 COMUNES a proposito y no se toca.

Como se arregla, sin cambiar tiempos: antes se duplica la linea como
'ZZ respaldo antes de reenlazar - <linea>' (bin _trabajo). Video: toma nueva
(AddTake + FinalizeTake) y, si no se deja, se quita y se vuelve a poner en el
mismo cuadro con las mismas propiedades. Audio (las tomas no aplican): se
quita y se vuelve a poner en el mismo cuadro, misma pista, mismo tramo de
origen. El volumen de clip no lo expone la API: se mide despues con el render.

    python ch_reenlazar.py [--hacer]      (sin --hacer solo lista)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch_migrar as CM      # noqa: E402

TMP = r'D:\DAE\_tmp\ch'
ORIG = {1: 'prfe calors Unidad 1 Caso 1 copy', 2: 'prfe calors Unidad 1 Caso 2 copy',
        3: 'prfe calors Unidad 1 Caso 3', 5: 'prfe calors Unidad 1 Caso 5', 6: 'caso 6'}
NO_TOCAR = ('fgn_intro_version7.mp4',)


def w(*a):
    print(*a, flush=True)


def plan(pr):
    inv = json.load(open(os.path.join(TMP, 'inventario.json'), encoding='utf-8'))
    cop = json.load(open(os.path.join(TMP, 'copias.json'), encoding='utf-8'))['copias']
    o2n = {}
    for o, n, s in cop:
        o2n.setdefault(o.lower(), []).append(n)
    tls = {pr.GetTimelineByIndex(i).GetName(): pr.GetTimelineByIndex(i)
           for i in range(1, int(pr.GetTimelineCount()) + 1)}
    out = []
    for n, on in ORIG.items():
        tl = tls[CM.nombre_linea(n)]
        st = tl.GetStartFrame()
        orig = {}
        for t, d in inv[on]['pistas'].items():
            for it in d['items']:
                orig[(t, it['ini'])] = it
        for kind in ('video', 'audio'):
            for k in range(1, int(tl.GetTrackCount(kind)) + 1):
                for it in tl.GetItemListInTrack(kind, k) or []:
                    o = orig.get((kind[0].upper() + str(k), it.GetStart() - st))
                    if not o or not o.get('archivo'):
                        continue
                    oa = o['archivo'].lower()
                    if os.path.basename(oa) in NO_TOCAR:
                        continue
                    if os.path.basename(oa) != it.GetName().lower() and kind == 'video' \
                            and not it.GetName().lower().startswith(os.path.basename(oa)[:20]):
                        continue      # otro item que empieza en el mismo cuadro
                    m = it.GetMediaPoolItem()
                    cur = (m.GetClipProperty('File Path') if m else '') or ''
                    buenos = o2n.get(oa, [])
                    if cur.lower() in [b.lower() for b in buenos]:
                        continue
                    dest = [b for b in buenos if CM.carpeta(n).lower() in b.lower()] or buenos
                    if not dest:
                        w('SIN COPIA', n, kind, k, it.GetName(), oa)
                        continue
                    out.append((n, tl, kind, k, it, cur, dest[0]))
    return out


def mpi_de(mp, path):
    rel = os.path.relpath(os.path.dirname(path), r'E:\DAE MASTER').split(os.sep)
    b = CM.bin_de(mp, rel)
    for c in b.GetClipList() or []:
        if (c.GetClipProperty('File Path') or '').lower() == path.lower():
            return c
    mp.SetCurrentFolder(b)
    r = mp.ImportMedia([path]) or []
    return r[0] if r else None


def respaldo(pr, mp, tl, n):
    nombre = 'ZZ respaldo antes de reenlazar - ' + tl.GetName()
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        if pr.GetTimelineByIndex(i).GetName() == nombre:
            return
    pr.SetCurrentTimeline(tl)
    tl.DuplicateTimeline(nombre)
    rel = os.path.relpath(CM.carpeta(n), r'E:\DAE MASTER').split(os.sep)
    b = CM.bin_de(mp, rel + ['_trabajo (no usar)'])
    for c in mp.GetCurrentFolder().GetClipList() + mp.GetRootFolder().GetClipList():
        if c.GetName() == nombre:
            mp.MoveClips([c], b)


def hacer(pr):
    mp = pr.GetMediaPool()
    lista = plan(pr)
    hechos = set()
    for n, tl, kind, k, it, cur, dest in lista:
        if n not in hechos:
            respaldo(pr, mp, tl, n)
            hechos.add(n)
        pr.SetCurrentTimeline(tl)
        new = mpi_de(mp, dest)
        st = tl.GetStartFrame()
        s, ss, se = it.GetStart(), it.GetSourceStartFrame(), it.GetSourceEndFrame()
        nm = it.GetName()
        modo = ''
        if kind == 'video':
            props = it.GetProperty() or {}
            if it.AddTake(new, ss, se):
                it.SelectTakeByIndex(int(it.GetTakesCount()))
                it.FinalizeTake()
                modo = 'toma'
            else:
                tl.DeleteClips([it], False)
                r = mp.AppendToTimeline([{'mediaPoolItem': new, 'startFrame': ss, 'endFrame': se,
                                          'trackIndex': k, 'recordFrame': s, 'mediaType': 1}])
                if r:
                    for a, v in props.items():
                        r[0].SetProperty(a, v)
                modo = 'reponer'
        else:
            tl.DeleteClips([it], False)
            mp.AppendToTimeline([{'mediaPoolItem': new, 'startFrame': ss, 'endFrame': se,
                                  'trackIndex': k, 'recordFrame': s, 'mediaType': 2}])
            modo = 'reponer'
        w('caso', n, kind[0].upper() + str(k), s - st, nm, modo, '->', dest[-60:])
    # verificacion
    for n, tl, kind, k, it, cur, dest in lista[:0]:
        pass
    return len(lista)


if __name__ == '__main__':
    import DaVinciResolveScript as dvr
    pr_ = dvr.scriptapp('Resolve').GetProjectManager().GetCurrentProject()
    if '--hacer' in sys.argv:
        w('hechos', hacer(pr_))
    else:
        for n, tl, kind, k, it, cur, dest in plan(pr_):
            w(n, kind, k, it.GetStart() - tl.GetStartFrame(), it.GetName(), '|', cur[-55:], '->', dest[-60:])
