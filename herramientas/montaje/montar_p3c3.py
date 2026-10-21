#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del PRIORIDAD 03 · Caso 3 «Ruta del Golfo».

    python montar_p3c3.py medios     importa a la carpeta del caso
    python montar_p3c3.py linea      crea la linea con el mapa de pistas
    python montar_p3c3.py v1         intro + entrada + 31 ranuras + respiro
                                     + cierre + outro
    python montar_p3c3.py v2         la capa de movimiento, que se puede apagar
    python montar_p3c3.py v3         los cartones tenidos
    python montar_p3c3.py v7         los seis lower thirds
    python montar_p3c3.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_p3c3.py chequeo    el chequeo
    python montar_p3c3.py borrar     borra la linea para rehacerla entera

ESTE ES EL PRIMER CASO QUE NACE CON EL FORMATO NUEVO
    Los dos anteriores se montaron con el viejo y despues se transformaron con
    `sin_preguntas.py`. Este arranca ya con las tres reglas que salieron de esa
    revision, asi que aqui no hay nada que transformar:

    EL INTRO SE CORTA EN 182, NO EN 222
        `FGN_intro_version7.mp4` dura 222 cuadros, pero el cuadro 182 es el
        primero de blanco limpio -medido contando pixeles que se apartan del
        maximo: 172 ya esta en 0,6 %, 181 en 0,012 % y 182 en 0,000 %-. Del 182
        al 208 son 27 cuadros de blanco muerto y en el 209 entra un corte duro
        a otro edificio. Su audio esta en cero absoluto desde el 168, asi que
        el corte no parte ningun sonido. Y como el carton de entrada y el de
        cierre son blancos, el empalme queda blanco contra blanco.

    NO HAY BLOQUE DE PREGUNTAS
        La votacion y la tarea del foro van en la implementacion web. La pieza
        termina donde termina el caso: ultima toma, respiro de 48 cuadros con
        su ultimo cuadro congelado, carton de cierre y outro.

    LA MARCA DE AGUA ENTRA DOS VECES, 168 CUADROS CADA UNA
        Al principio del caso y justo antes del carton de cierre. En medio no
        esta.

LAS DOS CITAS NO VAN DONDE SE CITAN
    `cap01` y `cap02` -«se entregan el viernes» y «el saldo queda alla»- son
    del bloque de las capturas, pero esa ranura mide 178 cuadros y ya lleva
    `ae02`. Van al final, en r26, sobre la conversacion integra: 102 + 103
    cuadros, uno detras de otro, que es justo el largo de la ranura. Se leen
    cuando la pieza las esta reexaminando, que es mejor que donde estaban.

LAS TRES PROPUESTAS, Y SU CAMA
    `prop1`, `prop2` y `prop3` son las propuestas equivocadas que el caso cita
    literales, y no caen nunca sobre una cara: van sobre la mesa del equipo en
    cenital, el informe y el esfero, y la sala de reunion. Cada vez que
    aparece una mala propuesta, la pieza se va a la oficina y no a la ruta.
