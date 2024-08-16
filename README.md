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

### snake_vault.timekeeper

`time_as_id()`

Returns a string representing the time now that can be used as an ID or a timestamp.
