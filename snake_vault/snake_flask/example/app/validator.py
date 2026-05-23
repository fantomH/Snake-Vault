# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/example/app/validator.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-21 19:40:24 UTC
# updated       : 2026-05-21 19:40:24 UTC
# description   : Data validator.

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
