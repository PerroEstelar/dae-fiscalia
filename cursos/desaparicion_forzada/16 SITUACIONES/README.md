# 16 situaciones · curso de Desaparición Forzada

Documento del Drive: «16 situaciones» (carpeta *PRIORIDAD 3 - Investigación
Judicial y Forense de la Desaparición Forzada*). Fuera del caso integrador,
dentro del mismo curso.

## Lo que trae el documento

Se llama «16 situaciones» pero trae **once**, de la A a la K. Cada una es un
**contexto** (el caso) y una **consigna para el participante** (preguntas,
opciones, retroalimentación, plantillas). La consigna **no va en ninguna
pieza**: la agencia la marcó en el propio documento, comentario por
comentario, con «No incluir esto en el video» (A–E) y «No incluir esto en la
IMAGEN» (F–K). Va a Moodle.

## Video o imagen

| | palabras | va en | título de trabajo | voz |
|---|---|---|---|---|
| A | 268 | video | La última llamada | Carlos |
| B | 243 | video | La nota sobre la cama | Pilar |
| C | 233 | video | El plazo de 24 horas | Carlos |
| D | 255 | video | La creciente de La Miel | Pilar |
| E | 272 | video | El camión hacia El Vergel | Carlos |
| F | 77 | imagen | El primer contacto | — |
| G | 86 | video (y su imagen) | La vocera | Pilar |
| H | 103 | imagen | Dos mujeres, dos impactos | — |
| I | 70 | imagen | La minuta | — |
| J | 57 | imagen | Las piezas del expediente | — |
| K | 56 | imagen | El informe integral | — |

Entre la E (272) y la H (103) no hay nada: son dos poblaciones. La marca de la
agencia y el largo del texto dicen lo mismo.

La **G** la marcó la agencia como imagen y pasó a video el 27 de octubre por
pedido de Sebastián: es la única de las imágenes con secuencia (la vocera, las
18:00, el teléfono, la Fiscalía). La forma de imagen se conserva en
`IMAGENES/SITUACION G`.

## Los seis videos, medidos

| | ranuras | pieza | duración | voz | cartones | cobertura | estado |
|---|---|---|---|---|---|---|---|
| A | 13 | 3366 | 2:20,4 | −19,0 LUFS | 7 | 61 % | **v1 montada** |
| B | 12 | 2880 | 2:00,1 | −19,0 LUFS | 6 | 56 % | **v1 montada** |
| C | 11 | 3000 | 2:05,1 | −19,1 LUFS | 7 | 63 % | **v1 montada** |
| D | 12 | 3137 | 2:10,8 | −19,0 LUFS | 8 | 59 % | bases |
| E | 13 | 3151 | 2:11,4 | −19,2 LUFS | 6 | 54 % | bases |
| G | 5 | 1565 | 1:05,3 | — | 3 | 52 % | bases |

### La v1 de A, B y C (27 de octubre)

Entregadas en el `05 EXPORTS` de cada una: `SIT_<X>_v1.mp4` (receta Fiscalía)
y `SIT_<X>_v1_revision_720p.mp4`. Medido sobre el archivo entregado: los
cuadros son exactamente la `pieza`, ningún negro, integrado −19,6 a −19,8 LUFS,
pico −4,1 a −4,4 dBFS. La línea de cada una está en Resolve (`SIT A …`, `SIT B
…`, `SIT C …`) dentro de su bin, y el `.drt` en `10 TIMELINE SEBASTIAN`.

- **Placas**: Seedream 5 Pro, 2k, 16:9, dos candidatas por ranura, con la hoja
  de personaje corregida como referencia. 72 candidatas, 7.200 créditos. Las
  dos quedan en `01 PLANOS/_candidatas`; la elegida está en
  `herramientas/prompts/elegidas_sit.json`.
- **Limpieza de color por bandas** antes del grade (`sit_pieza.limpia`): las
  placas de noche salieron azules (r08 de la A: 17 % del cuadro sobre
  saturación 0,25, todo en la franja fría). Verde/frío/magenta ×0,08 siempre;
  amarillo ×0,15 si el plano no lleva acento; plano sin gente y sin acento,
  todo ×0,15. Peso difuminado, rampa de 8 de tono, la piel no se toca.
- **Grade** por registro con techo y **horneado** sin empuje (encuadre 0,88,
  pulso 5), respiro = r01 quieta 48 cuadros: lo mismo del caso integrador.
- **Entrada y cierre**: antetítulo el curso, título «Situación X». Los nombres
  de carpeta («La última llamada»…) son de trabajo y no salen en pantalla.
- **Música**: la TA03 del caso integrador, ducking horneado contra los tramos
  reales de la voz.

Geometría de la serie: intro 182 · entrada 119 · ranuras · respiro 48 ·
cierre 119 · outro 182.

## Dónde está cada cosa

```
UNIDAD DESAPARICION FORZADA/16 SITUACIONES/
  00 FUENTE/        el documento exportado del Drive
  _PERSONAJES/      15 hojas de personaje (corregidas) + _crudos + ids
  VIDEOS/SITUACION A..E/   las diez carpetas del caso integrador
  IMAGENES/SITUACION F..K/ 01 PLANOS · 02 LAMINA · 05 EXPORTS · 06 GUION Y PROMPTS
```

El mismo árbol existe como bins en `DAE MASTER - CURSOS`, bajo
PRIORIDAD 03 › CURSO … › UNIDAD DESAPARICION FORZADA › 16 SITUACIONES.

## Herramientas

| | |
|---|---|
| `herramientas/voz/textos/guion_sit.py` | guion verbatim + tts, por bloque; textos de las láminas |
| `herramientas/voz/textos/rutas_sit.py` | el árbol |
| `herramientas/voz/lanzar_voz_sit.py` | pide las voces (Carlos / Pilar) |
| `herramientas/voz/armar_sit.py` | máster −19 LUFS, rejilla y ranuras |
| `herramientas/prompts/base_sit.py` | reparto nuevo sobre `base_df_v1` |
| `herramientas/prompts/escenas_sit_[a-e].py` | una placa por ranura + DET + BROLL + MOV |
| `herramientas/prompts/imagenes_sit.py` | dos angulaciones por imagen |
| `herramientas/prompts/personajes_sit.py` | hojas de personaje |
| `herramientas/prompts/prompts_sit.py` | arma todo y escribe el storyboard .md de cada situación |
| `herramientas/cartones/cartones_sit.py` | cartones escogidos a mano, tiempos y verbatim por máquina |
| `herramientas/cartones/lamina_sit.py` | la lámina de las imágenes |
| `herramientas/prompts/bajar_placas_sit.py` | baja las candidatas y arma la hoja de contacto |
| `herramientas/prompts/elegidas_sit.json` | qué candidata va en cada ranura |
| `herramientas/montaje/sit_pieza.py` | elegir · construir · blancos · musica · montar · exportar · entregas · verificar |

## Lo que falta, uno por uno

- A, B y C: la revisión de Sebastián; después, segundo pase de planos de
  detalle (V3, los `DET` de cada escena) y movimiento (V2).
- D, E y G: placas, y el mismo `sit_pieza.py`.
- F, H, I, J, K (y la G en imagen): las dos angulaciones y su lámina.
