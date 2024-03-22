## ----------------------------------------------------------------------- INFO
## [snake_vault/flask/app/utils.py]
## author        : fantomH
## created       : 2024-03-21 02:03:31 UTC
## updated       : 2024-03-21 02:03:31 UTC
## description   : Flask utils.

from flask import (jsonify,
                   request,
                   Response)
import json
HELL = 'yes'

def get_ip():

    """
    Get IP address from connected clients.
    ref. https://stackoverflow.com/questions/3759981/get-ip-address-of-visitors-using-flask-for-python
    """

    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
        
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
