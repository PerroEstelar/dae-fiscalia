# -*- coding: utf-8 -*-
r"""Arma la linea de tiempo completa de un capitulo dentro de Resolve.

LA GEOMETRIA ES LA DE LA SERIE
    intro 182 · entrada 119 · las ranuras · respiro 48 · cierre 119 ·
    outro 182. El `pieza` que la rejilla de voz trae escrito ya cuenta con
    esta cabeza y esta cola.

EL CUADRO NEGRO ENTRE CLIP Y CLIP: endFrame NO ES INCLUSIVO
    27 de octubre, Sebastian: «estas dejando gaps entre clips, unos pequenos
    gaps negros que no sirven». Medido: UN CUADRO NEGRO ENTERO en CADA corte
    -veinte en el capitulo 1, quince en el 2-.

    La causa: este armador pasaba `endFrame = largo - 1`, pero la duracion
    que Resolve calcula es `endFrame - startFrame`. O sea que cada clip
    quedaba un cuadro corto y el siguiente arrancaba en su sitio, dejando el
    hueco. Tambien explica por que el total de la linea daba siempre UNO
    MENOS que el `pieza` de la rejilla.

    Se comprueba al final: `huecos()` recorre V1 y falla si queda uno solo.

LAS PISTAS SON LAS DE LAS OTRAS 46 LINEAS DEL PROYECTO
    V1 VIDEO          intro, entrada, ranuras, respiro, cierre, outro.
    V2 MOVIMIENTO     los clips generados, cada uno sobre SU ranura, con la
                      fundida horneada en el archivo.
    V3 CARTONES       los verbatim. Cada uno dura LO QUE LA VOZ TARDA EN
                      DECIR SU ORACION y va en su posicion absoluta de la
                      pieza, cruzando los cortes que haga falta.
    V4 APOYO          vacia, como en el resto de la serie.
    V5 MARCA DE AGUA  al principio y al final del cuerpo.
    V6 EFECTOS        vacia.
    V7 LOWER THIRD    el rotulo de quien acaba de entrar.
    A1 NARRADOR       el master de voz, despues del intro y de la entrada.
    A5 MUSICA         la cama. VA EN A5: una pista de audio agregada en el
                      indice 2 no llega al bus principal de este build y el
                      render sale con los huecos en silencio digital, sin un
                      solo error.

NO REMONTA ENCIMA: APARTA Y VUELVE A ARMAR
    Una linea que ya tiene clips no se borra -puede llevar trabajo a mano-.
    Se le cambia el nombre, queda en el proyecto, y la nueva se arma limpia.
"""
import os
import sys
import time

sys.path.insert(0, 'D:/DAE/_repo/herramientas/prompts')
import movimiento_df as M                          # noqa: E402
import plan_camara_df as PC                        # noqa: E402
from armar_df import NOMBRE                        # noqa: E402

T0 = 86400
COMUNES = r'E:\DAE MASTER\00 COMUNES'
INTRO = os.path.join(COMUNES, 'INTRO', 'FGN_intro_version7.mp4')
MARCA = os.path.join(COMUNES, 'MARCA DE AGUA', 'MARCA_DE_AGUA_DAE_7s_fade.mov')
N_INTRO, N_BLANCO, N_RESPIRO, N_MARCA = 182, 119, 48, 168

PISTAS_V = ((1, 'VIDEO'), (2, 'MOVIMIENTO'), (3, 'CARTONES'), (4, 'APOYO'),
            (5, 'MARCA DE AGUA'), (6, 'EFECTOS'), (7, 'LOWER THIRD'))
PISTAS_A = ((1, 'NARRADOR'), (2, 'PREGUNTAS'), (3, 'DIALOGO'),
            (4, 'AMBIENTE'), (5, 'MUSICA'))
PISTA_MUSICA = 5

# El lower third entra 14 cuadros despues de que abre su ranura, y dura 120.
LT_OFF, LT_LARGO = 14, 120
LOWERS = {
    1: {1: 'DF_C1_lt01_lugar.mov', 2: 'DF_C1_lt02_miriam.mov',
        11: 'DF_C1_lt03_gregoria.mov'},
    2: {1: 'DF_C2_lt01_rosaelena.mov', 2: 'DF_C2_lt02_mariana.mov'},
    3: {5: 'DF_C3_lt01_fiscal.mov'},
    4: {1: 'DF_C4_lt01_rosaelena.mov', 4: 'DF_C4_lt02_fiscal.mov'},
    5: {8: 'DF_C5_lt01_perito.mov', 10: 'DF_C5_lt02_analista.mov'},
}


