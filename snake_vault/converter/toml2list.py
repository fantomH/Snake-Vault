# +-------------------------------------------------------------------- INFO -+
# | [Snake-Vault/snake_vault/converter/toml2list.py]                          |
# |                                                                           |
# | Author      : Pascal Malouin (https://github.com/fantomH)                 |
# | Created     : 2026-07-02 18:02:21 UTC                                     |
# | Updated     : 2026-07-02 18:02:21 UTC                                     |
# | Description : Get list from TOML.                                         |
# +---------------------------------------------------------------------------+

from __future__ import annotations

import io
import tomllib
from pathlib import Path
from typing import BinaryIO


def toml_to_list(
    source: str | Path | BinaryIO,
    table_name: str,
    *,
    sort_by: str | None = None,
) -> list[dict]:
    """Return a list from a TOML section.

    Parameters
    ----------
    source:
        Either:
            - a path to a TOML file,
            - an opened binary file object,
            - or a TOML string.

    table_name:
        Name of the TOML table array to return.

    Returns
    -------
    list[dict]
        The requested TOML section, or an empty list if it does not exist.

    Examples
    --------
    >>> toml_to_list("bookmarks.toml", "bookmark", sort_by="name")

    >>> with open("bookmarks.toml", "rb") as f:
    ...     toml_to_list(f, "bookmark")

    >>> toml_to_list(toml_text, "bookmark")
    """

    if isinstance(source, Path):
        with source.open("rb") as f:
            data = tomllib.load(f)

    elif isinstance(source, str):
        path = Path(source)

        if path.exists():
            with path.open("rb") as f:
                data = tomllib.load(f)
        else:
            data = tomllib.loads(source)

    else:
        data = tomllib.load(source)

    value = data.get(table_name, [])

    if not isinstance(value, list):
        raise TypeError(
            f"TOML section '{table_name}' must be a list, got {type(value).__name__}."
        )

    if sort_by is not None:
        value.sort(key=lambda v: v.get(sort_by, ""))

    return value
