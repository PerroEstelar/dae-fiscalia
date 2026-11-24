# Revisión con pantallazos marcados (24 nov 2026)

Pedido de Sebastián: «solo hagamos exceles de revisiones… sin miniaturas, solo comentarios breves y concisos y
con screenshot de cada diapositiva como están en este momento, no nuestras versiones sino las que nos han
enviado», y después: «los screenshots sí deben llevar unas diagramaciones tipo Paint de flechas tipo hechas a
mano o círculos de qué debería cambiar y hacia dónde». Comentarios: una frase breve por diapositiva.

## Pasos

1. **Pantallazos** (`pantallazos.py`, en la máquina de Sebastián): Chrome sin ventana con DevTools y un perfil
   aparte, `view.genially.com/<id>`, flecha derecha. La página actual se lee del rótulo accesible
   «Page N of M, <nombre de la diapositiva>», así que un clic que revela elementos no cuenta como
   diapositiva. Junto a cada PNG (1280 × 720) queda un JSON con las cajas de texto e imágenes visibles de la
   página y de cada iframe (Runtime por contexto, con `--disable-site-isolation-trials`;
   `DOM.getFrameOwner` + `DOM.getBoxModel` para ubicar el iframe). Dos corridas en paralelo
   (puertos 9333/9334) hacen DA (299) y DP (216) en unos 20 min.
2. **Comentario y marcas por diapositiva** (`specs/<curso>_uN.py`): `S['U1 L1'][n] = (comentario, marcas)`,
   con `n` igual al número del pantallazo. Marcas: `c` círculo, `x` tachón, `s` subrayado, `f` flecha
   «unir/mover hacia», `+` recuadro punteado «falta aquí». El blanco es un texto a buscar (se ubica con las
   cajas del JSON), una zona (`zona:titulo`, `zona:escena`, `zona:video`, `zona:sig`…) o un rectángulo.
3. `aplicar.py DA|DP` dibuja las marcas (trazo rojo sobremuestreado con temblor, nota en Kalam Bold con
   borde rojo) y avisa si un texto no se encontró o si faltan comentarios. Un blanco grande va en
   recuadro redondeado y no en elipse.
4. `hoja.py` / `hojam.py`: hojas de contactos para revisar (todas, o solo las marcadas).
5. `excel_rev.py DA|DP <salida>`: «REVISION COMENTARIOS - <CURSO>.xlsx», hojas «Unidad N - revisión»
   (fila 1 = lecciones con su título, columna A = número de diapositiva del pantallazo) y
   «Generales - revisión» (`generales_<curso>.json`). Arial 20, «Bien así.» en gris, texto en sharedStrings.

DP: los comentarios salen de la revisión del 23 nov (`dp_viejos.py` los lleva de la fila del mapa a la
escena E##) acortados a una frase.

Entregado en «Mi unidad › Revisiones Sebastián › <curso>»: el Excel y `Pantallazos/<U# L#>/U# L# - NN.png`.
Terminaciones anticipadas no tiene Genially enviado (solo los nuestros), así que no lleva pantallazos.
