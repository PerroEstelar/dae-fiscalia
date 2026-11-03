# -*- coding: utf-8 -*-
r"""Arma el árbol del curso Ley 1826 en disco y en los bins de Resolve.

    python arbol_lp.py            (venv del MCP: disco + bins)
    arbol(resolve)                desde run_inline

Idempotente: lo que ya existe no se toca. Nada se borra.
"""
import os
import sys

H = r'D:\DAE\_repo\herramientas'
sys.path.insert(0, os.path.join(H, 'voz', 'textos'))
sys.path.insert(0, os.path.join(H, 'montaje'))
import rutas_lp as R                                    # noqa: E402
from guion_lp import PIEZAS, UNIDADES                  # noqa: E402


def disco():
    hechas = 0
    base = [R.RAIZ, R.FUENTE, R.PERSONAJES,
            os.path.join(R.PERSONAJES, '_crudos'),
            os.path.join(R.PERSONAJES, '_piel_ref')]
    base += [R.unidad(n) for n in UNIDADES]
    for clave, v in PIEZAS.items():
        subs = R.SUB_VIDEO if v[0] == 'video' else R.SUB_IMAGEN
        base.append(R.carpeta(clave))
        base += [R.sub(clave, s) for s in subs]
        if v[0] == 'video':
            base += [R.sub(clave, os.path.join('10 TIMELINE SEBASTIAN', s))
                     for s in ('RANURAS', 'RESPIRO')]
            base += [R.sub(clave, os.path.join('01 PLANOS', s))
                     for s in ('_candidatas', '_grade')]
        else:
            base += [R.sub(clave, os.path.join('01 PLANOS', s))
                     for s in ('_candidatas', '_grade')]
    for p in base:
        if not os.path.isdir(p):
            os.makedirs(p)
            hechas += 1
    return hechas, len(base)


def _hijo(mp, f, n):
    for x in f.GetSubFolderList() or []:
        if x.GetName().strip().upper() == n.strip().upper():
            return x
    return mp.AddSubFolder(f, n)


def bins(resolve):
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    raiz = mp.GetRootFolder()
    n = 0
    for clave, v in PIEZAS.items():
        f = raiz
        for parte in R.bins(clave):
            f = _hijo(mp, f, parte)
        for s in (R.BINS_VIDEO if v[0] == 'video' else R.BINS_IMAGEN):
            _hijo(mp, f, s)
            n += 1
    resolve.GetProjectManager().SaveProject()
    return n


def arbol(resolve=None):
    h, t = disco()
    print('disco: %d carpetas nuevas de %d' % (h, t))
    if resolve is not None:
        print('bins: %d' % bins(resolve))


if __name__ == '__main__':
    import dh_pieza as SP
    arbol(SP._resolve())
