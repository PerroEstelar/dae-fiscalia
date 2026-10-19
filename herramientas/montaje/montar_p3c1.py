#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del PRIORIDAD 03 · Caso 1 «El hospedaje El Mirador».

Mismo metodo del C5U3: por pasos, porque cada llamada al puente tiene un tope
de ~55 s, y cada paso es idempotente -vuelve a correr sin duplicar nada-.

    python montar_p3c1.py medios     importa a la carpeta del caso
    python montar_p3c1.py linea      crea la linea con el mapa de pistas
    python montar_p3c1.py v1         intro + entrada + 31 ranuras + lecho + cierre + outro
    python montar_p3c1.py v3         los cartones tenidos y los de narracion
    python montar_p3c1.py v7         los once lower thirds
    python montar_p3c1.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_p3c1.py chequeo    el chequeo de seis puntos
    python montar_p3c1.py marcas     los dos marcadores H5P y el .drt
    python montar_p3c1.py borrar     borra la linea para rehacerla entera

LO QUE CAMBIO EN LA VERSION 2, QUE ES LA REVISION DE SEBASTIAN
    Las diez losas BLANCAS a cuadro completo se acabaron. El fondo blanco es,
    casi siempre, solo el titulo general de la pieza. De los diez tramos:

        ocho pasaron a CARTON TENIDO en V3, sobre una cama que corre en V1
        por la ranura entera -r01 r04 r07 r10 r15 r18 r27 r29-;

        dos pasaron a GRAFICA DE MOTION a cuadro completo en V1, sin carton
        encima, porque la grafica ES el carton -r20 la linea de tiempo y r31
        el mapa de Colombia con la trayectoria-.

    Y entro la pista que nunca se habia usado: V7 LOWER THIRD, con once
    piezas. Toda fecha que el narrador dice va en pantalla, y cada persona
    que entra al relato lleva su nombre impreso.

LA REGLA DE CONVIVENCIA ENTRE V3 Y V7
    Un lower third y un carton tenido no pueden coincidir: el tenido cubre el
    cuadro con 46 % de azul y los dos juntos se leen como dos cartones. Donde
    la ranura lleva los dos, el lower third va primero, pegado a la cabeza, y
    el carton despues con holgura. Por eso los cartones de narracion ya no se
    centran en su ranura: cada uno trae su propio desplazamiento.

    `n07_comision` desaparecio de V3. Decia «cobro el precio ordinario y la
    comision habitual», que es exactamente un nombre con un dato corto: se
    volvio el lower third de Diana.

LO QUE CAMBIA RESPECTO DEL C5U3
    Las ranuras de placa son .mp4 -las hornea `camara.py`- y las de grafico
    son .mov. El filtro de V1 no puede mirar la extension: mira el prefijo
    `_v`, que es el de las versiones archivadas, y nada mas.

    La musica cubre TAMBIEN el carton de cierre, de OFF_ENTRADA a OFF_OUTRO,
    para que el fundido de 2,5 s caiga sobre el carton y no sobre el ultimo
    cuadro de la votacion.
