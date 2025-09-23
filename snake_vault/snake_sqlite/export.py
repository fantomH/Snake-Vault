# :: --------------------------------------------------------------------- INFO
# :: [snake_vault/snake_sqlite/export.py]
# :: author        : Pascal Malouin @ github.com/fantomH
# :: created       : 2025-09-12 16:59:37 UTC
# :: updated       : 2025-09-22 20:28:03 UTC
# :: description   : Export SQLite db functions.

"""
Export SQLite db functions.
"""

import csv
import os
import sqlite3
import sys
from typing import Sequence, Union

def export_as_csv(
    headers: Sequence[str],
    rows: Sequence[Sequence[Union[str, int, float]]],
    dest_path: str | None,
    csv_name: str = "query_results"
    ) -> str:
    """
    Write CSV to file (dest_path) or stdout ('-').

    If dest_path is a directory or None, build a filename using csv_name.

    Args:
        headers (Sequence[str]): Column headers.
        rows (Sequence[Sequence[Union[str, int, float]]]): Table rows.
        dest_path (str | None): Output path, directory, None, or '-' for stdout.
        csv_name (str, optional): Fallback filename if dest_path is None or a directory.
                                  Defaults to "query_results".

    Returns:
        str: The output filename, or '-' if written to stdout.
    """

    if dest_path == "-":
        writer = csv.writer(sys.stdout, lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)
        return "-"
    if not dest_path:
        out = f"{csv_name}.csv"
    elif os.path.isdir(dest_path):
        out = os.path.join(dest_path, f"{csv_name}.csv")
    else:
        out = dest_path
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    return out

def export_table_to_db(
    src_db: str,
    src_table: str,
    out_db: str,
    out_table: str | None = None
    ) -> str:
    """
    Export a table from one SQLite database into another.

    Args:
        src_db (str): Path to the source database.
        src_table (str): Name of the table in the source database.
        out_db (str): Path to the destination database.
        out_table (str | None, optional): Name of the table in the destination database.
            If None, defaults to the same name as src_table.

    Returns:
        str: The actual name of the table created in the destination database.
    """

    out_table = out_table or src_table
    conn = sqlite3.connect(src_db)
    try:
        conn.execute(f"ATTACH DATABASE ? AS outdb", (out_db,))
        conn.execute(f"DROP TABLE IF EXISTS outdb.{out_table}")
        conn.execute(f"CREATE TABLE outdb.{out_table} AS SELECT * FROM main.{src_table}")
        conn.commit()
        conn.execute("DETACH DATABASE outdb")
    finally:
        conn.close()
    return out_table

def export_query_to_db(
    src_db: str,
    query: str,
    out_db: str,
    out_table: str
    ) -> str:
    """
    Execute a SQL query on a source database and export the result set
    into a table in a destination database.

    Args:
        src_db (str): Path to the source SQLite database.
        query (str): SQL query whose result set will be exported.
        out_db (str): Path to the destination SQLite database.
        out_table (str): Name of the table to create in the destination database.

    Returns:
        str: The name of the table created in the destination database.
    """

    conn = sqlite3.connect(src_db)
    try:
        conn.execute(f"ATTACH DATABASE ? AS outdb", (out_db,))
        conn.execute(f"DROP TABLE IF EXISTS outdb.{out_table}")
        conn.execute(f"CREATE TABLE outdb.{out_table} AS {query}")
        conn.commit()
        conn.execute("DETACH DATABASE outdb")
    finally:
        conn.close()
    return out_table
