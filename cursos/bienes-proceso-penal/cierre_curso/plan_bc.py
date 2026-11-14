# -*- coding: utf-8 -*-
"""Cierre del curso «Bienes en el proceso penal» (Curso 5, 14 nov 2026).

**Pedido.** Es el mismo de la introducción (`plan_bi.py`): profe a cámara con intro,
outro, cartones de entrada y salida con el nombre del curso, lower thirds, cartones
de apoyo y gráficos de AE.

**Fuente.** Drive, curso → `VIDEOS UNIDADES/bienes_cierre_curso.mp4`.
- Es una grabación de Teams de 43:18, 1280×720 a 30 fps, con el mismo fondo virtual
  del edificio y el mismo profe, Sergio Andrés López Zamora.
- Es una recapitulación completa del curso:
  1. las cuatro unidades;
  2. un ejercicio integrador con cinco bienes y siete preguntas;
  3. las competencias;
  4. cinco recomendaciones;
  5. la metodología y una reflexión final.

**Un arranque en falso.** En 2493,1 dice «La adecuada intervención patrimonial…», se
detiene y la repite entera en 2499,0.
- Se cortan 6,3 s (2492,4 → 2498,7) con `TRAMOS`.
- La frase repetida va en un plano más cerrado (ventana 1024×576 desde (96, 40),
  ×1,875) hasta 2507,9. Eso disimula el salto y subraya la frase.
- El panel DAE/Fiscalía entra entero también en ese plano.
- En el corte de audio hay fundidos de 15 ms.
- Ese tramo no lleva gráficos.
- Los tiempos del plan son de la fuente; `cuadro` los pasa a la línea descontando
  el corte.

**Ventana:** 1143×643 desde (0, 40), ×1,68. Es la estándar.
- Se midió sobre los cuadros de la fuente, cada 2,5 s, con el fondo calculado como
  la mediana.
- La cabeza empieza en y≈310, con el borde izquierdo en x 479–523 (p2), 534–561
  (p10) y 602–634 (p50) en las filas 340–460. En la salida eso da desde x≈805 (p2).
- Los hombros abren desde y≈480. En la caja (hasta y 720 de salida, fila 468 de la
  fuente) no entran.
- El panel DAE/Fiscalía (x 127–595, y 52–157) entra entero.

**Textos.** Salen de Scribe (WAV a 16 kHz, una voz), sin muletillas. Se corrigieron
estos errores de transcripción:
- «votar» → «adoptar» (decisiones);
- «editarse» → «evitarse» (errores);
- «FEAD» y «FEAP» → «FEAB»;
- «dirigencia» → «diligencia»;
- «bona fe» → «buena fe».

En 1383 dice «adquirido ilícitamente, pero utilizado como instrumento». Por el
contraste con la causal de origen, y porque en 1786 lo repite así, es «lícitamente».

No se ponen en pantalla dos frases que dicen otra cosa de lo que quiere decir:
- «no cumplen necesariamente una función jurídica» (176,5);
- «que su extinción resulte proporcional» (1871).

**Gráficos.**
- Las listas y las tarjetas se midieron antes de armar (cima ≥ 250) con las mismas
  fuentes y el mismo `maquetar`. Los rótulos son sus palabras recortadas.
- El ícono `vehiculo` se dibujó en el estilo de los de SRPA
  (`herramientas/motion/icono_vehiculo.py`), porque ese juego no traía ninguno.
- Son casi todos cartones, porque pesan poco. Hay listas de AE donde enumera, y
  tarjetas (`mg_act`) para las competencias.

Los tiempos están en segundos de la fuente. En la línea, cuadro = 409 +
round(a_salida(t) · 23,976).
"""

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal'
R = CURSO + '/CIERRE DEL CURSO'
BIN = ['C5 BIENES EN EL PROCESO PENAL', 'CIERRE DEL CURSO']
ORIGINAL = R + '/01 VIDEO/bienes_cierre_curso.mp4'
COMPUESTO = R + '/01 VIDEO/BC_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo bienes cierre del curso.mp4'
TITULO_BASE = None
CURSO_LINEAS = ['Bienes en el proceso penal']
SUB = 'Cierre del curso'
NOMBRE_LINEA = 'BIENES - CURSO - CIERRE'
EXPORT = 'bienes - CURSO - CIERRE-v%d'
PREFIJO = 'BC'
TMP = 'D:/DAE/_tmp/bienes/bc'
XY, VENTANA = (0, 40), (1143, 643)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
AEP = CURSO + '/00 MOTION GRAPHICS/BIENES_intros_mg.aep'
ICONOS = CURSO + '/00 MOTION GRAPHICS/iconos'
MASTER_DIR = 'D:/DAE/_masters_archivo/CURSO 5 - Bienes en el proceso penal/CIERRE DEL CURSO'

