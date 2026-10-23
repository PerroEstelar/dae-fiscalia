#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del PRIORIDAD 03 · Caso 5 «Voces, registros y cuentas» — VERSION 2.

QUE CAMBIA, Y QUE NO
    NO cambia nada de lo que se oye ni de lo que se lee: la rejilla, la voz,
    la musica, los 17 cartones y los 5 lower thirds y sus posiciones son los
    mismos. Las 43 ranuras miden lo mismo.

    Cambia lo que se VE, bajo la BIBLIA_puesta_en_escena_P3: doce lugares en
    vez de tres, 19 ranuras con gente en vez de siete, TRES cenitales en vez
    de veintidos, tres primeros planos donde no habia ninguno, y tres
    registros de luz donde solo habia «flat even light».

    Y cinco ranuras llevan video generado con Seedance sobre el keyframe.


    python montar_p3c5.py medios     importa a la carpeta del caso
    python montar_p3c5.py linea      crea la linea con el mapa de pistas
    python montar_p3c5.py v1         intro + entrada + 43 ranuras + respiro
                                     + cierre + outro
    python montar_p3c5.py v3         los cartones tenidos y las dos citas
    python montar_p3c5.py v7         los cinco lower thirds
    python montar_p3c5.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_p3c5.py chequeo    el chequeo
    python montar_p3c5.py borrar     borra la linea para rehacerla entera

LA CUENTA, QUE TIENE QUE CUADRAR AL CUADRO
    intro 182 + entrada 119 + ranuras 8307 + respiro 48 + cierre 119
    + outro 182 = 8957 cuadros = 6:13,6 a 23,976.

NO HAY CAPA V2 EN ESTE MONTAJE, Y ESTA VEZ ES UNA DECISION
    En el Caso 4 no habia V2 porque la camara va horneada en el clip. Aqui
    tampoco la hay, pero ademas NO SE DIBUJAN graficos de movimiento, y no
    por falta de tiempo: el repertorio de la pieza ya absorbio los tres que
    tendrian sentido. La rima mayor r33/r35 es el grafico de «que quedo
    probado»; r39, los cuatro informes iguales, es el de «cuatro copias no
    son cuatro corroboraciones»; r01/r43, las dos bandejas, es el de
    «entra / queda». Dibujarlos encima seria decir dos veces lo mismo.

    El empuje de cada ranura esta asignado por lo que la placa significa
    -abre donde hay falta, cierra donde hay acumulacion-, y las rimas llevan
    el mismo empuje en sus dos mitades. Esta escrito en `plan_camara_p3c5.py`.

LAS NUEVE PROPUESTAS, Y SU CAMA
    Ninguna cae sobre una cara. Las siete placas con rostro son r03, r05,
    r21, r23, r27, r28 y r32; los cartones de propuesta van en r11, r19, r20,
    r24, r25, r31, r39, r40 y r41, que son banda, pluma, rollo, carpeta,
    patrones, puerta, hojas, sitio vacio y pago. Comprobado en el chequeo,
    paso 11.

LA RIMA MAYOR VA LIMPIA, Y EL CHEQUEO LO EXIGE
    r33 y r35 son el mismo encuadre con distinto contenido sobre la mesa. Si
    cae un carton sobre una de las dos, la diferencia que el espectador ve ya
    no es la del caso: es la del grafico. El carton del acta va en r34, que es
    justo el plano de en medio. Comprobado en el chequeo, paso 12.

Y LAS CUATRO RIMAS SE MIDEN, NO SE SUPONEN
    El paso 13 compara el plano de fondo y la saturacion de las dos mitades de
    cada rima sobre la placa ya graduada. Existe porque dos rimas de este caso
    -r33/r35 y r01/r43- llegaron rotas hasta el master sin que ningun chequeo
    las viera: las dos habian pasado por el grade por separado. `graduar_par.py`
    las arregla; el paso 13 es lo que avisa cuando alguna no paso por ahi.

EL NARRADOR YA SALE NORMALIZADO
    `armar_p3c5.py` lo deja en -19,1 LUFS integrados con el limitador a
    -2 dBFS. Es la correccion que el Caso 4 necesito a posteriori -alli el
    armador de la serie nunca normalizaba- y que aqui esta hecha en origen.
    No hay archivo `_n19`: el que sale del armador ya es el bueno.

