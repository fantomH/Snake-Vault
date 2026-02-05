<!-- INFO {{{

# [Snake-Vault/README.md]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-09-21 15:08:02 UTC
# updated       : 2026-02-05 09:07:43 UTC
# description   : Snake-Vault README

}}} -->

# Snake-Vault

Miscellanous Python utilities.

## Package content

### snake_vault.enigma

`md5sum(filepath)`

Calculates the md5sum of a file.

### snake_vault.files

`file_info(f, filename=True, path=True, size=True, mime=True, md5=True)`

Gives information on a file.

`directory_files_info(dirpath)`

Gives information for all files in a directory.

### snake_vault.manipulator

`sanitize_input(data, accepted_characters=" a-zA-Z0-9_\-", replace_characters=None)`

Takes a list, a tuple or a string.

Give a list of tuples to replace_characters argument, to replace characters.

Removes any characters not in accepted_characters.

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

### snake_vault.snake_converter

Multi-format data converter.

Provides the command `snake-converter`, which is the equivalent of `python -m snake_vault.snake_converter`.

See https://github.com/fantomH/Snake-Vault/blob/main/snake_vault/snake_converter/README.md for further information.

### snake_vault.snake_sqlite

SQLite helper.

Provides the command `snake-sqlite`, which is the equivalent of `python -m snake_vault.snake_sqlite`.

See https://github.com/fantomH/Snake-Vault/blob/main/snake_vault/snake_sqlite/README.md for further information.

### snake_vault.timekeeper

`time_as_id()`

Returns a string representing the time now that can be used as an ID or a timestamp.

### snake_vault.snake_utils

Snake Utils.

Provides the command `snake-utils`, which is the equivalent of `python -m snake_vault.snake_utils`.

See https://github.com/fantomH/Snake-Vault/blob/main/snake_vault/snake_utils/README.md for further information.

<!--
# vim: foldmethod=marker
-->
