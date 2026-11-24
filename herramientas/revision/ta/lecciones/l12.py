# -*- coding: utf-8 -*-
from maqueta import *

ESCENAS = [
    lamina('Pregunta orientadora de la lección', T(1241, 1), obj='balanza', rotulo='¿Qué decisión corresponde adoptar?',
           com='La lección abre con su pregunta orientadora, como en el DI.'),
    ruta('Ruta de la lección', [
        ('a. La inadmisión de la denuncia', T(1248, 1), 'documento'),
        ('b. La preclusión', T(1393, 1), 'mazo'),
        ('c. Una ruta práctica para el fiscal', T(1435, 1), 'escalones')]),
    rejilla('Tres figuras, tres lógicas', [
        ('1. Inadmisión de la denuncia', ['Se adopta cuando la noticia criminal no cumple los requisitos mínimos para dar inicio a la actuación penal, porque resulta claramente infundada, implausible, absurda o reiterativa.',
                                          'Art. 69 CPP · Sentencia C-1177 de 2005.'], 'documento'),
        ('2. Archivo de las diligencias', ['Decisión del fiscal, durante la indagación, cuando no existen motivos o circunstancias fácticas que permitan caracterizar el hecho como delito.',
                                           'Art. 79 CPP · Sentencia C-1154 de 2005 · Directiva 0002 de 2025 (FGN).'], 'carpetas'),
        ('3. Preclusión', ['Decisión del juez de conocimiento cuando, con base en los motivos legales del art. 332 CPP, se establece que debe terminarse la actuación penal de manera anticipada.',
                          'Arts. 331 y 332 CPP.'], 'mazo')],
        com='Las tres figuras de la infografía del DI («¿Cuándo corresponde cada institución?»), una por recuadro: la infografía se vuelve interactiva y se lee por partes.'),
    # a. Inadmisión
    esquema('a. La inadmisión de la denuncia', 'documento', [
        ('El artículo 69 del CPP', T(1248, 1, 1), 'libros'),
        ('La Sentencia C-1177 de 2005', J(T(1248, 1, 2), T(1253)), 'mazo'),
        ('No es una liberalidad del funcionario', T(1255, 1), 'escudo'),
        ('Una garantía de acceso a la justicia', T(1266, 2), 'personas'),
        ('La aptitud de la noticia criminal', T(1273), 'lupa')]),
    compara('Inadmisión y archivo: dos momentos distintos', [
        ('En la inadmisión', J(T(1277, 1, 1)), 'documento'),
        ('En el archivo', J(T(1277, 1, 2)), 'carpetas')],
        com='Dos columnas que se despliegan: la diferencia está en el momento y en el objeto del análisis.'),
    compacta('Auto AP-4299-2016: una imputación concreta y seria', [
        ('p', T(1291, 1, 1)),
        ('p', T(1303, 1), 'regla'),
        ('p', T(1309, 2), 'alerta')],
        com='La providencia, la regla que deja y el límite que el DI le pone, en ese orden.'),
    compacta('Lo que agregan las directivas de 2025 y 2026', [
        ('p', T(1319, 2)),
        ('p', J(T(1324), T(1325)), 'clave')]),
] + ejemplo('«Quiero denunciar a una persona»', T(1329), T(1336), B(1337, 1343), [T(1345), T(1350), T(1353), T(1359)],
            com='Este ejemplo trae en el DI un cuarto momento («¿Qué disposición o criterio normativo debe tener presente?»): va como cuarta casilla, al mismo nivel.') + \
    ejemplo('Tres denuncias por los mismos créditos', J(T(1362), T(1365)), T(1369), B(1370, 1374), [T(1376), T(1382), T(1387)]) + [
    # b. Preclusión
    esquema('b. La preclusión: lo esencial', 'mazo', [
        ('Naturaleza', 'La preclusión es una decisión judicial, jurisdiccional y definitiva que pone fin a la acción penal cuando no existen motivos para continuar hacia la acusación. Una vez en firme, produce efectos de cosa juzgada.', 'balanza'),
        ('Propósito', 'Depurar el proceso penal, evitando que continúe cuando, tras la investigación, se verifica que no se configuran los presupuestos legales para formular acusación.', 'escalones'),
        ('Jurisprudencia', 'La Corte Constitucional, en la Sentencia C-591 de 2005, declaró inexequible la expresión «a partir de la formulación de la imputación» contenida en el art. 331, por lo que el fiscal puede solicitar la preclusión en cualquier momento del proceso y la decisión siempre debe ser adoptada judicialmente por el juez de conocimiento. La C-055 de 2018 reafirmó la necesidad de que el juez motive de forma suficiente la decisión de preclusión.', 'libros'),
        ('Causales (art. 332 CPP)', 'Imposibilidad de iniciar o continuar el ejercicio de la acción penal; existencia de una causal que excluya la responsabilidad; inexistencia del hecho investigado; atipicidad del hecho investigado; ausencia de intervención del imputado en el hecho; imposibilidad de desvirtuar la presunción de inocencia; vencimiento del término máximo del art. 294 CPP.', 'lupa'),
        ('Trámite y efectos (arts. 333 y 334)', 'Se realiza audiencia ante el juez de conocimiento. La decisión es judicial. Una vez en firme, pone fin a la acción penal con cosa juzgada e impide los mismos de enjuiciamiento.', 'tribunal')],
        com='La infografía «La preclusión» del DI convertida en mapa conceptual: cinco tarjetas que se abren en vez de nueve recuadros en una sola imagen. La preclusión se estudia a fondo en la unidad 2.'),
    compara('Archivo frente a preclusión', [
        ('Archivo', 'Decisión del fiscal, directa y motivada. Solo durante la indagación (antes de la imputación). No produce cosa juzgada.', 'carpetas'),
        ('Preclusión', 'Decisión del juez de conocimiento. Puede solicitarse en cualquier etapa. Termina la acción penal con cosa juzgada y reviste las medidas de aseguramiento.', 'mazo')],
        com='Así dice la infografía del DI: «reviste las medidas de aseguramiento»; parece que es «revoca». Confirmar con el autor.'),
] + ejemplo('El conductor y la maniobra', T(1397), T(1402), B(1403, 1411), [J(T(1413), T(1415)), T(1421), T(1426)], clave=T(1431),
            video=('c09', 'Caso: El conductor y la maniobra'),
            com='Caso animado ya producido para esta lección.') + [
    # c. Ruta práctica
    compacta('c. ¿Inadmisión, archivo o preclusión? Diferencias clave', [
        ('tabla', ['', 'Inadmisión', 'Archivo', 'Preclusión'], [
            ['¿Quién decide?', 'El fiscal.', 'El fiscal.', 'El juez de conocimiento.'],
            ['¿En qué momento procede?', 'Antes de iniciar la indagación.', 'Durante la indagación (antes de la imputación).', 'En cualquier etapa del proceso (arts. 331 y 332 CPP).'],
            ['¿Cuál es el fundamento?', 'Falta de requisitos mínimos de la noticia criminal.', 'Ausencia de motivos o circunstancias fácticas que permitan caracterizar el hecho como delito (atipicidad objetiva).', 'Configuración de alguna de las causales del art. 332 CPP.'],
            ['¿Qué efecto tiene?', 'Impide el inicio de la actuación penal.', 'Termina la indagación, sin cosa juzgada (puede reanudarse si surgen nuevos elementos).', 'Termina la acción penal con cosa juzgada y reviste las medidas de aseguramiento.']])],
        com='Cuadro comparativo de la infografía del DI: cuatro preguntas por tres figuras. Descargable como PDF para tenerlo a mano.'),
    giro('Principios orientadores', [
        ('Legalidad', 'La decisión debe basarse en los presupuestos y límites previstos en la ley.', 'escudo'),
        ('Proporcionalidad', 'Debe adoptarse la medida menos restrictiva y adecuada a las circunstancias del caso.', 'balanza'),
        ('Protección de derechos', 'Se deben garantizar los derechos de las víctimas, del imputado y la correcta administración de la justicia.', 'personas')]),
    ruta('Ruta práctica de decisión', [
        ('1. Verifique la noticia criminal', '¿Cumple los requisitos mínimos y es verosímil?', 'lupa'),
        ('2. Analice los hechos y la investigación', '¿Existen motivos o circunstancias fácticas que permitan estimar un delito?', 'documento'),
        ('3. Examine las causales legales', 'Si ya hay proceso, ¿se configura alguna de las causales del art. 332 CPP?', 'balanza'),
        ('4. Adopte la decisión', 'Inadmisión, archivo o solicitud de preclusión, según corresponda.', 'escalones'),
        ('5. Motive y comunique', 'Fundamente la decisión y comuníquela a quienes corresponda.', 'carpetas')],
        com='Los cinco pasos de la infografía como ruta: cada paso con su pregunta.'),
    compacta('Cierre de la lección', [
        ('p', T(1440, 3), 'clave'),
        ('p', T(1444, 2))],
        ilus='comunidad-interes-general.webp'),
]
