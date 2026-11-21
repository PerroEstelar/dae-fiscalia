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

Faltan: los cierres de U2 a U4, las retroalimentaciones y el cierre del curso (no hay grabación).

- **Qué se corta**: lo que el profe le dice al técnico entre tomas («Suspendamos ahí, por favor, Camilo»), la toma
  fallida que viene antes y la conversación del principio y del final. Cada plan dice qué sale y por qué.
- **Qué no se toca**: los tropiezos sueltos de una palabra sin disculpa («se exis— se presentó», «Presentaremo—
  prestaremos», «a una pie— a una persona»), como en Desaparición forzada.
- **Bordes**: a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última,
  comprobados en RMS de 10 ms (`D:\DAE\_tmp\dp_p\rms_bordes.py`). Seis cuadros de mezcla en cada corte (`SUAVE`).

## Cómo se arma

- `base_dp_profe.py` y los seis planes; `lote/cadena_dp.py` (compuesto, cartón de título y rótulo, tres a la vez) y
  `lote/entrega_gpu.py` (línea de Resolve y entrega por la placa NVIDIA, ~5 Mb/s, fuera de receta, como en
  Desaparición forzada), los dos en `D:\DAE\_tmp\dp_p\`.
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
