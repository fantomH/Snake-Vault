# :: --------------------------------------------------------------------- INFO
# :: [snake_vault/snake_sqlite/core.py]
# :: author        : fantomH / Pascal Malouin
# :: created       : 2025-09-12 16:55:53 UTC
# :: updated       : 2025-09-22 20:36:57 UTC
# :: description   : SQLite helper.

"""
Core functions.
"""

import sqlite3
from typing import Any

from .udf import regexp

def get_headers(db_path: str, table: str) -> list[str]:
    """
    Retrieve the column names (headers) of a table in a SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.
        table (str): Name of the table.

    Returns:
        list[str]: A list of column names in the given table.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(f"PRAGMA table_info({table})")
        headers = [row[1] for row in cursor.fetchall()]
    return headers

def list_tables(db_path: str) -> list[str]:
    """
    List all table names in a SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        list[str]: A list of table names in the database.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        tables = [row[0] for row in cursor.fetchall()]
    return tables

def print_info(db_path: str) -> None:
    """
    Print detailed information about all tables in a SQLite database.

    For each table, prints its name and a tree-like list of columns
    with type, default value, and constraints.

    Args:
        db_path (str): Path to the SQLite database file.
    """

    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        tables = [row[0] for row in cursor.fetchall()]

        if not tables:
            print("(no tables)")
            return

        for table in tables:
            print(f"📂 {table}")
            info = conn.execute(f"PRAGMA table_info({table})").fetchall()
            # :: Each row: (cid, name, type, notnull, dflt_value, pk)
            for cid, name, coltype, notnull, dflt, pk in info:
                flags = []
                if pk:
                    flags.append("PK")
                if notnull:
                    flags.append("NOT NULL")
                colinfo = f"{coltype}" if coltype else "UNKNOWN"
                if dflt is not None:
                    colinfo += f" DEFAULT {dflt}"
                if flags:
                    colinfo += " [" + ", ".join(flags) + "]"
                print(f"   └── {name} ({colinfo})")
            print()

def run_sql_file(db_path: str, sql_file: str) -> tuple[list[str], list[tuple[Any, ...]], str]:
    """
    Execute a SQL query read from a file against a SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.
        sql_file (str): Path to the SQL file containing the query.

    Returns:
        tuple[list[str], list[tuple[Any, ...]], str]:
            - headers: List of column names (empty if the query returns no columns).
            - rows: List of result rows as tuples.
            - query: The SQL text that was executed.
    """

    with open(sql_file, "r", encoding="utf-8") as f:
        query = f.read()

    with sqlite3.connect(db_path) as conn:
        conn.create_function("REGEXP", 2, regexp)
        cursor = conn.execute(query)
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description] if cursor.description else []

    return headers, rows, query

def print_table(headers: list[str], rows: list[tuple[Any, ...]], pretty: bool = True) -> None:
    """
    Print a table given headers and rows.

    Args:
        headers (list[str]): Column headers.
        rows (list[tuple[Any, ...]]): Table rows as tuples of values.
        pretty (bool, optional): If True, adjust column widths for alignment.
                                 If False, print values separated by '|'.
                                 Defaults to True.

    Notes:
        - NULL values are printed as the literal string "NULL".
        - When pretty=False, columns are not padded.
    """

    if not headers:
        print("(no headers)")
        return

    if not pretty:
        # :: Simple print, no alignment
        print(" | ".join(headers))
        print("-+-".join("-" * len(h) for h in headers))
        for row in rows:
            print(" | ".join(str(val) if val is not None else "NULL" for val in row))
        return

    # :: Pretty mode with aligned columns
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            text = str(val) if val is not None else "NULL"
            col_widths[i] = max(col_widths[i], len(text))

    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("-+-".join("-" * w for w in col_widths))

    for row in rows:
        print(" | ".join(
            (str(val) if val is not None else "NULL").ljust(col_widths[i])
            for i, val in enumerate(row)
        ))
