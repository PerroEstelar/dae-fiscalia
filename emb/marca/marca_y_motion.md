# Marca EMB y línea de motion graphics

Investigado el 14 nov 2026 sobre `metrodebogota.gov.co` (home, SVG de los logos, estilos
computados del sitio) y documentos públicos de la EMB.

## 1. ¿Hay manual de marca público?

**No encontrado.** La caracterización del proceso de Comunicación Corporativa de la EMB
(CC-CP-001 v.05, feb 2026) nombra dos manuales como salida de «Gestionar la imagen corporativa
y marca de la EMB», a cargo de la Gerencia de Comunicaciones, Ciudadanía y Cultura:

- «Manual institucional de imagen para Metro de Bogotá S.A.»
- «Manual de obra Metro de Bogotá S.A.»

Ninguno está publicado en «Políticas, lineamientos y manuales» de transparencia. Hay que
**pedirlos a la EMB por medio de JP/UECP**, junto con los logos en vector. Mientras tanto,
lo de abajo sale de medir el sitio oficial.

Sí son públicos y aplican:
- Manual de uso de marca ciudad «Bogotá» (Alcaldía, versión sep 2026):
  `bogota.gov.co/sites/default/files/2026-09/manual-de-uso-de-marca-ciudad-bogota.pdf`
- Manual de contenidos accesibles para las comunicaciones digitales de la EMB, CC-MN-004 v02.

## 2. Logos que usa el sitio oficial

| logo | archivo en el sitio | colores medidos en el SVG |
|---|---|---|
| Metro de Bogotá, horizontal color | `/sites/default/files/2023-08/logo-metrobogota-horizontal.color_.svg` | rojo `#DF1F15`, amarillo `#FFC400` |
| Alcaldía Mayor de Bogotá (escudo) + marca ciudad «Bogotá» | `/sites/default/files/2023-08/logo-alcaldiabog-color.svg` | rojo `#E61C29`, amarillo `#FBBC1E`, negro `#060A0D` |
| Gobierno de Colombia («Colombia Potencia de la Vida») | `/sites/default/files/2023-08/logo_potencia_de_la_vida.svg` | multicolor |
| Barra GOV.CO | `/sites/default/files/2023-08/logo-govco.svg` | — |

**Ojo con el del Gobierno:** «Colombia Potencia de la Vida» es la marca del gobierno
2022–2026. El sitio todavía la muestra, pero el gobierno nacional cambió en agosto de 2026.
**Confirmar con la EMB qué logo nacional va**, o si va solo el par Metro + Alcaldía, que es el
que el sitio pone en el encabezado.

El curso además es de la **UECP de la Universidad Nacional** (membrete del documento de
estructura). Confirmar si el logo UNAL va en el outro.

## 3. Lenguaje gráfico del sitio (medido)

- **Tipografías:** `Work Sans` (titulares, bold) y `Montserrat` (cuerpo). Montserrat ya está
  instalada en la máquina por la serie DAE.
- **Paleta en uso:** rojo y amarillo de marca; texto casi negro `#212529`; azul de enlaces y
  encabezado `#1B418B`; blanco; grises claros `#F5F5F5`.
- **Formas:** tarjetas con esquinas muy redondeadas; bloques planos de color (rojo, amarillo,
  azul, verde) con foto en duotono del color del bloque («Línea 1» en rojo, «Línea 2» en
  amarillo); botones en píldora amarilla con texto oscuro; una línea curva amarilla que
  atraviesa fotos de estaciones; tarjetas de redes con fondo rojo y titular blanco.
- **Fotografía:** obra real, viaducto, tren rojo, personas reales en primer plano y sonriendo.
- **Movimiento:** los encabezados del home son GIF animados a 1920×1080.

### Contraste (WCAG, calculado)

| texto / fondo | contraste | uso |
|---|---|---|
| blanco sobre rojo `#DF1F15` | 4,83 | titulares y cuerpo grande, sí |
| `#212529` sobre amarillo `#FFC400` | 9,66 | sí, cualquier tamaño |
| blanco sobre amarillo | 1,60 | **nunca** |
| rojo sobre amarillo | 3,03 | solo elementos gráficos, no texto |
| blanco sobre azul `#1B418B` | 9,65 | sí |

