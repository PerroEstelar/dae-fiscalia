#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Arma el master de narracion del P3C5 «Voces, registros y cuentas».

ESTE ARMADOR NORMALIZA, Y LOS ANTERIORES NO
    El Caso 4 salio a -15,4 LUFS cuando la serie fija -19, y hubo que
    rehacerlo despues de renderizar el master. La causa: `carga()` solo
    decodifica, y en toda la cadena -medir.py, armar.py, armar_p3c4.py- no
    habia un solo loudnorm. El nivelado entre bloques igualaba los bloques
    ENTRE SI, que es otra cosa que igualarlos contra el objetivo.

    Aqui se hacen las dos, y en este orden:

      1. Nivelar cada bloque contra la MEDIANA de los bloques, para que no
         haya escalon entre uno y el siguiente.
      2. Concatenar con las pausas.
      3. Medir el master entero y aplicar UNA ganancia lineal para dejarlo
         en -19,0 LUFS.

    La ganancia del paso 3 es lineal y no loudnorm, a proposito: loudnorm
    comprime y desharia el nivelado del paso 1.

Y NO USA NUMPY
    La instalacion de Python de esta maquina no lo tiene, asi que todo el
    calculo lo hace ffmpeg con un solo filter_complex. Ademas sale exacto:
    no hay redondeos de ida y vuelta por float32.

LAS PAUSAS MARCAN LA FORMA, Y AQUI LA FORMA SON CUATRO MOVIMIENTOS
    Los casos 1 a 3 eran una situacion con sus propuestas al lado. El 4 eran
    seis actuaciones sucesivas. Este corre en dos tiempos sobre el mismo
    expediente, con un resultado en medio y un alegato al final:

      1,4 s  antes de b16, el RESULTADO de la practica probatoria. Es el eje
             de la pieza y el unico sitio donde el documento pone titulo
             propio. Si esa frontera no se oye, la pieza es un listado.
      1,0 s  antes de cada movimiento nuevo -b04 la preparatoria, b13 el
             juicio, b17 la mitad de Tomas, b18 el alegato-. b17 lleva pausa
             de movimiento aunque siga a b16 porque la asimetria entre Oscar
             y Tomas ES el caso: tienen que oirse como dos cosas.
      1,2 s  antes del cierre.
      0,9 s  antes de cada afirmacion que va a carton.
      0,8 s  el resto.
