# Caso Nico — «Importancia del principio de culpabilidad en la justicia penal para adolescentes»

Prioridad 1 · Sistema de responsabilidad penal para adolescentes y justicia
restaurativa · Unidad 1. Pedido de Sebastián del 12 nov 2026: el caso «de pe a
pa», con la receta de los cursos de casos (no es un profe a cámara).

- **Fuente:** Google Doc «Caso Nico» (`1TWtuxipDr0u5irRp8Dz_FfOaAV6tTkj_08bR1p-4bFg`).
  La copia de trabajo está en `00_fuente.md` y en
  `00 DOCUMENTOS FUENTE\Caso Nico.md`. El documento no trae preguntas ni
  consigna: es solo el caso.
- **En disco:** `E:\DAE MASTER\PRIORIDAD 1\CURSO - SRPA Y JUSTICIA RESTAURATIVA\UNIDAD 1\CASO NICO - Principio de culpabilidad\`,
  con las diez carpetas de la serie (01 PLANOS … 10 TIMELINE SEBASTIAN).
- **En Resolve:** `DAE MASTER - CURSOS` › `CURSO - SRPA Y JUSTICIA RESTAURATIVA` ›
  `UNIDAD 1` › `CASO NICO - Principio de culpabilidad`. La línea se llama
  `SRPA - U1 - CASO NICO` y su `.drt` está en `10 TIMELINE SEBASTIAN`.
- **Receta:** `herramientas/montaje/sr_pieza.py` (es `ei_pieza`). Las
  diferencias están en su encabezado.

## Voz

`herramientas/voz/textos/guion_sr.py`, 43 bloques. Es el documento entero y en
su orden, comprobado palabra por palabra (1.127 de 1.127).

- **Narra Pilar.** La cita del defensor (n28, n29) la dice Julián, con el paso
  alto contra los golpes de aire. La frase del comerciante («esperarlo entre
  todos…») la dice la narradora, citada.
- **Números:** en la voz van en letras; en los cartones, en dígitos (15 años,
  9:15 a. m., $18.000, 30 metros, 10 minutos).
- **Máster:** 8:17,8 a −19,0 LUFS, pico −4,9 dBTP. El peor salto entre bloques
  es de 0,30 LU.
- **Errata que no se toca:** el documento dice «el domingo 12 de abril de
  2022», pero ese día fue martes. Va verbatim; se le avisó a Sebastián.

## Personajes (00 PERSONAJES)

Cinco hojas (Seedream 5 flash, sobre las hojas de estilo de EI):

- Nico, con el buzo mostaza: el único acento de la pieza.
- Nico rapado, para el corte y el aislamiento.
- El defensor público.
- La cocinera de la plaza.
- La enfermera del CAE.

Los comerciantes van siempre de espaldas o en silueta. Los patrulleros llevan
el uniforme de la Policía Nacional, sin letras ni insignias.

## Placas

Son 74 ranuras cortadas sobre las palabras de Scribe
(`escenas_sr_nico.CUADROS`, 11.934 cuadros).

- **Madres:** se hicieron 18 sobre las anclas de estilo, una por lugar: el
  pueblo, la plaza de noche, el puente, el comedor, la patrulla, el CIP, la
  sala del defensor, la oficina, el pasillo del juzgado, el CAE, la recepción
  y la enfermería.
- **Hijas:** se pidieron con la hoja del personaje primero y la madre al
  final.
- **Elegidas:** están en `prompts/elegidas_sr.json`.
- **Rehechas:**
  - r16, los comerciantes discutiendo: salieron con la cara a la vista y se
    rehicieron en silueta.
  - r57 y r59, la oficina del defensor: salieron llenas de gente. El defensor
    tiene que estar solo.
- **La agresión no se dibuja en acto** (r29-r33). Se ve así:
  - r29: el caldo en el suelo;
  - r30: el corro de espaldas;
  - r31: los gritos en contraluz;
  - r32: el celular;
  - r33: Nico encogido entre botas.

  Ninguna mano levantada.
- **Grade:** limpieza por bandas de EI, `graduar_registro` y la curva GRIS
  (30, 130). Los patrulleros (r34-r40) tienen el verde y el chaleco acotados,
  no apagados (`escenas.CHALECO`).
- **Color:** todo va en Rec.709 etiquetado (ranuras, respiro, clips,
  entregas).
- **El buzo después de la curva GRIS:** la curva va después de nivelar el
  acento y le corre el tono. La r45 quedó a 29,6° (naranja), la r49 a 31,1° y
  la r07 y la r42 a 33,9°, contra 35-42° en el resto. Ahora `construir` vuelve
  a nivelar al final, y esas cuatro se rehornearon (quedaron a 39,5-40,9°).

## Movimiento (V2, Kling 2.5, 720p)

Se pidieron 50 clips (`prompts/kling_sr.json`). Todos son de 5 s salvo r42 y
r43, de 10 s. Usan como cuadro inicial la placa graduada, en JPEG de 2048,
subida desde la nube.

**Sin clip a propósito** (llevan la cámara de la casa):

- las ranuras bajo las listas de After Effects;
- las de solo manos;
- las que valen por quietas;
- la agresión.

**Descartados después de mirarlos:**

| ranura | motivo |
|---|---|
| r12 | Nico sale de cuadro a los 2 s |
| r27 | aparece un objeto y los comerciantes desaparecen |
| r42 | pasan la cámara y el pasillo queda vacío |
| r43 | el defensor da media vuelta |
| r52 | vaho y un rayo de luz |

**Recortados:**

- r28 a 3,6 s: después, la cámara se mete en la plaza.
- r72 a 3,0 s: después, el pelo vuelve a aparecer. Esos 72 cuadros llenan
  una ranura de 134, así que `mov_sr` interpola los intermedios (minterpolate)
  en vez de repetir cuadros. Pasa con cualquier estiramiento de más de 1,4x.

**Conformado** (`montaje/mov_sr.py`): el corte al 88 %, la limpieza de la
placa, la saturación igualada a la placa y el acento llevado al tono de la
placa. En r45 Kling había corrido la mostaza al naranja.

## Gráficos

- **Cartones:** 35, verbatim (`cartones/cartones_sr.py`), con el tinte #004890
  al 46 %.
  - Sin cartón: la agresión (n14, n15), como en ED y EI.
  - La cita del defensor va reducida a la condición («Si acepta…») y al remate
    («Piénselo bien…»). Entera quedaba a 21-24 car/s.
- **Rótulo:** Nico, «Un adolescente de aproximadamente 15 años», en la r02
  (`cartones/lowerthirds_sr.py`). El defensor, los patrulleros y la enfermera
  no tienen nombre, así que van sin rótulo.
- **Listas de After Effects** (`motion/mg_sr.py`, en `00 MOTION GRAPHICS/SRPA_mg.aep`):
  - **el desayuno:** el tamal, el caldo, la bebida y los $18.000;
  - **lo que la policía no hizo;**
  - **lo que el CAE le daría;**
  - **lo que el defensor no hizo;**
  - **la valoración inicial.**

  Usan la retícula A de los cartones y el mismo tinte a cuadro completo.
  Salen en ProRes 4444 con alfa premultiplicado: en Resolve van con *Alpha
  mode: Premultiplied* (`sr_pieza.construye` lo fija).
- **Íconos:** 18 nuevos, en dos hojas de Magnific (`motion/iconos_sr.py`).

## Música y línea

- **Música:** TA05, la cama quieta de los casos que no se resuelven en
  pantalla. Va con el ducking horneado (−32 LUFS bajo la voz, −26 en los
  huecos) y calla durante el sonido del intro y del cierre.
- **Geometría:** intro 182 · entrada 119 · 74 ranuras · respiro 48 (la placa
  del aislamiento, con fundido a negro) · cierre 119 · outro 182. Son 12.584
  cuadros.
- **Pistas:**

  | pista | qué va |
  |---|---|
  | V1 | la pieza entera |
  | V2 | movimiento |
  | V4 | cartones |
  | V5 | motion graphics |
  | V6 | marca de agua, al principio y al final del cuerpo |
  | V8 | lower third |
  | A1 | narrador |
  | A4 | sonido del intro y del outro |
  | A5 | música |

## Montaje y entrega (12 nov)

- **Línea:** `SRPA - U1 - CASO NICO` mide 12.584 cuadros (8:44,9) y no tiene
  huecos.

  | pista | clips |
  |---|---|
  | V1 | 79 |
  | V2 | 45 |
  | V4 | 35 |
  | V5 | 5 (premultiplicadas) |
  | V6 | 2 |
  | V8 | 1 |

  El `.drt` está en `10 TIMELINE SEBASTIAN`.
- **Revisión interna** (`revisar`, en `D:\DAE\_tmp\sr\revision`): se hizo
  antes de exportar y la hoja ya muestra las listas de AE (V5).
- **Entrega:** `05 EXPORTS\SR_NICO_v1.mp4`, de 170 MB, y la de revisión en
  720p, de 34 MB. Los dos miden 12.584 cuadros, igual que la pieza, y llevan
  audio.
  - Sonoridad: −19,0 LUFS, LRA 3,7 LU, pico −4,1 dBFS.
  - El único negro es el último cuadro del respiro (512,26 s), y es a
    propósito.
- **Drive:** VIDEOS FINALIZADOS › unidad 1 ›
  [PRIO 1 - SRPA - U1 - CASO NICO PRINCIPIO DE CULPABILIDAD.mp4](https://drive.google.com/file/d/1d_VRGsS3M5PQY2kCO-6IhPXMMsyxK3U4/view).
- **Magnific:** unos 13.000 créditos.
  - 164 imágenes (hojas, madres, hijas y rehechas) en Seedream 5 flash.
  - Dos hojas de íconos.
  - 48 clips de Kling de 5 s y 2 de 10 s.

### v2 (12 nov, con los ajustes de Sebastián)

Sebastián hizo tres cambios a mano en la línea:
- quitó el clip de movimiento de r05, r28 y r35;
- sacó de V1 la placa del respiro;
- estiró el clip de r74 en V2 (151 cuadros) para que cubra el respiro.

Se re-exportó sin tocar su línea. Las medidas son las mismas que en v1:
12.584 cuadros, −19,0 LUFS, pico −4,1 dBFS y audio OK.
- **Archivos:** `05 EXPORTS\SR_NICO_v2.mp4`, de 167 MB, y la de 720p, de
  33 MB. Los de v1 se pasaron a `_descartes`.
- **Drive:** la v1 se mandó a la papelera y la v2 ocupa su lugar, con el mismo
  nombre.
