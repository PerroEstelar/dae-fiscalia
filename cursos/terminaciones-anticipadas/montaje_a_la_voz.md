# Las tres piezas, montadas contra la voz

Hasta aquí las rejillas salían de la fórmula `palabras ÷ 142 × 60`. Ahora salen
de la voz: se midieron los silencios de cada pista con `silencedetect` y cada
cartón de pregunta dura exactamente lo que dura su pregunta en boca del narrador.

## Las voces

Generadas por la API de ElevenLabs desde `herramientas/voz/elevenlabs.py`, con
dos voces colombianas de la biblioteca, alternadas:

| | narración | preguntas |
|---|---|---|
| Caso 02 | Carlos | Elisa María |
| Caso 06 | Elisa María | Carlos |
| Caso 08 | Carlos | Elisa María |

Multilingüe v2, estabilidad 0,50, similitud 0,80, *style* en 0. 4.406 caracteres
en total.

### El bug de los −16 no era loudnorm

Veníamos creyendo que `loudnorm` en una pasada estimaba mal, porque pedíamos −19
y salía −16. **No era eso.** Era el orden: el máster convertía a estéreo
dual-mono *después* de normalizar, y duplicar un canal mono en L y R suma 3 dB a
la medida EBU R128. Exactamente los 3 dB que faltaban.

El orden correcto, que es el que está en el repositorio:

1. `aresample` a 48 kHz
2. `pan=stereo|c0=c0|c1=c0` — se arma el dual-mono
3. **y solo entonces** medir y normalizar

Las seis quedaron entre −18,8 y −19,1 LUFS, con pico bajo −1,0 dBTP.

## Cómo se mapearon los silencios

`silencedetect` devuelve todas las pausas, incluidas las comas. Para separar las
pausas de párrafo de las intra-frase se contrastó cada candidata contra el conteo
de caracteres de la frase que le tocaba, a ~1,55 cuadros por carácter. Las que
cuadraban son las fronteras; el resto se descartó.

En el Caso 06 eso se ve limpio: la pregunta 2 trae tres pausas internas —
«constituye, por sí sola, una causal» — y ninguna de las tres cayó cerca de donde
el conteo pedía una frontera.

## Las rejillas nuevas

| | antes | ahora |
|---|---|---|
| Caso 02 | 3 385 cuadros · 2:21 | **3 400 · 2:21** |
| Caso 06 | 3 508 · 2:26 | **3 283 · 2:16** |
| Caso 08 | 2 299 · 1:35 | **2 032 · 1:24** |

El 02 casi no se movió; el 06 y el 08 se apretaron porque la fórmula les había
dado más aire del que la voz necesita.

Estructura, igual en los tres:

```
   0 → 194    intro
 194 → 313    cartón de entrada
 313 → …      narración          (A2)
      + 36    respiro
     … → …    bloque de preguntas (A3)
      + 36    respiro
     … → …    cartón de cierre
     … → …    outro
```

Los 36 cuadros de respiro son un segundo y medio: el último plano del tramo se
extiende sobre ellos, así que en V1 no hay corte.

## Los planos

Los 38 se reajustaron con `herramientas/montaje/ajustar_planos.py`, que tiene
tres modos. El que importa es el nuevo:

- **`loop`** — ventana a velocidad nativa. Es el default.
- **`hold`** — una imagen fija estirada.
- **`loop_congela`** — el loop entero a velocidad nativa y después su último
  cuadro quieto hasta completar la ranura. Para cuando la ranura es más larga que
  el loop **y el gesto ya terminó**: en vez de arrastrar el movimiento al 1,7×,
  se deja reposar. Lo usa el KF02 del Caso 02, donde la entrega de los $120
  millones son 121 cuadros de loop en una ranura de 204.

Las repeticiones de un plano entran siempre por otro punto del loop, o por la
variante B de la imagen, para que no se lean como repetición literal.

## La música

Las tres camas se volvieron a hornear contra los tramos de voz **medidos**, no
los de la rejilla. Verificado por regiones:

| | bajo narración | bajo preguntas |
|---|---|---|
| Caso 02 | −31,6 LUFS | −26,0 |
| Caso 06 | −31,6 | −26,1 |
| Caso 08 | −32,3 | −25,4 |

## Las pistas

`A3` dejó de llamarse FACILITADOR en estas tres líneas: ahí va la voz del bloque
de preguntas. A4 sigue vacía.

Las tres líneas se llaman `TA CASO NN - a la voz`. V1 sin un solo hueco en las
tres. Los huecos que quedan son los que deben estar: en V2 entre los cartones de
narración, y en A1 entre el intro y el outro.
