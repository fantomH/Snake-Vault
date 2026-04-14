# ------------------------------------------------------------------------ INFO
# [/Snake-Vault/snake_vault/snake_converter/csv2sqlite.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-04-13 20:50:49 UTC
# updated       : 2026-04-14 11:49:10 UTC
# description   : Convert CSV to SQLite.

import csv
import sqlite3
import re
from pathlib import Path
from typing import Iterable, Optional

def _sanitize_identifier(name: str) -> str:
    """
    Make a safe SQLite identifier from a CSV header:
    - strips whitespace
    - replaces non [a-zA-Z0-9_] with _
    - prefixes with c_ if it starts with a digit or becomes empty
    """
    n = (name or "").strip()
    n = re.sub(r"\s+", "_", n)
    n = re.sub(r"[^0-9a-zA-Z_]", "_", n)
    if not n or n[0].isdigit():
        n = f"c_{n}"
    return n

def _dedupe(names: Iterable[str]) -> list[str]:
    """Ensure column names are unique: col, col_2, col_3, ..."""
    seen: dict[str, int] = {}
    out: list[str] = []
    for n in names:
        base = n
        if base not in seen:
            seen[base] = 1
            out.append(base)
        else:
            seen[base] += 1
            out.append(f"{base}_{seen[base]}")
    return out

def csv_to_sqlite(
    src_csv: str | Path,
    dst_db: str | Path,
    dst_table: str,
    *,
    delimiter: str = ",",
    encoding: str = "utf-8",
    batch_size: int = 2000,
    drop_existing: bool = False,
) -> None:
    """
    Load a CSV into SQLite.

    - The first row is treated as headers (column names).
    - Columns are created as TEXT to avoid type issues.
    - Inserts are batched for speed.
    """
    src_csv = Path(src_csv)
    dst_db = Path(dst_db)

    if not src_csv.exists():
        raise FileNotFoundError(src_csv)

    with src_csv.open("r", encoding=encoding, newline="") as f, sqlite3.connect(dst_db) as conn:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")

        reader = csv.reader(f, delimiter=delimiter)
        try:
            raw_headers = next(reader)
        except StopIteration:
            raise ValueError("CSV is empty (no header row).")

        headers = _dedupe([_sanitize_identifier(h) for h in raw_headers])
        if not headers:
            raise ValueError("No headers found in first row.")

        # --| Quote identifiers safely (SQLite accepts double quotes).
        qtable = '"' + dst_table.replace('"', '""') + '"'
        qcols = ['"' + c.replace('"', '""') + '"' for c in headers]

        if drop_existing:
            conn.execute(f"DROP TABLE IF EXISTS {qtable}")

        col_defs = ", ".join(f"{c} TEXT" for c in qcols)
        conn.execute(f"CREATE TABLE IF NOT EXISTS {qtable} ({col_defs})")

        placeholders = ", ".join(["?"] * len(headers))
        insert_sql = f"INSERT INTO {qtable} ({', '.join(qcols)}) VALUES ({placeholders})"

        buf: list[list[Optional[str]]] = []
        for row in reader:
            # --| Normalize row length to header count.
            if len(row) < len(headers):
                row = row + [""] * (len(headers) - len(row))
            elif len(row) > len(headers):
                row = row[: len(headers)]

            buf.append(row)

            if len(buf) >= batch_size:
                conn.executemany(insert_sql, buf)
                buf.clear()

        if buf:
            conn.executemany(insert_sql, buf)

        conn.commit()
