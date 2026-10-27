# -*- coding: utf-8 -*-
r"""Las situaciones en video, de la placa elegida al MP4 de entrega.

    python sit_pieza.py A elegir construir blancos musica
    python sit_pieza.py A montar            (dentro de Resolve: venv del MCP)
    python sit_pieza.py A exportar entregas verificar

Es el pipeline del caso integrador (construir_df, respiros_df, linea_df_v2,
montar_v2_df, exportar_df, entregas_df) puesto en UN modulo y apuntado al
arbol de `rutas_sit`. Nada de la geometria cambia:

    intro 182 · entrada 119 · ranuras · respiro 48 · cierre 119 · outro 182

y la pieza que sale mide exactamente el `pieza` de SIT_<L>_ranuras.json.

LOS PASOS
    elegir     copia la candidata escogida (elegidas_sit.json) de
               01 PLANOS/_candidatas a 01 PLANOS/<nombre>.png, con la
               LIMPIEZA DE COLOR por bandas (abajo). Si ya habia otra
               elegida, la vieja va a _descartes con el motivo en el nombre.
    construir  grade por registro con techo (graduar_registro) a _grade, y
               horneado de camara SIN empuje (encuadre 0,88, pulso 5) a
               10 TIMELINE SEBASTIAN/RANURAS. Respiro: r01 graduada, 48
               cuadros quieta, a RESPIRO.
    blancos    carton de entrada y de cierre: fondo blanco, filete amarillo,
               marca al 10 %. Antetitulo el curso, titulo «Situación X».
               No se inventa un titulo: los nombres de carpeta («La ultima
               llamada»...) son de trabajo y no salen en pantalla.
    musica     la cama TA03 del caso integrador, con el ducking horneado
               contra los tramos REALES de la voz (rejilla).
    montar     la linea en Resolve, en los bins del arbol, y el .drt.
    exportar   master H264_NVIDIA 80000 en D:\DAE\_tmp\sit\render.
    entregas   MP4 Fiscalia (x264 crf 18 slow animation) + copia 720p.
    verificar  cuadros, negros, loudness y una hoja de cuadros sueltos.

LA LIMPIEZA DE COLOR, POR QUE Y COMO
    Las placas de noche de la A salieron AZULES: en r08 el 16-17 % de los
    pixeles pasa de saturacion 0,25, todos en la franja fria. La regla de la
    serie es que el unico color saturado del cuadro es el acento de quien
    es buscado. Se hace lo del C4 (franja fria desaturada con rampa), y se
    agrega lo que la situacion pide:
        - verde, franja fria y magenta (H PIL 58-255): x0,08 siempre;
        - amarillo (H 26-58) x0,15 si el plano NO lleva acento: un amarillo
          suelto le roba el color a quien lo lleva;
        - plano sin gente y sin acento: todo x0,15 (ni el cielo calido ni
          la luz trasera roja de un carro quedan en color).
    El peso se difumina en el espacio antes de aplicarse (la leccion de
    `fijar_suave`: dos vecinos nunca se tratan distinto) y las bandas
    tienen rampa de 8 unidades de tono. La piel -calida, H 0-25- no se toca.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', 'musica', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_sit as R                                   # noqa: E402
from guion_sit import SITUACIONES                       # noqa: E402

FPS = '24000/1001'
FPS_N = 24000 / 1001.0
T0 = 86400
N_INTRO, N_BLANCO, N_RESPIRO, N_MARCA = 182, 119, 48, 168
CABEZA = N_INTRO + N_BLANCO
COMUNES = r'E:\DAE MASTER\00 COMUNES'
INTRO = os.path.join(COMUNES, 'INTRO', 'FGN_intro_version7.mp4')
MARCA = os.path.join(COMUNES, 'MARCA DE AGUA', 'MARCA_DE_AGUA_DAE_7s_fade.mov')
MARCA_PNG = os.path.join(COMUNES, 'MARCA DE AGUA', 'APRENDE_CON_LA_DAE_alfa.png')
PISTA_MUSICA_FUENTE = r'D:\DAE\_tmp\musica\TA03.mp3'
TMP = r'D:\DAE\_tmp\sit'
RENDER = os.path.join(TMP, 'render')
ELEGIDAS = os.path.join(H, 'prompts', 'elegidas_sit.json')
ANTE = 'Investigación judicial y forense de la desaparición forzada'

PISTAS_V = ((1, 'VIDEO'), (2, 'MOVIMIENTO'), (3, 'DETALLE'), (4, 'CARTONES'),
            (5, 'APOYO'), (6, 'MARCA DE AGUA'), (7, 'EFECTOS'), (8, 'LOWER THIRD'))
PISTAS_A = ((1, 'NARRADOR'), (2, 'PREGUNTAS'), (3, 'DIALOGO'),
            (4, 'AMBIENTE'), (5, 'MUSICA'))
PISTA_MUSICA, PISTA_AMBIENTE = 5, 4


def w(*a):
    print(*a, flush=True)


def E(L):
    return __import__('escenas_sit_%s' % L.lower())


def nombre(L, n):
    return 'SIT_%s_r%02d_%s' % (L, n, E(L).NOMBRE[n])


def pieza(L):
    return json.load(open(os.path.join(R.voces(L), 'SIT_%s_ranuras.json' % L),
                          encoding='utf-8'))['pieza']


VERSION = 1


def nombre_linea(L):
    """La v1 se llama como siempre; desde la v2 la linea lleva la version en
    el nombre, para que en el bin se distingan sin abrirlas."""
    base = 'SIT ' + SITUACIONES[L][1].replace('SITUACION ', '').replace(' - ', ' ')
    return base if VERSION <= 1 else '%s v%d' % (base, VERSION)


def cuadros(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                        '-count_frames', '-show_entries', 'stream=nb_read_frames',
                        '-of', 'default=nw=1:nk=1', p], capture_output=True,
                       text=True).stdout.split()
    return int(r[0]) if r else -1


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def aparta(p, motivo):
    """Nada se borra: lo que se reemplaza va a _descartes con el motivo."""
    if not os.path.exists(p):
        return
    d = os.path.join(os.path.dirname(p), '_descartes')
    os.makedirs(d, exist_ok=True)
    b, e = os.path.splitext(os.path.basename(p))
    dest = os.path.join(d, '%s__%s%s' % (b, motivo, e))
    k = 2
    while os.path.exists(dest):
        dest = os.path.join(d, '%s__%s_%d%s' % (b, motivo, k, e))
        k += 1
    shutil.move(p, dest)


# ---------------------------------------------------------------- color
def _peso_banda(h, a, b, rampa=8.0):
    """1 dentro de [a, b], 0 fuera, con rampa lineal."""
    import numpy as np
    x = np.minimum(h - (a - rampa), (b + rampa) - h) / rampa
    return np.clip(x, 0.0, 1.0)


def limpia(src, dst, acento, gente):
    import numpy as np
    from PIL import Image, ImageFilter
    im = Image.open(src).convert('RGB')
    hsv = np.asarray(im.convert('HSV')).astype(np.float32)
    h, s = hsv[..., 0], hsv[..., 1]
    k = np.ones_like(s)
    frio = _peso_banda(h, 66, 262)
    k = np.minimum(k, 1 - frio * (1 - 0.08))
    if not acento:
        am = _peso_banda(h, 30, 54)
        k = np.minimum(k, 1 - am * (1 - 0.15))
    if not acento and not gente:
        k = np.minimum(k, 0.15)
    # el peso se difumina antes de aplicarse: dos vecinos nunca distintos
    km = Image.fromarray(np.clip(k * 255, 0, 255).astype(np.uint8), 'L')
    km = km.filter(ImageFilter.GaussianBlur(6))
    k = np.asarray(km).astype(np.float32) / 255.0
    hsv[..., 1] = s * k
    out = Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV').convert('RGB')
    out.save(dst)
    return medir_color(dst)


def medir_color(p):
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(p).convert('HSV')).reshape(-1, 3).astype(np.float32)
    h, s, v = a[:, 0], a[:, 1] / 255.0, a[:, 2]
    lit = v > 40
    def banda(lo, hi):
        # un gris puro tiene tono 0: sin el piso de saturacion cae en la calida
        m = lit & (s > 0.04) & (h >= lo) & (h <= hi)
        return float(np.percentile(s[m], 90)) if m.sum() > 500 else 0.0
    return {'calida_p90': round(banda(0, 27), 3),
            'amarilla_p90': round(banda(28, 55), 3),
            'fria_p90': round(max(banda(110, 255), 0), 3),
            'sat_media': round(float(s[lit].mean()) if lit.any() else 0, 3)}


def con_acento(L, n):
    import base_sit as S
    r = E(L).R[n]
    gente, acento = r[2], r[3]
    if acento is None:
        acento = any(p in S.CON_ACENTO for p in gente)
    # el sombrero de la D (r06) es acento sin persona: lo dice el texto
    if 'mustard' in r[6].lower():
        acento = True
    return bool(acento), bool(gente)


# ---------------------------------------------------------------- pasos
def elegir(L):
    el = json.load(open(ELEGIDAS, encoding='utf-8'))[L]
    pl = R.sub(L, '01 PLANOS')
    cand = os.path.join(pl, '_candidatas')
    hecho_p = os.path.join(pl, '_elegidas_aplicadas.json')
    hecho = json.load(open(hecho_p, encoding='utf-8')) if os.path.exists(hecho_p) else {}
    for n in sorted(E(L).R):
        nm = nombre(L, n)
        v = el[str(n)]
        src = os.path.join(cand, '%s_%s.png' % (nm, v))
        dst = os.path.join(pl, nm + '.png')
        assert os.path.exists(src), src
        firma = '%s:%s' % (v, md5(src)[:10])
        if hecho.get(nm) == firma and os.path.exists(dst):
            w('r%02d %s ya aplicada' % (n, v))
            continue
        if os.path.exists(dst):
            aparta(dst, 'reemplazada_por_candidata_%s' % v)
        ac, ge = con_acento(L, n)
        antes = medir_color(src)
        despues = limpia(src, dst, ac, ge)
        hecho[nm] = firma
        w('r%02d %s  acento %-5s gente %-5s  fria %.3f->%.3f  amarilla %.3f->%.3f'
          '  calida %.3f->%.3f' % (n, v, ac, ge, antes['fria_p90'], despues['fria_p90'],
                                   antes['amarilla_p90'], despues['amarilla_p90'],
                                   antes['calida_p90'], despues['calida_p90']))
    json.dump(hecho, open(hecho_p, 'w', encoding='utf-8'), indent=1)


def construir(L, solo=None):
    import camara
    import graduar_registro as GR
    pl = R.sub(L, '01 PLANOS')
    gd = os.path.join(pl, '_grade')
    os.makedirs(gd, exist_ok=True)
    tl = R.sub(L, '10 TIMELINE SEBASTIAN')
    ran = os.path.join(tl, 'RANURAS')
    os.makedirs(ran, exist_ok=True)
    for n in sorted(E(L).R):
        if solo and n not in solo:
            continue
        largo, reg = E(L).R[n][0], E(L).R[n][1]
        nm = nombre(L, n)
        o, g = os.path.join(pl, nm + '.png'), os.path.join(gd, nm + '.png')
        c = GR.medir(o)
        GR.graduar(o, g, reg, techo=True)
        # 27 oct: el grade de contraluz le devolvio un cian a A r09 (frio p90
        # 0,02 -> 0,07; se ve en la ropa clara). Si el grade deja frio, la
        # limpieza de bandas se vuelve a pasar DESPUES del grade.
        fr = medir_color(g)['fria_p90']
        if fr > 0.05:
            ac, ge = con_acento(L, n)
            w('r%02d frio despues del grade %.3f -> %.3f'
              % (n, fr, limpia(g, g, ac, ge)['fria_p90']))
        v = GR.medir(g)
        sal = os.path.join(ran, '%s_v%d.mp4' % (nm, largo))
        if os.path.exists(sal):
            aparta(sal, 'rehorneada_%s' % time.strftime('%H%M%S'))
        t0 = time.time()
        camara.render({'modo': 'camara', 'fuente': g, 'salida': sal,
                       'frames': largo, 'encuadre': 0.88, 'empuje': 0.0,
                       'deriva': [0.0, 0.0], 'vibra': 5.0})
        nf = cuadros(sal)
        w('r%02d %-9s crudo %3.0f/%3.0f/%3.0f  final %3.0f/%3.0f/%3.0f  obj %3d  '
          '%4d/%4d %s  %.0f s' % (n, reg, c[0], c[1], c[2], v[0], v[1], v[2],
                                  GR.REGISTRO[reg][1], nf, largo,
                                  'OK' if nf == largo else 'FALLA', time.time() - t0))
        assert nf == largo, (nm, nf, largo)
    # el respiro: la r01 graduada, 48 cuadros, quieta
    g1 = os.path.join(gd, nombre(L, 1) + '.png')
    rd = os.path.join(tl, 'RESPIRO')
    os.makedirs(rd, exist_ok=True)
    d = os.path.join(rd, 'SIT_%s_respiro_v%d.mp4' % (L, N_RESPIRO))
    if os.path.exists(d):
        aparta(d, 'rehecho_%s' % time.strftime('%H%M%S'))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-i', g1,
                    '-vf', 'scale=1920:1080:flags=lanczos,fps=%s' % FPS,
                    '-frames:v', str(N_RESPIRO), '-c:v', 'libx264', '-crf', '14',
                    '-preset', 'slow', '-pix_fmt', 'yuv420p', '-an', d], check=True)
    w('respiro %d/%d' % (cuadros(d), N_RESPIRO))


def blancos(L):
    import cartones_ta as C
    C.MARCA = MARCA_PNG
    cart = R.sub(L, '02 CARTONES')
    for k in ('entrada', 'cierre'):
        p = os.path.join(cart, 'SIT_%s_carton_%s.mov' % (L, k))
        if os.path.exists(p):
            aparta(p, 'rehecho_%s' % time.strftime('%H%M%S'))
        C.render_carton({'ante': ANTE, 'titulo': 'Situación %s' % L}, N_BLANCO,
                        C.BLANCO_FONDO, False, p, con_marca=True)
        w('%s %d cuadros' % (os.path.basename(p), cuadros(p)))


def musica(L):
    rej = json.load(open(os.path.join(R.voces(L), 'SIT_%s_rejilla.json' % L),
                        encoding='utf-8'))
    off = CABEZA / FPS_N
    voz = [[round(off + t['entra'], 3), round(off + t['sale'], 3)] for t in rej['tramos']]
    sal = os.path.join(R.sub(L, '08 MUSICA'), 'SIT_%s_MUSICA_cama.wav' % L)
    os.makedirs(os.path.dirname(sal), exist_ok=True)
    if os.path.exists(sal):
        aparta(sal, 'rehecha_%s' % time.strftime('%H%M%S'))
    spec = [{'pista': PISTA_MUSICA_FUENTE, 'salida': sal,
             'dur': round(pieza(L) / FPS_N, 3), 'voz': voz, 'objetivo': -26.0}]
    sp = os.path.join(TMP, 'spec_musica_sit_%s.json' % L)
    json.dump(spec, open(sp, 'w', encoding='utf-8'), indent=1)
    r = subprocess.run([sys.executable, os.path.join(H, 'musica', 'cama_musica.py'), sp],
                       capture_output=True, text=True)
    w(r.stdout.strip(), r.stderr.strip()[-400:])


# ---------------------------------------------------------------- linea
def plan(L):
    import cartones_sit as CS
    base = R.carpeta(L)
    tl = os.path.join(base, '10 TIMELINE SEBASTIAN')
    cart = os.path.join(base, '02 CARTONES')
    v1, t = [], 0
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'SIT_%s_carton_entrada.mov' % L)))
    t += N_BLANCO
    ini = t
    for n in sorted(E(L).R):
        largo = E(L).R[n][0]
        v1.append((t, largo, os.path.join(tl, 'RANURAS', '%s_v%d.mp4'
                                          % (nombre(L, n), largo))))
        t += largo
    fin = t
    v1.append((t, N_RESPIRO, os.path.join(tl, 'RESPIRO', 'SIT_%s_respiro_v%d.mp4'
                                          % (L, N_RESPIRO))))
    t += N_RESPIRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'SIT_%s_carton_cierre.mov' % L)))
    t += N_BLANCO
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO
    v4 = [(c['ini'], c['cuadros'], os.path.join(cart, c['archivo']))
          for c in CS.calcula(L)]
    v6 = [(ini, N_MARCA, MARCA), (fin - N_MARCA, N_MARCA, MARCA)]
    voz = os.path.join(R.voces(L), 'SIT_%s_NARRADOR.wav' % L)
    mus = os.path.join(base, '08 MUSICA', 'SIT_%s_MUSICA_cama.wav' % L)
    return v1, v4, v6, voz, mus, ini, fin - ini, t


def capas(L):
    """V2 MOVIMIENTO, V3 DETALLE y V8 LOWER THIRD: lo que exista en disco.
    Las tres son capas que se pueden apagar: debajo, V1 tiene la pieza
    completa.
        V2  10 TIMELINE SEBASTIAN/MOVIMIENTO/<ranura>_mov_v<largo>.mp4, la
            ranura entera (el clip ya trae fundidos horneados contra V1)
        V3  10 TIMELINE SEBASTIAN/DETALLE/<det>_v<cuadros>.mp4, en la ranura
            madre + `entra` (prompts_sit_<L>.json -> detalles)
        V8  02 CARTONES/LOWER THIRDS, 14 cuadros despues de abrir la ranura
    Devuelve las tres listas y lo que se espero y no estaba (para el reporte).
    """
    import lowerthirds_sit as LTS
    base = R.carpeta(L)
    tl = os.path.join(base, '10 TIMELINE SEBASTIAN')
    pos, t = {}, CABEZA
    for n in sorted(E(L).R):
        pos[n] = t
        t += E(L).R[n][0]
    v2, v3, v8, faltan = [], [], [], []
    for n in sorted(E(L).R):
        largo = E(L).R[n][0]
        p = os.path.join(tl, 'MOVIMIENTO', '%s_mov_v%d.mp4' % (nombre(L, n), largo))
        if os.path.exists(p):
            v2.append((pos[n], largo, p))
    sp = os.path.join(TMP, 'prompts_sit_%s.json' % L)
    dets = json.load(open(sp, encoding='utf-8')).get('detalles', {}) if os.path.exists(sp) else {}
    for nm, d in sorted(dets.items()):
        p = os.path.join(tl, 'DETALLE', '%s_v%d.mp4' % (nm, d['cuadros']))
        largo = E(L).R[d['ranura']][0]
        assert d['entra'] + d['cuadros'] <= largo, (nm, d, largo)
        if os.path.exists(p):
            v3.append((pos[d['ranura']] + d['entra'], d['cuadros'], p))
        else:
            faltan.append(os.path.basename(p))
    for r, n, p in LTS.lista(L):
        if os.path.exists(p):
            v8.append((pos[r] + LTS.OFF, n, p))
        else:
            faltan.append(os.path.basename(p))
    return v2, v3, v8, faltan


def huecos(tl, pista=1):
    fuera, pos = [], 0
    tot = tl.GetEndFrame() - tl.GetStartFrame()
    for it in tl.GetItemListInTrack('video', pista):
        a, b = it.GetStart() - tl.GetStartFrame(), it.GetEnd() - tl.GetStartFrame()
        if a > pos:
            fuera.append((pos, a))
        pos = max(pos, b)
    if pos < tot:
        fuera.append((pos, tot))
    return fuera


def construye(resolve, L):
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    nl = nombre_linea(L)
    existentes = [pr.GetTimelineByIndex(i) for i in range(1, int(pr.GetTimelineCount()) + 1)]
    for x in [x for x in existentes if x is not None]:
        if x.GetName() != nl:
            continue
        if x.GetItemListInTrack('video', 1):
            nombres = {pr.GetTimelineByIndex(j).GetName()
                       for j in range(1, int(pr.GetTimelineCount()) + 1)}
            k, nuevo = 1, '%s (anterior)' % nl
            while nuevo in nombres:
                k += 1
                nuevo = '%s (anterior %d)' % (nl, k)
            x.SetName(nuevo)
        else:
            mp.DeleteTimelines([x])

    v1, v4, v6, voz, mus, ini, dur_cuerpo, tot = plan(L)
    v2, v3, v8, _ = capas(L)
    assert tot == pieza(L), (tot, pieza(L))
    todos = [p for _, _, p in v1 + v2 + v3 + v4 + v6 + v8] + [voz, mus]
    falta = sorted({p for p in todos if not os.path.exists(p)})
    if falta:
        return None, 'faltan en disco: %s' % falta[:4]

    raiz = mp.GetRootFolder()

    def _hijo(f, n):
        for x in f.GetSubFolderList():
            if x.GetName() == n:
                return x
        return None

    def _asegura(f, n):
        return _hijo(f, n) or mp.AddSubFolder(f, n)

    def _baja(f, partes):
        for q in partes:
            if q:
                f = _asegura(f, q)
        return f

    comunes = None
    for x in raiz.GetSubFolderList():
        if x.GetName().strip() == '00 COMUNES':
            comunes = x
    unidad_rel = os.path.relpath(R.carpeta(L), r'E:\DAE MASTER')
    carp = _baja(raiz, unidad_rel.split(os.sep))
    sdir = R.carpeta(L)

    def _bin_de(ruta):
        r = ruta.replace('/', os.sep)
        if r.lower().startswith(sdir.lower()):
            rel = os.path.dirname(os.path.relpath(r, sdir))
            return _baja(carp, rel.split(os.sep)) if rel else carp
        if comunes is not None and '00 COMUNES' in r.upper():
            return _asegura(comunes, 'INTRO' if 'INTRO' in r.upper() else 'MARCA DE AGUA')
        return carp

    quiero = {os.path.basename(x) for x in todos if '00 COMUNES' not in x.upper()}

    def _todos(f):
        for c in f.GetClipList():
            yield c
        for sf in f.GetSubFolderList():
            for c in _todos(sf):
                yield c

    viejos = [c for c in _todos(carp)
              if os.path.basename((c.GetClipProperty('File Path') or '').replace('/', os.sep))
              in quiero]
    if viejos:
        mp.DeleteClips(viejos)

    pedidos = sorted(set(todos))
    por_bin = {}
    for x in pedidos:
        b = _bin_de(x)
        por_bin.setdefault(id(b), [b, []])[1].append(x)

    def _puestos():
        d = {}
        for b, _ in por_bin.values():
            for c in b.GetClipList():
                r = (c.GetClipProperty('File Path') or '').replace('/', os.sep)
                if r:
                    d[os.path.basename(r)] = c
        return d

    for b, lista in por_bin.values():
        mp.SetCurrentFolder(b)
        ya = _puestos()
        nuevos = [x for x in lista if os.path.basename(x) not in ya]
        if nuevos:
            mp.ImportMedia(nuevos)
    for _ in range(6):
        pool = _puestos()
        faltan = [x for x in pedidos if os.path.basename(x) not in pool]
        if not faltan:
            break
        time.sleep(0.7)
        for x in faltan:
            mp.SetCurrentFolder(_bin_de(x))
            mp.ImportMedia([x])
            time.sleep(0.15)
    pool = _puestos()
    faltan = [x for x in pedidos if os.path.basename(x) not in pool]
    if faltan:
        return None, 'no entraron al pool: %s' % faltan[:3]

    mp.SetCurrentFolder(_asegura(carp, '10 TIMELINE SEBASTIAN'))
    tl = mp.CreateEmptyTimeline(nl)
    pr.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < len(PISTAS_V):
        tl.AddTrack('video')
    while tl.GetTrackCount('audio') < len(PISTAS_A):
        tl.AddTrack('audio', 'stereo')
    for i, n in PISTAS_V:
        tl.SetTrackName('video', i, n)
    for i, n in PISTAS_A:
        tl.SetTrackName('audio', i, n)

    for lista, pista in ((v1, 1), (v2, 2), (v3, 3), (v4, 4), (v6, 6), (v8, 8)):
        if not lista:
            continue
        items = []
        for pos, largo, p in lista:
            it = pool.get(os.path.basename(p))
            if it is None:
                return None, 'no quedo en el pool: %s' % p
            items.append({'mediaPoolItem': it, 'startFrame': 0, 'endFrame': largo,
                          'trackIndex': pista, 'recordFrame': T0 + pos, 'mediaType': 1})
        mp.AppendToTimeline(items)
    for p, largo, pos, pista in ((voz, dur_cuerpo, ini, 1),
                                 (mus, tot, 0, PISTA_MUSICA),
                                 (INTRO, N_INTRO, 0, PISTA_AMBIENTE),
                                 (INTRO, N_INTRO, tot - N_INTRO, PISTA_AMBIENTE)):
        it = pool.get(os.path.basename(p))
        if it is None:
            return None, 'no quedo en el pool: %s' % p
        mp.AppendToTimeline([{'mediaPoolItem': it, 'startFrame': 0, 'endFrame': largo,
                              'trackIndex': pista, 'recordFrame': T0 + pos,
                              'mediaType': 2}])
    h = huecos(tl)
    if h:
        return tl, 'QUEDARON HUECOS en V1: %s' % h[:6]
    largo_real = tl.GetEndFrame() - tl.GetStartFrame()
    if largo_real != tot:
        return tl, 'la linea mide %d y el plan pedia %d' % (largo_real, tot)
    return tl, None


def _resolve():
    import DaVinciResolveScript as dvr
    return dvr.scriptapp('Resolve')


def montar(L):
    resolve = _resolve()
    pr = resolve.GetProjectManager().GetCurrentProject()
    w('proyecto:', pr.GetName())
    tl, err = construye(resolve, L)
    largo = (tl.GetEndFrame() - tl.GetStartFrame()) if tl else -1
    w('%s  largo %d (pieza %d)  %s' % (nombre_linea(L), largo, pieza(L), err or 'OK'))
    if err:
        raise SystemExit(err)
    v = [(i, tl.GetTrackName('video', i), len(tl.GetItemListInTrack('video', i)))
         for i in range(1, tl.GetTrackCount('video') + 1)]
    a = [(i, tl.GetTrackName('audio', i), len(tl.GetItemListInTrack('audio', i)))
         for i in range(1, tl.GetTrackCount('audio') + 1)]
    w('   ', [x for x in v if x[2]])
    w('   ', [x for x in a if x[2]])
    w('    capas que faltan en disco:', capas(L)[3] or 'ninguna')
    dest = R.sub(L, '10 TIMELINE SEBASTIAN')
    drt = os.path.join(dest, '%s.drt' % nombre_linea(L))
    if os.path.exists(drt):
        aparta(drt, 'remontada_%s' % time.strftime('%H%M%S'))
    tl.Export(drt, resolve.EXPORT_DRT)
    w('   .drt', os.path.getsize(drt) if os.path.exists(drt) else 'NO SE ESCRIBIO')
    resolve.GetProjectManager().SaveProject()


REVISION = os.path.join(TMP, 'revision')


def exportar(L, destino=None, nm=None):
    resolve = _resolve()
    pr = resolve.GetProjectManager().GetCurrentProject()
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre_linea(L):
            tl = t
    if tl is None:
        raise SystemExit('no hay linea %s' % nombre_linea(L))
    destino = destino or RENDER
    os.makedirs(destino, exist_ok=True)
    pr.SetCurrentTimeline(tl)
    pr.DeleteAllRenderJobs()
    nm = nm or 'SIT_%s_master' % L
    m = os.path.join(destino, nm + '.mp4')
    if os.path.exists(m):
        aparta(m, 'rerender_%s' % time.strftime('%H%M%S'))
    ok = pr.SetRenderSettings({'SelectAllFrames': True, 'TargetDir': destino,
                               'CustomName': nm, 'FormatWidth': 1920,
                               'FormatHeight': 1080, 'VideoQuality': 80000,
                               'AudioCodec': 'lpcm', 'AudioBitDepth': 24,
                               'AudioSampleRate': 48000})
    pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    job = pr.AddRenderJob()
    w('render %s job %s settings %s' % (nm, job, ok))
    pr.StartRendering([job])
    t0 = time.time()
    while pr.IsRenderingInProgress():
        time.sleep(3)
    st = pr.GetRenderJobStatus(job)
    w('   %s %s %.0f s' % (st.get('JobStatus'), st.get('CompletionPercentage'),
                           time.time() - t0))


FISCALIA = ['-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-tune', 'animation',
            '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
            '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
            '-c:a', 'copy', '-movflags', '+faststart']
LIGERA = ['-vf', 'scale=1280:720:flags=lanczos', '-c:v', 'libx264', '-crf', '25',
          '-preset', 'medium', '-tune', 'animation', '-pix_fmt', 'yuv420p',
          '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart']


def entregas(L, version=1):
    m = os.path.join(RENDER, 'SIT_%s_master.mp4' % L)
    exp = R.sub(L, '05 EXPORTS')
    os.makedirs(exp, exist_ok=True)
    f = os.path.join(exp, 'SIT_%s_v%d.mp4' % (L, version))
    l = os.path.join(exp, 'SIT_%s_v%d_revision_720p.mp4' % (L, version))
    for p in (f, l):
        if os.path.exists(p):
            aparta(p, 'reexportada_%s' % time.strftime('%H%M%S'))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', m] + FISCALIA + [f], check=True)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', m] + LIGERA + [l], check=True)
    a, b, c = cuadros(m), cuadros(f), cuadros(l)
    w('cuadros master %d fiscalia %d ligera %d pieza %d  %s'
      % (a, b, c, pieza(L), 'OK' if a == b == c == pieza(L) else 'NO CUADRA'))
    w('MB %d / %d / %d' % (os.path.getsize(m) >> 20, os.path.getsize(f) >> 20,
                           os.path.getsize(l) >> 20))


def verificar(L, version=1):
    exp = R.sub(L, '05 EXPORTS')
    f = os.path.join(exp, 'SIT_%s_v%d.mp4' % (L, version))
    n = cuadros(f)
    w('cuadros %d / pieza %d  %s' % (n, pieza(L), 'OK' if n == pieza(L) else 'FALLA'))
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', f, '-vf',
                        'blackdetect=d=0.04:pix_th=0.06', '-an', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    negros = [l.split('blackdetect')[1].strip() for l in r.splitlines() if 'black_start' in l]
    w('negros:', negros or 'ninguno')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f, '-af', 'ebur128=peak=true',
                        '-vn', '-f', 'null', '-'], capture_output=True, text=True).stderr
    for l in r.splitlines()[-14:]:
        if l.strip().startswith(('I:', 'Peak:', 'LRA:')):
            w('   ', l.strip())
    # una hoja con un cuadro a mitad de cada ranura + entrada y cierre
    from PIL import Image
    v1, v4, v6, voz, mus, ini, dur, tot = plan(L)
    marcas = [pos + largo // 2 for pos, largo, _ in v1]
    hoja = Image.new('RGB', (4 * 480, ((len(marcas) + 3) // 4) * 270), (20, 20, 20))
    for i, q in enumerate(marcas):
        p = os.path.join(TMP, '_q_%s.png' % L)   # uno por situacion: corren a la vez
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ((q + 0.5) / FPS_N),
                        '-i', f, '-frames:v', '1', '-vf', 'scale=480:270', p], check=True)
        hoja.paste(Image.open(p), ((i % 4) * 480, (i // 4) * 270))
    hp = os.path.join(TMP, 'verif_%s.jpg' % L)
    hoja.save(hp, quality=85)
    w('hoja', hp)


def revisar(L):
    """Chequeo de la linea SIN EXPORTAR (27 oct, Sebastian: «timeline
    completa en su carpeta de DaVinci, sin exportar todavia»). Se rinde a
    D:\\DAE\\_tmp\\sit\\revision -nunca a 05 EXPORTS- y sobre ese archivo:
    cuadros = pieza, negros, loudness, y una hoja con un cuadro a mitad de
    cada ranura, de cada detalle (V3), de cada movimiento (V2) y de cada
    rotulo (V8): lo que la pista agrega se tiene que VER en la hoja."""
    nm = 'SIT_%s_v%d_REVISION_INTERNA' % (L, VERSION)
    exportar(L, REVISION, nm)
    f = os.path.join(REVISION, nm + '.mp4')
    n = cuadros(f)
    w('cuadros %d / pieza %d  %s' % (n, pieza(L), 'OK' if n == pieza(L) else 'FALLA'))
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', f, '-vf',
                        'blackdetect=d=0.04:pix_th=0.06', '-an', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    negros = [l.split('blackdetect')[1].strip() for l in r.splitlines() if 'black_start' in l]
    w('negros:', negros or 'ninguno')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f, '-af', 'ebur128=peak=true',
                        '-vn', '-f', 'null', '-'], capture_output=True, text=True).stderr
    for l in r.splitlines()[-14:]:
        if l.strip().startswith(('I:', 'Peak:', 'LRA:')):
            w('   ', l.strip())
    from PIL import Image, ImageDraw
    v1, v4, v6, voz, mus, ini, dur, tot = plan(L)
    v2, v3, v8, _ = capas(L)
    marcas = [('V1', pos + largo // 2) for pos, largo, _ in v1]
    marcas += [('V2', pos + largo // 2) for pos, largo, _ in v2]
    marcas += [('V3', pos + largo // 2) for pos, largo, _ in v3]
    marcas += [('V8', pos + 60) for pos, largo, _ in v8]
    marcas.sort(key=lambda x: x[1])
    hoja = Image.new('RGB', (4 * 480, ((len(marcas) + 3) // 4) * 270), (20, 20, 20))
    d = ImageDraw.Draw(hoja)
    for i, (k, q) in enumerate(marcas):
        p = os.path.join(TMP, '_q_%s.png' % L)
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ((q + 0.5) / FPS_N),
                        '-i', f, '-frames:v', '1', '-vf', 'scale=480:270', p], check=True)
        x, y = (i % 4) * 480, (i // 4) * 270
        hoja.paste(Image.open(p), (x, y))
        d.text((x + 6, y + 4), '%s %d' % (k, q), fill=(255, 255, 0))
    hp = os.path.join(TMP, 'revision_%s_v%d.jpg' % (L, VERSION))
    hoja.save(hp, quality=85)
    w('hoja', hp, ' V2 %d  V3 %d  V8 %d' % (len(v2), len(v3), len(v8)))


PASOS = {'elegir': elegir, 'construir': construir, 'blancos': blancos,
         'musica': musica, 'montar': montar, 'exportar': exportar,
         'entregas': entregas, 'verificar': verificar, 'revisar': revisar}

if __name__ == '__main__':
    # `construir=5,6,7` rehace solo esas ranuras (27 oct: un apagon corto D y E
    # a mitad del horneado; lo ya horneado y verificado no se toca).
    # `v=2` antes de los pasos: la linea se llama «... v2» (montar, revisar).
    L = sys.argv[1].upper()
    for p in sys.argv[2:]:
        if p.startswith('v='):
            VERSION = int(p[2:])
            continue
        w('===', L, p)
        t0 = time.time()
        paso, _, arg = p.partition('=')
        if arg:
            PASOS[paso](L, solo={int(x) for x in arg.split(',')})
        else:
            PASOS[paso](L)
        w('--- %s %.0f s' % (p, time.time() - t0))
    w('LISTO')
