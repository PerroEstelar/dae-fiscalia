# -*- coding: utf-8 -*-
r"""Clausulas y reparto del curso «Gerencia judicial» (PRIORIDAD 2).

EL SISTEMA ES EL DE LA SERIE, SIN UNA COMA DE MAS
    No hay biblia propia de la PRIORIDAD 2, y Sebastian pidio «todos los
    procesos que ya conoces». El sistema visual mas maduro y aprobado de la
    casa es el del P3 y de Desaparicion Forzada: rostros dibujados y
    simplificados, piel gris calida, los tres registros de luz, superficie
    lisa, el acento como PRENDA mate, la escena como unidad, cartones
    verbatim. Todo lo que no es reparto se importa de `base_df_v1` tal cual.

LO NUEVO ES EL LUGAR
    Las situaciones de Desaparicion Forzada pasaban en un municipio pequeno
    y en el campo. Aqui los tres casos pasan, sobre todo, ADENTRO de la
    Fiscalia: un despacho, una sala de reuniones, una oficina de
    coordinacion. El T3 sale a una empresa de servicios publicos de ciudad y
    el T4 a una zona rural distante. Por eso hay tres clausulas de lugar:
    OFICINA (la de la serie), CIUDAD, RURAL y SALA (la de audiencias del T3).

EL COLOR, CASO POR CASO
    La regla de la serie: un solo saturado por composicion, mostaza mate,
    como prenda. En Desaparicion Forzada lo llevaba quien es buscado y quien
    busca. Aqui lo lleva quien esta en el centro de cada caso:
        T1  el fiscal recien nombrado -una corbata-: el caso es lo que el
            hace con su despacho;
        T3  el fiscal delegado -un sueter bajo el saco-: el caso es su
            decision;
        T4  las DOS personas sobre las que trata el enfoque diferencial: la
            servidora (un cardigan) y la joven (una manta sobre los
            hombros, vista siempre de lejos). La coordinacion va en gris.
    La institucion, los equipos y los demas, en gris.

QUIEN NO LLEVA CARA, Y POR QUE
    La regla del paso 11: una decision equivocada no cae sobre un rostro.
        T1  el equipo que atiende «en el estricto orden en que llegan»: se
            cuenta por las manos, la fila y las carpetas. El fiscal SI lleva
            cara: el caso lo nombra y lo que le falta -conocer la mision- no
            es un gesto, es lo que el curso le va a dar.
        T3  el procesado y los directivos: espalda, silueta y manos. El
            hecho es una inferencia («habrian utilizado») y el hecho debatido
            no se ilustra: las ordenes y los contratos entran como
            ELEMENTOS MATERIALES PROBATORIOS sobre la mesa del fiscal, nunca
            como una escena de alguien firmandolos.
        T4  el coordinador que responde y el investigador que sostiene: los
            dos dicen lo que el ejercicio discute. Espalda, hombro, manos.
            La JOVEN no lleva cara en ningun plano: es menor de edad,
            victima de violencia sexual y de un pueblo indigena que el
            documento no nombra. Aparece solo de lejos y de espaldas, en su
            territorio. La agresion no se dibuja de ninguna forma, ni en
            silueta: esta en la voz, verbatim, y nada mas. El presunto
            responsable no aparece nunca.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_df_v1 as B                          # noqa: E402
from base_df_v1 import (PIEL, ROSTRO, PLANOS, REGISTRO, CAMARA, LIMPIA,  # noqa
                        SIN_ROLES, SILUETA, ESTILO, FIGURA, LUGAR, ACENTO, NEG)

# ------------------------------------------------------------------ lugar
OFICINA = ('The setting is an ordinary Colombian public prosecution office: '
           'plain painted masonry walls, simple metal-framed windows with '
           'plain glass, modest grey institutional desks and metal filing '
           'shelves, plain office chairs, ordinary computer screens. Nothing '
           'lavish, nothing north-american in the fittings, no wood '
           'panelling, no courtroom bench, no flag, no portrait on the wall.')

CIUDAD = ('The setting is an ordinary Colombian city: plain rendered and '
          'painted facades, a simple concrete pavement, plain metal fences '
          'and gates, a few street trees. Nothing lavish, nothing '
          'picturesque, nothing north-american in the fittings, no '
          'billboard, no shop sign, no lettering anywhere.')

RURAL = ('The setting is a remote rural area of Colombia far from any town: '
         'steep green mountains, a narrow footpath of bare earth, a small '
         'river with stones, scattered simple houses of plain timber and '
         'plain sheet roofs far apart from each other. Nothing picturesque, '
         'no postcard framing, no tourist colour, no costume, no feathers, '
         'no face paint, no folkloric ornament.')

SALA = ('The setting is an ordinary Colombian hearing room: plain painted '
        'walls, plain institutional tables and chairs, plain wooden public '
        'benches, high plain windows. No raised judge\'s bench with carving, '
        'no flag, no shield, no emblem, no portrait, no lettering, nothing '
        'north-american and nothing lavish.')

LUGARES = {'oficina': OFICINA, 'ciudad': CIUDAD, 'rural': RURAL, 'sala': SALA}

# ------------------------------------------------------------------ reparto
CUERPO = {
 # ---- T1
 'fiscal1': ('THE NEWLY APPOINTED PROSECUTOR, a mestizo Colombian man of about '
             'forty-two, medium build, short dark hair with a neat side part, '
             'clean-shaven, in a plain dark grey suit jacket over a plain light '
             'grey shirt with a plain matte mustard-yellow tie, plain grey '
             'trousers and plain dark grey shoes'),
 'equipo1': ('TWO MEMBERS OF HIS TEAM, office assistants: a woman of about '
             'thirty in a plain mid-grey blouse and grey trousers with her '
             'dark hair tied back, and a young man of about twenty-six in a '
             'plain light grey shirt and grey trousers'),
 'publico1': ('PEOPLE WAITING TO FILE COMPLAINTS: ordinary Colombian men and '
              'women of different ages in plain grey everyday clothes, each '
              'holding a few papers'),
 # ---- T3
 'fiscal3': ('THE DELEGATE PROSECUTOR, a mestizo Colombian man of about '
             'forty-eight, solid build, short greying dark hair, a short '
             'trimmed grey beard, in a plain charcoal grey suit jacket over a '
             'plain matte mustard-yellow V-neck sweater and a plain light grey '
             'shirt, plain grey trousers'),
 'procesado': ('THE ACCUSED EXECUTIVE, a man of about fifty-five, heavy-set, '
               'thinning grey hair, in a plain dark grey suit with no tie'),
 'defensor': ('THE DEFENCE LAWYER, a man of about fifty, lean, grey hair cut '
              'short, in a plain mid-grey suit with a plain grey tie, holding '
              'a plain grey folder'),
 'victimas': ('THE VICTIMS, a few ordinary Colombian adults -a woman of about '
              'sixty in a plain grey cardigan, a man of about forty in a '
              'plain grey work shirt, a woman of about thirty-five in a plain '
              'grey blouse- seated side by side'),
 # ---- T4
 'coordinadora': ('THE COORDINATOR, a mestiza Colombian woman of about fifty, '
                  'medium build, dark shoulder-length hair with a few grey '
                  'strands, small plain reading glasses, in a plain mid-grey '
                  'blazer over a plain light grey blouse and plain grey '
                  'trousers'),
 'servidora': ('THE STAFF MEMBER, a Colombian woman of about thirty-five who '
               'has a visual disability, slim, dark hair cut in a short bob, in a plain matte '
               'mustard-yellow cardigan over a plain light grey blouse and '
               'plain grey trousers, wearing a plain dark grey over-ear '
               'headset'),
 'coordinador': ('ANOTHER COORDINATOR, a man of about fifty-five, heavy-set, '
                 'short grey hair, in a plain dark grey suit jacket over a '
                 'plain white shirt, no tie'),
 'investigador': ('THE INVESTIGATOR, a man of about forty-five, solid build, '
                  'close-cropped dark hair, in a plain dark grey zip jacket '
                  'over a plain light grey shirt and plain grey trousers, no '
                  'marking of any kind on the clothing'),
 'equipo4': ('THE TEAM of the office: prosecutors, assistants, investigators '
             'and support staff, ordinary Colombian men and women of different '
             'ages in plain grey office clothes'),
 'joven': ('A TEENAGE GIRL of an indigenous community, slight, long '
           'straight black hair, in a plain long grey skirt and a plain grey '
           'long-sleeved top with a plain matte mustard-yellow woven shawl '
           'over BOTH shoulders, seen only FROM FAR AWAY and FROM BEHIND'),
 'testigos': ('TWO WITNESSES from the rural community, an older man of about '
              'sixty in a plain grey shirt and a woman of about forty in a '
              'plain grey blouse, ordinary everyday clothes'),
}

VIDA = {
 'fiscal1': ('He arrived this week from another city and another post. He '
             'carries a plain grey leather briefcase and has not yet had time '
             'to take his jacket off.'),
 'equipo1': ('They have kept this office running for years and do what they '
             'have always done: the next folder on the pile.'),
 'publico1': ('Each of them came with one complaint, the most important '
              'thing that happened to them this year.'),
 'fiscal3': ('Twenty years of investigations. He reads every page himself '
             'and keeps a plain grey pen clipped to the folder he is working '
             'on.'),
 'procesado': ('He ran a department of the company for years and is used to '
               'signing what others prepare.'),
 'defensor': ('He speaks little and keeps his folder closed until he needs '
              'it.'),
 'victimas': ('They have waited years for this hearing.'),
 'coordinadora': ('She has coordinated teams for fifteen years and listens '
                  'before she answers. She keeps a plain grey notebook open in '
                  'front of her.'),
 'servidora': ('She has done this job for years with a screen reader and '
               'knows exactly what she needs to do it. Her hands rest on the '
               'keyboard with the confidence of someone who types without '
               'looking.'),
 'coordinador': ('He has run his own team the same way for years.'),
 'investigador': ('He writes down what happened and moves on to the next '
                  'case.'),
 'equipo4': ('It is Monday morning and the week is already full.'),
 'joven': ('She lives in her own territory, hours away from any office.'),
 'testigos': ('They know the girl and her family.'),
}

# Quien lleva acento.
CON_ACENTO = {'fiscal1', 'fiscal3', 'servidora', 'joven'}

# Quien NO se dibuja nunca con rostro.
SIN_ROSTRO = {'equipo1', 'publico1', 'procesado', 'coordinador',
              'investigador', 'joven'}

TOKENS = CUERPO


def arma(escena, registro='dia', personas=(), con_acento=None,
         con_lugar=True, con_rostro=True, lugar='oficina', silueta=False,
         exterior=None):
    """Arma el prompt final. `con_acento=None` lo decide el reparto: lleva
    acento si en el plano hay alguien de CON_ACENTO. `lugar` es oficina,
    ciudad o rural. `exterior` se acepta por compatibilidad con las
    herramientas de las situaciones y no hace nada: el lugar lo dice `lugar`.
    """
    if con_acento is None:
        con_acento = any(p in CON_ACENTO for p in personas)
    p = [escena.strip()]
    if personas:
        vidas = [VIDA[x] for x in personas if x in VIDA]
        if vidas:
            p.append('WHO THESE PEOPLE ARE. ' + ' '.join(vidas))
    p.append(REGISTRO[registro])
    p.append(PLANOS)
    if silueta:
        p.append(ESTILO + FIGURA)
        p.append(SILUETA)
    else:
        con_cara = con_rostro and any(x not in SIN_ROSTRO for x in personas)
        p.append(ESTILO + (ROSTRO if con_cara else '')
                 + (PIEL + ' ' if personas else '') + FIGURA)
    p.append(CAMARA)
    if con_acento:
        p.append(ACENTO)
    if con_lugar:
        p.append(LUGARES[lugar])
    p.append(LIMPIA)
    p.append(SIN_ROLES)
    p.append(NEG)
    return '\n\n'.join(x.strip() for x in p if x and x.strip())