"""
import os
import sys

import bins

NOM = 'P3C1 EL HOSPEDAJE EL MIRADOR - a la voz v1'
CASO_BIN = ['PRIORIDAD 03', 'CASO 01 - El hospedaje El Mirador']
T0 = 86400                     # arranque de linea, 01:00:00:00 a 23,976

C = 'E:/DAE MASTER/PRIORIDAD 03/CASO 01 - El hospedaje El Mirador'
R = C + '/10 TIMELINE SEBASTIAN/RANURAS'
K = C + '/02 CARTONES'
A = C + '/06 AUDIO'
MU = C + '/08 MUSICA'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_100s.mov'

PISTAS_V = ['VIDEO', 'TINTE', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

N_INTRO, N_BLANCO, N_RANURAS, N_LECHO = 222, 119, 5450, 1016
OFF_ENTRADA = N_INTRO                                  #  222
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #  341
OFF_LECHO = OFF_RANURAS + N_RANURAS                    # 5791
OFF_CIERRE = OFF_LECHO + N_LECHO                       # 6807
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      # 6926
FIN = OFF_OUTRO + N_INTRO                              # 7148

RAN = {}
_o = OFF_RANURAS
for _r, _n in [('r01', 89), ('r02', 229), ('r03', 239), ('r04', 156),
               ('r05', 209), ('r06', 141), ('r07', 105), ('r08', 214),
               ('r09', 109), ('r10', 181), ('r11', 150), ('r12', 224),
               ('r13', 243), ('r14', 109), ('r15', 195), ('r16', 167),
               ('r17', 253), ('r18', 154), ('r19', 195), ('r20', 124),
               ('r21', 152), ('r22', 141), ('r23', 206), ('r24', 210),
               ('r25', 156), ('r26', 104), ('r27', 226), ('r28', 145),
               ('r29', 170), ('r30', 233), ('r31', 221)]:
    RAN[_r] = (_o, _n)
    _o += _n
assert _o == OFF_LECHO, _o

# ------------------------------------------------------------------- V3
# Cartones TENIDOS: ocupan la ranura entera, sobre la cama que corre en V1.
TENIDOS = [('P3C1_ae01_establecidos.mov', 'r01'),
           ('P3C1_ae02_el_acuerdo.mov', 'r04'),
           ('P3C1_ae03_no_todas.mov', 'r07'),
           ('P3C1_ae04_deuda.mov', 'r10'),
           ('P3C1_ae05_paula.mov', 'r15'),
           ('P3C1_ae06_cambio.mov', 'r18'),
           ('P3C1_ae09_interrumpido.mov', 'r27'),
           ('P3C1_ae10_mensajes.mov', 'r29')]

# Cartones de NARRACION: (archivo, ranura, cuadro de entrada en la ranura).
# Ya no se centran: donde la ranura comparte con un lower third, el carton
# entra despues de que el lower third haya salido.
CARTONES = [('P3C1_n01_instagram.mov', 'r03', 120),
            ('P3C1_n02_mesera.mov', 'r08', 112),
            ('P3C1_n03_alimentos.mov', 'r11', 27),
            ('P3C1_n04_tarifa.mov', 'r12', 120),
            ('P3C1_n05_disponible.mov', 'r17', 132),
            ('P3C1_n06_terminal.mov', 'r24', 57),
            ('P3C1_n08_si_pregunto.mov', 'r30', 62)]
PAUSA = ['P3C1_p1a_votacion.mov', 'P3C1_p1b_opciones.mov', 'P3C1_p2_foro.mov']

# ------------------------------------------------------------------- V7
# (archivo, ranura, cuadro de entrada en la ranura). Todos miden 96.
LOWERS = [('P3C1_lt01_fecha_enero_mayo.mov', 'r02', 10),
          ('P3C1_lt02_cristina.mov', 'r03', 8),
          ('P3C1_lt03_victor.mov', 'r05', 24),
          ('P3C1_lt04_daniela.mov', 'r08', 4),
          ('P3C1_lt05_camilo.mov', 'r12', 8),
          ('P3C1_lt06_paula.mov', 'r13', 30),
          ('P3C1_lt07_elena.mov', 'r16', 20),
          ('P3C1_lt08_fecha_diez_mayo.mov', 'r22', 22),
          ('P3C1_lt09_diana.mov', 'r25', 30),
          ('P3C1_lt10_juliana.mov', 'r26', 4),
          ('P3C1_lt11_yeimi.mov', 'r28', 24)]

REAL = {'FGN_intro_version7.mp4': 222, 'MARCA_DE_AGUA_DAE_100s.mov': 2400,
        'P3C1_carton_entrada.mov': 119, 'P3C1_carton_cierre.mov': 119,
        'P3C1_lecho_votacion_v1016.mp4': 1016,
        'P3C1_ae01_establecidos.mov': 89, 'P3C1_ae02_el_acuerdo.mov': 156,
        'P3C1_ae03_no_todas.mov': 105, 'P3C1_ae04_deuda.mov': 181,
        'P3C1_ae05_paula.mov': 195, 'P3C1_ae06_cambio.mov': 154,
        'P3C1_ae09_interrumpido.mov': 226, 'P3C1_ae10_mensajes.mov': 170,
        'P3C1_n01_instagram.mov': 96, 'P3C1_n02_mesera.mov': 96,
        'P3C1_n03_alimentos.mov': 96, 'P3C1_n04_tarifa.mov': 96,
        'P3C1_n05_disponible.mov': 96, 'P3C1_n06_terminal.mov': 96,
        'P3C1_n08_si_pregunto.mov': 109,
        'P3C1_p1a_votacion.mov': 365, 'P3C1_p1b_opciones.mov': 385,
        'P3C1_p2_foro.mov': 266}
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
            if not f.startswith('_v') and 'lecho' not in f
            and f.endswith(('.mov', '.mp4'))]


def medios(mp):
    rutas = [INTRO, MARCA, A + '/P3C1_NARRADOR.wav',
             MU + '/P3C1_MUSICA_cama.flac']
    rutas += [R + '/' + f for f in sorted(os.listdir(R))
              if not f.startswith('_v') and f.endswith(('.mov', '.mp4'))]
    rutas += [K + '/' + f for f in sorted(os.listdir(K))
              if not f.startswith('_v') and f.endswith('.mov')]
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
           ('P3C1_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in _ranuras()]
    sec += [('P3C1_lecho_votacion_v1016.mp4', N_LECHO),
            ('P3C1_carton_cierre.mov', N_BLANCO),
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


def v3(pr, mp):
    tl = _linea(pr)
    if tl.GetItemListInTrack('video', 3):
        print('V3 ya tiene clips, no se toca')
        return
    IT = _clips(mp)
    lote = []
    for nombre, r in TENIDOS:
        ini, largo = RAN[r]
        n = REAL[nombre]
        assert n == largo, (nombre, r, n, largo)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 3, 'recordFrame': T0 + ini})
    for nombre, r, off in CARTONES:
        ini, largo = RAN[r]
        n = REAL[nombre]
        assert 0 <= off and off + n <= largo, (nombre, r, off, n, largo)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 3, 'recordFrame': T0 + ini + off})
    pos = OFF_LECHO
    for nombre in PAUSA:
        n = REAL[nombre]
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 3, 'recordFrame': T0 + pos})
        pos += n
    assert pos == OFF_CIERRE, pos
    mp.AppendToTimeline(lote)
    print('V3 %d cartones (%d tenidos, %d narracion, %d pausa)'
          % (len(tl.GetItemListInTrack('video', 3)), len(TENIDOS),
             len(CARTONES), len(PAUSA)))


def v7(pr, mp):
    tl = _linea(pr)
    if tl.GetItemListInTrack('video', 7):
        print('V7 ya tiene clips, no se toca')
        return
    IT = _clips(mp)
    lote = []
    for nombre, r, off in LOWERS:
        ini, largo = RAN[r]
        n = REAL[nombre]
        assert 0 <= off and off + n <= largo, (nombre, r, off, n, largo)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 7, 'recordFrame': T0 + ini + off})
    mp.AppendToTimeline(lote)
    print('V7 %d lower thirds' % len(tl.GetItemListInTrack('video', 7)))


def pegado(pr, mp):
    tl = _linea(pr)
    IT = _clips(mp)
    lote = []
    if not tl.GetItemListInTrack('video', 5):
        pos, L = OFF_RANURAS, REAL['MARCA_DE_AGUA_DAE_100s.mov']
        while pos < OFF_CIERRE:
            n = min(L, OFF_CIERRE - pos)
            lote.append({'mediaPoolItem': IT['MARCA_DE_AGUA_DAE_100s.mov'],
                         'startFrame': 0, 'endFrame': n, 'trackIndex': 5,
                         'recordFrame': T0 + pos})
            pos += n
    if not tl.GetItemListInTrack('audio', 2):
        lote.append({'mediaPoolItem': IT['P3C1_NARRADOR.wav'], 'startFrame': 0,
                     'endFrame': N_RANURAS, 'trackIndex': 2,
                     'recordFrame': T0 + OFF_RANURAS, 'mediaType': 2})
    if not tl.GetItemListInTrack('audio', 5):
        lote.append({'mediaPoolItem': IT['P3C1_MUSICA_cama.flac'], 'startFrame': 0,
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


def _revisar_pista(tl, pista, cortes, permite_cubrir_ranura):
    """Solapes, duraciones y cruces de corte en una pista de texto."""
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
    print('1) V1 %d clips contiguos, termina en %d' % (len(v), pos))

    malos = []
    for k in ('video', 'audio'):
        for i in range(tl.GetTrackCount(k)):
            for c in tl.GetItemListInTrack(k, i + 1):
                n, d = c.GetName(), c.GetEnd() - c.GetStart()
                if n in REAL and n != 'MARCA_DE_AGUA_DAE_100s.mov' and d != REAL[n]:
                    malos.append((k, i + 1, n, d, REAL[n]))
    print('2) duraciones contra el conteo real:', 'OK' if not malos else malos)
    if malos:
        fallos.append('2: %s' % malos)

    debe_estar_vacia = [('video', 2), ('video', 4), ('video', 6),
                        ('audio', 3), ('audio', 4)]
    ocup = [x for x in debe_estar_vacia if tl.GetItemListInTrack(*x)]
    print('3) V2/V4/V6/A3/A4 vacias:', 'OK' if not ocup else ocup)
    if ocup:
        fallos.append('3: %s' % ocup)

    prob3, p3 = _revisar_pista(tl, 3, cortes, True)
    print('4) cartones V3 (%d):' % len(p3), 'OK' if not prob3 else prob3)
    if prob3:
        fallos.append('4: %s' % prob3)

    prob7, p7 = _revisar_pista(tl, 7, cortes, False)
    # un lower third no puede estar al tiempo que un carton de V3
    pisa = [(n7, n3) for a7, b7, n7 in p7 for a3, b3, n3 in p3
            if a7 < b3 and a3 < b7]
    if pisa:
        prob7 += [('V3 encima', pisa)]
    print('5) lower thirds V7 (%d):' % len(p7), 'OK' if not prob7 else prob7)
    if prob7:
        fallos.append('5: %s' % prob7)

    esp = {('video', 5): (OFF_RANURAS, OFF_CIERRE, 3),
           ('audio', 1): (0, FIN, 2),
           ('audio', 2): (OFF_RANURAS, OFF_LECHO, 1),
           ('audio', 5): (OFF_ENTRADA, OFF_OUTRO, 1)}
    for k, q in esp.items():
        it = tl.GetItemListInTrack(*k)
        g = (it[0].GetStart() - T0, it[-1].GetEnd() - T0, len(it)) if it else None
        print('6) %s%d %s esperado %s %s'
              % (k[0].upper(), k[1], g, q, 'OK' if g == q else 'FALLA'))
        if g != q:
            fallos.append('6: %s%d' % (k[0].upper(), k[1]))

    print('\nFALLOS:', fallos if fallos else 'NINGUNO')
    return not fallos


def marcas(resolve, pr):
    tl = _linea(pr)
    for f, nota in ((OFF_LECHO + REAL['P3C1_p1a_votacion.mov']
                     + REAL['P3C1_p1b_opciones.mov'] - 1, 'H5P votacion'),
                    (OFF_CIERRE - 1, 'H5P foro')):
        print(f, tl.AddMarker(f, 'Cyan', nota, nota, 1))
    d = C + '/10 TIMELINE SEBASTIAN/' + NOM + '.drt'
    print('drt', tl.Export(d, resolve.EXPORT_DRT))


if __name__ == '__main__':
    paso = sys.argv[1] if len(sys.argv) > 1 else 'chequeo'
    resolve, pr, mp = _handles()
    if paso == 'medios':
        medios(mp)
    elif paso == 'borrar':
        borrar(pr, mp)
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
    elif paso == 'marcas':
        marcas(resolve, pr)
    else:
        print('paso desconocido:', paso)
