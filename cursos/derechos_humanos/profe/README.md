# Derechos humanos · videos de profe a cámara

Pedido de Sebastián (16 nov 2026): «tenemos otro inicio de curso profe hablando a cámara,
necesito que lo proceses de pe a pa con todos los protocolos y requerimientos establecidos».
El formato es el de Enfoque diferencial y Bienes: intro FGN, cartón de título con el nombre
del curso y el de la pieza, el profe con cartones de caja, listas de AE y lower third, cartón
de cierre y outro. Base común: `base_dh_profe.py`.

## Profe

**Yefri Yoel Torrado Verjel**, coautor del curso. En el video no dice su nombre y ningún
documento del Drive dice quién graba. La ficha lista tres autores (Estanislao Escalante Barreto,
Yefri Yoel Torrado Verjel, Laura Juliana Galvez Depablos); no es Estanislao, que es el profe de
SRPA. Lo confirmó Sebastián. El cargo del lower third es el que pidió: «Coautor del curso
Derechos humanos aplicados a la función judicial».

## Fuentes

Drive del curso (de JP) → `VIDEOS` (`16xDO2LgXTBunKGEeu8BQzzMZ6pY-kX6w`):

| archivo | qué es | estado |
|---|---|---|
| `01. Video Presentación.mp4` | presentación del curso, toma cruda 1620×1080, 4:05,7 | **entregado** (`plan_dh00`) |
| `DDHH_funcion_inio_curso/` | la misma toma, recortada en Camtasia y a 720p | no se usa |
| `DDHH_funcion_inio_unidad1/` | paquete de Camtasia del inicio de la U1 (4:11 según su xml) | **falta el mp4**: solo están el html, el xml y las carpetas; tampoco hay crudo «02» |
| `DDHH_funcion_cierre_unidad1/` | la misma toma del cierre U1, a 720p | no se usa |
| `3. Video Cierre U1.mp4` | cierre U1, toma cruda 1620×1080, 2:29,2 | **entregado** (`plan_dh1c`) |
| `4. Video Inicio U2.mp4`, `05. Video Cierre U2.mp4` | U2 | sin procesar |
| `06. Video Inicio U3.mp4`, `07. Video Cierre U3.mp4` | U3 | sin procesar |
| `08. Video Inicio U4.mp4`, `09. Video Cierre U4.mp4` | U4 (cierre 2:58) | sin procesar |

Los cierres de la U1 y la U4 se transcribieron al principio y al final buscando el nombre del
profe: no lo dice.

## Ventana y columna

Toda la fuente a lo ancho: 1620×912 desde (0, 40), ×1,185. La cabeza queda desde x≈750 de
salida, así que la columna de cartones y listas es de 520 (`MAXW`) y el lower third va con el
nombre a 40 px y el cargo a 410 de ancho. Plano cerrado para los cortes: 1472×828 desde (0, 40).
Pruebas: `D:\DAE\_tmp\dh_profe\caja_A.jpg` (caja sobre 16 cuadros) y `sim\sim_dh00.jpg`
(cartones y lower third rendidos sobre el compuesto).

## Entregas

Drive: «Videos» del curso (`1Oa_NdV5Uwl6IgMccYY-BO38RofKr7iAk`) → «VIDEOS PROFE - Yefri Yoel
Torrado Verjel» (`1O1O4kbtNFGO4N7vtb-Ydph5K4PUZ3EQ1`).

| pieza | plan | línea | entrega |
|---|---|---|---|
| Presentación del curso | `plan_dh00` | `DH - CURSO - PRESENTACION` | `PRIO 2 - DERECHOS HUMANOS - PRESENTACION DEL CURSO-v1.mp4` |
| Cierre de la unidad 1 | `plan_dh1c` | `DH - U1 - CIERRE PROFE` | `PRIO 2 - DERECHOS HUMANOS - UNIDAD 1 CIERRE-v1.mp4` |

**Presentación del curso (16 nov 2026).** 6447 cuadros (4:28,9) = la línea; −16,1 LUFS, pico
−2,0 dBTP; PSNR contra el máster 50,3 dB; 136 MB (`12hd2DkrGdZq__PXacd_fJYTTqe7yaJU7`). El
máster de 32 Mb/s (901 MB) queda en `05 EXPORTS\_master`, el `.drt` en `10 TIMELINE SEBASTIAN`.
- Dos cortes: el arranque en falso («…un listado de trabajos. Un, dos, tres.», 45,50–53,80) y
  la pausa de 3,6 s antes de «Al final…» (205,70–208,25), cada uno seguido del plano cerrado.
- 14 cartones, 3 listas de AE (las cuatro decisiones, lo que se hace en cada unidad, las tres
  reglas prácticas) y el lower third. Cobertura ≈ 77 % (pieza corta).
- La copia del Drive para trabajar (`_MA subidas/_DH profes`) se mandó a la papelera; la fuente
  quedó en `PRESENTACION DEL CURSO\01 VIDEO`.

**Cierre de la unidad 1 (16 nov 2026).** 4395 cuadros (3:03,3) = la línea; −16,2 LUFS, pico
−2,8 dBTP; PSNR contra el máster 50,5 dB; 95 MB (`1bBsHJlybjJ2ZWluuPNonQL3EQ78lnZlW`). Disco:
`…\UNIDAD 1 - CIERRE PROFE\` (máster de 637 MB en `05 EXPORTS\_master`, `.drt` en
`10 TIMELINE SEBASTIAN`, fuente en `01 VIDEO`).
- Sebastián mandó el enlace de la versión de Camtasia; se usó la toma cruda. Las dos
  transcripciones calzan palabra por palabra: JP solo le quitó 1,4 s de cola. Va entera.
- Cartón de título: «Unidad 1. El fiscal como garante: fundamentos de los derechos humanos y doble
  incidencia de la función fiscal» (nombre de la ficha), como en SRPA.
- 11 cartones (uno con antetítulo por cada parte del repaso), 2 listas de AE (las tres
  dimensiones de la dignidad, lo que implica garantizar) y el lower third. Cobertura ≈ 77 %.
- El primer `mg_armar` cortó por el timeout de 30 s de aftr (importaba los íconos nuevos). Se
  mataron la cadena y la entrega que esperaba, no se había rendido nada, y se volvió a correr con
  la máquina libre: 37 s.
