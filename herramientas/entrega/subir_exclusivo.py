# -*- coding: utf-8 -*-
r"""Copia una entrega a «Mi unidad» para que Drive para escritorio la suba, sin que la pueda
leer a medias (17 nov 2026).

    python subir_exclusivo.py <origen> <nombre en Drive> <log> [carpeta en G:]

o, desde otro script, `copiar_exclusivo(origen, destino)`.

La entrega `enfoquediferencial - U5 - CIERRE-v1.mp4` quedó en Drive con el mismo tamaño que la
local y con todo el último 22 % en ceros (desde el byte 930.086.912): el reproductor se
congelaba en el minuto 22. La copia a G: se había hecho con `shutil.copy2`, que deja el archivo
con su tamaño final desde el principio y lo va llenando; Drive para escritorio lo leyó antes de
que terminara de escribirse.

Aquí el archivo `.parcial` se abre con `CreateFileW` y `dwShareMode = 0`: mientras se escribe,
nadie más lo puede abrir. Al cerrarlo se renombra al nombre final. Devuelve bytes y md5.

Esto evita el caso medido, pero no garantiza nada por sí solo: lo que vale es
`verificar_drive.py` sobre una copia de servidor del archivo subido.
"""
import ctypes
import ctypes.wintypes as W
import hashlib
import os
import sys
import time

GENERIC_WRITE, CREATE_ALWAYS, NORMAL = 0x40000000, 2, 0x80


def copiar_exclusivo(origen, destino):
    """Copia `origen` a `destino` pasando por `destino + '.parcial'`, sin compartir el
    archivo mientras se escribe. Devuelve (bytes, md5). Lanza OSError si algo falla."""
    k = ctypes.WinDLL('kernel32', use_last_error=True)
    k.CreateFileW.restype = W.HANDLE
    k.CreateFileW.argtypes = [W.LPCWSTR, W.DWORD, W.DWORD, ctypes.c_void_p, W.DWORD, W.DWORD,
                              W.HANDLE]
    tmp = destino + '.parcial'
    h = k.CreateFileW(tmp.replace('/', '\\'), GENERIC_WRITE, 0, None, CREATE_ALWAYS, NORMAL, None)
    if h is None or h == W.HANDLE(-1).value:
        raise OSError('no se pudo abrir %s (error %d)' % (tmp, ctypes.get_last_error()))
    md5 = hashlib.md5()
    n = 0
    escrito = W.DWORD()
    try:
        with open(origen, 'rb') as f:
            for c in iter(lambda: f.read(8 << 20), b''):
                md5.update(c)
                if not k.WriteFile(h, c, len(c), ctypes.byref(escrito), None) or escrito.value != len(c):
                    raise OSError('falla al escribir %s (error %d)' % (tmp, ctypes.get_last_error()))
                n += len(c)
        k.FlushFileBuffers(h)
    finally:
        k.CloseHandle(h)
    os.replace(tmp, destino)
    return n, md5.hexdigest()


if __name__ == '__main__':
    origen, nombre, logp = sys.argv[1], sys.argv[2], sys.argv[3]
    G = sys.argv[4] if len(sys.argv) > 4 else 'G:/My Drive/_MA subidas/'
    log = open(logp, 'w', encoding='utf-8')
    t = time.time()
    try:
        n, md5 = copiar_exclusivo(origen, G + nombre)
    except OSError as e:
        print('FALLO', e, file=log, flush=True)
        sys.exit(1)
    print('copiado', n, 'bytes en %.0f s' % (time.time() - t), 'md5', md5, file=log, flush=True)
    print('LISTO', file=log, flush=True)
