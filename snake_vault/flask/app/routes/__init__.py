# :----------------------------------------------------------------------- INFO
# [Snake-Vault/snake_vault/flask/app/routes/__init__.py]
# /author        : fantomH
# /created       : 2024-01-07 03:47:37 UTC
# /updated       : 2024-04-17 11:25:23 UTC
# /description   : Default routes

from flask import (Blueprint,
                   current_app,
                   render_template)
from flask_login import (current_user)

# :----- [STATUS]

status = Blueprint("status", __name__)

# :(404)
@status.errorhandler(404)
def not_found(e):
    title = "404"
    return render_template("status/404.html", title=title, user=current_user)

# :------------------------------------------------------------- FIN ¯\_(ツ)_/¯