def plan(cap, cartones):
    """(v1, v2, v3, v5, v7, voz, musica, ini_cuerpo, dur_cuerpo, total).

    `cartones` es la lista del proponedor: cada uno con su `ini` absoluto en
    cuadros de la pieza y su `cuadros`.
    """
    E = __import__('escenas_df_c%d' % cap)
    base = os.path.join(PC.RAIZ, PC.CAPS[cap])
    tl = os.path.join(base, '10 TIMELINE SEBASTIAN')
    cart = os.path.join(base, '02 CARTONES')
    lt = os.path.join(cart, 'LOWER THIRDS')
    cpieza = os.path.join(cart, 'PIEZA')

    v1, v2, v7, t = [], [], [], 0
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'DF_C%d_carton_entrada.mov' % cap)))
    t += N_BLANCO
    ini = t
    for n in sorted(E.R):
        largo = E.R[n][0]
        nm = 'DF_C%d_r%02d_%s' % (cap, n, NOMBRE[cap][n])
        v1.append((t, largo, os.path.join(tl, 'RANURAS', '%s_v%d.mp4' % (nm, largo))))
        if (cap, n) in M.MOV:
            v2.append((t, largo, os.path.join(tl, 'MOVIMIENTO',
                                              '%s_mov_v%d.mp4' % (nm, largo))))
        if n in LOWERS.get(cap, {}):
            v7.append((t + LT_OFF, LT_LARGO,
                       os.path.join(lt, LOWERS[cap][n])))
        t += largo
    fin = t
    v1.append((t, N_RESPIRO, os.path.join(tl, 'RESPIRO',
                                          'DF_C%d_respiro_v%d.mp4' % (cap, N_RESPIRO))))
    t += N_RESPIRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'DF_C%d_carton_cierre.mov' % cap)))
    t += N_BLANCO
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO

    v3 = [(c['ini'], c['cuadros'], os.path.join(cpieza, c['archivo']))
          for c in cartones if c['cap'] == cap]
    v5 = [(ini, N_MARCA, MARCA), (fin - N_MARCA, N_MARCA, MARCA)]
    voz = os.path.join(base, '03 VOCES', 'DF_C%d_NARRADOR.wav' % cap)
    musica = os.path.join(base, '08 MUSICA', 'DF_C%d_MUSICA_cama.wav' % cap)
    return v1, v2, v3, v5, v7, voz, musica, ini, fin - ini, t


def huecos(tl, pista=1):
    """Todo hueco que quede en una pista. Un solo cuadro ya es un parpadeo."""
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


