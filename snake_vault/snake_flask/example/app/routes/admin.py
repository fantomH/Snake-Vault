# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/routes/admin.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 16:01:48 UTC
# updated       : 2026-05-19 16:01:48 UTC
# description   : Admin routes.

from flask import (
    Blueprint,
    current_app,
    jsonify,
    render_template,
    request,
)

from ..linguae import ( get_display_language )
from ..login_manager import ( login_required )
from ..model_user import ( User )
from ..plugins.snake_flask_table import TableGenerator
from ..tables.admin import get_users_table

admin = Blueprint("admin", __name__)

# [+] ------------------------------| /admin/users
@admin.route("/admin/users/", methods=["GET", "POST"])
@login_required
def users():

    display_language = get_display_language()
    table_generator = get_users_table()

    if request.method == "POST":
        print(request)

    return render_template(
        "admin/users.html",
        table_generator=table_generator,
        display_language=display_language,
    )


# [+] ------------------------------| /admin/users/data/
@admin.route("/admin/users/data/")
@login_required
def users_data():

    table_generator = get_users_table()

    return jsonify(
        table_generator.get_data()
    )

# [+] ---------------| /admin/users/update/
@admin.route("/admin/users/update/", methods=["POST"])
@login_required
def users_update():


    data = request.get_json()

    User.update_user(
        data.get("id"),
        **{
            data.get("column"): data.get("value")
        }
    )

    return jsonify({
        "ok": True,
    })

# [+] ------------------------------| /admin/users/<username>/
@admin.route("/admin/users/account/<username>/")
def user_account(username):

    user_account = User.fetch_by_username(username)
    return f"Editing user: {user_account}"
