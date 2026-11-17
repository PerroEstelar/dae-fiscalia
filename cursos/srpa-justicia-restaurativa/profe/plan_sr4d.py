# -*- coding: utf-8 -*-
r"""Desarrollo de la unidad 4 de SRPA: la clase completa (17 nov 2026).

**Fuente.** `srpa_u4_inicio_v2_fuente.mp4` (Drive del curso → VIDEOS/UNIDADES,
«SRPA_unidad_4_inicio_v2.mp4», `1lDPp4niSdZZ1th82hPZfZOmxcn6S3x02`, subida el 17 nov): grabación
de Teams, 1280×720, 30 fps parejos (60.414 cuadros), BT.601, AAC estéreo a −13,0 LUFS con picos
de +1,5 dBTP. Carlos Humberto Ramírez Romero (ver `plan_sr4b`). Los primeros 3.522 cuadros son la
bienvenida de la unidad, que es otra pieza; esta va del cuadro 3570 (119,0 s, 0,8 s antes de
«Sean ustedes bienvenidos, queridos discentes, a nuestra unidad número cuatro») al 60390
(2.013,0 s; el audio queda en silencio digital desde 2.012,6). STT (Scribe, WAV a 16 kHz): 4.183
palabras en todo el archivo. No hay frases repetidas.

**La fuente ya viene montada con tomas.** Medido cuadro a cuadro (`prep_u4.py`: diferencia media
contra el cuadro anterior y diferencia del panel DAE/Fiscalía contra su mediana; tiras en
`D:\DAE\_tmp\sr_ta\tira_u4_*.jpg` y `saltos_u4.jpg`):
- **Un cubo 3D** entre dos bloques, cuadros 23181–23210 (772,7–773,7 s), en la pausa entre
  «…frente a la reparación integral.» y «Ahora bien, el módulo…». Se tapa con el primer cuadro
  limpio de después, quieto (`CONGELA`, cuadros 23181–23211 → el 23212).
- **Cuatro cortes secos de toma** (un pico aislado de la diferencia, con la cabeza en otro sitio):
  cuadros 24199 (806,63 s, «Todos recordamos | el impacto…»), 48933 (1.631,10 s, «Continuamos |
  con la lección número cuatro»), 51964 (1.732,13 s, «los cuales | quedarán autorizados») y
  60291 (2.009,70 s, «Muchas gracias. | Finalizamos unidad número cuatro.»). Después de cada uno
  va el **plano cerrado** hasta la pausa del final de la frase, para que el salto se lea como
  cambio de plano; ahí no va ningún gráfico.
- En el cuadro 29134 (971,13 s) hay otro corte, casi sin desplazamiento (diferencia 3,5): se deja.

**Ventana 1143×643 desde (12, 30), ×1,68**, la de la presentación y el desarrollo de la unidad 3.
Borde izquierdo de la cabeza: x 588 (p50), 521 (p5), 453 (p1) de la fuente → x≈968, 855 y 741 de
salida. Con la caja en x 86–750 de salida, la persona pasa del 1,5 % de la caja 12,5 s en todo el
archivo (manos, de a medio segundo; `caja_u4.log`). **Columna de 560.**
**Plano cerrado 960×540 desde (20, 34), ×2,0**, en los tres primeros: el panel DAE/Fiscalía
(x 35–497, y 42–142) entra entero. El tope de la cabeza va de y 148 a 218 y el borde derecho no
pasa de x 914 (`cerrado_u4.log`): el mentón queda dentro (la ventana termina en y=574). No hay
ventana que deje el panel afuera sin cortar la cabeza.
**El último plano cerrado es otro: 960×540 desde (140, 146)**, sin el panel. En esa toma el profe
está más abajo (tope en y 238) y al final se inclina: con la ventana de los otros tres el mentón
tocaba el borde y en el último medio segundo se cortaba la boca. Se vio en la tira de 4 cuadros
por segundo de la simulación, con el compuesto v1 ya hecho. El **compuesto v2** cambia solo esos
99 cuadros (ver `COMPUESTO` más abajo).

**Textos.** Sus palabras, sin muletillas. Los nombres de las lecciones, los de la ficha. «Howard
Zehr» y «Flórez y Peña (2025)», como los escribe la ficha (Scribe oyó «Johan Ser» y «Flores»).
El auto de la Sala de Casación Penal es el AP1827-2026, radicación 65824 (ficha, lección 4).

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_sr_profe import *  # noqa: E402,F401,F403
from base_sr_profe import armar, columna, CARLOS, cita, c_tit, c_ante, lista  # noqa: E402

XY, VENTANA = (12, 30), (1143, 643)
MAXW = columna(560)
LT = (44, 560)
CERRADO = (20, 34, 960, 540)
CERRADO_FINAL = (140, 146, 960, 540)
K_INI, K_FIN = 3570, 60390
K_CUBO, K_LIMPIO = 23181, 23212
K_C1, K_R1 = 24199, 24366
K_C2, K_R2 = 48933, 49239
K_C3, K_R3 = 51964, 52110
K_C4 = 60291
globals().update(armar(
    'srpa_u4_inicio_v2_fuente.mp4', 'UNIDAD 4/DESARROLLO', 4, 'SRPA - U4 - DESARROLLO', 'srpa - U4 - DESARROLLO',
    'SR4D', [(K_INI / 30.0, K_C1 / 30.0, None), (K_C1 / 30.0, K_R1 / 30.0, CERRADO),
             (K_R1 / 30.0, K_C2 / 30.0, None), (K_C2 / 30.0, K_R2 / 30.0, CERRADO),
             (K_R2 / 30.0, K_C3 / 30.0, None), (K_C3 / 30.0, K_R3 / 30.0, CERRADO),
             (K_R3 / 30.0, K_C4 / 30.0, None), (K_C4 / 30.0, K_FIN / 30.0, CERRADO_FINAL)]))
CONGELA = [(K_CUBO / 30.0, K_LIMPIO / 30.0)]
# v2 del compuesto: el último plano cerrado con CERRADO_FINAL. Son los últimos 99 cuadros y la v1
# tiene un cuadro clave justo en el corte (el 56721 del compuesto): se codificaron solo esos 99 con
# la misma receta y se pegaron a los primeros 56.721 de la v1 sin recodificar; el audio es el de la
# v1 (`D:\DAE\_tmp\sr_ta\cola_sr4d.py`, que compara cuadro a cuadro). La v1 está en
# `01 VIDEO/_descartes`.
COMPUESTO = R + '/01 VIDEO/SR4D_compuesto_v2.mp4'  # noqa: F821

ITEMS = [
    ('lt01', 'lt', 120.0, 128.0, CARLOS),
    ('c01_leccion1', 'carton', 128.2, 136.8, c_ante(
        'Lección 1', 'De la justicia restaurativa y la justicia terapéutica', 'Desarrollo conceptual.')),
    ('c02_no_nuevo', 'carton', 143.5, 158.6, c_tit(
        'No es un invento nuevo',
        'Es parte de las prácticas y procesos que a nivel histórico han venido desarrollando los pueblos '
        'originarios.')),
    ('c03_zehr', 'carton', 161.8, 172.7, c_ante(
        'Desde los años 70', 'La labor de Howard Zehr', 'Se retoman prácticas de carácter restaurativo.')),
    ('c05_encuentros', 'carton', 181.6, 197.0, c_tit(
        'Encuentros restaurativos',
        'En escenarios comunitarios se busca la reparación de las víctimas y garantías de no repetición '
        'de los hechos.')),
    ('c06_menonitas', 'carton', 210.7, 222.8, c_ante(
        'A partir de los años 70', 'Encuentros víctima-ofensor',
        'En comunidades menonitas de Ontario y de Indiana.')),
    ('c07_inmemoriales', 'carton', 237.5, 250.5, c_tit(
        'Ni es nuevo ni tiene un origen norteamericano',
        'Desde tiempos inmemoriales las comunidades originarias resuelven sus conflictos.')),
    ('m01_ejemplos', 'mg_lista', 262.6, 270.2, lista(
        None,
        ('mundo', 'El pueblo navajo, en Estados Unidos', 263.5),
        ('mundo', 'El pueblo maorí, en Nueva Zelanda', 265.8))),
    ('c08_definicion', 'carton', 278.4, 292.0, c_ante(
        'Justicia restaurativa', 'Un modelo alternativo de justicia',
        'Complementario al proceso penal ordinario: no lo reemplaza en ningún caso.')),
    ('m02_participan', 'mg_lista', 292.3, 309.0, lista(
        None,
        ('persona', 'La víctima', 293.2),
        ('persona', 'El ofensor', 295.5),
        ('grupos', 'La comunidad', 297.5),
        ('apreton', 'Con o sin ayuda de un tercero facilitador', 303.3))),
    ('c09_resultado', 'carton', 313.9, 324.2, c_tit(
        'Un resultado restaurativo',
        'Que desarrolle los componentes de reparación, reintegración y reconciliación.')),
    ('m03_componentes', 'mg_lista', 324.6, 357.0, lista(
        None,
        ('mano_corazon', 'Reparación a las víctimas', 324.9),
        ('persona', 'Responsabilización del ofensor', 330.2),
        ('grupos', 'Reintegración en la comunidad', 344.7),
        ('escudo', 'Garantías de no repetición', 352.4))),
    ('c11_comparativo', 'carton', 375.6, 384.9, c_ante(
        'Un cuadro comparativo', 'Justicia restaurativa y justicia penal ordinaria')),
    ('c12_delito_jr', 'carton', 393.2, 402.7, c_ante(
        'Justicia restaurativa', 'El delito es un daño ocasionado a otra persona o a la comunidad')),
    ('c13_delito_jo', 'carton', 403.0, 410.2, c_ante(
        'Justicia penal ordinaria', 'El delito es una infracción a la ley únicamente')),
    ('c14_enfasis_jr', 'carton', 417.6, 426.0, c_ante(
        'El énfasis de la justicia restaurativa', 'La singularidad del ofendido, las víctimas')),
    ('c15_enfasis_jo', 'carton', 426.7, 437.6, c_ante(
        'El énfasis de la justicia penal ordinaria',
        'La vigencia de la ley, la seguridad de la sociedad y la sanción al infractor')),
    ('c16_papel_jr', 'carton', 446.4, 452.6, c_ante(
        'En la justicia restaurativa', 'El papel central es el de la víctima')),
    ('c17_papel_jo', 'carton', 453.1, 459.8, c_ante(
        'En el proceso penal ordinario', 'El papel central está centrado en el ofensor')),
    ('c18_objetivo_jo', 'carton', 465.0, 481.5, c_ante(
        'El objetivo de la justicia penal ordinaria', 'La finalidad retributiva de la sanción penal',
        'A quien vulneró el bien jurídico se le impone una sanción.')),
    ('c19_objetivo_jr', 'carton', 494.1, 506.4, c_ante(
        'El objetivo de la justicia restaurativa', 'La construcción de un resultado restaurativo',
        'No es sancionar, no es imponer una pena.')),
    ('m04_tres_erres', 'mg_lista', 511.7, 524.0, lista(
        'Las tres erres',
        ('mano_corazon', 'Reparación', 514.7),
        ('persona', 'Responsabilización', 516.0),
        ('grupos', 'Resocialización', 518.0))),
    ('c20_responsabilizacion', 'carton', 525.5, 539.1, c_tit(
        'La responsabilización',
        'Que el ofensor interiorice la conducta y tenga manifestaciones auténticas de arrepentimiento.')),
    ('c21_reparacion', 'carton', 543.4, 555.6, c_tit(
        'La reparación',
        'Un componente de restauración a las víctimas, partiendo de sus necesidades e intereses.')),
    ('m05_compensacion', 'mg_lista', 561.2, 572.8, lista(
        'La compensación',
        ('billete', 'Económica', 564.2),
        ('mano_corazon', 'Simbólica', 565.9),
        ('circulo', 'O de otra naturaleza', 567.4))),
    ('m06_reintegracion', 'mg_lista', 587.4, 605.7, lista(
        None,
        ('escudo', 'Garantía de no repetición', 588.0),
        ('birrete', 'Formación para el ofensor', 592.7),
        ('ruta', 'Un proyecto de vida', 599.7))),
    ('c23_florez', 'carton', 613.2, 626.6, c_ante(
        'La clasificación', 'Flórez y Peña (2025)',
        'Protocolo de justicia restaurativa de la Escuela Judicial Rodrigo Lara Bonilla.')),
    ('c24_zehr_libro', 'carton', 630.5, 647.2, c_ante(
        'Howard Zehr (2010)', 'El pequeño libro de la justicia restaurativa',
        'Una tabla comparativa entre la justicia penal ordinaria y la justicia restaurativa.')),
    ('c25_ofensa_jo', 'carton', 650.0, 656.4, c_ante(
        'Justicia penal ordinaria', 'El delito es una ofensa contra la ley y el Estado')),
    ('c26_ofensa_jr', 'carton', 656.6, 665.4, c_ante(
        'Justicia restaurativa', 'El delito es una ofensa a las personas y las relaciones interpersonales')),
    ('c27_ofensas', 'carton', 665.6, 675.4, c_tit(
        'Las ofensas',
        'Para la justicia penal ordinaria generan culpabilidad; para la justicia restaurativa, obligaciones.')),
    ('c28_requiere', 'carton', 675.8, 682.6, c_ante(
        'Justicia penal ordinaria', 'La justicia requiere que el Estado imponga sanciones')),
    ('c29_involucra', 'carton', 682.8, 693.2, c_ante(
        'Justicia restaurativa', 'Involucra víctimas, ofensores y miembros de la comunidad',
        'En un esfuerzo por enmendar el daño.')),
    ('c30_preguntas', 'carton', 694.8, 701.3, c_ante('Howard Zehr', 'Las preguntas fundamentales')),
    ('m07_preguntas1', 'mg_lista', 706.6, 716.4, lista(
        None,
        ('libro_ley', 'Ordinaria: ¿qué leyes se violaron?', 706.8),
        ('persona', 'Restaurativa: ¿quién ha sido dañado?', 712.2))),
    ('m08_preguntas2', 'mg_lista', 716.6, 732.2, lista(
        None,
        ('lupa_persona', 'Ordinaria: ¿quién lo hizo?', 717.3),
        ('mano_corazon', 'Restaurativa: ¿cuáles son las necesidades?', 723.3),
        ('apreton', '¿Quién tiene la responsabilidad?', 726.7))),
    ('c31_conflicto', 'carton', 734.0, 743.3, c_ante(
        'En la justicia restaurativa', 'El delito es un conflicto',
        'Ya no es solamente una infracción a la ley.')),
    ('m09_solucion', 'mg_lista', 750.4, 760.2, lista(
        None,
        ('persona', 'El ofensor', 751.4),
        ('persona', 'La víctima', 752.5),
        ('grupos', 'La comunidad', 753.4),
        ('apreton', 'Terceros, como los facilitadores', 755.5))),
    ('m10_ofensor', 'mg_lista', 760.4, 772.4, lista(
        'Que el ofensor',
        ('doc_check', 'Se responsabilice de sus actos', 761.6),
        ('firma', 'Asuma obligaciones', 763.9),
        ('escudo', 'Brinde garantías de no repetición', 765.5))),
    ('c32_terapeutica', 'carton', 774.2, 781.8, c_ante(
        'El módulo también desarrolla', 'La justicia terapéutica')),
    ('c33_nuevo_concepto', 'carton', 791.9, 804.9, c_tit(
        'Un nuevo concepto',
        'Estudiar el proceso penal como un componente terapéutico que tiene efectos en la vida de las '
        'personas.')),
    ('c34_positivo', 'carton', 812.5, 821.9, cita(
        'La justicia terapéutica busca que ese efecto sea positivo, que no sea un efecto negativo.')),
    ('c35_tribunales', 'carton', 828.5, 843.7, c_tit(
        'Tribunales de solución de problemas',
        'Se destacan los tribunales de tratamiento de drogas, desarrollados con gran éxito en los Estados '
        'Unidos.')),
    ('c36_seguimiento', 'carton', 844.2, 857.9, c_tit(
        'Un proceso con seguimiento',
        'Los infractores son presentados ante la corte de tratamiento, que los cita periódicamente.')),
    ('m11_remision', 'mg_lista', 882.0, 894.7, lista(
        None,
        ('cruz_medica', 'Remisión a un programa de desintoxicación', 883.1),
        ('doc_check', 'Cumplir unos compromisos', 885.9),
        ('bombilla', 'Solucionar esa problemática', 888.0))),
    ('c38_alternativa', 'carton', 903.4, 915.2, cita(
        'Estas cortes son una alternativa al proceso penal ordinario, y en Colombia ya se han venido '
        'implementando.')),
    ('c39_juzgados', 'carton', 933.6, 946.2, c_tit(
        'Los juzgados penales de adolescentes',
        'Despachos especializados que buscan la solución de problemas de los adolescentes entre 14 y 18 '
        'años.')),
    ('c40_reiterativas', 'carton', 958.0, 966.2, c_ante(
        'Señores fiscales delegados', 'Las problemáticas de los adolescentes infractores son reiterativas')),
    ('m12_problematicas', 'mg_lista', 968.5, 990.4, lista(
        None,
        ('cruz_medica', 'Consumo de sustancias psicoactivas', 969.6),
        ('familia', 'Influencias negativas en su hogar', 976.6),
        ('persona', 'Alta influenciabilidad', 979.1),
        ('puerta_salida', 'Ausencia de figuras de autoridad', 983.4))),
    ('c41_finalidad', 'carton', 993.0, 1005.4, c_tit(
        'La finalidad del proceso',
        'Una solución definitiva a este tipo de casos, garantizando la no reincidencia.')),
    ('c43_programa', 'carton', 1018.5, 1028.3, c_tit(
        'Programa de Seguimiento Judicial al Tratamiento de Drogas',
        'Actualmente llamado Programa de Ruta Alterna.')),
    ('m13_lideran', 'mg_lista', 1028.5, 1042.4, lista(
        None,
        ('balanza', 'Ministerio de Justicia y del Derecho', 1028.6),
        ('cruz_medica', 'Ministerio de Salud', 1030.1),
        ('familia', 'Instituto Colombiano de Bienestar Familiar', 1035.9))),
    ('m14_rutas', 'mg_lista', 1049.3, 1061.5, lista(
        None,
        ('estetoscopio', 'Ruta de salud: la desintoxicación', 1049.5),
        ('balanza', 'Ruta jurídica: la salida alternativa', 1054.5))),
    ('c45_voluntario', 'carton', 1061.7, 1072.0, cita(
        'Quienes ingresen voluntariamente están sometidos a seguimiento del juez de adolescentes.')),
    ('m15_marco', 'mg_lista', 1074.8, 1091.6, lista(
        None,
        ('libro_ley', 'Causal 7 del principio de oportunidad', 1075.8),
        ('firma', 'Compromisos específicos', 1082.0),
        ('mazo', 'Audiencias de seguimiento', 1086.0))),
    ('c46_bogota', 'carton', 1097.6, 1110.0, c_ante(
        'El caso de Bogotá', 'Programa de justicia restaurativa y terapéutica',
        'De la Secretaría Distrital de Seguridad.')),
    ('m16_oferta', 'mg_lista', 1111.3, 1129.0, lista(
        None,
        ('cruz_medica', 'Consumo de sustancias', 1112.4),
        ('escudo', 'Ofensores en delitos sexuales', 1118.3),
        ('apreton', 'Justicia restaurativa en general', 1122.4))),
    ('c47_tasas', 'carton', 1129.3, 1135.3, cita('Altísimas tasas de no reincidencia.')),
    ('c49_finalidad', 'carton', 1154.5, 1168.9, c_tit(
        'La finalidad del proceso',
        'De un proceso retributivo a uno eminentemente restaurativo, donde se busca solucionar el '
        'conflicto.')),
    ('c50_complementa', 'carton', 1176.0, 1183.9, cita(
        'La justicia restaurativa complementa, mas no reemplaza, el proceso ordinario.')),
    ('c51_prueba', 'carton', 1186.0, 1198.7, c_tit(
        'El procedimiento a prueba',
        'Una condición de la causal 7 del artículo 324 del Código de Procedimiento Penal.')),
    ('c52_articulo326', 'carton', 1199.2, 1207.2, c_ante(
        'Artículo 326', 'Las condiciones a cumplir', 'Durante la suspensión del procedimiento a prueba.')),
    ('c54_literal_b', 'carton', 1222.4, 1235.2, c_ante(
        'Artículo 326, literal b', 'Participar en programas especiales de tratamiento',
        'Para superar problemas de dependencia de drogas o bebidas alcohólicas.')),
    ('c55_literal_d', 'carton', 1235.4, 1241.9, c_ante(
        'Literal d', 'Someterse a un tratamiento médico o psicológico')),
    ('c56_literal_h', 'carton', 1242.1, 1248.3, c_ante(
        'Literal h', 'Actividades a favor de la recuperación de las víctimas')),
    ('c57_literal_i', 'carton', 1248.5, 1261.0, c_ante(
        'Literal i', 'Colaboración activa y efectiva',
        'En el tratamiento para la recuperación de las víctimas, siempre y cuando medie su consentimiento.')),
    ('c58_vinculacion', 'carton', 1263.7, 1275.0, cita(
        'El artículo 326 ya permite la vinculación del ofensor a un programa de justicia restaurativa y '
        'terapéutica.')),
    ('c59_practicas', 'carton', 1275.4, 1282.4, c_tit('Prácticas restaurativas', 'Formales e informales.')),
    ('c61_programas', 'carton', 1298.0, 1306.5, c_tit(
        'Los programas de justicia restaurativa', 'Se integran por prácticas restaurativas.')),
    ('c62_cpp', 'carton', 1311.0, 1323.8, c_ante(
        'Código de Procedimiento Penal', 'Procesos en los que la víctima y el procesado participan activamente',
        'En búsqueda de un resultado restaurativo.')),
    ('c63_resultado', 'carton', 1326.8, 1341.7, c_ante(
        'Artículo 518', 'Resultado restaurativo',
        'Un acuerdo encaminado a atender las necesidades de las partes y la reintegración en la comunidad.')),
    ('c64_onu', 'carton', 1350.5, 1366.7, c_ante(
        'Organización de las Naciones Unidas', 'Manual sobre programas y prácticas restaurativas',
        'Un proceso formal que busque una salida alternativa al proceso ordinario.')),
    ('c65_que_son', 'carton', 1371.7, 1390.8, c_ante(
        '¿Qué entendemos por prácticas restaurativas?', 'Una actividad',
        'En el marco de un programa o individual y esporádica, con contenidos de reparación, '
        'responsabilización o reintegración.')),
    ('c66_formales', 'carton', 1394.6, 1402.8, c_tit(
        'Prácticas formales', 'Tienen una metodología clara en el marco de un programa claro.')),
    ('c67_ejemplo', 'carton', 1403.0, 1414.0, c_ante(
        'Por ejemplo', 'El programa de justicia restaurativa de la Secretaría Distrital de Seguridad',
        'De la Alcaldía de Bogotá.')),
    ('m17_ejemplos', 'mg_lista', 1421.3, 1435.4, lista(
        None,
        ('circulo', 'Círculos restaurativos', 1422.3),
        ('familia', 'Conferencias familiares', 1423.8),
        ('dialogo', 'Encuentros víctima-ofensor', 1425.5),
        ('apreton', 'Mediación con un facilitador', 1430.0))),
    ('c68_no_formales', 'carton', 1435.7, 1451.3, c_tit(
        'Prácticas no formales',
        'Sin una metodología concreta, pero sí buscan componentes mínimos de reparación, '
        'responsabilización o reintegración.')),
    ('c69_fiscal', 'carton', 1457.0, 1473.8, c_tit(
        'La labor del fiscal delegado',
        'Si le presentan un resultado restaurativo, le puede dar efectos jurídicos para buscar una salida '
        'alternativa al proceso.')),
    ('c71_leccion3', 'carton', 1489.2, 1499.4, c_ante(
        'Lección 3', 'El Sistema Nacional de Coordinación en materia de justicia restaurativa')),
    ('c72_decreto', 'carton', 1503.0, 1515.3, c_ante(
        'Decreto 1885 de 2015', 'Sistema Nacional de Coordinación de Responsabilidad Penal para Adolescentes',
        'La instancia nacional de coordinación.')),
    ('m18_niveles', 'mg_lista', 1516.2, 1530.0, lista(
        None,
        ('edificio', 'Nivel departamental', 1516.4),
        ('edificio', 'Nivel distrital', 1517.5),
        ('lupa_doc', 'Seguimiento y evaluación del sistema', 1522.7))),
    ('c73_articulacion', 'carton', 1537.7, 1548.2, c_tit(
        'Instancia de articulación interinstitucional',
        'Tiene a cargo la expedición de directrices generales de política pública.')),
    ('c74_nacional', 'carton', 1548.4, 1561.4, c_ante(
        'En el nivel nacional', 'Preside el ministro de Justicia y del Derecho',
        'La secretaría técnica es del Instituto Colombiano de Bienestar Familiar.')),
    ('c75_departamental', 'carton', 1562.2, 1572.5, c_ante(
        'En el nivel departamental', 'Preside el gobernador',
        'La secretaría técnica corresponde a la regional del ICBF.')),
    ('c76_funcion', 'carton', 1576.5, 1586.9, c_ante(
        'Dentro de sus funciones', 'Formular y recomendar directrices',
        'Para garantizar el óptimo funcionamiento del sistema.')),
    ('m19_directrices', 'mg_lista', 1603.2, 1612.6, lista(
        None,
        ('doc_check', 'Formulación de planes de desarrollo', 1604.2),
        ('apreton', 'Programas de justicia juvenil restaurativa', 1607.5))),
    ('c78_existen', 'carton', 1612.8, 1621.9, cita(
        'Las directrices para la formulación de programas de justicia restaurativa ya existen.')),
    ('c80_mediacion', 'carton', 1642.0, 1651.5, c_ante(
        'Lección 4: mecanismos procesales', 'La mediación como mecanismo de justicia restaurativa')),
    ('c81_manual', 'carton', 1652.3, 1667.9, c_ante(
        'Fiscalía General de la Nación (2022)', 'Manual de mediación y justicia restaurativa',
        'Contempla el trámite de la mediación del artículo 523.')),
    ('c83_paso1', 'carton', 1687.8, 1697.4, c_ante(
        'Paso 1', 'Solicitud de intención de la mediación',
        'Por iniciativa del fiscal, la víctima o el procesado.')),
    ('c84_evalua', 'carton', 1697.6, 1706.0, cita(
        'El fiscal evalúa la procedencia de la mediación y sus efectos en el proceso.')),
    ('c85_paso2', 'carton', 1707.6, 1714.5, c_ante(
        'Paso 2', 'Aceptación y remisión del caso a un centro de mediación')),
    ('c86_centros', 'carton', 1718.0, 1730.7, c_tit(
        'Centros de mediación',
        'Se podrán hacer convenios con la Fiscalía General de la Nación para su habilitación.')),
    ('c87_paso3', 'carton', 1739.9, 1753.4, c_ante(
        'Paso 3', 'Desarrollo de la mediación',
        'El centro de mediación habilitado citará a las partes y adelantará lo pertinente.')),
    ('m20_despues', 'mg_lista', 1762.5, 1780.2, lista(
        None,
        ('doc_sello', 'Un acta de mediación', 1763.5),
        ('doc_check', 'Un informe del resultado restaurativo', 1765.5),
        ('carpeta', 'Se remite al fiscal', 1770.9),
        ('balanza', 'El fiscal le otorga efectos jurídicos', 1772.5))),
    ('c88_efectos', 'carton', 1785.5, 1798.5, c_tit(
        'Los efectos jurídicos',
        'Dependen del caso, del proceso y del delito: no van a ser los mismos para todos los casos.')),
    ('c89_archivo', 'carton', 1798.9, 1809.8, c_ante(
        'Un efecto', 'Archivo de las diligencias por conciliación previa',
        'Delitos querellables: artículo 522 de la Ley 906 de 2004.')),
    ('c90_oportunidad', 'carton', 1810.0, 1822.3, c_ante(
        'Otro posible efecto', 'El principio de oportunidad',
        'En la modalidad de suspensión o renuncia: artículo 324 de la Ley 906 de 2004.')),
    ('c91_preclusion', 'carton', 1824.2, 1839.0, c_ante(
        'Un efecto también puede ser', 'Solicitar la preclusión de la acción penal',
        'Ley 2477 de 2025: extinción de la acción penal por reparación integral.')),
    ('c92_ley1826', 'carton', 1839.5, 1851.5, c_ante(
        'O conforme al', 'Artículo 24 de la Ley 1826 de 2017',
        'Para los delitos del procedimiento penal abreviado.')),
    ('m21_efectos', 'mg_lista', 1865.5, 1879.3, lista(
        None,
        ('doc_sello', 'Extinción de la acción penal', 1866.6),
        ('carpeta', 'Archivo de las diligencias', 1868.4),
        ('balanza', 'Principio de oportunidad', 1870.4),
        ('bifurcacion', 'No son aplicables en todos los casos', 1872.7))),
    ('c93_extraprocesal', 'carton', 1884.1, 1896.9, c_ante(
        'La conciliación', 'Extraprocesal',
        'Antes de la formulación de imputación: genera el archivo de las diligencias por conciliación '
        'previa.')),
    ('c94_incidente', 'carton', 1897.1, 1907.3, c_ante(
        'O puede ser', 'En el incidente de reparación integral',
        'Se busca la reparación de las consecuencias económicas del delito.')),
    ('c95_jurisprudencia', 'carton', 1911.0, 1919.2, c_ante(
        'En la jurisprudencia', 'Los programas de justicia restaurativa')),
    ('c96_auto', 'carton', 1929.6, 1937.6, c_ante(
        'Sala de Casación Penal', 'Auto AP1827-2026', 'Radicación 65824.')),
    ('c97_conflicto', 'carton', 1946.0, 1960.5, c_tit(
        'El conflicto',
        'Los programas de justicia restaurativa se estaban imponiendo como una sanción, desconociendo el '
        'principio de legalidad.')),
    ('c98_corte', 'carton', 1960.9, 1970.3, c_ante(
        'Para la Corte', 'No es una pena ni una sanción: es una medida complementaria')),
    ('c100_asistencia', 'carton', 1989.8, 2000.4, c_tit(
        'Una medida de asistencia psicosocial',
        'Dirigida al adolescente infractor en quien se detectaron factores de vulnerabilidad.')),
    ('c101_herramientas', 'carton', 2000.9, 2009.0, cita(
        'Herramientas para gestionar su comportamiento conforme a su propio bienestar.')),
]
