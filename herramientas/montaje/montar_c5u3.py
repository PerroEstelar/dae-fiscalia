#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del C5U3 «Eslabon Financiero» sobre la API de Resolve.

Se ejecuta por pasos desde el puente, porque cada llamada al puente tiene un
tope de ~55 s. Cada paso es idempotente: vuelve a correr sin duplicar nada.

    python montar_c5u3.py medios     importa a la carpeta del caso
    python montar_c5u3.py linea      crea la linea con el mapa de pistas
    python montar_c5u3.py v1         intro + entrada + 21 ranuras + lecho + cierre + outro
    python montar_c5u3.py v3         los 16 cartones, centrados en su ranura
    python montar_c5u3.py pegado     V5 marca de agua, A2 narrador, A5 musica
    python montar_c5u3.py chequeo    el chequeo de cinco puntos
    python montar_c5u3.py marcas     los dos marcadores H5P y el .drt

POR QUE EL CHEQUEO NO VUELVE A LLAMAR A ffprobe
    `ffprobe -count_frames` sobre los 26 clips de V1 se pasa del tope del
    puente: el lecho solo pesa 181 MB. Los conteos se miden UNA vez al
    hornear, se guardan en REAL, y el chequeo compara la linea contra esa
    tabla. Sigue siendo verificacion contra algo externo a la linea: la tabla
    salio del archivo, no de la aritmetica de GetEnd().
"""
import os
import sys

NOM = 'C5U3 ESLABON FINANCIERO - a la voz'
CARPETA = 'C5U3 ESLABON FINANCIERO'
T0 = 86400                     # arranque de linea, 01:00:00:00 a 23,976

C = ('E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/UNIDAD 3/'
     'CASO 03 - eslabon financiero')
R = C + '/10 TIMELINE SEBASTIAN/RANURAS'
K = C + '/02 CARTONES'
A = C + '/06 AUDIO'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_100s.mov'

PISTAS_V = ['VIDEO', 'TINTE', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

N_INTRO, N_BLANCO, N_RANURAS, N_LECHO = 222, 119, 3675, 1292
OFF_ENTRADA = N_INTRO                                  #  222
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #  341
OFF_LECHO = OFF_RANURAS + N_RANURAS                    # 4016
OFF_CIERRE = OFF_LECHO + N_LECHO                       # 5308
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      # 5427
FIN = OFF_OUTRO + N_INTRO                              # 5649

# ranura -> (offset absoluto en la linea, cuadros)
RAN = {}
_o = OFF_RANURAS
for _r, _n in [('r01', 173), ('r02', 181), ('r03', 207), ('r04', 193),
               ('r05', 182), ('r06', 146), ('r07', 188), ('r08', 187),
               ('r09', 161), ('r10', 207), ('r11', 115), ('r12', 238),
               ('r13', 144), ('r14', 174), ('r15', 186), ('r16', 123),
               ('r17', 202), ('r18', 165), ('r19', 151), ('r20', 193),
               ('r21', 159)]:
    RAN[_r] = (_o, _n)
    _o += _n
assert _o == OFF_LECHO

# cartones de narracion: SOLO sobre ranuras de foto, nunca sobre piezas de AE
CARTONES = [('C5U3_n01_investigacion.mov', 'r01'),
            ('C5U3_n02_allanamiento.mov', 'r04'),
            ('C5U3_n03_diligencia.mov', 'r06'),
            ('C5U3_n04_vehiculos.mov', 'r07'),
            ('C5U3_n05_instrumentos.mov', 'r08'),
            ('C5U3_n06_bodega.mov', 'r09'),
            ('C5U3_n07_repuestos.mov', 'r10'),
            ('C5U3_n08_servidores.mov', 'r12'),
            ('C5U3_n09_efectivo.mov', 'r14'),
            ('C5U3_n10_contabilidad.mov', 'r15'),
            ('C5U3_n11_apartamentos.mov', 'r17'),
            ('C5U3_n12_disponer.mov', 'r18'),
            ('C5U3_n13_valor.mov', 'r20')]
PAUSA = ['C5U3_p1a_votacion.mov', 'C5U3_p1b_opciones.mov', 'C5U3_p2_foro.mov']

# cuadros REALES, medidos con `ffprobe -count_frames` al hornear
REAL = {'FGN_intro_version7.mp4': 222, 'MARCA_DE_AGUA_DAE_100s.mov': 2400,
        'C5U3_carton_entrada.mov': 119, 'C5U3_carton_cierre.mov': 119,
        'C5U3_lecho_votacion_v1292.mov': 1292,
        'C5U3_n01_investigacion.mov': 96, 'C5U3_n02_allanamiento.mov': 96,
        'C5U3_n03_diligencia.mov': 96, 'C5U3_n04_vehiculos.mov': 99,
        'C5U3_n05_instrumentos.mov': 96, 'C5U3_n06_bodega.mov': 96,
        'C5U3_n07_repuestos.mov': 148, 'C5U3_n08_servidores.mov': 109,
        'C5U3_n09_efectivo.mov': 99, 'C5U3_n10_contabilidad.mov': 119,
        'C5U3_n11_apartamentos.mov': 99, 'C5U3_n12_disponer.mov': 96,
        'C5U3_n13_valor.mov': 158, 'C5U3_p1a_votacion.mov': 434,
        'C5U3_p1b_opciones.mov': 513, 'C5U3_p2_foro.mov': 345}


def _handles():
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    return resolve, pr, pr.GetMediaPool()


def _carpeta(mp):
    raiz = mp.GetRootFolder()
    for f in raiz.GetSubFolderList():
        if f.GetName() == CARPETA:
            return f
    return mp.AddSubFolder(raiz, CARPETA)


def _clips(mp):
    return {c.GetName(): c for c in _carpeta(mp).GetClipList()}


def _linea(pr):
    for i in range(pr.GetTimelineCount()):
        t = pr.GetTimelineByIndex(i + 1)
        if t.GetName() == NOM:
            return t
    return None


def medios(mp):
    rutas = [INTRO, MARCA, A + '/C5U3_NARRADOR.wav', A + '/C5U3_MUSICA_cama.wav']
    rutas += [R + '/' + f for f in sorted(os.listdir(R))]
    rutas += [K + '/' + f for f in sorted(os.listdir(K))]
    mp.SetCurrentFolder(_carpeta(mp))
    mp.ImportMedia(rutas)
    hay = _clips(mp)
    faltan = [os.path.basename(x) for x in rutas if os.path.basename(x) not in hay]
    print('en carpeta %d; faltan %s' % (len(hay), faltan or 'ninguno'))


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
           ('C5U3_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in ran]
    sec += [('C5U3_lecho_votacion_v1292.mov', N_LECHO),
            ('C5U3_carton_cierre.mov', N_BLANCO),
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
        lote.append({'mediaPoolItem': IT['C5U3_NARRADOR.wav'], 'startFrame': 0,
                     'endFrame': N_RANURAS, 'trackIndex': 2,
                     'recordFrame': T0 + OFF_RANURAS, 'mediaType': 2})
    if not tl.GetItemListInTrack('audio', 5):
        lote.append({'mediaPoolItem': IT['C5U3_MUSICA_cama.wav'], 'startFrame': 0,
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
    for f, nota in ((OFF_LECHO + REAL['C5U3_p1a_votacion.mov']
                     + REAL['C5U3_p1b_opciones.mov'] - 1, 'H5P votacion'),
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
