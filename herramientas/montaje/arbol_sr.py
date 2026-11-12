# -*- coding: utf-8 -*-
r"""Arma el árbol de los casos del curso SRPA (PRIORIDAD 1) en disco y en los
bins de Resolve. Es `arbol_ei` apuntado a `rutas_sr`.

    arbol(resolve)                desde run_inline

Idempotente: lo que ya existe no se toca. Nada se borra.
"""
import os
import sys

H = r'D:\DAE\_repo\herramientas'
sys.path.insert(0, os.path.join(H, 'voz', 'textos'))
sys.path.insert(0, os.path.join(H, 'montaje'))
import rutas_sr as R                                    # noqa: E402
from guion_sr import PIEZAS                            # noqa: E402


def disco():
    hechas = 0
    base = [R.RAIZ, R.FUENTE, R.PERSONAJES, os.path.join(R.PERSONAJES, '_crudos')]
    for clave, v in PIEZAS.items():
        base.append(R.carpeta(clave))
        base += [R.sub(clave, s) for s in R.SUB_VIDEO]
        base += [R.sub(clave, os.path.join('10 TIMELINE SEBASTIAN', s))
                 for s in ('RANURAS', 'RESPIRO', 'MOVIMIENTO', 'DETALLE')]
        base += [R.sub(clave, os.path.join('01 PLANOS', s))
                 for s in ('_candidatas', '_grade')]
        base += [R.sub(clave, os.path.join('02 CARTONES', 'LOWER THIRDS'))]
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
    pm = resolve.GetProjectManager()
    pr = pm.GetCurrentProject()
    if pr is None or pr.GetName() != 'DAE MASTER - CURSOS':
        pr = pm.LoadProject('DAE MASTER - CURSOS')
    resolve.OpenPage('edit')      # AddSubFolder devuelve None en Deliver
    mp = pr.GetMediaPool()
    raiz = mp.GetRootFolder()
    n = 0
    for clave, v in PIEZAS.items():
        f = raiz
        for parte in R.bins(clave):
            f = _hijo(mp, f, parte)
            assert f is not None, parte
        for s in R.BINS_VIDEO:
            assert _hijo(mp, f, s) is not None, s
            n += 1
    pm.SaveProject()
    return n


def arbol(resolve=None):
    h, t = disco()
    print('disco: %d carpetas nuevas de %d' % (h, t))
    if resolve is not None:
        print('bins: %d' % bins(resolve))
