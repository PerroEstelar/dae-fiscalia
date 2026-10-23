#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del PRIORIDAD 03 · Caso 4 «Puerto de salida» — VERSION 2.

QUE CAMBIA CONTRA LA v1, Y QUE NO
    NO cambia nada de lo que se oye ni de lo que se lee: la rejilla, la voz,
    la musica, los dieciseis cartones, los cuatro lower thirds y sus
    posiciones son exactamente los mismos. Las 39 ranuras miden lo mismo.

    Cambia lo que se VE. Las 39 placas se rehicieron bajo la
    BIBLIA_puesta_en_escena_P3: once lugares en vez de cuatro, 23 ranuras
    con gente en vez de cuatro caras, tres cenitales en vez de diecisiete,
    cuatro primeros planos de expresion donde no habia ninguno, y tres
    registros de luz donde solo habia «flat even light».

    Y cinco ranuras llevan video generado con Seedance sobre el keyframe
    -las cinco que tienen accion real-. Las otras 34 siguen siendo placa
    sostenida con la camara horneada.

LA LINEA v1 NO SE BORRA
    Queda en el proyecto con su nombre. Esta es una linea nueva.


    python montar_p3c4.py medios     importa a la carpeta del caso
    python montar_p3c4.py linea      crea la linea con el mapa de pistas
    python montar_p3c4.py v1         intro + entrada + 39 ranuras + respiro
                                     + cierre + outro
    python montar_p3c4.py v3         los cartones tenidos y las dos citas
    python montar_p3c4.py v7         los cuatro lower thirds
    python montar_p3c4.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_p3c4.py chequeo    el chequeo
    python montar_p3c4.py borrar     borra la linea para rehacerla entera

LA CUENTA, QUE TIENE QUE CUADRAR AL CUADRO
    intro 182 + entrada 119 + ranuras 8006 + respiro 48 + cierre 119
    + outro 182 = 8656 cuadros = 6:01,0 a 23,976.

NO HAY CAPA V2 EN ESTE MONTAJE
    Las 36 ranuras llevan la camara HORNEADA en el propio clip -`camara.py`,
    el mismo pulso de mano de la serie-, asi que la pieza no queda sostenida
    sobre imagenes fijas aunque no haya clips de movimiento generados. La capa
    V2 se puede anadir despues sin tocar nada: cada clip de movimiento cubre
    su ranura entera y se monta encima.

    Y el empuje de cada ranura esta asignado por lo que la placa significa
    -abre donde hay falta, cierra donde hay acumulacion-, no por variar. Esta
    escrito en `plan_camara_p3c4.py`.

LAS SIETE PROPUESTAS, Y SU CAMA
    Ninguna cae sobre una cara. Las seis placas con rostro son r02, r05, r13,
    r19, r22 y r25; los cartones de propuesta van en r08, r10, r15, r20, r24 y
    r29, que son mesa, estrado, microfono, silla y hoja. Comprobado en el
    chequeo, paso 11.

    La septima -«simples precisiones»- no lleva carton: r36 YA ES la grafica
    que la desarma. Ponerla ademas en letra seria decir dos veces lo mismo y
    tapar la grafica justo cuando entra.

LA MARCA DE AGUA ENTRA DOS VECES, 168 CUADROS CADA UNA
    Al principio del caso y justo antes del carton de cierre. En medio no
    esta. Es el formato nuevo, igual que el Caso 3.
