# -*- coding: utf-8 -*-
"""Unidad 4, contenido: «Etnicidad» (25:50). Cuadros 54–46519: sin el silencio del arranque ni
el final, cuando el profe se acerca a la cámara.

Textos de la transcripción de Scribe, sin muletillas. Las sentencias van con su forma escrita
(«la T254 del 94» es la T-254 de 1994)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u4_contenido', 'UNIDAD 4/CONTENIDO', 'Unidad 4. Etnicidad',
                     'ED - U4 - CONTENIDO', 'enfoquediferencial - U4 - CONTENIDO', 'ED4C', 54, 46519))

# «Rrom» (24 nov 2026): revisión de la Fiscalía (Tatiana López), «la forma correcta de escribir es Rrom» (grafía del
# Decreto 2957 de 2010). El cartón corregido se rinde como «… v2.mov» y la entrega es la v3 (`reparchar.py`).
VERSION = 3
VERSIONES = {'c16_afro_rom': 2}

ITEMS = [
    ('lt01', 'lt', 2.2, 8.2, PROFE),
    ('c01_jei', 'carton', 8.4, 19.9, c_tit(
        'Una unidad sobre los casos étnicos',
        'La confluencia entre las acciones de la Fiscalía y las de la Jurisdicción Especial Indígena.')),
    ('m01_personas', 'mg_lista', 24.5, 41.8, lista(
        'Personas que',
        ('lupa_persona', 'Se reconocen como étnicamente diversas', 27.5),
        ('mano_corazon', 'Solicitan una atención preferencial', 30.7),
        ('escudo', 'Invocan el derecho propio o el fuero', 34.2))),
    ('c02_herramientas', 'carton', 43.6, 56.7, cita(
        'Herramientas generales para una atención más oportuna y orientada por parte de los servidores de la '
        'Fiscalía.')),
    ('c03_pregunta', 'carton', 63.5, 75.6, c_ante(
        'Una primera pregunta',
        '¿Estamos habilitados para determinar quiénes son indígenas o afrodescendientes?')),
    ('c04_casos_dificiles', 'carton', 78.5, 86.0, cita(
        '¿A quiénes corresponde precisar tal carácter frente a casos difíciles?')),
    ('c05_estereotipos', 'carton', 98.0, 111.5, cita(
        'Podemos aferrarnos a visiones estereotipadas: atribuir una identidad étnica a la vestimenta o al '
        'color de la piel.')),
    ('m02_t576', 'mg_lista', 122.5, 138.3, lista(
        'Sentencia T-576 de 2014',
        ('personas', 'Ni la raza', 125.5),
        ('mapa', 'Ni el territorio que habita', 126.9),
        ('doc_sello', 'Ni el reconocimiento formal del Estado', 130.5))),
    ('c06_t376', 'carton', 143.3, 151.3, c_ante(
        'Sentencia T-376 de 2012', 'La confluencia de varios factores')),
    ('c07_hechos', 'carton', 155.9, 170.1, cita(
        'La existencia de una comunidad no depende de un acto de las autoridades, sino de la diversidad '
        'cultural y el autorreconocimiento del grupo.')),
    ('c08_oficial', 'carton', 170.2, 183.9, cita(
        'El reconocimiento oficial facilita la prueba de la existencia de la comunidad y el acceso a los '
        'servicios del Estado.')),
    ('c09_idea', 'carton', 187.6, 199.8, c_ante(
        'Primera idea fuerza', 'Dar pie a los enfoques diferenciales',
        'Independientemente de su percepción inicial.')),
    ('c10_precisar', 'carton', 204.3, 213.1, cita(
        'En el curso de los procesos habrá tiempo de precisar tal carácter.')),
    ('c11_derecho_propio', 'carton', 215.1, 231.7, c_tit(
        'El derecho propio',
        'Resolver los conflictos al interior de sus comunidades, de acuerdo con sus propios usos, costumbres, '
        'procedimientos y sanciones.')),
    ('c12_art246', 'carton', 239.0, 255.7, c_nota(
        'Artículo 246 de la Constitución',
        'Las autoridades de los pueblos indígenas podrán ejercer funciones jurisdiccionales dentro de su '
        'ámbito territorial.')),
    ('c13_coordinacion', 'carton', 265.6, 273.1, cita(
        'La ley establecerá la coordinación con el sistema judicial nacional.')),
    ('c14_art8', 'carton', 274.0, 291.4, c_ante(
        'Convenio 169 de la OIT', 'Artículo 8.2',
        'El derecho de conservar sus costumbres e instituciones propias, si no son incompatibles con los '
        'derechos fundamentales.')),
    ('c14b_procedimientos', 'carton', 301.1, 313.0, cita(
        'Los gobiernos deberán establecer procedimientos para solucionar los conflictos que puedan surgir.')),
    ('c15_art9', 'carton', 313.3, 327.6, c_nota(
        'Artículo 9',
        'Deberán respetarse los métodos a los que los pueblos recurren tradicionalmente para la represión de '
        'los delitos.')),
    ('c16_afro_rom', 'carton', 337.0, 350.8, cita(
        'Las comunidades afrodescendientes y el pueblo Rrom esperan un reconocimiento pleno de su forma de '
        'tramitar conflictos.')),
    ('c17_t254', 'carton', 369.5, 381.8, c_ante(
        'Sentencia T-254 de 1994', 'La autonomía jurisdiccional',
        'No estaba condicionada a la expedición de una ley.')),
    ('c18_t617', 'carton', 385.1, 394.1, c_ante(
        'Sentencia T-617 de 2010', 'Un derecho colectivo de carácter fundamental')),
    ('c19_reconocimiento', 'carton', 397.0, 410.0, c_tit(
        'La tesis del reconocimiento',
        '¿Sobre cuáles comportamientos tiene competencia la jurisdicción especial indígena?')),
    ('c20_colisiones', 'carton', 424.9, 436.7, cita(
        'La Corte ha ido acotando el debido proceso en esta jurisdicción y las colisiones de competencia.')),
    ('c20b_limite', 'carton', 450.4, 456.9, cita(
        'El debido proceso como límite.')),
    ('c21_t514', 'carton', 458.8, 467.7, c_ante(
        'Sentencia T-514 de 2009', 'Tres reglas de interpretación y sus límites')),
    ('c22_maximizar', 'carton', 482.6, 496.7, c_ante(
        'Primer principio', 'Maximizar la autonomía',
        'Las restricciones solo son admisibles cuando sean necesarias y las menos gravosas.')),
    ('c23_internos', 'carton', 516.6, 531.1, c_ante(
        'Segundo principio', 'Mayor autonomía en los conflictos internos',
        'Entre dos culturas, deben armonizarse sus principios esenciales.')),
    ('c24_conservacion', 'carton', 546.5, 556.5, c_ante(
        'Tercer principio', 'A mayor conservación de la identidad cultural, mayor autonomía')),
    ('c25_descriptivo', 'carton', 567.5, 574.0, cita(
        'Un valor más descriptivo que normativo.')),
    ('c25b_integrados', 'carton', 579.4, 592.5, cita(
        'Los grupos más integrados a la cultura occidental tendrían el deber de regirse por las leyes de la '
        'República.')),
    ('c26_limites', 'carton', 597.3, 610.9, c_tit(
        'Los límites',
        'Solo lo verdaderamente intolerable: el respeto a la vida, la prohibición de la tortura y la '
        'esclavitud.')),
    ('c27_previsibilidad', 'carton', 627.1, 636.3, cita(
        'Legalidad y debido proceso: la previsibilidad de las actuaciones de las autoridades tradicionales.')),
    ('c28_petrificar', 'carton', 636.4, 647.0, cita(
        'Lo que no implica petrificar las instituciones y prácticas sociales de la comunidad.')),
    ('c28b_segunda', 'carton', 650.8, 663.3, c_tit(
        'Una segunda limitación',
        'Los derechos fundamentales, mínimos de la convivencia social, protegidos de la arbitrariedad.')),
    ('c29_nucleo', 'carton', 678.0, 689.9, c_tit(
        'Un núcleo duro',
        'Una decisión que desconozca la vida, la integridad o las prohibiciones de tortura y servidumbre está '
        'prohibida.')),
    ('c30_cultura', 'carton', 690.0, 701.6, cita(
        'La evaluación debe realizarse a la luz de la cultura específica en que se presenten los hechos.')),
    ('c31_segundo', 'carton', 705.0, 719.3, c_tit(
        'Un segundo círculo',
        'Los demás derechos fundamentales: prima facie, la autonomía y la diversidad cultural tienen mayor '
        'peso.')),
    ('c32_dialogo', 'carton', 729.5, 742.7, cita(
        'Propiciar el diálogo interno, para que el conflicto se solucione en el marco de la cosmovisión de la '
        'comunidad.')),
    ('m03_casos', 'mg_lista', 754.1, 763.9, lista(
        'Casos concretos',
        ('grupos', 'Penas colectivas', 757.1),
        ('mazo', 'Castigos corporales', 758.6),
        ('ruta', 'Expulsión del territorio', 760.0))),
    ('c33_fuero', 'carton', 764.0, 779.0, c_ante(
        'El fuero indígena', 'Un derecho individual, no colectivo',
        'Ser juzgados por sus autoridades, de acuerdo con sus normas y procedimientos.')),
    ('m04_t617', 'mg_lista', 801.4, 824.0, lista(
        'Sentencia T-617 de 2010',
        ('mapa', 'Territorial y personal', 804.4),
        ('mano_corazon', 'Protege la conciencia étnica', 808.0),
        ('escudo', 'Una garantía colectiva', 817.8))),
    ('c34_interdependencia', 'carton', 831.9, 843.4, cita(
        'Una interdependencia entre el fuero individual y la jurisdicción especial indígena colectiva.')),
    ('c35_no_procede', 'carton', 849.6, 862.1, cita(
        'Si la comunidad no ejerce jurisdicción ni tiene la institucionalidad para ello, no procedería el '
        'fuero.')),
    ('c36_juez_natural', 'carton', 867.3, 881.3, cita(
        'Si en un caso similar la comunidad sí adelantó un juicio, por vía de igualdad podría invocar su '
        'derecho a juez natural.')),
    ('c37_2021', 'carton', 891.5, 900.7, c_ante(
        'Desde 2021', 'La Corte Constitucional define las colisiones de competencia')),
    ('c38_t349', 'carton', 901.8, 916.7, cita(
        'Antes las definía la Sala Disciplinaria del Consejo Superior de la Judicatura, con reglas que inició '
        'la sentencia T-349 de 1996.')),
    ('m05_criterios', 'mg_lista', 925.5, 938.2, lista(
        'Cuatro criterios',
        ('persona', 'Personal', 928.5),
        ('mapa', 'Territorial', 929.7),
        ('edificio', 'Institucional', 930.6),
        ('balanza', 'Objetivo', 932.2))),
    ('c39_personal', 'carton', 944.7, 953.8, c_ante(
        'Elemento personal', 'La pertenencia del acusado a una comunidad indígena')),
    ('c40_dentro', 'carton', 955.7, 967.5, cita(
        'Si los hechos ocurrieron en el territorio de su comunidad, sus autoridades tradicionales tendrán '
        'competencia.')),
    ('m06_fuera', 'mg_lista', 977.3, 1004.6, lista(
        'Fuera del territorio',
        ('ojo', 'No lo comprendía como ilícito: absolver', 980.3),
        ('mundo', 'Condicionada por su cultura: al resguardo', 985.3),
        ('mazo', 'Aculturación: jurisdicción ordinaria', 997.0))),
    ('c41_territorial', 'carton', 1016.4, 1026.4, c_ante(
        'Elemento territorial', 'Los hechos ocurrieron dentro del territorio del resguardo')),
    ('c42_desplazamiento', 'carton', 1030.8, 1043.1, cita(
        'Pocas excepciones: comunidades víctimas de desplazamiento forzado, reubicadas o en proceso de '
        'retorno.')),
    ('c43_territorio', 'carton', 1051.5, 1062.3, c_tit(
        'El territorio',
        'Más que un ámbito geográfico: el ámbito donde se desenvuelve su cultura.')),
    ('c44_expansivo', 'carton', 1069.9, 1085.8, c_tit(
        'Un efecto expansivo',
        'Un hecho por fuera de los linderos, pero remitido al espacio vital de la comunidad, puede juzgarse '
        'por sus autoridades.')),
    ('c45_institucional', 'carton', 1099.7, 1110.1, c_ante(
        'Elemento institucional', 'Autoridades, usos, costumbres y procedimientos tradicionales')),
    ('c45b_coercion', 'carton', 1115.0, 1124.2, cita(
        'Cierto poder de coerción social y un concepto genérico de nocividad social.')),
    ('m07_sub', 'mg_lista', 1136.5, 1167.0, lista(
        'Subreglas',
        ('escudo', 'Que asegure los derechos de las víctimas', 1136.8),
        ('dialogo', 'Voluntad de adelantar el proceso', 1147.8),
        ('lupa_doc', 'Control judicial posterior', 1160.4))),
    ('m08_sub', 'mg_lista', 1182.6, 1221.8, lista(
        None,
        ('mano_corazon', 'Una jurisdicción voluntaria u optativa', 1182.9),
        ('balanza', 'No renunciar a casos similares sin una razón legítima', 1195.5),
        ('reloj', 'Debido proceso como previsibilidad', 1214.4))),
    ('c46_escritas', 'carton', 1233.0, 1245.0, cita(
        'No puede exigirse que acredite normas escritas: se exige un concepto genérico de nocividad social.')),
    ('c47_objetivo', 'carton', 1249.9, 1258.0, c_ante(
        'Elemento objetivo', 'La naturaleza del bien jurídico tutelado')),
    ('m09_objetivo', 'mg_lista', 1269.7, 1307.4, lista(
        None,
        ('mundo', 'Bien de la comunidad: jurisdicción indígena',
         1270.7),
        ('edificio', 'Bien de la cultura mayoritaria: ordinaria',
         1285.5),
        ('balanza', 'Bien de ambas: sin solución específica', 1299.6))),
    ('c48_nocividad', 'carton', 1320.1, 1332.4, cita(
        'Una conducta de especial nocividad no lleva en todo caso a excluir la jurisdicción especial indígena.')),
    ('c48b_impunidad', 'carton', 1335.4, 1347.6, cita(
        'El juez debe asegurarse de que la remisión no derive en impunidad o en desprotección para la '
        'víctima.')),
    ('c49_consenso', 'carton', 1360.0, 1371.3, c_tit(
        'Sin consenso',
        'La competencia indígena cuando el victimario es alguien externo a la comunidad.')),
    ('c50_t208', 'carton', 1388.0, 1402.5, c_ante(
        'Sentencia T-208 de 2019', 'Criterios que no deben ser concurrentes',
        'Deben ser ponderados y evaluados razonablemente en cada caso.')),
    ('c50b_factores', 'carton', 1409.7, 1422.0, cita(
        'El incumplimiento de uno de los factores no lleva inmediatamente el caso a la jurisdicción ordinaria.')),
    ('c51_no_indigena', 'carton', 1435.6, 1447.9, cita(
        'Si el procesado no es indígena, no hay fuero a su favor: su juez natural es la jurisdicción '
        'ordinaria.')),
    ('c52_sp9243', 'carton', 1461.0, 1478.3, c_ante(
        'Corte Suprema de Justicia, SP9243 de 2017', 'Reconocer el pluralismo jurídico',
        'Si se dan los otros factores, la competencia sería de la jurisdicción indígena.')),
    ('c53_enfoque', 'carton', 1495.2, 1508.7, c_tit(
        'El enfoque étnico',
        'Se entrecruza con derechos fundamentales individuales y colectivos de las comunidades indígenas.')),
    ('c54_directiva', 'carton', 1515.4, 1525.8, c_nota(
        'Directiva 012',
        'La Fiscalía puede provocar o ser parte de estos conflictos interjurisdiccionales.')),
    ('c55_final', 'carton', 1525.9, 1538.8, cita(
        'Un cuidadoso enfoque diferencial étnico desde los primeros momentos, que evite retroprocesos y no '
        'revictimice.')),
]
