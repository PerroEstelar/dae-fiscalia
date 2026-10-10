# -*- coding: utf-8 -*-
"""Exporta una linea de tiempo del curso TA con los ajustes de la serie,
la nombra como la convencion de entrega y la deja en la carpeta de paso
de Google Drive para que Drive para escritorio la suba.

Uso (desde un run_inline con resolve ya enlazado, o suelto con DaVinciResolveScript):

    import exportar_y_subir as e
    e.entregar(timeline='TA CASO 08 - a la voz', unidad=1, caso='08',
               destino=r'E:\\...\\05 EXPORTS')

El movimiento desde la carpeta de paso hasta la carpeta compartida del
Drive lo hace Claude con el conector (update_file), porque la carpeta
compartida no se sincroniza en el disco.
"""

import os
import shutil
import subprocess
import json
import time

PRESET = 'H.264 Master'
PASO = os.path.join('G:\\', 'My Drive', '_TA subidas')

# Medidos de los propios exports de la serie.
AJUSTES = {
    'FormatWidth': 1920,
    'FormatHeight': 1080,
    'FrameRate': 23.976,
    'VideoQuality': 6000,        # tope en kb/s, el codificador va en VBR por debajo
    'EncodingProfile': 'High',   # sin esta clave sale Main
    'AudioCodec': 'aac',
    'AudioSampleRate': 48000,
    'ExportVideo': True,
    'ExportAudio': True,
    'SelectAllFrames': True,
}

FFPROBE = os.environ.get('FFPROBE', os.path.join(
    'C:\\', 'Users', 'call_', 'AppData', 'Local', 'Microsoft', 'WinGet', 'Packages',
    'Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe',
    'ffmpeg-9.0-full_build', 'bin', 'ffprobe.exe'))


def nombre_entrega(unidad, caso, version=1):
    return 'TA - U%d - CASO %s - V%d' % (int(unidad), str(caso).zfill(2), int(version))


def _proyecto(resolve):
    pm = resolve.GetProjectManager()
    pr = pm.GetCurrentProject()
    if pr is None or pr.GetName() != 'DAE MASTER - CURSOS':
        pm.LoadProject('DAE MASTER - CURSOS')
        pr = pm.GetCurrentProject()
    return pr


def _buscar_timeline(pr, nombre):
    for i in range(1, pr.GetTimelineCount() + 1):
        tl = pr.GetTimelineByIndex(i)
        if tl.GetName() == nombre:
            return tl
    raise RuntimeError('no existe la linea de tiempo %r' % nombre)


def renderizar(resolve, timeline, destino, nombre, espera=600):
    """Renderiza y devuelve la ruta del archivo. Borra un archivo anterior
    con el mismo nombre para que ffprobe no mida uno viejo."""
    pr = _proyecto(resolve)
    tl = _buscar_timeline(pr, timeline)
    pr.SetCurrentTimeline(tl)
    cuadros = tl.GetEndFrame() - tl.GetStartFrame()

    os.makedirs(destino, exist_ok=True)
    salida = os.path.join(destino, nombre + '.mov')
    if os.path.exists(salida):
        os.remove(salida)

    pr.DeleteAllRenderJobs()
    pr.LoadRenderPreset(PRESET)
    pr.SetCurrentRenderFormatAndCodec('mov', 'H264')
    s = dict(AJUSTES)
    s['TargetDir'] = destino
    s['CustomName'] = nombre
    if not pr.SetRenderSettings(s):
        raise RuntimeError('SetRenderSettings devolvio False')
    jid = pr.AddRenderJob()
    pr.StartRendering([jid], isInteractiveMode=False)

    t0 = time.time()
    while pr.IsRenderingInProgress() and time.time() - t0 < espera:
        time.sleep(2)
    estado = pr.GetRenderJobStatus(jid)
    if estado.get('JobStatus') != 'Complete':
        raise RuntimeError('el render no termino: %r' % estado)
    return salida, cuadros


def verificar(ruta, cuadros_esperados=None):
    """Compara el archivo con el patron de la serie. Devuelve el informe."""
    d = json.loads(subprocess.run(
        [FFPROBE, '-v', 'quiet', '-print_format', 'json',
         '-show_format', '-show_streams', ruta],
        capture_output=True, text=True).stdout)
    v = [x for x in d['streams'] if x.get('codec_type') == 'video'][0]
    a = [x for x in d['streams'] if x.get('codec_type') == 'audio'][0]
    inf = {
        'tam_mb': round(os.path.getsize(ruta) / 1048576.0, 1),
        'duracion': float(d['format']['duration']),
        'codec': v['codec_name'],
        'perfil': v.get('profile'),
        'ancho': v['width'],
        'alto': v['height'],
        'cadencia': v['r_frame_rate'],
        'cuadros': int(v.get('nb_frames', 0)),
        'vbr': int(v.get('bit_rate', 0)),
        'audio': a['codec_name'],
        'muestreo': int(a['sample_rate']),
        'canales': a['channels'],
    }
    fallos = []
    if inf['codec'] != 'h264':
        fallos.append('codec %s' % inf['codec'])
    if inf['perfil'] != 'High':
        fallos.append('perfil %s' % inf['perfil'])
    if (inf['ancho'], inf['alto']) != (1920, 1080):
        fallos.append('tamano %dx%d' % (inf['ancho'], inf['alto']))
    if inf['cadencia'] != '24000/1001':
        fallos.append('cadencia %s' % inf['cadencia'])
    if inf['audio'] != 'aac' or inf['muestreo'] != 48000 or inf['canales'] != 2:
        fallos.append('audio %s %d %dch' % (inf['audio'], inf['muestreo'], inf['canales']))
    if cuadros_esperados and inf['cuadros'] != cuadros_esperados:
        fallos.append('cuadros %d, esperaba %d' % (inf['cuadros'], cuadros_esperados))
    inf['fallos'] = fallos
    return inf


def a_paso(ruta):
    """Copia el render a la carpeta de paso de Drive para escritorio."""
    os.makedirs(PASO, exist_ok=True)
    dst = os.path.join(PASO, os.path.basename(ruta))
    shutil.copy2(ruta, dst)
    return dst


def entregar(resolve, timeline, unidad, caso, destino, version=1, subir=True):
    nombre = nombre_entrega(unidad, caso, version)
    salida, cuadros = renderizar(resolve, timeline, destino, nombre)
    inf = verificar(salida, cuadros)
    paso = a_paso(salida) if subir and not inf['fallos'] else None
    return {'render': salida, 'paso': paso, 'informe': inf}
