# -*- coding: utf-8 -*-
r"""VIDEO 05 · Operación «Raíces Profundas» (U4 L2). Narra Carlos. 23 ranuras.
El caso práctico del PDF (pp. 112-113), casi literal, con las cuatro
preguntas orientadoras como columna (un gráfico por pregunta).

LA PROGRESIÓN
    r01-r02   la maquinaria entra al resguardo · la retro en la orilla
    r03-r04   el agua con mercurio · el bosque de las plantas, talado
    r05-r06   la Fiscalía interviene · los procesados piden la oportunidad
    r07-r08   la casa comunal: Fiscalía, autoridad ambiental y Cabildo
    r09-r11   1. ¿quiénes? (gráfico): las familias · el río · el jaibaná
    r12-r15   2. ¿cómo? (gráfico): el bosque sagrado · la cosmovisión · los
              niños · enseñar sin bosque
    r16-r19   3. ¿qué medidas? (gráfico): ciencia y saber · el mercurio · la
              siembra · la armonización
    r20-r21   4. ¿cómo participa? (gráfico): la Guardia mide el agua
    r22-r23   el juez · las dos firmas (gráfico)

EL RESGUARDO ES EMBERA, EN EL CHOCÓ (tambos de palma, champas, la Guardia con
bastón). «Río Sagrado» es el nombre del caso, no un lugar real: nada se
rotula. Nadie armado; la maquinaria la manejan figuras sin cara.

R[n] = (cuadros, registro, gente, acento, fuego, lugar, escena)
"""

R = {}

R[1] = (100, 'aire', (), 'the excavator on the barge', False, 'resguardo_choco', '''
High aerial view of a wide river of the Colombian Pacific rainforest, the
camera far above looking down at a steep angle, the horizon level near the
top: on the near bank, small, the thatched stilt houses of an Embera reserve;
in mid-river, coming upstream, a flat plain grey barge carrying a
mustard-yellow excavator, a long wake behind it; the dense forest all around.
''')

R[2] = (100, 'dia', ('operador',), 'the excavator', False, 'resguardo_choco', '''
Wide shot on the riverbank at the edge of the forest, the camera at standing
height, perfectly level: a mustard-yellow excavator digs into the bank, its
bucket lifting a load of wet earth and roots, fallen trees pushed aside
around it; %(operador)s; a muddy pit already open beside the river.
''')

R[3] = (100, 'contra_ext', (), None, False, 'resguardo_choco', '''
Medium-wide shot of a forest stream below the mining pit, the camera low at
the water, perfectly level: the stream runs dull opaque ochre-grey with a
faint metallic grey sheen on the surface, between muddy banks; upstream, the
raw earth of the pit; downstream, small and soft, the thatched roof of a
stilt house. Nobody in the frame.
''')

R[4] = (100, 'dia', ('embera_mujer',), None, False, 'resguardo_choco', '''
Medium-wide shot at the edge of a felled patch of forest, the camera at
standing height, perfectly level: grey stumps and fallen trunks where the
forest stood; %(embera_mujer)s stands at the edge of the clearing with an
empty woven basket on her back, its strap across her forehead, looking at the
stumps, her hands resting on the strap.
''')

R[5] = (100, 'dia', ('fiscal', 'investigador'), 'the stopped excavator', False, 'resguardo_choco', '''
Wide shot at the muddy riverbank by the pit, the camera at standing height,
perfectly level: a plain grey aluminium boat has just landed; %(fiscal)s
steps onto the bank with her folder under her arm and %(investigador)s
photographs the mustard-yellow excavator, now stopped and silent, its bucket
resting on the ground.
''')

R[6] = (100, 'dia', ('defensor', 'empresario'), None, False, 'sala', '''
Medium shot in the hearing room, the camera at seated height behind the
defence table, perfectly level: %(defensor)s stands and speaks toward the
judge's desk, one hand open, palm up; beside him %(empresario)s sits with
his shoulders hunched and his hands folded on the table.
''')

