# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_sqlite/udf.py]
# author        : Pascal Malouin @https://github.com/fantomH
# created       : 2025-11-05 20:50:45 UTC
# updated       : 2025-11-05 20:50:45 UTC
# description   : User-defined SQLite functions

"""
User-defined SQLite functions.
"""

import re
import sqlite3
from typing import Optional

def regexp(pattern: str, text: Optional[str]) -> int:
    """
    SQLite does not have regular expression ability by default.

    To register the function in your Python script, add:
        conn.create_function("REGEXP", 2, regexp)

    Example of SQL script:

    ```sql
    SELECT *
    FROM
        users
    WHERE
        last_name REGEX 'miller[- ]?';
    ```
    
    """

    if text is None:
        return 0
    return 1 if re.search(pattern, text, re.IGNORECASE) else 0
