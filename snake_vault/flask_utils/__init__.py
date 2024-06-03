# :----------------------------------------------------------------------- INFO
# :[snake_vault/flask_utils/__init__.py]
# /author        : fantomH
# /created       : 2024-06-03 11:11:09 UTC
# /updated       : 2024-06-03 11:11:09 UTC
# /description   : Flask utils

from flask import current_app

# :-----/ (function) get_app_context() /-----:
def get_app_context():

    with current_app.app_context():
        print("Attributes accessible within app_context:")
        for attr_name in dir(current_app):
            if not attr_name.startswith('_'):
                attr_value = getattr(current_app, attr_name)
                print(f"{attr_name}: {attr_value}")
