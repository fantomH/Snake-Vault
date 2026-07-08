# +-------------------------------------------------------------------- INFO -+
# | [Snake-Vault/snake_vault/timekeeper.py]                                   |
# |                                                                           |
# | Author      : Pascal Malouin (https://github.com/fantomH)                 |
# | Created     : 2024-05-30 11:10:24 UTC                                     |
# | Updated     : 2026-06-19 13:55:50 UTC                                     |
# | Description : Time utilities.                                             |
# +---------------------------------------------------------------------------+

"""
Time utilities.
"""

import datetime

__all__ = ["time_as_id"]

def time_as_id() -> str:
    """
    time_as_id() returns a string representing the time now that can be used as
    an ID or a timestamp.

    example: 20240530111024
    """

    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
