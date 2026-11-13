# Cierres de unidad (Delitos ambientales)

## El pedido

Sebastián lo pidió el 13 nov 2026. Cada unidad tiene un video de **cierre**, y
lleva nuestra intro y nuestro outro, «solo eso». Se entrega en nuestro MP4 sin
pérdida visible.

En Drive van a la carpeta de los cierres, dentro de una carpeta nueva
`VIDEOS EXPORTADOS`. Los nombres son «unidad n cierre intro/outro».

## El material

- **Drive:** carpeta `1YeYJfdz6Kdg80Mo5TOnenBklzROuezBB`, con las subcarpetas
  `UNIDAD 1` a `UNIDAD 5`. Cada una tiene su cierre.
  - Se bajaron por `_MA subidas`, una copia en Mi unidad que Drive sincroniza.
  - Después esas copias se mandaron a la papelera.
- **Qué son:** videos de diapositivas animadas con voz en off.
  - Formato: 1280×720 a 24 fps, Rec.709, AAC 44,1 kHz mono.
  - Empiezan en el título de la unidad («Unidad 3: Investigación»).
  - Terminan en una pregunta. Después, en silencio, viene una tarjeta de
    **«Gemini Notebook»** de 3 s. La diapositiva entra con un corte seco y
    queda quieta hasta el final.
  - Todas las diapositivas llevan esa marca, chiquita, abajo a la derecha. Está
    quemada en la imagen y no se toca.
  - No traen intro ni outro propios.

| Unidad | Largo | Sonoridad | Pico |
|---|---|---|---|
| 1 | 7:20,1 | −16,4 LUFS | +0,2 dBTP |
| 2 | 9:03,5 | −16,2 LUFS | +0,1 dBTP |
| 3 | 6:30,5 | −18,9 LUFS | 0,0 dBTP |
| 4 | 7:59,3 | −16,3 LUFS | +0,1 dBTP |
| 5 | 7:12,9 | −18,3 LUFS | −0,1 dBTP |

