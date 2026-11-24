# -*- coding: utf-8 -*-
"""Miniaturas SVG de la revisión de Derecho de petición, lección 1.1 (una por diapositiva + una general).

    python3 miniaturas.py <carpeta_salida>

Lienzo 400×170 (proporción del iframe 1113×448). Paleta del curso (tema-curso: marino, teal, óxido, coral,
crema, niebla, hielo). Cada miniatura lleva la etiqueta «PROPUESTA» y muestra solo la idea de distribución.
"""
import os
import sys
from xml.sax.saxutils import escape

M, T, O, C, CR, N, H, W = '#002F46', '#396B83', '#A75260', '#EE616B', '#F8F5C6', '#E5F1F1', '#F2F8F8', '#FFFFFF'
G = '#B9CACF'  # líneas de texto simuladas
F = "Poppins, 'Segoe UI', Arial, sans-serif"


class S:
    def __init__(self, clave, titulo):
        self.clave, self.titulo, self.p = clave, titulo, []

    def add(self, s):
        self.p.append(s)

    def rect(self, x, y, w, h, fill=W, stroke=None, rx=6, sw=1.2, dash=None):
        st = ' stroke="%s" stroke-width="%s"' % (stroke, sw) if stroke else ''
        if dash:
            st += ' stroke-dasharray="%s"' % dash
        self.add('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"%s/>' % (x, y, w, h, rx, fill, st))

    def text(self, x, y, s, size=9, fill=M, weight=400, anchor='start', italic=False):
        it = ' font-style="italic"' if italic else ''
        self.add('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" fill="%s" '
                 'text-anchor="%s"%s>%s</text>' % (x, y, F, size, weight, fill, anchor, it, escape(s)))

    def lines(self, x, y, w, n, gap=7, last=0.6, color=G):
        for i in range(n):
            ww = w * (last if i == n - 1 else 1)
            self.add('<rect x="%s" y="%s" width="%s" height="3" rx="1.5" fill="%s"/>' % (x, y + i * gap, ww, color))

    def chip(self, x, y, s, size=7.5, fill=W, stroke=T, color=M, weight=500):
        w = len(s) * size * 0.56 + 10
        self.rect(x, y, w, size + 7, fill, stroke, rx=(size + 7) / 2, sw=0.9)
        self.text(x + w / 2, y + size + 2.2, s, size, color, weight, 'middle')
        return w

    def arrow(self, x1, y1, x2, y2, color=T, sw=1.4):
        self.add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
                 'marker-end="url(#fl)"/>' % (x1, y1, x2, y2, color, sw))

    def line(self, x1, y1, x2, y2, color=T, sw=1.2, dash=None):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        self.add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
                 % (x1, y1, x2, y2, color, sw, d))

    def persona(self, x, y, s=1.0, color=T):
        self.add('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (x, y, 4.2 * s, color))
        self.add('<path d="M%s %s q%s -%s %s 0 v%s h-%s z" fill="%s"/>'
                 % (x - 6 * s, y + 17 * s, 6 * s, 12 * s, 12 * s, 0.01, 12 * s, color))

    def doc(self, x, y, w=16, h=20, color=T):
        self.rect(x, y, w, h, W, color, rx=2, sw=1)
        for i in range(3):
            self.add('<rect x="%s" y="%s" width="%s" height="1.6" fill="%s"/>' % (x + 3, y + 5 + i * 4, w - 6, G))

    def pdf(self, x, y, label='Descargar texto (PDF)'):
        w = len(label) * 7.5 * 0.56 + 26
        self.rect(x, y, w, 16, C, None, rx=8)
        self.add('<path d="M%s %s v6 m-3 -3 l3 3 l3 -3 M%s %s h6" stroke="%s" stroke-width="1.3" fill="none" '
                 'stroke-linecap="round"/>' % (x + 11, y + 3.5, x + 8, y + 12.5, W))
        self.text(x + 19, y + 11, label, 7.5, W, 600)
        return w

    def svg(self):
        cab = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 170" width="400" height="170">'
               '<title>%s</title><defs><marker id="fl" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" '
               'markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="%s"/></marker></defs>'
               % (escape(self.titulo), T))
        fondo = ('<rect x="1" y="1" width="398" height="168" rx="10" fill="%s" stroke="%s" stroke-width="1.5"/>'
                 % (H, T))
        tag = ('<rect x="8" y="7" width="58" height="13" rx="6.5" fill="%s"/><text x="37" y="16.5" font-family="%s" '
               'font-size="7" font-weight="700" fill="%s" text-anchor="middle" letter-spacing="0.6">PROPUESTA</text>'
               '<text x="72" y="17" font-family="%s" font-size="8.5" font-weight="600" fill="%s">%s</text>'
               % (C, F, W, F, M, escape(self.titulo)))
        return cab + fondo + tag + ''.join(self.p) + '</svg>'