## 4. Propuesta de línea de motion graphics

Una sola familia de piezas para los 4 módulos, armada como plantilla (AE o Magnific Move):

| pieza | uso | forma |
|---|---|---|
| **Título de lección** | arranque de cada video | tarjeta blanca redondeada; antetítulo «Módulo 1 · Lección 1.1.1» en Montserrat SemiBold; título en Work Sans Bold; filete rojo a la izquierda |
| **Tarjeta de concepto** | cada concepto (violencia directa, paz positiva…) | tarjeta de color plano + ícono lineal + nombre + una frase; entran en fila como vagones |
| **Comparador** | lo que en el documento es tabla de 3–4 filas | tarjetas apiladas que se revelan una a una, la activa en rojo o amarillo, las demás en gris claro |
| **Rótulo de cita** | autor y año (Galtung, 1969) | píldora pequeña abajo a la izquierda |
| **Marca de caso** | toda escena dramatizada | etiqueta fija «Situación hipotética con fines pedagógicos», discreta, arriba |
| **Pregunta de actividad** | cierre de cada video | panel amarillo con texto oscuro, la pregunta de la actividad de la lección |
| **Mapa conceptual** | cierre de módulo | el mapa del documento redibujado, que se arma nodo a nodo |

Movimiento: los elementos entran deslizando de izquierda a derecha, en el sentido de un tren
que llega, con desaceleración suave. Nada rebota ni gira. Una línea curva (la del viaducto, como
la amarilla del sitio) puede hilar las transiciones entre bloques.

## 5. Intro y outro (propuesta)

- **Intro (3–4 s):** fondo blanco; una línea roja se curva como un viaducto y deja paso a un
  tren abstracto (bloque rojo redondeado) que cruza; al pasar arma el logo del Metro (la «M» de
  montañas y la palabra); aparece el nombre del curso. Sonido de paso de tren muy suave.
- **Outro (4–5 s):** la línea vuelve, se aquieta y deja la franja de logos institucionales
  (Metro · Alcaldía/Bogotá · Gobierno de Colombia o el que confirme la EMB · UNAL si va), sobre
  blanco y con su área de reserva.
- Cortos a propósito: en piezas de 1–3 min, 16 s de bumper (como el FGN) serían 10–15 % del video.

## 6. Magnific Move (lanzado en octubre de 2026)

Qué es, según la documentación oficial (`magnific.com/ai/docs/move`):
- Convierte una descripción en un motion graphic: texto, formas, imágenes, transiciones y
  audio. Sirve para explicativos, slides animados y **revelado de logos**.
- Se le adjuntan logos, imágenes, video y audio (hasta 100 archivos por motion).
- **Brand Kit:** guarda colores, fuentes y logo para que todas las piezas salgan iguales.
  Encaja con la plantilla de arriba.
- Hasta 180 s por pieza, 16:9 entre otros formatos, con opción de bucle.
- Se edita por instrucciones o comentando un cuadro; cada cambio deja una versión nueva.
- Exporta **solo MP4**, a 24, 30 o 60 fps.

Lo que eso implica para nosotros:
- **No exporta alfa.** Una tarjeta de Move no se puede poner encima de una placa en Resolve.
  O la pieza va a cuadro completo (título, comparador, mapa conceptual, intro y outro), o se le
  adjunta la placa/el clip para que lo componga adentro.
- **No hay 23,976.** Rendir a 24 y conformar en la línea (0,1 % de diferencia de velocidad).
  Revisar el audio si trae.
- La documentación no menciona API ni MCP: por ahora se opera desde la web, a mano.
- El costo por versión se ve en cada versión; editar es barato, generar medios es caro
  (activar «Ask first»).

**Propuesta:** probar Move con dos piezas antes del lunes: el intro con el logo del Metro y el
comparador de las tres violencias (lección 1.1.1). Si sostiene la marca, la línea de motion
graphics se hace ahí y AE queda para lo que necesita alfa (rótulos sobre placas, marca de caso,
lower thirds).
