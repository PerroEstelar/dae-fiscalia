# -*- coding: utf-8 -*-
r"""Listas animadas (After Effects, por aftr) de los CASOS del curso SRPA y
justicia restaurativa.

    python mg_sr.py plan NICO       imprime las ventanas (no toca AE)
    python mg_sr.py armar NICO      arma las composiciones en SRPA_mg.aep
    python mg_sr.py render NICO     las rinde (aerender, alfa) a 09 MOTION GRAPHICS

EL DIBUJO
    Es el de los motion graphics de la serie (`mg_ma`: barra #FEB900 de 14 px,
    Montserrat blanca, íconos blancos de línea que entran con un pop cuando la
    voz nombra cada cosa), puesto en la RETÍCULA DE LOS CARTONES DE CASO
    (rejilla A): barra en x=175, texto desde x=243, el bloque centrado en el
    centro óptico (y≈575), y sobre el TINTE de los cartones (#004890 al 46 %,
    el azul del intro oficial) a cuadro completo, que entra y sale con la lista.
    Sin sombras: el tinte ya da la lectura (como los cartones de caso), y una
    sombra de capa de ajuste sobre un panel a cuadro completo lo oscurece.

EL TEXTO
    Cada fila es literal del documento (la única licencia: la mayúscula
    inicial). Entra cuando Scribe oye sus primeras palabras. La lista entra
    10 cuadros antes de su primera fila y sale 12 cuadros después de que la
    voz termina el último bloque que cubre, sin pisar el bloque siguiente.

CASO NICO (12 nov): cinco listas
    desayuno    n11  lo que recibió el cliente y lo que valía
    policia     n20  lo que los uniformados no hicieron
    cae         n26  lo que el CAE le daría (el final del bloque; el comienzo
                     lleva cartón)
    defensor    n33  lo que el defensor no hizo
    valoracion  n37-n40  lo que se observó en la valoración inicial
    Íconos: hojas H e I de `iconos_sr.py` y `familia` de SRPA.
"""
import os
import subprocess
import sys
import time

