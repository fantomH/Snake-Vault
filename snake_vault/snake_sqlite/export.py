# :: --------------------------------------------------------------------- INFO
# :: [snake_vault/snake_sqlite/export.py]
# :: author        : Pascal Malouin @ github.com/fantomH
# :: created       : 2025-09-12 16:59:37 UTC
# :: updated       : 2025-09-21 15:13:50 UTC
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
    filename: str = "query_results"
    ) -> str:
    """
    Write CSV to file (dest_path) or stdout ('-').

    If dest_path is a directory or None, build a filename using default_name.

    Args:
        headers (Sequence[str]): Column headers.
        rows (Sequence[Sequence[Union[str, int, float]]]): Table rows.
        dest_path (str | None): Output path, directory, None, or '-' for stdout.
        filename (str, optional): Fallback filename if dest_path is None or a directory.
                                  Defaults to "query_results".

    Returns:
        str: The output filename, or '-' if written to stdout.
    """

    if dest_path == "-":
        writer = csv.writer(sys.stdout, lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)
        return "-"
    # :: Pick filename.
    if not dest_path:
        out = f"{default_name}.csv"
    elif os.path.isdir(dest_path):
        out = os.path.join(dest_path, f"{default_name}.csv")
    else:
        out = dest_path
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    return out

def export_table_to_db(src_db: str, src_table: str, out_db: str, out_table: str | None = None):
    out_table = out_table or src_table
    conn = sqlite3.connect(src_db)
    try:
        conn.execute(f"ATTACH DATABASE ? AS outdb", (out_db,))
        conn.execute(f"DROP TABLE IF EXISTS outdb.{out_table}")
        # Create by selecting to preserve data without manual schema mapping
        conn.execute(f"CREATE TABLE outdb.{out_table} AS SELECT * FROM main.{src_table}")
        conn.commit()
        conn.execute("DETACH DATABASE outdb")
    finally:
        conn.close()
    return out_table

def export_query_to_db(src_db: str, query: str, out_db: str, out_table: str):
    conn = sqlite3.connect(src_db)
    try:
        conn.execute(f"ATTACH DATABASE ? AS outdb", (out_db,))
        conn.execute(f"DROP TABLE IF EXISTS outdb.{out_table}")
        # CREATE TABLE AS SELECT <query>
        conn.execute(f"CREATE TABLE outdb.{out_table} AS {query}")
        conn.commit()
        conn.execute("DETACH DATABASE outdb")
    finally:
        conn.close()
