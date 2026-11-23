# -*- coding: utf-8 -*-
"""Inventario de videos de profe a cámara (18 nov 2026). Una fila por pieza, con la versión vigente.
Las filas salen de los manifiestos de subtítulos y de los README del repo; los enlaces, de los id de Drive."""
import json, re, os
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'cursos')) + '/'
V = 'https://drive.google.com/file/d/%s/view'
C = 'https://drive.google.com/drive/folders/%s'

def man(curso):
    return {x['nombre']: x for x in json.load(open(R + curso + '/subtitulos/manifiesto.json', encoding='utf-8'))}

def tabla(curso):
    """nombre -> (subtítulos, dura, srt_id) de la tabla del README de subtítulos."""
    out = {}
    for l in open(R + curso + '/subtitulos/README.md', encoding='utf-8'):
        m = re.match(r"\| `([^`]+)`[^|]*\| (\d+) \| ([\d:]+) \| `([^`]+)`", l)
        if m:
            out[m.group(1)] = (int(m.group(2)), m.group(3), m.group(4))
    return out

DUR = {x['nombre']: x['dur'] for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'duraciones.json'), encoding='utf-8'))}

def mmss(s):
    s = int(round(s)); return '%d:%02d' % (s // 60, s % 60)

F = []
def fila(pri, curso, unidad, pieza, profe, archivo, vid, dur, srt=None, carpeta=None, grafica='Completa', fecha='', nota='',
         estado='Entregado', n_srt=None):
    F.append(dict(pri=pri, curso=curso, unidad=unidad, pieza=pieza, profe=profe, archivo=archivo, vid=vid, dur=dur, srt=srt,
                  carpeta=carpeta, grafica=grafica, fecha=fecha, nota=nota, estado=estado, n_srt=n_srt))

PROV = 'Provisional: sin gráficos en el cuerpo'

# ---------- Prioridad 1 · SRPA
CUR = 'Sistema de responsabilidad penal para adolescentes y justicia restaurativa'
M, T = man('srpa-justicia-restaurativa'), tabla('srpa-justicia-restaurativa')
EST, CH = 'Estanislao Escalante Barreto', 'Carlos Humberto Ramírez Romero'
for nombre, uni, pieza, profe, graf, fecha, nota in [
    ('srpa - CURSO - PRESENTACION-v2', 'Curso', 'Presentación del curso', EST, 'Completa', '13 nov', ''),
    ('srpa - U1 - BIENVENIDA-v2', 'Unidad 1', 'Presentación de la unidad', EST, 'Completa', '11 nov (aprox.)', 'El video está en .mov (anterior a la regla de entregar en MP4).'),
    ('srpa - U1 - CIERRE-v1', 'Unidad 1', 'Cierre de la unidad', EST, 'Completa', '17 nov', 'Del 5:45 al 13:49 el profe comparte una lámina; va a cuadro completo.'),
    ('srpa - U3 - BIENVENIDA-v2', 'Unidad 3', 'Presentación de la unidad', CH, 'Completa', '11 nov (aprox.)', 'El video está en .mov.'),
    ('srpa - U3 - DESARROLLO-v2', 'Unidad 3', 'Desarrollo (clase completa)', CH, 'Completa', '11 nov (aprox.)', 'El video está en .mov. La ficha no lo pide; vino en la carpeta y se hizo igual.'),
    ('srpa - U3 - CIERRE-v2', 'Unidad 3', 'Cierre de la unidad', CH, 'Completa', '11 nov (aprox.)', 'El video está en .mov.'),
    ('srpa - U4 - INICIO-v1', 'Unidad 4', 'Presentación de la unidad', CH, 'Completa', '17 nov', 'Son los primeros 1:57 de la grabación; el resto es la clase.'),
    ('srpa - U4 - DESARROLLO-v1', 'Unidad 4', 'Desarrollo (clase completa)', CH, 'Completa', '17 nov', 'La ficha no lo pide; vino en la misma grabación que la presentación.'),
    ('srpa - U4 - CIERRE-v2', 'Unidad 4', 'Cierre de la unidad', CH, 'Completa', '11 nov (aprox.)', 'El video está en .mov.'),
    ('srpa - U5 - INICIO-v1', 'Unidad 5', 'Presentación de la unidad', CH, 'Completa', '17 nov', 'Son los primeros 1:54 de la grabación; el resto es la clase.'),
    ('srpa - U5 - DESARROLLO-v1', 'Unidad 5', 'Desarrollo (clase completa)', CH, PROV, '17 nov', 'La ficha no lo pide; vino en la misma grabación que la presentación.'),
    ('srpa - U5 - CIERRE-v2', 'Unidad 5', 'Cierre de la unidad', CH, 'Completa', '11 nov (aprox.)', 'El video está en .mov.'),
    ('srpa - CURSO - CIERRE-v1', 'Curso', 'Cierre del curso', EST, 'Completa', '13 nov', ''),
]:
    m, t = M[nombre], T[nombre]
    fila(1, CUR, uni, pieza, profe, nombre, m['video_id'], t[1], t[2], m['carpeta'], graf, fecha, nota, n_srt=t[0])
for pieza, fuente in [('Presentación de la unidad', 'Unidad 2 - presentacion.mp4'), ('Cierre de la unidad (partes A y B)', 'Unidad 2 - A.mp4 y Unidad 2 - B.mp4')]:
    fila(1, CUR, 'Unidad 2', pieza, 'Sin identificar (no dice su nombre)', fuente + ' (grabación sin producir)', None, '', None, None, '', '',
         'En pausa desde el 17 nov: está grabada contra una pared blanca, sin el fondo de la serie, y se espera otra grabación.',
         estado='En pausa: llegará otra grabación')

# ---------- Prioridad 1 · Terminaciones anticipadas
CUR = 'Terminaciones anticipadas del proceso penal'
M, T = man('terminaciones-anticipadas'), tabla('terminaciones-anticipadas')
JD = 'Juan David Peña Gómez'
for nombre, uni, pieza, graf, fecha, nota in [
    ('terminacionesanticipadas - CURSO - INICIO-v1', 'Curso', 'Inicio del curso', 'Completa', '17 nov', ''),
    ('terminacionesanticipadas - U1 - INICIO-v1', 'Unidad 1', 'Inicio de la unidad', PROV, '17 nov', ''),
    ('terminacionesanticipadas - U1 - CIERRE-v1', 'Unidad 1', 'Cierre de la unidad', PROV, '17 nov', ''),
    ('terminacionesanticipadas - U2 - INICIO-v2', 'Unidad 2', 'Inicio de la unidad', PROV, '18 nov', 'La v2 quita la toma repetida del principio; la v1 sigue en la carpeta.'),
    ('terminacionesanticipadas - U2 - CIERRE-v1', 'Unidad 2', 'Cierre de la unidad', PROV, '17 nov', ''),
    ('terminacionesanticipadas - U3 - INICIO-v1', 'Unidad 3', 'Inicio de la unidad', PROV, '17 nov', ''),
    ('terminacionesanticipadas - U3 - CIERRE-v1', 'Unidad 3', 'Cierre de la unidad', PROV, '17 nov', ''),
    ('terminacionesanticipadas - U4 - INICIO-v2', 'Unidad 4', 'Inicio de la unidad', PROV, '18 nov', 'La v2 quita el párrafo repetido (corte directo en 0:55); la v1 sigue en la carpeta.'),
    ('terminacionesanticipadas - U4 - CIERRE-v2', 'Unidad 4', 'Cierre de la unidad', PROV, '18 nov', 'La v2 quita el arranque en falso del principio; la v1 sigue en la carpeta.'),
    ('terminacionesanticipadas - CURSO - CIERRE-v1', 'Curso', 'Cierre del curso', 'Completa', '17 nov', ''),
]:
    m, t = M[nombre], T[nombre]
    fila(1, CUR, uni, pieza, JD, nombre, m['video_id'], t[1], t[2], m['carpeta'], graf, fecha, nota, n_srt=t[0])

# ---------- Prioridad 1 · Bienes
CUR = 'Bienes en el proceso penal'
M, T = man('bienes-proceso-penal'), tabla('bienes-proceso-penal')
SL = 'Sergio Andrés López Zamora'
fila(1, CUR, 'Curso', 'Introducción al curso', SL, 'bienes - CURSO - INTRODUCCION-v1', '1Lw6GFHitCzgpz92BNr5xUpgIN7c56o6Y',
     mmss(DUR['bienes - CURSO - INTRODUCCION-v1.mp4']), T['bienes - CURSO - INTRODUCCION-v1'][2], '1dyVsM9n4SkDRWIwzj4YGvsjNly4OW2qw', 'Completa', '14 nov', '',
     n_srt=T['bienes - CURSO - INTRODUCCION-v1'][0])
for nombre, uni, pieza, nota, fecha in [
    ('bienes - U1 - INICIO-v1', 'Unidad 1', 'Inicio de la unidad', '', '17 nov'),
    ('bienes - U1 - CIERRE-v1', 'Unidad 1', 'Cierre de la unidad', 'Tiene «repito» del profe que se dejaron (decisión del 18 nov).', '17 nov'),
    ('bienes - U2 - INICIO-v2', 'Unidad 2', 'Inicio de la unidad', 'La v2 quita la toma repetida; la v1 sigue en la carpeta.', '18 nov'),
    ('bienes - U2 - CIERRE-v1', 'Unidad 2', 'Cierre de la unidad', 'Tiene «repito» del profe que se dejaron.', '17 nov'),
    ('bienes - U3 - INICIO-v1', 'Unidad 3', 'Inicio de la unidad', '', '17 nov'),
    ('bienes - U3 - CIERRE-v1', 'Unidad 3', 'Cierre de la unidad', '', '17 nov'),
    ('bienes - U4 - INICIO-v1', 'Unidad 4', 'Inicio de la unidad', '', '17 nov'),
    ('bienes - U4 - CIERRE-v1', 'Unidad 4', 'Cierre de la unidad', 'Tiene «repito» del profe que se dejaron.', '17 nov'),
]:
    m, t = M[nombre], T[nombre]
    fila(1, CUR, uni, pieza, SL, nombre, m['video_id'], t[1], t[2], m['carpeta'], PROV, fecha, nota, n_srt=t[0])
fila(1, CUR, 'Curso', 'Cierre del curso', SL, 'bienes - CURSO - CIERRE-v1', '1q0bBsu_6uuhyh1K0faHRpUoIrtt02ORm',
     mmss(DUR['bienes - CURSO - CIERRE-v1.mp4']), T['bienes - CURSO - CIERRE-v1'][2], '13q_woiBdN6fQlOvThAGXzUtvGJ8YxTey', 'Completa', '14 nov',
     'Lleva un corte donde el profe vuelve a empezar una frase. Dice «inmueble adquirido ilícitamente» (23:19 y 28:54) '
     'donde por el contexto iría «lícitamente»; el .srt deja lo que dice.', n_srt=T['bienes - CURSO - CIERRE-v1'][0])

# ---------- Prioridad 1 · Justicia restaurativa
CUR = 'Justicia restaurativa en la práctica del fiscal'
M, T = man('justicia_restaurativa'), tabla('justicia_restaurativa')
VM, VJM, VJ = 'Víctor Hugo Ospina Vargas y Martín Posada Martínez', 'Víctor Hugo Ospina Vargas, Martín Posada Martínez y Jhonatan Sandoval (invitado)', 'Víctor Hugo Ospina Vargas y Jhonatan Sandoval (invitado)'
JR = [
    ('justiciarestaurativa - CURSO - INICIO-v1', 'Curso', 'Inicio del curso', VM, 'Lleva un corte de 30 s donde el profesor pide repetir.'),
    ('justiciarestaurativa - U1 - INICIO-v1', 'Unidad 1', 'Inicio de la unidad', VJM, 'Sin cortes.'),
    ('justiciarestaurativa - U1 - CIERRE-v1', 'Unidad 1', 'Cierre de la unidad', VJM, 'Lleva un corte de 46 s donde un profesor se traba y vuelve a empezar.'),
    ('justiciarestaurativa - U2 - INICIO-v1', 'Unidad 2', 'Inicio de la unidad', VJ, 'Sin cortes.'),
    ('justiciarestaurativa - U2 - CIERRE-v1', 'Unidad 2', 'Cierre de la unidad', VJ, 'Lleva un corte de 19 s donde el profesor pide repetir («voy a repetir ahí porque de pronto no queda bien el corte»).'),
    ('justiciarestaurativa - U3 - INICIO-v1', 'Unidad 3', 'Inicio de la unidad', VJM, 'Lleva un corte de 14,5 s que pide el profesor («un corte, por favor»).'),
    ('justiciarestaurativa - U3 - CIERRE-v1', 'Unidad 3', 'Cierre de la unidad', VJM, 'Sin cortes.'),
    ('justiciarestaurativa - U4 - INICIO-v1', 'Unidad 4', 'Inicio de la unidad', VJM, 'Sin cortes; no entra el arranque de frase que la grabación deja cortado al final («Es un—»).'),
    ('justiciarestaurativa - U4 - CIERRE-v1', 'Unidad 4', 'Cierre de la unidad', VJM, 'Sin cortes. La grabación termina sin despedida.'),
    ('justiciarestaurativa - CURSO - CIERRE-v1', 'Curso', 'Cierre del curso', VM, ''),
]
RAYA = ' Tiene una raya negra de 1 px en el borde de arriba durante el cuerpo (viene en la grabación); pendiente decidir si sale una v2.'
for nombre, uni, pieza, profe, nota in JR:
    if nombre not in M:
        continue
    m, t = M[nombre], T[nombre]
    if nombre in ('justiciarestaurativa - CURSO - INICIO-v1', 'justiciarestaurativa - U1 - INICIO-v1', 'justiciarestaurativa - U1 - CIERRE-v1', 'justiciarestaurativa - U2 - INICIO-v1'):
        nota = (nota + RAYA).strip()
    fila(1, CUR, uni, pieza, profe, nombre, m['video_id'], t[1], t[2], m['carpeta'], PROV, '19 nov' if ('U4' in nombre or 'U2 - CIERRE' in nombre or 'U3 - CIERRE' in nombre) else '18 nov', nota, n_srt=t[0])

# ---------- Prioridad 1 · Ley 1826 (19 nov 2026: los diez de profe, recortados sobre el fondo de la Fiscalía)
CUR = 'Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado'
M, T = man('ley_1826'), tabla('ley_1826')
JC = 'Jorge Eduardo Castillo Pantoja'
FONDO = ' El profe va recortado sobre el fondo de la Fiscalía.'
for nombre, uni, pieza, nota in [
    ('ley1826 - CURSO - INICIO-v1', 'Curso', 'Inicio del curso', 'Sin cortes.'),
    ('ley1826 - U1 - INICIO-v2', 'Unidad 1', 'Inicio de la unidad', 'v2: borde del recorte difuminado (la v1 se mandó a la papelera).'),
    ('ley1826 - U1 - CIERRE-v1', 'Unidad 1', 'Cierre de la unidad', 'Sin cortes.'),
    ('ley1826 - U2 - INICIO-v1', 'Unidad 2', 'Inicio de la unidad', 'Dos cortes de palabras en falso, con tres cuadros de mezcla.'),
    ('ley1826 - U2 - CIERRE-v1', 'Unidad 2', 'Cierre de la unidad', 'Sin cortes.'),
    ('ley1826 - U3 - INICIO-v1', 'Unidad 3', 'Inicio de la unidad',
     'Sin cortes. Dice «imputabilidad» donde va «inimputabilidad» (2:30); el .srt lleva «inimputabilidad».'),
    ('ley1826 - U3 - CIERRE-v1', 'Unidad 3', 'Cierre de la unidad', 'Un corte de una palabra en falso, con tres cuadros de mezcla.'),
    ('ley1826 - U4 - INICIO-v1', 'Unidad 4', 'Inicio de la unidad', 'Un corte de una palabra en falso, tapado con 4 s de plano cerrado.'),
    ('ley1826 - U4 - CIERRE-v1', 'Unidad 4', 'Cierre de la unidad', 'Sin cortes.'),
    ('ley1826 - CURSO - CIERRE-v1', 'Curso', 'Cierre del curso', 'Sin cortes.'),
]:
    m, t = M[nombre], T[nombre]
    fila(1, CUR, uni, pieza, JC, nombre, m['video_id'], t[1], t[2], m['carpeta'], PROV, '19 nov', nota + FONDO, n_srt=t[0])

# ---------- Prioridad 1 · Audiencias preliminares (20 nov 2026: ocho grabaciones de Teams, introducción y recapitulación)
CUR = 'Audiencias preliminares y medidas de aseguramiento'
M, T = man('audiencias_preliminares'), tabla('audiencias_preliminares')
JZ = 'John Zuluaga Taborda'


def _ap_curso(suf, pieza, nota):
    """Inicio y cierre del curso: llegaron el 23 nov a la carpeta del profe («Apertura de curso», «Cierre de curso»)."""
    nombre = 'audienciaspreliminares - CURSO - %s-v1' % suf
    m, t = M[nombre], T[nombre]
    fila(1, CUR, 'Curso', pieza, JZ, nombre, m['video_id'], t[1], t[2], m['carpeta'], PROV, '23 nov', nota, n_srt=t[0])


_ap_curso('INICIO', 'Presentación del curso', 'Llegó el 23 nov («Apertura de curso», en la carpeta del profe). Sin cortes. '
          'Grabación de Teams: el rótulo de Teams con el nombre queda fuera del cuadro.')
for u in range(1, 5):
    for suf, pieza in (('INICIO', 'Inicio de la unidad'), ('CIERRE', 'Cierre de la unidad (recapitulación)')):
        nombre = 'audienciaspreliminares - U%d - %s-v1' % (u, suf)
        if nombre not in M or nombre not in T:
            continue
        m, t = M[nombre], T[nombre]
        extra = {3: ' El subtítulo dice «artículo 250 constitucional» donde él dice «ciento cincuenta».',
                 4: ' El cartón lleva el nombre de la unidad de la lista de contenidos (la ficha repite el de la U3).'}.get(u, '')
        fila(1, CUR, 'Unidad %d' % u, pieza, JZ, nombre, m['video_id'], t[1], t[2], m['carpeta'], PROV, '20 nov',
             'Sin cortes. Grabación de Teams: el rótulo de Teams con el nombre queda fuera del cuadro.' + extra, n_srt=t[0])
_ap_curso('CIERRE', 'Cierre del curso', 'Llegó el 23 nov («Cierre de curso», en la carpeta del profe; la ficha lo da como '
          'mensaje escrito). Sin cortes: el tropiezo en el nombre del curso (0:30) se queda en el video y sale del subtítulo.')

# ---------- Prioridad 2 · Derechos humanos
CUR = 'Derechos humanos aplicados a la función judicial'
M, T = man('derechos_humanos'), tabla('derechos_humanos')
YT = 'Yefri Yoel Torrado Verjel'
FALTA = {'PRIO 2 - DERECHOS HUMANOS - UNIDAD 2 CIERRE-v1': '1I_1aW3cSIjiDOYoKrr7rQpJf8HR_MKJC', 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 3 INICIO-v1': '1DVdevh-4CN7L76NSmKCFgTHET3MMNua3',
         'PRIO 2 - DERECHOS HUMANOS - UNIDAD 5 INICIO-v1': '1Rq4kFP9Kc8CtBh02c0jO_9_ngngZE7UN'}
for suf, uni, pieza, nota in [
    ('PRESENTACION DEL CURSO-v1', 'Curso', 'Presentación del curso', ''),
    ('UNIDAD 1 CIERRE-v1', 'Unidad 1', 'Cierre de la unidad', ''),
    ('UNIDAD 2 INICIO-v1', 'Unidad 2', 'Inicio de la unidad', ''),
    ('UNIDAD 2 CIERRE-v1', 'Unidad 2', 'Cierre de la unidad', ''),
    ('UNIDAD 3 INICIO-v1', 'Unidad 3', 'Inicio de la unidad', ''),
    ('UNIDAD 3 CIERRE-v1', 'Unidad 3', 'Cierre de la unidad', ''),
    ('UNIDAD 4 INICIO-v2', 'Unidad 4', 'Inicio de la unidad', 'La v2 deja más tiempo la última fila de una lista.'),
    ('UNIDAD 4 CIERRE-v1', 'Unidad 4', 'Cierre de la unidad', ''),
    ('UNIDAD 5 INICIO-v1', 'Unidad 5', 'Inicio de la unidad', ''),
    ('UNIDAD 5 CIERRE-v1', 'Unidad 5', 'Cierre de la unidad', ''),
    ('CIERRE DEL CURSO-v1', 'Curso', 'Cierre del curso', ''),
]:
    nombre = 'PRIO 2 - DERECHOS HUMANOS - ' + suf
    m, t = M[nombre], T[nombre]
    fila(2, CUR, uni, pieza, YT, nombre, m.get('video_id') or FALTA[nombre], t[1], t[2], m['carpeta'], 'Completa', '16 nov', nota, n_srt=t[0])

# ---------- Prioridad 2 · Enfoque diferencial
CUR = 'Enfoques diferenciales'
M, T = man('enfoque_diferencial'), tabla('enfoque_diferencial')
CB = 'Camilo Borrero García'
for nombre, uni, pieza in [
    ('enfoquediferencial - CURSO - INICIO-v3', 'Curso', 'Inicio del curso'),
    ('enfoquediferencial - U1 - INICIO-v2', 'Unidad 1', 'Inicio de la unidad'), ('enfoquediferencial - U1 - CIERRE-v3', 'Unidad 1', 'Cierre de la unidad (clase)'),
    ('enfoquediferencial - U2 - INICIO-v2', 'Unidad 2', 'Inicio de la unidad'), ('enfoquediferencial - U2 - CIERRE-v3', 'Unidad 2', 'Cierre de la unidad (clase)'),
    ('enfoquediferencial - U3 - INICIO-v2', 'Unidad 3', 'Inicio de la unidad'), ('enfoquediferencial - U3 - CIERRE-v3', 'Unidad 3', 'Cierre de la unidad (clase)'),
    ('enfoquediferencial - U4 - INICIO-v2', 'Unidad 4', 'Inicio de la unidad'), ('enfoquediferencial - U4 - CIERRE-v2', 'Unidad 4', 'Cierre de la unidad (clase)'),
    ('enfoquediferencial - U5 - INICIO-v2', 'Unidad 5', 'Inicio de la unidad'), ('enfoquediferencial - U5 - CIERRE-v3', 'Unidad 5', 'Cierre de la unidad (clase)'),
    ('enfoquediferencial - CURSO - CONCLUSIONES-v2', 'Curso', 'Conclusiones del curso'),
]:
    m, t = M[nombre], T[nombre]
    fila(2, CUR, uni, pieza, CB, nombre, m['video_id'], t[1], t[2], m['carpeta'], 'Completa', '15–17 nov',
         'Grabado con teléfono, en vertical; va recompuesto a 16:9.', n_srt=t[0])

# ---------- Prioridad 3 · Delitos ambientales
CUR = 'Investigación y judicialización de delitos contra el medio ambiente y los recursos naturales'
DC = 'Diana Carolina Florez Vallona'
MOV = 'El video está en .mov (anterior a la regla de entregar en MP4).'
SINPRES = ('Sin la presentación de la docente (nombre y credenciales), que queda solo en la introducción al curso '
           '(23 nov). La %s y su .srt están en VIDEOS › _anteriores.')
DA = [
    ('Curso', 'Introducción al curso', DC, 'delitosambientales - CURSO - INTRODUCCION-v1.mp4', '1_RvHWIfTUKEzUF9QeXOhy2lGtQl3sz9c', '1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_', '12 nov', ''),
    ('Unidad 1', 'Introducción a la unidad', DC, 'delitosambientales - U1 - INTRODUCCION-v4.mp4', '19z2MzFAjA5zhSzAQk980CrQ-xies1myW', '1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_', '23 nov', SINPRES % 'v3 (.mov)'),
    ('Unidad 1', 'Conversatorio: articulación DEMA y DECOC', 'Ana María Díaz González y Camilo Andrés González López', 'delitosambientales - U1 - CONVERSATORIO DEMA y DECOC-v1.mov', '1Ioh_PHsJgbXdnOidNAXdROmNNr20QWMu', '13B1FO9EgVKEwq63GuNDO8-yYnm-gXITO', '11 nov', MOV),
    ('Unidad 2', 'Introducción a la unidad', DC, 'delitosambientales - U2 - INTRODUCCION-v3.mp4', '19OwA__9qpNllhKcsShugpXe7yz8FohIL', '1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_', '23 nov', SINPRES % 'v2 (.mov)'),
    ('Unidad 3', 'Introducción a la unidad', DC, 'delitosambientales - U3 - INTRODUCCION-v3.mp4', '1AskjduHzz72ekAw1DvhwGFGTSED9Gnri', '1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_', '23 nov', SINPRES % 'v2 (.mov)'),
    ('Unidad 3', 'Entrevista: técnicas especiales de investigación', 'Jairo Porras', 'delitosambientales - U3 - ENTREVISTA TECNICAS ESPECIALES-v1.mov', '1WO2LxXUeUoGVVCK9odeqOfMr1_aJ-jl4', '1Z_7O-mlITWgInSRArm1_qqug0vqfYeGm', '11 nov', MOV),
    ('Unidad 3', 'Lección 4: investigación financiera', 'Alba Lucía Solís Ramírez', 'delitosambientales - U3 - LECCION 4-v1.mp4', '1l8o9AdVubTc3mBvKtYPuuP8b1jBOpDea', '138IERkCos3CdTH3SEjUCul6pLJ_sy5pv', '15 nov', 'La grabación venía armada con varias tomas; se quitaron dos frases repetidas.'),
    ('Unidad 3', 'Lección 5: la prueba pericial', 'Hugo Ascencio Salazar', 'delitosambientales - U3 - LECCION 5-v1.mp4', '1Hkg0kpqF8xIgFMDW2LWjeiz6bweDdMv3', '1owzhcZV_mOam7wdU9TRYJzqL45cfFb5s', '15 nov', ''),
    ('Unidad 4', 'Introducción a la unidad', DC, 'delitosambientales - U4 - INTRODUCCION-v3.mp4', '1mWGUrj4uGMRipr2LTUov9CPpBf6LO4VS', '1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_', '23 nov', SINPRES % 'v2 (.mov)'),
    ('Unidad 4', 'Lección 1: justicia restaurativa', 'Daniela Escallón', 'delitosambientales - U4 - LECCION 1-v1.mp4', '1hELVGGJV83mUYZyVRpcW6cukOqWAVHYU', '1973M2cTX9faj2KPkfbUx0Yh9tlAerfGj', '15 nov', 'Desde 15:38 la imagen va un cuadro (33 ms) detrás del sonido.'),
    ('Unidad 5', 'Introducción a la unidad', DC, 'delitosambientales - U5 - INTRODUCCION-v3.mp4', '15ZC3brxNbXay23vZupaDUxUHg0tNbUAd', '1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_', '23 nov', SINPRES % 'v2 (.mov)'),
    ('Curso', 'Cierre del curso', DC, 'delitosambientales - CURSO - CIERRE-v2.mp4', '1gSVHiOkeV9quWKgzMzQyXxv03JN_BIbs', '1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_', '23 nov', SINPRES % 'v1'),
]
T = tabla('medio-ambiente')     # subtítulos del 22 nov 2026
for uni, pieza, profe, arch, vid, carp, fecha, nota in DA:
    n = os.path.splitext(arch)[0]
    fila(3, CUR, uni, pieza, profe, n, vid, mmss(DUR[arch]), T[n][2], carp, 'Completa', fecha, nota, n_srt=T[n][0])

# ---------- Prioridad 3 · Trata
CUR = 'Investigación y judicialización de los delitos de tráfico de migrantes y trata de personas'
JM = 'José María Peláez Mejía (avatar)'
MR = 'Mariana Lisbeth Rodríguez Muñoz'
V2 = 'v2 con su rótulo de nombre (21 nov); la v1, sin rótulo, está en _anteriores.'
T = tabla('prioridad-03')     # subtítulos del 20 nov 2026
TR = {}
for l in open(R + 'prioridad-03/profe/README.md', encoding='utf-8'):
    m = re.match(r"\| `(traficoytrata - [^`]+)\.mp4` \| ([\d:]+) \|.*\| `([^`]+)` \|", l)
    if m: TR[m.group(1)] = (m.group(2), m.group(3))
for nombre, uni, pieza, profe, nota in [
    ('traficoytrata - CURSO - INICIO-v1', 'Curso', 'Bienvenida al curso', JM, ''),
    ('traficoytrata - U1 - INICIO-v1', 'Unidad 1', 'Introducción a la unidad', JM, ''),
    ('traficoytrata - U1 - RETROALIMENTACION-v1', 'Unidad 1', 'Retroalimentación de la evaluación', JM, ''),
    ('traficoytrata - U1 - CIERRE-v2', 'Unidad 1', 'Cierre de la unidad', MR, V2),
    ('traficoytrata - U2 - INICIO-v1', 'Unidad 2', 'Introducción a la unidad', JM, ''),
    ('traficoytrata - U2 - RETROALIMENTACION-v1', 'Unidad 2', 'Retroalimentación de la evaluación', JM, 'El subtítulo dice «asistencia mediata» donde el avatar dice «inmediata».'),
    ('traficoytrata - U2 - CIERRE-v2', 'Unidad 2', 'Cierre de la unidad', MR, V2 + ' La grabación termina a mitad de palabra («descartar la hipó…»).'),
    ('traficoytrata - U3 - INICIO-v1', 'Unidad 3', 'Introducción a la unidad', JM, ''),
    ('traficoytrata - U3 - RETROALIMENTACION-v1', 'Unidad 3', 'Retroalimentación de la evaluación', JM, ''),
    ('traficoytrata - U3 - CIERRE-v2', 'Unidad 3', 'Cierre de la unidad', MR, V2 + ' La grabación termina a mitad de frase («la comunicación clara de…»).'),
    ('traficoytrata - CURSO - CIERRE-v1', 'Curso', 'Cierre del curso', JM, ''),
]:
    d, vid = TR[nombre]
    extra = 'Es un avatar generado; va recortado sobre el fondo de la DAE. ' if 'avatar' in profe else ''
    n_srt, _, srt = T[nombre]
    fila(3, CUR, uni, pieza, profe, nombre, vid, d, srt, '1A3rlk8CCzw0cRq2sFEAZ_H6plaFMkq_l', PROV, '18 nov', (extra + nota).strip(), n_srt=n_srt)
# Unidades 4 y 5 (21 nov 2026): llegaron después, como zip en la carpeta VIDEOS del curso
for nombre, uni, pieza, profe, nota in [
    ('traficoytrata - U4 - INICIO-v1', 'Unidad 4', 'Introducción a la unidad', JM, ''),
    ('traficoytrata - U4 - RETROALIMENTACION-v1', 'Unidad 4', 'Retroalimentación de la evaluación', JM, ''),
    ('traficoytrata - U4 - CIERRE-v2', 'Unidad 4', 'Cierre de la unidad', MR, V2),
    ('traficoytrata - U5 - INICIO-v1', 'Unidad 5', 'Introducción a la unidad', JM, ''),
    ('traficoytrata - U5 - RETROALIMENTACION-v1', 'Unidad 5', 'Retroalimentación de la evaluación', JM, ''),
    ('traficoytrata - U5 - CIERRE-v2', 'Unidad 5', 'Cierre de la unidad', MR, V2),
]:
    d, vid = TR[nombre]
    extra = 'Es un avatar generado; va recortado sobre el fondo de la DAE. ' if 'avatar' in profe else ''
    n_srt, _, srt = T[nombre]
    fila(3, CUR, uni, pieza, profe, nombre, vid, d, srt, '1A3rlk8CCzw0cRq2sFEAZ_H6plaFMkq_l', PROV, '21 nov', (extra + nota).strip(), n_srt=n_srt)

# ---------- Prioridad 3 · Desaparición forzada (19–20 nov 2026: las 17 piezas salen de una sola grabación)
CUR = 'Investigación judicial y forense de desaparición forzada'
M, T = man('desaparicion_forzada'), tabla('desaparicion_forzada')
CV = 'Carlos Eduardo Valdés Moreno'
RETRO = 'Junta las tres retroalimentaciones que grabó el profe (actividad 1, actividad 2 y cuestionario), con seis cuadros de mezcla entre una y otra.'
DF = [('CURSO - INICIO', 'Curso', 'Inicio del curso')]
for u in range(1, 6):
    DF += [('U%d - INICIO' % u, 'Unidad %d' % u, 'Presentación de la unidad'),
           ('U%d - RETROALIMENTACION' % u, 'Unidad %d' % u, 'Retroalimentación de evaluaciones'),
           ('U%d - CIERRE' % u, 'Unidad %d' % u, 'Cierre de la unidad')]
DF += [('CURSO - CIERRE', 'Curso', 'Cierre del curso')]
NOTA_DF = {
    'U1 - CIERRE': 'Es la segunda toma: en la primera el profe dice «artículo 166» y pide repetir.',
    'U2 - INICIO': 'Un corte de 13 s donde el profe dice «Hasta ahí ese video… perdón, continúa».',
    'U5 - INICIO': 'Un corte de 3,6 s de una palabra en falso («excúsenme»).',
    'CURSO - CIERRE': 'Dura 15 min (la ficha da de 5 a 8). Un corte de 6 s de una palabra en falso («perdónenme, eh, eh»).',
}
for suf, uni, pieza in DF:
    nombre = 'desaparicionforzada - %s-v1' % suf
    if nombre not in M or nombre not in T:
        continue
    m, t = M[nombre], T[nombre]
    nota = NOTA_DF.get(suf) or (RETRO if suf.endswith('RETROALIMENTACION') else 'Sin cortes.')
    fila(3, CUR, uni, pieza, CV, nombre, m['video_id'], t[1], t[2], m['carpeta'], PROV, '19–20 nov',
         nota + ' Sale de la misma grabación que las otras 16 piezas del curso.', n_srt=t[0])

# ---------- Prioridad 3 · Derecho de petición (20 nov 2026: siete grabaciones, seis piezas; 21 nov: cuatro más, los cierres de U2 y U3 y el del curso; ver cursos/derecho_peticion/profe)
CUR = 'Derecho de petición y acción de tutela: régimen constitucional, legal y jurisprudencial para servidores públicos'
M, T = man('derecho_peticion'), tabla('derecho_peticion')
OF = 'Óscar Jairo Fonseca Fonseca'
TOMAS = ' Se sacan las tomas fallidas y lo que el profe le dice al técnico entre tomas («Suspendamos ahí, por favor»).'
for nombre, uni, pieza, nota in [
    ('derechodepeticion - CURSO - INICIO-v2', 'Curso', 'Inicio del curso', 'Dos cortes de toma y la charla del principio. La v2 lleva el rótulo al empezar (en la v1 entraba en el 1:31).'),
    ('derechodepeticion - U1 - INICIO-v1', 'Unidad 1', 'Inicio de la unidad', 'Se compone de la toma 2, en tres tramos; la toma 1 (un primer intento) no entra.'),
    ('derechodepeticion - U1 - CIERRE-v1', 'Unidad 1', 'Cierre de la unidad', 'Dos cortes de toma.'),
    ('derechodepeticion - U2 - INICIO-v1', 'Unidad 2', 'Inicio de la unidad', 'Un corte de toma.'),
    ('derechodepeticion - U3 - INICIO-v1', 'Unidad 3', 'Inicio de la unidad', 'Sin cortes adentro.'),
    ('derechodepeticion - U4 - INICIO-v1', 'Unidad 4', 'Inicio de la unidad', 'Tres cortes de toma, uno de ellos una frase que el profe pidió repetir.'),
    ('derechodepeticion - U2 - CIERRE-v1', 'Unidad 2', 'Cierre de la unidad', 'Se compone con las dos tomas (la 1 se pausa por un ruido; la 2 retoma en «Quien recibe…»). Se sacan cuatro frases que el profe repite y la charla con el técnico. El profe dice «orientar y emitir»; el subtítulo dice «remitir», como sigue el texto.'),
    ('derechodepeticion - U3 - CIERRE-v1', 'Unidad 3', 'Cierre de la unidad', 'Se sacan cinco arranques en falso que el profe anuncia y se acorta una pausa de 7,9 s.'),
    ('derechodepeticion - CURSO - CIERRE-v1', 'Curso', 'Cierre del curso', 'Se sacan dos arranques en falso que el profe anuncia («Voy a retomar desde la precisión», «retomo en esa frase»).'),
]:
    if nombre not in M or nombre not in T:
        continue
    m, t = M[nombre], T[nombre]
    nuevo = nombre.endswith(('U2 - CIERRE-v1', 'U3 - CIERRE-v1', 'CURSO - CIERRE-v1'))      # llegaron el 21 nov, con otro técnico
    fila(3, CUR, uni, pieza, OF, nombre, m['video_id'], t[1], t[2], m['carpeta'], PROV, '21 nov' if nuevo else '20 nov',
         nota + ('' if 'Sin cortes' in nota or nuevo else TOMAS), n_srt=t[0])
for uni, pieza in [('Unidad 4', 'Cierre de la unidad'),
                   ('Unidades 1 a 4', 'Retroalimentación de la evaluación')]:
    fila(3, CUR, uni, pieza, '', '(sin grabación)', None, '', None, None, '', '',
         'No llegó grabación (en E:\\DAE MASTER\\CURSO DERECHOS DE PETICION hay inicio y cierre del curso, inicios de U1 a U4 y cierres de U1 a U3).',
         estado='Sin grabación')

# ---------- Prioridad 3 · Delitos informáticos (22 nov 2026: cinco videos que el profe ya editó; ver cursos/delitos_informaticos/profe)
CUR = 'Delitos informáticos'
M, T = man('delitos_informaticos'), tabla('delitos_informaticos')
YG = 'Yefrin Garavito Navarro'
SUYO = (' Va su edición: se quitan su cartón de entrada (y el de salida, si lo trae) y la placa «DAE | FISCALÍA» que puso '
        'arriba a la derecha; quedan sus rótulos y sus láminas.')
for nombre, uni, pieza, nota in [
    ('delitosinformaticos - U3 - INICIO-v1', 'Unidad 3', 'Inicio de la unidad',
     'Sin cortes adentro. A las 5:39 dice «avance en el caso sin registrar ante su decisión»; su lámina dice «Registre su '
     'decisión antes de avanzar». Queda como se oye.'),
    ('delitosinformaticos - U3 - INTERMEDIO-v1', 'Unidad 3', 'Video intermedio (síntesis de la unidad)', 'Sin cortes adentro.'),
    ('delitosinformaticos - U4 - INICIO-v1', 'Unidad 4', 'Inicio de la unidad', 'Sin cortes adentro; sale también su cartón final.'),
    ('delitosinformaticos - U4 - INTERMEDIO-v1', 'Unidad 4', 'Video intermedio (síntesis de la unidad)',
     'Sin cortes adentro. A las 4:54 dice «describe… las máscaras de tiempo» (el subtítulo: «escribe… las marcas»); a las '
     '5:41, «condición necesaria y suficiente» (sería «necesaria pero no suficiente»): quedan como se oyen.'),
    ('delitosinformaticos - U4 - CIERRE-v1', 'Unidad 4', 'Cierre de la unidad', 'Sin cortes adentro; sale también su cartón final.'),
]:
    if nombre not in M or nombre not in T:
        continue
    m, t = M[nombre], T[nombre]
    fila(3, CUR, uni, pieza, YG, nombre, m['video_id'], t[1], t[2], m['carpeta'], 'Del profe: sus rótulos y láminas', '22 nov',
         nota + SUYO, n_srt=t[0])
for uni, pieza in [('Unidad 3', 'Cierre de la unidad'), ('Unidades 1 y 2', 'Inicio, intermedio y cierre'),
                   ('Curso', 'Presentación del curso')]:
    fila(3, CUR, uni, pieza, '', '(sin grabación)', None, '', None, None, '', '',
         'No llegó grabación (en E:\\DAE MASTER\\CURSO DELITOS INFORMATICOS están inicio e intermedio de la U3 e inicio, '
         'intermedio y cierre de la U4; los archivos van numerados 1, 2, 4, 5 y 6: falta el 3).',
         estado='Sin grabación')

# ---------- Prioridad 3 · Estándares interamericanos
fila(3, 'Estándares interamericanos de investigación de graves violaciones a los derechos humanos', 'Unidad 1', 'Inicio de la unidad', 'Sin identificar',
     'Estándares Interamericanos Unidad 1 - Inicio.mp4 (grabación sin producir)', '1Ex6HRmTnUOlVrKkXzO-TZCl-5n-ZzEgC', '5:26', None, None, '', '',
     'La calidad de imagen de la grabación no da para publicar. Está en estudio rehacerlo con un avatar (informe del 19 nov); falta la prueba de 30 s y la autorización del profesor.',
     estado='Sin producir: calidad de la grabación')
