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

## Pendiente

- `16 situaciones`: en produccion desde el 27 de octubre de 2026, por
  indicacion de Sebastian. Trae once (A-K): cinco en video, seis en imagen.
  Ver `16 SITUACIONES/README.md`.
- `escenas_df.py` y `armar_df.py` se escriben cuando el desglose este
  aprobado.
