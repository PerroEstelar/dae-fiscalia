# V2 de los casos del profe Carlos Humberto — parte hecha en la nube (28 oct 2026)

Estos scripts corrieron en el sandbox de Claude (Linux, numpy/PIL/soundfile/scipy),
con las rutas absolutas de allá. Se guardan como registro del método; para volver
a correrlos hay que cambiar las rutas (`/mnt/user-data/uploads/DAE/_tmp/ch/...`
eran copias de `D:\DAE\_tmp\ch\...`).

- `v2audio.py`     primitivas de audio: limpiar tramos, insertar tiempo (fondo
                   repite los segundos anteriores con fundido de igual potencia),
                   poner tomas al nivel del tramo que reemplazan, LUFS, limitador.
- `audio_v2.py`    el plan por caso (tramos a silenciar, insertos, tomas) y la
                   normalización a −18 LUFS. La voz de la V1 se centra (venía 7,7 dB
                   a la izquierda).
- `sep_c4.py`      caso 4 (sin línea): separa narración y fondo de la V1 entregada
                   alineando el mp3 de ElevenLabs (dos tramos, offsets 12,480 y
                   11,771 s) y restándolo de la mezcla.
- `v2graf.py`      gráficos en el estilo medido de la V1: cartón (Bold 71, paso 86,
                   x 236, centro y 583, barra 176–203 × 491–677, velo (6,71,148) 45 %),
                   etiqueta, cambio de palabra en el rótulo, marca «APRENDE CON LA DAE».
- `graf_c2/c3/c4/c6.py`  las piezas de cada caso (cuadros exactos de la V1).
- `montajes.py`    escribe los `montaje_c0N.json` que arma `ch_montar_v2.py` en Resolve.
- `analiza.py`     ubicación de los tramos en la transcripción (Scribe) de cada V1.

Lo que corre en Windows está en `herramientas/montaje/ch_*.py` y `herramientas/voz/ch_*.py`.
