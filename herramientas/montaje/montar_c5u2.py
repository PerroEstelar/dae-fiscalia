#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaje del C5U2 «El siniestro vial» sobre la API de Resolve.

Escrito al rehacer el bloque 4 (el avaluo del 1:14). La version original se
monto a mano; esto deja el montaje reproducible, por pasos e idempotente,
igual que el del C5U3 y el C5U4.

    python montar_c5u2.py medios | linea | v1 | v3 | pegado | chequeo | marcas

QUE CAMBIO EN LA v2
    Solo el bloque 4. Se reescribio la locucion porque «Avalulo: novecientos
    millones» -dos puntos, sin verbo- no fluia en ElevenLabs, y porque «por
    ciento ochenta millones» se podia leer como un porcentaje. Ahora los dos
    bienes van «avaluada en tanto». Con eso b4 paso de 29,40 a 30,05 s y sus
    tres ranuras de 257/174/292 a 314/175/325.

    La velocidad se decidio midiendo, no a oido: el ritmo de HABLA -palabras
    por minuto descontando las pausas- de los siete bloques que no se tocaron
    es 178; el b4 original iba a 164, deliberadamente mas lento porque es el
    inventario y hay tres bienes y tres cifras que absorber. A 0,92 el bloque
    nuevo daba 176 y perdia esa calma; a 0,88 da 161, que es el del original.

    Los otros bloques no se regrabaron. Dos ranuras suyas se movian un cuadro
    -kf09_flota +1, ae11_reloj -1-, pero eso es ruido de cuantizacion del
    detector de silencios (ventana de 0,05 s) al desplazarse todo 3,1 s, no un
    cambio real: se fijan a su largo original y el cuadro lo absorbe el vecino
    del mismo bloque (ae10_patrimonios 239->240, kf12_llaves 149->148).
