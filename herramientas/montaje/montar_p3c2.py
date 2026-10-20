#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del PRIORIDAD 03 · Caso 2 «El taller del segundo piso».

    python montar_p3c2.py medios     importa a la carpeta del caso
    python montar_p3c2.py linea      crea la linea con el mapa de pistas
    python montar_p3c2.py v1         intro + entrada + 28 ranuras + lecho + cierre + outro
    python montar_p3c2.py v2         la capa de movimiento, que se puede apagar
    python montar_p3c2.py v3         los cartones tenidos y los de narracion
    python montar_p3c2.py v7         los seis lower thirds
    python montar_p3c2.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_p3c2.py chequeo    el chequeo de seis puntos
    python montar_p3c2.py marcas     los dos marcadores H5P y el .drt
    python montar_p3c2.py borrar     borra la linea para rehacerla entera

LO QUE CAMBIO EN LA VERSION 2
    La mitad de la pieza era losa blanca: catorce de veintiocho ranuras, con
    tramos de dos y tres seguidas. Se repartieron asi:

        dos a GRAFICA DE MOTION a cuadro completo, sin carton encima
            r03 la fila de seis que se abre en 2 y 4
            r26 las cinco decisiones renglon a renglon
        uno a LOWER THIRD
            r19, que era Elisa y su edad: un nombre con un dato corto
        once a CARTON TENIDO sobre una cama que corre en V1 la ranura entera

    Y tres cartones de narracion -n01 la fecha, n04 Mara, n07 Dario- tambien
    eran nombres con un dato corto y se mudaron a V7. `n02` desaparecio: decia
    lo mismo que la grafica de r03, que va justo antes.

LAS CUATRO PROPUESTAS, Y SU CAMA
    `ae05`, `ae07`, `ae08` y `ae11` son las propuestas equivocadas que el caso
    cita literales. La regla es que no caigan nunca sobre una cara, para no
    atribuirle a la persona en cuadro lo que propone otro. La cumplen: van
    sobre camas del mundo INSTITUCIONAL -la mesa del equipo en cenital, el
    informe y el esfero, el pasillo, la sala de entrevista-. Cada vez que
    aparece una mala propuesta, la pieza se va a la oficina y no al taller.

LA REGLA DE CONVIVENCIA ENTRE V3 Y V7
    Un tenido cubre el cuadro con 46 % de azul; un lower third encima se lee
    como dos cartones. Donde la ranura lleva los dos -solo r12- el lower third
    va primero y el carton despues con holgura. Por eso los cartones de
    narracion ya no se centran: cada uno trae su desplazamiento.
