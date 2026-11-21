# Derecho de petición y acción de tutela · videos de profe (20 nov 2026)

Curso «Derecho de petición y acción de tutela: régimen constitucional, legal y jurisprudencial para servidores
públicos» (Prioridad 3). Profe: **Óscar Jairo Fonseca Fonseca**, autor del curso (lo dice él en el inicio del curso y
es el «1.5 Autor» de los vaciados). **Entrega provisional**: intro, cartón de título, rótulo, cartón de cierre y
outro; el cuerpo va sin gráficos.

## Lo que pide el documento y lo que hay

El formato de diseño pide, por unidad, «video de presentación», «video de retroalimentación de la evaluación» y
«video de cierre, síntesis y conclusiones»; la guía de recursos nombra además «videos de bienvenida». Llegaron siete
grabaciones (`E:\DAE MASTER\CURSO DERECHOS DE PETICION\`), que dan **seis piezas**:

| plan | pieza | fuente | dura | cortes |
|---|---|---|---|---|
| `plan_dpci` | inicio del curso | `VIDEO 1 PRESENTACION GENERAL DEL CURSO - TOMA1` | 7:57 | dos tomas fallidas y la charla del principio |
| `plan_dpu1i` | U1 inicio | `VIDEO2 - PRESENTACION UNIDAD 1 - TOMA 2` (la toma 1 no entra) | 6:32 | tres tramos de la toma 2 |
| `plan_dpu2i` | U2 inicio | `VIDEO2 - PRESENTACION UNIDAD 2- TOMA 1` | 7:30 | una toma fallida |
| `plan_dpu3i` | U3 inicio | `VIDEO4 - PRESENTACION UNIDAD 3- TOMA 1` | 7:34 | — |
| `plan_dpu4i` | U4 inicio | `VIDEO5 - PRESENTACION UNIDAD 4- TOMA 1` | 7:32 | tres tomas fallidas |
| `plan_dpu1c` | U1 cierre | `VIDEO6 - CIERRE UNIDAD 1- TOMA 1` | 27:04 | dos tomas fallidas |

Faltan: los cierres de U2 a U4, las retroalimentaciones y el cierre del curso (no hay grabación).

- **Qué se corta**: lo que el profe le dice al técnico entre tomas («Suspendamos ahí, por favor, Camilo»), la toma
  fallida que viene antes y la conversación del principio y del final. Cada plan dice qué sale y por qué.
- **Qué no se toca**: los tropiezos sueltos de una palabra sin disculpa («se exis— se presentó», «Presentaremo—
  prestaremos», «a una pie— a una persona»), como en Desaparición forzada.
- **Bordes**: a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última,
  comprobados en RMS de 10 ms (`D:\DAE\_tmp\dp_p\rms_bordes.py`). Seis cuadros de mezcla en cada corte (`SUAVE`).

## Cómo se arma

- `base_dp_profe.py` y los seis planes; `lote/cadena_dp.py` (compuesto, cartón de título y rótulo, tres a la vez) y
  `lote/entrega_gpu.py` (línea de Resolve y entrega por la placa NVIDIA, ~5 Mb/s, fuera de receta, como en
  Desaparición forzada), los dos en `D:\DAE\_tmp\dp_p\`.
- Árbol: `D:\DAE MASTER\PRIORIDAD 03\CURSO DERECHO DE PETICION - VIDEOS PROFE\<CURSO|UNIDAD n>\<INICIO|CIERRE>`.
- Rótulo abajo a la **derecha** (x=1330): las manos del profe entran a menudo en la esquina de la izquierda.
