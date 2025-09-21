# :: --------------------------------------------------------------------- INFO
# :: [snake_vault/snake_sqlite/core.py]
# :: author        : fantomH / Pascal Malouin
# :: created       : 2025-09-12 16:55:53 UTC
# :: updated       : 2025-09-12 16:55:53 UTC
# :: description   : SQLite helper.

import sqlite3

def get_headers(db_path: str, table: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(f"PRAGMA table_info({table})")
    headers = [row[1] for row in cursor.fetchall()]
    conn.close()
    return headers

def list_tables(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables

def print_info(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    tables = [row[0] for row in cursor.fetchall()]

    if not tables:
        print("(no tables)")
        conn.close()
        return

    for table in tables:
        print(f"📂 {table}")
        info = conn.execute(f"PRAGMA table_info({table})").fetchall()
        # Each row: (cid, name, type, notnull, dflt_value, pk)
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
    conn.close()

def run_sql_file(db_path: str, sql_file: str):
    with open(sql_file, "r", encoding="utf-8") as f:
        query = f.read()

    conn = sqlite3.connect(db_path)
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description] if cursor.description else []
    conn.close()

    return headers, rows, query

def print_table(headers, rows):
    if not headers:
        return

    # :: Compute column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)) if val is not None else 4)

    # :: Header
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("-+-".join("-" * w for w in col_widths))

    # :: Rows
    for row in rows:
        print(" | ".join(
            (str(val) if val is not None else "NULL").ljust(col_widths[i])
            for i, val in enumerate(row)
        ))