"""
import os
import sys

import bins

NOM = 'P3C2 EL TALLER DEL SEGUNDO PISO - a la voz v1'
CASO_BIN = ['PRIORIDAD 03', 'CASO 02 - El taller del segundo piso']
T0 = 86400

C = 'E:/DAE MASTER/PRIORIDAD 03/CASO 02 - El taller del segundo piso'
R = C + '/10 TIMELINE SEBASTIAN/RANURAS'
K = C + '/02 CARTONES'
MV = C + '/07 MOVIMIENTO/CAPA V2'
A = C + '/06 AUDIO'
MU = C + '/08 MUSICA'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_100s.mov'

# V2 se llama MOVIMIENTO en esta serie, no TINTE: lleva la capa opcional de
# clips animados, encima de la placa quieta y debajo de los cartones.
PISTAS_V = ['VIDEO', 'MOVIMIENTO', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

N_INTRO, N_BLANCO, N_RANURAS, N_LECHO = 222, 119, 5352, 1055
OFF_ENTRADA = N_INTRO                                  #  222
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #  341
OFF_LECHO = OFF_RANURAS + N_RANURAS                    # 5693
OFF_CIERRE = OFF_LECHO + N_LECHO                       # 6748
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      # 6867
FIN = OFF_OUTRO + N_INTRO                              # 7089

RAN = {}
_o = OFF_RANURAS
for _r, _n in [('r01', 165), ('r02', 263), ('r03', 217), ('r04', 238),
               ('r05', 154), ('r06', 140), ('r07', 180), ('r08', 130),
               ('r09', 203), ('r10', 185), ('r11', 213), ('r12', 287),
               ('r13', 167), ('r14', 138), ('r15', 267), ('r16', 127),
               ('r17', 212), ('r18', 168), ('r19', 157), ('r20', 157),
               ('r21', 224), ('r22', 163), ('r23', 164), ('r24', 255),
               ('r25', 198), ('r26', 215), ('r27', 138), ('r28', 227)]:
    RAN[_r] = (_o, _n)
    _o += _n
assert _o == OFF_LECHO, _o

# ------------------------------------------------------------------- V2
# Cada clip cubre su ranura ENTERA: apagar la pista devuelve la pieza a su
# version de placas sostenidas, sin huecos ni saltos de encuadre.
IDLE = [('P3C2_r06_idle_mara_cu_v140.mp4', 'r06'),
        ('P3C2_r09_idle_mara_entera_v203.mp4', 'r09'),
        ('P3C2_r10_idle_maquinas_v185.mp4', 'r10'),
        ('P3C2_r12_idle_samuel_cu_v287.mp4', 'r12'),
        ('P3C2_r14_idle_dario_v138.mp4', 'r14'),
        ('P3C2_r15_idle_samuel_aparte_v267.mp4', 'r15'),
        ('P3C2_r16_idle_informe_v127.mp4', 'r16'),
        ('P3C2_r18_idle_elisa_entera_v168.mp4', 'r18'),
        ('P3C2_r19_idle_escalera_v157.mp4', 'r19'),
        ('P3C2_r22_idle_elisa_cu_v163.mp4', 'r22'),
        ('P3C2_r23_idle_patricia_cu_v164.mp4', 'r23'),
        ('P3C2_r24_idle_mensajes_v255.mp4', 'r24')]

# ------------------------------------------------------------------- V3
TENIDOS = [('P3C2_ae01_primer_contacto.mov', 'r01'),
           ('P3C2_ae03_pasaporte.mov', 'r07'),
           ('P3C2_ae04_pide.mov', 'r10'),
           ('P3C2_ae05_la_propuesta.mov', 'r11'),        # propuesta
           ('P3C2_ae06_lo_que_vio.mov', 'r13'),
           ('P3C2_ae07_suplir.mov', 'r16'),              # propuesta
           ('P3C2_ae08_descartarse.mov', 'r17'),         # propuesta
           ('P3C2_ae10_ya_escuchada.mov', 'r20'),
           ('P3C2_ae11_repetir.mov', 'r21'),             # propuesta
           ('P3C2_ae12_no_verificado.mov', 'r25'),
           ('P3C2_ae14_hipotesis.mov', 'r28')]

# (archivo, ranura, cuadro de entrada en la ranura)
CARTONES = [('P3C2_n03_candados.mov', 'r05', 29),
            ('P3C2_n05_domingos.mov', 'r09', 53),
            ('P3C2_n06_senas.mov', 'r12', 120),
            ('P3C2_n08_por_separado.mov', 'r15', 84),
            ('P3C2_n09_delante.mov', 'r22', 33),
            ('P3C2_n10_amenaza.mov', 'r24', 43),
            ('P3C2_n11_sin_riesgos.mov', 'r27', 21)]
PAUSA = ['P3C2_p1a_votacion.mov', 'P3C2_p1b_opciones.mov', 'P3C2_p2_foro.mov']

# ------------------------------------------------------------------- V7
LOWERS = [('P3C2_lt01_fecha_cucuta.mov', 'r02', 12),
          ('P3C2_lt02_mara.mov', 'r06', 10),
          ('P3C2_lt03_samuel.mov', 'r12', 8),
          ('P3C2_lt04_dario.mov', 'r14', 8),
          ('P3C2_lt05_elisa.mov', 'r19', 28),
          ('P3C2_lt06_patricia.mov', 'r23', 30)]

REAL = {'FGN_intro_version7.mp4': 222, 'MARCA_DE_AGUA_DAE_100s.mov': 2400,
        'P3C2_carton_entrada.mov': 119, 'P3C2_carton_cierre.mov': 119,
        'P3C2_lecho_votacion_v1055.mp4': 1055,
        'P3C2_n03_candados.mov': 96, 'P3C2_n05_domingos.mov': 96,
        'P3C2_n06_senas.mov': 138, 'P3C2_n08_por_separado.mov': 99,
        'P3C2_n09_delante.mov': 96, 'P3C2_n10_amenaza.mov': 168,
        'P3C2_n11_sin_riesgos.mov': 96,
        'P3C2_p1a_votacion.mov': 375, 'P3C2_p1b_opciones.mov': 394,
        'P3C2_p2_foro.mov': 286}
REAL.update({f: RAN[r][1] for f, r in TENIDOS})
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
            if not f.startswith('_v') and 'lecho' not in f
            and f.endswith(('.mov', '.mp4'))]


def medios(mp):
    rutas = [INTRO, MARCA, A + '/P3C2_NARRADOR.wav',
             MU + '/P3C2_MUSICA_cama.wav']
    rutas += [R + '/' + f for f in sorted(os.listdir(R))
              if not f.startswith('_v') and f.endswith(('.mov', '.mp4'))]
    rutas += [K + '/' + f for f in sorted(os.listdir(K))
              if not f.startswith('_v') and f.endswith('.mov')]
    rutas += [MV + '/' + f for f in sorted(os.listdir(MV))
              if not f.startswith('_v') and f.endswith('.mp4')]
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
           ('P3C2_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in _ranuras()]
    sec += [('P3C2_lecho_votacion_v1055.mp4', N_LECHO),
            ('P3C2_carton_cierre.mov', N_BLANCO),
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


def v2(pr, mp):
    tl = _linea(pr)
    if tl.GetItemListInTrack('video', 2):
        print('V2 ya tiene clips, no se toca')
        return
    IT = _clips(mp)
    lote = []
    for nombre, r in IDLE:
        ini, largo = RAN[r]
        n = REAL[nombre]
        assert n == largo, (nombre, r, n, largo)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 2, 'recordFrame': T0 + ini})
    mp.AppendToTimeline(lote)
    print('V2 %d clips de movimiento' % len(tl.GetItemListInTrack('video', 2)))


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
        lote.append({'mediaPoolItem': IT['P3C2_NARRADOR.wav'], 'startFrame': 0,
                     'endFrame': N_RANURAS, 'trackIndex': 2,
                     'recordFrame': T0 + OFF_RANURAS, 'mediaType': 2})
    if not tl.GetItemListInTrack('audio', 5):
        lote.append({'mediaPoolItem': IT['P3C2_MUSICA_cama.wav'], 'startFrame': 0,
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

    debe_estar_vacia = [('video', 4), ('video', 6), ('audio', 3), ('audio', 4)]
    ocup = [x for x in debe_estar_vacia if tl.GetItemListInTrack(*x)]
    print('3) V4/V6/A3/A4 vacias:', 'OK' if not ocup else ocup)
    if ocup:
        fallos.append('3: %s' % ocup)

    prob2 = []
    for nombre, r in IDLE:
        ini, largo = RAN[r]
        hay = [c for c in tl.GetItemListInTrack('video', 2)
               if c.GetName() == nombre]
        if len(hay) != 1:
            prob2.append((nombre, 'aparece %d veces' % len(hay)))
            continue
        c = hay[0]
        if (c.GetStart() - T0, c.GetEnd() - T0) != (ini, ini + largo):
            prob2.append((nombre, 'va en %d-%d, deberia %d-%d'
                          % (c.GetStart() - T0, c.GetEnd() - T0, ini, ini + largo)))
    n2 = len(tl.GetItemListInTrack('video', 2))
    if n2 != len(IDLE):
        prob2.append(('V2', '%d clips, deberian %d' % (n2, len(IDLE))))
    print('3b) capa de movimiento V2 (%d):' % n2, 'OK' if not prob2 else prob2)
    if prob2:
        fallos.append('3b: %s' % prob2)

    prob3, p3 = _revisar_pista(tl, 3, cortes)
    print('4) cartones V3 (%d):' % len(p3), 'OK' if not prob3 else prob3)
    if prob3:
        fallos.append('4: %s' % prob3)

    prob7, p7 = _revisar_pista(tl, 7, cortes)
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
    for f, nota in ((OFF_LECHO + REAL['P3C2_p1a_votacion.mov']
                     + REAL['P3C2_p1b_opciones.mov'] - 1, 'H5P votacion'),
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
    elif paso == 'marcas':
        marcas(resolve, pr)
    else:
        print('paso desconocido:', paso)
