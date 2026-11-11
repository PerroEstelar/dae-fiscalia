# -*- coding: utf-8 -*-
r"""Motion graphics del conversatorio «Articulación DEMA y DECOC», en After Effects.

Usa el mismo dibujo que mg_ma (las introducciones U2–U5): barra #FEB900, texto
Montserrat blanco, íconos blancos de Magnific con pop y sombra en una capa de
ajuste. La diferencia es la maqueta: van en la banda de abajo de la composición
de pantalla dividida, debajo de quien habla, anclados arriba en y=725 y con 720
de ancho.

- `mg_act`: el ícono a la izquierda y, a su derecha, el antetítulo, el título
  y el cuerpo (los cuatro frentes y los tres ejes).
- `mg_lista`: un título y filas de ícono de 52 px con su rótulo, cada fila en el
  cuadro de su palabra.

Las composiciones se llaman `DEMA_<clave>` y van en el mismo proyecto que las de
las introducciones (`00 MOTION GRAPHICS/MA_intros_mg.aep`). Se rinden con
aerender a `CONVERSATORIO - Articulacion DEMA y DECOC/09 MOTION GRAPHICS`.

    python mg_dema.py medir     alturas, sin tocar AE
    python mg_dema.py armar
    python mg_dema.py render
"""
import os
import subprocess
import sys
import time

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\conversatorio_dema')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mg_ma as M  # noqa: E402
import plan_dema as P  # noqa: E402

DEST = M.CURSO + '/UNIDAD 1/CONVERSATORIO - Articulacion DEMA y DECOC/09 MOTION GRAPHICS'
ICON_ACT, GAP_ICON = 64, 16
ICON_FILA, GAP_FILA, SEP_FILA = 52, 18, 10
ROT = 31                                  # rótulo de fila
TOPE = 1050                               # nada pasa de acá


def lados(lado):
    M.BAR_X = P.LADO[lado]['bar_x']
    return P.LADO[lado]['text_x']


def mg_act(nombre, n, lado, d):
    """Ícono a la izquierda, y a su derecha la columna de antetítulo, título y cuerpo."""
    tx = lados(lado)
    cx = tx + ICON_ACT + GAP_ICON + 2
    lineas = [(d['ante'], 'med', P.ANTE, 0), (d['titulo'], 'bold', P.TIT, P.GAP_ANTE)]
    if d.get('cuerpo'):
        lineas.append((d['cuerpo'], 'med', P.CUE, P.GAP_CUE + 8))
    laid, total = M.maquetar(lineas, P.MAXW - (cx - tx))
    alto = max(ICON_ACT, total)
    off = P.BANDA_TOP
    c = M.Comp(nombre, n)
    c.barra(off - M.BAR_PAD, alto + 2 * M.BAR_PAD)
    out = M.salidas(n, 1 + len(laid))
    c.icono(d['icono'], tx + ICON_ACT / 2.0, off + ICON_ACT / 2.0, ICON_ACT, 3, out[0])
    for i, ln in enumerate(laid):
        c.texto(cx, off + ln['base'], ln, 6 + i * M.RET_IN, out[1 + i])
    c.sombra()
    return c, off + alto + M.BAR_PAD


def mg_lista(nombre, n, lado, t0, d):
    tx = lados(lado)
    tit, th = M.maquetar([(d['titulo'], 'bold', P.TIT, 0)], P.MAXW)
    x_lab = tx + ICON_FILA + GAP_FILA
    filas = []
    for ico, rotulo, t_pal in d['filas']:
        lab, lh = M.maquetar([(rotulo, 'med', ROT, 0)], P.MAXW - ICON_FILA - GAP_FILA)
        filas.append((ico, lab, lh, max(ICON_FILA, lh), max(12, int(round((t_pal - t0) * P.FPS)))))
    alto = th + P.GAP_TIT + sum(f[3] for f in filas) + SEP_FILA * (len(filas) - 1)
    off = P.BANDA_TOP
    c = M.Comp(nombre, n)
    c.barra(off - M.BAR_PAD, alto + 2 * M.BAR_PAD)
    out = M.salidas(n, len(tit) + sum(1 + len(f[1]) for f in filas))
    k = 0
    for i, ln in enumerate(tit):
        c.texto(tx, off + ln['base'], ln, 6 + i * M.RET_IN, out[k]); k += 1
    y = off + th + P.GAP_TIT
    for ico, lab, lh, rh, fr in filas:
        c.icono(ico, tx + ICON_FILA / 2.0, y + rh / 2.0, ICON_FILA, fr, out[k]); k += 1
        ytxt = y + (rh - lh) / 2.0
        for j, ln in enumerate(lab):
            c.texto(x_lab, ytxt + ln['base'], ln, fr + 3 + j * 2, out[k]); k += 1
        y += rh + SEP_FILA
    c.sombra()
    return c, off + alto + M.BAR_PAD


def items():
    for clave, tipo, lado, t0, t1, d in P.ITEMS:
        if tipo in ('mg_act', 'mg_lista'):
            yield clave, tipo, lado, t0, t1, d


def construir(clave, tipo, lado, t0, t1, d):
    n = int(round((t1 - t0) * P.FPS))
    nm = 'DEMA_' + clave
    if tipo == 'mg_act':
        return mg_act(nm, n, lado, d)
    return mg_lista(nm, n, lado, t0, d)


def medir():
    for it in items():
        c, fondo = construir(*it)
        print('%-18s %s %4d f  %2d capas  fondo %4d%s' % (it[0], it[2], c.n, c.k, fondo,
                                                         '  <-- SE SALE' if fondo > TOPE else ''))


def armar():
    if (M.cmd('getProjectInfo', {}) or {}).get('path') is None:
        raise SystemExit('el proyecto de AE no está guardado: abrir MA_intros_mg.aep')
    r = M.cmd('getProjectItems', {})
    existentes = {it['name']: it for it in (r['items'] if isinstance(r, dict) else r)}
    iconos = sorted({d['icono'] for _c, tipo, _l, _a, _b, d in items() if tipo == 'mg_act'} |
                    {f[0] for _c, tipo, _l, _a, _b, d in items() if tipo == 'mg_lista' for f in d['filas']})
    for ico in iconos:
        if 'ico_' + ico not in existentes:
            M.cmd('importFootage', {'path': '%s/%s.png' % (M.ICONOS, ico), 'name': 'ico_' + ico})
    for it in items():
        nm = 'DEMA_' + it[0]
        if nm in existentes:
            M.cmd('deleteItem', {'itemName': nm})
        c, fondo = construir(*it)
        M.batch(c.c)
        print('%-18s %4d f  fondo %d' % (it[0], c.n, fondo), flush=True)
    M.cmd('saveProject', {'path': M.AEP})
    print('ARMADO', flush=True)


def render():
    os.makedirs(DEST, exist_ok=True)
    for it in items():
        nm = 'DEMA_' + it[0]
        out = '%s/%s.mov' % (DEST, nm)
        t0 = time.time()
        r = subprocess.run([M.AERENDER, '-project', M.AEP.replace('/', '\\'), '-comp', nm,
                            '-OMtemplate', M.OM, '-output', out.replace('/', '\\')],
                           capture_output=True, text=True, errors='replace')
        ok = os.path.exists(out) and os.path.getsize(out) > 0
        print('%-18s %s %.0f s %s' % (it[0], 'OK' if ok else 'FALLA', time.time() - t0,
                                      '' if ok else r.stdout[-600:]), flush=True)
    print('RENDER LISTO', flush=True)


if __name__ == '__main__':
    {'medir': medir, 'armar': armar, 'render': render}[sys.argv[1]]()
