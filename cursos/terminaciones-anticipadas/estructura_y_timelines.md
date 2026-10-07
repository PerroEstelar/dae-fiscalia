# Dónde está cada cosa, y cuál es la timeline buena

Había **dos estructuras superpuestas** dentro de `CURSO 4 - TERMINACIONES
ANTICIPADAS`, y eran el origen de la confusión:

1. Un árbol viejo `UNIDAD 4 → LECCIÓN 4.1/4.2/4.3 → CASO 01…09`, hecho cuando la
   numeración todavía seguía el orden del documento del profesor. Ahí el «CASO 01»
   era el doble beneficio y el «CASO 05» eran los tres escenarios.
2. Un árbol plano `CASO 01…08` con la numeración definitiva —la de la selección de
   ocho— y con todo el material real adentro.

Las cuatro timelines terminadas estaban guardadas en el árbol viejo, dentro de un
«CASO 01» que no es el caso 01. De ahí que abrir la carpeta correcta no llevara a
la línea correcta.

El árbol viejo ya no se usa. Quedó bajo `_NO USAR - estructura vieja por
lecciones`, sin borrar nada, para poder consultarlo si hace falta.

## Las dos unidades

La selección de ocho casos reparte **cinco en la Unidad 4** (preacuerdos y
negociaciones) y **tres en la Unidad 1** (archivo de la indagación). El número del
caso no cambia al entrar en su unidad: el caso 06 se sigue llamando caso 06.

| | caso | unidad |
|---|---|---|
| 01 | Los tres escenarios probatorios | **U4** · lección 4.2 |
| 02 | El doble beneficio y el reintegro | **U4** · 4.1 |
| 03 | Coautoría, complicidad y subrogados | **U4** · 4.3 |
| 04 | La marginalidad alegada sin sustento | **U4** · 4.1 |
| 05 | La negociación paso a paso | **U4** · 4.2 |
| 06 | El hurto de madrugada | **U1** · 1.1 |
| 07 | ¿Incumplimiento contractual o delito? | **U1** · 1.1 |
| 08 | El video que aparece seis meses después | **U1** · 1.3 |

## El árbol, igual en disco y en el pool

```
CURSO 4 - TERMINACIONES ANTICIPADAS
├── 00 GUIONES                      (el docx del curso, para todo)
├── 00 PLANTILLA                    TA - CASO 01 - PLANTILLA
├── UNIDAD 1 - ARCHIVO DE LA INDAGACION
│   ├── CASO 06 - hurto de madrugada
│   ├── CASO 07 - incumplimiento o delito
│   └── CASO 08 - video seis meses despues
├── UNIDAD 4 - PREACUERDOS Y NEGOCIACIONES
│   ├── CASO 01 - tres escenarios probatorios
│   ├── CASO 02 - doble beneficio y reintegro
│   ├── CASO 03 - coautoria complicidad y subrogados
│   ├── CASO 04 - marginalidad sin sustento
│   └── CASO 05 - negociacion paso a paso
├── _ARCHIVO versiones sin voz      las cuatro líneas viejas, sin voces
└── _NO USAR - estructura vieja por lecciones
```

Y dentro de cada caso, las mismas diez:

```
01 PLANOS · 02 CARTONES · 03 VOCES · 04 B-ROLL · 05 EXPORTS
06 GUION Y STORYBOARD · 07 MUSICA · 07 MOVIMIENTO · 08 A LA VOZ
09 TIMELINE SEBASTIAN
```

## `09 TIMELINE SEBASTIAN`

La carpeta nueva. Es la respuesta a «¿cuál abro?»: **la única timeline que hay
ahí dentro es la buena**, y no hay ninguna otra en ninguna otra parte del caso.

| caso | timeline | cuadros | duración |
|---|---|---|---|
| 02 | `TA CASO 02 - a la voz` | 3 400 | 2:21 |
| 06 | `TA CASO 06 - a la voz` | 3 283 | 2:16 |
| 07 | `TA CASO 07 - a la voz` | 3 068 | 2:07 |
| 08 | `TA CASO 08 - a la voz` | 2 032 | 1:24 |

En disco la misma carpeta lleva dos archivos:

- el `.drt` de esa timeline, exportado, reimportable con *Archivo → Importar →
  Timeline* si el proyecto de Resolve se dañara;
- un `LEER - esta es la buena.txt` que dice el nombre, la ruta en el pool y la
  duración, para no tener que abrir Resolve sólo para saberlo.

Lo que distingue a estas cuatro de cualquier otra versión: llevan las voces de
ElevenLabs en **A2** (narrador) y **A3** (preguntas), y su rejilla sale de los
silencios medidos de la voz, no de la fórmula `palabras ÷ 142 × 60`.

Las versiones anteriores, sin voz, están en `_ARCHIVO versiones sin voz` con el
prefijo `ARCHIVO sin voz -`. No se abren para trabajar.

## Mover carpetas en disco rompe los enlaces

Las ocho carpetas de caso cambiaron de ruta, así que los 240 clips del pool
quedaron apuntando a sitios que ya no existen. Se arregló con una sola llamada
por caso:

```python
mp.RelinkClips(clips_del_caso, ruta_nueva_de_la_carpeta)
```

`RelinkClips` busca recursivamente dentro de la carpeta que se le pasa, así que
basta darle la raíz del caso y encuentra los `01 PLANOS`, `07 MOVIMIENTO` y demás
por su cuenta. Quedaron 0 sin resolver y las cuatro timelines sin un solo clip
offline.

Los dos clips comunes del Caso 02 —el intro de la FGN y el video de criptoactivos—
nunca vivieron bajo la carpeta del caso y por eso no necesitaban relink.
