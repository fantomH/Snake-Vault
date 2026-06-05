# ┌──────────────────────────────────────────────────────────────────── INFO ─┐
# │ Snake-Vault / flask / example app                                         │
# ├───────────────────────────────────────────────────────────────────────────┤
# │ [Snake-Vault/snake_vault/flask/example/app/__init__.py]                   │
# │ Author      : Pascal Malouin (https://github.com/fantomH)                 │
# │ Created     : 2026-05-19 11:30:00 UTC                                     │
# │ Updated     : 2026-06-05 15:07:56 UTC                                     │
# │ Description : Flask example.                                              │
# └───────────────────────────────────────────────────────────────────────────┘
# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/example/app/__init__.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 11:30:00 UTC
# updated       : 2026-06-04 18:10:12 UTC
# description   : Flask Example.

import os
from datetime import timedelta

from flask import Flask
from flask import g
from flask import render_template

from snake_vault.flask.linguae import SnakeLinguae
from snake_vault.flask.quiz import SnakeQuiz
from snake_vault.flask.snake_tables import SnakeTables
from snake_vault.flask.utils import get_client_ip
from snake_vault.snake_utils.logger import SnakeLogger

from .db import close_db
from .db import init_db
from .db import migrate_command
from .login_manager import init_app
from .login_manager import login_required
from .utils import get_language_dictionary

linguae = SnakeLinguae()
quiz = SnakeQuiz()
tables = SnakeTables()
log = SnakeLogger(profile="development")

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    # [+] ---------------| config
    # [+] ───────────────┤ config

    # Default configuration.
    app.config.from_mapping(
        DATABASE=app.instance_path + "/data.sqlite",
        DEFAULT_LANGUAGE="french",
        SECRET_KEY="secret",
        SESSION_TIMEOUT=60,
    )

    # Load instance/config.py if exists.
    app.config.from_pyfile("config.py", silent=True)

    # Override config for testing.
    # In /run.py add Test config in create_app():
    #   app = create_app({
    #       "SECRET_KEY": "test-secret"
    #   })
    if test_config is not None:
        app.config.update(test_config)

    # Make sure /instance exists.
    os.makedirs(app.instance_path, exist_ok=True)

    app.teardown_appcontext(close_db)

    # [+] ---------------| cli

    # Register CLI command.
    app.cli.add_command(init_db)
    app.cli.add_command(migrate_command)

    # [+] ---------------| session

    app.permanent_session_lifetime = timedelta(minutes=app.config.get("SESSION_TIMEOUT", 60))

    # [+] ---------------| SnakeLinguae

    linguae.init_app(app)
    linguae.register_package("snake_vault.flask.example.app.linguae")
    linguae.register_package("snake_vault.flask.quiz.linguae")
    linguae.register_package("snake_vault.flask.snake_tables.linguae")

    # [+] ---------------| login manager

    login_manager.init_app(app)

    # [+] ---------------| SnakeTables

    tables.init_app(app)

    # [+] ---------------| SnakeQuiz

    quiz.init_app(app)

    # [+] ---------------| routes / blueprint
    @app.route("/", methods=["GET", "POST"])
    @login_required
    def index():

        display_language = get_language_dictionary()

        log.info(str(getattr(g, "current_user", None).username) + " from " + get_client_ip(), category="ACCESS")

        return render_template(
            'index.html',
            title=display_language.get("HOME-title", "Welcome"),
            display_language=display_language
        )

    from .routes.auth import auth
    app.register_blueprint(auth, url_prefix="/")

    from .routes.admin import admin
    app.register_blueprint(admin, url_prefix="/")

    return app
