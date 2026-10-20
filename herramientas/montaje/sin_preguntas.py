#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las seis piezas sin el bloque de preguntas, con intro y outro cortados al
blanco y la marca de agua en dos apariciones de 7 s.

    python sin_preguntas.py medios            importa los tres medios nuevos
    python sin_preguntas.py montar [COD ...]  arma las lineas nuevas
    python sin_preguntas.py chequeo [COD ...] el chequeo de siete puntos
    python sin_preguntas.py borrar [COD ...]  borra las lineas nuevas

LOS TRES CAMBIOS

1. EL INTRO Y EL OUTRO SE CORTAN DONDE EL CLIP LLEGA A BLANCO
   `FGN_intro_version7.mp4` dura 222 cuadros y se venia usando entero. Medido
   cuadro a cuadro a 320x180, contando pixeles que se apartan del maximo:

       160-169   9,1 % de pixeles no blancos   el bloque DAE | FISCALIA, quieto
       170-171   8,7 % y 7,4 %                 los logos empiezan a salir
       172       0,6 %                         ya casi no queda nada
       173-181   0,135 % bajando a 0,012 %     el filete y los bordes suavizados
       182       0,000 %                       BLANCO LIMPIO
       182-208   0,000 %                       27 cuadros de blanco muerto
       209       98,4 %                        corte duro a otra toma del edificio

   El corte va en 182: es el primer cuadro completamente blanco. Los 27 de
   blanco muerto y la toma extra de 13 cuadros se quedan afuera. El audio del
   intro ya esta en silencio absoluto desde el cuadro 168, asi que el corte no
   parte ningun sonido.

   Empalma mejor que antes: el carton de entrada y el de cierre son blancos,
   asi que el blanco del intro entra al carton sin cambio de fondo.

2. EL BLOQUE DE PREGUNTAS SALE ENTERO
   `p1a_votacion`, `p1b_opciones` y `p2_foro` en V3, y el lecho que corria
   debajo en V1. Ese bloque no lleva narracion -A2 termina exactamente donde
   empieza el lecho-, asi que quitarlo no corta ni una palabra. Las preguntas
   viven ahora en la implementacion web.

   NO sale la grafica de cierre de cada caso -`ae*_pregunta`, `ae16b_categoria`,
   el mapa de Colombia, el taller vacio-: esas SI van narradas y son el ultimo
   golpe del caso, no el bloque interactivo. Se quedan.

3. LA MARCA DE AGUA, DOS VECES SIETE SEGUNDOS
   Venia cubriendo la pieza entera. Ahora entra de golpe donde entraba -apenas
   termina el carton de entrada- 168 cuadros, y se desvanece en 24. Reaparece
   168 cuadros antes del carton de cierre y se va cuando el carton entra. El
   carton de entrada, el de cierre y el outro ya traen el logo impreso, asi que
   la pieza nunca se queda sin marca en sus extremos.

EL RESPIRO
   Sin el bloque de preguntas la narracion callaba y entraba el carton de
   cierre de una. Se sostiene la ultima toma 48 cuadros -2 segundos- antes del
   carton, y la musica resuelve ahi. Es un congelado del ultimo cuadro de esa
   toma, medido: difiere de la fuente en 1 o 2 niveles de 255.

LA EXCEPCION DE P3C1
   En P3C1 la ultima toma es el mapa de Colombia, y la etiqueta «Cucuta» cae
   justo en la esquina donde va la marca de agua -comprobado componiendo las dos
   a 1:1-. Por eso la segunda aparicion termina donde EMPIEZA el mapa, no donde
   empieza el carton de cierre. La linea actual ya hacia esto: su marca de agua
   se interrumpia en el mapa y volvia en el lecho.

POR QUE SE RECONSTRUYE Y NO SE EDITA
   P3C1 lo ajusto Sebastian a mano -V2 tiene 38 clips, varios partidos en
   pedazos de nueve cuadros- y eso no se puede perder. Asi que la linea nueva
   no se arma desde una receta: se COPIA clip por clip de la vieja, con su mismo
   punto de entrada y su misma duracion, corridos a la posicion nueva. Se
   comprobo antes que ninguno de los 334 clips de video de las seis lineas lleva
   transformacion, recorte ni opacidad hechos dentro de Resolve -todo esta
   horneado en los archivos-, asi que reubicar no pierde nada.
