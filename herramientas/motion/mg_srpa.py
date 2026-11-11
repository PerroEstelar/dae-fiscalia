# -*- coding: utf-8 -*-
r"""Motion graphics de los videos de profes del curso SRPA y justicia restaurativa,
en After Effects por aftr.

Es el dibujo de los motion graphics de las introducciones de Delitos ambientales
(`mg_ma`): barra #FEB900 de 14 px en x=86, texto Montserrat blanco desde x=170,
bloque anclado abajo en y=690, ancho 615, sombra ambiental + contacto en una
capa de ajuste, íconos blancos que entran con un pop cuando el profe nombra cada
cosa. Dos diferencias con mg_ma:
- La tarjeta (`mg_act`) puede ir sin título: ícono + antetítulo y debajo el cuerpo
  (las competencias específicas, que son frases largas).
- La lista (`mg_lista`) puede ir sin título.

Corre en la máquina de Sebastián, con el panel de aftr abierto en AE. Las
composiciones se llaman `SRPA_<video>_<clave>` y viven en
`00 MOTION GRAPHICS/SRPA_mg.aep`; `render` las rinde con aerender (alfa,
ProRes 4444) a `<video>/09 MOTION GRAPHICS/<comp>.mov`.

    python mg_srpa.py armar curso u1b     arma las composiciones
    python mg_srpa.py render curso u1b    las rinde
"""
import os
import shutil
import subprocess
import sys
import time

from PIL import ImageFont

sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mg_ma as M  # noqa: E402
import plan_srpa as P  # noqa: E402
import srpa as S  # noqa: E402

AEP = S.RAIZ + '/00 MOTION GRAPHICS/SRPA_mg.aep'
ICONOS = S.RAIZ + '/00 MOTION GRAPHICS/iconos'


def mg_act(nombre, n, d):
    piezas = []
    if d['titulo']:
        piezas.append((d['titulo'], 'bold', P.TIT, 0))
    if d['cuerpo']:
        piezas.append((d['cuerpo'], 'med', P.CUE, (P.GAP_CUE + 8) if piezas else 0))
    resto, total = M.maquetar(piezas, M.MAXW)
    alto = M.ICON_ACT + P.GAP_ANTE + total
    off = M.BASE_Y - alto
    c = M.Comp(nombre, n)
    c.barra(off - M.BAR_PAD, alto + 2 * M.BAR_PAD)
    out = M.salidas(n, 2 + len(resto))
    c.icono(d['icono'], M.TEXT_X + M.ICON_ACT / 2.0, off + M.ICON_ACT / 2.0, M.ICON_ACT, 3, out[0])
    ft = ImageFont.truetype(M.TTF['med'], P.ANTE)
    alto_mayus = -ft.getbbox('A', anchor='ls')[1]
    ante = {'text': d['ante'], 'peso': 'med', 'px': P.ANTE}
    c.texto(M.TEXT_X + M.ICON_ACT + M.GAP_ICON, off + M.ICON_ACT / 2.0 + alto_mayus / 2.0, ante, 6, out[1])
    y0 = off + M.ICON_ACT + P.GAP_ANTE
    for i, ln in enumerate(resto):
        c.texto(M.TEXT_X, y0 + ln['base'], ln, 9 + i * M.RET_IN, out[2 + i])
    c.sombra()
    return c, off - M.BAR_PAD


def mg_lista(nombre, n, filas_cuadro, d):
    """filas_cuadro: cuadro (desde el inicio del ítem) en que entra cada fila."""
    if d['titulo']:
        tit, th = M.maquetar([(d['titulo'], 'bold', P.TIT, 0)], M.MAXW)
        th += P.GAP_TIT
    else:
        tit, th = [], 0
    x_lab = M.TEXT_X + M.ICON_FILA + M.GAP_FILA
    filas = []
    for (ico, rotulo, _t), fr in zip(d['filas'], filas_cuadro):
        lab, lh = M.maquetar([(rotulo, 'med', P.CUE, 0)], M.MAXW - M.ICON_FILA - M.GAP_FILA)
        filas.append((ico, lab, lh, max(M.ICON_FILA, lh), max(8, fr)))
    alto = th + sum(f[3] for f in filas) + M.SEP_FILA * (len(filas) - 1)
    off = M.BASE_Y - alto
    c = M.Comp(nombre, n)
    c.barra(off - M.BAR_PAD, alto + 2 * M.BAR_PAD)
    elementos = len(tit) + sum(1 + len(f[1]) for f in filas)
    out = M.salidas(n, elementos)
    k = 0
    for i, ln in enumerate(tit):
        c.texto(M.TEXT_X, off + ln['base'], ln, 6 + i * M.RET_IN, out[k])
        k += 1
    y = off + th
    for ico, lab, lh, rh, fr in filas:
        c.icono(ico, M.TEXT_X + M.ICON_FILA / 2.0, y + rh / 2.0, M.ICON_FILA, fr, out[k])
        k += 1
        ytxt = y + (rh - lh) / 2.0
        for j, ln in enumerate(lab):
            c.texto(x_lab, ytxt + ln['base'], ln, fr + 3 + j * 2, out[k])
            k += 1
        y += rh + M.SEP_FILA
    c.sombra()
    return c, off - M.BAR_PAD


