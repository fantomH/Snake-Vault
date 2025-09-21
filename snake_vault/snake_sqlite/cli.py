# :: --------------------------------------------------------------------- INFO
# :: [snake_vault/snake_sqlite/cli.py]
# :: author        : fantomH / Pascal Malouin
# :: created       : 2025-09-12 16:59:37 UTC
# :: updated       : 2025-09-12 16:59:37 UTC
# :: description   : CLI

import argparse
import sqlite3
from . import ( export_as_csv,
                export_query_to_db,
                export_table_to_db,
                get_headers,
                list_tables, 
                print_info,
                print_table,
                run_sql_file )

def main():
    parser = argparse.ArgumentParser(description="Snake SQLite utilities")
    parser.add_argument("--db", required=True, help="Path to sqlite database")
    parser.add_argument("--tables", action="store_true", help="List tables in the DB")
    parser.add_argument("--table", metavar="TABLE", help="Operate on this table")
    parser.add_argument("--info", action="store_true", help="Print database schema (tables and columns)")
    parser.add_argument("--headers", action="store_true", help="Show table headers")
    parser.add_argument("--from-sql-file", metavar="SQLFILE", help="Run SQL from a file and print results")

    # :: Exports
    parser.add_argument(
        "--export-as-csv",
        nargs="?",
        const=True,           # if not value given
        metavar="OUT",
        help="Export result (from --table or --from-sql-file) as CSV. "
             "Optionally provide OUT as a file path, a directory, or '-' for stdout."
    )
    parser.add_argument(
        "--export-to-db",
        metavar="OUT_DB",
        help="Export result to another SQLite DB (creates DB if missing; drops/replaces table)."
    )
    parser.add_argument(
        "--out-table",
        metavar="NAME",
        help="Override destination table name for --export-to-db. "
             "Default: source table name, or SQL filename stem."
    )


    args = parser.parse_args()

    # :: Tree-like view
    if args.info:
        print_info(args.db)
        return

    # :: Display tables name to stdout.
    if args.tables:
        _tables = list_tables(args.db)
        for table in _tables:
            print(table)

    # :: --db <db_name> --table <table_name>
    if args.table:
        if args.headers:
            _headers = get_headers(args.db, args.table)
            for header in _headers:
                print(header)

        # :: --table <table_name> --export-as-csv <optional_output_path>
        if args.export_as_csv is not None and not args.from_sql_file:

            # :: Fetch all rows + headers for the table.
            conn = sqlite3.connect(args.db)
            cur = conn.execute(f"SELECT * FROM {args.table}")
            rows = cur.fetchall()
            headers = [d[0] for d in cur.description] if cur.description else []
            conn.close()

            dest = None if args.export_as_csv is True else args.export_as_csv
            out = export_as_csv(headers, rows, dest, default_name=args.table)
            print(f"Exported {args.table} → {out}")

        # :: --export-to-db
        if args.export_to_db:
            out_table = args.out_table or args.table
            export_table_to_db(args.db, args.table, args.export_to_db, out_table)
            print(f"Exported table {args.table} → {args.export_to_db}:{out_table} (replaced if existed)")

    # :: --from_sql_file
    if args.from_sql_file:
        headers, rows, query = run_sql_file(args.db, args.from_sql_file)

        # :: --export-to-db.
        if args.export_to_db:
            if args.out_table is not None:
                export_query_to_db(args.db, query, args.export_to_db, args.out_table)
                print(f"Exported query result → {args.export_to_db}:{args.out_table} (replaced if existed)")
            else:
                parser.error("--out-table is required when using --from-sql-file with --export-to-db")
        # :: --export-as-csv
        elif args.export_as_csv is not None:
            dest = None if args.export_as_csv is True else args.export_as_csv
            out = export_as_csv(headers, rows, dest, default_name="query_result")
            print(f"Exported query result → {out}")
        else:
            # :: Default print a the results as a table to the stdout.
            print_table(headers, rows)
