# ┌──────────────────────────────────────────────────────────────────── INFO ─┐
# │ Snake-Vault / flask / exemple / validator                                 │
# ├───────────────────────────────────────────────────────────────────────────┤
# │ [Snake-Vault/snake_vault/flask/example/app/validator.py]                  │
# │ Author      : Pascal Malouin (https://github.com/fantomH)                 │
# │ Created     : 2026-05-21 19:40:24 UTC                                     │
# │ Updated     : 2026-06-11 18:42:34 UTC                                     │
# │ Description : Data validator                                              │
# └───────────────────────────────────────────────────────────────────────────┘

import re

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False

    checks = [
        r"[a-z]",        # lowercase
        r"[A-Z]",        # uppercase
        r"\d",           # number
        r"[^A-Za-z0-9]", # special character
    ]

    return all(re.search(pattern, password) for pattern in checks)
