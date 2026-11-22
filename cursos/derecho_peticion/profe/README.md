# Derecho de petición y acción de tutela · videos de profe (20 nov 2026)

Curso «Derecho de petición y acción de tutela: régimen constitucional, legal y jurisprudencial para servidores
públicos» (Prioridad 3). Profe: **Óscar Jairo Fonseca Fonseca**, autor del curso (lo dice él en el inicio del curso y
es el «1.5 Autor» de los vaciados). **Entrega provisional**: intro, cartón de título, rótulo, cartón de cierre y
outro; el cuerpo va sin gráficos.

## Lo que pide el documento y lo que hay

El formato de diseño pide, por unidad, «video de presentación», «video de retroalimentación de la evaluación» y
«video de cierre, síntesis y conclusiones»; la guía de recursos nombra además «videos de bienvenida». Llegaron siete
grabaciones (`E:\DAE MASTER\CURSO DERECHOS DE PETICION\`), que dan **seis piezas**:

| plan | pieza | fuente | dura | cortes |
|---|---|---|---|---|
| `plan_dpci` | inicio del curso | `VIDEO 1 PRESENTACION GENERAL DEL CURSO - TOMA1` | 7:57 | dos tomas fallidas y la charla del principio |
| `plan_dpu1i` | U1 inicio | `VIDEO2 - PRESENTACION UNIDAD 1 - TOMA 2` (la toma 1 no entra) | 6:32 | tres tramos de la toma 2 |
| `plan_dpu2i` | U2 inicio | `VIDEO2 - PRESENTACION UNIDAD 2- TOMA 1` | 7:30 | una toma fallida |
| `plan_dpu3i` | U3 inicio | `VIDEO4 - PRESENTACION UNIDAD 3- TOMA 1` | 7:34 | — |
| `plan_dpu4i` | U4 inicio | `VIDEO5 - PRESENTACION UNIDAD 4- TOMA 1` | 7:32 | tres tomas fallidas |
| `plan_dpu1c` | U1 cierre | `VIDEO6 - CIERRE UNIDAD 1- TOMA 1` | 27:04 | dos tomas fallidas |

Faltan: el cierre de la U4 y las retroalimentaciones (no hay grabación). Los cierres de U2 y U3 y el cierre del curso
llegaron el 21 nov (ver abajo).

- **Qué se corta**: lo que el profe le dice al técnico entre tomas («Suspendamos ahí, por favor, Camilo»), la toma
  fallida que viene antes y la conversación del principio y del final. Cada plan dice qué sale y por qué.
- **Qué no se toca**: los tropiezos sueltos de una palabra sin disculpa («se exis— se presentó», «Presentaremo—
  prestaremos», «a una pie— a una persona»), como en Desaparición forzada.
- **Bordes**: a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última,
  comprobados en RMS de 10 ms (`D:\DAE\_tmp\dp_p\rms_bordes.py`). Seis cuadros de mezcla en cada corte (`SUAVE`).

## Cómo se arma

- `base_dp_profe.py` y los nueve planes; `lote/cadena_dp.py` (compuesto, cartón de título y rótulo, tres a la vez) y
  `lote/entrega_gpu.py` (línea de Resolve y entrega por la placa NVIDIA, ~5 Mb/s, fuera de receta, como en
  Desaparición forzada). Se lanzan desde el repo (`D:\DAE\_repo\cursos\derecho_peticion\profe\lote\`) con
  `D:\DAE\_tmp\dp_p\` como carpeta de trabajo (`cola.txt` y los logs).
- Árbol: `D:\DAE MASTER\PRIORIDAD 03\CURSO DERECHO DE PETICION - VIDEOS PROFE\<CURSO|UNIDAD n>\<INICIO|CIERRE>`.
- Rótulo abajo a la **derecha** (x=1330): las manos del profe entran a menudo en la esquina de la izquierda.

## Entregas (20 nov 2026)

Las seis, entre las 20:02 y las 20:25 (hora de Colombia), en Drive: carpeta del curso «Derecho de petición, acción de
tutela y daño antijurídico…» (`1cFcqb0KRRcI-z2YqvpjHMzroUGq2LaUw`) › **VIDEOS PROFE** (`1KXrk6azeO_3KQhsvM2p8z8AVrTaaXmBX`,
creada para esto), cada una con su `.srt` al lado (y en `05 EXPORTS` junto al video). Render por la placa NVIDIA desde
Resolve, ~5,4 Mb/s (fuera de receta, como en Desaparición forzada). Sonido: −16,0 a −16,1 LUFS, pico −2,8 a −3,0.

| video | dura | MB | id en Drive | `.srt` |
|---|---|---|---|---|
| `derechodepeticion - CURSO - INICIO-v2.mp4` | 8:31 | 325 | `1XFDMwmEK0RoTBVsLnSgzmp-RAXXKdmet` | `1eH4awdo2WmU0e65_L_lhEzYHktijS-xD` |
| `derechodepeticion - U1 - INICIO-v1.mp4` | 7:06 | 272 | `1QW5rmivoBDnp9C5dNuSm6I6qsafsgF04` | `1o9iL2poXvcXcEishauYAN_5mcN4_Mb4P` |
| `derechodepeticion - U2 - INICIO-v1.mp4` | 8:04 | 309 | `1wdhgCIlmMwl3QmudzAiWs6xxjqRGhbIG` | `11VjFDvrPQYR26n4ZI06S-zc45mwaJILS` |
| `derechodepeticion - U3 - INICIO-v1.mp4` | 8:08 | 312 | `13Y6c7j1fkd7qwLoSrG9eqMnIiqZojJB_` | `1YMZmfAryjFLWFffvxHR91FUKTScifTs0` |
| `derechodepeticion - U4 - INICIO-v1.mp4` | 8:06 | 311 | `1AWt9am_EMSO5pz1JWNo1VaZgzG7MiDAv` | `10GY_MZXMmcU0Z1FMaQwL4uwH35QlbOpL` |
| `derechodepeticion - U1 - CIERRE-v1.mp4` | 27:38 | 1062 | `1BcTOOisIWxosEkWsf4TSVqEijVOby9zh` | `1-Ykv_ckWIoQ0SZEFZXPWG3eIpXw4mK9y` |

- **Verificadas contra el disco**: copia de servidor en `_MA subidas` (`verif_<clave>.mp4`), comparada por bloques con la
  de `05 EXPORTS` (`D:\DAE\_tmp\dp_p\verif_loop.py`, `verif.log`: seis «OK»); después el video pasó a VIDEOS PROFE y
  la copia, a la papelera. (`verificar_drive.py` con un mapa de piezas que todavía no existen en disco se cae al primer
  `getsize`: para una tanda que va saliendo, el bucle.)
- Hojas de revisión (`<TMP>/hoja_rev_1.jpg`) miradas en las seis: intro, cartón de título (tres renglones de curso y el
  subtítulo de la unidad), rótulo, cartón de cierre y outro. Tiras de los cortes (`profe_sim.py … c1@t`): la mezcla de
  seis cuadros entre tomas se ve como una disolvencia corta.
- **Rótulo de la U4**: el profe abre las manos mientras está el rótulo y una mano pasa por detrás del nombre cerca de un
  segundo (cuadros 540–600 de la entrega). El texto se lee; si molesta, se mueve el rótulo a otro momento y sale una v2.
- **Inicio del curso v2 (20 nov, 21:00).** Sebastián: «por lo menos en uno de los videos no veo el rótulo del
  profesor». Medido en las seis entregas (píxeles de la barra amarilla en la esquina del rótulo): estaba en todas, pero en
  el inicio del curso entraba en el 1:31, cuando dice su nombre, y en las demás al empezar (0:18). La v2 lo lleva al
  empezar, como las demás; misma línea con otro nombre de rótulo, mismo compuesto. La línea de la v1 quedó como «DP -
  CURSO - INICIO v1 rotulo tarde» (`SetName` con «:» o «,» en el nombre devuelve False y no renombra). Verificada byte a
  byte. El `.srt` de la v1 está en la papelera; **el video v1 sigue en VIDEOS PROFE** (la papelera no se aplicó a ese
  archivo): queda para que Sebastián lo quite.

## Cierres de las unidades 2 y 3 (21 nov 2026)

Sebastián: «tenemos nuevos videos en la carpeta de derechos de petición… cierre de unidad 2 y cierre de unidad 3, procésalos de
pe a pa, con gráfica provisional, compón de ser necesario, edita, verifica todo, exporta, sube, actualiza». Llegaron tres
grabaciones nuevas en `E:\DAE MASTER\CURSO DERECHOS DE PETICION\` (mismo profe, misma cámara y mismo fondo que las demás):

| plan | pieza | fuente | dura | cortes |
|---|---|---|---|---|
| `plan_dpu2c` | U2 cierre | `Derecho de petición - Unidad 2 Cierre Toma 1.mp4` (29:42) + `… Toma 2.mp4` (2:29) | 28:38 | la charla con el técnico, cuatro frases repetidas y el cambio de toma |
| `plan_dpu3c` | U3 cierre | `Derecho de petición Unidad 3 cierre.mp4` (30:47) | 29:36 | cinco arranques en falso y una pausa |

- **U2: se compone con las dos tomas.** La toma 1 termina en «Pauso porque tengo un ruido acá… Voy a pausar»; la toma 2 dice
  «Retomo este video desde la anterior pausa» y lee el párrafo de «Quien recibe puede advertir una barrera…» y el resto del
  guion. El cambio de toma va en «…trabajar coordinadamente. | Quien recibe…» (la toma 2 lee ese párrafo de corrido con lo que
  sigue). Las dos tomas se pegaron en una sola fuente **sin recodificar el video** (`01 VIDEO/dpu2c_fuente_unida.mov`: demuxer
  `concat` con `duration` = 53.465 cuadros / 30, audio en PCM), comprobado con `framemd5` en la costura, a mitad de la toma 1 y
  a los 100 s de la toma 2: los cuadros son idénticos a los de las tomas. NVENC desde ffmpeg no sirve en esta máquina (el
  controlador es más viejo que el que pide ffmpeg 9), por eso la copia.
- En esta grabación el técnico es otro («profesor Juan») y le dice al profe que no pare, que ellos editan: el profe dice en voz
  alta desde dónde retoma («Retomo desde la línea anterior…», «Que retomo la línea desde los lineamientos»). Cada plan dice qué
  sale y por qué; los bordes, en RMS de 10 ms (`D:\DAE\_tmp\dp_p\bordes_c23.json`).
- **U3:** una sola toma con cinco arranques en falso que el profe anuncia, y una pausa de 7,9 s que se acorta.
- El rótulo, abajo a la derecha como en las otras seis: el profe está en el centro del cuadro.

### Entregas (21 nov 2026)

Las dos a las 19:09 y 19:13 (hora de Colombia), en VIDEOS PROFE, cada una con su `.srt` al lado (y en `05 EXPORTS` junto
al video). Render por la placa NVIDIA desde Resolve, ~5,4 Mb/s, a 23,976 cuadros/s. Sonido: −16,0 LUFS,
pico −2,9.

| video | dura | MB | id en Drive | `.srt` |
|---|---|---|---|---|
| `derechodepeticion - U2 - CIERRE-v1.mp4` | 28:38 | 1105 | `1r9L05LW7-4SxOBDJyut2l0q2D9u4Nmvq` | `1jnD281rx1AHRjNbPkkP5igRFg-UuTeEX` |
| `derechodepeticion - U3 - CIERRE-v1.mp4` | 29:36 | 1140 | `11xGfvAf_oNwAWzvDAOFXG8d3JBAAp4KT` | `1b27yvO4fLn1WSaKBv9sFK5mWjUTru9xW` |

- **Verificadas byte a byte** contra `05 EXPORTS` (copia de servidor `verif_<clave>.mp4` en `_MA subidas`,
  `D:\DAE\_tmp\dp_p\c23\verif.log` y `verif_2.log`); después el video pasó a VIDEOS PROFE y la copia, a la papelera.
- Hojas de revisión miradas en las dos (intro, cartón de título con «Unidad 2. Gestión y respuesta del derecho de petición»
  y «Unidad 3. Acción de tutela: fundamentos y procedencia», rótulo, cartón de cierre y outro).
- **Los cortes, comprobados en la transcripción de la entrega** (Scribe sobre el MP4 final) contra la de las grabaciones
  con los mismos tramos: U2 0,996 de coincidencia (ninguna palabra de más ni de menos en los cortes ni en el cambio de
  toma), U3 0,981 (las únicas diferencias grandes son los seis tramos que salen).
- **Primer intento de entrega fallido:** Resolve estaba en «Untitled Project» (página `None`, Master vacío) y
  `entrega_gpu` no pudo armar las líneas (`'NoneType' object has no attribute 'GetSubFolderList'`). Se cargó «DAE MASTER -
  CURSOS» (`LoadProject` pasa de los 58 s del `run_inline`: se sigue cargando; se espera mirando
  `GetCurrentProject().GetName()`) y se relanzó; con `cola.txt` como estaba, rehízo solo lo que faltaba.

## Cierre del curso (21 nov 2026)

Sebastián: «acabo de incluir el cierre de todo ese curso, por favor procésalo». Llegó `Derecho de petición - Cierre.mp4`
(14:23,4) a la misma carpeta, a las 21:21: una sola toma, mismo profe, cámara y fondo.

| plan | pieza | fuente | dura | cortes |
|---|---|---|---|---|
| `plan_dpcc` | cierre del curso | `Derecho de petición - Cierre.mp4` (14:23) | 14:23 | dos arranques en falso |

- Salen «La precisión protege a quien solicita la atención y la propia entidad. Voy a retomar desde la precisión» (la
  frase se vuelve a leer entera) y «El paso a siguientes— retomo en esa frase el paso siguiente». Los bordes, en RMS de
  10 ms (`D:\DAE\_tmp\dp_p\cc\bordes.json`); el de entrada va a 0,84 s de la primera palabra porque de 6,32 a 7,0 hay
  respiración.
- El profe nombra al final a su estudiante auxiliar («en compañía de mi estudiante auxiliar Miguel Ángel Torres»): va
  en el subtítulo; el rótulo sigue siendo solo el del profe.
- Cartón de título «Cierre del curso», rótulo a 1,5 s del arranque, como el inicio del curso.

**Entrega** (21:34, hora de Colombia), en VIDEOS PROFE con su `.srt` al lado (y en `05 EXPORTS`): render por la placa
NVIDIA desde Resolve, ~5,4 Mb/s, −16,0 LUFS, pico −2,9.

| video | dura | MB | id en Drive | `.srt` |
|---|---|---|---|---|
| `derechodepeticion - CURSO - CIERRE-v1.mp4` | 14:23 | 553 | `1ryxSVw1DRsPGEm5QLtN-8wK9st40rXhP` | `1b6IVHVNjz7htI-d_0SqN_mid58K93-Sy` |

- Hoja de revisión mirada (cartón de título con «Cierre del curso», rótulo, cartón de cierre y outro). Los cortes,
  comprobados en la transcripción de la entrega contra la de la grabación en los mismos tramos: 1.713 palabras de cada
  lado, 0,999 (la única diferencia es una tilde).
- **Verificada byte a byte** contra `05 EXPORTS` (`verif_dpcc.mp4` en `_MA subidas`, `D:\DAE\_tmp\dp_p\cc\verif.log`);
  después pasó a VIDEOS PROFE y la copia, a la papelera.

