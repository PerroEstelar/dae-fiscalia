# Terminaciones anticipadas — subtítulos (18 nov 2026)

Prioridad 1 del pedido de Esteban: los 19 videos del aula 119. Cómo se hacen: `herramientas/subtitulos/README.md`.
`manifiesto.json` tiene cada video (ruta local, nombre y carpeta de Drive); `correcciones.json`, lo que se corrigió
en cada uno.

| video | subtítulos | dura | id del `.srt` en Drive |
|---|---|---|---|
| `terminacionesanticipadas - CURSO - INICIO-v1` | 136 | 8:38 | `12env-z7_zHp0dTkvvBJ6RBtZ8Il7e3A8` |
| `terminacionesanticipadas - CURSO - CIERRE-v1` | 124 | 8:26 | `1AQOAKkKXshyi8UXTgClTOf3MgSkHwuJS` |
| `terminacionesanticipadas - U1 - INICIO-v1` | 115 | 7:26 | `1Jm8TPYOihnYR6CNpAF6W1p9sasHdCvhh` |
| `terminacionesanticipadas - U1 - CIERRE-v1` | 98 | 6:32 | `1X252Fq289bpuya5wBPlWQjmxI4TzwGsl` |
| `terminacionesanticipadas - U2 - INICIO-v1` | 118 | 8:06 | `1P5NLtV5EGk2oi7MTz84GxZajGteFNJxI` |
| `terminacionesanticipadas - U2 - INICIO-v2` (la repetición, cortada) | 111 | 7:36 | `1RpFTMut3hRHlQtGZW84VvKbVjLE3P1HG` |
| `terminacionesanticipadas - U2 - CIERRE-v1` | 97 | 6:33 | `1hJO_TZ9P1ns1vnds3jttX6ongrgOSyZF` |
| `terminacionesanticipadas - U3 - INICIO-v1` | 114 | 7:25 | `1VPvLHiRU6tmtmN-NI-WJDDhEdIzgBaZ0` |
| `terminacionesanticipadas - U3 - CIERRE-v1` | 100 | 6:39 | `1iRFstqPQ-H3GJil_dU42-oocXEtPJjBr` |
| `terminacionesanticipadas - U4 - INICIO-v1` | 125 | 8:22 | `1f_HKxkDBCFWZd8sWr7aPmjtxRgSKmcbi` |
| `terminacionesanticipadas - U4 - INICIO-v2` (la repetición, cortada) | 115 | 7:49 | `1Yp6hmNmwgfW7dGsCHrP-VLqLjrDafV7N` |
| `terminacionesanticipadas - U4 - CIERRE-v1` | 112 | 7:37 | `1FBKz5u8-C8KtYn1BwlJq4PH9NLJ-YHK_` |
| `terminacionesanticipadas - U4 - CIERRE-v2` (la repetición, cortada) | 109 | 7:27 | `1QGsNzNcKw22qaN0hXwRVtELX67f124Lf` |
| `TA - U1 - CASO 06 - V1` | 34 | 2:17 | `11fI14on_jSt-qXLRRXav7pn53c_xqYrb` |
| `TA - U1 - CASO 07 - V1` | 31 | 2:08 | `1ujXMx76meZoyau6_jTvH_oMQWLft7eo4` |
| `TA - U1 - CASO 08 - V1` | 17 | 1:25 | `1rHR0TBMwl8k0oRcXVsBBlLSOLLeyhYzw` |
| `TA - U1 - CASO 09 - V1` | 15 | 1:25 | `1PTnFOxgwpI33hJ0DXMuTDHWh5LyN3qKz` |
| `TA - U4 - CASO 01 - V1` | 62 | 3:59 | `1g1LZuI88zpKwsz-cH-nj-9WE-OHon5tx` |
| `TA - U4 - CASO 02 - V1` | 31 | 2:22 | `19PfdGLGir_V3VuA_nEH0fjx1eogK6JQD` |
| `TA - U4 - CASO 03 - V1` | 71 | 4:40 | `1zlMjyblOYQ2CadF7EsNesmb7F_vAXYGJ` |
| `TA - U4 - CASO 04 - V1` | 40 | 2:36 | `1ypUHw-z5Bxb_Yt_gxFLmglG-thht8wYd` |
| `TA - U4 - CASO 05 - V1` | 76 | 4:59 | `1JByosta8Kdp7Qnkm-1PzzGJPEr0zvK6c` |

