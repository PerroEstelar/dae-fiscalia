#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bajar creaciones de Magnific a disco, y de una importarlas a Resolve.

POR QUÉ EXISTE
    La sesión de Claude corre en un contenedor en la nube cuya salida a
    internet no alcanza el CDN de Magnific (`pikaso.cdnpk.net` responde 403 al
    proxy). La máquina de Sebastián sí lo alcanza. Entonces Claude arma el
    manifiesto y lo ejecuta acá, con `script_plugin run_inline`, que es un
    Python completo sobre esta máquina y ve E: y D:.

CÓMO SE USA
    python bajar_de_magnific.py manifiesto.json
    python bajar_de_magnific.py manifiesto.json --sin-importar

    o, desde Claude, sin archivo de por medio:
        import bajar_de_magnific as m
        m.bajar(manifiesto_dict)

EL MANIFIESTO
    {
      "destino":  "E:\\\\DAE MASTER\\\\CURSO 4 ...\\\\CASO 02 ...\\\\01 PLANOS",
      "carpeta_pool": ["CURSO 4 - TERMINACIONES ANTICIPADAS",
                       "CASO 02 - doble beneficio y reintegro", "01 PLANOS"],
      "archivos": [
        {"nombre": "KF02_la_entrega_vA.png", "url": "https://pikaso..."},
        {"nombre": "KF02_la_entrega_vB.png", "url": "https://pikaso...",
         "destino": "...otra carpeta si este archivo va a otro lado..."}
      ]
    }

    `carpeta_pool` es opcional: si está, los archivos bajados se importan a esa
    carpeta del media pool del proyecto abierto. Las rutas de carpeta se
    comparan sin distinguir mayúsculas ni espacios de los bordes, porque en el
    proyecto hay una carpeta que se llama " 00 COMUNES", con espacio adelante.

LO QUE CUIDA
    — Las URL de Magnific llevan un token con vencimiento. Si una devuelve 403
      o 410, el token ya venció: hay que volver a pedir la URL con
      `creations_wait`, no reintentar.
    — Reintenta tres veces los errores de red, con espera creciente.
    — No pisa un archivo existente sin avisar: lo renombra a `<nombre>.bak`.
    — Verifica que lo bajado pese algo y, si es PNG o MOV, que el encabezado
      sea el que dice ser. Un HTML de error pesa 2 KB y se cuela sin esto.
"""
import json, os, shutil, sys, time, urllib.error, urllib.request

MAGIA = {
    b"\x89PNG\r\n\x1a\n": ".png",
    b"\xff\xd8\xff": ".jpg",
    b"RIFF": ".wav",
    b"ID3": ".mp3",
    b"\xff\xfb": ".mp3",
}


def _parece_lo_que_dice(ruta, ext=None):
    """ext: la extensión del DESTINO. Se pasa a mano porque el archivo que se
    revisa es el temporal `.parcial`, y mirarle la extensión a él hacía que
    todo fallara."""
    ext = (ext or os.path.splitext(ruta)[1]).lower()
    with open(ruta, "rb") as fh:
        cab = fh.read(12)
    if ext in (".mov", ".mp4", ".m4a"):
        return cab[4:8] == b"ftyp" or cab[4:8] == b"moov" or cab[4:8] == b"mdat"
    for firma, e in MAGIA.items():
        if cab.startswith(firma):
            return e == ext or (e == ".mp3" and ext == ".mp3")
    return ext not in (".png", ".jpg", ".wav", ".mp3")


def _bajar_uno(url, destino, intentos=3):
    tmp = destino + ".parcial"
    ultimo = None
    for i in range(intentos):
        try:
            urllib.request.urlretrieve(url, tmp)
            break
        except urllib.error.HTTPError as e:
            if e.code in (403, 410):
                raise RuntimeError(
                    f"{e.code}: el token de la URL venció. Hay que volver a pedir la "
                    f"URL con creations_wait; reintentar no sirve."
                ) from e
            ultimo = e
        except Exception as e:                      # red, DNS, timeout
            ultimo = e
        time.sleep(2 * (i + 1))
    else:
        raise RuntimeError(f"no pude bajar después de {intentos} intentos: {ultimo}")

    if os.path.getsize(tmp) < 1024:
        os.remove(tmp)
        raise RuntimeError("lo que bajó pesa menos de 1 KB — probablemente es una página de error")
    if not _parece_lo_que_dice(tmp, os.path.splitext(destino)[1]):
        os.remove(tmp)
        raise RuntimeError("lo que bajó no tiene el encabezado del formato que dice la extensión")

    if os.path.exists(destino):
        shutil.move(destino, destino + ".bak")
    shutil.move(tmp, destino)
    return os.path.getsize(destino)


def _carpeta_pool(mp, ruta):
    f = mp.GetRootFolder()
    for n in ruta:
        sig = None
        for s in f.GetSubFolderList():
            if s.GetName().strip().upper() == n.strip().upper():
                sig = s
                break
        if sig is None:
            return None
        f = sig
    return f


def bajar(manifiesto, importar=True):
    base = manifiesto.get("destino")
    bajados, fallidos = [], []
    for a in manifiesto["archivos"]:
        dest_dir = a.get("destino", base)
        if not dest_dir:
            fallidos.append((a["nombre"], "no hay destino"))
            continue
        os.makedirs(dest_dir, exist_ok=True)
        ruta = os.path.join(dest_dir, a["nombre"])
        try:
            n = _bajar_uno(a["url"], ruta)
            bajados.append(ruta)
            print(f"  ok   {a['nombre']}  {n // 1024} KB")
        except Exception as e:
            fallidos.append((a["nombre"], str(e)))
            print(f"  FALLO {a['nombre']}: {e}")

    if importar and bajados and manifiesto.get("carpeta_pool"):
        try:
            import DaVinciResolveScript as dvr      # noqa
            r = dvr.scriptapp("Resolve")
        except Exception:
            r = globals().get("resolve")
        if r is None:
            print("  (Resolve no está a la mano: no importé nada)")
        else:
            mp = r.GetProjectManager().GetCurrentProject().GetMediaPool()
            f = _carpeta_pool(mp, manifiesto["carpeta_pool"])
            if f is None:
                print("  (no encontré la carpeta del pool:", manifiesto["carpeta_pool"], ")")
            else:
                mp.SetCurrentFolder(f)
                imp = mp.ImportMedia(bajados)
                print(f"  importados al pool: {len(imp or [])} en «{f.GetName()}»")

    print(f"\n{len(bajados)} bajados, {len(fallidos)} fallidos")
    for n, e in fallidos:
        print("   ·", n, "—", e)
    return bajados, fallidos


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        raise SystemExit(2)
    with open(args[0], encoding="utf-8") as fh:
        man = json.load(fh)
    bajar(man, importar="--sin-importar" not in sys.argv)