CORTE = (2492.4, 2498.7)              # arranque en falso de «La adecuada intervención patrimonial…»
PLANO_CERRADO = (96, 40, 1024, 576)   # la frase repetida, hasta 2507,9
TRAMOS = [(0.0, CORTE[0], None), (CORTE[1], 2507.9, PLANO_CERRADO), (2507.9, None, None)]

NOMBRE_CURSO = 'Bienes en el proceso penal'
PROFE = ('Sergio Andrés López Zamora',
         'Abogado, doctor en Derecho Público, magíster en Derecho Penal y Procesal Penal y en '
         'Derechos Humanos')


def a_salida(t):
    """Segundo de la fuente → segundo del clip compuesto (sin el arranque en falso)."""
    if CORTE[0] < t < CORTE[1]:
        raise ValueError('%.2f cae dentro del corte' % t)
    return t - (CORTE[1] - CORTE[0]) if t >= CORTE[1] else t


def cuadro(t):
    return CLIP0 + int(round(a_salida(t) * FPS))


def cita(t):
    return [(t, 'bold', TIT, 0)] if len(t) <= 78 else [(t, 'med', CUE, 0)]


def c_tit(titulo, cuerpo):
    return [(titulo, 'bold', TIT, 0), (cuerpo, 'med', CUE, GAP_TIT)]


def c_ante(ante, titulo, cuerpo=None):
    ls = [(ante, 'med', ANTE, 0), (titulo, 'bold', TIT, GAP_ANTE)]
    if cuerpo:
        ls.append((cuerpo, 'med', CUE, GAP_CUE + 8))
    return ls


def c_suelta(t):
    return [(t, 'bold', SUELTA, 0)]


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}


