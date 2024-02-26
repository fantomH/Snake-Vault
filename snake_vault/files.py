## ----------------------------------------------------------------------- INFO
## [snake_vault/files.py]
## author        : fantomH
## created       : 2024-02-23 20:11:19 UTC
## updated       : 2024-02-23 20:11:19 UTC
## description   : Files utilities.

import os
import hashlib

def file_info(f):
    '''
    f must be an absolute path.
    
    For exemple:
    PATH = '/home/ghost/.ael'
    for f in os.listdir(PATH):
        FILE_INFO = file_info(os.path.join(PATH, f))
        if FILE_INFO:
            print(FILE_INFO)
    '''

    if os.path.isfile(f):

        FILE_INFO = {}
        FILE_INFO['path'] = os.path.abspath(f)
        FILE_INFO['filename'] = os.path.basename(f)
        FILE_INFO['size'] = os.path.getsize(f)

        md5 = hashlib.md5()
        with open(FILE_INFO.get('path'), 'rb') as _INPUT:
            for line in _INPUT:
                md5.update(line)
            FILE_INFO['md5sum'] = md5.hexdigest()

        return FILE_INFO
    return False

list_of_directories = [
                       '/home/ghost/main',
                       '/home/ghost/Downloads'
                      ]
for directory in list_of_directories:
    for root, dirs, files in os.walk(directory):
        if dirs != ".git":
            print(file_info(os.path.join(root, file)))

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