"""
import os
import sys

import bins

NOM = 'C5U2 SINIESTRO VIAL - a la voz v2'
CASO_BIN = ['C5 BIENES EN EL PROCESO PENAL', 'U2',
            'CASO 02 - el siniestro vial']
T0 = 86400

C = ('E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/UNIDAD 2/'
     'CASO 02 - el siniestro vial')
R = C + '/10 TIMELINE SEBASTIAN/RANURAS'
K = C + '/02 CARTONES'
A = C + '/06 AUDIO'
COMUNES = 'E:/DAE MASTER/00 COMUNES'
INTRO = COMUNES + '/INTRO/FGN_intro_version7.mp4'
MARCA = COMUNES + '/MARCA DE AGUA/MARCA_DE_AGUA_DAE_100s.mov'

PISTAS_V = ['VIDEO', 'TINTE', 'CARTONES', 'APOYO',
            'MARCA DE AGUA', 'EFECTOS', 'LOWER THIRD']
PISTAS_A = ['VIDEO', 'NARRADOR', 'PREGUNTAS', 'DIALOGO', 'MUSICA']

N_INTRO, N_BLANCO, N_RANURAS, N_LECHO = 222, 119, 3884, 1193
OFF_ENTRADA = N_INTRO                                  #  222
OFF_RANURAS = OFF_ENTRADA + N_BLANCO                   #  341
OFF_LECHO = OFF_RANURAS + N_RANURAS                    # 4225
OFF_CIERRE = OFF_LECHO + N_LECHO                       # 5418
OFF_OUTRO = OFF_CIERRE + N_BLANCO                      # 5537
FIN = OFF_OUTRO + N_INTRO                              # 5759

RAN = {}
_o = OFF_RANURAS
for _r, _n in [('r01', 235), ('r02', 269), ('r03', 188), ('r04', 251),
               ('r05', 143), ('r06', 239), ('r07', 314), ('r08', 175),
               ('r09', 325), ('r10', 215), ('r11', 240), ('r12', 182),
               ('r13', 148), ('r14', 152), ('r15', 127), ('r16', 189),
               ('r17', 170), ('r18', 132), ('r19', 190)]:
    RAN[_r] = (_o, _n)
    _o += _n
assert _o == OFF_LECHO, _o

# Cartones de narracion: SOLO sobre ranuras de FOTO. Las de After Effects
# -r05 r09 r11 r12 r14 r17 r19- no llevan carton: ya son grafica.
CARTONES = [('C5U2_n01_frenos.mov', 'r01'),
            ('C5U2_n02_victimas.mov', 'r02'),
            ('C5U2_n03_imputacion.mov', 'r03'),
            ('C5U2_n04_cautelares.mov', 'r04'),
            ('C5U2_n05_licito.mov', 'r06'),
            ('C5U2_n06_casa.mov', 'r07'),
            ('C5U2_n07_camioneta.mov', 'r08'),
            ('C5U2_n08_flota.mov', 'r10'),
            ('C5U2_n09_vender.mov', 'r13'),
            ('C5U2_n10_poliza.mov', 'r15'),
            ('C5U2_n11_caucion.mov', 'r16'),
            ('C5U2_n12_venta.mov', 'r18')]
PAUSA = ['C5U2_p1a_votacion.mov', 'C5U2_p1b_opciones.mov', 'C5U2_p2_foro.mov']

REAL = {'FGN_intro_version7.mp4': 222, 'MARCA_DE_AGUA_DAE_100s.mov': 2400,
        'C5U2_carton_entrada.mov': 119, 'C5U2_carton_cierre.mov': 119,
        'C5U2_r20_lecho_sala_v1193.mov': 1193,
        'C5U2_n01_frenos.mov': 158, 'C5U2_n02_victimas.mov': 207,
        'C5U2_n03_imputacion.mov': 129, 'C5U2_n04_cautelares.mov': 188,
        'C5U2_n05_licito.mov': 158, 'C5U2_n06_casa.mov': 207,
        'C5U2_n07_camioneta.mov': 119, 'C5U2_n08_flota.mov': 178,
        'C5U2_n09_vender.mov': 96, 'C5U2_n10_poliza.mov': 96,
        'C5U2_n11_caucion.mov': 119, 'C5U2_n12_venta.mov': 96,
        'C5U2_p1a_votacion.mov': 414, 'C5U2_p1b_opciones.mov': 483,
        'C5U2_p2_foro.mov': 296}


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


def _ranuras():
    """Los .mov de RANURAS, sin las versiones archivadas.

    Las viejas se guardan con prefijo _v1_, _v2_, ... No se borran: si algo
    sale mal se vuelve a la anterior sin rehornear. El filtro tiene que
    excluirlas TODAS, no solo _v1_.
    """
    return [f for f in sorted(os.listdir(R))
            if f.endswith('.mov') and not f.startswith('_v')]


def medios(mp):
    rutas = [INTRO, MARCA, A + '/C5U2_NARRADOR.wav', A + '/C5U2_MUSICA_cama.wav']
    rutas += [R + '/' + f for f in _ranuras()]
    rutas += [K + '/' + f for f in sorted(os.listdir(K)) if not f.startswith('_v')]
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
    ran = [f for f in _ranuras() if 'lecho' not in f]
    sec = [('FGN_intro_version7.mp4', N_INTRO),
           ('C5U2_carton_entrada.mov', N_BLANCO)]
    sec += [(f, int(f.rsplit('_v', 1)[1].split('.')[0])) for f in ran]
    sec += [('C5U2_r20_lecho_sala_v1193.mov', N_LECHO),
            ('C5U2_carton_cierre.mov', N_BLANCO),
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
        lote.append({'mediaPoolItem': IT['C5U2_NARRADOR.wav'], 'startFrame': 0,
                     'endFrame': N_RANURAS, 'trackIndex': 2,
                     'recordFrame': T0 + OFF_RANURAS, 'mediaType': 2})
    if not tl.GetItemListInTrack('audio', 5):
        lote.append({'mediaPoolItem': IT['C5U2_MUSICA_cama.wav'], 'startFrame': 0,
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

    vacias = [('video', 2), ('video', 4), ('video', 6), ('video', 7),
              ('audio', 3), ('audio', 4)]
    ocup = [x for x in vacias if tl.GetItemListInTrack(*x)]
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
    for f, nota in ((OFF_LECHO + REAL['C5U2_p1a_votacion.mov']
                     + REAL['C5U2_p1b_opciones.mov'] - 1, 'H5P votacion'),
                    (OFF_CIERRE - 1, 'H5P foro')):
        print(f, tl.AddMarker(f, 'Cyan', nota, nota, 1))
    d = C + '/10 TIMELINE SEBASTIAN/' + NOM + '.drt'
    print('drt', tl.Export(d, resolve.EXPORT_DRT))


if __name__ == '__main__':
    paso = sys.argv[1] if len(sys.argv) > 1 else 'chequeo'
    resolve, pr, mp = _handles()
    {'medios': lambda: medios(mp), 'linea': lambda: linea(pr, mp),
     'v1': lambda: v1(pr, mp), 'v3': lambda: v3(pr, mp),
     'pegado': lambda: pegado(pr, mp), 'chequeo': lambda: chequeo(pr),
     'marcas': lambda: marcas(resolve, pr)}[paso]()
