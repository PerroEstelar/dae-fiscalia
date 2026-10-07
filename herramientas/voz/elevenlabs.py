#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ElevenLabs por API, para las voces de la serie DAE.

LA LLAVE NO VIVE AQUÍ NI EN EL REPOSITORIO
    Se lee de la variable de entorno `ELEVENLABS_API_KEY` o, si no está, de la
    primera línea de `D:\\DAE\\_secretos\\elevenlabs.txt`. Esa carpeta está fuera
    del repositorio y además en el .gitignore. El script nunca la imprime: donde
    tiene que mostrarla, muestra los últimos cuatro caracteres.

USO
    python elevenlabs.py voces
    python elevenlabs.py voces --buscar colombia
    python elevenlabs.py cuota
    python elevenlabs.py decir <archivo_de_texto> <voice_id> <salida.mp3>
    python elevenlabs.py lote <carpeta_de_textos> <voice_id> <carpeta_salida>

    `lote` toma todos los .txt de una carpeta y genera un mp3 por cada uno, con
    el mismo nombre. Es la forma de pedir las seis pistas de una sentada.

NIVELES
    Lo que sale de aquí es material crudo. El master a −19 LUFS / −1,0 dBTP /
    estéreo dual-mono 48 kHz se hace después, con loudnorm en DOS pasadas: una
    sola pasada estima mal (se pidió −19 y dio −16).
"""
import json
import os
import sys
import urllib.error
import urllib.request

BASE = "https://api.elevenlabs.io/v1"
LLAVE_ARCHIVO = r"D:\DAE\_secretos\elevenlabs.txt"

# El multilingüe v2 es el que sostiene el acento latino neutro sin derivar a
# español peninsular. Si se cambia de modelo hay que volver a oír una pista
# completa antes de pedir las seis.
MODELO = "eleven_multilingual_v2"

# Para locución institucional: estabilidad alta para que no haga interpretación,
# similitud alta para que no se despegue de la voz escogida, y nada de style,
# que es lo que mete el dramatismo de audiolibro.
AJUSTES = {
    "stability": 0.50,
    "similarity_boost": 0.80,
    "style": 0.0,
    "use_speaker_boost": True,
}


def llave():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k and os.path.exists(LLAVE_ARCHIVO):
        with open(LLAVE_ARCHIVO, encoding="utf-8") as f:
            k = f.readline().strip()
    if not k:
        sys.exit(
            "No hay llave.\n"
            "  Opción A: crear %s con la llave en la primera línea.\n"
            "  Opción B: definir la variable de entorno ELEVENLABS_API_KEY.\n"
            % LLAVE_ARCHIVO
        )
    return k


def _pedir(ruta, datos=None, binario=False):
    req = urllib.request.Request(
        BASE + ruta,
        data=json.dumps(datos).encode("utf-8") if datos is not None else None,
        headers={
            "xi-api-key": llave(),
            "Content-Type": "application/json",
            "Accept": "audio/mpeg" if binario else "application/json",
        },
        method="POST" if datos is not None else "GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.read() if binario else json.loads(r.read())
    except urllib.error.HTTPError as e:
        cuerpo = e.read().decode("utf-8", "replace")[:500]
        sys.exit("ElevenLabs respondió %s: %s" % (e.code, cuerpo))


def voces(buscar=None):
    datos = _pedir("/voices")
    filas = []
    for v in datos.get("voices", []):
        et = v.get("labels") or {}
        linea = "%-22s %-24s %s" % (
            v.get("voice_id", "")[:22],
            (v.get("name") or "")[:24],
            " · ".join(filter(None, [et.get("accent"), et.get("gender"),
                                     et.get("age"), et.get("use_case"),
                                     v.get("category")])),
        )
        if buscar and buscar.lower() not in linea.lower():
            continue
        filas.append(linea)
    print("%-22s %-24s %s" % ("VOICE_ID", "NOMBRE", "ETIQUETAS"))
    for f in sorted(filas, key=lambda x: x[23:]):
        print(f)
    print("\n%d voces" % len(filas))


def cuota():
    d = _pedir("/user/subscription")
    usados = d.get("character_count", 0)
    tope = d.get("character_limit", 0)
    print("plan:       %s" % d.get("tier"))
    print("caracteres: %s de %s  (quedan %s)" % (usados, tope, tope - usados))
    print("llave:      …%s" % llave()[-4:])


def decir(texto, voice_id, salida):
    audio = _pedir(
        "/text-to-speech/%s?output_format=mp3_44100_192" % voice_id,
        {"text": texto, "model_id": MODELO, "voice_settings": AJUSTES},
        binario=True,
    )
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    with open(salida, "wb") as f:
        f.write(audio)
    print("%s  %d KB  (%d caracteres)" % (os.path.basename(salida),
                                          len(audio) // 1024, len(texto)))


def lote(carpeta_textos, voice_id, carpeta_salida):
    txts = sorted(f for f in os.listdir(carpeta_textos) if f.lower().endswith(".txt"))
    if not txts:
        sys.exit("No hay .txt en %s" % carpeta_textos)
    total = 0
    for t in txts:
        with open(os.path.join(carpeta_textos, t), encoding="utf-8") as f:
            texto = f.read().strip()
        total += len(texto)
        decir(texto, voice_id, os.path.join(carpeta_salida, t[:-4] + ".mp3"))
    print("\n%d pistas · %d caracteres en total" % (len(txts), total))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "voces":
        voces(a[2] if len(a) > 2 and a[1] == "--buscar" else None)
    elif a[0] == "cuota":
        cuota()
    elif a[0] == "decir":
        with open(a[1], encoding="utf-8") as f:
            decir(f.read().strip(), a[2], a[3])
    elif a[0] == "lote":
        lote(a[1], a[2], a[3])
    else:
        sys.exit(__doc__)
