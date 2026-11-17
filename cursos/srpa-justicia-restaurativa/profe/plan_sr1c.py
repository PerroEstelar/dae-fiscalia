# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de SRPA (17 nov 2026).

**Fuente.** `srpa_u1_cierre_fuente.mp4` (Drive del curso → VIDEOS/UNIDADES, «Unidad 1 -
cierre.mp4», `18Gdlyg_7e0q_6stYaBnG48pSAENnca9A`, subida el 12 nov): grabación de Teams,
1280×720, 30 fps parejos (30.470 cuadros, 1.015,67 s), BT.601, AAC estéreo a −18,9 LUFS.
Estanislao Escalante Barreto (el mismo fondo y encuadre del cierre del curso; se comparó con
cuadros de sus otros videos). STT (Scribe, WAV a 16 kHz): 2.571 palabras, de 1,22 a 1.015,18 s.
No hay tomas repetidas ni frases cortadas: va entera.

**La lámina.** Del minuto 5:45 al 13:49 el profe comparte una diapositiva («La visión
multidimensional del SRPA. Una apuesta para su comprensión») y él queda en una miniatura a la
izquierda. Ese tramo va a cuadro completo (1276×718 desde (0, 2), ×1,5) y sin gráficos: la lámina
ya es el gráfico, y es blanca. La ventana deja fuera la raya negra de 1 px que Teams pone en y=0.
- **Entrada.** Teams hace un barrido de los cuadros 10343 a 10371; la lámina queda limpia en el
  10372. El tramo de la lámina empieza en el 10343 y esos 29 cuadros muestran quieto el 10372
  (`CONGELA`): se ve un corte seco del profe a la lámina.
- **Salida.** La lámina se mueve desde el cuadro 24840 (un cubo 3D), salta al profe en el 24860 y
  el profe queda asentado hacia el 24872. Los cuadros 24840–24871 muestran quieta la lámina del
  24839 (`CONGELA` con 'antes') y el profe entra en vivo en el 24872 (829,07 s), 0,2 s después
  de empezar «Ahora bien, para finalizar». Así no se congela una cara que habla.
Medido cuadro a cuadro (`D:\DAE\_tmp\sr_ta\prep\prep1.log`): diferencia media contra el cuadro
anterior y contra un cuadro limpio de cada lado.

**Ventana 1088×612 desde (0, 44), ×1,765**, en los dos tramos del profe. Está centrado y cerca:
el borde izquierdo de la cabeza va de x 388 (p5) a 448 (p50) de la fuente, así que queda desde
x≈685 de salida y la columna de texto es de 470. El panel DAE/Fiscalía entra entero. Probado con
la caja dibujada sobre 16 cuadros.

**Textos.** Sus palabras, sin muletillas ni repeticiones. «Ley de infancia y adolescencia» va
en minúscula, como en los otros videos del curso.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_sr_profe import *  # noqa: E402,F401,F403
from base_sr_profe import armar, ESTANISLAO, cita, c_tit, c_ante, lista  # noqa: E402

XY, VENTANA = (0, 44), (1088, 612)
# el cargo de Estanislao es largo: a 440 de ancho daba cinco renglones y el último se salía del cuadro.
# A 560 son tres, parejos, y termina en x≈680, sobre el saco (el nombre, en x≈726).
LT = (40, 560)
LAMINA = (0, 2, 1276, 718)
K_ENTRA, K_LAMINA, K_MUEVE, K_PROFE, K_FIN = 10343, 10372, 24840, 24872, 30470
globals().update(armar(
    'srpa_u1_cierre_fuente.mp4', 'UNIDAD 1/CIERRE', 1, 'SRPA - U1 - CIERRE', 'srpa - U1 - CIERRE', 'SR1C',
    [(0.0, K_ENTRA / 30.0, None), (K_ENTRA / 30.0, K_PROFE / 30.0, LAMINA), (K_PROFE / 30.0, K_FIN / 30.0, None)]))
CONGELA = [(K_ENTRA / 30.0, K_LAMINA / 30.0), (K_MUEVE / 30.0, K_PROFE / 30.0, 'antes')]
# v2 del compuesto: la lámina sin la raya negra de y=0 (a 1080 era un filete oscuro arriba durante
# ocho minutos). Solo cambió la imagen (`ic_pieza reimagen`); la v1 está en `01 VIDEO/_descartes`.
COMPUESTO = R + '/01 VIDEO/SR1C_compuesto_v2.mp4'  # noqa: F821