R[7] = (100, 'dia', ('fiscal', 'corpo', 'gobernador', 'emberas'), None, False, 'casa_comunal', '''
Wide shot inside the community house, the camera at standing height at the
edge of the circle, perfectly level: on the plain wooden benches arranged in
a circle sit %(gobernador)s with his staff of authority upright beside him,
%(fiscal)s with her folder on her knees and %(corpo)s with a plain notebook;
around them, sitting and standing, %(emberas)s listen. The river and the
forest beyond the open sides.
''')

R[8] = (100, 'dia', ('gobernador', 'fiscal'), None, False, 'casa_comunal', '''
Medium shot in the community house, the camera at seated height, perfectly
level: %(gobernador)s speaks, his staff of authority held upright in one
hand, the other hand open toward the river; across from him %(fiscal)s
listens and writes in a plain notebook on her knee.
''')

R[9] = (100, 'dia', ('emberas',), None, False, 'resguardo_choco', '''
Wide shot of the Embera reserve along the river, the camera at standing
height on the sandy bank, perfectly level: a row of thatched stilt houses
with notched log ladders; %(emberas)s go about the morning: a woman climbs a
ladder with a pot, two men pull a dugout canoe up the sand, children sit on a
log by the water.
''')

R[10] = (100, 'dia', ('embera_mujer',), None, False, 'resguardo_choco', '''
Medium shot at the river's edge, the camera low near the water, perfectly
level: %(embera_mujer)s kneels on a flat stone and fills a plain dark pot with
river water, holding it with both hands; behind her, out on the river, a man
in a dugout canoe casts a net.
''')

R[11] = (100, 'contra_ext', ('sabedor',), None, False, 'resguardo_choco', '''
Medium-wide shot at the edge of the forest, the camera at standing height,
perfectly level: %(sabedor)s stands between two tall trees at the edge of the
felled area, the small bundle of medicinal leaves held against his chest,
looking at the stumps beyond. The forest behind him is dense and dark grey.
''')

R[12] = (100, 'aire', (), None, False, 'resguardo_choco', '''
High aerial view of the reserve, the camera far above looking down at a steep
angle, the horizon level near the top: the thatched stilt houses along the
river, the dense forest behind them, and cutting into the forest a raw scar
of earth, pits and felled trees reaching toward the river.
''')

R[13] = (100, 'dia', ('sabedor', 'gobernador'), None, False, 'casa_comunal', '''
Medium shot on the floor of a stilt house open to the river, the camera at
seated height, perfectly level: %(sabedor)s and %(gobernador)s sit side by
side on a plain bench, quiet, both looking out at the river; the sabedor's
bundle of leaves rests on his knee, the governor's staff leans against the
bench.
''')

R[14] = (100, 'dia', ('madre_nino',), None, False, 'resguardo_choco', '''
Medium shot inside a stilt house, the camera at seated height, perfectly
level: %(madre_nino)s sits on the palm-board floor with a small child asleep
on her lap, wrapped in a plain cloth; she rests one hand on the child's
back; beside her, a plain covered water container. Calm, quiet, nothing
dramatic.
''')

R[15] = (100, 'dia', ('sabedor', 'jovenes'), None, False, 'resguardo_choco', '''
Medium-wide shot at the edge of the felled area, the camera at standing
height, perfectly level: %(sabedor)s holds up one leaf from his bundle and
shows it to %(jovenes)s who stand in front of him; behind them only stumps
and bare earth where the forest was.
''')

R[16] = (100, 'dia', ('corpo', 'sabedor'), None, False, 'resguardo_choco', '''
Medium shot at the forest stream, the camera at standing height, perfectly
level: %(corpo)s crouches at the water and holds up a plain glass sample
bottle against the light; %(sabedor)s stands beside her and holds out a leaf
from his bundle; they look at each other, about to speak.
''')

R[17] = (100, 'dia', ('tecnicos', 'corpo'), None, False, 'resguardo_choco', '''
Wide shot at the muddy mining pit by the river, the camera at standing
height, perfectly level: %(tecnicos)s shovel grey sludge from the pit into
plain grey drums with sealed lids lined up on the bank; %(corpo)s stands at
the edge with a plain clipboard, checking each drum.
''')

