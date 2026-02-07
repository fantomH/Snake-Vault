# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_enigma/md5.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2024-05-30 12:04:28 UTC
# updated       : 2026-02-06 12:29:54 UTC
# description   : MD5 manipulation.

"""
MD5 manipulation.
"""

import hashlib

def file_md5sum(filepath):
    '''
    Calculate the md5sum of a file.
    '''

    md5 = hashlib.md5()

    with open(filepath, "rb") as _input:
        for chunk in iter(lambda: _input.read(4096), b""):
            md5.update(chunk)

    return md5.hexdigest()
