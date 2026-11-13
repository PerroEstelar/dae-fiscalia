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
  - Terminan en una pregunta, con unos 3,9 s de silencio.
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

Pendiente: se completa con la verificación de cada unidad (cuadros, sonido, PSNR
contra la fuente escalada y hoja de empalmes).