R[18] = (100, 'dia', ('emberas', 'sabedor'), None, False, 'resguardo_choco', '''
Wide shot of the felled area, the camera at standing height, perfectly
level: %(emberas)s plant young seedlings in rows in the bare earth, kneeling,
pressing the soil around each one with their hands; %(sabedor)s walks
between the rows and points at the next place to plant.
''')

R[19] = (100, 'contra_ext', ('sabedor', 'emberas'), None, False, 'resguardo_choco', '''
Wide shot at the forest stream, the camera at standing height, perfectly
level: %(sabedor)s stands at the water's edge and holds his bundle of leaves
over the water; %(emberas)s stand in a quiet half circle behind him; the
forest rises dark grey behind them. Respectful and calm; no fire.
''')

R[20] = (100, 'dia', ('guardia',), None, False, 'resguardo_choco', '''
Medium-wide shot at the river's edge, the camera at standing height,
perfectly level: %(guardia)s stand in the shallow water; she dips a plain
grey water-monitoring probe on a cable into the river while he holds both
staffs and a plain grey carrying case open on his arm.
''')

R[21] = (100, 'dia', ('guardia',), None, False, 'resguardo_choco', '''
Medium close shot of the two guards, the camera at their eye level,
perfectly level: the young woman reads the small plain grey meter in her
hand, the young man writes the reading in a plain notebook; their staffs
with the plain grey ribbons lean against a post behind them. Nothing legible
on the meter.
''')

R[22] = (100, 'dia', ('juez',), None, False, 'sala', '''
Medium shot of %(juez)s at his plain desk on the low platform of the hearing
room, the camera at seated height, perfectly level: he turns the last page of
a thick plain report bound in plain grey card and looks at the two signature
lines at the bottom of the page. Nothing legible anywhere.
''')

R[23] = (100, 'dia', ('perito', 'gobernador'), None, False, 'casa_comunal', '''
Medium shot at a plain table set up in the community house, the camera at
seated height, perfectly level: %(perito)s signs the last page of the plain
report with a plain pen; across the table %(gobernador)s waits with his
staff of authority upright in one hand, the pen for him lying ready beside
the report.
''')

NOMBRE = {1: 'la_barcaza', 2: 'la_retro', 3: 'el_agua', 4: 'el_bosque',
          5: 'interviene', 6: 'la_oportunidad', 7: 'la_casa_comunal',
          8: 'el_gobernador', 9: 'las_familias', 10: 'el_rio',
          11: 'el_jaibana', 12: 'la_herida', 13: 'la_cosmovision',
          14: 'los_ninos', 15: 'ensenar', 16: 'ciencia_y_saber',
          17: 'el_mercurio', 18: 'la_siembra', 19: 'la_armonizacion',
          20: 'la_guardia', 21: 'los_veedores', 22: 'el_juez', 23: 'las_firmas'}

CORTE = {
 1: ('k01_empresa', 'Una empresa'),
 2: ('k01_empresa', 'ingresó maquinaria'),
 3: ('k02_dano', 'La actividad'),
 4: ('k02_dano', 'y destruyó'),
 5: ('k03_oportunidad', 'La Fiscalía'),
 6: ('k03_oportunidad', 'buscan acogerse'),   # 7 nov: la intervención tenía 31
 7: ('k04_cabildo', 'Para construir'),
 8: ('k04_cabildo', 'deben coordinarse'),
 9: ('k05_quienes', 'Primera'),
 10: ('k05_quienes', 'que dependen'),
 11: ('k06_sabedores', 'Y los médicos'),
 12: ('k07_como', 'Segunda'),
 13: ('k07_como', 'El daño no'),
 14: ('k08_ninos', 'El río'),
 15: ('k08_ninos', 'Y sin el bosque'),
 16: ('k09_medidas', 'Tercera'),
 17: ('k10_mercurio', 'El procesado'),
 18: ('k11_semillas', 'La reforestación'),
 19: ('k11_semillas', 'Y el procesado'),
 20: ('k12_guardia', 'Cuarta'),
 21: ('k12_guardia', 'ellos serán'),
 22: ('k13_firmas', 'Y para que'),
 23: ('k13_firmas', 'el informe final'),
}

