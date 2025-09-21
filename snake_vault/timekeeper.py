# :: --------------------------------------------------------------------- INFO
# :: [Snake-Vault/snake_vault/timekeeper.py]
# :: author        : Pascal Malouin / fantomH (pascal.malouin@gmail.com)
# :: created       : 2024-05-30 11:10:24 UTC
# :: updated       : 2025-09-21 14:44:37 UTC
# :: description   : Time utilities.

"""
Time utilities.
"""

import datetime

def time_as_id() -> str:
    """
    time_as_id() returns a string representing the time now that can be used as
    an ID or a timestamp.

    example: 20240530111024
    """

    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
