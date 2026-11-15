# -*- coding: utf-8 -*-
"""Unidad 5, contenido: «El enfoque de género» (27:51). Cuadros 17–50160: sin el silencio del
arranque ni el final, cuando el profe se acerca a la cámara.

Textos de la transcripción de Scribe, sin muletillas. Lo que el profe nombra de oído va con su
forma escrita: la corporación es Sisma Mujer, el feminicidio es el artículo 104A del Código Penal
(él dice «ciento cuatro») y la ley es la 1761 de 2015."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u5_contenido', 'UNIDAD 5/CONTENIDO', 'Unidad 5. El enfoque de género',
                     'ED - U5 - CONTENIDO', 'enfoquediferencial - U5 - CONTENIDO', 'ED5C', 17, 50160))

ITEMS = [
    ('lt01', 'lt', 1.0, 7.0, PROFE),
    ('c01_recurrencia', 'carton', 7.2, 18.7, c_tit(
        'Una preocupante recurrencia',
        'Violencias contra las mujeres y personas con identidades diversas.')),
    ('m01_escenarios', 'mg_lista', 34.2, 45.8, lista(
        'Tres escenarios',
        ('escudo', 'Violencias sexuales', 37.2),
        ('casa_lote', 'Violencia intrafamiliar', 38.9),
        ('persona', 'Feminicidios', 41.1))),
    ('c02_protocolo', 'carton', 45.9, 55.6, c_ante(
        'Violencia sexual', 'Protocolo de Investigación de Violencia Sexual',
        'De la Fiscalía General de la Nación.')),
    ('m02_consulta', 'mg_lista', 67.2, 80.6, lista(
        'Un amplio proceso consultivo',
        ('grupos', 'Sisma Mujer', 70.2),
        ('mundo', 'El sistema de Naciones Unidas', 71.3),
        ('escudo', 'Defensoría y Procuraduría', 74.1))),
    ('c03_herramientas', 'carton', 100.4, 112.8, cita(
        'Con un adecuado enfoque diferencial desde el comienzo, los funcionarios profundizarán en las '
        'herramientas que la institución pone a su servicio.')),
    ('c04_definicion', 'carton', 113.2, 134.2, c_nota(
        'Protocolo de la Fiscalía',
        'Violencia sexual: todo acto que, mediante la violencia física, psíquica o moral, se ejerce sobre una '
        'persona para imponer una conducta sexual en contra de su voluntad.')),
    ('c05_contacto', 'carton', 148.6, 159.8, cita(
        'No se limita al acceso carnal: puede darse sin algún tipo de contacto físico del perpetrador.')),
    ('m03_casos', 'mg_lista', 160.0, 177.3, lista(
        'Por ejemplo',
        ('ojo', 'Acoso', 161.0),
        ('cruz_medica', 'Anticoncepción, embarazo o aborto forzados', 162.8),
        ('candado', 'Explotación o esclavitud sexual', 170.2))),
    ('m04_derechos', 'mg_lista', 185.3, 198.1, lista(
        'Derechos comprometidos',
        ('mano_corazon', 'La vida y la dignidad', 188.3),
        ('persona', 'La libertad y la integridad', 190.4),
        ('familia', 'Los derechos sexuales y reproductivos', 194.1))),
    ('c06_concurso', 'carton', 198.2, 210.6, cita(
        'Puede perpetrarse en concurso con otras conductas punibles: exige una investigación y judicialización '
        'efectiva.')),
    ('c07_universo', 'carton', 220.9, 232.8, c_tit(
        'Un universo extenso',
        'Afecta principalmente a mujeres, pero los hombres pueden ser igualmente agredidos sexualmente.')),
    ('c08_ninas', 'carton', 232.9, 241.2, cita(
        'El número de niñas y adolescentes que la sufren es alarmante.')),
    ('c09_naturaliza', 'carton', 242.7, 253.9, cita(
        'Un fenómeno tan extendido que muchas veces se naturaliza, lo que hace difícil su denuncia.')),
    ('c10_interseccionalidad', 'carton', 256.1, 272.6, c_tit(
        'Un terreno fértil para la interseccionalidad',
        'Víctimas del conflicto armado, de pueblos étnicos, mujeres cabeza de familia, lideresas desplazadas.')),
    ('c11_dominacion', 'carton', 277.4, 290.3, cita(
        'Periodistas, defensoras de derechos humanos o sindicalistas: la violencia sexual es también un acto '
        'de dominación.')),
    ('c12_degradar', 'carton', 290.4, 302.5, cita(
        'Comportamientos que buscan lesionar, degradar, humillar, ejercer presión o dominio sobre una '
        'persona.')),
    ('c13_contextos', 'carton', 315.7, 331.8, c_tit(
        'Estructuras de desigualdad',
        'Conflicto armado, delincuencia organizada, pobreza extrema, machismo o racismo: hay que caracterizar '
        'los contextos.')),
    ('c14_victima', 'carton', 353.2, 359.2, c_ante(
        'Los lineamientos del protocolo', 'Una aproximación centrada en la víctima')),
    ('m05_priorizar', 'mg_lista', 359.3, 399.1, lista(
        'Priorizar',
        ('escudo', 'Su seguridad, privacidad y bienestar', 359.9),
        ('mano_corazon', 'Sensibilidad y profesionalismo', 380.9),
        ('lupa_doc', 'Evitar la revictimización', 392.6))),
    ('m06_informar', 'mg_lista', 404.5, 425.9, lista(
        None,
        ('dialogo', 'Mantenerlas informadas', 404.8),
        ('ruta', 'Rutas de atención integral', 419.3))),
    ('c15_prejuicios', 'carton', 434.4, 446.2, cita(
        'Muchas veces, la principal barrera para el acceso a la justicia son nuestros propios prejuicios.')),
    ('m07_mitos', 'mg_lista', 461.7, 482.6, lista(
        'Seis mitos',
        ('dialogo', 'No hablan sobre sus experiencias', 464.7),
        ('persona', 'Son responsables de su victimización', 471.8),
        ('ojo', 'Mienten al denunciar', 478.5))),
    ('m08_mitos', 'mg_lista', 482.7, 502.5, lista(
        None,
        ('balanza', 'No son tan graves como otros delitos', 482.9),
        ('personas', 'Solo afecta a las mujeres', 488.8),
        ('mano_corazon', 'La discapacidad impide reconocerlos', 495.0))),
    ('c16_verdad', 'carton', 503.9, 510.6, cita(
        '¿Usted realmente cree que hay algo de verdad en ellas?')),
    ('c17_mito1', 'carton', 515.0, 521.6, c_ante(
        'Primer mito', 'No hablarán de sus experiencias')),
    ('m08b_razones', 'mg_lista', 523.5, 538.0, lista(
        'Las razones',
        ('candado', 'Temor, riesgo, privacidad', 526.4),
        ('persona', 'Pudor, honor personal o familiar', 530.7),
        ('ojo', 'Desconfianza o desconocimiento', 533.8))),
    ('c17b_presumir', 'carton', 546.5, 553.2, cita(
        'Lo que no debemos hacer es presumirlo ni anticiparlo.')),
    ('c18_relato', 'carton', 553.3, 564.9, cita(
        'Generar las condiciones para el relato, sin actitudes incriminatorias, descalificadoras o '
        'revictimizantes.')),
    ('c19_mito2', 'carton', 565.2, 574.1, c_ante(
        'Segundo mito', '¿La forma de vestir de la víctima produce la agresión?')),
    ('c20_frases', 'carton', 580.7, 590.2, cita(
        '«Tomaba demasiado». «Era una coqueta». «Si no se resistió, lo consintió».')),
    ('c21_juzgar', 'carton', 596.9, 611.6, c_tit(
        'Abstenerse de juzgar a la víctima',
        'El perpetrador, sean cuales sean las circunstancias, es el responsable de su propia conducta.')),
    ('c22_no_responsables', 'carton', 630.8, 641.1, cita(
        'Ayudar a las víctimas a entender que no son responsables de lo que les aconteció.')),
    ('c23_mito3', 'carton', 643.3, 650.9, c_ante(
        'Tercer mito', 'Las víctimas siempre mienten al denunciar')),
    ('c24_ciertas', 'carton', 668.3, 676.2, c_tit(
        'La gran mayoría de denuncias son ciertas',
        'Y existe un gran subregistro de ellas.')),
    ('c25_credibilidad', 'carton', 692.4, 705.1, cita(
        'Las dudas sobre la credibilidad de la víctima no pueden justificar sesgos en la recepción de la '
        'denuncia.')),
    ('c26_mito4', 'carton', 715.6, 722.9, c_ante(
        'Cuarto mito', 'Los delitos sexuales no son tan graves')),
    ('c27_graves', 'carton', 742.1, 755.0, cita(
        'Son tan graves como otros delitos: atentan contra la integridad personal, la libertad o la formación '
        'sexual.')),
    ('c28_trascienden', 'carton', 755.2, 767.2, cita(
        'Sus consecuencias trascienden lo privado y permean todos los ámbitos relacionales de las víctimas.')),
    ('c29_mito5', 'carton', 777.7, 791.0, c_ante(
        'Quinto mito', 'Solo afecta a las mujeres',
        'Un estereotipo: que los hombres no pueden ser víctimas gracias a su fuerza.')),
    ('c29b_control', 'carton', 803.2, 813.4, cita(
        'Una idea más profunda: que los hombres deben y pueden estar en control de sí mismos y de sus '
        'emociones.')),
    ('c30_denunciar', 'carton', 813.5, 825.3, cita(
        'A los niños y hombres les queda difícil denunciar: se teme que el relato ponga en duda su hombría.')),
    ('c31_mujeres', 'carton', 837.4, 848.6, cita(
        'Algunas mujeres pueden cometer estos delitos: madres, tías, profesoras, jefas, terapeutas.')),
    ('c32_devastadora', 'carton', 865.7, 877.6, cita(
        'La experiencia de ser víctima, más allá de su género, es devastadora y extremadamente traumática.')),
    ('c33_mito6', 'carton', 899.0, 909.0, c_ante(
        'Sexto mito', 'Las personas con discapacidad no reconocen ni denuncian estos delitos')),
    ('c34_cuidadosos', 'carton', 913.4, 926.0, cita(
        'Las dudas deben llevar a los funcionarios a ser aún más cuidadosos, dada su condición de '
        'vulnerabilidad.')),
    ('c35_lineamientos', 'carton', 935.6, 946.6, cita(
        'Algunos lineamientos iniciales pueden determinar el éxito posterior de la investigación.')),
    ('m09_registro', 'mg_lista', 959.1, 976.4, lista(
        'La noticia criminal',
        ('persona', 'Caracterización completa de la víctima', 962.1),
        ('dialogo', 'Relato completo de los hechos y su contexto', 965.8),
        ('libro_ley', 'Selección provisional del tipo penal', 972.5))),
    ('c36_denuncia', 'carton', 977.2, 993.0, c_ante(
        'En segundo lugar', 'La denuncia de la víctima',
        'Podría ser la única testigo: del trato que reciba puede depender su participación en el proceso.')),
    ('m10_condiciones', 'mg_lista', 998.8, 1015.6, lista(
        'Condiciones',
        ('candado', 'Privacidad y seguridad', 1002.0),
        ('mano_corazon', 'Accesibilidad y comodidad', 1005.2),
        ('escudo', 'Lejos del presunto agresor', 1009.0))),
    ('c37_informacion', 'carton', 1022.2, 1034.8, cita(
        'Información adecuada sobre sus derechos, las características del proceso y los medios de atención '
        'integral.')),
    ('c38_minimizar', 'carton', 1035.1, 1045.7, cita(
        'Evitar comentarios que minimicen lo ocurrido, y no prometer un resultado específico.')),
    ('c39_lgbti', 'carton', 1065.1, 1080.7, c_tit(
        'Orientación sexual e identidad',
        'Respetarlas, no usar lenguaje discriminatorio y tener en cuenta el prejuicio contra la población '
        'LGBTIQ+.')),
    ('c40_trans', 'carton', 1087.5, 1099.0, cita(
        'A una persona trans se le llama por su nombre identitario, independientemente de su documento.')),
    ('c41_prejuicio', 'carton', 1112.0, 1122.2, c_tit(
        'Violencia basada en prejuicios',
        'Afecta preponderantemente a la población LGBTIQ+.')),
    ('c41b_diferencia', 'carton', 1124.0, 1131.1, cita(
        'Las prácticas de discriminación y exclusión marcan una diferencia con el otro.')),
    ('c41c_inferior', 'carton', 1131.2, 1141.6, cita(
        'Busca mostrar al otro como inferior, darle un lugar de subordinación, o suprimirlo.')),
    ('c42_otras', 'carton', 1158.5, 1166.9, c_tit(
        'Otras violencias',
        'El feminicidio y la violencia intrafamiliar.')),
    ('c43_feminicidio', 'carton', 1175.5, 1184.3, cita(
        'Dos situaciones diferentes, pero que pueden estar interconectadas.')),
    ('c44_art229', 'carton', 1199.7, 1214.2, c_ante(
        'Código Penal, artículo 229', 'Violencia intrafamiliar',
        'El maltrato físico o psicológico a cualquier miembro del núcleo familiar.')),
    ('c45_art104a', 'carton', 1229.5, 1245.4, c_ante(
        'Código Penal, artículo 104A', 'Feminicidio',
        'Causar la muerte a una mujer por su condición de ser mujer o por motivos de su identidad de género.')),
    ('m11_circunstancias', 'mg_lista', 1249.2, 1291.4, lista(
        'Circunstancias',
        ('familia', 'Una relación familiar, íntima o de convivencia', 1249.5),
        ('persona', 'Instrumentalización de género', 1270.5),
        ('balanza', 'Aprovechar relaciones de poder', 1284.4))),
    ('m12_circunstancias', 'mg_lista', 1298.9, 1337.7, lista(
        None,
        ('escudo', 'Generar terror o humillación', 1299.2),
        ('lupa_doc', 'Antecedentes de violencia o amenaza', 1305.2),
        ('candado', 'Incomunicación o privación de la libertad', 1329.6))),
    ('c46_ley1761', 'carton', 1337.8, 1344.2, c_ante(
        'Ley 1761 de 2015', 'Ley Rosa Elvira Cely')),
    ('c47_estereotipos', 'carton', 1346.3, 1359.1, c_tit(
        'Los estereotipos de género',
        'Tienden a determinar lo que debe ser una mujer o un hombre en ciertos contextos.')),
    ('c48_debiles', 'carton', 1359.3, 1372.9, cita(
        'Mujeres débiles, cuidadoras, serviles y sentimentales; hombres racionales, independientes, fuertes, '
        'con el control.')),
    ('c49_privado', 'carton', 1384.7, 1394.1, cita(
        '«La violencia de pareja es un asunto privado en el que no debo meterme».')),
    ('c50_calladita', 'carton', 1410.5, 1421.8, cita(
        'Que mantengan la unidad de la familia, sumisas y silenciosas: «Calladita se ve más bonita».')),
    ('c51_responsabilidad', 'carton', 1430.4, 1442.6, c_tit(
        'Disminuir la responsabilidad del agresor',
        '«Ella provoca la agresión». «Los celos son sinónimo de amor».')),
    ('c52_vigilarlas', 'carton', 1456.5, 1469.7, cita(
        'Que a las mujeres jóvenes hay que vigilarlas: sus relaciones, sus llamadas, sus amistades, sus redes '
        'sociales.')),
    ('c53_diversas', 'carton', 1492.6, 1504.8, cita(
        'En la violencia intrafamiliar, las identidades diversas se patologizan o se asumen como '
        'contagiosas.')),
    ('c54_terapias', 'carton', 1521.7, 1532.3, cita(
        'Las terapias de corrección no consentidas, orientadas a suprimir o castigar estas expresiones.')),
    ('c55_hipotesis', 'carton', 1532.4, 1547.1, c_tit(
        'Desde el inicio de la investigación',
        'Partir de la hipótesis de que se trató de la consumación o la tentativa de un feminicidio.')),
    ('c56_trans', 'carton', 1551.4, 1559.4, cita(
        'Una mujer trans también puede ser víctima de feminicidio.')),
    ('c57_opresion', 'carton', 1560.8, 1572.9, cita(
        'En la violencia intrafamiliar, observar las relaciones de opresión, subordinación y discriminación.')),
    ('c58_contexto', 'carton', 1574.1, 1586.3, c_tit(
        'El contexto es fundamental',
        'Para comprender los móviles, las formas de maltrato y su dinámica cíclica.')),
    ('c58b_retractacion', 'carton', 1591.4, 1604.8, cita(
        'Permite explicar la retractación, la defensa del agresor por parte de la víctima o la reanudación de '
        'la relación.')),
    ('c59_lgbti', 'carton', 1611.8, 1626.7, cita(
        'Si la víctima es o se percibe LGBTIQ+, la primera hipótesis es que el delito fue cometido en razón a '
        'su orientación o identidad.')),
    ('c60_conclusion', 'carton', 1645.6, 1653.2, c_ante(
        'En conclusión', 'La importancia del análisis de contexto')),
    ('c61_patrones', 'carton', 1653.9, 1667.5, cita(
        'Abundan las violencias basadas en prejuicios y se multiplican patrones asociados, por ejemplo, al '
        'conflicto armado.')),
]