ITEMS = [
    # ---------------------------------------------------------------- apertura
    ('lt01', 'lt', 2.7, 10.8, PROFE),
    ('c01_dimension', 'carton', 35.6, 48.3, c_tit(
        'A lo largo del curso',
        'Examinamos el tratamiento jurídico, probatorio y administrativo de los bienes relacionados '
        'con conductas delictivas.')),
    ('c02_no_se_limita', 'carton', 49.3, 64.0, cita(
        'La actividad de la Fiscalía no se limita a establecer la existencia de una conducta punible, '
        'identificar a sus posibles responsables y sustentar las pretensiones ante las autoridades '
        'judiciales.')),
    ('m01_comprende', 'mg_lista', 65.4, 82.7, lista(
        None,
        ('lupa_doc', 'Identificar bienes y reconstruir operaciones', 68.0),
        ('escudo', 'Garantizar los derechos de las víctimas', 71.7),
        ('candado', 'Preservar activos susceptibles de comiso', 73.9),
        ('libro_ley', 'Reconocer la extinción de dominio', 76.2))),
    ('m02_exigen', 'mg_lista', 86.1, 101.4, lista(
        'Estas actuaciones exigen',
        ('cerebro', 'Conocimientos especializados', 88.1),
        ('lupa_doc', 'Capacidad de análisis', 90.6),
        ('apreton', 'Coordinación entre fiscales, asistentes y policía judicial', 92.9))),
    ('c03_herramientas', 'carton', 103.0, 116.5, cita(
        'Este curso fue diseñado para proporcionar herramientas jurídicas y metodológicas que '
        'fortalezcan la calidad de las decisiones relacionadas con los bienes en el proceso penal.')),
    ('m03_hoy', 'mg_lista', 117.0, 142.5, lista(
        'Hoy realizaremos',
        ('lista', 'Una recapitulación general', 118.6),
        ('birrete', 'Las competencias', 124.1),
        ('engranaje', 'Un ejercicio práctico', 127.1),
        ('ojo', 'Los errores a evitar', 136.2))),
    ('c04_proposito', 'carton', 150.5, 165.8, cita(
        'Una metodología de actuación para adoptar decisiones patrimoniales jurídicamente fundamentadas, probatoriamente '
        'sustentadas y respetuosas de los derechos fundamentales.')),

    # ---------------------------------------------------------------- unidad 1
    ('c05_u1', 'carton', 170.7, 176.3, c_ante('Unidad 1', 'Función del bien')),
    ('c06_mismo_activo', 'carton', 189.5, 199.0, cita(
        'Un mismo activo puede resultar relevante desde diferentes perspectivas y encontrarse '
        'sometido a tratamientos jurídicos distintos.')),
    ('c07_mod1', 'carton', 199.5, 211.7, c_ante(
        'Primera modalidad', 'Elementos materiales probatorios y evidencia física',
        'Contribuyen al esclarecimiento de los hechos investigados.')),
    ('c08_telefono', 'carton', 216.9, 232.7, cita(
        'Un teléfono celular con comunicaciones sobre la planificación de una conducta delictiva: '
        'importa por la información que permite obtener para reconstruir los acontecimientos.')),
    ('c09_reglas', 'carton', 234.7, 244.9, cita(
        'Su tratamiento debe observar las reglas de obtención, preservación, autenticidad y '
        'valoración de los elementos de conocimiento.')),
    ('c10_mod2', 'carton', 245.6, 257.6, c_ante(
        'Segunda modalidad', 'Objeto material del delito',
        'La persona, cosa o realidad sobre la cual recae directamente la conducta punible.')),
    ('c11_hurto', 'carton', 258.0, 268.5, cita(
        'En un hurto, el vehículo sustraído puede constituir el objeto material, al igual que un '
        'cúmulo de criptoactivos en una wallet digital.')),
    ('c12_intangibles', 'carton', 281.1, 293.1, c_tit(
        'No siempre es físico',
        'Puede recaer sobre intangibles, derechos de contenido económico, derechos morales o recursos '
        'digitales.')),
    ('c13_mod3', 'carton', 305.5, 318.0, c_ante(
        'Tercera modalidad', 'Bienes para garantizar la reparación',
        'Su relevancia no depende de que hayan sido utilizados para cometer el delito.')),
    ('c14_inmueble', 'carton', 321.2, 334.2, cita(
        'Un inmueble adquirido lícitamente por una persona imputada podría servir como respaldo '
        'patrimonial para una eventual reparación integral.')),
    ('c15_mod4', 'carton', 337.2, 348.5, c_ante(
        'Cuarta modalidad', 'Bienes susceptibles de comiso',
        'La privación definitiva de bienes vinculados con una conducta punible.')),
    ('c16_no_confundir', 'carton', 355.9, 368.4, cita(
        'El comiso no debe confundirse con una medida cautelar para indemnizar a las víctimas: '
        'responden a finalidades jurídicas distintas.')),
    ('c17_mod5', 'carton', 376.2, 383.5, c_ante(
        'Quinta modalidad', 'Bienes para la extinción del derecho de dominio')),
    ('m04_naturaleza', 'mg_lista', 389.5, 399.2, lista(
        'Una acción',
        ('libro_ley', 'Constitucional', 392.5),
        ('casa_lote', 'Real', 394.2),
        ('billete', 'Patrimonial', 395.2),
        ('bifurcacion', 'Autónoma frente al proceso penal', 396.9))),
    ('c18_ley1708', 'carton', 399.8, 410.6, c_tit(
        'Ley 1708 de 2014',
        'Su aplicación exige verificar las causales y los procedimientos específicos de este '
        'régimen.')),
    ('m05_medidas', 'mg_lista', 416.8, 433.3, lista(
        'Dos clases de medidas',
        ('candado', 'Materiales: la tenencia física del bien', 419.8),
        ('libro_ley', 'Jurídicas: su situación jurídica o su disposición', 425.6))),
    ('c19_aprehension', 'carton', 434.0, 442.0, cita(
        'La afectación de un activo no siempre requiere su aprehensión material.')),
    ('c20_estandares', 'carton', 444.4, 453.2, c_ante(
        'Otro aprendizaje fundamental', 'Los estándares probatorios y las cargas argumentativas')),
    ('c21_no_basta', 'carton', 462.6, 475.3, cita(
        'La simple indagación o investigación penal no constituye por sí misma un fundamento '
        'suficiente para afectar patrimonialmente un bien.')),
    ('c22_respaldo', 'carton', 477.7, 488.6, cita(
        'Toda intervención debe estar respaldada por elementos fácticos, jurídicos y probatorios '
        'que justifiquen la medida.')),
    ('c23_hipotesis', 'carton', 489.3, 500.9, c_tit(
        'Hipótesis patrimoniales verificables',
        'Y relaciones jurídicamente relevantes entre los activos y los hechos investigados.')),
    ('c24_terceros', 'carton', 502.4, 517.1, c_tit(
        'Víctimas y terceros',
        'La eficacia de la investigación debe armonizarse con el debido proceso, el derecho de '
        'propiedad y los intereses legítimos sobre los bienes.')),
    ('m06_trazabilidad', 'mg_lista', 525.8, 536.2, lista(
        'Reconstruir el activo',
        ('ruta', 'Su origen y su titularidad', 528.8),
        ('ciclo', 'Su circulación y transformación', 531.3),
        ('lupa_doc', 'Su destinación', 534.2))),
    ('c25_conclusion_u1', 'carton', 537.6, 551.9, c_tit(
        'Conclusión de la unidad 1',
        'La correcta intervención sobre un bien comienza por identificar su función jurídica y la '
        'finalidad legítima de la actuación estatal.')),
    ('c26_base', 'carton', 552.6, 562.8, cita(
        'Es la base para seleccionar las medidas procedentes y evitar afectaciones patrimoniales '
        'injustificadas.')),

    # ---------------------------------------------------------------- unidad 2
    ('c27_u2', 'carton', 564.2, 569.4, c_ante('Unidad 2', 'Medidas cautelares con fines de reparación')),
    ('c28_preservar', 'carton', 569.6, 581.6, cita(
        'La investigación penal también debe preservar los bienes que puedan responder por los '
        'perjuicios ocasionados a las víctimas.')),
    ('c29_importancia', 'carton', 598.8, 612.0, c_tit(
        'Su importancia',
        'Evitar la transferencia, el ocultamiento o la disminución de los activos que podrían '
        'satisfacer obligaciones indemnizatorias.')),
    ('m07_armonizar', 'mg_lista', 624.9, 642.1, lista(
        'Intereses a armonizar',
        ('casa_lote', 'La propiedad privada (art. 58 de la Constitución)', 627.9),
        ('escudo', 'Los derechos de las víctimas', 635.9))),
    ('c30_ley906', 'carton', 651.2, 660.9, c_tit(
        'Ley 906 de 2004, artículos 92 a 100',
        'Y sus diferencias frente al sistema de la Ley 600 de 2000.')),
    ('c31_juez', 'carton', 675.4, 689.4, c_tit(
        'Juez de control de garantías',
        'En la Ley 906 impone el embargo y el secuestro con fines de reparación. La Fiscalía '
        'construye el soporte y acude ante él.')),
    ('c32_no_autoriza', 'carton', 703.9, 710.9, cita(
        'Identificar bienes de una persona investigada no autoriza su afectación.')),
    ('m08_necesario', 'mg_lista', 711.5, 722.9, lista(
        None,
        ('lupa_doc', 'Individualizar los activos', 713.4),
        ('mano_corazon', 'Establecer la finalidad indemnizatoria', 715.6),
        ('doc_check', 'Verificar las circunstancias que justifican la solicitud', 718.5))),
    ('m09_criterios', 'mg_lista', 723.0, 733.5, lista(
        'Tres criterios',
        ('balanza', 'Necesidad', 725.0),
        ('engranaje', 'Adecuación', 726.3),
        ('reloj_arena', 'Proporcionalidad', 727.5))),
    ('c33_estafa', 'carton', 742.5, 756.2, c_tit(
        'Una investigación por estafa',
        'Antes de afectar inmuebles y vehículos se examinan la cuantía de los perjuicios y la '
        'situación jurídica de los bienes.')),
    ('c34_indiscriminadas', 'carton', 763.4, 768.9, cita(
        'La reparación no autoriza restricciones patrimoniales indiscriminadas.')),
    ('m10_embargo', 'mg_lista', 771.0, 788.7, lista(
        'Embargo y secuestro',
        ('libro_ley', 'Embargo: restringe la disposición', 774.0),
        ('candado', 'Secuestro: tenencia, custodia o administración', 781.2))),
    ('c35_provisional', 'carton', 794.3, 807.2, c_tit(
        'Medidas provisionales',
        'Pueden modificarse, reducirse, sustituirse o levantarse: su permanencia depende de que '
        'subsistan sus presupuestos.')),
    ('c36_reparacion', 'carton', 822.5, 835.5, cita(
        'Una reparación integral efectiva también requiere mecanismos jurídicos que preserven los '
        'bienes destinados a responder patrimonialmente.')),
    ('c37_buena_fe', 'carton', 839.5, 850.0, cita(
        'Con respeto por el debido proceso y los derechos legítimos de propietarios y terceros de '
        'buena fe, exentos de culpa.')),
    ('c38_ley975', 'carton', 851.3, 861.0, c_tit(
        'Ley 975 de 2005',
        'Un régimen especial para los bienes destinados a la reparación de las víctimas.')),
    ('c39_conclusion_u2', 'carton', 864.2, 879.4, c_tit(
        'Conclusión de la unidad 2',
        'Las medidas cautelares preservan los derechos patrimoniales de las víctimas, pero exigen '
        'una justificación jurídica y probatoria suficiente.')),
    ('m11_solicitud', 'mg_lista', 892.6, 907.0, lista(
        'Una solicitud explica',
        ('balanza', 'Por qué la medida es procedente', 895.6),
        ('ojo', 'Qué finalidad persigue', 900.2),
        ('escudo', 'Qué garantías deben observarse', 903.2))),

    # ---------------------------------------------------------------- unidad 3
    ('c40_u3', 'carton', 909.0, 917.1, c_ante(
        'Unidad 3', 'Medidas cautelares con fines de comiso y administración de bienes')),
    ('c41_comiso', 'carton', 925.1, 935.8, c_tit(
        'Más allá de la reparación',
        'Actuaciones para asegurar bienes respecto de los cuales podría proceder el comiso.')),
    ('m12_medidas_u3', 'mg_lista', 949.5, 975.6, lista(
        None,
        ('mano_corazon', 'Incautación: muebles o recursos', 950.5),
        ('casa_lote', 'Ocupación: inmuebles', 960.3),
        ('candado', 'Suspensión del poder dispositivo: restricción jurídica', 969.0))),
    ('c42_vehiculo', 'carton', 983.2, 995.3, c_tit(
        'Un vehículo usado en el delito',
        'Podrá examinarse su incautación con fines de comiso, si se satisfacen los presupuestos '
        'legales.')),
    ('c43_control', 'carton', 1018.0, 1032.3, c_tit(
        'Control judicial de legalidad',
        'Artículo 84 de la Ley 906: dentro de las 36 horas siguientes a la incautación u ocupación, '
        'el fiscal comparece ante el juez.')),
    ('c44_no_termina', 'carton', 1053.0, 1067.3, c_tit(
        'Entrega y puesta a disposición',
        'La intervención no termina al aprehender un activo: surgen deberes de identificación, '
        'documentación, entrega y conservación.')),
    ('c45_documentar', 'carton', 1074.5, 1091.0, cita(
        'Al incautar un vehículo se documentan sus características, identificación, estado de '
        'conservación y demás circunstancias de la diligencia. Así se mantiene la trazabilidad del '
        'activo.')),
    ('c46_administracion', 'carton', 1110.3, 1124.0, c_tit(
        'Administración provisional',
        'Los bienes afectados pueden deteriorarse, depreciarse o generar gastos considerables si no '
        'se adoptan medidas oportunas.')),
    ('c47_almacenamiento', 'carton', 1162.4, 1175.6, c_tit(
        'No es simple almacenamiento',
        'Comprende la conservación, el seguimiento y el tratamiento de los activos, conforme con las '
        'competencias de ley.')),
    ('c48_ley1615', 'carton', 1182.5, 1193.5, c_tit(
        'Ley 1615 de 2013',
        'El Fondo Especial para la Administración de Bienes de la Fiscalía General de la Nación '
        '(FEAB).')),
    ('m13_funciones', 'mg_lista', 1213.7, 1229.8, lista(
        'Funciones distintas',
        ('lupa_doc', 'Almacenes de evidencia: preservación probatoria', 1216.7),
        ('finanzas', 'FEAB: administración patrimonial', 1223.3))),
    ('c49_informacion', 'carton', 1240.3, 1252.6, cita(
        'La coordinación exige información suficiente y verificable sobre la identidad, el estado y '
        'la situación jurídica de los bienes.')),
    ('c50_conclusion_u3', 'carton', 1263.0, 1278.9, c_tit(
        'Conclusión de la unidad 3',
        'La intervención no termina con la incautación, la ocupación o la suspensión: exige la '
        'conservación, administración y destinación legal de los bienes.')),

    # ---------------------------------------------------------------- unidad 4
    ('c51_u4', 'carton', 1284.6, 1292.6, c_ante(
        'Unidad 4', 'Medidas cautelares con fines de extinción del derecho de dominio')),
    ('c52_art34', 'carton', 1303.9, 1312.7, c_tit(
        'Artículo 34 de la Constitución',
        'Su regulación principal está en la Ley 1708 de 2014.')),
    ('c53_autonomia', 'carton', 1313.9, 1323.6, c_tit(
        'Autonomía frente al proceso penal',
        'Su ejercicio no depende de una sentencia penal condenatoria.')),
    ('c54_absolucion', 'carton', 1328.4, 1339.9, cita(
        'Una absolución por insuficiencia de pruebas no determina automáticamente la improcedencia '
        'de la extinción de dominio.')),
    ('m14_causales', 'mg_lista', 1353.8, 1367.7, lista(
        'Causales del artículo 16',
        ('ruta', 'El origen ilícito de los bienes', 1356.8),
        ('engranaje', 'Su utilización o destinación ilícita', 1358.8),
        ('lista', 'Otras previstas por el legislador', 1363.5))),
    ('m15_causal', 'mg_lista', 1371.5, 1391.1, lista(
        'Identificar la causal',
        ('billete', 'Origen: comprado con recursos ilícitos', 1374.5),
        ('casa_lote', 'Destinación: lícito, pero usado como instrumento', 1383.4))),
    ('c55_hipotesis', 'carton', 1408.4, 1422.1, cita(
        'Identificar un activo de una persona investigada no demuestra la causal: hace falta una '
        'hipótesis patrimonial sustentada en pruebas verificables.')),
    ('m16_herramientas', 'mg_lista', 1424.2, 1440.4, lista(
        None,
        ('ruta', 'Trazabilidad financiera', 1426.4),
        ('lupa_doc', 'Análisis de operaciones comerciales', 1428.2),
        ('lupa_persona', 'Identificación de titulares reales', 1430.3),
        ('ciclo', 'Reconstrucción de movimientos patrimoniales', 1433.1))),
    ('c56_buena_fe', 'carton', 1445.9, 1459.4, c_tit(
        'Terceros de buena fe, exentos de culpa',
        'Una investigación patrimonial no autoriza a desconocer los derechos de quienes adquirieron '
        'legítimamente.')),
    ('m17_cautelares', 'mg_lista', 1481.0, 1491.2, lista(
        None,
        ('candado', 'Suspensión del poder dispositivo', 1482.0),
        ('libro_ley', 'Embargo', 1484.1),
        ('mano_corazon', 'Secuestro', 1485.0),
        ('edificio', 'Toma de posesión de bienes, haberes y negocios', 1486.1))),
    ('c57_control', 'carton', 1502.5, 1514.4, c_tit(
        'Artículos 111 a 113 de la Ley 1708',
        'El control judicial de legalidad: una garantía frente a las restricciones patrimoniales.')),
    ('c58_sae', 'carton', 1528.4, 1538.7, c_tit(
        'SAE y FRISCO',
        'La Sociedad de Activos Especiales administra el FRISCO, una estructura distinta del FEAB.')),
    ('c59_terminacion', 'carton', 1550.3, 1562.9, c_tit(
        'Terminación anticipada',
        'Sentencia anticipada y negociación patrimonial, dentro de los requisitos, límites y '
        'controles del legislador.')),
    ('c60_conclusion_u4', 'carton', 1581.3, 1596.7, c_tit(
        'Conclusión de la unidad 4',
        'La extinción de dominio es autónoma: exige identificar la causal, construir el soporte '
        'probatorio y respetar a terceros y garantías judiciales.')),
    ('c61_estado', 'carton', 1607.6, 1618.5, c_tit(
        'Estado social y democrático de derecho',
        'Están en juego garantías como la propiedad privada y el debido proceso.')),

    # ---------------------------------------------------------------- ejercicio
    ('c62_ejercicio', 'carton', 1634.1, 1640.6, c_ante(
        'Ejercicio práctico', 'Integrar las cuatro unidades')),
    ('c63_caso', 'carton', 1651.9, 1662.6, c_tit(
        'El caso',
        'Una organización criminal dedicada a la estafa y al lavado de activos. Se identifican '
        'varios bienes.')),
    ('m18_bienes', 'mg_lista', 1675.3, 1737.2, lista(
        None,
        ('vehiculo', 'Un vehículo', 1675.3),
        ('casa_lote', 'Un inmueble cuestionado', 1689.4),
        ('billete', 'Una cuenta bancaria', 1706.2),
        ('casa_lote', 'Un inmueble lícito', 1717.4),
        ('finanzas', 'Una sociedad comercial', 1731.2))),
    ('c64_p1', 'carton', 1746.9, 1755.4, c_ante(
        'Primera pregunta', '¿Todos los bienes deben recibir el mismo tratamiento jurídico?')),
    ('c65_funcion', 'carton', 1755.6, 1763.6, cita(
        'Hay que identificar individualmente la función jurídica de cada activo.')),
    ('m19_funciones', 'mg_lista', 1764.1, 1804.4, lista(
        None,
        ('vehiculo', 'Vehículo: prueba o comiso', 1764.1),
        ('billete', 'Cuenta: información y recursos', 1773.9),
        ('casa_lote', 'Inmueble lícito: reparación', 1786.5),
        ('libro_ley', 'Origen o destino ilícito: extinción', 1797.7))),
    ('c66_antes', 'carton', 1808.4, 1816.3, cita(
        'La función del bien debe identificarse antes de seleccionar la medida.')),
    ('c67_p2', 'carton', 1820.0, 1829.2, c_ante(
        'Segunda pregunta',
        '¿Qué actuaciones garantizan los derechos patrimoniales de las víctimas?')),
    ('m20_p2', 'mg_lista', 1839.6, 1858.0, lista(
        None,
        ('lupa_doc', 'Identificar los activos', 1840.8),
        ('balanza', 'Estimar los perjuicios', 1843.4),
        ('doc_check', 'Verificar los presupuestos', 1846.2),
        ('mazo', 'Acudir ante el juez competente', 1851.7))),
    ('c68_no_exige', 'carton', 1860.8, 1870.5, cita(
        'La reparación no exige demostrar que todos los bienes se adquirieron con recursos del '
        'delito.')),
    ('c69_p3', 'carton', 1881.5, 1889.8, c_ante(
        'Tercera pregunta', '¿Y si el vehículo fue instrumento de la conducta delictiva?')),
    ('c70_p3_resp', 'carton', 1894.7, 1908.7, cita(
        'Verificar los presupuestos legales, decidir si corresponde una intervención material o '
        'jurídica y observar los procedimientos y controles judiciales.')),
    ('c71_estado_vehiculo', 'carton', 1918.6, 1930.7, cita(
        'Documentar el estado del vehículo, sus características y la intervención, y prever su '
        'entrega, conservación y administración.')),
    ('c72_p4', 'carton', 1939.4, 1948.4, c_ante(
        'Cuarta pregunta', '¿Qué se hace con los bienes mientras se define su situación jurídica?')),
    ('m21_p4', 'mg_lista', 1952.9, 1996.5, lista(
        None,
        ('bifurcacion', 'Sin confundir prueba y administración', 1952.9),
        ('finanzas', 'FEAB, según su régimen legal', 1964.7),
        ('edificio', 'SAE y FRISCO, en extinción de dominio', 1976.4),
        ('escudo', 'Conservar y evitar deterioros', 1990.3))),
    ('c73_p5', 'carton', 2002.4, 2012.2, c_ante(
        'Quinta pregunta',
        '¿Las operaciones cuestionadas permiten declarar automáticamente la extinción?',
        'No.')),
    ('c74_p5_resp', 'carton', 2014.1, 2027.7, c_tit(
        'Una causal legal y su prueba',
        'Las inconsistencias patrimoniales orientan la investigación, pero no sustituyen la '
        'acreditación de los presupuestos.')),
    ('c75_nexo', 'carton', 2038.9, 2048.3, cita(
        'Reconstruir las operaciones, examinar la titularidad real y verificar el nexo de ilicitud.')),
    ('c76_p6', 'carton', 2054.9, 2063.6, c_ante(
        'Sexta pregunta', '¿Y si un tercero afirma haber adquirido legítimamente el inmueble?')),
    ('c77_p6_resp', 'carton', 2068.8, 2083.1, cita(
        'Examinar la adquisición, la titularidad y la utilización del activo, con contradicción, '
        'defensa y respeto por los terceros de buena fe, exentos de culpa.')),
    ('c78_p7', 'carton', 2098.3, 2106.1, c_ante(
        'Séptima pregunta', '¿Qué importancia tiene la coordinación institucional?')),
    ('m22_roles', 'mg_lista', 2119.0, 2140.7, lista(
        None,
        ('mazo', 'Fiscales: orientan jurídicamente', 2119.0),
        ('lupa_persona', 'Policía judicial: investiga y documenta', 2124.5),
        ('carpeta', 'Asistentes: organizan y hacen seguimiento', 2133.5))),
    ('c79_articulada', 'carton', 2143.4, 2150.6, cita(
        'La calidad de la intervención depende de que estas funciones se articulen.')),
    ('m23_metodo', 'mg_lista', 2169.9, 2186.9, lista(
        None,
        ('lupa_doc', 'Identificar cada activo', 2170.9),
        ('ruta', 'Su relación con los hechos', 2173.5),
        ('balanza', 'Su función jurídica', 2176.5),
        ('doc_check', 'El soporte probatorio', 2178.7),
        ('mazo', 'La actuación procedente', 2180.9))),

    # ---------------------------------------------------------------- competencias
    ('a01_comp1', 'mg_act', 2200.9, 2214.6, act(
        'ojo', 'Competencia 1', None,
        'Determinar la función jurídica de los bienes: prueba, objeto material, reparación, comiso '
        'o extinción de dominio.')),
    ('a02_comp2', 'mg_act', 2227.4, 2239.2, act(
        'ruta', 'Competencia 2', None,
        'Identificar, analizar y sustentar la relación entre los bienes y los hechos investigados.')),
    ('a03_comp3', 'mg_act', 2249.9, 2261.2, act(
        'balanza', 'Competencia 3', None,
        'Los presupuestos jurídicos y probatorios de las medidas de afectación patrimonial.')),
    ('a04_comp4', 'mg_act', 2269.5, 2278.9, act(
        'casa_lote', 'Competencia 4', None,
        'La conservación y administración de los bienes afectados.')),
    ('a05_transversal', 'mg_act', 2294.6, 2303.8, act(
        'escudo', 'Competencia transversal', None,
        'La protección de los derechos fundamentales.')),

    # ---------------------------------------------------------------- recomendaciones
    ('m24_recom_a', 'mg_lista', 2322.3, 2343.8, lista(
        'Recomendaciones',
        ('candado', 'Evitar afectaciones automáticas', 2325.3),
        ('bifurcacion', 'Diferenciar siempre la finalidad', 2337.3))),
    ('m25_recom_b', 'mg_lista', 2354.9, 2396.8, lista(
        None,
        ('lupa_doc', 'Fortalecer la argumentación probatoria', 2354.9),
        ('doc_check', 'Documentar las actuaciones', 2371.2),
        ('apreton', 'Coordinación institucional efectiva', 2390.1))),
    ('c80_eficacia', 'carton', 2406.9, 2421.2, c_tit(
        'La eficacia institucional',
        'No se mide solo por la cantidad o el valor de los bienes afectados, sino por la legalidad, '
        'la prueba y la protección de derechos.')),

    # ---------------------------------------------------------------- cierre
    ('m26_metodologia', 'mg_lista', 2452.2, 2486.9, lista(
        None,
        ('lupa_doc', 'El activo y los hechos', 2452.2),
        ('balanza', 'Función, prueba y finalidad', 2460.1),
        ('mazo', 'Medida, competencias y controles', 2468.8),
        ('casa_lote', 'Conservación y destinación', 2479.7))),
    # 2492,4–2507,9: el corte y el plano cerrado, sin gráficos
    ('c81_consiste', 'carton', 2508.2, 2520.8, c_tit(
        'La adecuada intervención patrimonial',
        'Consiste en decisiones jurídicamente fundamentadas, probatoriamente sustentadas y '
        'orientadas a fines legítimos.')),
    ('c82_compatibles', 'carton', 2521.4, 2534.0, cita(
        'La protección de las víctimas, la eficacia de la persecución penal y las garantías '
        'constitucionales no son objetivos incompatibles.')),
    ('c83_detras', 'carton', 2558.5, 2568.2, cita(
        'Detrás de cada actuación patrimonial hay derechos, intereses legítimos y responsabilidades '
        'institucionales.')),
    ('m27_eficaz', 'mg_lista', 2568.3, 2582.4, lista(
        None,
        ('libro_ley', 'Conocimiento normativo', 2572.1),
        ('balanza', 'Criterio jurídico', 2574.5),
        ('lupa_doc', 'Rigor probatorio', 2576.2),
        ('apreton', 'Coordinación institucional', 2577.7),
        ('escudo', 'Respeto por las garantías', 2579.9))),
    ('lt02', 'lt', 2582.6, 2590.2, PROFE),
    ('c84_exitos', 'carton', 2590.4, 2597.3, cita(
        'Les deseo muchos éxitos en el ejercicio de sus funciones.')),
]
