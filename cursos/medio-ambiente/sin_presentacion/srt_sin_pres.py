# -*- coding: utf-8 -*-
"""Subtítulos de las entregas sin la presentación de la docente (23 nov 2026): se parte del .srt ya revisado de la
entrega anterior; los subtítulos dentro del corte se quitan, los de después se corren lo que dura el corte y el que
lo cruza se reescribe con lo que queda («…y en esta oportunidad» → «Y en esta oportunidad»)."""
import sys
F = 24000 / 1001
D = '/home/claude/sf/srt/'
O = '/home/claude/sinpres/srt/'
# clave: (srt anterior, srt nuevo, inicio del corte, fin del corte [s de la entrega anterior], arreglos)
# arreglos: {texto del que cruza o del primero de después: (texto nuevo, cuántos siguientes absorbe)}
J = {
    'dau1i': ('U1 - INTRODUCCION-v3', 'U1 - INTRODUCCION-v4', 618 / F, 1293 / F, {}),
    'dau2i': ('U2 - INTRODUCCION-v2', 'U2 - INTRODUCCION-v3', 588 / F, 760 / F, {}),
    'dau3i': ('U3 - INTRODUCCION-v2', 'U3 - INTRODUCCION-v3', 607 / F, 667 / F,
              {'Mi nombre es Diana Carolina Florez\nVallona y en esta oportunidad':
               ('Y en esta oportunidad quiero\npresentarles la unidad tres,', 1)}),
    'dau4i': ('U4 - INTRODUCCION-v2', 'U4 - INTRODUCCION-v3', 576 / F, 633 / F,
              {'y en esta oportunidad quiero\npresentarles la unidad cuatro,':
               ('Y en esta oportunidad quiero\npresentarles la unidad cuatro,', 0)}),
    'dau5i': ('U5 - INTRODUCCION-v2', 'U5 - INTRODUCCION-v3', 614 / F, 680 / F,
              {'y en esta oportunidad quiero\npresentarles la unidad quinta,':
               ('Y en esta oportunidad quiero\npresentarles la unidad quinta,', 0)}),
    # cierre: 17,059 s de intro y título + el corte de la fuente (104/30 → 173/30)
    'dacc': ('CURSO - CIERRE-v1', 'CURSO - CIERRE-v2', 409 / F + 104 / 30, 409 / F + 173 / 30,
             {'Soy Diana Carolina Florez\nVallona y quiero felicitarlos': ('Y quiero felicitarlos', 0)}),
}


def tc(s):
    h, m, r = s.split(':'); s_, ms = r.split(','); return int(h) * 3600 + int(m) * 60 + int(s_) + int(ms) / 1000


def fmt(t):
    ms = int(round(t * 1000)); return '%02d:%02d:%02d,%03d' % (ms // 3600000, ms // 60000 % 60, ms // 1000 % 60, ms % 1000)


for k, (viejo, nuevo, a, b, arr) in J.items():
    bl = [x for x in open(D + 'delitosambientales - %s.srt' % viejo, encoding='utf-8').read().replace('\r\n', '\n').split('\n\n') if x.strip()]
    subs = []
    for x in bl:
        L = x.split('\n'); i, j = [tc(s.strip()) for s in L[1].split('-->')]; subs.append([i, j, '\n'.join(L[2:]).strip()])
    sh = b - a
    out, n, quitados, salto = [], 0, [], 0
    for idx, (i, j, t) in enumerate(subs):
        if salto:
            salto -= 1; continue
        if t in arr:
            t2, absorbe = arr[t]
            j = subs[idx + absorbe][1]
            salto = absorbe
            i = max(i, b)          # lo que queda empieza en el borde del corte
            out.append([i - sh, j - sh, t2]); n += 1
            continue
        if i < a and a < j <= a + 0.15:       # la última palabra antes del corte estirada sobre la pausa cortada
            j = a
        if b - 0.15 <= i < b and j > b:       # la primera de después arrancando en la pausa cortada
            i = b
        if j <= a + 0.001:
            out.append([i, j, t])
        elif i >= b - 0.001:
            out.append([i - sh, j - sh, t])
        elif i >= a - 0.001 and j <= b + 0.001:
            quitados.append(t.replace('\n', ' '))
        else:
            raise SystemExit('%s: «%s» cruza el corte (%.3f-%.3f) sin arreglo' % (k, t, i, j))
    assert n == len(arr), (k, n)
    txt = '\r\n'.join('%d\r\n%s --> %s\r\n%s\r\n' % (q + 1, fmt(i), fmt(j), t.replace('\n', '\r\n')) for q, (i, j, t) in enumerate(out)) + '\r\n'
    open(O + 'delitosambientales - %s.srt' % nuevo, 'w', encoding='utf-8', newline='').write(txt)
    print('%-6s %3d → %3d subtítulos, corrido %.3f s; quitados: %s' % (k, len(subs), len(out), sh, ' | '.join(quitados)))
