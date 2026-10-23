#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Exporta una linea COMPROBANDO antes que el trabajo sea el que se pidio.

EL ERROR QUE ESTO IMPIDE, Y QUE CASI SE ENTREGA
    23 de octubre de 2026. Con la linea del Caso 4 v2 ya montada y chequeada,
    `SetCurrentTimeline` devolvio True, `GetCurrentTimeline().GetName()`
    devolvio «P3C4 PUERTO DE SALIDA v2»... y `AddRenderJob()` creo un trabajo
    sobre la linea del CASO 5:

        job        P3C5_VOCES_REGISTROS_Y_CUENTAS.mov
        marcas     86400  95356  = 8957 cuadros   (el Caso 4 tiene 8656)

    Y arranco sin un solo error. Escribio 204 MB antes de que lo parara.

    La causa: `AddRenderJob` no lee la linea actual del PROYECTO, lee el
    estado de la pagina DELIVER, que seguia donde la dejo el render anterior.
    `SetCurrentTimeline` no la mueve. Hay que abrir la pagina.

    Pero abrir la pagina tampoco basta como garantia: lo unico que garantiza
    es MIRAR EL TRABAJO YA CREADO y comprobar que su linea y su conteo de
    cuadros son los que se pidieron. Es la misma leccion del grade por
    registro y de las rimas: la herramienta no avisa, la medida si.

COMO SE USA
    import exportar
    exportar.exportar(resolve, project,
                      nombre_linea='P3C4 PUERTO DE SALIDA v2',
                      carpeta=r'E:\...\05 EXPORTS',
                      nombre_archivo='P3C4_..._v3',
                      cuadros=8656)

Si el trabajo no cuadra, se borra y se levanta una excepcion. Nunca arranca.
"""
import os
import time

AJUSTES = {
    'ExportVideo': True, 'ExportAudio': True,
    'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': '23.976',
    'VideoQuality': 0, 'AudioCodec': 'aac', 'AudioBitDepth': 16,
    'AudioSampleRate': 48000,
}


def _linea(pr, nombre):
    for i in range(pr.GetTimelineCount()):
        t = pr.GetTimelineByIndex(i + 1)
        if t.GetName() == nombre:
            return t
    raise RuntimeError('no existe la linea %r' % nombre)


def preparar(resolve, pr, nombre_linea, carpeta, nombre_archivo, cuadros,
             formato=('QuickTime', 'H264_NVIDIA')):
    """Deja un trabajo de render COMPROBADO. Devuelve su job id."""
    tl = _linea(pr, nombre_linea)
    pr.SetCurrentTimeline(tl)
    # sin esto, AddRenderJob se queda con la linea del render anterior
    resolve.OpenPage('deliver')
    time.sleep(2)
    os.makedirs(carpeta, exist_ok=True)
    pr.SetCurrentRenderFormatAndCodec(*formato)

    s = dict(AJUSTES)
    s.update({'SelectAllFrames': True, 'TargetDir': carpeta,
              'CustomName': nombre_archivo})
    if not pr.SetRenderSettings(s):
        raise RuntimeError('SetRenderSettings devolvio False')

    pr.DeleteAllRenderJobs()
    jid = pr.AddRenderJob()
    j = [x for x in pr.GetRenderJobList() if x['JobId'] == jid][0]

    n = j['MarkOut'] - j['MarkIn'] + 1
    problemas = []
    if j.get('TimelineName') != nombre_linea:
        problemas.append('la linea del trabajo es %r, no %r'
                         % (j.get('TimelineName'), nombre_linea))
    if n != cuadros:
        problemas.append('el trabajo abarca %d cuadros, no %d' % (n, cuadros))
    if not j.get('OutputFilename', '').startswith(nombre_archivo):
        problemas.append('el archivo de salida es %r, no empieza por %r'
                         % (j.get('OutputFilename'), nombre_archivo))
    if problemas:
        pr.DeleteAllRenderJobs()
        raise RuntimeError('el trabajo de render no cuadra, no se arranca:\n  '
                           + '\n  '.join(problemas))
    return jid, j


def exportar(resolve, pr, nombre_linea, carpeta, nombre_archivo, cuadros,
             formato=('QuickTime', 'H264_NVIDIA'), esperar=True):
    jid, j = preparar(resolve, pr, nombre_linea, carpeta, nombre_archivo,
                      cuadros, formato)
    print('linea   %s' % j.get('TimelineName'))
    print('archivo %s' % j.get('OutputFilename'))
    print('marcas  %d..%d = %d cuadros  ·  %s %sx%s %s'
          % (j['MarkIn'], j['MarkOut'], j['MarkOut'] - j['MarkIn'] + 1,
             j['VideoCodec'], j['FormatWidth'], j['FormatHeight'],
             j['FrameRate']))
    if not pr.StartRendering([jid], isInteractiveMode=False):
        raise RuntimeError('StartRendering devolvio False')
    if not esperar:
        return jid
    while pr.IsRenderingInProgress():
        time.sleep(4)
    e = pr.GetRenderJobStatus(jid)
    print('estado  %s %s%%  en %.1f s'
          % (e.get('JobStatus'), e.get('CompletionPercentage'),
             e.get('TimeTakenToRenderInMs', 0) / 1000.0))
    if e.get('JobStatus') != 'Complete':
        raise RuntimeError('el render no termino: %r' % e)
    return jid