def nombre_comp(video, clave):
    return 'SRPA_%s_%s' % (video, clave)


def items(videos):
    """videos: 'curso' (todo el video) o 'curso:m14' (las claves que empiezan así)."""
    for tok in videos:
        v, _, pref = tok.partition(':')
        for clave, tipo, t0, t1, d in P.ITEMS[v]:
            if tipo in ('mg_act', 'mg_lista') and clave.startswith(pref):
                yield v, clave, tipo, t0, t1, d


def iconos_usados(videos):
    out = set()
    for _v, _c, tipo, _a, _b, d in items(videos):
        out |= {d['icono']} if tipo == 'mg_act' else {f[0] for f in d['filas']}
    return sorted(out)


def armar(videos):
    info = M.cmd('getProjectInfo', {})
    if os.path.normcase(os.path.normpath(info.get('path') or '')) != os.path.normcase(os.path.normpath(AEP)):
        if os.path.exists(AEP):
            raise SystemExit('AE tiene abierto %r y no el AEP del curso' % info.get('path'))
        M.cmd('saveProject', {'path': AEP})
    r = M.cmd('getProjectItems', {})
    existentes = {it['name']: it for it in (r['items'] if isinstance(r, dict) else r)}
    for ico in iconos_usados(videos):
        src = '%s/%s.png' % (ICONOS, ico)
        if not os.path.exists(src):
            ma = '%s/%s.png' % (M.ICONOS, ico)          # los de Delitos ambientales
            shutil.copy2(ma, src)
        if 'ico_' + ico not in existentes:
            M.cmd('importFootage', {'path': src, 'name': 'ico_' + ico})
    for v, clave, tipo, t0, t1, d in items(videos):
        nm = nombre_comp(v, clave)
        n = int(round((t1 - t0) * P.FPS))
        if nm in existentes:
            M.cmd('deleteItem', {'itemName': nm})
        if tipo == 'mg_act':
            c, cima = mg_act(nm, n, d)
        else:
            fr = [int(round((f[2] - t0) * P.FPS)) for f in d['filas']]
            c, cima = mg_lista(nm, n, fr, d)
        M.batch(c.c)
        print('%-5s %-22s %4d f  %3d capas  cima %d%s' % (
            v, clave, n, c.k, cima, '  <-- SE SUBE DE LA ZONA' if cima < 250 else ''), flush=True)
    M.cmd('saveProject', {'path': AEP})
    print('ARMADO', flush=True)


def render(videos, saltar=False):
    for v, clave, tipo, t0, t1, d in items(videos):
        nm = nombre_comp(v, clave)
        dst = '%s/09 MOTION GRAPHICS' % S.carpeta(v)
        os.makedirs(dst, exist_ok=True)
        out = '%s/%s.mov' % (dst, nm)
        if saltar and os.path.exists(out) and os.path.getsize(out) > 0:
            continue
        t = time.time()
        r = subprocess.run([M.AERENDER, '-project', AEP.replace('/', '\\'), '-comp', nm,
                            '-OMtemplate', M.OM, '-output', out.replace('/', '\\')],
                           capture_output=True, text=True, errors='replace')
        ok = os.path.exists(out) and os.path.getsize(out) > 0
        print('%-5s %-22s %s %.0f s %s' % (v, clave, 'OK' if ok else 'FALLA', time.time() - t,
                                           '' if ok else r.stdout[-600:]), flush=True)
    print('RENDER LISTO', flush=True)


if __name__ == '__main__':
    accion, videos = sys.argv[1], sys.argv[2:]
    if accion == 'faltan':                      # rinde solo lo que no está en disco
        render(videos, saltar=True)
    else:
        {'armar': armar, 'render': render}[accion](videos)
