# -*- coding: utf-8 -*-
r"""Que voz (y que modelo y ajustes) narro cada caso del profe Carlos Humberto
en la V1, para que los tramos nuevos suenen igual.

    python ch_voces_origen.py

Busca en el historial de ElevenLabs de la cuenta propia (llave en
D:\DAE\_secretos\elevenlabs.txt; nunca se imprime) los textos con nombres de
los casos, y lista los proyectos de Studio. Escribe
D:\DAE\_tmp\ch\eleven_hist.json.
"""
import json
import time
import urllib.parse
import urllib.request

KEY = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()
CLAVES = ['santiago', 'valeria', 'valentina', 'rodman', 'disney', 'arley', 'susana',
          'juan', 'lenin', 'jimmy', 'ibagu', 'cúcuta', 'cucuta', 'mariano ramos',
          'principio de oportunidad', 'psicosocial']


def get(path, **q):
    u = 'https://api.elevenlabs.io' + path + ('?' + urllib.parse.urlencode(q) if q else '')
    req = urllib.request.Request(u, headers={'xi-api-key': KEY})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode('utf-8'))


def main():
    out = {'historial': [], 'proyectos': [], 'voces': {}}
    last = None
    vistos = 0
    for _ in range(40):
        q = {'page_size': 1000}
        if last:
            q['start_after_history_item_id'] = last
        h = get('/v1/history', **q)
        items = h.get('history', [])
        for it in items:
            vistos += 1
            t = (it.get('text') or '').lower()
            if any(k in t for k in CLAVES):
                out['historial'].append({
                    'id': it.get('history_item_id'), 'fecha': time.strftime(
                        '%Y-%m-%d %H:%M', time.localtime(it.get('date_unix', 0))),
                    'voz': it.get('voice_name'), 'voice_id': it.get('voice_id'),
                    'modelo': it.get('model_id'), 'ajustes': it.get('settings'),
                    'texto': it.get('text', '')[:160]})
        if not h.get('has_more') or not items:
            break
        last = h.get('last_history_item_id') or items[-1].get('history_item_id')
    out['vistos'] = vistos
    try:
        for p in get('/v1/studio/projects').get('projects', []):
            out['proyectos'].append({k: p.get(k) for k in (
                'project_id', 'name', 'create_date_unix', 'default_paragraph_voice_id',
                'default_model_id', 'state')})
    except Exception as e:                                     # noqa: BLE001
        out['proyectos_error'] = str(e)[:200]
    try:
        for v in get('/v1/voices').get('voices', []):
            out['voces'][v['voice_id']] = v.get('name')
    except Exception as e:                                     # noqa: BLE001
        out['voces_error'] = str(e)[:200]
    json.dump(out, open(r'D:\DAE\_tmp\ch\eleven_hist.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('historial revisado', vistos, 'coincidencias', len(out['historial']),
          'proyectos', len(out['proyectos']))


if __name__ == '__main__':
    main()
