# -*- coding: utf-8 -*-
r"""Profe Carlos Humberto, Unidad 1 (casos para talleres): inventario de las
seis lineas que viven fuera de DAE MASTER, y su .drt.

    python ch_inventario.py

Abre en Resolve, uno tras otro, los proyectos donde estan las lineas
(INTRO CRIPTO: casos 1-4; DAE: casos 5 y 6), y de cada linea guarda:
ajustes (fps, tamano), pistas, cada item con su archivo, y el .drt. Al final
vuelve a abrir DAE MASTER - CURSOS. No modifica ningun proyecto: solo lee y
exporta .drt a D:\DAE\_tmp\ch\drt.

Escribe D:\DAE\_tmp\ch\inventario.json.
"""
import json
import os
import sys
import time

sys.path.insert(0, r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules')
import DaVinciResolveScript as dvr                                    # noqa: E402

OUT = r'D:\DAE\_tmp\ch'
FUENTES = [
    ('INTRO CRIPTO', ['prfe calors Unidad 1 Caso 1 copy', 'prfe calors Unidad 1 Caso 2 copy',
                      'prfe calors Unidad 1 Caso 3', 'prfe calors Unidad 1 Caso 4']),
    ('DAE', ['prfe calors Unidad 1 Caso 5', 'caso 6']),
]
VOLVER = 'DAE MASTER - CURSOS'


def w(*a):
    print(*a, flush=True)


def linea(resolve, tl, drt_dir):
    st = tl.GetStartFrame()
    d = {'nombre': tl.GetName(), 'inicio': st, 'largo': tl.GetEndFrame() - st,
         'fps': tl.GetSetting('timelineFrameRate'),
         'ancho': tl.GetSetting('timelineResolutionWidth'),
         'alto': tl.GetSetting('timelineResolutionHeight'), 'pistas': {}}
    for kind in ('video', 'audio', 'subtitle'):
        n = int(tl.GetTrackCount(kind) or 0)
        for k in range(1, n + 1):
            items = []
            for it in tl.GetItemListInTrack(kind, k) or []:
                m = it.GetMediaPoolItem()
                items.append({'ini': it.GetStart() - st, 'fin': it.GetEnd() - st,
                              'off': it.GetLeftOffset(), 'nombre': it.GetName(),
                              'archivo': m.GetClipProperty('File Path') if m else '',
                              'clip': m.GetName() if m else ''})
            d['pistas']['%s%d' % (kind[0].upper(), k)] = {'nombre': tl.GetTrackName(kind, k),
                                                          'items': items}
    os.makedirs(drt_dir, exist_ok=True)
    p = os.path.join(drt_dir, tl.GetName() + '.drt')
    if os.path.exists(p):
        os.replace(p, p + '.%s.bak' % time.strftime('%H%M%S'))
    ok = tl.Export(p, resolve.EXPORT_DRT)
    d['drt'] = p if ok and os.path.exists(p) else None
    return d


def main():
    resolve = dvr.scriptapp('Resolve')
    pm = resolve.GetProjectManager()
    w('actual', pm.GetCurrentProject().GetName())
    pm.SaveProject()
    inv = {}
    for proy, nombres in FUENTES:
        t0 = time.time()
        p = pm.LoadProject(proy)
        w('cargado', proy, bool(p), '%.0f s' % (time.time() - t0))
        if not p:
            continue
        tls = {}
        for i in range(1, int(p.GetTimelineCount()) + 1):
            t = p.GetTimelineByIndex(i)
            tls[t.GetName()] = t
        for n in nombres:
            if n not in tls:
                w('  NO ESTA', n)
                continue
            d = linea(resolve, tls[n], os.path.join(OUT, 'drt'))
            d['proyecto'] = proy
            inv[n] = d
            nv = sum(len(v['items']) for k, v in d['pistas'].items() if k.startswith('V'))
            na = sum(len(v['items']) for k, v in d['pistas'].items() if k.startswith('A'))
            w('  %s  %d cuadros @ %s  %sx%s  video %d  audio %d  drt %s'
              % (n, d['largo'], d['fps'], d['ancho'], d['alto'], nv, na, bool(d['drt'])))
    json.dump(inv, open(os.path.join(OUT, 'inventario.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    p = pm.LoadProject(VOLVER)
    w('de vuelta en', p.GetName() if p else 'NO SE PUDO VOLVER')


if __name__ == '__main__':
    main()
    w('LISTO')
