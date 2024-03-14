## ----------------------------------------------------------------------- INFO
## [snake_vault/files.py]
## author        : fantomH
## created       : 2024-02-23 20:11:19 UTC
## updated       : 2024-02-23 20:11:19 UTC
## description   : Files utilities.

import os
import hashlib
import csv

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

        try:
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
        except:
            FILE_INFO = {}
            FILE_INFO['path'] = "PASS"
            FILE_INFO['filename'] = "PASS"
            FILE_INFO['size'] = "PASS"
            FILE_INFO['md5sum'] = "PASS"

            return FILE_INFO
    return False

list_of_directories = [ '/home/ghost/main/radimed/' ]
_newline = "\n"
with open('/home/ghost/tmp/filesmd5.csv', mode="w") as _output:
    fieldnames = ['filename', 'path', 'size', 'md5sum']
    writer = csv.DictWriter(_output, fieldnames=fieldnames)

    for directory in list_of_directories:
        for root, dirs, files in os.walk(directory):
            if "/.git/" not in root:
                for file in files:
                    _info = file_info(os.path.join(root.encode('UTF-8', 'surrogateescape'), file.encode('UTF-8', 'surrogateescape')))
                    writer.writerow(_info)

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