def construye(resolve, cap, nombre_linea, cartones, sufijo_viejo='anterior'):
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()

    # Una linea con clips no se borra: se aparta con otro nombre.
    # La lista se toma de una vez: renombrar y borrar mueve los indices,
    # y GetTimelineByIndex devuelve None a mitad del recorrido.
    existentes = [pr.GetTimelineByIndex(i)
                  for i in range(1, int(pr.GetTimelineCount()) + 1)]
    for t in [x for x in existentes if x is not None]:
        if t.GetName() != nombre_linea:
            continue
        if t.GetItemListInTrack('video', 1):
            k, nuevo = 1, '%s (%s)' % (nombre_linea, sufijo_viejo)
            nombres = {pr.GetTimelineByIndex(j).GetName()
                       for j in range(1, int(pr.GetTimelineCount()) + 1)}
            while nuevo in nombres:
                k += 1
                nuevo = '%s (%s %d)' % (nombre_linea, sufijo_viejo, k)
            t.SetName(nuevo)
        else:
            mp.DeleteTimelines([t])

    v1, v2, v3, v5, v7, voz, musica, ini, dur_cuerpo, tot = plan(cap, cartones)
    todos = [p for _, _, p in v1 + v2 + v3 + v5 + v7] + [voz, musica]
    falta = sorted({p for p in todos if not os.path.exists(p)})
    if falta:
        return None, 'faltan en disco: %s' % falta[:4]

    raiz = mp.GetRootFolder()
    carp = None
    for f in raiz.GetSubFolderList():
        if f.GetName() == nombre_linea:
            carp = f
    if carp is None:
        carp = mp.AddSubFolder(raiz, nombre_linea)
    mp.SetCurrentFolder(carp)

    #  SE VACIA EL BIN ANTES DE IMPORTAR, Y NO ES POR ORDEN
    #      Las ranuras se rehornearon CON EL MISMO NOMBRE DE ARCHIVO. Resolve
    #      guarda la media decodificada del item del pool, asi que un item
    #      viejo sigue sirviendo los cuadros viejos -con el zoom- aunque el
    #      archivo en disco ya sea otro. Y como el archivo ya esta en el
    #      proyecto, ImportMedia lo salta y ni siquiera aparece en este bin:
    #      asi fue como el capitulo 2 fallo con 'no quedo en el pool'.
    #
    #      Vaciar el bin y volver a importar fuerza la lectura de disco. La
    #      linea anterior queda offline, que es honesto: su media ya no existe
    #      con ese contenido. En disco no se borra nada.
    #      Y se busca en TODO el pool, no solo en este bin: una copia vieja
    #      en otra carpeta hace que ImportMedia salte el archivo y entonces
    #      no aparece aqui -asi fallaron el capitulo 2 y el 3-.
    quiero = {os.path.basename(x) for x in todos}

    def _todos_los_clips(f):
        for c in f.GetClipList():
            yield c
        for sf in f.GetSubFolderList():
            for c in _todos_los_clips(sf):
                yield c

    viejos = [c for c in _todos_los_clips(raiz)
              if os.path.basename(
                  (c.GetClipProperty('File Path') or '').replace('/', os.sep))
              in quiero]
    if viejos:
        mp.DeleteClips(viejos)
    mp.SetCurrentFolder(carp)

    #  IMPORTMEDIA PIERDE ARCHIVOS CUANDO SE LE PASA LA LISTA ENTERA
    #      27 de octubre: con 26 rutas de una vez se quedaron fuera una cada
    #      vez -el capitulo 3 fallo primero en r05 y despues en r08-, sin
    #      error y sin aviso. El mismo archivo importado solo entra bien.
    #      Entonces se importa y se COMPRUEBA, y lo que falte se reintenta
    #      uno por uno. Un valor de retorno no es una comprobacion.
    def _en_el_bin():
        return {os.path.basename(
            (c.GetClipProperty('File Path') or '').replace('/', os.sep))
            for c in carp.GetClipList()}

    pedidos = sorted(set(todos))
    mp.ImportMedia(pedidos)
    #      Y hay que DARLE UN RESPIRO entre intentos: reintentar al toque
    #      falla igual, y el mismo archivo entra solo con esperar medio
    #      segundo. Es tiempo, no el archivo.
    for _ in range(6):
        hay = _en_el_bin()
        faltan = [x for x in pedidos if os.path.basename(x) not in hay]
        if not faltan:
            break
        time.sleep(0.7)
        for x in faltan:
            mp.ImportMedia([x])
            time.sleep(0.15)
    hay = _en_el_bin()
    faltan = [x for x in pedidos if os.path.basename(x) not in hay]
    if faltan:
        return None, 'no entraron al pool ni uno por uno: %s' % faltan[:3]

    # por NOMBRE DE ARCHIVO: RAIZ usa barras normales y os.path.join las
    # invertidas, asi que la ruta que arma este script y la que Resolve
    # devuelve en 'File Path' no son la misma cadena.
    pool = {}
    for it in carp.GetClipList():
        pool[os.path.basename(
            it.GetClipProperty('File Path').replace('/', os.sep))] = it

    tl = mp.CreateEmptyTimeline(nombre_linea)
    pr.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < len(PISTAS_V):
        tl.AddTrack('video')
    while tl.GetTrackCount('audio') < len(PISTAS_A):
        tl.AddTrack('audio', 'stereo')
    for i, n in PISTAS_V:
        tl.SetTrackName('video', i, n)
    for i, n in PISTAS_A:
        tl.SetTrackName('audio', i, n)

    for lista, pista in ((v1, 1), (v2, 2), (v3, 3), (v5, 5), (v7, 7)):
        if not lista:
            continue
        items = []
        for pos, largo, p in lista:
            it = pool.get(os.path.basename(p))
            if it is None:
                return None, 'no quedo en el pool: %s' % p
            # endFrame NO es inclusivo: la duracion es endFrame - startFrame.
            items.append({'mediaPoolItem': it, 'startFrame': 0,
                          'endFrame': largo, 'trackIndex': pista,
                          'recordFrame': T0 + pos, 'mediaType': 1})
        mp.AppendToTimeline(items)

    for p, largo, pos, pista in ((voz, dur_cuerpo, ini, 1),
                                 (musica, tot, 0, PISTA_MUSICA)):
        it = pool.get(os.path.basename(p))
        if it is None:
            return None, 'no quedo en el pool: %s' % p
        mp.AppendToTimeline([{'mediaPoolItem': it, 'startFrame': 0,
                              'endFrame': largo, 'trackIndex': pista,
                              'recordFrame': T0 + pos, 'mediaType': 2}])

    h = huecos(tl)
    if h:
        return tl, 'QUEDARON HUECOS en V1: %s' % h[:6]
    largo_real = tl.GetEndFrame() - tl.GetStartFrame()
    if largo_real != tot:
        return tl, 'la linea mide %d y el plan pedia %d' % (largo_real, tot)
    return tl, None
