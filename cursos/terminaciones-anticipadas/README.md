# Curso Terminaciones Anticipadas · serie de casos en video

Ocho casos del *Curso Terminaciones Anticipadas* (FGN – UNAL) convertidos en piezas
cortas de video. Cinco salen de la Unidad 4 (preacuerdos y negociaciones) y tres de la
Unidad 1, para que la serie quede equilibrada entre las dos unidades.

El criterio de selección y la transcripción verbatim de cada caso están en
`fuentes/TA_Seleccion_8_Casos.md`.

## Regla de contenido

El contenido jurídico sale **del material escrito por los profesores**, verbatim o
parafraseado de cerca. No se inventa doctrina, no se completan vacíos del guion con
conocimiento general. Cuando a una lección le falta el texto expositivo, se marca el
hueco y se busca la fuente del profesor antes de escribir.

## Qué hay acá y qué no

Este repo guarda **texto**: guiones, prompts, rejillas, scripts y decisiones. Las
imágenes, los audios y los renders viven en disco, en `E:\DAE MASTER`, y se referencian
por ruta desde cada documento. Un PNG de 2560 × 1440 pesa ~8 MB y git no es el lugar
para eso.

```
cursos/terminaciones-anticipadas/
  README.md                       este archivo
  fuentes/                        material del curso y la selección de casos
  casos/<caso>/                   un folder por caso
    00_preproduccion.md           guion, bloques de voz, rejilla, cartones
    01_guion_y_prompts.md         guion definitivo + keyframes y b-roll
    02_seleccion_keyframes.md     qué variante quedó y por qué
```

## Estado

| # | Caso | Unidad | Estado |
|---|---|---|---|
| 01 | Tres escenarios probatorios | 4 | pendiente |
| 02 | El doble beneficio y el reintegro | 4 | **keyframes generados y escogidos** |
| 03 | Coautoría, complicidad y subrogados | 4 | pendiente |
| 04 | Marginalidad sin sustento | 4 | pendiente |
| 05 | La negociación paso a paso | 4 | pendiente |
| 06 | Hurto de madrugada | 1 | pendiente |
| 07 | ¿Incumplimiento o delito? | 1 | pendiente |
| 08 | El video seis meses después | 1 | pendiente |

## Formato de la serie

23,976 fps · 1920 × 1080 · DaVinci YRGB, Rec.709 (Scene) · scaleToFit.
Intro 194 f · cartón de entrada 119 f · cartones de pausa 144 f · cartón de cierre
119 f · outro 194 f. Locución a 150 palabras por minuto; la duración de una pieza se
estima como `palabras ÷ 150 × 60 × 1,10 + 30 s`.

Los detalles de método —la rejilla de cartones, los niveles de audio, las trampas de
la API de Resolve y el método de prompts— están en `CLAUDE.md`, en la raíz del repo.