EXTRA_TOKENS = {
 'embera_mujer': ('AN EMBERA WOMAN of about thirty-five, straight black hair to '
                  'the shoulders, fully dressed in a plain short-sleeved blouse '
                  'and a long plain wrap skirt of muted printed cloth, a bead '
                  'collar in muted grey-white'),
 'madre_nino': ('AN EMBERA MOTHER of about twenty-five, straight black hair, '
                'fully dressed in a plain long-sleeved blouse buttoned to the '
                'neck and a long plain wrap skirt of muted printed cloth'),
 'jovenes': ('three EMBERA YOUNG PEOPLE of about sixteen, two boys and a girl, '
             'in plain light shirts'),
 'tecnicos': ('two technicians in plain grey coveralls, plain grey rubber '
              'gloves and rubber boots'),
}

REF = {
 5: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator is the SAME man; the prosecutor is the one of the first reference.'),
 6: ('DA_V02_r19_el_juicio', 'lugar', 'It is the SAME hearing room and the SAME defence lawyer.'),
 22: ('DA_V02_r19_el_juicio', 'lugar', 'It is the SAME hearing room and the SAME judge, closer.'),
 8: (7, 'lugar', 'It is the SAME community house with the SAME governor and prosecutor, closer.'),
 13: (7, 'gente', 'The governor is the SAME man.'),
 23: (7, 'lugar', 'It is the SAME community house and the SAME governor.'),
 10: (4, 'gente', 'It is the SAME woman.'),
 15: (11, 'gente', 'It is the SAME healer.'),
 16: (11, 'gente', 'It is the SAME healer.'),
 18: (11, 'gente', 'It is the SAME healer.'),
 19: (11, 'gente', 'It is the SAME healer.'),
 12: (1, 'lugar', 'It is the SAME reserve on the SAME river, closer.'),
 3: (2, 'lugar', 'It is the SAME mining pit, at the stream below it.'),
 17: (2, 'lugar', 'It is the SAME pit, months later: the excavator is gone.'),
 21: (20, 'lugar', 'It is the SAME two guards, closer.'),
}
REF2 = {5: 'DA_V01_r30_la_fiscal', 7: 'DA_V01_r30_la_fiscal',
        8: 'DA_V01_r30_la_fiscal', 23: ('DA_V04_r09_el_perito', 'THE ENVIRONMENTAL EXPERT'),
        13: ('DA_V05_r11_el_jaibana', 'THE TRADITIONAL HEALER')}

ANCLA_DE = {1: 'rural', 2: 'rural', 4: 'rural', 7: 'pueblo', 9: 'rural',
            11: 'rural', 20: 'rural'}

CON_PERSONA = {2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23}
AEREOS = {1, 12}
CENITALES = set()
SOLO_MANOS = set()
TOPE_SIN_GENTE = 3
TOTAL = 2300
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

GRIS = (20, 110)
SIN_TECHO = set()

# las cuatro preguntas (una por bloque que la abre) y las dos firmas
GRAFICOS = {9: 'q1', 12: 'q2', 16: 'q3', 20: 'q4', 23: 'firmas'}