"""
import os
import sys

import bins

T0 = 86400
N_INTRO_VIEJO = 222
N_INTRO = 182            # medido: primer cuadro de blanco limpio
D = N_INTRO_VIEJO - N_INTRO                     # 40
N_BLANCO = 119           # carton de entrada y de cierre
N_RESPIRO = 48           # 2 s
N_MARCA = 168            # 7 s a 23,976

COMUNES = 'E:/DAE MASTER/00 COMUNES'
MARCA7 = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_7s_fade.mov'

B5 = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/UNIDAD '
P3 = 'E:/DAE MASTER/PRIORIDAD 03/CASO 0'

# musica_hasta: donde termina la cama. El Curso 5 la corta en el carton de
# cierre; PRIORIDAD 03 la lleva a traves del carton hasta el outro. Se respeta
# la convencion de cada curso en vez de unificarla.
CASOS = [
    dict(cod='C5U1',
         vieja='C5U1 LOGISTICA CMR - a la voz',
         nueva='C5U1 LOGISTICA CMR - SIN PREGUNTAS',
         bin=['C5 BIENES EN EL PROCESO PENAL', 'U1',
              'CASO 01 - logistica CMR del norte'],
         carpeta=B5 + '1/CASO 01 - logistica CMR del norte',
         musica_sub='08 MUSICA', musica_hasta='cierre', marca2=None),
    dict(cod='C5U2',
         vieja='C5U2 SINIESTRO VIAL - a la voz v2',
         nueva='C5U2 SINIESTRO VIAL - SIN PREGUNTAS',
         bin=['C5 BIENES EN EL PROCESO PENAL', 'U2',
              'CASO 02 - el siniestro vial'],
         carpeta=B5 + '2/CASO 02 - el siniestro vial',
         musica_sub='06 AUDIO', musica_hasta='cierre', marca2=None),
    dict(cod='C5U3',
         vieja='C5U3 ESLABON FINANCIERO - a la voz v2',
         nueva='C5U3 ESLABON FINANCIERO - SIN PREGUNTAS',
         bin=['C5 BIENES EN EL PROCESO PENAL', 'U3',
              'CASO 03 - eslabon financiero'],
         carpeta=B5 + '3/CASO 03 - eslabon financiero',
         musica_sub='06 AUDIO', musica_hasta='cierre', marca2=None),
    dict(cod='C5U4',
         vieja='C5U4 LOS ILUSTRES - a la voz',
         nueva='C5U4 LOS ILUSTRES - SIN PREGUNTAS',
         bin=['C5 BIENES EN EL PROCESO PENAL', 'U4',
              'CASO 04 - los ilustres'],
         carpeta=B5 + '4/CASO 04 - los ilustres',
         musica_sub='06 AUDIO', musica_hasta='cierre', marca2=None),
    dict(cod='P3C1',
         vieja='P3C1 EL HOSPEDAJE EL MIRADOR - a la voz v1',
         nueva='P3C1 EL HOSPEDAJE EL MIRADOR - SIN PREGUNTAS',
         bin=['PRIORIDAD 03', 'CASO 01 - El hospedaje El Mirador'],
         carpeta=P3 + '1 - El hospedaje El Mirador',
         musica_sub='08 MUSICA', musica_hasta='outro',
         marca2='antes_de_la_ultima_toma'),
    dict(cod='P3C2',
         vieja='P3C2 EL TALLER DEL SEGUNDO PISO - a la voz v1',
         nueva='P3C2 EL TALLER DEL SEGUNDO PISO - SIN PREGUNTAS',
         bin=['PRIORIDAD 03', 'CASO 02 - El taller del segundo piso'],
         carpeta=P3 + '2 - El taller del segundo piso',
         musica_sub='08 MUSICA', musica_hasta='outro', marca2=None,
         # Revision de Sebastian del 20 de octubre. La linea nueva ya no
         # tiene el mismo numero de clips que la vieja, y eso es correcto:
         #   V1 +1  r02 se parte en r02a fachada y r02b Saul en su oficina
         #   V2 +2  Sebastian parte r19_idle en 2 y r23_idle en 3 (+3), y
         #          sale r24_idle_mensajes, el clip del telefono con dedos
         #          que estaba fallado (-1)
         #   V3 +1  lt05_elisa pasa de V7 a V3, retimado a 3587
         #   V4 +1  el parche de Sebastian sobre la palabra ELISA horneada
         #          en r18_idle (96x54 px en 609..705, 235..289)
         #   V7 -1  el mismo lt05_elisa que se fue a V3
         revisiones={'V1': 1, 'V2': 2, 'V3': 1, 'V4': 1, 'V7': -1}),
]

PREGUNTAS = ('_p1a_', '_p1b_', '_p2_')


def _handles():
    import DaVinciResolveScript as dvr
    r = dvr.scriptapp('Resolve')
    pr = r.GetProjectManager().GetCurrentProject()
    return r, pr, pr.GetMediaPool()


def _linea(pr, nombre):
    for i in range(pr.GetTimelineCount()):
        t = pr.GetTimelineByIndex(i + 1)
        if t.GetName() == nombre:
            return t
    return None


def _respiro(c):
    return c['carpeta'] + '/10 TIMELINE SEBASTIAN/RESPIRO/%s_respiro_v48.mp4' % c['cod']


def _musica(c):
    return c['carpeta'] + '/' + c['musica_sub'] + '/%s_MUSICA_v2.wav' % c['cod']


def _es_preguntas(nombre):
    n = nombre.lower()
    return ('lecho' in n) or any(p in n for p in PREGUNTAS)


# ------------------------------------------------------------------ medios

def medios(mp):
    for c in CASOS:
        print(c['cod'])
        raiz = bins.carpeta(mp, c['bin'])
        subs = {s.GetName(): s for s in raiz.GetSubFolderList()}
        ya = bins.clips(mp, c['bin'])
        for ruta, sub in ((MARCA7, 'COMUNES'),
                          (_respiro(c), 'RANURAS'),
                          (_musica(c), 'MUSICA')):
            base = os.path.basename(ruta)
            if not os.path.exists(ruta):
                raise RuntimeError('no esta en disco: %s' % ruta)
            if base in ya:
                print('   ya estaba  %s' % base)
                continue
            mp.SetCurrentFolder(subs.get(sub, raiz))
            mp.ImportMedia([ruta])
            print('   importado  %-40s -> %s' % (base, sub))
        hay = bins.clips(mp, c['bin'])
        faltan = [os.path.basename(r) for r in
                  (MARCA7, _respiro(c), _musica(c))
                  if os.path.basename(r) not in hay]
        if faltan:
            raise RuntimeError('%s no entraron: %s' % (c['cod'], faltan))


# ------------------------------------------------------------------ lectura

def leer(tl):
    """Todo lo que hay en la linea, por pista, en coordenadas relativas."""
    t0 = int(tl.GetStartFrame())
    d = {'t0': t0, 'fin': int(tl.GetEndFrame()) - t0,
         'pistas_v': tl.GetTrackCount('video'),
         'pistas_a': tl.GetTrackCount('audio'),
         'nombres_v': [], 'nombres_a': [], 'v': {}, 'a': {}}
    for tipo, clave, nom in (('video', 'v', 'nombres_v'),
                             ('audio', 'a', 'nombres_a')):
        for k in range(1, tl.GetTrackCount(tipo) + 1):
            d[nom].append(tl.GetTrackName(tipo, k))
            it = []
            for x in (tl.GetItemListInTrack(tipo, k) or []):
                # Un generador de Resolve -un Solid Color, por ejemplo- no
                # tiene medio en el pool, y eso NO es un error: el parche de
                # Elisa que Sebastian puso en V4 del Caso 2 es exactamente
                # eso. El lector lo lee como cualquier otro clip. Lo unico
                # que no se puede hacer con el es recolocarlo con
                # AppendToTimeline, y de eso se queja `montar` cuando le
                # toca mover uno, que es donde el fallo significa algo.
                mpi = x.GetMediaPoolItem()
                it.append({'mpi': mpi, 'nom': x.GetName(),
                           'generador': mpi is None,
                           'ini': int(x.GetStart()) - t0,
                           'fin': int(x.GetEnd()) - t0,
                           'off': int(x.GetLeftOffset() or 0),
                           'dur': int(x.GetDuration() or
                                      (int(x.GetEnd()) - int(x.GetStart())))})
            d[clave][k] = it
    return d


def planta(d, c):
    """Las posiciones nuevas, calculadas de la lectura de la linea vieja."""
    nar = d['a'].get(2) or []
    if len(nar) != 1:
        raise RuntimeError('A2 NARRADOR deberia tener un clip, tiene %d' % len(nar))
    caso_fin = nar[0]['fin']

    v1 = d['v'][1]
    intro = v1[0]
    if intro['ini'] != 0 or intro['dur'] != N_INTRO_VIEJO:
        raise RuntimeError('el intro no es 0..%d: %r' % (N_INTRO_VIEJO, intro))
    lecho = [x for x in v1 if x['ini'] == caso_fin]
    if len(lecho) != 1 or 'lecho' not in lecho[0]['nom'].lower():
        raise RuntimeError('no encuentro el lecho en %d: %r' % (caso_fin, lecho))
    lecho = lecho[0]
    bed_fin = lecho['fin']
    cierre = [x for x in v1 if x['ini'] == bed_fin]
    if len(cierre) != 1 or 'carton_cierre' not in cierre[0]['nom']:
        raise RuntimeError('no encuentro el carton de cierre en %d' % bed_fin)
    cierre = cierre[0]
    outro = v1[-1]
    if outro['ini'] != cierre['fin'] or outro['dur'] != N_INTRO_VIEJO:
        raise RuntimeError('el outro no cuadra: %r' % outro)

    # la ultima toma del caso, la que se congela para el respiro
    previas = [x for x in v1 if x['ini'] < caso_fin]
    ultima = previas[-1]

    p = {'caso_fin': caso_fin, 'bed_fin': bed_fin,
         'intro': intro, 'lecho': lecho, 'cierre': cierre, 'outro': outro,
         'ultima': ultima,
         'off_entrada': N_INTRO,
         'off_ranuras': N_INTRO + N_BLANCO,
         'off_respiro': caso_fin - D,
         'off_cierre': caso_fin - D + N_RESPIRO,
         'off_outro': caso_fin - D + N_RESPIRO + N_BLANCO}
    p['fin'] = p['off_outro'] + N_INTRO
    p['marca1'] = p['off_ranuras']
    if c['marca2'] == 'antes_de_la_ultima_toma':
        p['marca2'] = (ultima['ini'] - D) - N_MARCA
    else:
        p['marca2'] = p['off_cierre'] - N_MARCA
    p['musica_fin'] = p['off_cierre'] if c['musica_hasta'] == 'cierre' else p['off_outro']
    p['musica_dur'] = p['musica_fin'] - p['off_entrada']
    if p['marca2'] < p['marca1'] + N_MARCA:
        raise RuntimeError('las dos marcas se tocan')
    return p


def _mover(x, pista):
    """El medio con el que se recoloca un clip, o un fallo que se entiende."""
    if x['mpi'] is None:
        raise RuntimeError(
            'no puedo recolocar un generador sin medio en %s: %s. '
            'Hay que rehacerlo a mano en la linea nueva.' % (pista, x['nom']))
    return x['mpi']


def nueva_pos(x, p, pista_v):
    """Donde va este clip en la linea nueva, o None si se cae."""
    if pista_v == 1:
        if x is p['intro']:
            return (0, 0, N_INTRO)
        if x is p['outro']:
            return (p['off_outro'], 0, N_INTRO)
        if x is p['cierre']:
            return (p['off_cierre'], x['off'], x['dur'])
        if x is p['lecho']:
            return None
    if _es_preguntas(x['nom']):
        return None
    if x['ini'] >= p['caso_fin']:
        raise RuntimeError('clip inesperado despues del caso: %r' % x['nom'])
    if x['fin'] > p['caso_fin']:
        raise RuntimeError('clip que cruza el final del caso: %r' % x['nom'])
    return (x['ini'] - D, x['off'], x['dur'])


# ------------------------------------------------------------------ montaje

def montar(pr, mp, cods):
    for c in CASOS:
        if cods and c['cod'] not in cods:
            continue
        print('')
        print('=== %s ===' % c['cod'])
        vieja = _linea(pr, c['vieja'])
        if vieja is None:
            raise RuntimeError('no encuentro %r' % c['vieja'])
        if _linea(pr, c['nueva']) is not None:
            print('   la linea nueva ya existe, no se toca')
            continue
        d = leer(vieja)
        p = planta(d, c)
        IT = bins.clips(mp, c['bin'])
        print('   caso termina en %d -> %d; fin %d -> %d (%+d)'
              % (p['caso_fin'], p['caso_fin'] - D, d['fin'], p['fin'],
                 p['fin'] - d['fin']))

        mp.SetCurrentFolder(bins.carpeta(mp, c['bin'], crear_subbins=False))
        tl = mp.CreateEmptyTimeline(c['nueva'])
        while tl.GetTrackCount('video') < d['pistas_v']:
            tl.AddTrack('video')
        while tl.GetTrackCount('audio') < d['pistas_a']:
            tl.AddTrack('audio', 'stereo')
        for i, n in enumerate(d['nombres_v']):
            tl.SetTrackName('video', i + 1, n)
        for i, n in enumerate(d['nombres_a']):
            tl.SetTrackName('audio', i + 1, n)
        pr.SetCurrentTimeline(tl)

        caidos = []
        # --- V1 primero: su intro y su outro arrastran el audio a A1
        lote = []
        for x in d['v'][1]:
            n = nueva_pos(x, p, 1)
            if n is None:
                caidos.append(('V1', x['nom']))
                continue
            rec, off, dur = n
            lote.append({'mediaPoolItem': _mover(x, 'V1'), 'startFrame': off,
                         'endFrame': off + dur, 'trackIndex': 1,
                         'recordFrame': T0 + rec})
        lote.append({'mediaPoolItem': IT['%s_respiro_v48.mp4' % c['cod']],
                     'startFrame': 0, 'endFrame': N_RESPIRO, 'trackIndex': 1,
                     'recordFrame': T0 + p['off_respiro']})
        lote.sort(key=lambda z: z['recordFrame'])
        if not mp.AppendToTimeline(lote):
            raise RuntimeError('fallo el volcado de V1')

        # --- el resto de las pistas de video
        for k in range(2, d['pistas_v'] + 1):
            nombre = d['nombres_v'][k - 1]
            if nombre == 'MARCA DE AGUA':
                for x in d['v'][k]:
                    caidos.append(('V%d' % k, x['nom']))
                lote = [{'mediaPoolItem': IT[os.path.basename(MARCA7)],
                         'startFrame': 0, 'endFrame': N_MARCA, 'trackIndex': k,
                         'recordFrame': T0 + pos}
                        for pos in (p['marca1'], p['marca2'])]
                if lote and not mp.AppendToTimeline(lote):
                    raise RuntimeError('fallo la marca de agua')
                continue
            lote = []
            for x in d['v'][k]:
                n = nueva_pos(x, p, k)
                if n is None:
                    caidos.append(('V%d' % k, x['nom']))
                    continue
                rec, off, dur = n
                lote.append({'mediaPoolItem': _mover(x, 'V%d' % k), 'startFrame': off,
                             'endFrame': off + dur, 'trackIndex': k,
                             'recordFrame': T0 + rec})
            if lote:
                lote.sort(key=lambda z: z['recordFrame'])
                if not mp.AppendToTimeline(lote):
                    raise RuntimeError('fallo el volcado de V%d' % k)

        # --- audio: A1 ya vino enganchado al intro y al outro
        for k in range(2, d['pistas_a'] + 1):
            nombre = d['nombres_a'][k - 1]
            if nombre == 'MUSICA':
                for x in d['a'][k]:
                    caidos.append(('A%d' % k, x['nom']))
                lote = [{'mediaPoolItem': IT['%s_MUSICA_v2.wav' % c['cod']],
                         'startFrame': 0, 'endFrame': p['musica_dur'],
                         'trackIndex': k, 'mediaType': 2,
                         'recordFrame': T0 + p['off_entrada']}]
                if not mp.AppendToTimeline(lote):
                    raise RuntimeError('fallo la musica')
                continue
            lote = []
            for x in d['a'][k]:
                n = nueva_pos(x, p, 0)
                if n is None:
                    caidos.append(('A%d' % k, x['nom']))
                    continue
                rec, off, dur = n
                lote.append({'mediaPoolItem': _mover(x, 'A%d' % k), 'startFrame': off,
                             'endFrame': off + dur, 'trackIndex': k,
                             'mediaType': 2, 'recordFrame': T0 + rec})
            if lote:
                lote.sort(key=lambda z: z['recordFrame'])
                if not mp.AppendToTimeline(lote):
                    raise RuntimeError('fallo el volcado de A%d' % k)

        print('   cayeron %d clips:' % len(caidos))
        for pista, nom in caidos:
            print('      %-4s %s' % (pista, nom))


# ------------------------------------------------------------------ chequeo

def chequeo(pr, mp, cods):
    malos = 0
    for c in CASOS:
        if cods and c['cod'] not in cods:
            continue
        print('')
        print('=== %s ===' % c['cod'])
        vieja = _linea(pr, c['vieja'])
        nueva = _linea(pr, c['nueva'])
        if nueva is None:
            print('   FALLO no existe la linea nueva')
            malos += 1
            continue
        vi = leer(vieja)
        p = planta(vi, c)
        n = leer(nueva)
        fallos = []

        # 1 V1 sin encabalgamientos, con el final calculado, y con los MISMOS
        #   huecos que traia la linea vieja. P3C1 trae uno: Sebastian dejo 147
        #   cuadros de V1 vacios en el bloque de Paula y los tapo con el clip
        #   de movimiento de V2. Un hueco heredado y tapado esta bien; uno
        #   nuevo, o uno que se quede sin tapa, no.
        def _huecos(d):
            g, pos = [], 0
            for x in d['v'][1]:
                if x['ini'] > pos:
                    g.append((pos, x['ini']))
                pos = max(pos, x['fin'])
            return g, pos

        v1 = n['v'][1]
        pos = 0
        for x in v1:
            if x['ini'] < pos:
                fallos.append('V1 encabalgado en %d' % x['ini'])
            pos = max(pos, x['fin'])
        g_nuevos, pos = _huecos(n)
        g_viejos, _ = _huecos(vi)
        heredados = set((a - D, b - D) for a, b in g_viejos)
        for a, b in g_nuevos:
            if (a, b) not in heredados:
                fallos.append('V1 hueco nuevo en %d..%d' % (a, b))
                continue
            tapa = [x for k in range(2, n['pistas_v'] + 1)
                    for x in n['v'].get(k, [])
                    if n['nombres_v'][k - 1] != 'MARCA DE AGUA'
                    and x['ini'] <= a and x['fin'] >= b]
            if not tapa:
                fallos.append('V1 hueco %d..%d sin tapar: sale negro' % (a, b))
            else:
                print('   aviso: hueco heredado %d..%d (%d cuadros), tapado por %s'
                      % (a, b, b - a, tapa[0]['nom']))
        if pos != p['fin']:
            fallos.append('V1 termina en %d, esperado %d' % (pos, p['fin']))
        if n['fin'] != p['fin']:
            fallos.append('la linea mide %d, esperado %d' % (n['fin'], p['fin']))
        print('1) V1 %d clips, termina en %d, %d hueco(s) heredado(s)'
              % (len(v1), pos, len(g_nuevos)))

        # 2 intro y outro de 182
        if v1[0]['dur'] != N_INTRO:
            fallos.append('el intro mide %d' % v1[0]['dur'])
        if v1[-1]['dur'] != N_INTRO:
            fallos.append('el outro mide %d' % v1[-1]['dur'])
        print('2) intro %d, outro %d' % (v1[0]['dur'], v1[-1]['dur']))

        # 3 ni rastro del bloque de preguntas
        rastro = []
        for clave in ('v', 'a'):
            for k, its in n[clave].items():
                for x in its:
                    if _es_preguntas(x['nom']):
                        rastro.append('%s%d %s' % (clave.upper(), k, x['nom']))
        if rastro:
            fallos.append('queda bloque de preguntas: %s' % rastro)
        print('3) bloque de preguntas: %s' % (rastro or 'no queda nada'))

        # 4 el respiro
        resp = [x for x in v1 if 'respiro' in x['nom']]
        if len(resp) != 1 or resp[0]['dur'] != N_RESPIRO \
                or resp[0]['ini'] != p['off_respiro']:
            fallos.append('el respiro no esta en %d x%d: %r'
                          % (p['off_respiro'], N_RESPIRO, resp))
        print('4) respiro %d..%d' % (resp[0]['ini'], resp[0]['fin']) if resp
              else '4) respiro FALTA')

        # 5 la marca de agua, dos tramos de 168
        km = n['nombres_v'].index('MARCA DE AGUA') + 1
        ma = n['v'][km]
        esp = [(p['marca1'], p['marca1'] + N_MARCA),
               (p['marca2'], p['marca2'] + N_MARCA)]
        hay = [(x['ini'], x['fin']) for x in ma]
        if hay != esp:
            fallos.append('marca de agua %r, esperado %r' % (hay, esp))
        print('5) marca de agua %r' % (hay,))

        # 6 la musica
        ka = n['nombres_a'].index('MUSICA') + 1
        mu = n['a'][ka]
        if len(mu) != 1 or mu[0]['ini'] != p['off_entrada'] \
                or mu[0]['fin'] != p['musica_fin']:
            fallos.append('la musica no va de %d a %d: %r'
                          % (p['off_entrada'], p['musica_fin'],
                             [(x['ini'], x['fin']) for x in mu]))
        print('6) musica %d..%d (esperado %d..%d)'
              % (mu[0]['ini'], mu[0]['fin'], p['off_entrada'], p['musica_fin'])
              if mu else '6) musica FALTA')

        # 7 no se perdio ni un clip que debia quedarse
        for clave in ('v', 'a'):
            # Una pista puede existir solo en la linea nueva -V4 APOYO del
            # Caso 2 nacio con el parche de Elisa-, asi que se recorren las
            # dos y la que falta cuenta cero.
            for k in sorted(set(vi[clave]) | set(n[clave])):
                its = vi[clave].get(k, [])
                if clave == 'a' and k == 1:
                    continue
                nombres = (vi['nombres_v'] if clave == 'v'
                           else vi['nombres_a'])
                if k > len(nombres):
                    nombres = (n['nombres_v'] if clave == 'v'
                               else n['nombres_a'])
                nom_pista = nombres[k - 1]
                if nom_pista in ('MARCA DE AGUA', 'MUSICA'):
                    continue
                deben = len([x for x in its if not _es_preguntas(x['nom'])])
                tiene = len([x for x in n[clave].get(k, [])
                             if 'respiro' not in x['nom']])
                # Una linea ya entregada se sigue editando: una revision
                # anade, quita o parte clips a proposito. Esos cambios se
                # declaran en `revisiones` del caso -con su motivo escrito
                # al lado- y el conteo los da por buenos. Lo que el punto 7
                # sigue cazando es el clip que se pierde sin que nadie lo
                # haya decidido, que es para lo que se escribio.
                esp = deben + c.get('revisiones', {}).get(
                    '%s%d' % (clave.upper(), k), 0)
                if esp != tiene:
                    fallos.append('%s%d esperaba %d clips utiles y quedaron %d'
                                  % (clave.upper(), k, esp, tiene))
        rev = c.get('revisiones', {})
        print('7) conteo de clips por pista: %s%s'
              % ('OK' if not [f for f in fallos if 'clips utiles' in f]
                 else 'revisar',
                 '  (revisiones declaradas: %s)' % rev if rev else ''))

        if fallos:
            malos += 1
            print('   FALLOS:')
            for f in fallos:
                print('      - %s' % f)
        else:
            print('   SIN FALLOS')
    print('')
    print('lineas con fallos: %d' % malos)
    return malos


def borrar(pr, mp, cods):
    for c in CASOS:
        if cods and c['cod'] not in cods:
            continue
        tl = _linea(pr, c['nueva'])
        if tl is None:
            print('%s: no hay linea nueva' % c['cod'])
            continue
        mp.SetCurrentFolder(bins.carpeta(mp, c['bin'], crear_subbins=False))
        print('%s borrada: %s' % (c['cod'], mp.DeleteTimelines([tl])))


if __name__ == '__main__':
    _r, _pr, _mp = _handles()
    _acc = sys.argv[1] if len(sys.argv) > 1 else 'chequeo'
    _cods = [a.upper() for a in sys.argv[2:]]
    if _acc == 'medios':
        medios(_mp)
    elif _acc == 'montar':
        montar(_pr, _mp, _cods)
    elif _acc == 'chequeo':
        sys.exit(1 if chequeo(_pr, _mp, _cods) else 0)
    elif _acc == 'borrar':
        borrar(_pr, _mp, _cods)
    else:
        print(__doc__)