def e01():
    s = S('E01', 'E01 · Objetivo de la lección')
    s.rect(14, 28, 262, 132, W, N, rx=8)
    s.text(24, 46, 'Objetivo de la lección', 11, M, 700)
    s.rect(23, 53, 52, 13, CR, None, rx=3)
    s.text(27, 63, 'Reconocer', 8.5, O, 700)
    s.lines(80, 58, 186, 1)
    s.lines(24, 72, 242, 3, last=0.75)
    x = 24
    for c in ('Naturaleza constitucional', 'Persona ⇄ autoridad', 'Derechos y ESD'):
        x += s.chip(x, 102, c, 6.4) + 4
    s.text(24, 146, 'Texto fijo, sale completo de una (sin animación)', 7.5, T, 500, italic=True)
    s.rect(286, 28, 102, 132, N, None, rx=8)
    s.persona(320, 82, 1.6, T)
    s.persona(355, 82, 1.6, O)
    s.text(337, 140, 'ilustración', 7, T, 400, 'middle', True)
    return s


def e02():
    s = S('E02', 'E02 · Mapa conceptual, no camino')
    s.rect(120, 27, 160, 32, M, None, rx=8)
    s.text(200, 41, 'Derecho de petición', 10, W, 700, 'middle')
    s.text(200, 53, 'derecho fundamental (art. 23 C.P.)', 7, CR, 500, 'middle')
    for cx in (70, 200, 330):
        s.line(200, 59, cx, 76, T, 1.2)
    nodos = (('Garantía', 'fundamental', 70), ('Doble vía', 'persona ⇄ autoridad', 200),
             ('Valores del', 'Estado social de derecho', 330))
    for a, b, cx in nodos:
        s.rect(cx - 58, 76, 116, 34, W, T, rx=7)
        s.text(cx, 90, a, 8.5, M, 700, 'middle')
        s.text(cx, 102, b, 7, T, 500, 'middle')
        s.add('<circle cx="%s" cy="76" r="5.5" fill="%s"/><text x="%s" y="79" font-family="%s" font-size="8" '
              'font-weight="700" fill="%s" text-anchor="middle">+</text>' % (cx + 52, C, cx + 52, F, W))
    x = 236
    for fila in (('dignidad', 'participación', 'igualdad'), ('buena fe', 'transparencia', 'acceso')):
        xx = 254 if fila[0] == 'buena fe' else 240
        for c in fila:
            xx += s.chip(xx, 118 + (0 if fila[0] == 'dignidad' else 15), c, 6.5) + 3
    s.text(14, 132, 'Cada nodo abre su ventana', 7.5, T, 500, italic=True)
    s.text(14, 144, 'con el texto del DI', 7.5, T, 500, italic=True)
    return s


