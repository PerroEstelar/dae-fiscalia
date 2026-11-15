# -*- coding: utf-8 -*-
"""Unidad 1, contenido: «Igualdad y diferencia» (22:11). Cuadros 50–39876: sin el silencio del
arranque ni el final, cuando el profe se acerca a la cámara para cortar.

Textos de la transcripción de Scribe, sin muletillas. Correcciones de la transcripción:
«atisonante» es «altisonante», «individuo privilegio» es «indebido privilegio», el apartheid
«campeó» (no «cambió») y en el ejemplo del tenis la asamblea vota contra los «mancos» (no
«bancos»)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u1_contenido', 'UNIDAD 1/CONTENIDO', 'Unidad 1. Igualdad y diferencia',
                     'ED - U1 - CONTENIDO', 'enfoquediferencial - U1 - CONTENIDO', 'ED1C', 50, 39876))

ITEMS = [
    ('lt01', 'lt', 2.1, 7.1, PROFE),
    ('c01_unicos', 'carton', 7.3, 13.3, cita('Somos únicos e irrepetibles')),
    ('c02_dignidad', 'carton', 14.1, 25.5, c_tit(
        'La dignidad humana',
        'La autenticidad y luz propia que se agita en el fondo de cada ser humano.')),
    ('c03_proyecto', 'carton', 27.2, 34.5, cita(
        'La posibilidad de darle vida a un proyecto de vida propio.')),
    ('c04_iguales', 'carton', 35.2, 43.9, cita(
        'Suena un poco raro que a renglón seguido se nos afirme que todos somos iguales.')),
    ('c05_familia', 'carton', 49.3, 57.2, c_ante(
        'Veámoslo por espacios', 'La familia como modelo de igualdad')),
    ('c06_navidad', 'carton', 73.3, 85.6, c_tit(
        'La Navidad',
        'Intercambiar regalos con todo ese conglomerado amplio y diverso en edades, roles y afectos.')),
    ('c07_regalo', 'carton', 96.6, 103.3, cita(
        '¿Un regalo idéntico a cada cual? ¿O al menos del mismo valor?')),
    ('c08_criterios', 'carton', 103.5, 111.5, cita(
        '¿Podríamos distinguir por criterios aparentemente objetivos como edad o proximidad?')),
    ('m01_escenarios', 'mg_lista', 118.1, 134.2, lista(
        'Otros escenarios',
        ('carpeta', 'Compra de vestuario o útiles', 121.6),
        ('plato', 'Repartos de comida', 124.3),
        ('libros', 'Gastos en materia educativa', 127.5))),
    ('c09_tiendas', 'carton', 135.9, 142.4, c_ante(
        'Otros espacios', 'Las tiendas')),
    ('c10_orden', 'carton', 147.5, 152.6, cita(
        'A veces, por estricto orden de llegada.')),
    ('c11_mañas', 'carton', 153.4, 162.7, cita(
        'Entre más acumulación de personas crece la presión, y la clientela recurrente se da sus '
        'mañas para no esperar.')),
    ('c12_pequeño', 'carton', 171.8, 184.2, cita(
        'Siempre estará un pequeño o pequeña que inútilmente agita sus monedas o billetes para '
        'hacerse visible.')),
    ('c13_tendero', 'carton', 184.3, 193.5, cita(
        '¿Debe el tendero romper los lazos de vecindad y establecer un estricto control de igualdad?')),
    ('c14_empresa', 'carton', 199.5, 211.7, c_ante(
        'Un tercer espacio', 'Una empresa de calzado',
        'Se genera una plaza libre para el cargo de gerente de ventas.')),
    ('c15_hermano', 'carton', 215.1, 223.2, cita(
        'La mayoría de socios quiere darle el puesto a uno de mis hermanos, pero él no tiene '
        'experiencia.')),
    ('c16_concurso', 'carton', 223.3, 229.5, cita(
        '¿Estamos obligados a hacer un concurso de méritos?')),
    ('c17_diferentes', 'carton', 230.0, 239.3, cita(
        'No solo somos diferentes, sino que en muchos espacios no funciona plenamente lo de la '
        'igualdad.')),
    ('c18_ley', 'carton', 239.4, 249.1, c_tit(
        'Igualdad frente a la ley',
        'Es lo que se predica en las democracias modernas.')),
    ('c19_una_ley', 'carton', 256.2, 263.5, cita(
        '¿Podría decirme al menos una ley que aplique por igual para todos?')),
    ('c20_diferenciaciones', 'carton', 279.4, 287.8, cita(
        'En la mayoría de las leyes no somos realmente iguales: lo que hacen es establecer '
        'diferenciaciones.')),
    ('c21_retorica', 'carton', 287.9, 294.1, cita(
        'Una mera frase retórica que se incumple por doquier.')),
    ('c22_optimizacion', 'carton', 295.2, 303.6, c_tit(
        'Un principio de optimización',
        'La igualdad como principio y no como regla.')),
    ('m02_principios', 'mg_lista', 311.3, 328.2, lista(
        'Principios y reglas',
        ('lista', 'Las reglas se cumplen o se incumplen', 314.3),
        ('ruta', 'Los principios indican un derrotero, un ideal', 320.3))),
    ('c23_fumar', 'carton', 330.9, 338.7, c_tit(
        'Prohibido fumar',
        'Hay pocas formas de discutir si se cumple o no la obligación.')),
    ('c24_limite', 'carton', 351.3, 357.8, cita(
        'Podrían existir situaciones límite que correspondería dilucidar una a una.')),
    ('c25_prospectiva', 'carton', 373.4, 389.9, c_tit(
        'Los principios funcionan de manera prospectiva',
        'Invocar el libre desarrollo de la personalidad no significa que pueda hacer lo que me venga '
        'en gana.')),
    ('c26_clausula', 'carton', 406.4, 419.8, c_ante(
        'Una cláusula',
        'Todos debemos ser tratados por la ley de la misma manera.',
        'Cualquier diferenciación debe justificarse.')),
    ('c27_discriminacion', 'carton', 422.2, 434.4, cita(
        'Si la justificación no es razonable, estaremos frente a una discriminación o un indebido '
        'privilegio.')),
    ('c28_respeto', 'carton', 439.4, 446.5, c_tit(
        'Igual consideración y respeto',
        'Cualquier diferenciación debe justificarse.')),
    ('c29_trato', 'carton', 447.6, 457.9, c_ante(
        'Igualdad de trato',
        'Tratar igual a los iguales y de manera desigual a los desiguales')),
    ('c30_lo_igual', 'carton', 460.5, 465.0, c_suelta('¿Qué es lo igual y qué es lo desigual?')),
    ('c31_punto', 'carton', 480.7, 486.9, cita(
        'Tenemos desigualdades o igualdades desde cierto punto de vista.')),
    ('m03_sospechosas', 'mg_lista', 496.2, 512.0, lista(
        'Categorías sospechosas',
        ('personas', 'Sexo, raza', 499.2),
        ('mundo', 'Origen nacional o familiar, lengua', 501.1),
        ('dialogo', 'Religión, opinión política o filosófica', 504.1))),
    ('c32_esclavitud', 'carton', 515.9, 526.2, c_tit(
        'La esclavitud',
        'No hubiese sido posible sin despersonalizar a quienes la sufrieron.')),
    ('c33_cosa', 'carton', 531.9, 538.2, cita(
        'Se disponía de ellos como una cosa.')),
    ('c34_derechos', 'carton', 552.1, 563.1, cita(
        'No tenían derecho ni a la educación, ni a la representación política, ni a disponer de sus '
        'pertenencias.')),
    ('c35_nazismo', 'carton', 564.0, 578.0, c_tit(
        'El nacionalsocialismo alemán',
        'Normas y sentencias minaron la consideración de la población judía como ciudadanos iguales.')),
    ('m04_prohibiciones', 'mg_lista', 581.4, 593.0, lista(
        'Prohibiciones',
        ('casa_lote', 'Tener propiedades inmuebles', 582.4),
        ('dialogo', 'Participar en política', 584.3),
        ('ruta', 'Transitar libremente', 588.7))),
    ('c36_andamiaje', 'carton', 594.2, 602.6, cita(
        'A los campos de concentración les antecedió todo un andamiaje jurídico que los ubicó como '
        'diferentes.')),
    ('c37_apartheid', 'carton', 602.8, 611.1, c_tit(
        'El apartheid en los Estados Unidos',
        'Por cerca de noventa años, hasta bien avanzado el siglo pasado.')),
    ('c38_separados', 'carton', 611.2, 617.7, c_ante(
        'La Corte Suprema', '«Separados, pero iguales»')),
    ('c39_segregacion', 'carton', 624.9, 633.7, cita(
        'La segregación racial en sí no violaba la constitución si los espacios ofrecidos eran '
        'equivalentes.')),
    ('c40_filtro', 'carton', 646.1, 654.8, cita(
        'Vagones de tren, bibliotecas o restaurantes con un filtro de ingreso conforme al color de la '
        'piel.')),
    ('c41_brown', 'carton', 654.9, 661.4, c_ante(
        '1954', 'Brown versus Board of Education')),
    ('m05_escuelas', 'mg_lista', 673.4, 686.1, lista(
        'Las escuelas segregadas',
        ('edificio', 'Menos prestaciones materiales', 676.4),
        ('grupos', 'Más hacinadas', 678.7),
        ('birrete', 'Maestros menos calificados', 681.3))),
    ('c42_dano', 'carton', 695.3, 706.1, c_tit(
        'Un grave daño psicológico',
        'Baja autoestima e internalización de un menor estatus social.')),
    ('c43_sesenta', 'carton', 707.7, 719.2, cita(
        'Solo hasta la década de los 60 se avanzó en una legislación que fue desmontando el apartheid.')),
    ('m06_hoy', 'mg_lista', 722.2, 746.7, lista(
        'Los ejemplos no terminan en el pasado',
        ('personas', 'Los intocables en la India', 725.2),
        ('mundo', 'La comunidad tibetana en China', 733.2),
        ('persona', 'Las mujeres bajo el régimen talibán', 739.9))),
    ('c44_narrativa', 'carton', 746.8, 757.0, c_tit(
        'Un sustento legal e ideológico',
        'Las diferencias de trato buscan arroparse bajo un sustento que es a la vez legal e ideológico.')),
    ('c45_test', 'carton', 776.6, 791.4, c_tit(
        'Los test de igualdad',
        'Para dilucidar cuándo se está ante una discriminación o ante el establecimiento indebido de un '
        'privilegio.')),
    ('m07_depende', 'mg_lista', 799.5, 811.5, lista(
        'Depende de',
        ('personas', 'Los sujetos involucrados', 802.5),
        ('mapa', 'El contexto', 804.5),
        ('balanza', 'Los derechos que están en juego', 807.2))),
    ('c46_escuela', 'carton', 811.6, 823.2, cita(
        'No es lo mismo el valor de un regalo de Navidad que decidir cuáles de los hermanos o hermanas '
        'deben ir a la escuela.')),
    ('m08_tipos', 'mg_lista', 834.1, 844.0, lista(
        'Tres tipos de test',
        ('balanza', 'Débil', 838.1),
        ('balanza_hoja', 'Intermedio', 838.7),
        ('lupa_doc', 'Estricto', 839.7))),
    ('c47_debil', 'carton', 844.1, 855.5, c_ante(
        'Test débil',
        'Medidas generales que no tengan la potencialidad de afectar derechos fundamentales.')),
    ('c48_razonable', 'carton', 865.9, 871.4, cita(
        'Se espera evaluar que la medida sea razonable y no arbitraria.')),
    ('m09_criterios', 'mg_lista', 873.1, 887.0, lista(
        'Dos criterios',
        ('escudo', 'La finalidad no está prohibida por la Constitución', 876.1),
        ('engranaje', 'El medio es adecuado o idóneo', 880.6))),
    ('c49_muebles', 'carton', 908.0, 918.1, cita(
        '¿Aceptaríamos que los utensilios se dispongan en lugares altos que no estén al alcance de '
        'niños pequeños?')),
    ('c50_intermedio', 'carton', 928.0, 940.8, c_ante(
        'Test intermedio',
        'Derechos no fundamentales, o criterios sospechosos para favorecer a esas mismas poblaciones.')),
    ('c51_fin', 'carton', 946.9, 960.6, c_tit(
        'Un fin importante constitucionalmente',
        'Y medios conducentes, que no afecten esos derechos de manera desproporcionada.')),
    ('m10_materias', 'mg_lista', 973.2, 984.7, lista(
        None,
        ('firma', 'Contratación pública', 974.2),
        ('doc_check', 'Acceso a la función pública', 976.3),
        ('mazo', 'Diseño de las instancias judiciales', 980.7))),
    ('m11_afirmativas', 'mg_lista', 996.5, 1020.2, lista(
        'Acciones afirmativas',
        ('birrete', 'Becas o cupos preferenciales', 999.5),
        ('personas', 'Equidad de género en las instituciones', 1007.5),
        ('mano_corazon', 'Población con movilidad reducida', 1016.1))),
    ('c52_enfoques', 'carton', 1020.3, 1028.5, cita(
        'Una conexión directa con el objetivo nodal de este curso: los enfoques diferenciales.')),
    ('c53_filas', 'carton', 1035.9, 1045.4, c_tit(
        'Un ejemplo',
        'Las filas preferenciales en entidades bancarias o comerciales.')),
    ('c54_estricto', 'carton', 1053.0, 1065.2, c_ante(
        'Test estricto',
        'Derechos fundamentales en riesgo, criterios sospechosos, grupos marginados o privilegios.')),
    ('m12_estricto', 'mg_lista', 1078.8, 1095.8, lista(
        'Tres criterios',
        ('escudo', 'Una medida imperiosa', 1081.1),
        ('mano_corazon', 'Los medios menos lesivos', 1084.7),
        ('balanza', 'Restricciones que no superen los beneficios', 1088.5))),
    ('c55_supervivencia', 'carton', 1098.0, 1109.7, c_tit(
        'Un examen riguroso',
        'Puede estar en riesgo incluso la supervivencia misma de algunas comunidades.')),
    ('m13_derechos', 'mg_lista', 1112.3, 1125.5, lista(
        'Derechos en juego',
        ('mano_corazon', 'Vida y dignidad', 1115.3),
        ('persona', 'Libre desarrollo de la personalidad', 1116.9),
        ('dialogo', 'Salud, participación política, expresión o educación', 1119.4))),
    ('c56_privilegios', 'carton', 1125.6, 1135.4, cita(
        'La creación de privilegios, como exenciones tributarias o regímenes especiales de protección '
        'social.')),
    ('c57_legislar', 'carton', 1135.6, 1149.2, cita(
        'No está prohibido legislar en estas materias: para declarar su exequibilidad se aplica un test '
        'de igualdad más riguroso.')),
    ('c58_cartas', 'carton', 1161.9, 1172.7, c_tit(
        'Cartas de triunfo',
        'El papel que en determinado juego de naipes tienen el joker o el as.')),
    ('c59_minorias', 'carton', 1186.4, 1200.9, cita(
        'Las democracias se caracterizan por la manera en que tratan a sus minorías, en especial a la más '
        'radical de ellas: el individuo.')),
    ('c60_freno', 'carton', 1201.7, 1211.6, cita(
        'Los derechos fundamentales operan como freno a posibles extralimitaciones de las decisiones '
        'mayoritarias.')),
    ('c61_tenis', 'carton', 1229.9, 1243.4, c_tit(
        'Un ejemplo',
        'Una persona que nació sin una mano, fanática del tenis, forma una asociación para construir una '
        'cancha.')),
    ('c62_votacion', 'carton', 1262.9, 1273.8, c_tit(
        'Cuarenta y nueve a uno',
        'La asamblea vota una norma que impide que los mancos la utilicen.')),
    ('c63_triunfo', 'carton', 1277.6, 1288.0, cita(
        '¿Debe resignarse al triunfo de la mayoría, o puede ejercer sus cartas de triunfo?')),
    ('m14_conclusion', 'mg_lista', 1299.5, 1310.1, lista(
        'En conclusión',
        ('balanza', 'Igualdad y diferencia', 1302.5),
        ('ruta', 'La igualdad como principio, no como regla', 1305.3))),
    ('m15_conclusion', 'mg_lista', 1310.4, 1329.0, lista(
        None,
        ('personas', 'La igualdad de trato', 1310.4),
        ('lupa_doc', 'Test diferenciados', 1319.1),
        ('escudo', 'Los derechos fundamentales como cartas de triunfo', 1322.0))),
]
