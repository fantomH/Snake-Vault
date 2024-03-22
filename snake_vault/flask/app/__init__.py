## ----------------------------------------------------------------------- INFO
## [snake_vault/flask/app/__init__.py]
## author        : fantomH 
## created       : 2024-03-21 01:43:40 UTC
## updated       : 2024-03-21 01:43:40 UTC
## description   : Basic flask app factory.

import json
from flask import (Flask)

from .utils import get_ip

def init_app():

    app = Flask(__name__)

    @app.route("/")
    def home():
        data = get_ip()
        print(data)
        return data

    return app

## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