def e03():
    s = S('E03', 'E03 · Cuatro cajas con ícono propio')
    cajas = ((14, 27), (206, 27), (14, 97), (206, 97))
    for x, y in cajas:
        s.rect(x, y, 180, 64, W, T, rx=7)
    # 1: línea de tiempo
    s.text(22, 40, '1 · El CPACA vigente', 8.5, M, 700)
    s.line(30, 60, 170, 60, T, 1.4)
    for x, a, b in ((34, '2011', 'Ley 1437 · CPACA'), (112, '2015', 'Ley 1755: arts. 13 a 33')):
        s.add('<circle cx="%s" cy="60" r="4" fill="%s"/>' % (x, C))
        s.text(x - 4, 54, a, 7.5, O, 700)
        s.text(x - 6, 73, b, 6.5, M, 500)
    s.text(22, 85, '= leer el CPACA con la 1755', 7, T, 500, italic=True)
    # 2: objeto
    s.text(214, 40, '2 · Objeto del derecho', 8.5, M, 700)
    s.chip(214, 48, 'Respuesta pronta', 7)
    s.chip(214, 64, 'completa y de fondo', 7)
    s.doc(360, 50, 18, 24, T)
    # 3: contenido manda
    s.text(22, 110, '3 · Cuenta el contenido,', 8.5, M, 700)
    s.text(22, 121, 'no el nombre', 8.5, M, 700)
    x = 22
    for c in ('queja', 'reclamo', 'solicitud', 'requerimiento'):
        x += s.chip(x, 130, c, 6.5, CR, O, O) + 3
    # 4: lista de actuaciones
    s.text(214, 110, '4 · Actuaciones (art. 13)', 8.5, M, 700)
    items = ('reconocer un derecho', 'pedir información', 'solicitar copias', 'quejas y reclamos',
             'consultas', 'recursos')
    for i, it in enumerate(items):
        cx, cy = 216 + (i % 2) * 86, 122 + (i // 2) * 11
        s.rect(cx, cy - 6, 6, 6, W, T, rx=1, sw=0.8)
        s.text(cx + 9, cy, it, 6.5, M, 500)
    return s


def e04():
    s = S('E04', 'E04 · Columnas que se abren + viñetas')
    s.rect(14, 27, 54, 132, N, T, rx=7)
    s.rect(74, 27, 54, 132, N, T, rx=7)
    for x, t in ((41, 'Mecanismo'), (101, 'Diálogo')):
        s.add('<text transform="translate(%s 93) rotate(-90)" font-family="%s" font-size="8" font-weight="700" '
              'fill="%s" text-anchor="middle">%s</text>' % (x + 3, F, M, t))
    s.rect(134, 27, 252, 132, W, T, rx=7, sw=1.6)
    s.text(146, 44, 'Una fuente de información para la Entidad', 9, M, 700)
    s.text(146, 60, 'Las peticiones revelan:', 7.5, T, 500)
    for i, it in enumerate(('barreras de acceso', 'problemas recurrentes', 'necesidades de orientación',
                            'riesgos en la atención', 'aspectos por mejorar')):
        s.add('<circle cx="152" cy="%s" r="2.2" fill="%s"/>' % (70 + i * 11, C))
        s.text(158, 73 + i * 11, it, 7.5, M, 500)
    s.rect(146, 130, 228, 20, CR, None, rx=5)
    s.text(260, 143, 'No depende de una respuesta favorable', 8, O, 700, 'middle')
    return s


def e05():
    s = S('E05', 'E05 · Dos bloques sin scroll')
    s.rect(14, 27, 182, 98, W, T, rx=7)
    s.text(24, 42, 'Se conecta con…', 9, M, 700)
    y = 50
    for fila in (('Acceso a la información', 'Debido proceso'), ('Vida e integridad', 'Orientación')):
        x = 24
        for c in fila:
            x += s.chip(x, y, c, 7) + 4
        y += 17
    s.lines(24, 92, 160, 2, gap=7, last=0.5)
    s.text(186, 118, 'Leer completo ›', 7, C, 700, 'end')
    s.rect(204, 27, 182, 98, W, O, rx=7)
    s.add('<path d="M218 36 l7 12 h-14 z" fill="%s"/><text x="218" y="46.5" font-family="%s" font-size="8" '
          'font-weight="700" fill="%s" text-anchor="middle">!</text>' % (C, F, W))
    s.text(232, 46, 'Pero no reemplaza…', 9, O, 700)
    for i, it in enumerate(('procesos judiciales', 'procesos administrativos', 'procesos disciplinarios')):
        s.text(216, 64 + i * 12, '· ' + it, 7.5, M, 500)
    s.text(216, 108, 'y la persona debe saber cuál es la vía', 7, T, 500, italic=True)
    s.rect(14, 131, 372, 28, N, None, rx=6)
    s.text(24, 148, 'Límites:', 8, M, 700)
    x = 64
    for c in ('competencia', 'reserva legal', 'datos personales', 'derechos de terceros'):
        x += s.chip(x, 139, c, 6.8) + 4
    return s


def e06():
    s = S('E06', 'E06 · Escenario con botones a, b, c')
    s.rect(14, 27, 372, 132, CR, None, rx=7)
    s.rect(14, 120, 372, 39, '#F4D9DC', None, rx=0)
    s.rect(40, 92, 120, 30, T, None, rx=3)
    s.persona(70, 66, 1.5, M)
    s.persona(128, 66, 1.5, O)
    for i, (l, x, y) in enumerate((('a', 52, 52), ('b', 100, 46), ('c', 150, 52))):
        s.add('<circle cx="%s" cy="%s" r="8" fill="%s" stroke="%s" stroke-width="2"/><text x="%s" y="%s" '
              'font-family="%s" font-size="9" font-weight="700" fill="%s" text-anchor="middle">%s</text>'
              % (x, y, C, W, x, y + 3.2, F, W, l))
    s.rect(196, 34, 182, 118, W, T, rx=7, sw=1.4)
    s.text(206, 50, 'c) Oportunidad de la decisión', 8.5, M, 700)
    for i, (d, t, w) in enumerate(((15, 'regla general', 60), (10, 'documentos e información', 40),
                                   (30, 'consultas', 120))):
        y = 58 + i * 21
        s.text(206, y + 7, '%s días · %s' % (d, t), 7, M, 600)
        s.rect(206, y + 10, w, 7, (C if d == 15 else T), None, rx=3)
    s.rect(206, 124, 164, 22, N, None, rx=5)
    s.text(212, 133, 'No alcanza: avisar antes de vencer;', 6.8, M, 500)
    s.text(212, 142, 'nuevo plazo máximo el doble', 6.8, M, 700)
    return s


def e07():
    s = S('E07', 'E07 · Tres pestañas + flujo del traslado')
    for i, (t, w) in enumerate((('Orientar', 70), ('Trasladar', 74), ('Enfoque diferencial', 112))):
        x = 14 + sum((70, 74, 112)[:i]) + i * 4
        act = t == 'Trasladar'
        s.rect(x, 27, w, 18, M if act else N, None if act else T, rx=5)
        s.text(x + w / 2, 39.5, t, 8, W if act else M, 700, 'middle')
    s.rect(14, 47, 372, 112, W, T, rx=7)
    pasos = (('Llega a quien', 'no es competente'), ('Remite en 5 días', '+ copia al peticionario'),
             ('El término corre', 'desde que lo recibe'))
    for i, (a, b) in enumerate(pasos):
        x = 24 + i * 122
        s.rect(x, 62, 106, 38, N if i != 1 else CR, None, rx=6)
        s.text(x + 53, 78, a, 7.8, M, 700, 'middle')
        s.text(x + 53, 90, b, 7, M if i != 1 else O, 500, 'middle')
        if i < 2:
            s.arrow(x + 108, 81, x + 120, 81)
    s.text(24, 116, 'Si la pide verbalmente: avisar de inmediato que no es competente.', 7.3, T, 500, italic=True)
    s.text(24, 128, 'art. 21 Ley 1437 (sustituido por la Ley 1755)', 7, O, 600)
    s.pdf(232, 136)
    return s


def e08():
    s = S('E08', 'E08 · Tres tarjetas con chips')
    for i in range(3):
        s.rect(14 + i * 126, 27, 120, 132, W if i < 2 else CR, T if i < 2 else C, rx=7, sw=1.2)
    s.text(74, 44, 'A toda persona', 8.5, M, 700, 'middle')
    s.persona(60, 64, 1.3, T)
    s.persona(88, 64, 1.3, O)
    s.add('<g transform="rotate(-8 74 118)"><rect x="28" y="106" width="92" height="22" rx="4" fill="none" '
          'stroke="%s" stroke-width="1.6"/><text x="74" y="121" font-family="%s" font-size="7.4" font-weight="700" '
          'fill="%s" text-anchor="middle">Gratis · sin abogado</text></g>' % (C, F, C))
    s.text(200, 44, 'Sin barreras', 8.5, M, 700, 'middle')
    s.lines(150, 56, 100, 5, gap=8, last=0.5)
    s.text(326, 44, 'Quiénes llegan', 8.5, M, 700, 'middle')
    y = 52
    for fila in (('víctimas', 'testigos'), ('investigados', 'familiares'), ('apoderados', 'servidores'),
                 ('organizaciones',)):
        x = 272
        for c in fila:
            x += s.chip(x, y, c, 6.6, W, O, O) + 3
        y += 16
    s.text(326, 128, 'Barreras: discapacidad,', 6.6, M, 500, 'middle')
    s.text(326, 138, 'edad, idioma, ubicación…', 6.6, M, 500, 'middle')
    return s


def e09():
    s = S('E09', 'E09 · Frase fuerza + texto + PDF')
    s.rect(14, 27, 372, 30, CR, None, rx=6)
    s.text(200, 46, 'Las solicitudes son oportunidades, no cargas', 10, O, 700, 'middle')
    s.lines(24, 68, 352, 3, last=0.85)
    s.lines(24, 94, 352, 3, last=0.7)
    s.lines(24, 120, 352, 2, last=0.5)
    s.text(24, 152, 'Texto a todo el ancho, sin la columna de íconos', 7.3, T, 500, italic=True)
    s.pdf(244, 140)
    return s


def e10():
    s = S('E10', 'E10 · Caso con la carta en pantalla')
    s.rect(14, 27, 130, 106, W, T, rx=7)
    s.text(24, 42, 'Situación', 8.5, M, 700)
    s.rect(28, 50, 102, 74, H, M, rx=2, sw=1)
    s.text(34, 61, 'Asociación comunitaria', 6.6, O, 700)
    s.lines(34, 67, 88, 6, gap=8, last=0.5)
    for i, (t, extra) in enumerate((('Análisis', ''), ('Actividad de reflexión', 'pdf'))):
        y = 27 + i * 54
        s.rect(152, y, 234, 48, W, T, rx=7)
        s.text(162, y + 16, t, 8.5, M, 700)
        if extra:
            s.pdf(162, y + 24, 'Guía de reflexión (PDF)')
            s.text(300, y + 35, '4 preguntas + espacio', 6.5, T, 500, italic=True)
        else:
            s.lines(162, y + 26, 210, 2, gap=8, last=0.6)
    s.rect(14, 139, 372, 20, M, None, rx=5)
    s.text(24, 152.5, 'Idea clave', 8, CR, 700)
    s.text(76, 152.5, 'visible siempre, sin clic', 7.5, W, 500)
    return s


def e11():
    s = S('E11', 'E11 · Conclusión a todo el ancho')
    s.rect(14, 27, 372, 132, W, T, rx=7)
    s.lines(26, 42, 348, 4, last=0.9)
    s.lines(26, 76, 348, 4, last=0.6)
    s.rect(22, 106, 356, 34, W, C, rx=5, sw=1.4, dash='4 3')
    s.lines(30, 114, 330, 2, color='#F3B8BC', last=0.8)
    s.text(30, 135, 'Revisar con el autor: la 1.2 no es «fundamento y Política»', 7.5, O, 700)
    s.text(26, 153, 'Sin columna de íconos · sin scroll', 7.3, T, 500, italic=True)
    return s


def gen():
    s = S('GEN', 'Generales · Aviso abajo y botón PDF')
    s.rect(14, 27, 372, 104, W, T, rx=7)
    s.lines(26, 42, 348, 6, gap=9, last=0.7)
    s.add('<line x1="160" y1="60" x2="250" y2="82" stroke="%s" stroke-width="1.5"/><line x1="250" y1="60" '
          'x2="160" y2="82" stroke="%s" stroke-width="1.5"/>' % (C, C))
    s.rect(150, 56, 110, 30, '#6E7F86', None, rx=5)
    s.text(205, 74, 'aviso encima del texto', 7, W, 500, 'middle')
    s.add('<line x1="150" y1="56" x2="260" y2="86" stroke="%s" stroke-width="2"/>' % C)
    s.rect(14, 137, 372, 22, N, None, rx=5)
    s.text(22, 151, 'Pantalla completa · Texto fijo', 7, M, 600)
    s.rect(140, 141, 120, 14, '#6E7F86', None, rx=4)
    s.text(200, 151, 'aviso aquí, una sola vez', 6.8, W, 500, 'middle')
    s.pdf(268, 140, 'Texto completo (PDF)')
    return s


TODAS = (e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, gen)

if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for f in TODAS:
        s = f()
        nom = 'DP_U1_L1_%s.svg' % s.clave
        open(os.path.join(out, nom), 'w', encoding='utf-8').write(s.svg())
        print(nom)
