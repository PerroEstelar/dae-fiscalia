# Curso - Investigacion Judicial y Forense de la Desaparicion Forzada

Vive en PRIORIDAD 03 y hereda la biblia de puesta en escena P3.

## El arbol, en disco

```
E:/DAE MASTER/PRIORIDAD 03/
  CURSO - INVESTIGACION JUDICIAL Y FORENSE DE LA DESAPARICION FORZADA/
    UNIDAD DESAPARICION FORZADA/
      CASO MIRIAM Y MARIANA/
        00 FUENTE/            los documentos como llegaron del Drive
        _PERSONAJES/          hojas de personaje y referencias de imagen
        CAPITULO 1 - EL ECO EN LA PLAZA Y LA RESPUESTA DE PAPEL/
        CAPITULO 2 - RELOJES EN PAUSA Y EL CLAMOR EN LAS REDES/
        CAPITULO 3 - EL ENGRANAJE ROTO Y EL MAPA DE COMPETENCIAS/
        CAPITULO 4 - LAS VOCES QUE NO SE APAGAN Y EL DOLOR EN LA VENTANILLA/
        CAPITULO 5 - LA TIERRA HABLA Y LA MATRIZ DEL SILENCIO/
           01 PLANOS  02 CARTONES  03 VOCES  04 B-ROLL  05 EXPORTS
           06 GUION Y STORYBOARD  07 MOVIMIENTO  08 MUSICA  09 A LA VOZ
           10 TIMELINE SEBASTIAN
      16 SITUACIONES/
        00 FUENTE/  _PERSONAJES/
        VIDEOS/SITUACION A..E/       las mismas diez carpetas
        IMAGENES/SITUACION F..K/     01 PLANOS 02 LAMINA 05 EXPORTS 06 GUION Y PROMPTS
```

El mismo arbol existe como bins dentro del proyecto `DAE MASTER - CURSOS`.

## Que hay aqui

- `CASO MIRIAM Y MARIANA/CAPn_fuente.md` - el texto de cada capitulo,
  VERBATIM, con el enlace al documento original en la cabecera. Es la fuente
  de la narracion y de los cartones: no se parafrasea, no se reordena, no se
  cambia la sintaxis.
- `herramientas/prompts/base_df_v1.py` - bloque de estilo, reparto y la
  clausula de silueta.

## Las voces

| | voice_id | perfil |
|---|---|---|
| Carlos | Y4HwpMNrBWN5dFKi5Lw8 | colombian male, middle_aged, narrative |
| Pilar  | x6LHvMgpXmty838MUqHh | colombian female, middle_aged, narrative |

Las palabras que el modelo lee mal van en ortografia fonetica SOLO en el
guion de TTS -sicosocial, sicologica- y en el carton van con su ortografia.

## Entregas del caso integrador (Drive: CASO INTEGRADOR > CAPITULO n)

| cap | archivo en Drive | id |
|---|---|---|
| 1 | PRIO 3 - CASO INTEGRADOR - C1 EL ECO EN LA PLAZA.mp4 | 1vqoOQYc-XWMCC5TXbCBoy3-xpBBF90Tv |
| 2 | PRIO 3 - CASO INTEGRADOR - C2 RELOJES EN PAUSA.mp4 | 1-FxKqndSOW8R4uVvVa2Lgs5w5Jl-HtZm |
| 3 | PRIO 3 - CASO INTEGRADOR - C3 EL ENGRANAJE ROTO.mp4 | 1KroP4wBWgKOxh9XElvUWW8iRwYsxdl_v |
| 4 | PRIO 3 - CASO INTEGRADOR - C4 LAS VOCES QUE NO SE APAGAN.mp4 | 1V_8O-F6i1XQq-HO3MQPgeUvR42i31XQ2 |
| 5 | PRIO 3 - CASO INTEGRADOR - C5 LA TIERRA HABLA.mp4 | 1EjKILyuHiynlGtG23d62kWm8nQmYIlbJ |

Carpeta CASO INTEGRADOR: 1fPFqVTw7gqE6uK6LfCkXuSDeox_lMFAU. Sin .srt (ninguno de los cinco).

El C5 se subio el 20 de noviembre de 2026 (2:03, 2965 cuadros, -19,9 LUFS, pico -4,0 dBFS;
36.937.754 bytes, md5 c28a8119679370a94cfb57cd11718bc7). El MP4 que habia en `05 EXPORTS`
con ese nombre era el de la manana, sin dos de los tres planos de detalle (la brocha en la
excavacion y los ojos del analista): esta en `05 EXPORTS/_descartes`. Lo que se subio sale de
rendir otra vez la linea viva `DF C5 LA TIERRA HABLA Y LA MATRIZ DEL SILENCIO`
(`DF_C5_v2.mp4`, receta de `herramientas/montaje/exportar_df.py`); la hoja de comparacion
v1/v2 es `D:/DAE/_tmp/df/render/hoja_c5.jpg`. Antes de subir un capitulo, mirar que el MP4
de disco sea posterior al ultimo cambio de la linea. Verificado byte a byte con
`verificar_drive.py` sobre una copia de servidor.

## Pendiente

- `16 situaciones`: en produccion desde el 27 de octubre de 2026, por
  indicacion de Sebastian. Trae once (A-K): cinco en video, seis en imagen.
  Ver `16 SITUACIONES/README.md`.
- `escenas_df.py` y `armar_df.py` se escriben cuando el desglose este
  aprobado.
