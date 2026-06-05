# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/snake_tables/__init__.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-04 12:30:25 UTC
# updated       : 2026-06-04 12:30:25 UTC
# description   : SnakeTables extension.

from flask import Blueprint

from .table import Table

class SnakeTables:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        blueprint = Blueprint(
            "snake_tables",
            __name__,
            static_folder="static",
            static_url_path="/snake-tables/static",
            template_folder="templates",
        )

        app.register_blueprint(blueprint)
        app.extensions["snake_tables"] = self


__all__ = [
    "SnakeTables",
    "Table",
]
