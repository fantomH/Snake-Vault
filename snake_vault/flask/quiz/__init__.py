# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/quiz/__init__.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-02 18:51:23 UTC
# updated       : 2026-06-03 12:04:37 UTC
# description   : SnakeQuiz extension.

from pathlib import Path
from markdown import markdown

from .routes import quiz_bp

class SnakeQuiz:

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        app.config.setdefault(
            "SNAKE_QUIZ_DIR",
            Path(__file__).parent / "quiz",
        )

        app.extensions["snake_quiz"] = self

        @app.template_filter("markdown")
        def markdown_filter(text):
            return markdown(
                text or "",
                extensions=["fenced_code", "tables"],
            )

        app.register_blueprint(quiz_bp)
