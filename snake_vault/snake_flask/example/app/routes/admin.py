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

from ..db import get_db
from ..plugins.table_generator import TableGenerator
from ..tables.admin import get_users_table

admin = Blueprint("admin", __name__)

# [+] ------------------------------| /admin/users
@admin.route("/admin/users/")
def users():

    table_generator = get_users_table()

    return render_template(
        "admin/users.html",
        table_generator=table_generator,
    )


# [+] ------------------------------| /admin/users/data/
@admin.route("/admin/users/data/")
def users_data():

    table_generator = get_users_table()

    return jsonify(
        table_generator.get_data()
    )
