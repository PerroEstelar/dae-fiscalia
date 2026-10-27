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
| G | 86 | imagen | La vocera | — |
| H | 103 | imagen | Dos mujeres, dos impactos | — |
| I | 70 | imagen | La minuta | — |
| J | 57 | imagen | Las piezas del expediente | — |
| K | 56 | imagen | El informe integral | — |

Entre la E (272) y la H (103) no hay nada: son dos poblaciones. La marca de la
agencia y el largo del texto dicen lo mismo.

## Los cinco videos, medidos

| | ranuras | pieza | duración | voz | cartones | cobertura |
|---|---|---|---|---|---|---|
| A | 13 | 3366 | 2:20,4 | −19,0 LUFS | 7 | 61 % |
| B | 12 | 2880 | 2:00,1 | −19,0 LUFS | 6 | 56 % |
| C | 11 | 3000 | 2:05,1 | −19,1 LUFS | 7 | 63 % |
| D | 12 | 3137 | 2:10,8 | −19,0 LUFS | 8 | 59 % |
| E | 13 | 3151 | 2:11,4 | −19,2 LUFS | 6 | 54 % |

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

## Lo que falta, uno por uno

Placas, grade, horneado, detalles y movimiento de cada video; las dos
angulaciones de cada imagen y su lámina. Se hace situación por situación,
con revisión de Sebastián entre una y otra.
