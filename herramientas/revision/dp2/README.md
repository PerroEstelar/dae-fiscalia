# Derecho de petición revisado (24 nov 2026)

Pedido de Sebastián: virtualizar en otro Genially el curso de Derecho de petición **con toda la revisión** del 23 nov,
con la misma línea de recursos y visual, y actualizar el Excel de revisión con miniaturas, como en Terminaciones
anticipadas. Audio de los casos con ElevenLabs (voz de Pilar Durán).

## Qué quedó

- **Sitio:** https://zwaard88-source.github.io/prueba-terminaciones-anticipadas/derecho-peticion/
  (mismo repo de Pages que TA; copia local `D:\DAE\_sitios\terminaciones-anticipadas\derecho-peticion`).
- **16 Genially** («DP · U1 L1 · …», sin el «… Y DAÑO ANTIJURÍDICO»), publicados «Cualquiera con el enlace».
  Los ID están en `out/genially_ids.json` y en el documento «Enlaces a los Genially provisionales · Derecho de
  petición» de la carpeta de Drive «Revisiones Sebastián».
- **23 audios de casos** (MP3 192k, 48 kHz, −16 LUFS, −1,5 dBTP): `voz/lanzar_casos_audio_dp.py` con
  `voz/textos/dp_casos_tts.json`. Archivo en `E:\DAE MASTER\CURSO DERECHOS DE PETICION\Revision\AUDIOS CASOS`.
- **Excel v2** «REVISION DERECHOS DE PETICION NOV 23 v2.xlsx»: cada celda conserva el comentario y el boceto, y suma
  «Propuesta:» (coral), el título de la pantalla corregida y su miniatura real. La v1 pasó a `_anteriores`.

## Cómo se arma

```
python3 revisar.py && python3 pdfs.py && python3 render_dp.py --mapas   # lecciones revisadas, PDF y láminas
python3 genially_dp.py                                                   # buffers del editor (genially/lUL.json)
python3 ../html_leccion/armar.py dp                                      # un HTML autocontenido por lección
python3 capturas_prop.py                                                 # miniaturas reales (desde los HTML)
python3 excel_v2.py mapa.xlsx ../dp/revision_dp.json <bocetos> salida.xlsx
```

- `nucleo.py`: cambios generales de la hoja «Generales» (camino → mapa conceptual con PNG, listas en dos columnas
  con PDF, íconos propios en las rejillas, avisos del juego en la esquina, confeti en el encabezado, texto fijo
  por escena) y publicación.
- `revisar.py`: una función por lección con los cambios de cada celda; textos del DI vigente (`di_parrafos`).
- `genially_dp.py` usa el mismo armado de TA (`ta/genially_ta.py`, ahora con `esc`, `heading`, `base`, `sigla`).
  Índice de hasta 11 filas: de los casos con dos pantallas va la primera; salen antes las de contexto.
- `excel_v2.py`: `MAPA` dice qué escenas revisadas van en cada celda (donde el mapa tiene menos filas que el
  Genially, una celda cubre dos: E04-E05 de la 2.3, el caso 1 y el 4 de la 4.4, la 4.2 C7).

## Para tener en cuenta

- **Genially:** el título se cambia en la ventana del título (`setName` no se guarda) y lo pegado se guarda con
  `rootStore.requestStore.forceSend()`; sin eso, recargar pierde las diapositivas.
- **Un cambio en un Genially ya compartido no se ve hasta «Publish»** (barra de arriba: «Unpublished changes»).
- El chip «Lección 4» de la portada partía en dos renglones a 179 px, también en el DP original: va a 215 px.
- La 3.3 sigue el DI vigente: sin cosa juzgada, temeridad ni implicaciones. El DI escribe «Zalcedo» y «Salcedo».