KLING = {
 1: ('aire', 'The camera glides slowly forward high over the river; the barge with '
     'the excavator moves slowly upstream, leaving its long wake behind it.'),
 2: ('fija', 'The excavator lifts its bucket full of wet earth and roots out of '
     'the bank, swings it slowly to one side and tips the load out onto the pile; '
     'mud and water run down into the river.'),
 3: ('fija', 'The opaque ochre-grey stream flows slowly between the muddy banks, '
     'the faint metallic sheen sliding along its surface; the trees on the banks '
     'stir in a light breeze.'),
 4: ('fija', 'She stands at the edge of the clearing and slowly turns her head from '
     'the stumps toward the river, breathes, and lowers her eyes; a light breeze '
     'moves the leaves of the trees behind her.'),
 5: ('fija', 'The prosecutor walks up the bank from the boat with her folder under '
     'her arm, two steps toward the excavator; the investigator raises his camera '
     'and photographs it.'),
 6: ('fija', 'The defence lawyer speaks toward the judge, his open hand moving '
     'slowly as he talks; the judge listens; the man at the table in the '
     'foreground keeps his head down.'),
 7: ('fija', 'The governor speaks to the circle, one hand moving as he talks; the '
     'people on the benches listen and two of them nod; the prosecutor writes a '
     'line in her notebook.'),
 8: ('fija', 'The governor speaks, his open hand moving slowly toward the river and '
     'back; the prosecutor listens and writes in her notebook on her knee; the '
     'woman beside her nods.'),
 10: ('fija', 'She lifts the pot full of river water out of the river with both '
      'hands and sets it down on the stone beside her; behind her the man in the '
      'canoe pulls his net in.'),
 11: ('fija', 'He stands still between the trees, breathes slowly, and lifts the '
      'bundle of leaves a little closer to his chest while he looks at the '
      'stumps; a light breeze moves his long grey hair and the leaves of the '
      'trees.'),
 13: ('fija', 'The two men sit side by side and look out at the river; the governor '
      'turns his head to the elder and says a few words, and the elder nods '
      'slowly; the river flows past beyond the railing.'),
 14: ('fija', 'She breathes slowly and moves her hand gently up and down on the '
      'sleeping child\'s back; outside the river flows past.'),
 15: ('fija', 'The elder turns the leaf slowly in his fingers as he speaks to the '
      'young people; they look at the leaf and one of them nods.'),
 17: ('fija', 'The two technicians drive their shovels into the grey sludge, lift '
      'it and tip it into the open drum; the woman at the edge writes a line on '
      'her clipboard.'),
 18: ('fija', 'The women press the soil around the seedlings with both hands and '
      'set the next seedling in the earth; the elder walks slowly between the rows '
      'and points at the next place to plant.'),
 19: ('fija', 'The elder moves the bundle of leaves slowly over the water from side '
      'to side; the people behind him stand still in their half circle and watch; '
      'small ripples spread around his legs.'),
 21: ('fija', 'She reads the meter in her hand and says the reading; he writes it '
      'in his notebook with his pen and looks up at her.'),
 22: ('fija', 'He reads the open report, his eyes moving down the page to the two '
      'signature lines at the bottom, and slowly lifts his head. The pages stay '
      'flat on the desk.'),
}
# r09, r12, r16, r20 y r23 van bajo el panel de su pregunta.
KLING_PRESTADO = {}
KLING_FIJA = 'Tripod shot: the camera stays where it is.'
KLING_AIRE = 'The camera moves only forward, smoothly, at the same height.'
KLING_FIN = ('Every movement travels all the way and arrives; nothing stops '
             'halfway. Keep the picture exactly as drawn in the first frame: the '
             'same flat graphic illustration with broad flat tonal planes, the '
             'same muted grey palette, the same people with the same faces.')
KLING_NEG = ('photorealistic, photograph, 3D render, texture, film grain, noise, '
             'ink outlines, colour shift, saturated colours, morphing, distorted '
             'face, extra people, extra hands, new objects, text, letters, logo, '
             'flag, weapon')


def comprobar():
    fallos = []
    tot = sum(v[0] for v in R.values())
    if sorted(R) != list(range(1, len(NOMBRE) + 1)):
        fallos.append('faltan ranuras')
    if tot != TOTAL:
        fallos.append('los cuadros suman %d y la rejilla dice %d' % (tot, TOTAL))
    racha = mejor = 0
    for i in sorted(R):
        racha = 0 if i in CON_PERSONA else racha + 1
        mejor = max(mejor, racha)
    if mejor > TOPE_SIN_GENTE:
        fallos.append('%d ranuras seguidas sin gente' % mejor)
    return fallos, tot, mejor

# --- 7 nov: cuadros medidos (cortes de Scribe sobre la voz masterizada:
# cada ranura entra 3 cuadros antes de la primera palabra de su CORTE; la
# ultima termina con el master)
CUADROS = {1: 94, 2: 170, 3: 93, 4: 144, 5: 54, 6: 107, 7: 140, 8: 170, 9: 166, 10: 102, 11: 260, 12: 110, 13: 131, 14: 109, 15: 144, 16: 190, 17: 218, 18: 203, 19: 173, 20: 221, 21: 69, 22: 100, 23: 184}
for _n, _c in CUADROS.items():
    R[_n] = (_c,) + R[_n][1:]
TOTAL = 3352
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)
