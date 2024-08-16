# Snake-Vault
Miscellanous Python utilities.

## Package content

### snake_vault.enigma

`md5sum(filepath)`

Calculates the md5sum of a file.

### snake_vault.manipulator

`sanitize_input(data, accepted_characters=" a-zA-Z0-9_\-", replace_characters=None)`

Takes a list, a tuple or a string.

Give a list of tuples to replace_characters argument, to replace characters.

Removes any characters not in accepted_characters.
