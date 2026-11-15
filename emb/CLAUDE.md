# emb/CLAUDE.md — Proyecto Empresa Metro de Bogotá (EMB)

Este apartado es **otro cliente**. El CLAUDE.md de la raíz sigue valiendo para todo lo técnico
(Resolve, ffmpeg, Kling, voces, rejilla, entregas), pero **lo de marca, color y contenido se
rige por este archivo**. Donde los dos choquen, manda este.

Cadena: JP Soluciones Digitales → UECP, Facultad de Ingeniería, Universidad Nacional →
Empresa Metro de Bogotá S.A. Las fuentes viven en el Drive de JP (ver `cursos/*/README.md`).

---

## Lo que cambia respecto a la serie DAE (decidido por Sebastián, 14 nov 2026)

1. **Color.** El entorno NO va en grises. Las placas van a color natural, contenido.
   El **rojo** y el **amarillo** de la marca son los protagonistas y se **reservan** para dirigir
   la atención: la ropa o un accesorio de la persona que importa en el plano, un objeto clave,
   o la luz. Nada de rojos ni amarillos sueltos de relleno (carros, letreros, toldos al azar):
   si aparecen, compiten con el acento.
   - Rojo Metro `#DF1F15` · Amarillo Metro `#FFC400` (medidos del SVG oficial del logo).
   - El tren de la Línea 1 es rojo: cuando aparece, ES el acento del plano.
2. **Personajes sin nombre, pero fijos.** No se les pone nombre (el texto dice «una
   comerciante», «la persona cuidadora»). Sí se hace **hoja de personaje** de cada uno, y toda
   placa en que aparezca se pide con su hoja como referencia. Ver `cursos/cultura-de-paz/personajes.md`.
3. **Metro: mezcla de real e hipotético.** Se buscan referencias reales del tren y de las
   estaciones/viaducto de la Línea 1 y se generan versiones verosímiles pero no idénticas. Los
   casos del curso son hipotéticos: ningún plano debe poder leerse como «esta estación, este
   día». **Placa limpia sigue vigente**: ningún logo ni texto legible en la imagen generada
   (tampoco el logo del Metro en el tren). Todo logo entra en motion graphics.
4. **El documento es guía, no guion literal.** A diferencia de la Fiscalía, los textos de la
   UECP son la base técnica; nosotros los entregamos de forma más amable y accesible.
   - Lo que **sí** se mantiene: no se agregan conceptos, autores, normas ni datos que el módulo
     no traiga. Se resume, se ordena y se dice más simple; no se inventa contenido.
   - Las frases de diálogo que el texto trae literal («Nos hicieron perder la mañana y nadie
     responde») se pueden poner en boca de un personaje.
   - Las tablas e infografías del documento se rehacen como **motion graphics estandarizados**.
5. **Los videos no le restan tiempo a la lección.** Los tiempos del documento (10/15/5 min) son
   un promedio de lectura para el usuario; el video es un recurso aparte.
6. **Sin lengua de señas por ahora.** Subtítulos: pendiente de definir, pero conviene dejarlos
   listos (la EMB tiene manual de contenidos accesibles, CC-MN-004).
7. **Voz:** narración en ElevenLabs desde la cuenta de Sebastián, acento latino neutro,
   cifras y normas **en letras** («Ley mil setecientos doce de dos mil catorce»).
8. **Duración:** sin mínimo. Si queda corto, mejor.

9. **Estilo de ilustración** (referencia de Sebastián, 14 nov 2026): ilustración urbana a mano,
   tinta suelta de grosor vivo sobre color plano con textura de gouache, paleta apagada (cielo
   gris verdoso, verdes salvia, concreto, ladrillo desvaído) y ciudad llena de detalle: cables,
   antenas, tanques, rejas, matas. Encuadre de cine: primer plano que enmarca, diagonales que
   llevan al acento. Reemplaza el estilo plano sin contorno de la Fiscalía.
