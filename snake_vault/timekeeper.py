# :----------------------------------------------------------------------- INFO
# :[Snake-Vault/snake_vault/timekeeper.py]
# :author        : fantomH
# :created       : 2024-05-30 11:10:24 UTC
# :updated       : 2024-08-16 19:24:09 UTC
# :description   : Time utils.

import datetime

def time_as_id():
    '''
    time_as_id() returns a string representing the time now that can be used as
    an ID or a timestamp.

    example: 20240530111024
    '''

    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
