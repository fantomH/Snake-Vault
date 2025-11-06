<!-- INFO {{{

# [/home/ghost/main/Snake-Vault/snake_vault/snake_sqlite/README.md]
# author        : Pascal Malouin @https://github.com/fantomH
# created       : 2025-09-21 15:08:02 UTC
# updated       : 2025-11-06 11:14:47 UTC
# description   : Snake-SQLite README.

}}} -->

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

### Export to CSV:

```
snake-sqlite --db <db_name> --table <table_name> --export-as-csv -
```

Displays the full table in stdout as csv.

```
snake-sqlite --db <db_name> --table <table_name> --export-as-csv /path/to/filename.csv
```

Exports all data of the table to a csv file.

### Import XML data:

`snake-sqlite --db <db_name> --table <table_name> --import-xml <xml_file>`

_see_ `python -m pydoc snake_vault.snake_sqlite.xml2sqlite.import_xml` for optional options.

### SQLite user-defined functions

SQLite does not provide some functionality natively, but has the ability to plug-in user-defined functions.

#### REGEXEP

The string pattern-matching operators such as LIKE and GLOB provided by default 
can be limited in their ability to do complex search.

The function regexp() takes a regular expression pattern and a column.

It will search (case-insensitive) the pattern and return True if found.

While using the option --from-sql-file with the Snake-SQLite CLI app, you can 
use the function REGEXP to parse through a string, since the function is loaded 
by default.

```sql
SELECT id, name, email
FROM users
WHERE email REGEXP '(?i)@(gmail|hotmail|yahoo)\.com$';
```

This would output the following.

```text
3 | Alice Dupont   | alice.dupont@gmail.com
5 | Marc Tremblay  | marc.tremblay@hotmail.com
9 | Sophie Roy     | s.roy@yahoo.com
```

<!--
# vim: foldmethod=marker
-->
