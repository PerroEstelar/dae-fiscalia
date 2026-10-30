# -*- coding: utf-8 -*-
r"""Arma todos los prompts de Justicia restaurativa y los deja donde se usan.

Por cada tema:
    - una placa por ranura (`escenas_jr_t<n>.R`), con las comprobaciones de
      la serie: los cuadros suman lo que dice la rejilla, no hay mas de tres
      ranuras seguidas sin gente, no hay mas de tres cenitales;
    - las HOJAS de personaje que entran como referencia en cada placa;
    - los insertos de detalle (`DET`) para la pista V3 DETALLE, cada uno con
      su placa -que se pide con la placa madre como referencia- y su gesto
      para Kling, con la clausula de quietud de la serie;
    - el b-roll de reserva (`BROLL`), las notas de movimiento (`MOV`) y el
      rotulo (`LOWER_THIRD`).

Sale un json por tema en D:\DAE\_tmp\jr y, en la carpeta de guion de cada
tema, un .md legible con el guion verbatim, las ranuras con lo que se oye
encima y cada prompt: el storyboard escrito, para mirarlo antes de gastar un
credito.

    python prompts_jr.py            (en la maquina de Sebastian)
    python prompts_jr.py --aqui DIR (en otra: escribe todo en DIR)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import base_jr as S                              # noqa: E402
from guion_jr import TEMAS, VIDEOS, bloques     # noqa: E402

TMP = r'D:\DAE\_tmp\jr'

# las hojas de personaje ya son creaciones de Magnific: entran como
# referencia por su identificador (Seedream 5 Flash, 30 oct)
HOJA_ID = {'ana': 'fHiDlMKCDY', 'fiscal1': 'fHiDlerCDY', 'camilo': 'Bh7z50boQR',
           'diego': 'VXLiuZfMMU', 'mario': 'tCPcxpumZJ', 'juana': 'P3hrVU142C'}

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
              'style. It must be indistinguishable from it in treatment.')

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
            'composed as described above, with each person appearing ONCE.')

HOJAS_REF = ('The reference images are character model sheets: use them ONLY '
             'for the identity of the people -face, hair, build and clothes- '
             'and for the drawing style. Ignore their framing, their grey '
             'background, their poses and their repeated views: this picture '
             'is ONE scene, composed as described above, with each person '
             'appearing ONCE.')


def E(clave):
    return __import__('escenas_jr_%s' % clave.lower())


def nombre(clave, n):
    return 'JR_%s_r%02d_%s' % (clave, n, E(clave).NOMBRE[n])


def video(clave):
    mod = E(clave)
    falla, tot, racha = mod.comprobar()
    assert not falla, (clave, falla)
    out = {'tema': clave, 'carpeta': TEMAS[clave][0], 'placas': {},
           'detalles': {}, 'broll': {}, 'mov': mod.MOV,
           'lower_third': mod.LOWER_THIRD}
    reusa = getattr(mod, 'REUSA', {})
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
        p = S.arma(cuerpo, registro=reg, personas=gente, con_acento=acento,
                   lugar=lugar, silueta=sil, con_rostro=not manos)
        out['placas'][nombre(clave, n)] = {
            'ranura': n, 'cuadros': cuad, 'luz': reg, 'gente': list(gente),
            'lugar': lugar, 'hojas': hojas, 'hojas_id': [HOJA_ID[h] for h in hojas],
            'cenital': n in mod.CENITALES, 'carton_sugerido': n in mod.CARTONES,
            'prompt': p}
    for (n, nom), d in sorted(mod.DET.items()):
        madre = nombre(clave, n)
        gente = d.get('personas', out['placas'][madre]['gente'])
        # un detalle sobre una ranura que reusa placa: la referencia es la madre real
        base = out['placas'][madre].get('reusa') or madre
        # un detalle es una mano sobre su objeto: sin clausula de rostro
        p = S.arma(d['escena'] + '\n\n' + REFERENCIA, registro=d['registro'],
                   personas=tuple(gente), lugar=out['placas'][madre]['lugar'],
                   con_rostro=False)
        out['detalles']['JR_%s_r%02d_%s_det' % (clave, n, nom)] = {
            'ranura': n, 'madre': madre, 'placa_ref': base, 'cuadros': d['cuadros'],
            'entra': d['entra'], 'prompt_placa': p,
            'prompt_video': d['gesto'] + ' ' + QUIETO}
    for nom, (reg, esc) in sorted(mod.BROLL.items()):
        out['broll']['JR_%s_broll_%s' % (clave, nom)] = {
            'luz': reg, 'prompt': S.arma(esc, registro=reg)}
    return out, tot, racha


def md(o, cruce=None):
    k = o['tema']
    carpeta, voz, tema, titulo = TEMAS[k]
    s = ['# %s · %s' % (tema, carpeta.split(' - ', 1)[1]), '',
         '*%s* — caso introductorio. Voz: %s. Storyboard escrito: guion '
         'verbatim, ranuras y prompts. Generado por `prompts_jr.py`.'
         % (titulo, voz), '', '## Guion (verbatim)', '']
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
        else os.path.join(TMP, 'cruce_jr.json')
    if not aqui:
        import rutas_jr as R
    os.makedirs(aqui or TMP, exist_ok=True)
    for k in VIDEOS:
        o, tot, racha = video(k)
        texto = md(o, cruce_de(k, cruce))
        destino_json = os.path.join(aqui or TMP, 'prompts_jr_%s.json' % k)
        json.dump(o, open(destino_json, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        dmd = aqui or R.sub(k, '06 GUION Y STORYBOARD')
        with open(os.path.join(dmd, 'JR_%s_storyboard.md' % k), 'w',
                  encoding='utf-8') as f:
            f.write(texto)
        print('%s  %2d placas  %d detalles  %d broll  %5d cuadros  racha %d'
              % (k, len(o['placas']), len(o['detalles']), len(o['broll']),
                 tot, racha))
    print('LISTO')
