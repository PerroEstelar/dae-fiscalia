# SRPA y justicia restaurativa — subtítulos (18 nov 2026)

Prioridad 2 de la lista de Esteban del 18 nov: un `.srt` por video, en español, con los tiempos del video final (intro
incluida), con el mismo nombre del video y en su misma carpeta de Drive. Método y criterio:
`herramientas/subtitulos/README.md`. Aquí están el `manifiesto.json` (video local, carpeta e ids de Drive) y las
`correcciones.json` (reglas sobre el texto de Scribe; `_despues` se aplica cuando las cifras ya están en números).

| video | subtítulos | dura | id del `.srt` en Drive |
|---|---|---|---|
| `srpa - CURSO - PRESENTACION-v2` | 248 | 15:55 | `1gV4LYS-g5IhBGSFW8y0QcihhG36jnX-K` |
| `srpa - CURSO - CIERRE-v1` | 127 | 7:59 | `1UD8WOXCJE2OVHjFWe7_NmtDr0wCetkbC` |
| `srpa - U1 - BIENVENIDA-v2` | 136 | 8:52 | `1LeKLpnc_yJPOoBZ74avTBCqGP6kq7T9o` |
| `srpa - U1 - CIERRE-v1` | 280 | 17:29 | `19gS5OT-ABOBnlkfGNveShe1A1-7NzfCv` |
| `srpa - U3 - BIENVENIDA-v2` | 55 | 4:17 | `1neRy2E9KwE49GirWpcuaLe-ib_HGST0u` |
| `srpa - U3 - DESARROLLO-v2` | 627 | 39:57 | `1P7TPX6SgTXSvUHQqWUoS--OGvdFHRFy_` |
| `srpa - U3 - CIERRE-v2` | 177 | 11:55 | `1ICK73A-7M5k4zKihihpV3EZD2ecnxDYG` |
| `srpa - U4 - INICIO-v1` | 28 | 2:31 | `1xFUQgwvlSiaiW7blhWFpJeDgxgMZNLAo` |
| `srpa - U4 - DESARROLLO-v1` | 475 | 32:08 | `1_Ej8OfrF1WFXO2W_CuzD3iTN5r9Asxqk` |
| `srpa - U4 - CIERRE-v2` | 137 | 9:34 | `1WVTGb3iMaGqJUI8qWMrU-RQaxRbUI6ze` |
| `srpa - U5 - INICIO-v1` | 32 | 2:28 | `14sNE61MtwZOItJ9OZBQkaCr__BjcT8Un` |
| `srpa - U5 - DESARROLLO-v1` | 526 | 32:59 | `1M_ytf4vXE_3C7J1RSZxNIm6ITFO40rMB` |
| `srpa - U5 - CIERRE-v2` | 279 | 18:17 | `1vkOizTfPKDHjI5SwwGYWZ1FMx70p1ndW` |
| `PRIO 1 - SRPA - U1 - CASO NICO PRINCIPIO DE CULPABILIDAD` | 136 | 8:44 | `1_gwig1AR1j31BVrs5nJKd6w-Mbdtnubx` |
| `CASO IPANEMA V7` | 154 | 9:19 | `1xL_67RLCwmy3FcpUqvCgydRUHVhNREVl` |

Son 15 videos y 222 min. **La unidad 2 no está:** su presentación y su cierre no los hemos procesado (está en pausa
hasta que llegue la otra grabación); la lista de Esteban los cuenta («U2 de JP»).

## Cómo se revisó

Los profes hablan sin leer (29.000 palabras, cientos de tropiezos), así que la limpieza se hizo con reglas generales
en `srt_de_stt.py` y 77 reglas a mano. No se leyó cada palabra de las tres clases largas; se revisó:

- las repeticiones de toma (no hay ninguna: los cortes ya estaban hechos al montar);
- todo lo que quedaba cortado («…»), una por una, contra el texto crudo;
- las 157 palabras que Scribe marcó con menos confianza y las que un corrector ortográfico no conoce;
- todos los nombres propios, leyes, sentencias y cifras, contra los cartones de `plan_srpa.py` y de los planes de
  `profe/`, y contra los documentos del curso en Drive («Polcrymed», «Howard Zehr», «Myriam Ávila», «Bauman
  Polonio», «Neima», «Rodman», «Disney»);
- trece tramos dudosos, con una segunda escucha (`stt_tramo.py`);
- el principio y el final de cada video, y el cierre de la unidad 4 entero.

## Lo que queda como lo dijo el profe (avisado a Sebastián)

- Presentación del curso, 1:18: dice «el profesor Carlos Humberto Rodríguez» (es Ramírez Romero; más adelante lo
  nombra bien). El subtítulo sigue al audio.
- Desarrollo de la U5, 18:46: se oye «el artículo cincuenta de la Constitución» en tres de cuatro escuchas y «dos
  cincuenta» en una; en el resto de la clase cita tres veces el 250, que es el que corresponde. Quedó «artículo 250».
- Desarrollo de la U3, 23:17: Scribe dio cinco cosas distintas («En esos vendidas», «denegadas»…). Quedó «En ese
  entendido», que es el giro que encaja con el sonido y con la frase; es lo único que no sale de una escucha limpia.

## Un `.srt` reemplazado

El de `srpa - U3 - DESARROLLO-v2` se subió dos veces. En la primera, Scribe había estirado la palabra «¿Qué» de 12:17,7
a 12:25,9 (ocho segundos sobre un silencio) y el subtítulo aparecía siete segundos antes de la pregunta. `srt_de_stt.py`
ahora no le cree al principio de una palabra que dura más de 3 s. El archivo viejo (`1MUOWjn2EYNaoF6j0Wy1OeMNMAtShNdHU`)
está en la papelera de Drive.
