<!--
# :: --------------------------------------------------------------------- INFO
# :: [../snake_sqlite/README.md]
# :: author        : Pascal Malouin @ github.com/fantomH
# :: created       : 2025-09-21 15:08:02 UTC
# :: updated       : 2025-09-21 15:08:02 UTC
# :: description   : Snake-SQLite README
-->

# Snake-SQLite

SQLite 3 Helper

Provides the command `snake-sqlite`, which is the equivalent of `python -m snake_vault.snake_sqlite`.

## Command `snake-sqlite`

### SQLite db information:

`snake-sqlite --db <db_name> --info`

### SQLite db tables:

`snake-sqlite --db <db_name> --tables`

### SQLite table's headers:

`snake-sqlite --db <db_name> --table <table_name> --headers`

### Import XML data:

`snake-sqlite --db <db_name> --table <table_name> --import-xml <xml_file>`

see `python -m pydoc snake_vault.snake_sqlite.xml2sqlite.import_xml` for optional options.
