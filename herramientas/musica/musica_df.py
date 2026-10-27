# -*- coding: utf-8 -*-
r"""Pone la cama de musica en una linea de tiempo que ya esta montada.

NO REMONTA NADA
    Agrega las pistas de audio que falten hasta cinco, deja la cama en A5 y
    no toca ni un clip de video ni la voz. Si A5 ya tiene algo, no hace nada.

LA MUSICA VA EN A5, NO EN A2
    26 de octubre. La cama se puso primero en A2 y los cinco capitulos
    salieron con los huecos en SILENCIO DIGITAL -131 dB-, con el render
    reportando Complete 100 y sin un solo error. El archivo de entrega del
    capitulo 1 volvio con el MISMO TAMANO EXACTO que la version sin musica,
    que fue lo que delato el problema.

    Medido: la misma cama, el mismo clip, movida a A5, rinde -25,0 dB en el
    hueco de 8 a 12 s, que es justo lo que mide el wav. Una pista de audio
    agregada por API en el indice 2 no llega al bus principal de este build.
    A5 es ademas donde la musica vive en las otras 46 lineas del proyecto.

EL NIVEL YA VIENE HORNEADO
    La envolvente de ducking la hornea cama_musica.py -26 LUFS en los huecos,
    -32 bajo la narracion-. Aqui la pista entra con la ganancia en cero. Si
    hay que cambiar el balance se vuelve a correr cama_musica, no se toca el
    fader: la API de este build no escribe niveles de audio.
"""
import os
import sys

sys.path.insert(0, 'D:/DAE/_repo/herramientas/prompts')
import plan_camara_df as PC                        # noqa: E402

T0 = 86400
PISTAS = ((1, 'NARRADOR'), (2, 'PREGUNTAS'), (3, 'DIALOGO'),
          (4, 'AMBIENTE'), (5, 'MUSICA'))
PISTA_MUSICA = 5


def _carpeta(f, nombre):
    if f.GetName() == nombre:
        return f
    for s in f.GetSubFolderList():
        r = _carpeta(s, nombre)
        if r:
            return r
    return None


def poner(resolve, tl, wav):
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    if not os.path.exists(wav):
        return 'no hay cama en disco: %s' % wav
    pr.SetCurrentTimeline(tl)
    while tl.GetTrackCount('audio') < len(PISTAS):
        if not tl.AddTrack('audio', 'stereo'):
            return 'no pude agregar la pista de audio'
    for i, n in PISTAS:
        tl.SetTrackName('audio', i, n)
    if tl.GetItemListInTrack('audio', PISTA_MUSICA):
        return 'A%d ya tiene clips: no la toco' % PISTA_MUSICA
    carp = _carpeta(mp.GetRootFolder(), tl.GetName())
    if carp is None:
        return 'no encuentro la carpeta del pool'
    mp.SetCurrentFolder(carp)

    def hallar():
        for c in carp.GetClipList():
            r = c.GetClipProperty('File Path').replace('/', os.sep)
            if os.path.basename(r) == os.path.basename(wav):
                return c
        return None

    it = hallar()
    if it is None:
        mp.ImportMedia([wav])
        it = hallar()
    if it is None:
        return 'no quedo en el pool'
    tot = tl.GetEndFrame() - tl.GetStartFrame()
    mp.AppendToTimeline([{'mediaPoolItem': it, 'startFrame': 0,
                          'endFrame': tot - 1, 'trackIndex': PISTA_MUSICA,
                          'recordFrame': T0, 'mediaType': 2}])
    hay = tl.GetItemListInTrack('audio', PISTA_MUSICA)
    if not hay:
        return 'el clip no quedo en A%d' % PISTA_MUSICA
    return 'A%d MUSICA  %d cuadros' % (PISTA_MUSICA, tot)


if __name__ == '__main__':
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    lineas = {}
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName().startswith('DF C'):
            lineas[int(t.GetName()[4])] = t
    for cap in [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5]:
        wav = os.path.join(PC.RAIZ, PC.CAPS[cap], '08 MUSICA',
                           'DF_C%d_MUSICA_cama.wav' % cap)
        print('cap %d ->' % cap, poner(resolve, lineas[cap], wav), flush=True)
    resolve.GetProjectManager().SaveProject()
