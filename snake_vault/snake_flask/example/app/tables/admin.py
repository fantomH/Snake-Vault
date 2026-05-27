# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/tables/admin.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-24 16:34:45 UTC
# updated       : 2026-05-24 16:34:45 UTC
# description   : Tables definition.

from flask import current_app

from ..db import get_db
from ..plugins.snake_flask_table import TableGenerator

# [+] ---------------| column lang definition
english = {
    "column-edit-text": "Modify",
    "column-username-label": "Username",
    "column-is_active-label": "Active",
}

french = {
    "column-edit-text": "Modifier",
    "column-username-label": "Utilisateurs",
    "column-is_active-label": "Actif",
}

languages = {
    "english": english,
    "french": french,
}

def get_users_table():

    lang = TableGenerator.get_display_language(languages)

    # [+] ---------------| column definition
    ADMIN_USERS_TABLE = [
        {
            "name": "username",
            "label": lang["column-username-label"],
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
            "label": lang["column-is_active-label"],
            "type": "checkbox",
            "sortable": True
        },
        {
            "name": "edit",
            "label": "",
            "type": "link-button",
            "text": lang["column-edit-text"],
            "url": "/admin/users/account/{username}/",
            "db": False,
        },
    ]

    return TableGenerator(
        table_id="users-table",
        data_url="/admin/users/data/",
        data_update_url="/admin/users/update/",
        db = get_db(current_app.config["DATABASE"]),
        columns=ADMIN_USERS_TABLE,
        source_table="users",
        default_order_by="username ASC",
    )
