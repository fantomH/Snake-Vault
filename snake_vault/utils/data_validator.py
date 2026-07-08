# +-------------------------------------------------------------------- INFO -+
# | [Snake-Vault/snake_vault/utils/data_validator.py]                         |
# |                                                                           |
# | Author      : Pascal Malouin (https://github.com/fantomH)                 |
# | Created     : 2026-06-16 16:31:50 UTC                                     |
# | Updated     : 2026-06-16 16:31:50 UTC                                     |
# | Description : Generic data validator.                                     |
# +---------------------------------------------------------------------------+

"""
Data Validator
--------------

Ulity data validator.
"""

import re

__all__ = ["is_valid_password"]

def is_valid_password(password: str) -> bool:
    """
    Validates passwords.

    Takes a str and return a bool.
    """

    if len(password) < 8:
        return False

    checks = [
        r"[a-z]",        # lowercase
        r"[A-Z]",        # uppercase
        r"\d",           # number
        r"[^A-Za-z0-9]", # special character
    ]

    return all(re.search(pattern, password) for pattern in checks)
