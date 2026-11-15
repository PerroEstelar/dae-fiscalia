# -*- coding: utf-8 -*-
"""Unidad 3, lección 4 de Delitos ambientales: la investigación financiera (15 nov 2026).

**Pedido.** Sebastián: «de igual manera ahora con este, ambiental unidad 3 lección 4».

**Fuente.** Drive, curso → `VIDEOS/ambiental_unidad3_leccion4.mp4`.
- Es una grabación de Teams de 5:27, 1280×720 a 30 fps, con el fondo virtual del
  edificio y el panel DAE/Fiscalía.
- Abajo a la izquierda trae quemado el nombre de Teams, «Alba Lucía Solís Ramírez»
  (y 683–705).
- Audio: −17,2 LUFS, pico +0,2 dBTP.
- Viene editada a partir de varias tomas, y trae siete defectos (medidos cuadro a
  cuadro sobre el panel):
  1. cuadros 0–30: negro, mientras ella dice «Cordial saludo»;
  2. 799–827 (26,6 s): un cubo 3D entre tomas, con el audio en silencio digital;
  3. 1921–1949 (64,0 s): otro cubo;
  4. 4355–4365 (145,2 s): un fundido desde blanco;
  5. 8592–8620 (286,4 s): un cubo, dentro de una toma repetida;
  6. 8753–8792 (291,8 s): 1,3 s de negro;
  7. 9820–9821: negro al final.
- Y dos tomas repetidas:
  - «…quiénes aparecen formalmente como propietarios y quién es el verdadero
    beneficiario, eh, final económico» (223,4–231,3), que se repite limpia en
    232,8;
  - «Posteriormente, se realiza la recolección… y finalmente elabora un informe
    técnico de laboratorio» (279,1–291,4), que se repite corregida en 292,2: «…la
    elaboración de informes técnicos que apoyen la toma de decisiones del fiscal».

**Qué se hace** (`TRAMOS` y `CONGELA`):
- **El arranque.** Empieza en «Mi nombre es» (0,867). Cinco cuadros quietos tapan el
  final del negro. «Cordial saludo» queda fuera: se dice sobre negro.
- **Cubos y fundido.** Se tapan con el primer cuadro limpio, quieto, y el audio
  sigue corrido. Es lo que se hizo en la U4 L1.
- **Las tomas repetidas** se cortan y se queda la buena. Los cortes caen en pausas y
  llevan fundidos de audio de 15 ms. Después de cada corte, hasta el final de la
  frase, va un plano más cerrado (1024×576 desde (96, 40), como en el cierre de
  Bienes) para que el salto se lea como cambio de plano.
  - **Primer corte:** «…qué activos fueron adquiridos, | Quién aparece formalmente
    como propietario y quién es el verdadero beneficiario económico.»
  - **Segundo corte:** el «Posteriormente,» de la primera toma, y de la segunda «la
    recolección y procesamiento de información y, finalmente, la elaboración de
    informes técnicos que apoyen la toma de decisiones del fiscal». La segunda toma
    arranca en negro, así que su «Posteriormente» no tiene imagen.
- **Bordes a mitad de cuadro**, por lo que pasó en la U3 L5.

**Profe.** «Mi nombre es Alba Lucía Solís Ramírez, líder del grupo investigativo
contra la criminalidad organizada, análisis de investigaciones financieras, de la
Delegada contra la Criminalidad Organizada». Más adelante nombra al grupo como GAIF.

**Ventana: 1143×643 desde (0, 30), ×1,68.**
- Ella está al centro: la cabeza va de x≈615 a 860.
- Con esta ventana el pelo empieza en x≈907 de salida (p10) y la columna estándar
  (615) termina en 785.
- Abajo termina en y=673, antes del nombre quemado (683).
- El panel (y 46–134) entra entero.
- El plano cerrado de después de los cortes deja el pelo en x≈750–770. Por eso ahí
  no va ningún cartón.

**Textos.** Salen de Scribe (WAV a 16 kHz), sin muletillas.
- «Resolución cero cuarenta y dos del 5 de mayo del 2026» se escribe tal cual:
  Resolución 0042 del 5 de mayo de 2026.
- DIACO es la Dirección de Apoyo de Investigaciones y Análisis de la Criminalidad
  Organizada, como ella la nombra.

Los tiempos son segundos de la fuente; `cuadro` los pasa a la línea descontando los
cortes.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'herramientas',
                                'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
FQ = 30.0                               # la fuente
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
R = CURSO + '/UNIDAD 3/LECCION 4'
BIN = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE', 'UNIDAD 3', 'LECCION 4']
ORIGINAL = R + '/01 VIDEO/ambiental_unidad3_leccion4.mp4'
COMPUESTO = R + '/01 VIDEO/U3L4_compuesto_v2.mp4'   # el v1 (en _descartes) tenía 5 cuadros de más: los congelados se medían en segundos
TITULO = R + '/02 CARTONES/carton titulo ambientales u3 leccion 4.mp4'
TITULO_BASE = CURSO + '/UNIDAD 1/02 CARTONES/carton titulo ambientales u1v2.mp4'
SUB = 'Unidad 3. Lección 4'
NOMBRE_LINEA = 'MA - U3 - LECCION 4'
EXPORT = 'delitosambientales - U3 - LECCION 4-v%d'
PREFIJO = 'U3L4'
TMP = 'D:/DAE/_tmp/ma/u3l4'
XY, VENTANA = (0, 30), (1143, 643)
CERRADO = (96, 40, 1024, 576)
LT = (44, 560)                          # lower third: px del nombre y ancho del cargo (estándar 48 y 900)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
MASTER_DIR = 'D:/DAE/_masters_archivo/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/UNIDAD 3/LECCION 4'


def _c(k):
    """Borde a mitad del cuadro k de la fuente."""
    return (k + 0.5) / FQ


TRAMOS = [
    (26 / FQ, _c(6695), None),          # «Mi nombre es…» … «qué activos fueron adquiridos,»
    (_c(6980), _c(7166), CERRADO),      # «Quién aparece formalmente… económico.» (la toma limpia)
    (_c(7166), _c(8404), None),         # … «Posteriormente,» (de la primera toma)
    (_c(8795), _c(9095), CERRADO),      # «la recolección… decisiones del fiscal.» (la segunda toma)
    (_c(9095), _c(9818), None),         # … «difícilmente sobreviven cuando se afectan las finanzas criminales.»
]
CONGELA = [(26 / FQ, 31 / FQ),          # el final del negro del arranque
           (799 / FQ, 828 / FQ),        # cubo
           (1921 / FQ, 1950 / FQ),      # cubo
           (4355 / FQ, 4366 / FQ)]      # fundido desde blanco

ANCHO = 615
NOMBRE_CURSO = ('Investigación y judicialización de delitos contra el medio ambiente y los '
                'recursos naturales')
PROFE = ('Alba Lucía Solís Ramírez',
         'Líder del Grupo de Análisis de Investigaciones Financieras, Delegada contra la Criminalidad '
         'Organizada')


def cuadro(t):
    """Segundos de la fuente → cuadro de la línea, descontando los cortes."""
    acum = 0.0
    for a, b, _w in TRAMOS:
        if a - 1e-6 <= t <= b + 1e-6:
            return CLIP0 + int(round((acum + t - a) * FPS))
        acum += b - a
    raise ValueError('%.2f cae en un corte' % t)


def _p(texto, peso, px, gap):
    # renglones parejos (herramientas/cartones/balanceo.py): sin palabras solas abajo
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def c_ante(ante, titulo, cuerpo=None):
    ls = _p(ante, 'med', ANTE, 0) + _p(titulo, 'bold', TIT, GAP_ANTE)
    if cuerpo:
        ls += _p(cuerpo, 'med', CUE, GAP_CUE + 8)
    return ls


def c_suelta(t):
    return _p(t, 'bold', SUELTA, 0)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}


ITEMS = [
    ('lt01', 'lt', 1.1, 12.3, PROFE),
    ('c01_herramienta', 'carton', 12.6, 26.6, c_tit(
        'La investigación financiera',
        'Una herramienta estratégica para fortalecer las investigaciones por delitos contra el '
        'medio ambiente y los recursos naturales.')),
    ('c02_resolucion', 'carton', 29.0, 41.5, c_ante(
        'Resolución 0042 del 5 de mayo de 2026', 'Grupo de Análisis de Investigaciones Financieras',
        'Para las investigaciones sobre finanzas criminales.')),
    ('c04_transversal', 'carton', 65.1, 77.2, c_tit(
        'Un apoyo transversal',
        'Identificar las finanzas ilícitas y debilitar a las organizaciones criminales.')),
    ('m01_analisis', 'mg_lista', 83.0, 93.8, lista(
        None,
        ('libreta', 'Información contable', 85.1),
        ('doc_check', 'Tributaria', 86.4),
        ('finanzas', 'Financiera', 87.3),
        ('billete', 'Cambiaria', 88.2),
        ('edificio', 'Societaria', 89.6))),
    ('m02_fundamental', 'mg_lista', 99.4, 112.3, lista(
        'Es fundamental',
        ('lupa_doc', 'El contexto delictivo', 100.1),
        ('red', 'La estructura y los roles', 102.4),
        ('billete', 'Cómo se recaudan y movilizan los recursos', 108.3))),
    ('m03_identificar', 'mg_lista', 112.4, 122.0, lista(
        None,
        ('casa_lote', 'Bienes y productos financieros', 112.4),
        ('calendario', 'El periodo de la investigación', 116.8))),
    ('c06_diaco', 'carton', 122.3, 136.5, c_ante(
        'Si no está claro', 'Articularse con la DIACO',
        'Dirección de Apoyo de Investigaciones y Análisis de la Criminalidad Organizada.')),
    ('c07_focalizada', 'carton', 137.7, 146.4, cita(
        'Cuanto más clara sea la información que llega al GAIF, más focalizada será la '
        'investigación financiera.')),
    ('m04_capacidades', 'mg_lista', 146.6, 158.5, lista(
        '¿Qué aporta el GAIF?',
        ('finanzas', 'Análisis financieros y patrimoniales', 150.5),
        ('ruta', 'Trazabilidad de recursos', 153.8))),
    ('m05_capacidades2', 'mg_lista', 158.6, 168.8, lista(
        None,
        ('persona', 'Beneficiarios finales', 158.6),
        ('lupa_persona', 'Incrementos patrimoniales injustificados', 159.6),
        ('binoculares', 'Seguimiento de activos', 162.9),
        ('edificio', 'Estudios societarios', 164.7))),
    ('c08_porque', 'carton', 169.0, 175.0, cita(
        '¿Por qué es tan importante en los delitos ambientales?')),
    ('m06_afectacion', 'mg_lista', 181.2, 194.0, lista(
        'La afectación',
        ('mineria', 'Una mina ilegal', 182.3),
        ('tala', 'Un bosque deforestado', 183.4),
        ('excavadora', 'La maquinaria amarilla', 185.1),
        ('ruta', 'El transporte de minerales', 187.9))),
    ('c10_encontrarse', 'carton', 200.9, 207.6, cita(
        'Ahí deben encontrarse la investigación ambiental y la investigación financiera.')),
    ('m07_preguntas', 'mg_lista', 211.0, 223.1, lista(
        'Hay que preguntarse',
        ('finanzas', '¿Quién financió?', 215.0),
        ('persona', '¿Quién se benefició?', 216.4),
        ('billete', '¿De dónde llegó el dinero?', 217.6),
        ('edificio', '¿Qué empresas y qué activos?', 219.0))),
    ('c11_ruta', 'carton', 239.2, 243.9, c_suelta('Seguir la ruta del dinero')),
    ('c12_articulacion', 'carton', 244.0, 257.4, c_tit(
        'La articulación con el GAIF',
        'Un agendamiento con el fiscal y los investigadores de campo para presentar el caso al '
        'grupo financiero.')),
    ('m08_metodologia', 'mg_lista', 263.6, 280.1, lista(
        'Una metodología de trabajo',
        ('bombilla', 'La hipótesis financiera', 266.6),
        ('personas', 'Personas naturales y jurídicas', 269.8),
        ('calendario', 'El periodo de análisis', 275.0))),
    ('c13_conjunto', 'carton', 303.9, 314.0, c_tit(
        'Un trabajo conjunto',
        'Fiscales, investigadores, analistas y asistentes financieros, e investigadores de campo.')),
    ('c14_finanzas', 'carton', 314.2, 327.2, cita(
        'Las organizaciones criminales pueden reemplazar personas, rutas y mecanismos operativos, pero '
        'difícilmente sobreviven cuando se afectan sus finanzas.')),
]
