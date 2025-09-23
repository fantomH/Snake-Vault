# :: --------------------------------------------------------------------- INFO
# :: [snake_vault/snake_sqlite/__init__.py]
# :: author        : fantomH / Pascal Malouin
# :: created       : 2025-09-12 16:59:37 UTC
# :: updated       : 2025-09-23 17:05:44 UTC
# :: description   : Init

"""
SQLite helper.
"""

from .core import ( get_headers,
                    list_tables,
                    print_info,
                    print_table,
                    run_sql_file )

from .export import ( export_as_csv,
                      export_query_to_db,
                      export_table_to_db )

from .xml2sqlite import ( import_xml )

__all__ = [ "export_as_csv",
            "export_query_to_db",
            "export_table_to_db",
            "get_headers",
            "import_xml",
            "list_tables",
            "print_info",
            "print_table",
            "run_sql_file" ]