"""
import os
import sys

import bins

NOM = 'P3C3 RUTA DEL GOLFO - SIN PREGUNTAS'
CASO_BIN = ['PRIORIDAD 03', 'CASO 03 - Ruta del Golfo']
T0 = 86400

C = 'E:/DAE MASTER/PRIORIDAD 03/CASO 03 - Ruta del Golfo'
R = C + '/10 TIMELINE SEBASTIAN/RANURAS'
RESP = C + '/10 TIMELINE SEBASTIAN/RESPIRO'
K = C + '/02 CARTONES'
MV = C + '/07 MOVIMIENTO/CAPA V2'
A = C + '/06 AUDIO'
MU = C + '/08 MUSICA'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_7s_fade.mov'

PISTAS_V = ['VIDEO', 'MOVIMIENTO', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

N_INTRO, N_BLANCO, N_RANURAS, N_RESPIRO, N_MARCA = 182, 119, 6100, 48, 168
OFF_ENTRADA = N_INTRO                                  #  182
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #  301
OFF_RESPIRO = OFF_RANURAS + N_RANURAS                  # 6401
OFF_CIERRE = OFF_RESPIRO + N_RESPIRO                   # 6449
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      # 6568
FIN = OFF_OUTRO + N_INTRO                              # 6750

RAN = {}
_o = OFF_RANURAS
for _r, _n in [('r01', 202), ('r02', 243), ('r03', 168), ('r04', 303),
               ('r05', 178), ('r06', 167), ('r07', 178), ('r08', 237),
               ('r09', 150), ('r10', 223), ('r11', 257), ('r12', 169),
               ('r13', 229), ('r14', 228), ('r15', 210), ('r16', 233),
               ('r17', 101), ('r18', 170), ('r19', 197), ('r20', 104),
               ('r21', 173), ('r22', 358), ('r23', 170), ('r24', 182),
               ('r25', 174), ('r26', 205), ('r27', 184), ('r28', 201),
               ('r29', 176), ('r30', 177), ('r31', 153)]:
    RAN[_r] = (_o, _n)
    _o += _n
assert _o == OFF_RESPIRO, _o

# ------------------------------------------------------------------- V2
# Cada clip cubre su ranura ENTERA: apagar la pista devuelve la pieza a su
# version de placas sostenidas, sin huecos ni saltos de encuadre.
#
# Faltan dos a proposito. `r23` -Marta de lejos- porque a ese tamano el modelo
# le inventaba un paso y la capa no aportaba nada; `r30` -los dos viajeros que
# se van- porque van caminando, y frenar un paso 2,3 veces para que llene la
# ranura se lee como camara lenta. Las dos quedan con su horneado de camara.
IDLE = [('P3C3_r04_idle_kf02_los_cuatro_espaldas_v303.mp4', 'r04'),
        ('P3C3_r05_idle_kf03_luis_computador_v178.mp4', 'r05'),
        ('P3C3_r06_idle_kf04_marta_giros_v167.mp4', 'r06'),
        ('P3C3_r09_idle_kf05_omar_volante_v150.mp4', 'r09'),
        ('P3C3_r10_idle_kf06_teresa_cocina_v223.mp4', 'r10'),
        ('P3C3_r15_idle_kf08_nidia_local_v210.mp4', 'r15'),
        ('P3C3_r20_idle_kf12_viajero_documento_v104.mp4', 'r20')]

# ------------------------------------------------------------------- V3
#  ✦ = propuesta equivocada: cama institucional, nunca una cara
TENIDOS = [('P3C3_ae01_progresiva.mov', 'r01'),
           ('P3C3_ae02_no_identificada.mov', 'r07'),
           ('P3C3_prop1_tres_peticiones.mov', 'r08'),       # ✦
           ('P3C3_ae03_podian_salir.mov', 'r11'),
           ('P3C3_prop2_agregar_trata.mov', 'r12'),         # ✦
           ('P3C3_ae04_materialmente.mov', 'r14'),
           ('P3C3_ae05_sin_relacion.mov', 'r17'),
           ('P3C3_prop3_ignorar.mov', 'r21'),               # ✦
           ('P3C3_ae06_no_atribuido.mov', 'r25'),
           ('P3C3_ae07_si_describen.mov', 'r27'),
           ('P3C3_ae08_sin_cierre.mov', 'r28'),
           ('P3C3_ae09_sin_inercia.mov', 'r31')]

# las dos citas, una detras de otra, llenando r26 exacto
CITAS = [('P3C3_cap01_viernes.mov', 'r26', 0, 102),
         ('P3C3_cap02_saldo.mov', 'r26', 102, 103)]

# ------------------------------------------------------------------- V7
LOWERS = [('P3C3_lt01_fecha_lugar.mov', 'r02', 14),
          ('P3C3_lt02_luis.mov', 'r05', 10),
          ('P3C3_lt03_marta.mov', 'r06', 10),
          ('P3C3_lt04_omar.mov', 'r09', 8),
          ('P3C3_lt05_teresa.mov', 'r10', 12),
          ('P3C3_lt06_nidia.mov', 'r15', 12)]

REAL = {'FGN_intro_version7.mp4': N_INTRO,
        'MARCA_DE_AGUA_DAE_7s_fade.mov': N_MARCA,
        'P3C3_carton_entrada.mov': N_BLANCO,
        'P3C3_carton_cierre.mov': N_BLANCO,
        'P3C3_respiro_v48.mp4': N_RESPIRO}
REAL.update({f: RAN[r][1] for f, r in TENIDOS})
REAL.update({f: n for f, _, _, n in CITAS})
REAL.update({f: 96 for f, _, _ in LOWERS})
REAL.update({f: RAN[r][1] for f, r in IDLE})


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
    rutas = [INTRO, MARCA, A + '/P3C3_NARRADOR.wav',
             MU + '/P3C3_MUSICA_v2.wav', RESP + '/P3C3_respiro_v48.mp4']
    rutas += [R + '/' + f for f in _ranuras()]
    rutas += [K + '/' + f for f in sorted(os.listdir(K))
              if not f.startswith('_') and f.endswith('.mov')]
    rutas += [MV + '/' + f for f in sorted(os.listdir(MV))
              if not f.startswith('_') and f.endswith('.mp4')]
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
           ('P3C3_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in _ranuras()]
    sec += [('P3C3_respiro_v48.mp4', N_RESPIRO),
            ('P3C3_carton_cierre.mov', N_BLANCO),
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


def v2(pr, mp):
    tl = _linea(pr)
    IT = _clips(mp)
    lote = []
    for nombre, r in IDLE:
        ini, largo = RAN[r]
        assert REAL[nombre] == largo, (nombre, r)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0,
                     'endFrame': largo, 'trackIndex': 2,
                     'recordFrame': T0 + ini})
    _poner(mp, tl, 2, lote, 'clips de movimiento')


def v3(pr, mp):
    tl = _linea(pr)
    IT = _clips(mp)
    lote = []
    for nombre, r in TENIDOS:
        ini, largo = RAN[r]
        assert REAL[nombre] == largo, (nombre, r)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0,
                     'endFrame': largo, 'trackIndex': 3,
                     'recordFrame': T0 + ini})
    for nombre, r, off, n in CITAS:
        ini, largo = RAN[r]
        assert 0 <= off and off + n <= largo, (nombre, r, off, n, largo)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 3, 'recordFrame': T0 + ini + off})
    _poner(mp, tl, 3, lote, 'cartones (%d tenidos, %d citas)'
           % (len(TENIDOS), len(CITAS)))


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
        lote.append({'mediaPoolItem': IT['P3C3_NARRADOR.wav'], 'startFrame': 0,
                     'endFrame': N_RANURAS, 'trackIndex': 2,
                     'recordFrame': T0 + OFF_RANURAS, 'mediaType': 2})
    if not tl.GetItemListInTrack('audio', 5):
        lote.append({'mediaPoolItem': IT['P3C3_MUSICA_v2.wav'], 'startFrame': 0,
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
    elif paso == 'v2':
        v2(pr, mp)
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
