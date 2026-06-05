# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/linguae/__init__.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-03 17:48:07 UTC
# updated       : 2026-06-03 17:48:07 UTC
# description   : SnakeLinguae extension.

from importlib import import_module

from flask import current_app
from flask import g

class SnakeLinguae:
    def __init__(self, app=None):
        self.language_packages = []

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("DEFAULT_LANGUAGE", "english")
        app.config.setdefault("LINGUAE_PACKAGES", [])

        app.extensions["snake_linguae"] = self

        @app.before_request
        def load_display_language():
            g.display_language = self.get_display_language()

        app.jinja_env.globals["get_display_language"] = get_display_language
        app.jinja_env.globals["get_language_dictionary"] = get_language_dictionary

    def register_package(self, package_path):
        """
        Example:
        linguae.register_package("snake_vault.flask.quiz.linguae")
        """
        if package_path not in self.language_packages:
            self.language_packages.append(package_path)

    def get_display_language(self):
        user = getattr(g, "current_user", None)

        if user and getattr(user, "language", None):
            return user.language

        configured_language = current_app.config.get("DEFAULT_LANGUAGE")

        if configured_language:
            return configured_language

        return "english"

    def get_language_dictionary(self, language=None, prefix=None):
        language = language or self.get_display_language()

        merged = {}

        packages = [
            *current_app.config.get("LINGUAE_PACKAGES", []),
            *self.language_packages,
        ]

        for package_path in packages:
            module_path = f"{package_path}.{language}"

            try:
                module = import_module(module_path)
            except ModuleNotFoundError:
                continue

            for name in dir(module):
                if name.startswith("_"):
                    continue

                value = getattr(module, name)

                if not isinstance(value, dict):
                    continue

                if prefix and not name.startswith(prefix):
                    continue

                merged.update(value)

        return merged


def get_display_language():
    extension = current_app.extensions["snake_linguae"]
    return extension.get_display_language()


def get_language_dictionary(language=None, prefix=None):
    extension = current_app.extensions["snake_linguae"]
    return extension.get_language_dictionary(language, prefix)