LA MARCA DE AGUA ENTRA DOS VECES, 168 CUADROS CADA UNA
    Al principio del caso y justo antes del carton de cierre. En medio no
    esta. Es el formato nuevo, igual que los Casos 3 y 4.
"""
import os
import sys

import bins

NOM = 'P3C5 VOCES REGISTROS Y CUENTAS v2'
CASO_BIN = ['PRIORIDAD 03', 'CASO 05 - Voces, registros y cuentas']
T0 = 86400

C = 'E:/DAE MASTER/PRIORIDAD 03/CASO 05 - Voces, registros y cuentas'
R = C + '/10 TIMELINE SEBASTIAN/RANURAS v2'
# El respiro es el ultimo cuadro de la ultima ranura congelado, y r43
# cambio: va en su propia carpeta para no tocar el de la v1.
RESP = C + '/10 TIMELINE SEBASTIAN/RESPIRO v2'
# EN ESTE CASO LOS LOWER THIRDS VIVEN EN LA MISMA CARPETA QUE LOS CARTONES
#     En el Caso 4 habia un subdirectorio `LOWER THIRDS`. Aqui los 24
#     archivos -17 cartones, 5 rotulos y los 2 blancos- estan juntos en
#     `02 CARTONES`, que es una carpeta y no un criterio: lo que separa a
#     un rotulo de un carton es la pista en la que entra, no el directorio.
K = C + '/02 CARTONES'
GRADE = C + '/01 PLANOS v2/_grade'
A = C + '/06 AUDIO'
MU = C + '/08 MUSICA'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_7s_fade.mov'

PISTAS_V = ['VIDEO', 'MOVIMIENTO', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

NARRADOR = 'P3C5_NARRADOR.wav'
MUSICA = 'P3C5_MUSICA_cama.wav'
RESPIRO = 'P3C5_respiro_v2_v48.mp4'

N_INTRO, N_BLANCO, N_RANURAS, N_RESPIRO, N_MARCA = 182, 119, 8307, 48, 168
OFF_ENTRADA = N_INTRO                                  #   182
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #   301
OFF_RESPIRO = OFF_RANURAS + N_RANURAS                  #  8608
OFF_CIERRE = OFF_RESPIRO + N_RESPIRO                   #  8656
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      #  8775
FIN = OFF_OUTRO + N_INTRO                              #  8957

LARGOS = [167, 300, 230, 183, 199, 117, 189, 137, 246, 168,
          159, 122, 197, 277, 113, 120, 228, 152, 198, 167,
          194, 131, 241, 203, 293, 296, 222, 151, 284, 134,
          181, 243, 242, 152, 146, 184, 183, 99, 253, 214,
          195, 131, 266]
assert len(LARGOS) == 43, len(LARGOS)
RAN = {}
_o = OFF_RANURAS
for _i, _n in enumerate(LARGOS):
    RAN['r%02d' % (_i + 1)] = (_o, _n)
    _o += _n
assert _o == OFF_RESPIRO, _o

# ------------------------------------------------------------------- V3
#  ✦ = propuesta o premisa equivocada: cama institucional, nunca una cara
# LOS DOS CARTONES DE APERTURA
#     23 oct 2026. La pieza corria 57,6 s sin un solo carton. Las otras
#     cuatro de la tanda anclan antes de los quince segundos -12,6 el C3 y
#     el C4, 14,2 el C1 y el C2- y aqui el primero caia en r06. Se siente
#     de entrada: casi un minuto de imagen y voz sin nada que leer.
#
#     El hueco tenia su texto esperando, y era el encabezado del documento
#     del profesor, que ningun carton decia:
#
#       r01  la primera linea  -la tesis de toda la pieza-
#       r02  la tercera        -la que autoriza el ejercicio entero-
#
#     CADA UNO SOBRE SU IMAGEN. r01 son las dos bandejas identicas y
#     vacias: esa ES la diferencia entre lo ofrecido y lo practicado, asi
#     que el carton cae sobre la imagen que ya la dice. r02 es la sala
#     vacia, que es el marco del ejercicio.
#
#     El de r01 va con el texto CORTO, en dos lineas y con el separador
#     de ae02 y ae03. r01 dura 167 cuadros -7,0 s- y en tres lineas no se
#     alcanza a leer: la ultima termina de entrar a los 3,1 s.
#
#     Un carton sobre r01 ensucia la rima con r43 -el lavado azul es una
#     segunda diferencia entre las dos mitades, que es lo que el paso 12
#     vigila en la rima mayor-. Se acepta a sabiendas: estan a seis
#     minutos una de otra y lo que el espectador compara es el contenido
#     de las bandejas, no su tono.
#
#     Los numeros de `ae` son referencias al documento, no orden de
#     pantalla -por eso falta `prop2`-; `ae07` es el ultimo que se sumo.
TENIDOS = [('P3C5_ae00_medio_ofrecido.mov', 'r01'),
           ('P3C5_ae07_alcance.mov', 'r02'),
           ('P3C5_ae01_individualizan.mov', 'r06'),
           ('P3C5_ae02_no_se_acusa.mov', 'r07'),
           ('P3C5_prop1_informe.mov', 'r11'),               # ✦
           ('P3C5_ae03_andres.mov', 'r13'),
           ('P3C5_cita02_cuaderno.mov', 'r15'),
           ('P3C5_cita01_pertinencia.mov', 'r17'),
           ('P3C5_prop3_estipulacion.mov', 'r19'),          # ✦
           ('P3C5_prop4_interceptaciones.mov', 'r20'),      # ✦
           ('P3C5_ae04_voz_sin_dueno.mov', 'r22'),
           ('P3C5_prop5_renata.mov', 'r24'),                # ✦
           ('P3C5_prop6_credibilidad.mov', 'r25'),          # ✦
           ('P3C5_ae05_grafica.mov', 'r26'),
           ('P3C5_prop7_regresa.mov', 'r31'),               # ✦
           ('P3C5_ae06_acta.mov', 'r34'),
           ('P3C5_prop8y9_alegato.mov', 'r39'),             # ✦
           ('P3C5_prop10_tercera.mov', 'r40'),              # ✦
           ('P3C5_prop11_sin_encierro.mov', 'r41')]         # ✦

# las siete placas con rostro. El chequeo comprueba que ninguna propuesta cae
# sobre una de ellas.
CON_ROSTRO = {'r03', 'r05', 'r21', 'r23', 'r27', 'r28', 'r32'}
PROPUESTAS = {'r11', 'r19', 'r20', 'r24', 'r25', 'r31', 'r39', 'r40', 'r41'}
RIMA_MAYOR = {'r33', 'r35'}

# ------------------------------------------------------------------- V7
LOWERS = [('P3C5_lt02_oscar.mov', 'r03', 12),
          ('P3C5_lt01_fecha_lugar.mov', 'r04', 14),
          ('P3C5_lt03_tomas.mov', 'r05', 12),
          ('P3C5_lt04_lucia.mov', 'r21', 10),
          ('P3C5_lt05_renata.mov', 'r23', 12)]

REAL = {'FGN_intro_version7.mp4': N_INTRO,
        'MARCA_DE_AGUA_DAE_7s_fade.mov': N_MARCA,
        'P3C5_carton_entrada.mov': N_BLANCO,
        'P3C5_carton_cierre.mov': N_BLANCO,
        RESPIRO: N_RESPIRO,
        NARRADOR: N_RANURAS}
REAL.update({f: RAN[r][1] for f, r in TENIDOS})
REAL.update({f: 96 for f, _, _ in LOWERS})

# El tope del paso 14: la norma de la tanda, 12,6 a 14,2 s.
TOPE_PRIMER_CARTON = 15.0

BLANCOS = ('P3C5_carton_entrada.mov', 'P3C5_carton_cierre.mov')
EN_V7 = {f for f, _, _ in LOWERS}
EN_V3 = {f for f, _ in TENIDOS}


# ------------------------------------------------------------------- rimas
#  LAS RIMAS, MEDIDAS: EL PASO QUE FALTABA
#      Una rima visual son dos planos que el espectador compara. Si cada uno
#      se gradua por su cuenta, la diferencia que ve ya no es la del caso sino
#      la del grade, y en este montaje eso paso DOS VECES antes de que nadie
#      lo notara: r33/r35 con las mesas a 174 niveles, y r01/r43 con las
#      bandejas azules de un lado y grises del otro.
#
#      Lo que se mide es el PLANO DE FONDO -el borde del cuadro, que en estos
#      encuadres es mesa, suelo o pared- y la saturacion media. No se miden
#      los percentiles de la imagen entera: en r33 los papeles tapan la mesa
#      y la mediana sube a 195 mientras en r35 se queda en 83, y esa
#      diferencia ES el argumento de la pieza.
#
#      Los umbrales salen de medir, no de elegir. Sobre las versiones rotas
#      guardadas en `_grade\_sin_rima` y las buenas:
#
#                        borde p5        saturacion media
#          r01/r43   roto 3,7  bien 0,3    roto 0,050  bien 0,011
#          r27/r28   roto 59,7 bien 1,5    roto 0,007  bien 0,001
#          r33/r35   roto 73,8 bien 0,4    roto 0,017  bien 0,000
#
#      Con 2,5 y 0,020 los tres rotos caen y los cuatro buenos pasan.
#
#      r21/r22 NO comparten encuadre -una es un plano cerrado con Lucia y la
#      otra uno abierto de la sala vacia-, asi que el borde no es el mismo
#      material en las dos y solo se le mide la saturacion. Es la misma
#      distincion que `plan_camara_p3c5.py` hace para r12/r13.
#  La v2 cambio dos de las cuatro. r01/r43 dejaron de ser cenitales sobre
#  una mesa y pasaron a filmarse a altura de mesa con la sala detras, asi que
#  el borde del cuadro ya no es un plano uniforme y medirlo no dice nada: de
#  ese par solo se comprueba la saturacion. r21/r22 siguen sin compartir
#  encuadre. r27/r28 y r33/r35 son identicos de encuadre y se miden entero.
RIMAS = [('r01', 'r43', False),     # las bandejas, ahora dentro de la sala
         ('r21', 'r22', False),     # la onda: mismo sitio, distinto encuadre
         ('r27', 'r28', True),      # Lucia con la anotacion y sin ella
         ('r33', 'r35', True)]      # LA RIMA MAYOR
RIMA_BORDE = 2.5
RIMA_SAT = 0.020


def _medir_placa(ruta):
    """(p5 del borde del cuadro, saturacion media). None si no se puede."""
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return None
    a = np.asarray(Image.open(ruta).convert('RGB')).astype(np.float32)
    l = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    h, w = l.shape
    m = max(8, h // 16)
    borde = np.concatenate([l[:m].ravel(), l[-m:].ravel(),
                            l[:, :m].ravel(), l[:, -m:].ravel()])
    mx, mn = a.max(2), a.min(2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0)
    return float(np.percentile(borde, 5)), float(sat.mean())


def _placas():
    return {f.split('_')[1]: os.path.join(GRADE, f)
            for f in os.listdir(GRADE) if f.endswith('.png')}


def _handles():
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    return resolve, pr, pr.GetMediaPool()


def _carpeta(mp):
    return bins.carpeta(mp, CASO_BIN)


def _clips(mp):
    return bins.clips(mp, CASO_BIN)


def _linea(pr):
    for i in range(pr.GetTimelineCount()):
        t = pr.GetTimelineByIndex(i + 1)
        if t.GetName() == NOM:
            return t
    return None


def _ranuras():
    return [f for f in sorted(os.listdir(R))
            if not f.startswith('_') and f.endswith(('.mov', '.mp4'))]


def medios(mp):
    rutas = [INTRO, MARCA, A + '/' + NARRADOR, MU + '/' + MUSICA,
             RESP + '/' + RESPIRO]
    rutas += [R + '/' + f for f in _ranuras()]
    rutas += [K + '/' + f for f in sorted(os.listdir(K))
              if not f.startswith('_') and f.endswith('.mov')]
    bins.importar(mp, CASO_BIN, rutas)
    _refrescar_medios(mp)


def _refrescar_medios(mp):
    """Un medio reemplazado EN SU SITIO deja el media pool desactualizado.

    23 oct 2026. El carton de r01 se rehizo con el mismo nombre y paso de 300
    cuadros a 167. El archivo en disco era el nuevo -ffprobe lo medi­a- pero
    Resolve siguio sirviendo el viejo: el clip del pool apunta a esa ruta y no
    vuelve a leerla. El montaje puso 167 cuadros DEL CARTON ANTERIOR y las
    catorce comprobaciones pasaron, porque todas miran posiciones y
    duraciones, no contenido.

    Es el tercer disfraz del mismo error -el nombre que gana a la ruta, la
    calidad que se hereda de la pagina Deliver- y se arregla igual: midiendo.
    Aqui se compara lo que el pool CREE que dura cada medio contra lo que la
    tabla dice, y el que no cuadre se borra y se vuelve a importar.
    """
    # EN DOS ENTRADAS `REAL` ES LO QUE SE USA, NO LO QUE DURA
    #     El intro mide 222 cuadros en disco y la pieza corta 182; el
    #     narrador es audio. Comparar esos dos aqui da falso positivo.
    SALTAR = {os.path.basename(INTRO), NARRADOR}
    IT = _clips(mp)
    malos = []
    for nombre, n in REAL.items():
        if nombre in SALTAR:
            continue
        c = IT.get(nombre)
        if c is None:
            continue
        try:
            hay = int(c.GetClipProperty('Frames'))
        except (TypeError, ValueError):
            continue
        if hay != n:
            malos.append((nombre, hay, n, c))
    if not malos:
        return
    print('   %d medios desactualizados en el pool; se reimportan:' % len(malos))
    rutas = []
    for nombre, hay, n, c in malos:
        print('      %-44s pool %d, tabla %d' % (nombre, hay, n))
        rutas.append(c.GetClipProperty('File Path'))
    mp.DeleteClips([c for _, _, _, c in malos])
    bins.importar(mp, CASO_BIN, rutas)
    IT = _clips(mp)
    quedan = []
    for nombre, _, n, _ in malos:
        c = IT.get(nombre)
        if c is None or int(c.GetClipProperty('Frames')) != n:
            quedan.append(nombre)
    if quedan:
        raise RuntimeError('siguen desactualizados: %s' % quedan)


def borrar(pr, mp):
    tl = _linea(pr)
    if not tl:
        print('no hay linea que borrar')
        return
    mp.SetCurrentFolder(_carpeta(mp))
    print('borrada:', mp.DeleteTimelines([tl]))


def linea(pr, mp):
    if _linea(pr):
        print('la linea ya existe, no se toca')
        return
    mp.SetCurrentFolder(_carpeta(mp))
    tl = mp.CreateEmptyTimeline(NOM)
    while tl.GetTrackCount('video') < len(PISTAS_V):
        tl.AddTrack('video')
    while tl.GetTrackCount('audio') < len(PISTAS_A):
        tl.AddTrack('audio', 'stereo')
    for i, n in enumerate(PISTAS_V):
        tl.SetTrackName('video', i + 1, n)
    for i, n in enumerate(PISTAS_A):
        tl.SetTrackName('audio', i + 1, n)
    print('creada; arranque %s, %s fps' % (tl.GetStartTimecode(),
                                           tl.GetSetting('timelineFrameRate')))


def v1(pr, mp):
    tl = _linea(pr)
    pr.SetCurrentTimeline(tl)
    if tl.GetItemListInTrack('video', 1):
        print('V1 ya tiene clips, no se toca')
        return
    IT = _clips(mp)
    sec = [('FGN_intro_version7.mp4', N_INTRO),
           ('P3C5_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in _ranuras()]
    sec += [(RESPIRO, N_RESPIRO),
            ('P3C5_carton_cierre.mov', N_BLANCO),
            ('FGN_intro_version7.mp4', N_INTRO)]
    lote, off = [], 0
    for nombre, n in sec:
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 1, 'recordFrame': T0 + off})
        off += n
    assert off == FIN, off
    mp.AppendToTimeline(lote)
    it = tl.GetItemListInTrack('video', 1)
    print('V1 %d clips, termina en %d (esperado %d)'
          % (len(it), it[-1].GetEnd() - T0, FIN))


def _poner(mp, tl, pista, lote, etiqueta):
    if tl.GetItemListInTrack('video', pista):
        print('V%d ya tiene clips, no se toca' % pista)
        return
    mp.AppendToTimeline(lote)
    print('V%d %d %s' % (pista, len(tl.GetItemListInTrack('video', pista)),
                         etiqueta))


def v3(pr, mp):
    tl = _linea(pr)
    IT = _clips(mp)
    lote = []
    for nombre, r in TENIDOS:
        ini, largo = RAN[r]
        assert REAL[nombre] == largo, (nombre, r, REAL[nombre], largo)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0,
                     'endFrame': largo, 'trackIndex': 3,
                     'recordFrame': T0 + ini})
    _poner(mp, tl, 3, lote, 'cartones tenidos')


def v7(pr, mp):
    tl = _linea(pr)
    IT = _clips(mp)
    lote = []
    for nombre, r, off in LOWERS:
        ini, largo = RAN[r]
        n = REAL[nombre]
        assert 0 <= off and off + n <= largo, (nombre, r, off, n, largo)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 7, 'recordFrame': T0 + ini + off})
    _poner(mp, tl, 7, lote, 'lower thirds')


def pegado(pr, mp):
    tl = _linea(pr)
    IT = _clips(mp)
    lote = []
    if not tl.GetItemListInTrack('video', 5):
        for pos in (OFF_RANURAS, OFF_CIERRE - N_MARCA):
            lote.append({'mediaPoolItem': IT['MARCA_DE_AGUA_DAE_7s_fade.mov'],
                         'startFrame': 0, 'endFrame': N_MARCA, 'trackIndex': 5,
                         'recordFrame': T0 + pos})
    if not tl.GetItemListInTrack('audio', 2):
        lote.append({'mediaPoolItem': IT[NARRADOR], 'startFrame': 0,
                     'endFrame': N_RANURAS, 'trackIndex': 2,
                     'recordFrame': T0 + OFF_RANURAS, 'mediaType': 2})
    if not tl.GetItemListInTrack('audio', 5):
        lote.append({'mediaPoolItem': IT[MUSICA], 'startFrame': 0,
                     'endFrame': OFF_OUTRO - OFF_ENTRADA, 'trackIndex': 5,
                     'recordFrame': T0 + OFF_ENTRADA, 'mediaType': 2})
    if lote:
        mp.AppendToTimeline(lote)
    for k in ('video', 'audio'):
        for i in range(tl.GetTrackCount(k)):
            it = tl.GetItemListInTrack(k, i + 1)
            if it:
                print('%s%d %-14s %2d  %5d-%5d'
                      % (k[0].upper(), i + 1, tl.GetTrackName(k, i + 1), len(it),
                         it[0].GetStart() - T0, it[-1].GetEnd() - T0))


def _revisar_pista(tl, pista, cortes):
    prob, ant, puestos = [], 0, []
    for c in sorted(tl.GetItemListInTrack('video', pista),
                    key=lambda x: x.GetStart()):
        a, b, n = c.GetStart() - T0, c.GetEnd() - T0, c.GetName()
        if a < ant:
            prob.append((n, 'solape'))
        ant = b
        if n in REAL and b - a != REAL[n]:
            prob.append((n, 'recortado %d de %d' % (b - a, REAL[n])))
        cruza = [x for x in cortes if a < x < b]
        if cruza:
            prob.append((n, 'cruza corte en %s' % cruza))
        puestos.append((a, b, n))
    return prob, puestos


def chequeo(pr):
    tl = _linea(pr)
    fallos = []

    v = tl.GetItemListInTrack('video', 1)
    pos, cortes = 0, [0]
    for c in v:
        if c.GetStart() - T0 != pos:
            fallos.append('1: discontinuidad en %d' % pos)
        pos = c.GetEnd() - T0
        cortes.append(pos)
    if pos != FIN:
        fallos.append('1: V1 termina en %d, no %d' % (pos, FIN))
    print('1) V1 %d clips contiguos, termina en %d (esperado %d)'
          % (len(v), pos, FIN))

    intro = [c for c in v if c.GetName() == 'FGN_intro_version7.mp4']
    largos = [c.GetEnd() - c.GetStart() for c in intro]
    ok2 = len(intro) == 2 and largos == [N_INTRO, N_INTRO]
    print('2) intro y outro cortados en %d: %s %s'
          % (N_INTRO, largos, 'OK' if ok2 else 'FALLA'))
    if not ok2:
        fallos.append('2: intro/outro %s' % largos)

    print('3) bloque de preguntas: no existe en este montaje')

    resp = [c for c in v if 'respiro' in c.GetName()]
    ok4 = (len(resp) == 1 and resp[0].GetStart() - T0 == OFF_RESPIRO
           and resp[0].GetEnd() - T0 == OFF_CIERRE)
    print('4) respiro %s %s'
          % ([(c.GetStart() - T0, c.GetEnd() - T0) for c in resp],
             'OK' if ok4 else 'FALLA'))
    if not ok4:
        fallos.append('4: respiro')

    ma = [(c.GetStart() - T0, c.GetEnd() - T0)
          for c in tl.GetItemListInTrack('video', 5)]
    esp_ma = [(OFF_RANURAS, OFF_RANURAS + N_MARCA),
              (OFF_CIERRE - N_MARCA, OFF_CIERRE)]
    print('5) marca de agua %s esperado %s %s'
          % (ma, esp_ma, 'OK' if ma == esp_ma else 'FALLA'))
    if ma != esp_ma:
        fallos.append('5: marca de agua')

    malos = []
    for k in ('video', 'audio'):
        for i in range(tl.GetTrackCount(k)):
            for c in tl.GetItemListInTrack(k, i + 1):
                n, d = c.GetName(), c.GetEnd() - c.GetStart()
                if n in REAL and d != REAL[n]:
                    malos.append((k, i + 1, n, d, REAL[n]))
    print('6) duraciones contra el conteo real:', 'OK' if not malos else malos)
    if malos:
        fallos.append('6: %s' % malos)

    vacias = [('video', 2), ('video', 4), ('video', 6),
              ('audio', 3), ('audio', 4)]
    ocup = [x for x in vacias if tl.GetItemListInTrack(*x)]
    print('7) V2/V4/V6/A3/A4 vacias:', 'OK' if not ocup else ocup)
    if ocup:
        fallos.append('7: %s' % ocup)

    prob3, p3 = _revisar_pista(tl, 3, cortes)
    if len(p3) != len(TENIDOS):
        prob3.append(('faltan cartones', len(p3), len(TENIDOS)))
    print('8) cartones V3 (%d):' % len(p3), 'OK' if not prob3 else prob3)
    if prob3:
        fallos.append('8: %s' % prob3)

    prob7, p7 = _revisar_pista(tl, 7, cortes)
    pisa = [(n7, n3) for a7, b7, n7 in p7 for a3, b3, n3 in p3
            if a7 < b3 and a3 < b7]
    if pisa:
        prob7 += [('V3 encima', pisa)]
    if len(p7) != len(LOWERS):
        prob7.append(('faltan rotulos', len(p7), len(LOWERS)))
    print('9) lower thirds V7 (%d):' % len(p7), 'OK' if not prob7 else prob7)
    if prob7:
        fallos.append('9: %s' % prob7)

    esp = {('audio', 1): (0, FIN, 2),
           ('audio', 2): (OFF_RANURAS, OFF_RESPIRO, 1),
           ('audio', 5): (OFF_ENTRADA, OFF_OUTRO, 1)}
    for k, q in esp.items():
        it = tl.GetItemListInTrack(*k)
        g = (it[0].GetStart() - T0, it[-1].GetEnd() - T0, len(it)) if it else None
        print('10) %s%d %s esperado %s %s'
              % (k[0].upper(), k[1], g, q, 'OK' if g == q else 'FALLA'))
        if g != q:
            fallos.append('10: %s%d' % (k[0].upper(), k[1]))

    # LAS DOS COMPROBACIONES PROPIAS DE ESTE CASO
    #   11  Nueve de las decisiones que la pieza expone son equivocadas.
    #       Ninguna puede caer sobre una cara: la cara responderia por la
    #       decision, y la decision es de quien la pide, no de quien aparece.
    choque = PROPUESTAS & CON_ROSTRO
    print('11) ninguna propuesta sobre una cara:',
          'OK' if not choque else choque)
    if choque:
        fallos.append('11: %s' % choque)

    #   12  La rima mayor va limpia. r33 y r35 son el mismo encuadre: lo
    #       unico que cambia entre las dos es lo que hay sobre la mesa. Un
    #       carton encima pondria una segunda diferencia y el espectador
    #       leeria esa.
    sucias = set()
    for r in sorted(RIMA_MAYOR):
        a, n = RAN[r]
        b = a + n
        for pista in (3, 7):
            for x, y, nom in _revisar_pista(tl, pista, [])[1]:
                if x < b and a < y:
                    sucias.add((r, nom))
    print('12) la rima mayor r33/r35 sin graficos encima:',
          'OK' if not sucias else sucias)
    if sucias:
        fallos.append('12: %s' % sorted(sucias))

    #   13  Las cuatro rimas, medidas sobre la placa graduada. Ver RIMAS.
    P = _placas()
    sucias13, sin_medir = [], []
    for a, b, mismo in RIMAS:
        if a not in P or b not in P:
            sin_medir.append('%s/%s' % (a, b))
            continue
        ma, mb = _medir_placa(P[a]), _medir_placa(P[b])
        if ma is None or mb is None:
            sin_medir.append('%s/%s' % (a, b))
            continue
        if mismo and abs(ma[0] - mb[0]) > RIMA_BORDE:
            sucias13.append(('%s/%s' % (a, b), 'fondo a %.1f niveles'
                             % abs(ma[0] - mb[0])))
        if abs(ma[1] - mb[1]) > RIMA_SAT:
            sucias13.append(('%s/%s' % (a, b), 'saturacion a %.3f'
                             % abs(ma[1] - mb[1])))
    print('13) las %d rimas graduadas a la par:' % len(RIMAS),
          'OK' if not sucias13 else sucias13,
          '' if not sin_medir else '(sin medir: %s)' % sin_medir)
    if sucias13:
        fallos.append('13: %s' % sucias13)

    #   14  EL PRIMER CARTON ANCLA ANTES DE LOS QUINCE SEGUNDOS
    #       23 oct 2026. El P3C5 corria 57,6 s sin un solo carton y nada lo
    #       vio: las trece comprobaciones miran que cada carton este donde
    #       dice la tabla, ninguna miraba CUANDO entra el primero. Las
    #       cuatro piezas de la tanda anclan entre 12,6 y 14,2 s; esa es la
    #       norma de la casa y ahora se mide.
    it3 = tl.GetItemListInTrack('video', 3)
    pri = (it3[0].GetStart() - T0) / (24000 / 1001.0) if it3 else None
    ok14 = pri is not None and pri <= TOPE_PRIMER_CARTON
    print('14) el primer carton entra en %s (tope %.1f s): %s'
          % ('%.1f s' % pri if pri is not None else 'ninguno',
             TOPE_PRIMER_CARTON, 'OK' if ok14 else 'FALLA'))
    if not ok14:
        fallos.append('14: primer carton en %s'
                      % ('%.1f s' % pri if pri is not None else 'ninguno'))

    print('')
    print('FALLOS:', fallos if fallos else 'NINGUNO')
    return not fallos


if __name__ == '__main__':
    paso = sys.argv[1] if len(sys.argv) > 1 else 'chequeo'
    resolve, pr, mp = _handles()
    if paso == 'medios':
        medios(mp)
    elif paso == 'linea':
        linea(pr, mp)
    elif paso == 'v1':
        v1(pr, mp)
    elif paso == 'v3':
        v3(pr, mp)
    elif paso == 'v7':
        v7(pr, mp)
    elif paso == 'pegado':
        pegado(pr, mp)
    elif paso == 'chequeo':
        sys.exit(0 if chequeo(pr) else 1)
    elif paso == 'borrar':
        borrar(pr, mp)
    else:
        print(__doc__)