Cada `.srt` está en la carpeta de Drive de su video y junto al video en disco (`05 EXPORTS`, con el nombre de Drive:
los casos tienen otro nombre en disco). Se comprobó que el archivo local de cada video pesa lo mismo que el de Drive.
El `.srt` de un caso se leyó de vuelta de Drive y es idéntico al local. Trabajo: `D:\DAE\_tmp\subs\ta\`.

## Tomas repetidas que quedaron en tres videos entregados el 17 nov

Aparecieron al leer las transcripciones. El documento de esa entrega decía «hay tropiezos sueltos que se dejaron»:
estos tres no son tropiezos, y el compuesto debió cortarlos.

| video | dónde | qué pasa |
|---|---|---|
| U2 – INICIO | 0:17,6 a 0:47,5 | arranca, dice «ah, voy a volver a empezar» y empieza de nuevo |
| U4 – INICIO | 0:55,6 a 1:28,8 | «volver a hacer ese párrafo» y repite el párrafo |
| U4 – CIERRE | 0:17,5 a 0:25,8 | repite las dos primeras frases |

**Cortadas el 18 nov** (Sebastián: «haz los cambios ya», «solo corta esas partes», «para evitar reprocesar todo»),
sobre el MP4 entregado y sin reprocesarlo, con `herramientas/montaje/recortar_entrega.py`. Salieron como `-v2`; las
`-v1` y sus `.srt` siguen en la carpeta.

| entrega | corte (cuadros de la línea de la v1) | cuadros | copiados sin tocar | Drive |
|---|---|---|---|---|
| `terminacionesanticipadas - U2 - INICIO-v2.mp4` | 409–1129 (30,0 s) | 10.929 | 10.689 | `15hegG6gr3fJa_MYBfpyNpE1aGiiizCKo` |
| `terminacionesanticipadas - U4 - INICIO-v2.mp4` | 1321–2115 (33,1 s) | 11.243 | 11.226 | `1XWPje2Ts283xiJ6Zplqa0hWrHnw7lzl0` |
| `terminacionesanticipadas - U4 - CIERRE-v2.mp4` | 409–628 (9,1 s) | 10.726 | 10.465 | `18I-JJTa52X12iciAvrv-zVVR20evQgza` |

Las tres: −16,0 LUFS y −3,0 dBTP, 0 muestras de desfase contra el compuesto, y comparadas byte a byte con una copia
de servidor antes de moverlas a la carpeta de la unidad. En el inicio de la U4 el corte cae en medio del video
(0:55) y es un corte directo. Los `.srt` de las `-v2` se hicieron transcribiendo el archivo nuevo (claves
`tau2i_v2`, `tau4i_v2`, `tau4c_v2`): el texto es el de la `-v1` menos la repetición, palabra por palabra. Scribe no
devuelve dos veces lo mismo en los tropiezos, así que las reglas de la `-v1` no alcanzan y cada `-v2` lleva las suyas.

Quedan en el video dos frases que el profe rehace sobre la marcha, que no son tomas repetidas y no se cortaron: U1 –
CIERRE (hacia 4:30, «mi recomendación es que no comiencen pensando… mi recomendación es que no comiencen
redactando»; el subtítulo lleva solo la segunda) y U2 – INICIO-v2 (0:34 a 0:46, «La decisión no depende únicamente
de la convicción del fiscal sobre el caso. La decisión no depende únicamente de la convicción del fiscal de que el
caso no debe continuar»; el subtítulo lleva las dos).
