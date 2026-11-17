# -*- coding: utf-8 -*-
"""Unidad 3, contenido: «Enfoques diferenciales y derechos especiales» (26:14). Cuadros
18–47240: sin el silencio del arranque ni el final, cuando el profe se acerca a la cámara.

Textos de la transcripción de Scribe, sin muletillas. Tres cosas que el profe dice y el cartón
no repite: cita como «artículo 49» el que enumera los derechos de los niños (es el 44), así que
el cartón dice «La Constitución»; la Ley 70 es de 1993 (él dice 1992) y va sin año; y la
sentencia «T302 de 2025» va sin número, como «una sentencia reciente»."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u3_contenido', 'UNIDAD 3/CONTENIDO',
                     'Unidad 3. Enfoques diferenciales y derechos especiales',
                     'ED - U3 - CONTENIDO', 'enfoquediferencial - U3 - CONTENIDO', 'ED3C', 18, 47240))

# Revisión de textos del 17 nov 2026 (Sebastián: «en vez de "unas lentes" que diga "unos lentes"…
# revisa los guiones antes de entregar el paquete entero»). El profe dice «dársele… a los niños, niñas y adolescentes»; en pantalla concuerda: «dárseles».
# Los cartones corregidos se rinden como «… v2.mov» y la entrega es la v3 (`reparchar.py`).
VERSION = 3
VERSIONES = {'c48_frontera': 2}

ITEMS = [
    ('lt01', 'lt', 1.0, 7.0, PROFE),
    ('c01_moneda', 'carton', 7.2, 20.8, c_tit(
        'Dos caras de la misma moneda',
        'Lo corriente es que los labrados sean diferentes, aun cuando conformen una misma pieza.')),
    ('c02_complementariedad', 'carton', 26.8, 33.8, cita(
        'Existe un grado de complementariedad entre ambas.')),
    ('m01_caras', 'mg_lista', 39.8, 57.5, lista(
        'Dos caras',
        ('lupa_persona', 'Las estrategias del Estado', 40.1),
        ('personas', 'Los sujetos y sus derechos', 50.9))),
    ('m01b_variedad', 'mg_lista', 76.1, 92.1, lista(
        'Ya hemos visto',
        ('personas', 'Género e identidad sexual', 79.1),
        ('mundo', 'Etnia, edad, discapacidad', 81.6),
        ('casa_lote', 'Campesinos, líderes y reincorporados', 86.6))),
    ('c03_cruces', 'carton', 92.2, 100.8, cita(
        'Los cruces que pueden existir cuando una misma persona lleva en sí varias de estas condiciones.')),
    ('m02_tres', 'mg_lista', 119.3, 140.8, lista(
        'Tres poblaciones',
        ('mundo', 'La pertenencia étnica', 122.3),
        ('familia', 'Niños, niñas y adolescentes', 130.7),
        ('persona', 'Las mujeres', 135.6))),
    ('c04_indigenas', 'carton', 140.9, 152.4, c_ante(
        'Comunidades indígenas', 'Más de cien pueblos ancestrales',
        'Muchos mantienen su lengua, sus tradiciones e instituciones propias.')),
    ('c05_raices', 'carton', 154.3, 165.8, cita(
        'Otros intentan regresar a sus raíces y afirmar su ancestralidad como forma de vida colectiva.')),
    ('m03_piden', 'mg_lista', 169.2, 184.3, lista(
        'Piden',
        ('edificio', 'Autogobierno', 172.2),
        ('mapa', 'Reconocimiento territorial', 173.6),
        ('libros', 'Autonomía en educación, salud y control social', 175.7))),
    ('c06_plus', 'carton', 192.7, 200.8, cita(
        '¿Todas estas demandas no contienen un plus de derechos que quiebran la igualdad de trato?')),
    ('c07_afirmativas', 'carton', 201.2, 215.3, cita(
        'Responder que fueron discriminados o excluidos históricamente nos lleva de nuevo al terreno de '
        'las acciones afirmativas.')),
    ('c08_corrientes', 'carton', 226.9, 236.5, c_tit(
        'Dos corrientes de pensamiento',
        'El multiculturalismo y la interculturalidad.')),
    ('c09_neutral', 'carton', 239.6, 254.1, c_tit(
        'Un Estado neutral',
        'No tomar partido por una cultura, pero sí garantizar que los individuos puedan desarrollar la '
        'que quieran.')),
    ('c09b_pervivencia', 'carton', 261.5, 272.4, cita(
        'La pervivencia cultural o religiosa recae en los propios interesados, no en el Estado.')),
    ('c10_regla', 'carton', 275.8, 282.2, cita(
        '¿Le suena como regla? ¿Piensa que deberíamos aplicarlo en nuestra democracia?')),
    ('m04_errores', 'mg_lista', 290.9, 307.9, lista(
        'Dos errores básicos',
        ('balanza', 'Creer que el Estado liberal puede ser neutral', 293.9),
        ('personas', 'Creer que las diferencias caben en los derechos generales', 299.2))),
    ('c11_mayoritaria', 'carton', 311.2, 319.6, cita(
        'Los Estados siempre optan en materia institucional por la cultura mayoritaria o hegemónica.')),
    ('m05_oficinas', 'mg_lista', 322.8, 343.1, lista(
        'En las oficinas del Estado',
        ('dialogo', 'Se atiende en español', 325.8),
        ('reloj', 'De ocho a seis, con pausa para el almuerzo', 330.0),
        ('libros', 'Libros, códigos y autores europeos', 339.0))),
    ('c12_acceso', 'carton', 350.8, 365.7, cita(
        '¿Ese entramado cultural de raíces católicas y occidentales le permite a la persona indígena un '
        'acceso similar a bienes y servicios?')),
    ('c13_deuda', 'carton', 381.1, 392.8, c_tit(
        'Una deuda de igualdad',
        'El Estado no es neutral: opta de entrada por la protección de una cultura.')),
    ('c14_universo', 'carton', 400.6, 413.3, cita(
        'La igualdad tendría que operar en conexión con el universo cultural en que se desenvuelve cada '
        'individuo.')),
    ('c15_comunidad', 'carton', 417.1, 430.5, cita(
        'Si pertenezco a una comunidad indígena, es al interior de ella que puedo construir y evaluar mi '
        'proyecto de vida.')),
    ('m06_triada', 'mg_lista', 438.2, 448.0, lista(
        'La tríada básica',
        ('balanza', 'Igualdad', 441.2),
        ('ruta', 'Libertad', 442.1),
        ('mano_corazon', 'Dignidad', 442.9))),
    ('c16_preguntas', 'carton', 451.7, 458.4, cita(
        '¿Cuáles serían sus fortalezas y debilidades?')),
    ('c17_virtudes', 'carton', 459.5, 471.6, c_tit(
        'Sus virtudes',
        'Reconoce la diversidad, proyectada hacia las generaciones futuras y sus formas de vida.')),
    ('c18_defecto', 'carton', 477.0, 485.8, c_tit(
        'Su principal defecto',
        'Es una teoría de corrección del liberalismo.')),
    ('c19_prevalecen', 'carton', 494.8, 505.8, cita(
        'En un conflicto entre derechos individuales y colectivos, deben prevalecer los primeros.')),
    ('c20_horizontal', 'carton', 524.2, 533.5, c_ante(
        'La interculturalidad', 'Cada cultura vista y respetada de forma horizontal')),
    ('c21_coexistencia', 'carton', 538.4, 547.6, cita(
        'El quid es precisamente la coexistencia entre esas visiones distintas.')),
    ('c22_construccion', 'carton', 554.9, 569.5, cita(
        'Los derechos humanos no son ni universales ni inherentes per se a toda la humanidad: son una '
        'construcción occidental colonial.')),
    ('c23_dialogo', 'carton', 575.5, 589.7, c_tit(
        'Un diálogo intercultural',
        'La igualdad o la dignidad tienen diferentes acepciones según el universo cultural desde el que se '
        'postulen.')),
    ('c24_sin_prevalencia', 'carton', 598.7, 613.1, cita(
        'Un diálogo constructivo y horizontal con las comunidades, sin postular de entrada la prevalencia de '
        'un sistema determinado.')),
    ('c25_art7', 'carton', 634.8, 648.5, c_nota(
        'Artículo 7 de la Constitución',
        'El Estado reconoce y protege la diversidad étnica y cultural de la nación colombiana.')),
    ('c26_169', 'carton', 662.6, 670.1, c_ante(
        'Bloque de constitucionalidad', 'Convenio 169 de la OIT')),
    ('c27_declaracion', 'carton', 683.4, 708.8, c_ante(
        'Naciones Unidas, 2007', 'Declaración sobre los Derechos de los Pueblos Indígenas',
        'Un referente interpretativo en casos de controversia.')),
    ('m07_colectivos', 'mg_lista', 720.5, 735.5, lista(
        'Derechos colectivos',
        ('escudo', 'Sobrevivencia', 723.5),
        ('dialogo', 'Consulta previa y participación', 725.1),
        ('mapa', 'Autogobierno y territorialidad', 728.5))),
    ('c28_afro', 'carton', 739.2, 746.8, c_ante(
        'Comunidades afrodescendientes', '¿Es la misma situación?')),
    ('c29_asambleistas', 'carton', 759.0, 772.7, cita(
        'Los asambleístas de 1991 tenían en mente un modelo de diversidad étnica mucho más centrado en los '
        'pueblos indígenas.')),
    ('c30_mencionados', 'carton', 773.0, 784.8, cita(
        'Las demandas de los pueblos afrodescendientes y raizales quedaron, si acaso, apenas mencionadas.')),
    ('c31_ley70', 'carton', 790.8, 805.8, c_ante(
        'Artículo 55 transitorio', 'La Ley 70',
        'Considerada por algunos como el estatuto básico de protección de comunidades negras en Colombia.')),
    ('c32_polemica', 'carton', 820.0, 833.4, cita(
        'Una profunda polémica: a quiénes se consideraba afrodescendientes y cuáles derechos especiales '
        'les correspondían.')),
    ('c33_igualdad', 'carton', 842.8, 855.5, cita(
        'Formas de igualdad de trato entre las poblaciones afrocolombianas, y entre estas y los pueblos '
        'indígenas.')),
    ('c34_tribales', 'carton', 864.2, 881.8, c_ante(
        'Convenio 169 de la OIT', 'Los pueblos tribales',
        'Cuyas condiciones sociales, culturales y económicas les distingan de otros sectores de la '
        'colectividad nacional.')),
    ('c34b_costumbres', 'carton', 897.6, 908.5, cita(
        '«Regidos total o parcialmente por sus propias costumbres o tradiciones o por una legislación '
        'especial».')),
    ('m08_dos', 'mg_lista', 914.5, 936.2, lista(
        'Dos posibilidades',
        ('grupos', 'Condiciones sociales, culturales y económicas propias', 917.5),
        ('libro_ley', 'Una legislación especial, como la Ley 70', 929.4))),
    ('c35_rom', 'carton', 936.9, 946.2, c_tit(
        'El pueblo gitano o rom',
        'Caso único en materia de grupos de inmigrantes.')),
    ('c36_decreto', 'carton', 963.8, 971.6, c_ante(
        'Decreto 2957 de 2010', 'Protección integral del pueblo rom')),
    ('c37_autorreconocimiento', 'carton', 979.8, 992.7, c_tit(
        'El autorreconocimiento',
        'El criterio básico para determinar la pertenencia a un grupo identificado étnicamente.')),
    ('c38_conciencia', 'carton', 1000.5, 1010.2, cita(
        'La conciencia de la identidad indígena o tribal es el criterio fundamental.')),
    ('c39_credibilidad', 'carton', 1027.9, 1037.5, cita(
        'A una persona que invoca su identidad étnica debe otorgársele credibilidad.')),
    ('c40_nna', 'carton', 1053.0, 1060.9, c_ante(
        'Niños, niñas y adolescentes', 'Sus derechos son preferentes')),
    ('m09_derechos', 'mg_lista', 1070.3, 1090.0, lista(
        'La Constitución',
        ('mano_corazon', 'La vida y la integridad física', 1073.1),
        ('cruz_medica', 'La salud y la seguridad social', 1075.0),
        ('familia', 'Tener una familia y no ser separado de ella', 1081.7))),
    ('c41_protegidos', 'carton', 1092.6, 1104.0, cita(
        'Serán protegidos contra toda forma de abandono, violencia física o moral, secuestro, venta, abuso '
        'sexual y explotación.')),
    ('c41b_familia', 'carton', 1112.0, 1123.0, cita(
        'La familia, la sociedad y el Estado tienen la obligación de asistir y proteger al niño.')),
    ('c42_prevalecen', 'carton', 1130.5, 1138.4, cita(
        'Los derechos de los niños prevalecen sobre los derechos de los demás.')),
    ('c43_taxativa', 'carton', 1138.5, 1147.4, cita(
        'La enumeración no es taxativa: se extiende a otros derechos, todos con carácter de prevalencia.')),
    ('c44_convencion', 'carton', 1152.7, 1166.1, c_ante(
        'Bloque de constitucionalidad', 'Convención sobre los Derechos del Niño',
        'De 1989, adoptada mediante la Ley 12 de 1991.')),
    ('c45_interes', 'carton', 1172.0, 1180.2, c_tit(
        'El interés superior',
        'Aplicable a personas menores de dieciocho años.')),
    ('c46_codigo', 'carton', 1180.3, 1197.7, c_ante(
        'Código de la Infancia y la Adolescencia', 'Artículo 8',
        'La satisfacción integral y simultánea de todos sus derechos, universales, prevalentes e '
        'interdependientes.')),
    ('c47_favorable', 'carton', 1201.5, 1213.0, c_nota(
        'Artículo 9',
        'En caso de conflicto de normas, se aplicará la más favorable a su interés superior.')),
    ('c48_frontera', 'carton', 1216.8, 1228.1, cita(
        'No implica que deba dárseles siempre un trato diferencial a los niños, niñas y adolescentes.')),
    ('c48b_formativo', 'carton', 1239.8, 1250.7, cita(
        'En un contexto formativo, esta norma debe ponderarse incluso con otros de sus derechos.')),
    ('c49_personalidad', 'carton', 1251.3, 1265.0, cita(
        '¿El libre desarrollo de la personalidad quiere decir que el niño o niña puede hacer lo que quiere? '
        'Probablemente no.')),
    ('c50_instituciones', 'carton', 1280.4, 1291.5, cita(
        'El menor llega a las instituciones con una serie de derechos que debemos tener en cuenta.')),
    ('c51_escuchado', 'carton', 1298.4, 1311.9, c_tit(
        'El derecho a ser escuchado',
        'Una sentencia reciente de la Corte Constitucional resume la prevalencia de sus derechos.')),
    ('c52_mujeres', 'carton', 1324.8, 1332.6, c_ante(
        'Las mujeres', 'Más de la mitad de la población en Colombia')),
    ('c53_menores', 'carton', 1344.2, 1357.6, cita(
        'Fueron consideradas casi como menores de edad, sin plena capacidad para decidir sobre su '
        'representación política, su patrimonio o su propio cuerpo.')),
    ('c54_libre', 'carton', 1372.0, 1381.8, c_tit(
        'Un derecho especial',
        'El derecho de las mujeres a habitar un mundo libre de violencias.')),
    ('c55_belem', 'carton', 1382.5, 1399.4, c_ante(
        'Convención de Belém do Pará, 1994', 'Artículo 3',
        '«Toda mujer tiene derecho a una vida libre de violencia, tanto en el ámbito público como en el '
        'privado».')),
    ('c56_hombres', 'carton', 1402.6, 1414.1, cita(
        '¿Y los hombres no tienen el mismo derecho? ¿Por qué especificar a la mujer como destinataria?')),
    ('c57_cedaw', 'carton', 1421.7, 1432.7, c_ante(
        'Comité para la Eliminación de la Discriminación contra la Mujer', 'Recomendación general 35')),
    ('c58_genero', 'carton', 1439.9, 1446.6, cita(
        '«Dicha violencia está basada en el género».')),
    ('c58b_razon', 'carton', 1457.1, 1466.5, cita(
        '«Violencia por razón de género contra la mujer»: un término más preciso.')),
    ('c59_social', 'carton', 1473.7, 1484.7, cita(
        '«La violencia como problema social más que individual, que exige respuestas integrales».')),
    ('c60_subordinada', 'carton', 1489.9, 1503.0, cita(
        '«Uno de los medios fundamentales a través de los cuales se ha perpetuado la posición subordinada de '
        'la mujer».')),
    ('c61_obstaculo', 'carton', 1507.4, 1518.1, cita(
        '«Un grave obstáculo para el logro de la igualdad sustantiva entre mujeres y hombres».')),
    ('c62_especifico', 'carton', 1531.8, 1546.1, cita(
        'Si hay una violencia específica que afecta a la mujer, adquiere pleno sentido su derecho a habitar '
        'un mundo libre de ella.')),
    ('c63_conclusion', 'carton', 1547.1, 1564.7, c_ante(
        'En conclusión', 'No son una dádiva de los funcionarios',
        'Los enfoques diferenciales operan en estrecha vinculación con los derechos especiales de las '
        'poblaciones.')),
    ('c64_servidores', 'carton', 1567.8, 1574.5, cita(
        'Todo el tiempo en que actuamos como servidores públicos.')),
]
