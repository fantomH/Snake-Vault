# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/__init__.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 11:30:00 UTC
# updated       : 2026-05-19 15:12:52 UTC
# description   : Flask Example.

import os
from datetime import (
    timedelta
)

from flask import (
    Flask,
    render_template,
)

from .db import (
    close_db,
    init_db,
    migrate_command,
)
from .linguae import get_display_language
from .login_manager import (
    init_app,
    login_required,
)


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    # [+] ------------------------------| config

    # --| Default config.
    app.config.from_mapping(
        DATABASE=app.instance_path + "/data.sqlite",
        # DISPLAY_LANGUAGE="french",
        DISPLAY_LANGUAGE="english",
        SECRET_KEY="secret",
        SESSION_TIMEOUT=60,
    )

    # --| Load instance/config.py if exists.
    app.config.from_pyfile("config.py", silent=True)

    # --| Override config for testing.
    # ..| In /run.py add Test config in create_app():
    # ..|   app = create_app({
    # ..|       "SECRET_KEY": "test-secret"
    # ..|   })
    if test_config is not None:
        app.config.update(test_config)

    # --| Make sure /instance exists.
    os.makedirs(app.instance_path, exist_ok=True)

    app.teardown_appcontext(close_db)

    # [+] ------------------------------| cli

    # Register CLI command.
    app.cli.add_command(init_db)
    app.cli.add_command(migrate_command)

    # [+] ------------------------------| session

    app.permanent_session_lifetime = timedelta(minutes=app.config.get("SESSION_TIMEOUT", 60))

    # [+] ------------------------------| login manager

    login_manager.init_app(app)

    # [+] ------------------------------| routes / blueprint
    @app.route("/", methods=["GET", "POST"])
    @login_required
    def index():

        display_language = get_display_language()

        return render_template(
            'index.html',
            title=display_language["HOME-title"],
            display_language=display_language
        )

    from .routes.auth import auth
    app.register_blueprint(auth, url_prefix="/")

    return app
