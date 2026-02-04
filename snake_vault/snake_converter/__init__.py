# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_converter/__init__.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-10-20 16:02:26 UTC
# updated       : 2026-02-04 20:53:16 UTC
# description   : Init for snake_converter.

"""
File converter.
"""

from .csv2json import ( csv_to_json )
from .xml2sqlite import ( xml_to_sqlite )

__all__ = [
    "csv_to_json",
    "xml_to_sqlite"
    ]
