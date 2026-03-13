<!-- INFO {{{

# [Snake-Vault/README.md]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-09-21 15:08:02 UTC
# updated       : 2026-03-13 13:56:02 UTC
# description   : Snake-Vault README

}}} -->

<img src="logo.png" width="200">

# Snake-Vault

Miscellanous Python utilities.

## snake_vault.files

`file_info(f, filename=True, path=True, size=True, mime=True, md5=True)`

Gives information on a file.

`directory_files_info(dirpath)`

Gives information for all files in a directory.

### snake_vault.messages

`message(category, msg)`

```
Formated terminal messages.

Arguments:
    category: (str) Type of message available.
            - action:
            [*] Setting preset for random number.
            - result:
            [-] 33Gb found.
            - question:
            [?] What would you like?
            - alert:
            [!] You might want to install optional dependancies.
            - warning/error:
            [!] Unable to fetch file.
            - title:
            HOSTNAME          IP                PATH
            `title` will not align columns. You will have to do it manually.
```

## snake_vault.snake_converter (sub-package)

Multi-format data converter.

Provides the command `snake-converter`, which is the equivalent of `python -m snake_vault.snake_converter`.

### snake_vault.snake_converter.csv2json

* csv_to_json(*input_file, output_file*) -> Convert CSV file to JSON.

### snake_vault.snake_converter.xml2sqlite

* xml_to_sqlite(*xml_path, db_path, table, element_local, batch_size, drop_existing*) -> Stream-parse an XML file and insert rows into a SQLite table in batches.

See https://github.com/fantomH/Snake-Vault/blob/main/snake_vault/snake_converter/README.md for further information.

## snake_vault.snake_enigma (sub-package)

Hash, cipher, encryption helper.

Provides the command `snake-enigma`, which is the the equivalent of `python -m snake_vault.snake_enigma`.

### snake_vault.snake_enigma.md5

md5 manipulation.

* file_md5sum(*filepath*) -> Calculates the md5sum of a file.

See https://github.com/fantomH/Snake-Vault/blob/main/snake_vault/snake_enigma/README.md for further information.

## snake_vault.snake_sqlite (sub-package)

SQLite helper.

Provides the command `snake-sqlite`, which is the equivalent of `python -m snake_vault.snake_sqlite`.

See https://github.com/fantomH/Snake-Vault/blob/main/snake_vault/snake_sqlite/README.md for further information.

## snake_vault.timekeeper

`time_as_id()`

Returns a string representing the time now that can be used as an ID or a timestamp.

## snake_vault.snake_utils (sub-package)

Snake Utils.

Provides the command `snake-utils`, which is the equivalent of `python -m snake_vault.snake_utils`.

See https://github.com/fantomH/Snake-Vault/blob/main/snake_vault/snake_utils/README.md for further information.

<!--
# vim: foldmethod=marker
-->
