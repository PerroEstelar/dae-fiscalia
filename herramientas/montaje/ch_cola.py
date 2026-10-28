# -*- coding: utf-8 -*-
r"""Cola de renders del profe Carlos Humberto: en cada llamada mira el trabajo
actual y, si termino, lanza el siguiente que falte. Se llama desde run_inline
(los procesos sueltos dejaban el trabajo en 'Ready', 28 oct).
Bases de la V2 (full/limpio) y masters de la V2."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch_render1 as R   # noqa: E402

COLA = [('base', 6, 'full'), ('base', 2, 'full'), ('base', 3, 'full'), ('base', 5, 'full'), ('master', 2), ('master', 3), ('master', 4),
        ('base', 2, 'limpio'),
        ('master', 6), ('master', 1), ('master', 5),
        ('base', 3, 'limpio')]


def agregar(*x):
    if x not in COLA:
        COLA.append(x)


def paso(pr, extra=()):
    import ch_montar_v2 as M
    o, prog = R.estado(pr)
    if prog:
        return o
    for x in COLA + list(extra):
        if x[0] == 'base':
            r = R.kick(pr, x[1], x[2])
        else:
            r = M.kick_master(pr, x[1])
        if r.startswith('YA EXISTE'):
            continue
        return o + [r]
    return o + ['COLA VACIA']
