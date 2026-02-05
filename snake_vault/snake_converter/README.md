<!-- INFO {{{

# [Snake-Vault/snake_vault/snake_converter/README.md]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-10-20 16:23:59 UTC
# updated       : 2026-02-05 09:10:09 UTC
# description   : Snake-Converter README.

}}} -->

# Snake-Converter

Multi-format data converter.

Provides the command `snake-converter`, which is the equivalent of `python -m snake_vault.snake_converter`.

## csv2json

Convert a CSV file to JSON and write to a file or stdout.

### Command `snake-converter csv2json [options]`

```shell
# --- Convert a CSV file to a JSON file.
snake-converter csv2json --input file.csv --output file.json

# --- Convert a CSV file to JSON format and print to STDOUT.
snake-converter csv2json --input file.csv --output -
```

### csv_to_json(input_file, output_file)

* input_file: str. input CSV file.
* output_file: str. output JSON file path or '-' to print to terminal stdout.

## xml2sqlite

Convert data XML file to Sqlite table.

### Command `snake-converter xml2sqlite [options]`

Options:

* --input: input XML file.
* --db: output Sqlite database path. Will be created if non-existant.
* --table: output table. Will be created if non-existant.
* --element-local: Optional. Local name of the repeating record element. Will be auto-detected if this option is missing.
* --batch-size: Optional. Number of rows processed per batch (default: 1000).
* --drop-existing: Optional. Drop the destination table/view before importing (default: False).


### xml_to_sqlite(xml_path, db_path, table, element_local, batch_size, drop_existing)

* xml_path: str. Input XML file path.
* db_path: str. Output Sqlite database path.
* table: str. Output table name.
* element_local: str. Optional. Local name of the repeating record element.
* batch_size: int. Optional. Number of rows processed per batch (default: 1000). 
* drop_existing: bool. Optional. Drop the destination table/view before importing (default: False). 

<!--
# vim: foldmethod=marker
-->
