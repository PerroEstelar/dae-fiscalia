# DAE · Fiscalía — guiones, método y herramientas

Repositorio de **texto** de la serie audiovisual de la Dirección de Altos Estudios
(Fiscalía General de la Nación, Colombia).

Acá no vive media. La media está en `E:\DAE MASTER` y en `D:\DAE`, y el `.gitignore`
está puesto para que no se suba un solo fotograma por accidente. Lo que sí vive acá es
todo lo que se puede escribir desde cualquier parte: guiones, planes de montaje,
los scripts que generan los cartones y el proyecto de Resolve exportado.

El punto de esto es poder trabajar desde una **cloud session** de Claude Code —desde el
navegador o el celular— sin tener el computador encendido: escribir el guion del próximo
caso, ajustar la retícula de un cartón, preparar los prompts. Después, en la máquina,
`git pull` y se corre contra la media.

## Estructura

```
cursos/
  terminaciones-anticipadas/
    guiones/      los casos del guion FGN-UNAL, indexados y verbatim
  medio-ambiente/
    unidad-1/     el plan de cartones de la introducción
herramientas/
  cartones/       los generadores de cartones alfa
proyecto-resolve/ el .drp exportado (150 KB, el proyecto entero sin media)
```

## Los cursos

| curso | estado |
|---|---|
| **1 · SRPA** (profes Edwin, Carlos Humberto, Hugo Ascencio) | terminado |
| **2 · Delitos contra el medio ambiente** (5 unidades) | introducciones en montaje |
| **3 · Bernardo JEP** (5 videos) | videos 2, 3 y 4 terminados |
| **4 · Terminaciones Anticipadas** (8 casos elegidos) | en guion |

## El formato

Cada pieza lleva, en este orden: intro institucional de 194 frames, cartón de entrada de
119, el cuerpo, y cartón de cierre. Marca de agua y cama de música cubren el cuerpo.
Todo a **23.976 fps, 1920×1080**, DaVinci YRGB, Rec.709 (Scene).

La locución se calcula a **155 palabras por minuto**, que es el ritmo medido de la serie.
La duración de la pieza sale de: locución × 1,10 (pausas internas) + 30 s de intro,
cartón de entrada y cierre.

## Los cartones

`herramientas/cartones/cartones_v3.py` genera los cartones alfa con la retícula medida de
la serie. Produce QuickTime Animation (qtrle, ARGB) cuadro a cuadro, con la barra amarilla
animada y el texto escalonado línea por línea.

Necesita Python 3 con Pillow, ffmpeg en el PATH, y la familia Montserrat instalada.

```bash
python cartones_v3.py              # los rinde todos
python cartones_v3.py c05_leccion1 # sólo uno
```
