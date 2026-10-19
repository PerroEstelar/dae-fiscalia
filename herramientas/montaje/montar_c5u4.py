#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del C5U4 «Los Ilustres» sobre la API de Resolve.

Se ejecuta por pasos desde el puente, porque cada llamada tiene un tope de
~55 s. Cada paso es idempotente: vuelve a correr sin duplicar nada.

    python montar_c5u4.py medios     importa a la carpeta del caso
    python montar_c5u4.py linea      crea la linea con el mapa de pistas
    python montar_c5u4.py v1         intro + entrada + 23 ranuras + lecho + cierre + outro
    python montar_c5u4.py v3         los 18 cartones, centrados en su ranura
    python montar_c5u4.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_c5u4.py chequeo    el chequeo de cinco puntos
    python montar_c5u4.py marcas     los dos marcadores H5P y el .drt

POR QUE EL CHEQUEO NO VUELVE A LLAMAR A ffprobe
    `ffprobe -count_frames` sobre los 28 clips de V1 se pasa del tope del
    puente. Los conteos se miden UNA vez al hornear, se guardan en REAL, y el
    chequeo compara la linea contra esa tabla. Sigue siendo verificacion
    contra algo externo a la linea: la tabla salio del archivo, no de la
    aritmetica de GetEnd().
