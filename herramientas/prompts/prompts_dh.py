# -*- coding: utf-8 -*-
r"""Arma todos los prompts de Derechos humanos y los deja donde se usan.

Por cada tema:
    - una placa por ranura (`escenas_dh_t<n>.R`), con las comprobaciones de
      la serie: los cuadros suman lo que dice la rejilla, no hay mas de tres
      ranuras seguidas sin gente, no hay mas de tres cenitales;
    - las HOJAS de personaje que entran como referencia en cada placa;
    - los insertos de detalle (`DET`) para la pista V3 DETALLE, cada uno con
      su placa -que se pide con la placa madre como referencia- y su gesto
      para Kling, con la clausula de quietud de la serie;
    - el b-roll de reserva (`BROLL`), las notas de movimiento (`MOV`) y el
      rotulo (`LOWER_THIRD`).

Sale un json por tema en D:\DAE\_tmp\dh y, en la carpeta de guion de cada
tema, un .md legible con el guion verbatim, las ranuras con lo que se oye
encima y cada prompt: el storyboard escrito, para mirarlo antes de gastar un
credito.

    python prompts_dh.py            (en la maquina de Sebastian)
    python prompts_dh.py --aqui DIR (en otra: escribe todo en DIR)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import base_dh as S                              # noqa: E402
from guion_dh import TEMAS, VIDEOS, bloques     # noqa: E402

TMP = r'D:\DAE\_tmp\dh'

# las hojas de personaje ya son creaciones de Magnific: entran como
# referencia por su identificador (Seedream 5 Flash, 30 oct)
# hojas de personaje (Seedream 5 Flash, 31 oct; la elegida de cada par)
HOJA_ID_CRUDA = {'carmen': 'dtUeNZkXSL', 'andres': 'xSVrIz0jfW',
                 'entrevistador': 'WD1YwHLcXe', 'sandra': '1l0kozYr4r',
                 'quintero': 'LwDjm06swO', 'julian': 'p8gD9RNehw',
                 'salgado': 'p8gD9Z6ehw', 'juez': '798wuKaJAL',
                 'apoderada': 'gOdlaqtSXO'}
# 31 oct: las hojas crudas tenian la piel durazno-rosada (mediana hasta 0,30)
# y la pasaban a cada placa. Desde la ronda de las 20 h la referencia es la
# hoja con la piel de la serie (`hojas_ref_dh.py` -> 00 PERSONAJES\_piel_ref,
# mediana 0,13-0,15, sin rosado).
HOJA_ID = {'carmen': 'jUMjPTFLD0', 'andres': 'aF6ak9mfSh',
           'entrevistador': 'tCPtqyCmZJ', 'sandra': '0ex0IrvTfW',
           'quintero': 'xSVxyTTjfW', 'julian': 'JNIJ285Oq4',
           'salgado': 'u5ZujZ9QLD', 'juez': '5jY5UYVKxe',
           'apoderada': 'jUMjPMqLD0'}

QUIETO = ('The camera does not move at all and the framing does not change. '
          'Only the movement described happens; nothing else in the frame '
          'moves. No new hand, face or figure enters the frame. Hands keep '
          'their natural arrangement: the fingers never splay and never '
          'change in number. Skin stays a flat desaturated warm grey, never '
          'pink. The flat graphic illustration style, the light and the '
          'near-monochrome palette stay exactly unchanged.')

REFERENCIA = ('This is a CLOSER SHOT OF THE SAME SCENE as the reference '
              'image: the same person, the same clothes, the same light from '
              'the same side, the same palette and the same flat graphic '
              'style. It must be indistinguishable from it in treatment. The '
              'skin of the hands and face is exactly the grey of the skin in '
              'the reference: never warmer, pinker, more peach or more '
              'saturated.')

# 29 oct, primera tirada: tres de los cuatro cenitales salieron como hoja de
# historieta -dos o tres vinetas, una con gente- en las DOS candidatas (T1 r04,
# T3 r03, T3 r10). El cenital se lee como "storyboard" si no se dice. Se
# agrega a todo cenital, dentro del parrafo del plano.
UNA_IMAGEN = ('This is ONE single continuous picture that fills the whole '
              'frame: NOT a split screen, NOT a comic page, NOT a storyboard '
              'sheet, NO panels, NO inset pictures, NO dividing borders, NO '
              'second view of the room.')

HOJA_REF = ('The reference image is a character model sheet: use it ONLY for '
            'the identity of the person -face, hair, build and clothes- and '
            'for the drawing style. Ignore its framing, its grey background, '
            'its pose and its repeated views: this picture is ONE scene, '
            'composed as described above, with each person appearing ONCE. '
            'The skin on the sheet is already the grey of this film: keep '
            'exactly that grey.')

HOJAS_REF = ('The reference images are character model sheets: use them ONLY '
             'for the identity of the people -face, hair, build and clothes- '
             'and for the drawing style. Ignore their framing, their grey '
             'background, their poses and their repeated views: this picture '
             'is ONE scene, composed as described above, with each person '
             'appearing ONCE. The skin on the sheets is already the grey of '
             'this film: keep exactly that grey.')


# 31 oct: una placa aprobada como ULTIMA referencia (REF_PLACA del modulo de
# escenas). 'mismo': el mismo plano, se cambia solo lo dicho; 'lugar': el
# mismo lugar en otro plano, solo el dibujo y la luz. Sin esto Flash dibuja
# foto (U1 r04/r05) o se inventa otro lugar.
REF_MISMO = ('The LAST reference image is the SAME SHOT from this same film, '
             'already approved: %s Match its DRAWING exactly: a flat graphic '
             'illustration built from broad simplified tonal planes, no rendered '
             'texture anywhere, no photographic detail. This picture must look '
             'like it was drawn by the same hand as that plate, not like a '
             'photograph.')
REF_LUGAR = ('The LAST reference image is a finished plate of this same place '
             'from this same film, already approved: use it for the place, the '
             'light and the drawing, not for the framing, which is described '
             'above. %sMatch its DRAWING exactly: a flat graphic illustration '
             'built from broad simplified tonal planes, no rendered texture '
             'anywhere, no photographic detail. This picture must look like it '
             'was drawn by the same hand as that plate, not like a photograph.')


# DH, 31 oct: una placa aprobada de OTRO lugar del mismo curso, solo para el
# dibujo (la r10 de la U1 es la ancla del curso).
REF_ESTILO = ('The LAST reference image is a finished plate from this same film, '
              'of ANOTHER place: use it ONLY for the drawing, the treatment and '
              'the palette, never for the place, the people or the framing. '
              '%sMatch its DRAWING exactly: a flat graphic illustration built '
              'from broad simplified tonal planes, no rendered texture anywhere, '
              'no photographic detail. This picture must look like it was drawn '
              'by the same hand as that plate, not like a photograph.')

# placa aprobada -> identificador de Magnific de la candidata elegida (lo
# escribe quien elige; vive en D:\DAE\_tmp\dh\placa_id.json)
PLACA_ID_J = os.path.join(TMP, 'placa_id.json')


def placa_id():
    for f in (PLACA_ID_J, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       'placa_id_dh.json')):
        if os.path.exists(f):
            return json.load(open(f, encoding='utf-8'))
    return {}


def refs_de(ref):
    """Placas de referencia en el ORDEN del pedido (despues de las hojas):
    REF_PLACA trae primero la del mismo plano/lugar, que va al FINAL."""
    if not ref:
        return None
    lst = ref[0] if isinstance(ref[0], (list, tuple)) else [ref[0]]
    return list(lst[1:]) + [lst[0]]


# 31 oct (Sebastian, en vivo): la piel de las candidatas se iba saturando de
# plano en plano. Las referencias ya suben con la piel de la serie
# (`piel_ref`); la placa de referencia es ademas el TECHO de color de la piel.
REF_PIEL = (' Match its SKIN exactly too: the same flat warm GREY, never warmer, '
            'pinker, more peach or more saturated than the skin in that plate.')


def con_ref(cuerpo, ref, hojas):
    if ref[1] == 'mismo':
        extra = REF_MISMO % ref[2]
    elif ref[1] == 'estilo':
        extra = REF_ESTILO % ((ref[2] + ' ') if ref[2] else '')
    else:
        extra = REF_LUGAR % ((ref[2] + ' ') if ref[2] else '')
    extra += REF_PIEL
    if hojas:
        # con placas de referencia la hoja ya no es «la» referencia
        cuerpo = cuerpo.replace('The reference image is a character model sheet',
                                'The FIRST reference image is a character model sheet')
        cuerpo = cuerpo.replace('The reference images are character model sheets',
                                'The FIRST reference images are character model sheets')
    return cuerpo.strip() + '\n\n' + extra


def E(clave):
    return __import__('escenas_dh_%s' % clave.lower())


def nombre(clave, n):
    return 'DH_%s_r%02d_%s' % (clave, n, E(clave).NOMBRE[n])


def video(clave):
    mod = E(clave)
    falla, tot, racha = mod.comprobar()
    assert not falla, (clave, falla)
    out = {'tema': clave, 'carpeta': TEMAS[clave][0], 'placas': {},
           'detalles': {}, 'broll': {}, 'mov': mod.MOV,
           'lower_third': mod.LOWER_THIRD}
    reusa = getattr(mod, 'REUSA', {})
    PID = placa_id()
    for n, (cuad, reg, gente, acento, sil, lugar, txt) in sorted(mod.R.items()):
        if n in reusa:
            m, cam = reusa[n]
            out['placas'][nombre(clave, n)] = {
                'ranura': n, 'cuadros': cuad, 'luz': reg, 'gente': list(gente),
                'lugar': lugar, 'hojas': [], 'cenital': False,
                'carton_sugerido': n in mod.CARTONES, 'reusa': nombre(clave, m),
                'camara': cam, 'prompt': None}
            continue
        cuerpo = txt % S.TOKENS if '%(' in txt else txt
        if n in mod.CENITALES:
            cuerpo = cuerpo.strip() + '\n\n' + UNA_IMAGEN
        hojas = mod.HOJAS.get(n, [])
        if hojas:
            cuerpo = cuerpo.strip() + '\n\n' + (HOJA_REF if len(hojas) == 1
                                                 else HOJAS_REF)
        # en los planos de solo manos no va la clausula de rostro: pedir
        # caras donde no las hay hace que el modelo las meta
        manos = n in (getattr(mod, 'SOLO_MANOS', set()) | getattr(mod, 'SIN_CARA', set()))
        ref = getattr(mod, 'REF_PLACA', {}).get(n)
        if ref:
            cuerpo = con_ref(cuerpo, ref, hojas)
        p = S.arma(cuerpo, registro=reg, personas=gente, con_acento=acento,
                   lugar=lugar, silueta=sil, con_rostro=not manos)
        out['placas'][nombre(clave, n)] = {'ref_placa': refs_de(ref),
            'ref_ids': [PID.get(x) for x in (refs_de(ref) or [])],
            'ranura': n, 'cuadros': cuad, 'luz': reg, 'gente': list(gente),
            'lugar': lugar, 'hojas': hojas, 'hojas_id': [HOJA_ID[h] for h in hojas],
            'cenital': n in mod.CENITALES, 'carton_sugerido': n in mod.CARTONES,
            'prompt': p}
    # 31 oct: placas que no son una ranura entera (EXTRA), para las ranuras
    # compuestas (COMPUESTAS): mismo trato que una placa, con su hoja.
    out['extras'] = {}
    for k, (nom, reg, gente, acento, sil, lugar, txt, hojas) in sorted(
            getattr(mod, 'EXTRA', {}).items()):
        cuerpo = txt % S.TOKENS if '%(' in txt else txt
        if hojas:
            cuerpo = cuerpo.strip() + '\n\n' + (HOJA_REF if len(hojas) == 1
                                                 else HOJAS_REF)
        ref = getattr(mod, 'REF_PLACA', {}).get(k)
        if ref:
            cuerpo = con_ref(cuerpo, ref, hojas)
        p = S.arma(cuerpo, registro=reg, personas=gente, con_acento=acento,
                   lugar=lugar, silueta=sil, con_rostro=True)
        out['extras']['DH_%s_r%s_%s' % (clave, k, nom)] = {
            'ref_placa': refs_de(ref),
            'ref_ids': [PID.get(x) for x in (refs_de(ref) or [])],
            'clave': k, 'luz': reg, 'gente': list(gente), 'lugar': lugar,
            'hojas': hojas, 'hojas_id': [HOJA_ID[h] for h in hojas], 'prompt': p}
    for (n, nom), d in sorted(mod.DET.items()):
        madre = nombre(clave, n)
        gente = d.get('personas', out['placas'][madre]['gente'])
        # un detalle sobre una ranura que reusa placa: la referencia es la madre real
        base = out['placas'][madre].get('reusa') or madre
        if d.get('ref'):
            # 31 oct, noche (U1 r05, la moto): un inserto de OTRO lugar dentro
            # de la ranura. No es «el mismo plano mas cerrado»: lleva hoja,
            # cara y su placa de lugar, como una placa.
            esc = d['escena'] % S.TOKENS if '%(' in d['escena'] else d['escena']
            hojas = d.get('hojas', [])
            if hojas:
                esc = esc.strip() + '\n\n' + (HOJA_REF if len(hojas) == 1 else HOJAS_REF)
            esc = con_ref(esc, d['ref'], hojas)
            p = S.arma(esc, registro=d['registro'], personas=tuple(gente),
                       lugar=d.get('lugar', out['placas'][madre]['lugar']),
                       con_rostro=True)
            refs = refs_de(d['ref'])
            out['detalles']['DH_%s_r%02d_%s_det' % (clave, n, nom)] = {
                'ranura': n, 'madre': madre, 'placa_ref': refs[-1],
                'placa_ref_id': PID.get(refs[-1]), 'ref_placa': refs,
                'ref_ids': [PID.get(x) for x in refs], 'hojas': hojas,
                'hojas_id': [HOJA_ID[h] for h in hojas], 'cuadros': d['cuadros'],
                'entra': d['entra'], 'prompt_placa': p,
                'prompt_video': d['gesto'] + ' ' + QUIETO}
            continue
        # un detalle es una mano sobre su objeto: sin clausula de rostro
        p = S.arma(d['escena'] + '\n\n' + REFERENCIA, registro=d['registro'],
                   personas=tuple(gente), lugar=out['placas'][madre]['lugar'],
                   con_rostro=False)
        out['detalles']['DH_%s_r%02d_%s_det' % (clave, n, nom)] = {
            'ranura': n, 'madre': madre, 'placa_ref': base,
            'placa_ref_id': PID.get(base), 'cuadros': d['cuadros'],
            'entra': d['entra'], 'prompt_placa': p,
            'prompt_video': d['gesto'] + ' ' + QUIETO}
    for nom, (reg, esc) in sorted(mod.BROLL.items()):
        out['broll']['DH_%s_broll_%s' % (clave, nom)] = {
            'luz': reg, 'prompt': S.arma(esc, registro=reg)}
    return out, tot, racha


def md(o, cruce=None):
    k = o['tema']
    carpeta, voz, tema, titulo = TEMAS[k]
    s = ['# %s · %s' % (tema, carpeta.split(' - ', 1)[1]), '',
         '*%s* — %s del curso. Narra: %s. Storyboard escrito: guion '
         'verbatim, ranuras y prompts. Generado por `prompts_dh.py`.'
         % (titulo, tema, voz), '', '## Guion (verbatim)', '']
    for i, v, t, tts, p in bloques(k):
        s += ['**%s** · %s · pausa %.1f s' % (i, v, p), '', t, '']
    s += ['## Ranuras', '',
          '| ranura | cuadros | luz | gente | hojas | cartón | se oye |',
          '|---|---|---|---|---|---|---|']
    for nm, v in o['placas'].items():
        oye = (cruce or {}).get(v['ranura'], '')
        s.append('| %s | %d | %s%s | %s | %s | %s | %s |'
                 % (nm, v['cuadros'], v['luz'], ' · cenital' if v['cenital'] else '',
                    ', '.join(v['gente']) or '—',
                    ('= ' + v['reusa']) if v.get('reusa') else (', '.join(v['hojas']) or ''),
                    'sí' if v['carton_sugerido'] else '', oye))
    s += ['', 'Rótulo: ' + '; '.join('r%02d «%s»' % (n, t)
                                      for n, t in sorted(o['lower_third'].items())),
          '', '## Prompts de placa', '']
    for nm, v in o['placas'].items():
        if v.get('reusa'):
            s += ['### %s' % nm, '', 'reusa la placa de `%s` con cámara %s'
                  % (v['reusa'], v['camara']), '']
            continue
        s += ['### %s' % nm, '', '```', v['prompt'], '```', '']
    s += ['## Planos de detalle (V3 DETALLE)', '']
    for nm, v in o['detalles'].items():
        s += ['### %s' % nm, '', 'madre `%s` · %d cuadros · entra en %d'
              % (v['madre'], v['cuadros'], v['entra']), '',
              '**placa**', '', '```', v['prompt_placa'], '```', '',
              '**video (Kling, keyframe de inicio = placa)**', '', '```',
              v['prompt_video'], '```', '']
    s += ['## B-roll de reserva', '']
    for nm, v in o['broll'].items():
        s += ['### %s' % nm, '', '```', v['prompt'], '```', '']
    s += ['## Movimiento (candidatos)', '']
    for n, t in sorted(o['mov'].items()):
        s.append('- r%02d: %s' % (int(n), t))
    return '\n'.join(s) + '\n'


def cruce_de(clave, ruta):
    """Lo que se oye encima de cada ranura, de los tiempos de Scribe."""
    if not ruta or not os.path.exists(ruta):
        return {}
    d = json.load(open(ruta, encoding='utf-8'))[clave]
    fps = 24000 / 1001.0
    ran = d['ranuras']['ranuras']
    out = {}
    for i, r in enumerate(ran, 1):
        a, b = r['ini'] / fps, (r['ini'] + r['dur']) / fps
        out[i] = ' '.join(w[2] for w in d['words'] if a <= w[0] < b)
    return out


if __name__ == '__main__':
    aqui = None
    if '--aqui' in sys.argv:
        aqui = sys.argv[sys.argv.index('--aqui') + 1]
    cruce = sys.argv[sys.argv.index('--cruce') + 1] if '--cruce' in sys.argv \
        else os.path.join(TMP, 'cruce_dh.json')
    if not aqui:
        import rutas_dh as R
    os.makedirs(aqui or TMP, exist_ok=True)
    for k in VIDEOS:
        o, tot, racha = video(k)
        texto = md(o, cruce_de(k, cruce))
        destino_json = os.path.join(aqui or TMP, 'prompts_dh_%s.json' % k)
        json.dump(o, open(destino_json, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        dmd = aqui or R.sub(k, '06 GUION Y STORYBOARD')
        with open(os.path.join(dmd, 'DH_%s_storyboard.md' % k), 'w',
                  encoding='utf-8') as f:
            f.write(texto)
        print('%s  %2d placas  %d detalles  %d broll  %5d cuadros  racha %d'
              % (k, len(o['placas']), len(o['detalles']), len(o['broll']),
                 tot, racha))
    print('LISTO')
