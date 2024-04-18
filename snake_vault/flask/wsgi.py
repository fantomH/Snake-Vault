# :----------------------------------------------------------------------- INFO
# [Snake-Vault/snake_vault/flask/wsgi.py]
# /author        : fantomH
# /created       : 2024-04-16 18:55:54 UTC
# /updated       : 2024-04-16 18:55:54 UTC
# /description   : Application launcher.

from app import (create_app)

app = create_app()

if __name__ init== "__main__":
    # /Using '0.0.0.0' enables the application to be available on other devices
    # /on the same network.
    app.run(host='0.0.0.0', debug=True)

# :------------------------------------------------------------- FIN ¯\_(ツ)_/¯