H = r'D:\DAE\_repo\herramientas'
for sub in ('motion', 'cartones', 'montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_sr as R                                   # noqa: E402

AEP = R.MOTION + r'\SRPA_mg.aep'
ICONOS = R.MOTION + r'\iconos'
FPS = 24000 / 1001
CABEZA = 182 + 119

# la retícula de los cartones de caso
BAR_X, BAR_W, TEXT_X, MAXW, CENTRO_Y, BAR_PAD = 175, 14, 243, 1150, 575, 30
TIT, CUE = 54, 44
ICON, GAP_ICON, SEP_FILA, GAP_TIT = 72, 26, 26, 30
TINTE = [0, 72 / 255.0, 144 / 255.0]
TINTE_OP = 46
ANTES, DESPUES = 10, 12

# clave -> (titulo o None, [(icono, fila, (bloque, palabras con que entra))])
ITEMS = {
 'NICO': [
  ('desayuno', None, [
   ('plato', 'Un tamal', ('n11_desayuno', 'un tamal, una')),
   ('sopa', 'Una porción de caldo de costilla', ('n11_desayuno', 'una porción de caldo')),
   ('taza', 'Una bebida caliente', ('n11_desayuno', 'una bebida caliente')),
   ('billete', '$18.000', ('n11_desayuno', 'cuyo valor comercial')),
  ]),
  ('policia', None, [
   ('grupo', 'No identificaron plenamente a todas las personas que participaron en '
    'la agresión', ('n20_omisiones', 'no identificaron plenamente')),
   ('video', 'No solicitaron el video grabado por uno de los presentes',
    ('n20_omisiones', 'no solicitaron el video')),
   ('curita', 'Tampoco dejaron constancia inicial de las lesiones',
    ('n20_omisiones', 'tampoco dejaron constancia')),
  ]),
  ('cae', None, [
   ('plato', 'Alimentación', ('n26_cae', 'alimentación, alojamiento')),
   ('cama', 'Alojamiento', ('n26_cae', 'alojamiento, atención')),
   ('cruz_medica', 'Atención médica', ('n26_cae', 'atención médica y')),
   ('escudo', 'Protección', ('n26_cae', 'protección.')),
  ]),
  ('defensor', None, [
   ('lupa_doc', 'No profundizó en las circunstancias de las anteriores sustracciones',
    ('n33_preparacion', 'no profundizó en')),
   ('doc_sello', 'No verificó si existían denuncias formalmente presentadas por los '
    'demás comerciantes', ('n33_preparacion', 'no verificó si')),
   ('estetoscopio', 'No solicitó la valoración médico-legal de las lesiones',
    ('n33_preparacion', 'no solicitó la')),
   ('familia', 'Tampoco exploró las condiciones personales, familiares y sociales del '
    'adolescente', ('n33_preparacion', 'tampoco exploró las')),
  ]),
  ('valoracion', 'En la valoración inicial se observaron:', [
   ('pie', 'Uñas de los pies engrosadas, decoloradas y deterioradas',
    ('n37_valoracion', 'uñas de los')),
   ('zapato_olor', 'Olor intenso proveniente de sus pies y calzado',
    ('n38_olor', 'Olor intenso proveniente')),
   ('peine', 'Presencia de pediculosis en el cuero cabelludo',
    ('n38_olor', 'Presencia de pediculosis')),
   ('curita', 'Lesiones visibles en el rostro y las extremidades inferiores',
    ('n39_lesiones', 'Lesiones visibles en')),
   ('bascula', 'Bajo peso', ('n40_peso', 'Bajo peso y')),
  ]),
 ],
}
# el título de la valoración entra con su bloque (lo dice la voz)
TITULO_EN = {('NICO', 'valoracion'): ('n37_valoracion', 'En la valoración inicial')}


def nombre_comp(L, clave):
    return 'SR_%s_%s' % (L, clave)


def archivo(L, clave):
    return os.path.join(R.sub(L, '09 MOTION GRAPHICS'), nombre_comp(L, clave) + '.mov')


def _norm(s):
    import cartones_sr as CS
    return CS.norm(s)


def comprobar(L):
    """Cada fila (y cada título) es literal de su bloque, salvo la mayúscula."""
    from guion_sr import bloques
    tx = {b[0]: ' '.join(b[2].split()) for b in bloques(L)}
    fallas = []
    for clave, tit, filas in ITEMS[L]:
        if tit:
            bl = TITULO_EN[(L, clave)][0]
            if tit[0].lower() + tit[1:] not in tx[bl] and tit not in tx[bl]:
                fallas.append((clave, tit))
        for ico, fila, (bl, _) in filas:
            f = fila[0].lower() + fila[1:]
            if fila not in tx[bl] and f not in tx[bl]:
                fallas.append((clave, fila))
    return fallas


def tiempos(L):
    """{clave: (ini, fin, [cuadro de cada fila], cuadro del titulo)} en cuadros
    de la linea."""
    import json
    import cartones_sr as CS
    from guion_sr import bloques
    tx = {b[0]: ' '.join(b[2].split()) for b in bloques(L)}
    rej = json.load(open(os.path.join(R.voces(L), 'SR_%s_rejilla.json' % L), encoding='utf-8'))
    tr = rej['tramos']
    idx = {t['bloque']: i for i, t in enumerate(tr)}
    out = {}
    for clave, tit, filas in ITEMS[L]:
        fr = [CS.entra(L, bl, tx[bl], q)[0] for _, _, (bl, q) in filas]
        t_tit = None
        if tit:
            bl, q = TITULO_EN[(L, clave)]
            t_tit = CS.entra(L, bl, tx[bl], q)[0]
        ini = (t_tit if t_tit is not None else fr[0]) - ANTES
        ultimo = filas[-1][2][0]
        fin = CABEZA + int(round(tr[idx[ultimo]]['sale'] * FPS)) + DESPUES
        if idx[ultimo] + 1 < len(tr):
            fin = min(fin, CABEZA + int(round(tr[idx[ultimo] + 1]['entra'] * FPS)))
        out[clave] = (ini, fin, fr, t_tit)
    return out


def lista(L):
    """[(cuadro de la linea, cuadros, archivo)] para `sr_pieza` y `cartones_sr`."""
    if L not in ITEMS:
        return []
    return [(a, b - a, archivo(L, k)) for k, (a, b, _, _) in sorted(tiempos(L).items(),
                                                                       key=lambda x: x[1][0])]


# ------------------------------------------------------------------ After Effects
def componer(L, clave, tit, filas, t):
    import mg_ma as M
    ini, fin, fr, t_tit = t
    n = fin - ini
    if tit:
        lt, th = M.maquetar([(tit, 'bold', TIT, 0)], MAXW)
        th += GAP_TIT
    else:
        lt, th = [], 0
    x_lab = TEXT_X + ICON + GAP_ICON
    fl = []
    for (ico, rot, _), f in zip(filas, fr):
        lab, lh = M.maquetar([(rot, 'med', CUE, 0)], MAXW - ICON - GAP_ICON)
        fl.append((ico, lab, lh, max(ICON, lh), max(8, f - ini)))
    alto = th + sum(f[3] for f in fl) + SEP_FILA * (len(fl) - 1)
    off = int(CENTRO_Y - alto / 2.0)
    c = M.Comp(nombre_comp(L, clave), n)
    # el tinte de los cartones, a cuadro completo, debajo de todo
    c.add('addShape', shape='rectangle', size=[1920, 1080], fillColor=TINTE, name='tinte')
    c.add('setLayerProperty', layer='tinte', property='anchorPoint', value=[0, 0])
    c.add('setLayerProperty', layer='tinte', property='position', value=[960, 540])
    c.key('tinte', 'opacity', [0, 10, n - 10, n], [0, TINTE_OP, TINTE_OP, 0])
    # la barra amarilla, de la retícula A
    top, alto_b = off - BAR_PAD, alto + 2 * BAR_PAD
    c.add('addShape', shape='rectangle', size=[BAR_W, alto_b], fillColor=M.BAR_C, name='barra')
    c.add('setLayerProperty', layer='barra', property='anchorPoint', value=[0, -alto_b / 2.0])
    c.add('setLayerProperty', layer='barra', property='position', value=[BAR_X + BAR_W / 2.0, top])
    c.key('barra', 'scale', [0, 10, n - 10, n], [[100, 0], [100, 100], [100, 100], [100, 0]])
    elementos = len(lt) + sum(1 + len(f[1]) for f in fl)
    out = M.salidas(n, elementos)
    k = 0
    f_tit = max(6, (t_tit or ini) - ini + 4)
    for i, ln in enumerate(lt):
        c.texto(TEXT_X, off + ln['base'], ln, f_tit + i * M.RET_IN, out[k])
        k += 1
    y = off + th
    for ico, lab, lh, rh, f in fl:
        c.icono(ico, TEXT_X + ICON / 2.0, y + rh / 2.0, ICON, f, out[k])
        k += 1
        ytxt = y + (rh - lh) / 2.0
        for j, ln in enumerate(lab):
            c.texto(x_lab, ytxt + ln['base'], ln, f + 3 + j * 2, out[k])
            k += 1
        y += rh + SEP_FILA
    return c, off - BAR_PAD, off + alto + BAR_PAD


def armar(L):
    import shutil
    import mg_ma as M
    fallas = comprobar(L)
    if fallas:
        raise SystemExit('filas que no estan VERBATIM: %s' % fallas)
    info = M.cmd('getProjectInfo', {})
    if os.path.normcase(os.path.normpath(info.get('path') or '')) != os.path.normcase(AEP):
        raise SystemExit('AE tiene abierto %r y no el AEP del curso (%s)' % (info.get('path'), AEP))
    r = M.cmd('getProjectItems', {})
    existentes = {it['name']: it for it in (r['items'] if isinstance(r, dict) else r)}
    usados = sorted({f[0] for _, _, filas in ITEMS[L] for f in filas})
    for ico in usados:
        src = os.path.join(ICONOS, ico + '.png')
        if not os.path.exists(src):
            shutil.copy2(os.path.join(M.ICONOS, ico + '.png'), src)
        if 'ico_' + ico not in existentes:
            M.cmd('importFootage', {'path': src, 'name': 'ico_' + ico})
    T = tiempos(L)
    for clave, tit, filas in ITEMS[L]:
        nm = nombre_comp(L, clave)
        if nm in existentes:
            M.cmd('deleteItem', {'itemName': nm})
        c, cima, base = componer(L, clave, tit, filas, T[clave])
        M.batch(c.c)
        a, b = T[clave][0], T[clave][1]
        print('%-11s %5d-%5d  %4d f  %3d capas  bloque y %d-%d' % (clave, a, b, b - a, c.k, cima, base),
              flush=True)
    M.cmd('saveProject', {'path': AEP})
    print('ARMADO', flush=True)


def render(L, saltar=False):
    import mg_ma as M
    for clave, _, _ in ITEMS[L]:
        nm = nombre_comp(L, clave)
        out = archivo(L, clave)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if saltar and os.path.exists(out) and os.path.getsize(out) > 0:
            continue
        if os.path.exists(out):
            import sr_pieza as GP
            GP.aparta(out, 'rerender_%s' % time.strftime('%H%M%S'))
        t = time.time()
        r = subprocess.run([M.AERENDER, '-project', AEP, '-comp', nm, '-OMtemplate', M.OM,
                            '-output', out], capture_output=True, text=True, errors='replace')
        ok = os.path.exists(out) and os.path.getsize(out) > 0
        print('%-11s %s %.0f s %s' % (clave, 'OK' if ok else 'FALLA', time.time() - t,
                                      '' if ok else r.stdout[-600:]), flush=True)
    print('RENDER LISTO', flush=True)


def plan(L):
    print('fallas verbatim:', comprobar(L) or 'ninguna')
    for clave, (a, b, fr, tt) in sorted(tiempos(L).items(), key=lambda x: x[1][0]):
        print('%-11s %5d-%5d (%4d f)  titulo %s  filas %s' % (clave, a, b, b - a, tt, [f - a for f in fr]))


if __name__ == '__main__':
    accion, L = sys.argv[1], sys.argv[2].upper()
    {'plan': plan, 'armar': armar, 'render': render,
     'faltan': lambda L: render(L, saltar=True)}[accion](L)
