# :----------------------------------------------------------------------- INFO
# :[snake_vault/enigma.py]
# /author        : fantomH
# /created       : 2024-05-30 12:04:28 UTC
# /updated       : 2024-05-30 12:04:28 UTC
# /description   : Hash, cipher, encryption...

import hashlib

# :-----/ (function) md5sum /-----:
def md5sum(filepath):

    md5 = hashlib.md5()

    with open(filepath, "rb") as _input:
        for chunk in iter(lambda: _input.read(4096), b""):
            md5.update(chunk)

    return md5.hexdigest()
