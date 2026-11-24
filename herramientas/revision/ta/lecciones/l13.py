# -*- coding: utf-8 -*-
from maqueta import *


def afir(l_af, l_retro, extra=()):
    return sin_rotulo(T(l_af)), J(sin_rotulo(T(l_retro)), *[T(x) for x in extra])


a11, r11 = afir(1798, 1801); a12, r12 = afir(1808, 1811, [1814]); a13, r13 = afir(1817, 1820)
a21, r21 = afir(1845, 1847); a22, r22 = afir(1853, 1856); a23, r23 = afir(1864, 1867)
a31, r31 = afir(1897, 1900); a32, r32 = afir(1907, 1910); a33, r33 = afir(1917, 1920)

OCHO = [oraciones(limpia(re.sub(r'^\d+\.\s*', '', T(i))))[0] for i in (1716, 1717, 1718, 1719, 1720, 1721, 1722, 1724)]

ESCENAS = [
    lamina('Pregunta orientadora de la lección', T(1458, 1), obj='reloj', rotulo='¿Cuándo debe reactivarse una indagación archivada?'),
    ruta('Ruta de la lección', [
        ('a. Los derechos de las víctimas en el archivo', T(1466, 1), 'personas'),
        ('b. Desarchivo de las diligencias', T(1659, 1), 'carpetas'),
        ('c. Reactivación de la investigación', T(1747, 3, 1), 'lupa'),
        ('d. Una ruta práctica para el fiscal', T(1958, 1), 'escalones')]),
    # a. Víctimas
    esquema('a. Los derechos de las víctimas frente al archivo', 'personas', [
        ('Sentencia C-454 de 2006', T(1466, 3), 'mazo'),
        ('Acceso a la justicia (art. 229 CP)', T(1474, 1), 'escudo'),
        ('Sentencia C-1177 de 2005', T(1484), 'libros'),
        ('Comunicación eficaz y motivada', T(1493), 'telefono'),
        ('Cuándo y cómo comunicar', T(1498), 'reloj'),
        ('Especial cuidado del fiscal', T(1503), 'lupa')]),
] + ejemplo('Laura y la orden que nunca le comunicaron', T(1507), T(1513), B(1514, 1519), [T(1521), T(1528), T(1534)],
            com='Ejemplo sin video: situación en ventana y los tres momentos al mismo nivel.') + [
    compacta('El archivo no extingue la acción penal', [
        ('p', J(T(1541), T(1544))),
        ('p', T(1546, 1), 'alerta'),
        ('p', T(1546, 1, 2))]),
    compacta('Cuatro garantías y la comunicación del archivo', [
        ('p', T(1639)),
        ('p', T(1644, 2)),
        ('p', T(1651, 1), 'clave')],
        com='Las cuatro garantías de la C-1154 de 2005 y la T-520A de 2009 en una sola pantalla de lectura corta; la idea clave, resaltada.'),
    # b. Desarchivo
    compara('b. El desarchivo: dos dimensiones', [
        ('Reactivación oficiosa', T(1567, 1, 1), 'lupa'),
        ('Reactivación a partir de la víctima', T(1567, 1, 2), 'personas')],
        com='Las dos vías del desarchivo lado a lado; lo común a ambas queda en la pantalla siguiente.'),
    compacta('¿Qué cuenta como «nuevo elemento»?', [
        ('p', T(1567, 1, 3), 'regla'),
        ('p', T(1577)),
        ('lista', [T(1578), T(1580), T(1582)], True)],
        com='Lista numerada: las tres pruebas que debe pasar un elemento para justificar el desarchivo.'),
] + ejemplo('El video que aparece seis meses después', T(1593), T(1599), B(1600, 1605), [J(T(1607), T(1609)), J(T(1614), T(1617)), T(1621)],
            video=('c08', 'Caso: El video que aparece seis meses después'),
            com='Caso animado ya producido para esta lección.') + [
    compacta('Veamos otro ejemplo: «no estoy de acuerdo con la decisión»', [
        ('malla', [[('Situación', [T(1626)], 'expediente')]]),
        ('p', T(1632), 'clave'),
        ('p', T(1635))],
        com='El DI resuelve este ejemplo en un párrafo («La respuesta es sencilla…»), sin los tres momentos: va como idea clave.'),
    compacta('Sin control judicial automático, con autocontrol del fiscal', [
        ('p', T(1659, 1, 1)),
        ('p', T(1663, 1, 2)),
        ('p', T(1672, 1), 'clave')]),
] + ejemplo('Documentos que ya estaban en otra entidad', T(1679), T(1685), B(1686, 1690), [T(1692), T(1698), T(1704)]) + [
    compacta('Antes de archivar: ocho preguntas (1 a 4)', [
        ('p', T(1711, 1, 2)),
        ('chequeo', OCHO[:4])],
        com='Lista de chequeo con simulación (el estudiante marca cada pregunta), en dos pantallas de cuatro para que no pida scroll. Con botón para descargarla en PDF.'),
    compacta('Antes de archivar: ocho preguntas (5 a 8)', [
        ('chequeo', OCHO[4:])]),
    compacta('Comunicar el archivo y el control a solicitud de la víctima', [
        ('p', T(1725, 1, 2)),
        ('p', T(1735, 1, 2), 'clave'),
        ('p', T(1742, 1))]),
    # c. Reactivación
    esquema('c. Reactivación de la investigación', 'lupa', [
        ('¿Qué sucede cuando se desarchiva?', T(1747, 3, 1), 'carpetas'),
        ('No predetermina el resultado', T(1752, 1, 1), 'balanza'),
        ('Cuando no se pudo identificar al autor', T(1759), 'personas'),
        ('El límite: la acción penal vigente', T(1764), 'reloj'),
        ('Archivo y preclusión no se mezclan', T(1769, 2, 2), 'mazo'),
        ('Dos extremos que se evitan', T(1775), 'escudo')]),
    actividad('Actividad: ¿deficiencia investigativa o nuevo elemento?', [
        VF(a11, True, r11, contexto=sin_rotulo(T(1788))), VF(a12, False, r12), VF(a13, False, r13),
        VF(a21, False, r21, contexto=sin_rotulo(T(1832))), VF(a22, True, r22), VF(a23, True, r23),
        VF(a31, False, r31, contexto=sin_rotulo(T(1881))), VF(a32, True, r32), VF(a33, True, r33)],
        intro=[T(1783)], cierre=[sin_rotulo(T(1937, 4)), T(1951)], pagina=2,
        com='Verdadero o falso autocalificable con las tres situaciones del DI y su explicación. Sin «objetivo de la actividad».'),
    ruta('d. Una ruta práctica para el fiscal', [
        ('1. ¿Hubo una investigación diligente?', '¿La decisión inicial estuvo precedida de una investigación diligente?', 'lupa'),
        ('2. ¿El nuevo elemento cambia los fundamentos?', '¿Los nuevos elementos tienen capacidad para modificar los fundamentos del archivo?', 'carpetas'),
        ('3. ¿Se puede reanudar?', '¿Se encuentran satisfechos los presupuestos jurídicos para reanudar la indagación?', 'balanza'),
        ('Un mismo sistema de decisión', T(1958), 'escalones')],
        com='Las tres preguntas con que el DI cierra la actividad, como ruta; la última parada resume la lección.'),
    compacta('Síntesis de la unidad 1', [
        ('p', T(2034)),
        ('p', T(1963, 1, 1), 'clave')],
        video=('u1_cierre', 'Síntesis de la unidad 1'),
        guia='Vea el video de síntesis de la unidad.',
        com='«Actividad de acompañamiento dirigido»: el video de cierre de la unidad, ya producido.'),
    lamina('Finalización de la unidad', J(T(2210).replace(' 🎉', '').replace('¡Felicitaciones por completar esta unidad! ', ''), T(2213)), obj='escalones', rotulo='¡Felicitaciones por completar esta unidad!',
           ilus='comunidad-interes-general.webp',
           com='La evaluación de la unidad (seis preguntas sobre la caducidad de la querella) va como cuestionario del aula virtual, para que la nota quede registrada.'),
]
