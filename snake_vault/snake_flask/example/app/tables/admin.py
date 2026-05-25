# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/tables/admin.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-24 16:34:45 UTC
# updated       : 2026-05-24 16:34:45 UTC
# description   : Tables definition.

from flask import current_app

from ..db import get_db
from ..plugins.table_generator import TableGenerator

ADMIN_USERS_TABLE = [
    {"name": "selected", "label": "", "type": "select", "db": False},
    {"name": "username", "label": "Username", "sortable": True, "searchable": True},
    {"name": "email", "label": "Email", "sortable": True, "searchable": True},
    {"name": "is_active", "label": "Active", "type": "checkbox", "sortable": True},
    {"name": "good_boy", "label": "Good/Bad", "type": "checkbox", "sortable": True, "db": False},
]

def get_users_table():
    return TableGenerator(
        table_id="users-table",
        data_url="/admin/users/data/",
        db = get_db(current_app.config["DATABASE"]),
        columns=ADMIN_USERS_TABLE,
        source_table="users",
        default_order_by="username ASC",
    )