"""
import os
import sys

import bins
import os.path

NOM = 'P3C4 PUERTO DE SALIDA v2'
CASO_BIN = ['PRIORIDAD 03', 'CASO 04 - Puerto de salida']
T0 = 86400

C = 'E:/DAE MASTER/PRIORIDAD 03/CASO 04 - Puerto de salida'
R = C + '/10 TIMELINE SEBASTIAN/RANURAS v2'
# EL RESPIRO TAMBIEN ES NUEVO
#     Es el ultimo cuadro de la ultima ranura congelado, y r39 dejo de
#     ser las seis carpetas para ser la fachada al final del dia. Va en
#     su propia carpeta para no tocar el respiro de la v1, que sigue
#     sirviendo a la linea vieja.
RESP = C + '/10 TIMELINE SEBASTIAN/RESPIRO v2'
K = C + '/02 CARTONES'
LT = C + '/02 CARTONES/LOWER THIRDS'
A = C + '/06 AUDIO'
MU = C + '/08 MUSICA'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_7s_fade.mov'

PISTAS_V = ['VIDEO', 'MOVIMIENTO', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

# EL NARRADOR VA NORMALIZADO A -19 LUFS, Y NO LO ESTABA
#     Medido sobre el master v1 ya renderizado: la pieza entera salio en
#     -15,7 LUFS integrados. El culpable era el narrador, en -15,4 cuando la
#     serie lo fija en -19. El Caso 3, medido en el mismo sitio, esta en
#     -19,0 exactos: el Caso 4 habria sonado casi cuatro decibeles mas alto
#     que los otros tres en el mismo curso.
#
#     El nivelado entre bloques -que dejo el peor escalon en 0,15 LU- iguala
#     los dieciocho bloques ENTRE SI, no contra el objetivo de la serie. Son
#     dos cosas distintas y la segunda se me paso.
#
#     Se corrige con ganancia lineal y no con loudnorm, para no tocar el
#     nivelado entre bloques: -3,6 dB deja la integrada en -19,0 exactos y el
#     pico real en -5,0 dBFS.
#
#     La cama de musica NO se toca: se construyo contra los numeros absolutos
#     de la serie -26 en hueco y -32 bajo voz-, que no dependen del nivel del
#     archivo de voz.
NARRADOR = 'P3C4_NARRADOR_n19.wav'

N_INTRO, N_BLANCO, N_RANURAS, N_RESPIRO, N_MARCA = 182, 119, 8006, 48, 168
OFF_ENTRADA = N_INTRO                                  #   182
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #   301
OFF_RESPIRO = OFF_RANURAS + N_RANURAS                  #  8307
OFF_CIERRE = OFF_RESPIRO + N_RESPIRO                   #  8355
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      #  8474
FIN = OFF_OUTRO + N_INTRO                              #  8656

LARGOS = [240, 180, 150, 146, 244, 209, 285, 260, 162, 234,
          152, 208, 209, 167, 167, 272, 257, 102, 152, 237,
          131, 215, 300, 294, 206, 232, 289, 285, 118, 285,
          113, 161, 189, 241, 109, 205, 145, 292, 163]
RAN = {}
_o = OFF_RANURAS
for _i, _n in enumerate(LARGOS):
    RAN['r%02d' % (_i + 1)] = (_o, _n)
    _o += _n
assert _o == OFF_RESPIRO, _o

# ------------------------------------------------------------------- V3
#  ✦ = propuesta o decision equivocada: cama institucional, nunca una cara
TENIDOS = [('P3C4_ae01_preliminares.mov', 'r01'),
           ('P3C4_ae02_seis_meses.mov', 'r07'),
           ('P3C4_prop1_cuentas.mov', 'r08'),               # ✦
           ('P3C4_prop2_registro.mov', 'r10'),              # ✦
           ('P3C4_ae03_sin_actos.mov', 'r14'),
           ('P3C4_prop3_permanente.mov', 'r15'),            # ✦
           ('P3C4_ae04_no_demostrada.mov', 'r18'),
           ('P3C4_prop4_jueza.mov', 'r20'),                 # ✦
           ('P3C4_ae05_sin_anuncio.mov', 'r21'),
           ('P3C4_ae06_mensajes_nuevos.mov', 'r23'),
           ('P3C4_prop5_no_se_oye.mov', 'r24'),             # ✦
           ('P3C4_cita01_imputacion_lina.mov', 'r26'),
           ('P3C4_ae07_no_individualiza.mov', 'r27'),
           ('P3C4_prop6_silencio.mov', 'r29'),              # ✦
           ('P3C4_ae08_individualizadas.mov', 'r31'),
           ('P3C4_cita02_informe_anexos.mov', 'r37')]

# las seis placas con rostro. El chequeo comprueba que ninguna propuesta cae
# sobre una de ellas.
CON_ROSTRO = {'r02', 'r05', 'r13', 'r19', 'r22', 'r25'}
PROPUESTAS = {'r08', 'r10', 'r15', 'r20', 'r24', 'r29'}

# ------------------------------------------------------------------- V7
LOWERS = [('P3C4_lt01_nora.mov', 'r02', 12),
          ('P3C4_lt02_ivan.mov', 'r05', 14),
          ('P3C4_lt03_recepcionista.mov', 'r13', 10),
          ('P3C4_lt04_lina.mov', 'r25', 12)]

REAL = {'FGN_intro_version7.mp4': N_INTRO,
        'MARCA_DE_AGUA_DAE_7s_fade.mov': N_MARCA,
        'P3C4_carton_entrada.mov': N_BLANCO,
        'P3C4_carton_cierre.mov': N_BLANCO,
        'P3C4_respiro_v2_v48.mp4': N_RESPIRO,
        NARRADOR: N_RANURAS}
REAL.update({f: RAN[r][1] for f, r in TENIDOS})
REAL.update({f: 96 for f, _, _ in LOWERS})


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
    rutas = [INTRO, MARCA, A + '/' + NARRADOR,
             MU + '/P3C4_MUSICA_cama.wav', RESP + '/P3C4_respiro_v2_v48.mp4']
    rutas += [R + '/' + f for f in _ranuras()]
    rutas += [K + '/' + f for f in sorted(os.listdir(K))
              if not f.startswith('_') and f.endswith('.mov')]
    rutas += [LT + '/' + f for f in sorted(os.listdir(LT))
              if not f.startswith('_') and f.endswith('.mov')]
    bins.importar(mp, CASO_BIN, rutas)


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
           ('P3C4_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in _ranuras()]
    sec += [('P3C4_respiro_v2_v48.mp4', N_RESPIRO),
            ('P3C4_carton_cierre.mov', N_BLANCO),
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
        lote.append({'mediaPoolItem': IT['P3C4_MUSICA_cama.wav'], 'startFrame': 0,
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

    vacias = [('video', 4), ('video', 6), ('audio', 3), ('audio', 4)]
    ocup = [x for x in vacias if tl.GetItemListInTrack(*x)]
    print('7) V4/V6/A3/A4 vacias:', 'OK' if not ocup else ocup)
    if ocup:
        fallos.append('7: %s' % ocup)

    prob3, p3 = _revisar_pista(tl, 3, cortes)
    print('8) cartones V3 (%d):' % len(p3), 'OK' if not prob3 else prob3)
    if prob3:
        fallos.append('8: %s' % prob3)

    prob7, p7 = _revisar_pista(tl, 7, cortes)
    pisa = [(n7, n3) for a7, b7, n7 in p7 for a3, b3, n3 in p3
            if a7 < b3 and a3 < b7]
    if pisa:
        prob7 += [('V3 encima', pisa)]
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

    # LA COMPROBACION PROPIA DE ESTE CASO
    #   Seis de las siete decisiones que la pieza expone son equivocadas y una
    #   la toma una jueza. Ninguna puede caer sobre una cara.
    choque = PROPUESTAS & CON_ROSTRO
    print('11) ninguna propuesta sobre una cara:',
          'OK' if not choque else choque)
    if choque:
        fallos.append('11: %s' % choque)

    # LA RIMA r01/r39, QUE AQUI SE COMPRUEBA DE OTRA MANERA
    #     En el Caso 5 las rimas se miden exigiendo el MISMO plano de fondo,
    #     porque alli las dos mitades son el mismo sitio a la misma hora y lo
    #     unico que cambia es lo que hay encima.
    #
    #     Aqui no: r01 y r39 son la misma fachada AL AMANECER Y AL FINAL DEL
    #     DIA. Que el tono sea distinto ES la rima. Exigirles el mismo fondo
    #     seria borrar justo lo que dicen.
    #
    #     Lo que si tiene que coincidir es el EMPUJE DE CAMARA -si una mitad
    #     se mueve distinto de la otra, el espectador lee el movimiento y no
    #     la hora- y eso se comprueba en plan_camara_p3c4_v2.py, no aqui.
    print('13) la rima r01/r39 es de encuadre y hora, no de tono:'
          ' se comprueba en plan_camara_p3c4_v2.py')

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
