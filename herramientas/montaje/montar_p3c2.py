#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del PRIORIDAD 03 · Caso 2 «El taller del segundo piso».

Mismo metodo del C5U3: por pasos, porque cada llamada al puente tiene un tope
de ~55 s, y cada paso es idempotente -vuelve a correr sin duplicar nada-.

    python montar_p3c1.py medios     importa a la carpeta del caso
    python montar_p3c1.py linea      crea la linea con el mapa de pistas
    python montar_p3c1.py v1         intro + entrada + 31 ranuras + lecho + cierre + outro
    python montar_p3c1.py v3         los 8 cartones de narracion + los 3 de pausa
    python montar_p3c1.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_p3c1.py chequeo    el chequeo de cinco puntos
    python montar_p3c1.py marcas     los dos marcadores H5P y el .drt

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

NOM = 'P3C2 EL TALLER DEL SEGUNDO PISO - a la voz v1'
CASO_BIN = ['PRIORIDAD 03', 'CASO 02 - El taller del segundo piso']
T0 = 86400                     # arranque de linea, 01:00:00:00 a 23,976

C = 'E:/DAE MASTER/PRIORIDAD 03/CASO 02 - El taller del segundo piso'
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

# cartones de narracion: SOLO sobre ranuras de placa, nunca sobre un grafico,
# que ya es texto.
CARTONES = [('P3C2_n01_cucuta.mov', 'r02'),
            ('P3C2_n02_seis.mov', 'r04'),
            ('P3C2_n03_candados.mov', 'r05'),
            ('P3C2_n04_mara.mov', 'r06'),
            ('P3C2_n05_domingos.mov', 'r09'),
            ('P3C2_n06_senas.mov', 'r12'),
            ('P3C2_n07_dario.mov', 'r14'),
            ('P3C2_n08_por_separado.mov', 'r15'),
            ('P3C2_n09_delante.mov', 'r22'),
            ('P3C2_n10_amenaza.mov', 'r24'),
            ('P3C2_n11_sin_riesgos.mov', 'r27')]
PAUSA = ['P3C2_p1a_votacion.mov', 'P3C2_p1b_opciones.mov', 'P3C2_p2_foro.mov']

REAL = {'FGN_intro_version7.mp4': 222, 'MARCA_DE_AGUA_DAE_100s.mov': 2400,
        'P3C2_carton_entrada.mov': 119, 'P3C2_carton_cierre.mov': 119,
        'P3C2_lecho_votacion_v1055.mp4': 1055,
        'P3C2_n01_cucuta.mov': 96, 'P3C2_n02_seis.mov': 96,
        'P3C2_n03_candados.mov': 96, 'P3C2_n04_mara.mov': 96,
        'P3C2_n05_domingos.mov': 96, 'P3C2_n06_senas.mov': 138,
        'P3C2_n07_dario.mov': 96, 'P3C2_n08_por_separado.mov': 99,
        'P3C2_n09_delante.mov': 96, 'P3C2_n10_amenaza.mov': 168,
        'P3C2_n11_sin_riesgos.mov': 96,
        'P3C2_p1a_votacion.mov': 375, 'P3C2_p1b_opciones.mov': 394,
        'P3C2_p2_foro.mov': 286}


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
    bins.importar(mp, CASO_BIN, rutas)


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


def v3(pr, mp):
    tl = _linea(pr)
    if tl.GetItemListInTrack('video', 3):
        print('V3 ya tiene clips, no se toca')
        return
    IT = _clips(mp)
    lote = []
    for nombre, r in CARTONES:
        ini, largo = RAN[r]
        n = REAL[nombre]
        pos = ini + (largo - n) // 2
        assert ini <= pos and pos + n <= ini + largo, (nombre, r)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 3, 'recordFrame': T0 + pos})
    pos = OFF_LECHO
    for nombre in PAUSA:
        n = REAL[nombre]
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 3, 'recordFrame': T0 + pos})
        pos += n
    assert pos == OFF_CIERRE, pos
    mp.AppendToTimeline(lote)
    print('V3 %d cartones' % len(tl.GetItemListInTrack('video', 3)))


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

    debe_estar_vacia = [('video', 2), ('video', 4), ('video', 6), ('video', 7),
                        ('audio', 3), ('audio', 4)]
    ocup = [x for x in debe_estar_vacia if tl.GetItemListInTrack(*x)]
    print('3) V2/V4/V6/V7/A3/A4 vacias:', 'OK' if not ocup else ocup)
    if ocup:
        fallos.append('3: %s' % ocup)

    prob, ant = [], 0
    for c in sorted(tl.GetItemListInTrack('video', 3), key=lambda x: x.GetStart()):
        a, b, n = c.GetStart() - T0, c.GetEnd() - T0, c.GetName()
        if a < ant:
            prob.append((n, 'solape'))
        ant = b
        if b - a != REAL[n]:
            prob.append((n, 'recortado %d de %d' % (b - a, REAL[n])))
        cruza = [x for x in cortes if a < x < b]
        if cruza:
            prob.append((n, 'cruza corte en %s' % cruza))
    print('4) cartones:', 'OK' if not prob else prob)
    if prob:
        fallos.append('4: %s' % prob)

    esp = {('video', 5): (OFF_RANURAS, OFF_CIERRE, 3),
           ('audio', 1): (0, FIN, 2),
           ('audio', 2): (OFF_RANURAS, OFF_LECHO, 1),
           ('audio', 5): (OFF_ENTRADA, OFF_OUTRO, 1)}
    for k, q in esp.items():
        it = tl.GetItemListInTrack(*k)
        g = (it[0].GetStart() - T0, it[-1].GetEnd() - T0, len(it)) if it else None
        print('5) %s%d %s esperado %s %s'
              % (k[0].upper(), k[1], g, q, 'OK' if g == q else 'FALLA'))
        if g != q:
            fallos.append('5: %s%d' % (k[0].upper(), k[1]))

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
    elif paso == 'linea':
        linea(pr, mp)
    elif paso == 'v1':
        v1(pr, mp)
    elif paso == 'v3':
        v3(pr, mp)
    elif paso == 'pegado':
        pegado(pr, mp)
    elif paso == 'chequeo':
        sys.exit(0 if chequeo(pr) else 1)
    elif paso == 'marcas':
        marcas(resolve, pr)
    else:
        print('paso desconocido:', paso)
