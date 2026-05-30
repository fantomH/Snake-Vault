from markdown import markdown


def init_app(app):
    from .routes import snake_flask_quiz

    @app.template_filter("markdown")
    def markdown_filter(text):
        return markdown(
            text or "",
            extensions=["fenced_code", "tables"],
        )

    app.register_blueprint(snake_flask_quiz)
