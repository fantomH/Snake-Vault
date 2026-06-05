# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/example/app/tables/admin.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-24 16:34:45 UTC
# updated       : 2026-05-24 16:34:45 UTC
# description   : Tables definition.

from flask import current_app

from snake_vault.flask.snake_tables.table import Table
from snake_vault.flask.snake_tables.utils import get_language_dictionary

from ..db import get_db

# [+] ---------------| column lang definition

columns_lang_display = {
    "english": {
        "column-edit-text": "Modify",
        "column-username-label": "Username",
        "column-is_active-label": "Active",
    },
    "french": {
        "column-edit-text": "Modifier",
        "column-username-label": "Utilisateurs",
        "column-is_active-label": "Actif",
    }
}

def get_users_table():

    display_language = get_language_dictionary(custom=columns_lang_display)

    # [+] ---------------| column definition
    ADMIN_USERS_TABLE = [
        {
            "name": "username",
            "label": display_language.get("column-username-label", "Username"),
            "sortable": True,
            "searchable": True
        },
        {
            "name": "email",
            "label": "Email",
            "sortable": True,
            "searchable": True
        },
        {
            "name": "is_active",
            "label": display_language.get("column-is_active-label", "Active"),
            "type": "checkbox",
            "sortable": True
        },
        {
            "name": "edit",
            "label": "",
            "type": "link-button",
            "text": display_language.get("column-edit-text", "Modify"),
            "url": "/admin/users/account/{username}/",
            "db": False,
        },
    ]

    return Table(
        table_id="users-table",
        data_url="/admin/users/data/",
        data_update_url="/admin/users/update/",
        db = get_db(current_app.config["DATABASE"]),
        columns=ADMIN_USERS_TABLE,
        source_table="users",
        default_order_by="username ASC",
    )