"""
import json
import os
import re
import subprocess
import sys

PREFIJO = 'P3C5_'
SR = 48000
COLA = 0.6
OBJETIVO = -19.0
TECHO = -1.0          # dBTP, el destino de la serie
LIMITE = -2.0         # dBFS de muestra, deja margen para el pico real

MOVIMIENTO = 1.0
EJE = 1.4
GIRO = 0.9
CIERRE = 1.2
POR_DEFECTO = 0.8

PAUSA = {
    'b04_informe_unitario': MOVIMIENTO,   # empieza la preparatoria
    'b07_pertinencia': GIRO,
    'b08_estipulacion': GIRO,
    'b09_interceptaciones': GIRO,
    'b10_renata': GIRO,
    'b11_perita': GIRO,
    'b13_lucia_fecha': MOVIMIENTO,        # empieza el juicio
    'b16_resultado_oscar': EJE,           # el eje de la pieza
    'b17_resultado_tomas': MOVIMIENTO,    # la otra mitad, y se tiene que oir
    'b18_alegato_fiscalia': MOVIMIENTO,   # el alegato
    'b19_alegato_defensa': GIRO,
    'b20_cierre': CIERRE,
}

FF = os.environ.get('FFMPEG', 'ffmpeg')
FP = os.environ.get('FFPROBE', FF.replace('ffmpeg', 'ffprobe'))


def nombre(f):
    """P3C5_07_b07_pertinencia.mp3 -> b07_pertinencia"""
    return f.replace(PREFIJO, '').replace('.mp3', '').split('_', 1)[1]


def medir(ruta):
    """(sonoridad integrada, pico real) de un archivo."""
    s = subprocess.run([FF, '-nostats', '-i', ruta, '-af', 'ebur128=peak=true',
                        '-f', 'null', '-'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace').stderr
    i = re.findall(r'I:\s+(-?\d+\.\d+) LUFS', s)
    p = re.findall(r'Peak:\s+(-?\d+\.\d+) dBFS', s)
    return (float(i[-1]) if i else None), (float(p[-1]) if p else None)


def duracion(ruta):
    s = subprocess.run([FP, '-v', 'error', '-show_entries', 'format=duration',
                        '-of', 'csv=p=0', ruta], capture_output=True, text=True).stdout
    return float(s.strip())


def main(carpeta, salida, json_salida):
    fs = sorted(f for f in os.listdir(carpeta) if f.endswith(('.mp3', '.wav')))
    rutas = [os.path.join(carpeta, f) for f in fs]
    niveles = [medir(r)[0] for r in rutas]
    duraciones = [duracion(r) for r in rutas]

    vivos = sorted(n for n in niveles if n is not None)
    med = vivos[len(vivos) // 2] if len(vivos) % 2 else \
        (vivos[len(vivos) // 2 - 1] + vivos[len(vivos) // 2]) / 2.0

    # 1 y 2 · ganancia por bloque y concatenacion con las pausas, de una vez
    cmd = [FF, '-v', 'error', '-y']
    for r in rutas:
        cmd += ['-i', r]
    partes, etiquetas = [], []
    for i, (f, n) in enumerate(zip(fs, niveles)):
        g = (med - n) if n is not None else 0.0
        partes.append('[%d:a]aresample=%d,aformat=sample_fmts=fltp:channel_layouts=mono,'
                      'volume=%.4fdB[a%d]' % (i, SR, g, i))
        etiquetas.append('[a%d]' % i)
        if i < len(fs) - 1:
            p = PAUSA.get(nombre(fs[i + 1]), POR_DEFECTO)
            partes.append('aevalsrc=0:s=%d:d=%.4f,aformat=sample_fmts=fltp:'
                          'channel_layouts=mono[p%d]' % (SR, p, i))
            etiquetas.append('[p%d]' % i)
    partes.append('aevalsrc=0:s=%d:d=%.4f,aformat=sample_fmts=fltp:'
                  'channel_layouts=mono[cola]' % (SR, COLA))
    etiquetas.append('[cola]')
    partes.append('%sconcat=n=%d:v=0:a=1[out]' % (''.join(etiquetas), len(etiquetas)))
    tmp = salida + '.tmp.wav'
    cmd += ['-filter_complex', ';'.join(partes), '-map', '[out]',
            '-c:a', 'pcm_s24le', '-ar', str(SR), '-ac', '1', tmp]
    q = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if q.returncode:
        raise SystemExit('ffmpeg: ' + (q.stderr or '')[-1200:])

    # 3 · ganancia al objetivo, y un limitador que recorte solo las puntas
    #
    # NO se baja el master entero para que quepa el pico mas alto. Medido
    # aqui: b07 trae una cresta de 23,3 dB -el resto esta entre 15 y 21- y
    # dejar que esa punta mande habria clavado la pieza en -24,2 LUFS, cinco
    # por debajo de la serie. El limitador toca esas puntas y nada mas.
    antes, _ = medir(tmp)
    g = OBJETIVO - antes
    q = subprocess.run([FF, '-v', 'error', '-y', '-i', tmp,
                        '-af', 'volume=%.4fdB,'
                               'alimiter=limit=%.4f:attack=5:release=50:level=disabled,'
                               'aformat=channel_layouts=stereo'
                               % (g, 10 ** (LIMITE / 20.0)),
                        '-c:a', 'pcm_s24le', '-ar', str(SR), salida],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if q.returncode:
        raise SystemExit('ffmpeg: ' + (q.stderr or '')[-800:])

    # el limitador baja un poco la sonoridad: se corrige una vez y se vuelve
    # a limitar, que es mas honesto que dar por bueno el primer numero
    hecho, pico = medir(salida)
    if abs(hecho - OBJETIVO) > 0.2:
        g2 = g + (OBJETIVO - hecho)
        q = subprocess.run([FF, '-v', 'error', '-y', '-i', tmp,
                            '-af', 'volume=%.4fdB,'
                                   'alimiter=limit=%.4f:attack=5:release=50:level=disabled,'
                                   'aformat=channel_layouts=stereo'
                                   % (g2, 10 ** (LIMITE / 20.0)),
                            '-c:a', 'pcm_s24le', '-ar', str(SR), salida],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        if q.returncode:
            raise SystemExit('ffmpeg: ' + (q.stderr or '')[-800:])
        g = g2
    os.remove(tmp)

    # la rejilla, con las duraciones reales
    tramos, t = [], 0.0
    for i, (f, d) in enumerate(zip(fs, duraciones)):
        tramos.append({'bloque': nombre(f), 'entra': round(t, 3),
                       'sale': round(t + d, 3), 'dur': round(d, 3)})
        t += d
        if i < len(fs) - 1:
            t += PAUSA.get(nombre(fs[i + 1]), POR_DEFECTO)
    t += COLA

    pasos = [abs(niveles[i + 1] - niveles[i]) for i in range(len(niveles) - 1)
             if niveles[i] is not None and niveles[i + 1] is not None]
    info = {'dur': t, 'tramos': tramos, 'lufs_crudo': antes,
            'ganancia_db': g, 'peor_escalon_crudo': max(pasos) if pasos else None}
    json.dump(info, open(json_salida, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    return info


if __name__ == '__main__':
    info = main(sys.argv[1], sys.argv[2], sys.argv[3])
    d = info['dur']
    print('master %.2f s  (%d:%04.1f)' % (d, int(d) // 60, d % 60))
    print('crudo %.1f LUFS, ganancia %+.2f dB' % (info['lufs_crudo'], info['ganancia_db']))
    print('peor escalon entre bloques ANTES de nivelar: %.2f LU'
          % info['peor_escalon_crudo'])
    print()
    print('%-26s %7s %7s %7s' % ('bloque', 'entra', 'sale', 'dur'))
    for t in info['tramos']:
        print('%-26s %7.2f %7.2f %7.2f' % (t['bloque'], t['entra'], t['sale'], t['dur']))
    i, p = medir(sys.argv[2])
    print('\nmedido sobre el archivo escrito: %.1f LUFS, pico real %.1f dBFS' % (i, p))
