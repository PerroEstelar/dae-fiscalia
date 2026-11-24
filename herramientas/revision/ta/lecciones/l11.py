# -*- coding: utf-8 -*-
from maqueta import *

UNIDADES_LISTA = ['Unidad 1. Archivo de la indagación', 'Unidad 2. La preclusión en el proceso penal',
                  'Unidad 3. Aplicación del principio de oportunidad', 'Unidad 4. Preacuerdos y negociaciones en el sistema penal']


def afir(l_af, l_retro, extra=()):
    return sin_rotulo(T(l_af)), J(sin_rotulo(T(l_retro)), *[T(x) for x in extra])


a11, r11 = afir(560, 562); a12, r12 = afir(569, 572); a13, r13 = afir(578, 580)
a21, r21 = afir(605, 608); a22, r22 = afir(615, 618, [622]); a23, r23 = afir(624, 626, [631])
a31, r31 = afir(651, 654); a32, r32 = afir(661, 664); a33, r33 = afir(671, 674)

ESCENAS = [
    compacta('Presentación del curso', [
        ('p', T(8, 2)),
        ('sub', 'Las cuatro unidades del curso'),
        ('lista', UNIDADES_LISTA, True)],
        video=('curso_inicio', 'Presentación del curso · Juan David Peña Gómez'),
        guia='Vea el video de presentación del curso.',
        com='Abre el curso con el video del profe que ya está producido; al lado, las cuatro unidades para que el estudiante vea el recorrido completo desde el principio.'),
    compacta('Introducción a la unidad 1', [
        ('p', T(350, 1), 'clave'),
        ('sub', 'Las tres lecciones de la unidad'),
        ('lista', ['1.1. Fundamentos, causales y procedencia del archivo', '1.2. Archivo, inadmisión de denuncia y preclusión',
                   '1.3. Desarchivo, reactivación y derechos de las víctimas'])],
        video=('u1_inicio', 'Introducción a la unidad 1'),
        guia='Vea el video de introducción a la unidad.',
        com='Video del profe ya producido (inicio de la unidad 1). La pregunta central del curso queda escrita al lado: es el hilo de todas las unidades.'),
    lamina('Pregunta orientadora de la lección', T(387, 2), obj='lupa', rotulo='¿Cómo evitar los errores al ordenar el archivo?',
           com='Se reemplaza el «objetivo» por la pregunta orientadora, que es como el DI abre la lección.'),
    ruta('Ruta de la lección', [
        ('a. Fundamentos jurídicos', T(435, 1), 'libros'),
        ('b. Causales de archivo', T(451, 1), 'carpetas'),
        ('c. Procedencia del archivo', T(947, 1), 'balanza'),
        ('d. Deficiencia técnica y absolución perentoria', T(1104, 1), 'mazo')],
        com='Índice por temas, no por páginas: el estudiante sabe dónde está y qué falta.'),
    # a. Fundamentos
    esquema('a. Fundamentos jurídicos del archivo', 'libros', [
        ('El artículo 79 del CPP', T(395), 'libros'),
        ('Opera durante la indagación', T(400, 2), 'reloj'),
        ('Una lectura sistemática', T(409), 'escalones'),
        ('Decide el fiscal, sin autorización judicial', T(440), 'mazo'),
        ('Sustentado en hechos constatados', T(443), 'lupa')],
        com='Mapa conceptual con descarga: cinco ideas cortas en las tarjetas y el texto completo al abrir cada una.'),
    giro('Qué decide el fiscal cuando archiva', [
        ('No es renunciar a perseguir un delito', T(422, 1, 1), 'escudo'),
        ('No es una preclusión', J(T(422, 1, 2), T(400, 1, 2)), 'tribunal'),
        ('Es constatar que faltan los presupuestos objetivos', T(422, 1, 3), 'lupa')],
        com='Tres tarjetas que se giran: separa el archivo de las otras salidas antes de entrar a las causales.'),
    compacta('El precedente: Sentencia C-1154 de 2005', [
        ('p', T(413, 1)),
        ('p', T(447), 'regla')],
        com='La cita de la Corte va en cursiva y aparte del texto del autor; la pregunta que deja va como regla de decisión.'),
    # b. Causales
    compacta('b. Las causales: dos grandes grupos', [
        ('p', T(451, 1)),
        ('malla', [[('1. Atipicidad objetiva', [T(451, 1, 1), T(462, 2, 1)], 'lupa'),
                    ('2. Imposibilidad de encontrar al sujeto activo', [T(451, 1, 2), T(462, 1)], 'personas')]]),
        ('p', T(451, 1, 3), 'alerta')],
        com='Organizador de dos casillas al mismo nivel, como pidió la revisión, y la exigencia común a las dos como alerta.'),
    compacta('La atipicidad objetiva: del tipo penal a los hechos', [
        ('p', T(480, 1)),
        ('p', T(480, 2, 1)),
        ('p', T(487, 2), 'regla')],
        ilus='norma-competencia.webp'),
] + ejemplo('¿Incumplimiento contractual o delito?', T(492), T(503), B(504, 511), [T(513), T(520), T(526)], clave=T(534),
            video=('c07', 'Caso: ¿Incumplimiento contractual o delito?'),
            com='El caso animado ya está producido (María y Carlos): va una sola vez y al lado las preguntas del DI para pensar mientras se ve.',
            com_analisis='Los tres momentos del análisis al mismo nivel, sin repetir el texto del caso.') + [
    actividad('Actividad: ¿hay atipicidad objetiva?', [
        VF(a11, True, r11, contexto=sin_rotulo(T(549))), VF(a12, False, r12), VF(a13, False, r13),
        VF(a21, True, r21, contexto=J(*[sin_rotulo(T(593))])), VF(a22, False, r22), VF(a23, False, r23),
        VF(a31, True, r31, contexto=sin_rotulo(T(639))), VF(a32, False, r32), VF(a33, False, r33)],
        intro=[T(546)], cierre=[sin_rotulo(T(686)), T(691)], pagina=2,
        com='Verdadero o falso autocalificable: tres situaciones, tres afirmaciones cada una, con la explicación del DI al responder. Sin «objetivo de la actividad».'),
    ruta('Tres preguntas antes de archivar', [
        ('1. ¿Qué tipo penal podría caracterizar los hechos?', T(693, None, 2), 'libros'),
        ('2. ¿Qué elemento objetivo no está acreditado?', T(696, None, 2), 'lupa'),
        ('3. ¿Se hicieron las actividades investigativas necesarias?', T(699, None, 2), 'expediente')],
        com='La reflexión final de la actividad, en tres pasos: es lo que el fiscal se lleva para su despacho.'),
    compacta('Un error frecuente: confundir atipicidad objetiva y subjetiva', [
        ('p', T(707, 2)),
        ('p', J(T(714), T(715)), 'alerta'),
        ('p', T(717))]),
    compacta('El segundo grupo: no es posible encontrar al sujeto activo', [
        ('p', T(719, 2)),
        ('malla', [[('Imposibilidad de establecer quién es', T(725, 1, 2), 'personas'),
                    ('Imposibilidad de ubicar a quien ya se conoce', T(725, 1, 3), 'casa')]]),
        ('p', T(736), 'regla')],
        com='Las dos situaciones que el DI pide no confundir, lado a lado.'),
] + ejemplo('El hurto de madrugada', T(739), T(750), B(751, 761), [T(763), T(770), T(775)], clave=T(780),
            video=('c06', 'Caso: El hurto de madrugada'),
            com='Segundo caso animado ya producido.') + [
    compacta('Desconocer al autor no es establecer que alguien no lo cometió', [
        ('p', T(784, 1, 1)),
        ('p', T(788, 1)),
        ('p', T(800, 1), 'clave')],
        com='La cita de la Corte Suprema (SP-2810-2022) en cursiva y separada; la idea clave, resaltada.'),
] + ejemplo('Juan y la riña', T(804), T(809), B(810, 815), [J(T(816), T(819)), T(823), T(829)], clave=T(833),
            com='Ejemplo sin video: la situación en una ventana y los tres momentos del análisis al mismo nivel.') + [
    compacta('La misma lógica frente al sujeto pasivo', [
        ('p', T(837, 2)),
        ('p', T(837, 2, 2)),
        ('p', T(842, 2), 'alerta')]),
] + ejemplo('La estafa y las víctimas que no aparecen', T(850), T(858), B(859, 864), [T(865), T(872), T(878)], clave=T(882)) + [
    compacta('Una regla práctica antes de emitir la orden', [
        ('p', T(887, 1)),
        ('p', T(896, 1), 'regla'),
        ('p', T(896, 2, 1))]),
] + ejemplo('Pedro denuncia a su vecino', T(901), T(907), B(908, 915), [T(916), T(923), T(929)], clave=T(935)) + [
    compacta('Priorizar no es archivar: Directiva 0002 de 2023', [
        ('p', T(938, 2)),
        ('p', T(938, 1, 3), 'clave')]),
    # c. Procedencia
    compara('c. Procedencia: cuando la duda no es de tipicidad objetiva', [
        ('Dudas sobre quién fue o cómo actuó', T(947), 'personas'),
        ('Una posible causal de ausencia de responsabilidad', T(953), 'balanza')],
        com='Dos columnas que se despliegan: los dos riesgos que el DI describe; ninguno se resuelve con archivo.'),
] + ejemplo('La servidora pública y el pago al contratista', T(960), T(966), B(967, 972), [T(973), T(980), T(986)], clave=T(992),
            com='Ojo: en el DI, el análisis de este ejemplo repite el del ejemplo de Pedro (habla del vecino y del hurto). Confirmar con el autor el texto propio de este caso.') + [
    compacta('La motivación de la orden de archivo', [
        ('p', T(995, 2)),
        ('p', T(1011), 'clave')],
        com='El DI trae este párrafo dos veces casi igual (renglones de «En este orden de ideas» y «En esta línea»): va una sola vez.'),
    compacta('Sentencia SP-230-2023: el archivo no reemplaza la investigación', [
        ('p', T(1015, 3)),
        ('p', T(1025, 1))]),
    compacta('El vencimiento de términos no es una causal automática', [
        ('p', J(T(1031), T(1032, 1))),
        ('p', T(1032, 1, 1)),
        ('p', T(1060, 2), 'regla')]),
    ruta('Directiva 0002 de 2026: recepción, verificación y gestión inicial', [
        ('Verificación inicial', T(1066, 2), 'documento'),
        ('No toda decisión inicial es un archivo', T(1071, 2), 'carpetas'),
        ('Intervención temprana', T(1078, 3), 'camara'),
        ('Falta de información no es falta de actividad', T(1084, 2), 'lupa'),
        ('Los supuestos de archivo en esta etapa', T(1090), 'expediente')]),
    # d. Absolución perentoria
    esquema('d. Deficiencia técnica: la absolución perentoria', 'tribunal', [
        ('Un archivo que no se estudió a tiempo', T(1104), 'reloj'),
        ('Qué es la absolución perentoria', T(1109), 'libros'),
        ('Solo por atipicidad objetiva', T(1115), 'lupa'),
        ('La atipicidad debe ser manifiesta', T(1125, 2), 'alerta' if False else 'escudo'),
        ('Sentencia C-651 de 2011', T(1135), 'mazo')]),
    actividad('Preguntas de reflexión: la absolución perentoria', [
        MC(T(1153), [('A', sin_rotulo(T(1154))), ('B', sin_rotulo(T(1156))), ('C', sin_rotulo(T(1158))), ('D', sin_rotulo(T(1160)))], 'C',
           {'A': sin_rotulo(T(1163)), 'B': sin_rotulo(T(1171)), 'C': sin_rotulo(J(*[T(i) for i in range(1179, 1187)])), 'D': sin_rotulo(T(1187))}),
        MC(T(1197), [('A', sin_rotulo(T(1198))), ('B', sin_rotulo(T(1199))), ('C', sin_rotulo(T(1201))), ('D', sin_rotulo(T(1202)))], 'B',
           {'A': sin_rotulo(T(1204)), 'B': sin_rotulo(T(1211)), 'C': sin_rotulo(T(1221)), 'D': sin_rotulo(T(1227))})],
        intro=[T(1150)], pagina=1,
        com='Selección múltiple autocalificable, con la explicación de cada opción tal como la trae el DI.'),
    compacta('Cierre de la lección', [
        ('p', T(1095, 2), 'clave'),
        ('p', T(1100))],
        ilus='comunidad-interes-general.webp'),
]
