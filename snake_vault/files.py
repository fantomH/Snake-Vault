# :----------------------------------------------------------------------- INFO
# :[snake_vault/files.py]
# /author        : fantomH
# /created       : 2024-02-23 20:11:19 UTC
# /updated       : 2024-05-20 21:32:27 UTC
# /description   : Files utilities.

import csv
import hashlib
import os
import magic

def file_info(f, filename=True,
                 path=True,
                 size=True,
                 mime=True,
                 md5=True):
    '''
    f must be an absolute path.
    
    '''

    FILE_INFO = {}

    if os.path.isfile(f):
        if filename:
            FILE_INFO['filename'] = os.path.basename(f)

        if path:
            FILE_INFO['path'] = os.path.abspath(f)

        if size:
            FILE_INFO['size'] = os.path.getsize(f)

        if md5:
            md5 = hashlib.md5()
            filepath = os.path.abspath(f).encode('UTF-8', 'surrogateescape')
            with open(filepath, 'rb') as _INPUT:
                for line in _INPUT:
                    md5.update(line)
                FILE_INFO['md5sum'] = md5.hexdigest()
        if mime:
            FILE_INFO['mime'] = magic.from_file(f, mime=True)

    else:
        return

    return FILE_INFO

def _test_file_info():

    PATH = '/usr/local/bin'
    for root, dirs, files in os.walk(PATH):
        for file in files:
            print(file_info(os.path.join(root, file), mime=True))