ITEMS = [
    ('lt01', 'lt', 1.0, 9.0, ESTANISLAO),
    ('c01_sentido', 'carton', 17.6, 26.1, c_ante(
        'En primer lugar', 'El sentido de la ley de infancia y adolescencia')),
    ('c02_paradigma', 'carton', 30.2, 43.9, c_tit(
        'Un cambio de paradigma',
        'Nos quita la idea de que toda la justicia de infancia y adolescencia era una justicia tutelar.')),
    ('m01_sujeto', 'mg_lista', 55.4, 67.4, lista(
        None,
        ('escudo', 'Sujeto de especial protección constitucional', 56.3),
        ('persona', 'Sujeto de derechos', 60.4),
        ('balanza', 'Sujeto responsable', 63.3))),
    ('c03_irregular', 'carton', 67.5, 74.5, c_ante(
        'Antiguamente', 'Una persona en situación irregular')),
    ('c04_menores', 'carton', 86.4, 97.3, cita(
        'Quienes estaban en normalidad eran niños o niñas, y quienes no lo estaban eran menores.')),
    ('c05_institucionalizacion', 'carton', 108.2, 116.6, cita(
        'La medida que prevalecía era una medida de institucionalización.')),
    ('c06_principios', 'carton', 134.2, 143.0, cita(
        'Prevalecen principios y valores constitucionales que tienen fuerza normativa.')),
    ('c07_orden', 'carton', 143.2, 155.0, c_ante(
        'Privar de la libertad a un adolescente',
        'Requiere una orden judicial en el marco de un proceso penal')),
    ('c08_ratio', 'carton', 174.4, 185.6, c_tit(
        'Última ratio',
        'El último elemento al que acuda la justicia cuando se trata de un adolescente.')),
    ('c08b_forma', 'carton', 189.7, 197.4, cita(
        'Ver al niño como sujeto de derechos nos ha cambiado totalmente la forma de aplicar la ley.')),
    ('m02_titular', 'mg_lista', 201.2, 217.0, lista(
        None,
        ('personas', 'Los derechos de los adultos', 202.2),
        ('persona', 'Otros derechos por su edad', 205.1),
        ('escudo', 'Protección constitucional', 209.5),
        ('balanza', 'Carácter prevalente', 212.6))),
    ('m03_principios', 'mg_lista', 237.8, 246.9, lista(
        None,
        ('escudo', 'Interés superior del adolescente', 238.7),
        ('balanza', 'Libertad y pro infans', 241.9))),
    ('m04_principios', 'mg_lista', 247.0, 257.6, lista(
        None,
        ('grupos', 'Corresponsabilidad', 247.3),
        ('birrete', 'Pedagógico, educativo y restaurativo', 251.3))),
    ('c09_adultos', 'carton', 265.7, 275.1, cita(
        'El sistema penal no es el sistema de adultos aplicado a menores de edad.')),
    ('c10_centro', 'carton', 282.6, 291.6, c_tit(
        'En el análisis dogmático penal', 'El adolescente como centro de todo el esquema del delito.')),
    ('m05_categorias', 'mg_lista', 295.6, 308.3, lista(
        None,
        ('lupa_doc', 'La tipicidad', 296.5),
        ('persona', 'El error, la voluntad, el dolo', 298.2),
        ('balanza', 'La antijuridicidad', 301.3),
        ('mazo', 'La culpabilidad', 302.3))),
    ('c10b_aislado', 'carton', 312.8, 321.3, cita(
        'El proceso no puede ser un sistema de audiencias orales aislado.')),
    ('c11_proceso', 'carton', 322.3, 333.2, c_tit(
        'En el proceso',
        'Aplicar materialmente el principio educativo, el restaurativo y el pedagógico.')),
    ('m06_explicar', 'mg_lista', 335.9, 344.6, lista(
        None,
        ('mundo', 'En qué contexto están', 336.9),
        ('mazo', 'De qué trata la audiencia', 338.6),
        ('personas', 'Quiénes están a su alrededor', 339.9))),
    ('c12_no_solo', 'carton', 830.6, 840.0, cita(
        'Los principios no solamente son los que están en la ley de infancia y adolescencia.')),
    ('c13_ley_penal', 'carton', 840.2, 848.6, c_tit(
        'Los principios de la ley penal', 'También cobijan a la infancia y la adolescencia.')),
    ('m07_ley_penal', 'mg_lista', 848.8, 862.0, lista(
        None,
        ('escudo', 'La presunción de inocencia', 849.2),
        ('balanza', 'El principio de culpabilidad', 850.9),
        ('lupa_doc', 'El principio de tipicidad', 852.7),
        ('libro_ley', 'La no retroactividad de la ley penal', 854.4))),
    ('c14_procesal', 'carton', 866.1, 879.4, c_tit(
        'Los principios de la ley procesal penal',
        'También cobijan a los adolescentes, en el marco de su sistema especial y diferenciado.')),
    ('c15_corte', 'carton', 882.7, 897.1, c_ante(
        'Corte Suprema de Justicia', 'Revoca una decisión',
        'El tribunal impone una medida no prevista en la sentencia de primera instancia.')),
    ('c16_inamovibles', 'carton', 915.7, 926.0, cita(
        'En la ley procesal penal esos principios son inamovibles, y en materia de infancia y '
        'adolescencia también aplican.')),
    ('m08_sistema', 'mg_lista', 927.0, 940.3, lista(
        None,
        ('balanza', 'La ley penal', 928.0),
        ('mazo', 'La ley procesal penal', 929.6),
        ('libro_ley', 'La Constitución', 931.5),
        ('familia', 'La ley de infancia y adolescencia', 933.0))),
    ('c16b_normativo', 'carton', 952.6, 965.7, cita(
        'Todos esos principios hacen parte del sistema normativo que cobija la responsabilidad penal '
        'para adolescentes.')),
    ('c17_proxima', 'carton', 970.1, 978.7, c_ante(
        'La próxima unidad', 'Autoridades y políticas públicas de prevención')),
    ('m09_proxima', 'mg_lista', 980.6, 994.0, lista(
        None,
        ('grupos', 'El enfoque diferencial en las instituciones', 981.5),
        ('persona', 'La presunción de minoría de edad', 986.6),
        ('lupa_doc', 'La evaluación de políticas públicas', 989.2))),
    ('c18_especial', 'carton', 1002.0, 1012.8, cita(
        'Un sistema especial, diferenciado, con un enfoque educativo, pedagógico y restaurativo.')),
]