10. **Lenguaje de animación:** dinámico, expresivo, cinematográfico, al nivel más profesional.
   Las ilustraciones no se cortan: entran y salen integradas con el motion (máscaras, cámara 2.5D,
   líneas guía que se dibujan sobre la escena, transiciones con el tren).

## Lo que se mantiene de la casa

- Voz primero → rejilla por proporción de caracteres → placas → loops → cartones → música.
- Método de prompts hero, bloque de escenario colombiano (aquí: Bogotá), reglas de Kling
  (todo movimiento llega a destino, nada «a punto de», recortar ventana antes que regenerar).
- Nunca mayúsculas sostenidas en cartones. Tildes, ñ, ¿ y ¡ siempre.
- Nada se borra: `_descartes`. Medir, no asumir.
- Formato 23,976 · 1920×1080, ranuras codificadas con etiqueta **bt709** desde el primer
  render (lección del V05 de DA: sin etiqueta Resolve las sube 13–15 % de saturación).

## Marca

Todo en `marca/marca_y_motion.md`: logos, colores, tipografías, lenguaje gráfico del sitio,
línea de motion graphics, intro/outro y Magnific Move.

## Repo

Este apartado `emb/` es solo texto y se empuja de una, como el resto del repo. Medios en
disco, en una carpeta propia del EMB (por definir con Sebastián, p. ej. `E:\EMB MASTER`).

## Revisión del Video 1, corte sin voz (Sebastián, 15 nov 2026)

- **Fondos de tarjetas en duotono amarillo, no rojo.** El rojo intenso a cuadro completo pesa
  demasiado cuando se habla de violencia. Los `*_duoY.jpg` se hacen desde la placa con desenfoque
  de 16 px y tres paradas (#2E2406 → #D6A000 → #FFF0C4); la cabecera va en #212529.
- **Su transición favorita es el vagón** (barrido del tren rojo). Reemplaza al iris.
- **Nada de pausas muertas**: el clip del título no se congela; la ventana se abre antes (d=104).
- **Una mano en primer plano tiene que salir del cuadro con su brazo.** El A3 tenía manos
  flotando en medio del cuadro; se rehizo por encima del hombro, los antebrazos entrando por el
  borde inferior y la manga continua fuera de cuadro.
- **Un elemento que pasa de una sección a otra no puede saltar.** La tarjeta 2.5D de la escalera
  vuelve a cuadro completo desde su estado exacto (mismo cuadro del clip, misma escala, sin
  vaivén) y sin solape de dos copias; la escalera se desvanece antes del relevo.
- **Las puertas del vagón necesitan tiempo para leerse**: cierran en 18 cuadros, quedan
  cerradas 4 y abren en 22.
- **Movimiento de Kling: pedir la escena entera**, no solo el gesto. Una cámara que avanza suave
  sobre el hombro, alguien que cruza al fondo, hojas que se mueven; el resultado es más orgánico.
  Sigue valiendo que todo movimiento llegue a destino.
- La voz la genera él en su cuenta. `herramientas/voz/calzar_emb.py` reparte los bloques sobre la
  voz medida (fronteras en las pausas más cercanas a la proporción de caracteres) y
  `voz_a_escena.py` lo convierte en `window.VOZ` para la escena.

## Kling con multitudes, y la palabra «sigh» (revisión V2–V4, 15 nov 2026)

- Una multitud a la que se le pide «reacciona» reacciona al unísono: aplauden todos o giran
  todos juntos, y se lee robótico. Se pide una acción distinta por persona, en un momento
  distinto, y «nadie aplaude».
- «Sigh» o «exhala» producen un soplo de vapor delante de la boca: la persona parece fumar.
  No se escribe; la respiración se pide como «los hombros suben y bajan apenas».
- Dos trenes que se funden en uno: el plano de metro se pide con un solo tren, en una sola
  dirección, y se mira la cola (en a01n aparece un rótulo desde el cuadro 55).
