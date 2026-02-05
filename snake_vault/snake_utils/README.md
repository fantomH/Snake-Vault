<!-- INFO {{{

# [Snake-Vault/snake_vault/snake_utils/README.md]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-02-04 16:27:02 UTC
# updated       : 2026-02-05 16:42:16 UTC
# description   : Snake-Utils README.

}}} -->

# Snake-Utils

Snake Utils.

Provides the command `snake-utils`, which is the equivalent of `python -m snake_vault.snake_utils`.

## check_application.py

Simple function to verify if an application is installed on the system.

Use as `snake-utils check-application pandoc`.

Options:

* --verbose: Display message if application exists (Optional).

### check_application(application, verbose)

* application: str. Application to verify.
* verbose: bool. Display message if application exists (Optional. Default: False).

## Sanitize data

Function to sanitize a string.

Use as `snake-utils sanitize-data "Hello!"`

* --accepted-characters: String of allowed characters (Optional. Default: ' a-zA-Z0-9_-').
* --replace-characters: List of tuple.

### sanitize_data(data, accepted_characters, replace_characters)

* --accepted-characters: String of allowed characters (Optional. Default: ' a-zA-Z0-9_-').
* --replace-characters: List of tuple.

<!--
# vim: foldmethod=marker
-->