"""
import os
import sys

import bins

NOM = 'C5U4 LOS ILUSTRES - a la voz'
CASO_BIN = ['C5 BIENES EN EL PROCESO PENAL', 'U4',
            'CASO 04 - los ilustres']
T0 = 86400                     # arranque de linea, 01:00:00:00 a 23,976

C = ('E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/UNIDAD 4/'
     'CASO 04 - los ilustres')
R = C + '/10 TIMELINE SEBASTIAN/RANURAS'
K = C + '/02 CARTONES'
A = C + '/06 AUDIO'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_100s.mov'

PISTAS_V = ['VIDEO', 'TINTE', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

N_INTRO, N_BLANCO, N_RANURAS, N_LECHO = 222, 119, 3826, 1183
OFF_ENTRADA = N_INTRO                                  #  222
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #  341
OFF_LECHO = OFF_RANURAS + N_RANURAS                    # 4167
OFF_CIERRE = OFF_LECHO + N_LECHO                       # 5350
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      # 5469
FIN = OFF_OUTRO + N_INTRO                              # 5691

# ranura -> (offset absoluto en la linea, cuadros)
RAN = {}
_o = OFF_RANURAS
for _r, _n in [('r01', 131), ('r02', 199), ('r03', 201), ('r04', 122),
               ('r05', 239), ('r06', 208), ('r07', 212), ('r08', 210),
               ('r09', 150), ('r10', 231), ('r11', 183), ('r12', 139),
               ('r13', 121), ('r14', 151), ('r15', 159), ('r16', 152),
               ('r17', 163), ('r18', 168), ('r19', 114), ('r20', 156),
               ('r21', 163), ('r22', 138), ('r23', 116)]:
    RAN[_r] = (_o, _n)
    _o += _n
assert _o == OFF_LECHO, _o

# Cartones de narracion: SOLO sobre ranuras de FOTO. De las 23 ranuras, 8 son
# piezas de After Effects (r02 r05 r07 r10 r16 r20 r21 r23) y no llevan carton
# encima: ya son grafica.
CARTONES = [('C5U4_n01_direccion.mov', 'r01'),
            ('C5U4_n02_lavado.mov', 'r03'),
            ('C5U4_n03_medidas.mov', 'r04'),
            ('C5U4_n04_comerciante.mov', 'r06'),
            ('C5U4_n05_buena_fe.mov', 'r08'),
            ('C5U4_n06_setenta.mov', 'r09'),
            ('C5U4_n07_empleos.mov', 'r11'),
            ('C5U4_n08_hectareas.mov', 'r12'),
            ('C5U4_n09_titular.mov', 'r13'),
            ('C5U4_n10_sucesion.mov', 'r14'),
            ('C5U4_n11_urgencia.mov', 'r15'),
            ('C5U4_n12_legalidad.mov', 'r17'),
            ('C5U4_n13_colaboracion.mov', 'r18'),
            ('C5U4_n14_testaferrato.mov', 'r19'),
            ('C5U4_n15_oferta.mov', 'r22')]
PAUSA = ['C5U4_p1a_votacion.mov', 'C5U4_p1b_opciones.mov', 'C5U4_p2_foro.mov']

# cuadros REALES, medidos con `ffprobe -count_frames` al hornear
REAL = {'FGN_intro_version7.mp4': 222, 'MARCA_DE_AGUA_DAE_100s.mov': 2400,
        'C5U4_carton_entrada.mov': 119, 'C5U4_carton_cierre.mov': 119,
        'C5U4_lecho_votacion_v1183.mov': 1183,
        'C5U4_n01_direccion.mov': 96, 'C5U4_n02_lavado.mov': 119,
        'C5U4_n03_medidas.mov': 96, 'C5U4_n04_comerciante.mov': 109,
        'C5U4_n05_buena_fe.mov': 129, 'C5U4_n06_setenta.mov': 99,
        'C5U4_n07_empleos.mov': 99, 'C5U4_n08_hectareas.mov': 96,
        'C5U4_n09_titular.mov': 96, 'C5U4_n10_sucesion.mov': 96,
        'C5U4_n11_urgencia.mov': 119, 'C5U4_n12_legalidad.mov': 99,
        'C5U4_n13_colaboracion.mov': 129, 'C5U4_n14_testaferrato.mov': 96,
        'C5U4_n15_oferta.mov': 96, 'C5U4_p1a_votacion.mov': 414,
        'C5U4_p1b_opciones.mov': 493, 'C5U4_p2_foro.mov': 276}


def _handles():
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    return resolve, pr, pr.GetMediaPool()


def _carpeta(mp):
    """La raiz del caso en el media pool. Ahi va la linea de tiempo."""
    return bins.carpeta(mp, CASO_BIN)


def _clips(mp):
    """Los medios del caso, por nombre, de todo el subarbol."""
    return bins.clips(mp, CASO_BIN)


def _linea(pr):
    for i in range(pr.GetTimelineCount()):
        t = pr.GetTimelineByIndex(i + 1)
        if t.GetName() == NOM:
            return t
    return None


def medios(mp):
    rutas = [INTRO, MARCA, A + '/C5U4_NARRADOR.wav', A + '/C5U4_MUSICA_cama.wav']
    rutas += [R + '/' + f for f in sorted(os.listdir(R))
              if f.endswith('.mov') and not f.startswith('_v')]
    rutas += [K + '/' + f for f in sorted(os.listdir(K))
              if f.endswith('.mov') and not f.startswith('_v')]
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
    ran = [f for f in sorted(os.listdir(R)) if 'lecho' not in f]
    sec = [('FGN_intro_version7.mp4', N_INTRO),
           ('C5U4_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in ran]
    sec += [('C5U4_lecho_votacion_v1183.mov', N_LECHO),
            ('C5U4_carton_cierre.mov', N_BLANCO),
            ('FGN_intro_version7.mp4', N_INTRO)]
    # endFrame es EXCLUSIVO en AppendToTimeline: se pasa la duracion completa
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
    for nombre, r in CARTONES:                  # centrado, margen a lado y lado
        ini, largo = RAN[r]
        n = REAL[nombre]
        pos = ini + (largo - n) // 2
        assert ini <= pos and pos + n <= ini + largo, (nombre, r)
        lote.append({'mediaPoolItem': IT[nombre], 'startFrame': 0, 'endFrame': n,
                     'trackIndex': 3, 'recordFrame': T0 + pos})
    pos = OFF_LECHO                             # los de pausa van seguidos
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
    if not tl.GetItemListInTrack('video', 5):   # marca de agua, repetida a cubrir
        pos, L = OFF_RANURAS, REAL['MARCA_DE_AGUA_DAE_100s.mov']
        while pos < OFF_CIERRE:
            n = min(L, OFF_CIERRE - pos)
            lote.append({'mediaPoolItem': IT['MARCA_DE_AGUA_DAE_100s.mov'],
                         'startFrame': 0, 'endFrame': n, 'trackIndex': 5,
                         'recordFrame': T0 + pos})
            pos += n
    if not tl.GetItemListInTrack('audio', 2):
        lote.append({'mediaPoolItem': IT['C5U4_NARRADOR.wav'], 'startFrame': 0,
                     'endFrame': N_RANURAS, 'trackIndex': 2,
                     'recordFrame': T0 + OFF_RANURAS, 'mediaType': 2})
    if not tl.GetItemListInTrack('audio', 5):
        lote.append({'mediaPoolItem': IT['C5U4_MUSICA_cama.wav'], 'startFrame': 0,
                     'endFrame': OFF_CIERRE - OFF_ENTRADA, 'trackIndex': 5,
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
    """Los cinco puntos. Cualquier desviacion sale en FALLOS."""
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
           ('audio', 5): (OFF_ENTRADA, OFF_CIERRE, 1)}
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
    for f, nota in ((OFF_LECHO + REAL['C5U4_p1a_votacion.mov']
                     + REAL['C5U4_p1b_opciones.mov'] - 1, 'H5P votacion'),
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
        chequeo(pr)
    elif paso == 'marcas':
        marcas(resolve, pr)
    else:
        raise SystemExit('paso desconocido: %s' % paso)
