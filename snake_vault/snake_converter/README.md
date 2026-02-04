<!-- INFO {{{

# [Snake-Vault/snake_vault/snake_converter/README.md]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-10-20 16:23:59 UTC
# updated       : 2026-02-04 16:04:01 UTC
# description   : Snake-Converter README.

}}} -->

# Snake-Converter

File converter.

Provides the command `snake-converter`, which is the equivalent of `python -m snake_vault.converter`.

## Command `snake-converter --csv2json`

Convert a CSV file to JSON and write to a file or stdout.

```shell
# --- Convert a CSV file to a JSON file.
snake-converter --csv2json --input file.csv --output file.json

# --- Convert a CSV file to JSON format and print to STDOUT.
snake-converter --csv2json --input file.csv --output -
```

<!--
# vim: foldmethod=marker
-->
