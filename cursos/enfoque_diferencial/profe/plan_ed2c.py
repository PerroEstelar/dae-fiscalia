# -*- coding: utf-8 -*-
"""Unidad 2, contenido: «Sujetos de especial protección constitucional» (21:40). Cuadros
14–39013: sin el silencio del arranque ni el final, cuando el profe se acerca a la cámara.

Textos de la transcripción de Scribe, sin muletillas. Lo que el profe nombra de oído va con su
forma escrita: «la C586 del 16» es la sentencia C-586 de 2016, «la Ley cinco ochenta y uno» es
la Ley 581 de 2000 y «la SU-20 de 2022» es la SU-020 de 2022."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u2_contenido', 'UNIDAD 2/CONTENIDO',
                     'Unidad 2. Sujetos de especial protección constitucional',
                     'ED - U2 - CONTENIDO', 'enfoquediferencial - U2 - CONTENIDO', 'ED2C', 14, 39013))

ITEMS = [
    ('lt01', 'lt', 0.8, 6.6, PROFE),
    ('c01_1991', 'carton', 6.8, 21.2, c_tit(
        'La Constitución de 1991',
        'Las demandas por igualdad no podían quedarse en el aire: debían tener la posibilidad de '
        'materializarse.')),
    ('c02_partidor', 'carton', 21.4, 33.4, c_tit(
        'El partidor en una carrera de caballos',
        'Crear las condiciones para que todos salgan al mismo tiempo.')),
    ('c03_falso', 'carton', 50.6, 59.3, cita(
        'Una partida en falso anula toda la prueba, para no ofrecer indebidas ventajas.')),
    ('c04_proyecto', 'carton', 60.1, 70.9, cita(
        'Lo común que nos anima: la posibilidad de desarrollar nuestro propio proyecto de vida.')),
    ('m01_factores', 'mg_lista', 87.4, 96.9, lista(
        'Factores externos',
        ('birrete', 'Educación', 90.4),
        ('cruz_medica', 'Salud', 91.7),
        ('billete', 'Recursos financieros y capital social', 92.6))),
    ('c05_salida', 'carton', 97.0, 107.0, cita(
        'Algunos tienen asegurado un puesto en la línea de salida, gracias a trayectorias familiares y '
        'relaciones sociales.')),
    ('c06_estado_social', 'carton', 107.4, 113.8, c_ante(
        'Para los que no', 'El Estado social de derecho')),
    ('c07_dignidad', 'carton', 113.9, 128.8, cita(
        'Quien no tiene las condiciones básicas mínimas para desarrollar su plan de vida ve afectado su '
        'derecho fundamental a la dignidad.')),
    ('c08_art13', 'carton', 142.2, 159.7, c_nota(
        'Artículo 13 de la Constitución',
        '«El Estado promoverá las condiciones para que la igualdad sea real y efectiva y adoptará '
        'medidas en favor de grupos discriminados o marginados».')),
    ('c09_debilidad', 'carton', 159.8, 175.5, cita(
        '«El Estado protegerá especialmente a aquellas personas que por su condición económica, física o '
        'mental, se encuentren en circunstancia de debilidad manifiesta».')),
    ('m02_c586', 'mg_lista', 187.5, 205.3, lista(
        'Sentencia C-586 de 2016',
        ('dialogo', 'Discriminados: exclusión histórica',
         190.5),
        ('balanza', 'Marginados: reparto inequitativo', 198.1))),
    ('c10_confluir', 'carton', 210.7, 227.1, c_tit(
        'Ambas categorías pueden confluir',
        'Muchas comunidades afrodescendientes han soportado discriminaciones y han sido excluidas de '
        'beneficios sociales.')),
    ('c11_pobreza', 'carton', 231.4, 238.1, c_ante(
        'Una frase inquietante', '«La pobreza es negra»')),
    ('c12_riesgo', 'carton', 241.8, 250.1, cita(
        'En ambos casos, el principio de igualdad de oportunidades está claramente en riesgo.')),
    ('c13_generaciones', 'carton', 250.2, 263.4, c_tit(
        'Diez u once generaciones',
        'Para que una familia de bajos ingresos alcance un nivel medio: cerca de trescientos años.')),
    ('c14_inequitativo', 'carton', 268.7, 277.2, cita(
        'Somos el segundo país más inequitativo de América Latina, solo superados por Brasil.')),
    ('m03_estrategias', 'mg_lista', 282.0, 291.8, lista(
        'Dos estrategias públicas',
        ('mano_corazon', 'Las acciones afirmativas', 285.0),
        ('lupa_persona', 'Los enfoques diferenciales', 286.5))),
    ('c15_afirmativas', 'carton', 291.9, 305.9, c_ante(
        'Acciones afirmativas', 'Diferencias de trato temporales y excepcionales',
        'Que propicien en poco tiempo mayores condiciones de igualdad o de equidad.')),
    ('m04_criterios', 'mg_lista', 311.7, 346.3, lista(
        'Cinco criterios',
        ('reloj', 'Transitorias y temporales', 314.7),
        ('escudo', 'Corrigen tratos discriminatorios', 332.6),
        ('doc_check', 'Autorizadas por ley o acto administrativo', 338.2))),
    ('m05_criterios', 'mg_lista', 346.4, 360.1, lista(
        None,
        ('balanza', 'En situaciones de escasez de bienes o servicios', 346.6),
        ('grupos', 'Para un grupo determinado de personas', 352.4))),
    ('c16_cargos', 'carton', 368.5, 380.4, cita(
        'En cargos de dirección, el predominio de hombres era, y probablemente sigue siendo, '
        'indiscutible.')),
    ('c17_desproporcion', 'carton', 392.5, 397.3, cita(
        'Solo podía explicarse en razón a la discriminación.')),
    ('c18_cuotas', 'carton', 397.5, 409.8, c_ante(
        'Ley 581 de 2000', 'Ley de Cuotas',
        'Al menos un 30 % de mujeres en los niveles decisorios del poder público.')),
    ('c19_excepciones', 'carton', 425.8, 434.9, c_tit(
        'Las excepciones',
        'Cargos proveídos por concurso o por elección popular.')),
    ('c20_2024', 'carton', 456.0, 469.5, c_ante(
        '2024', 'Un mínimo de cincuenta por ciento de mujeres',
        'En cargos de máximo nivel decisorio y en otros niveles decisorios.')),
    ('c21_eleccion', 'carton', 471.2, 484.7, c_tit(
        'Ley 1475 de 2011',
        'Cuotas mínimas del 30 % de uno de los géneros en la inscripción de candidatos a elección '
        'popular.')),
    ('c22_temporalidad', 'carton', 497.9, 508.9, c_tit(
        'La temporalidad',
        'La Corte estimó que estaba implícita: en algún momento debería terminar.')),
    ('m06_ejemplos', 'mg_lista', 530.4, 547.5, lista(
        'Otros ejemplos',
        ('birrete', 'Cupos especiales en universidades públicas', 533.4),
        ('reloj', 'Edad mínima para pensionarse según el género', 542.1))),
    ('c23_anecdota', 'carton', 556.7, 567.1, c_ante(
        'Una anécdota personal', 'Un instituto para personas con severas limitaciones visuales')),
    ('c24_penumbra', 'carton', 576.6, 586.5, cita(
        'La penumbra aumentaba, hasta llegar un momento en que fui incapaz de seguirla.')),
    ('c25_vulnerable', 'carton', 591.2, 596.1, cita(
        'Me sentía absolutamente vulnerable y asustado.')),
    ('c26_luz', 'carton', 605.3, 614.1, cita(
        'De golpe, alguien operó un interruptor y la luz inundó el espacio.')),
    ('c27_yo', 'carton', 638.8, 646.7, cita(
        'En un lugar como este, era yo la persona más vulnerable.')),
    ('c28_contexto', 'carton', 659.2, 673.2, c_tit(
        'Una realidad contextual',
        'Frente a determinadas situaciones, algunas personas quedan expuestas a una mayor '
        'vulnerabilidad.')),
    ('m07_imaginese', 'mg_lista', 677.1, 708.1, lista(
        'Imagínese',
        ('persona', 'En silla de ruedas por una ciudad colombiana', 677.4),
        ('ruta', 'Una adolescente sola en calles poco iluminadas', 688.4),
        ('dialogo', 'Funcionarios que hablan otro idioma', 700.6))),
    ('c29_sillas', 'carton', 721.1, 735.9, c_tit(
        'Las sillas preferenciales',
        'Adultos mayores, mujeres embarazadas, personas con discapacidad, niños de brazos y movilidad '
        'reducida.')),
    ('c30_adolescentes', 'carton', 738.5, 750.9, cita(
        'No figuran los niños, niñas y adolescentes, que en algunos escritos se consideran los más '
        'vulnerables.')),
    ('c31_enfoque', 'carton', 757.3, 769.5, c_tit(
        'El enfoque diferencial',
        'El deber del Estado de mirar y analizar la realidad desde cierta perspectiva.')),
    ('c32_medidas', 'carton', 780.7, 788.7, cita(
        'Y adelantar medidas que restablezcan condiciones de igualdad material.')),
    ('m08_parametros', 'mg_lista', 799.8, 813.8, lista(
        'Parámetros de la Corte',
        ('personas', 'Género e identidades sexuales diversas', 802.8),
        ('mundo', 'Etnia, discapacidad, edad', 806.1),
        ('casa_lote', 'Campesinado', 809.7))),
    ('m09_parametros', 'mg_lista', 813.9, 818.5, lista(
        None,
        ('escudo', 'Defensoras y defensores de derechos humanos', 813.9),
        ('mano_corazon', 'Víctimas del conflicto armado', 814.2))),
    ('c33_cruces', 'carton', 818.6, 826.9, cita(
        'Cruces con otros enfoques, como el territorial y el intercultural.')),
    ('c34_particular', 'carton', 827.6, 837.4, cita(
        'Aun cuando todas estas poblaciones son de especial protección, es necesario analizar cada caso '
        'de manera particular.')),
    ('c35_lentes', 'carton', 837.5, 851.9, c_tit(
        'Una especie de lentes',
        'Para cuando están involucrados grupos puestos en condiciones de debilidad manifiesta o de '
        'marginalidad.')),
    ('c36_interseccional', 'carton', 852.5, 864.4, c_tit(
        'Enfoques interseccionales',
        'Una misma persona puede pertenecer a varias de las categorías señaladas.')),
    ('c37_caso', 'carton', 873.4, 889.8, c_ante(
        'Un ejemplo', 'Una mujer indígena y su hija de quince años',
        'Sacadas a la fuerza de un supermercado, por la mala imagen que proyectaban a la clientela.')),
    ('c38_preguntas', 'carton', 890.1, 900.8, cita(
        '¿Qué enfoques diferenciales debe considerar? ¿Qué medidas especiales debería aplicar?')),
    ('c39_no_dicen', 'carton', 903.6, 913.9, cita(
        'Los enfoques diferenciales no nos dicen de antemano cómo resolver el caso, pero sí qué '
        'circunstancias tener en cuenta.')),
    ('m10_circunstancias', 'mg_lista', 914.0, 925.3, lista(
        None,
        ('mundo', 'La pertenencia indígena en un contexto citadino', 914.2),
        ('persona', 'Una mujer adulta', 918.9),
        ('familia', 'Una menor que a su vez es indígena', 921.0))),
    ('c40_recepcion', 'carton', 925.4, 934.1, cita(
        'Deben ser ponderadas desde el momento mismo de la recepción del caso.')),
    ('c41_revictimizante', 'carton', 937.3, 952.3, cita(
        'Solo con un contexto amplio y comprensivo se podrá dar curso a una estrategia de atención y '
        'protección que no sea revictimizante.')),
    ('c42_ajustes', 'carton', 958.1, 971.8, c_ante(
        'Discapacidad', 'Los ajustes razonables',
        'Artículo 2 de la Convención sobre los Derechos de las Personas con Discapacidad.')),
    ('c43_ciudades', 'carton', 994.1, 1006.2, cita(
        'Implicaría reconstruir gran parte de nuestras ciudades, pero tampoco nos debe llevar a la '
        'inacción.')),
    ('c44_campesinado', 'carton', 1018.4, 1032.6, c_tit(
        'El campesinado',
        'Por respeto a sus formas comunitarias de vida y por las condiciones de vulnerabilidad en que se '
        'encuentran.')),
    ('c45_acto', 'carton', 1041.5, 1052.6, c_ante(
        'Acto Legislativo 1 de 2023', '«El campesinado es sujeto de derechos y de especial protección»')),
    ('c46_tierra', 'carton', 1062.1, 1073.2, cita(
        '«Tiene un particular relacionamiento con la tierra basado en la producción de alimentos».')),
    ('c47_colectivos', 'carton', 1082.5, 1095.9, cita(
        'Da pie para desarrollar derechos especiales colectivos, como en el caso de poblaciones '
        'étnicamente diferenciadas.')),
    ('c48_actores', 'carton', 1111.8, 1123.8, c_tit(
        'Actores específicos',
        'Líderes y defensores de derechos humanos, y firmantes del Acuerdo Final de Paz.')),
    ('c49_su546', 'carton', 1129.7, 1147.9, c_ante(
        'Sentencia SU-546 de 2023', 'Un estado de cosas inconstitucional',
        'Por la violencia generalizada y sistemática contra la población líder y defensora de derechos '
        'humanos.')),
    ('c50_riesgos', 'carton', 1167.2, 1179.6, cita(
        'Enfrentan riesgos que comprometen su vida, su integridad personal y el libre ejercicio de sus '
        'labores.')),
    ('c51_seguridad', 'carton', 1206.9, 1225.4, c_ante(
        'Sentencia SU-020 de 2022', 'La seguridad humana',
        'Tomarse en serio los riesgos, estigmas y hasta humillaciones que enfrentan los firmantes, sus '
        'familias y sus territorios.')),
    ('c52_conclusion', 'carton', 1247.7, 1258.8, c_ante(
        'En conclusión',
        'Amplios sectores de la sociedad han sido históricamente discriminados, invisibilizados y '
        'marginados.')),
    ('m11_piden', 'mg_lista', 1264.2, 1284.3, lista(
        'Lo que nos piden',
        ('ojo', 'Cambiar la manera de verlos y atenderlos', 1267.2),
        ('lupa_persona', 'Ser conscientes de los prejuicios', 1270.0),
        ('dialogo', 'Una escucha atenta y empática', 1279.2))),
    ('c53_cierre', 'carton', 1284.4, 1300.1, cita(
        'Garantizar los derechos fundamentales de todas las personas, especialmente de las que han sido '
        'colocadas en situaciones de mayor fragilidad.')),
]
