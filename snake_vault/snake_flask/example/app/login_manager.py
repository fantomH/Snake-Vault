# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/login_manager.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-20 19:48:23 UTC
# updated       : 2026-05-20 19:48:23 UTC
# description   : Login_manager

from functools import wraps

from flask import (
    g,
    redirect,
    request,
    session,
    url_for,
)

from .model_user import User


def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.current_user = None
        return

    g.current_user = User.fetch_by_id(user_id)


def init_app(app):
    app.before_request(load_logged_in_user)

    @app.context_processor
    def inject_current_user():
        return {
            "current_user": getattr(g, "current_user", None)
        }

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.current_user is None:
            return redirect(url_for("auth.login", next=request.path))

        return view(**kwargs)

    return wrapped_view