- **Disco:** `E:\DAE MASTER\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\UNIDAD n\CIERRE DE UNIDAD\`
  - La fuente va en `01 VIDEO\UNIDAD n - CIERRE.mp4`.
  - La entrega va en `05 EXPORTS\`.

## Cómo se hizo (`herramientas/montaje/cierres_unidad.py`)

No pasa por Resolve: es ffmpeg con una sola codificación. Así hay una generación
menos que con el máster de 32 Mb/s, y no hace falta armar cinco líneas para
pegar tres clips.

- **Intro y outro:** son los primeros 194 cuadros (8,09 s) de
  `00 COMUNES\INTRO\FGN_intro_version7.mp4`. Van al principio y al final, igual
  que en las líneas de las introducciones.
- **La tarjeta de Gemini Notebook se quita.**
  - La primera tanda la dejaba, por el «solo eso». Al verla, Sebastián pidió
    «sí, quítala de las 5».
  - `inicio_tarjeta` busca el último corte de escena de los 12 s finales y
    comprueba que lo que sigue sea la tarjeta quieta, con luma media de ~227.
  - El score del corte va de 0,15 a 0,38. La U3 es la más baja porque su última
    diapositiva es casi blanca. Por eso el umbral es 0,08.
  - El cierre termina un cuadro antes de la tarjeta, para que el `fps` no la
    alcance al redondear.
  - Se quitan 3,04–3,08 s por unidad. La voz termina unos 0,9 s antes, así que
    la última diapositiva respira un poco antes del outro.
  - La primera tanda quedó en `05 EXPORTS\_descartes` como
    «… con tarjeta Gemini.mp4». Las copias de Drive se mandaron a la papelera.
- **Imagen del cierre:**
  - Se escala a 1920×1080 con lanczos, en Rec.709 de entrada y de salida.
  - Pasa de 24 a 23,976 con `fps`: se descarta un cuadro cada ~42 s. En
    diapositivas no se nota, y el sonido no se corre.
- **Sonido del cierre:**
  - Pasa a 48 kHz estéreo, con el mismo canal a los dos lados.
  - No se le toca el nivel, porque el pedido era «solo eso».
  - Video y audio se cortan al mismo largo exacto. Un cuadro a 23,976 son 2002
    muestras a 48 kHz.
- **Codificación:** la receta de `Entrega_MP4_Fiscalia_Receta.md`.
  - x264 CRF 18, `preset slow`, `tune animation`, High L4.0, keyint 48,
    `+faststart`, Rec.709 etiquetado.
  - El audio va en AAC 256k. Hay que recodificarlo porque se empalma.

## Entrega

**Archivos:** `05 EXPORTS\unidad n cierre intro-outro.mp4`.

- Windows no acepta la «/» del nombre que pidió Sebastián, así que se usó un
  guion.
- Formato: H.264 High L4.0, 1920×1080, 23,976, Rec.709, AAC 48 kHz estéreo.

| Unidad | Cuadros | Largo | Peso | Sonoridad | Pico | PSNR medio / mínimo |
|---|---|---|---|---|---|---|
| 1 | 10.855 | 7:32,7 | 127 MB | −16,5 LUFS | −0,2 dBTP | 53,4 / 42,4 dB |
| 2 | 13.336 | 9:16,2 | 100 MB | −16,2 LUFS | +0,1 dBTP | 54,8 / 47,8 dB |
| 3 | 9.666 | 6:43,2 | 66 MB | −18,9 LUFS | −0,1 dBTP | 55,4 / 49,2 dB |
| 4 | 11.795 | 8:12,0 | 99 MB | −16,3 LUFS | 0,0 dBTP | 54,3 / 45,5 dB |
| 5 | 10.682 | 7:25,5 | 85 MB | −18,4 LUFS | −0,4 dBTP | 54,7 / 42,2 dB |

- **Cuadros:** son 194 de intro, más los del cierre, más 194 de outro. Coinciden
  en las cinco.
- **Audio:** dura lo mismo que el video, al milisegundo.
- **PSNR:** se midió el tramo del cierre contra la fuente escalada con la misma
  cadena. Por encima de 40 dB ya no se distingue.
- **Sonido:** el nivel es el de la fuente.
  - La U3 y la U5 quedan unos 2 LU por debajo de las otras.
  - Los picos rondan los 0 dBTP, como en los originales.
  - No se niveló porque no se pidió. Si se pide, es un paso de loudnorm.
- **Hoja de empalmes** (`D:\DAE\_tmp\ma\cu\rev2_un.png`): cada una tiene diez
  cuadros.
  - La intro arranca y termina en blanco.
  - Después va el título de la unidad.
  - La última diapositiva pasa directo al outro, sin la tarjeta de Gemini.
- **Drive:** los cierres están en `1YeYJfdz6Kdg80Mo5TOnenBklzROuezBB`, en la
  carpeta `VIDEOS EXPORTADOS` (`1NTcuKQJmFcqMQXLT-f8n99muflcJx7_L`).
  - La subida pasó por `G:\My Drive\_MA subidas`, y de ahí se movieron con
    `update_file`.
  - Las copias de las fuentes que habían quedado en `_MA subidas` se mandaron a
    la papelera.

**Una trampa de la subida.** Un proceso de revisión de la primera tanda quedó
colgado y no se mató a tiempo. Cuando Drive borró la copia local de la U2, ya
movida, ese proceso la volvió a copiar a `_MA subidas`, y Drive la subió como un
archivo nuevo.

- Antes de copiar con el mismo nombre, hay que matar con `taskkill /T` todo lo
  que quede de la tanda anterior.
- Después hay que buscar duplicados en `_MA subidas`.
- `rehacer.py` espera a que el nombre desaparezca de la carpeta local antes de
  copiar.
