# Caso 02 · Voces generadas y rejilla medida

Las voces ya no son estimación: están generadas y medidas. Esta rejilla reemplaza la de
`01_guion_y_prompts.md`, que estaba calculada a 150 palabras por minuto.

## Las tres voces

Generadas con **ElevenLabs `eleven_v3`** a través de Magnific.

| Papel | Voz | Por qué |
|---|---|---|
| **Narradora** | Valentina Santos · colombiana, media edad | Es la única voz colombiana del catálogo que sirve para narración; nunca se ve en cuadro, así que el género no choca con ningún plano. |
| **Abogado defensor** | Joaquín Quintana · neutro latino, media edad | Firme y creíble «sin sonar rígido ni teatral». Hombre, porque está en cuadro en el KF 04. |
| **Facilitador** | Andrés Quintana · neutro latino, media edad | Registro de mentor de academia: el de alguien que hace una pregunta y espera respuesta. Hombre, porque está en cuadro en el KF 10. |

En el catálogo de Magnific hay **89 voces en español** y solo **dos colombianas**, las dos
femeninas (Valentina Santos y Sofía Ramírez). No hay masculina colombiana. Si la DAE pide
que todas sean colombianas, la salida es volver femenino al facilitador —Sofía Ramírez— y
regenerar el KF 10 con una mujer. El abogado no, porque el KF 04 ya quedó.

Parámetros: `stability` 0,65 para la narradora (plana y firme) y 0,55 para los dos personajes;
`similarityBoost` 0,80; velocidad 0,95 en narración y defensa, 0,90 en el facilitador.
Cifras escritas en letras, incluido «artículo trescientos cuarenta y nueve».

**Masterizado**: −19 LUFS, −1,0 dBTP, dual-mono estéreo, 48 kHz, WAV 24 bits.
Los MP3 crudos de ElevenLabs quedan en `03 VOCES\_crudos elevenlabs\` por si hay que
remasterizar sin volver a gastar créditos.

## Lo que midió cada bloque

| Archivo | Estimado | Medido | Diferencia |
|---|---|---|---|
| `TA02_NARRADOR_B1` | 38,4 s | **36,32 s** · 871 f | −49 f |
| `TA02_DEFENSA` | 16,0 s | **13,60 s** · 326 f | −59 f |
| `TA02_NARRADOR_B2` | 44,0 s | **42,32 s** · 1015 f | −40 f |
| `TA02_NARRADOR_B3` | 34,0 s | **26,32 s** · 631 f | −184 f |
| `TA02_FACILITADOR` | 38,0 s | **47,60 s** · 1141 f | **+231 f** |
| **Total locución** | 2:50 | **2:46** · 3984 f | −4 s |

El total da casi exacto —la fórmula de 150 palabras por minuto sigue sirviendo— pero el
reparto interno no. El bloque 3 corre más rápido de lo calculado porque son frases cortas y
declarativas, y el facilitador corre más lento porque son preguntas, que el sintetizador
alarga. **La fórmula estima bien la pieza y mal el bloque**: sirve para presupuestar, no para
cortar.

## La rejilla medida

Cada bloque lleva 36 f de aire (18 adelante y 18 atrás); el diálogo de la defensa lleva 48,
porque necesita un respiro antes y después para leerse como escena y no como narración.

| Rel | Qué | Duración |
|---|---|---|
| 0 | Intro institucional | 194 f |
| 194 | Cartón de caso | 119 f |
| **313** | **BLOQUE 1** · los hechos | 907 f |
| **1220** | **DIÁLOGO** · la defensa | 374 f |
| **1594** | **BLOQUE 2** · el artículo 349 | 1051 f |
| **2645** | **BLOQUE 3** · no es moneda de cambio | 667 f |
| 3312 | Cartón de pausa | 144 f |
| **3456** | **BLOQUE 4** · el facilitador | 1177 f |
| 4633 | Cartón de cierre | 119 f |
| 4752 | Outro | 194 f |
| **4946** | **FIN — 3:26** | |

## Reparto de planos

| Plano | Entra | Sale | Frames |
|---|---|---|---|
| KF 01 · La oficina de contratación | 313 | 640 | 327 |
| KF 02 · La entrega | 640 | 940 | 300 |
| KF 03 · La bodega | 940 | 1220 | 280 |
| KF 04 · El abogado propone | 1220 | 1410 | 190 |
| KF 05 · Andrés escucha | 1410 | 1594 | 184 |
| **KF 06 · Gráfico AE** | 1594 | 2150 | 556 |
| KF 07 · El código abierto | 2150 | 2645 | 495 |
| KF 08 · Antes de sentarse | 2645 | 3000 | 355 |
| KF 09 · La carpeta cerrada | 3000 | 3312 | 312 |
| KF 10 · El facilitador | 3456 | 4150 | 694 |
| KF 11 · El acta sin firmar | 4150 | 4633 | 483 |

El KF 10 se queda con la mayor parte del bloque 4 porque es el único plano de la pieza en
que alguien mira al lente, y las tres preguntas se sostienen en esa mirada. El KF 11 entra
con la cuarta pregunta —la que de verdad pone a prueba el criterio— y aguanta hasta
«piénselo antes de continuar». La ausencia de gente en ese plano es la pregunta.

## Pendiente

- Montar el gráfico del **KF 06** en After Effects, 556 f: la marca del 50 % entra medio
  segundo después de que la voz dice la cifra, no mientras la dice.
- Los **prompts de movimiento**, ahora contra la imagen real.
- Confirmar con la DAE si los cartones de esta serie llevan tinte azul (rejilla A) o van en
  caja sin tinte (rejilla B).
