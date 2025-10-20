# ------------------------------------------------------------------------ INFO
# [/Snake-Vault/snake_vault/converter/csv2json.py]
# author        : Pascal Malouin @https://github.com/fantomH
# created       : 2025-10-20 15:47:32 UTC
# updated       : 2025-10-20 15:47:32 UTC
# description   : Convert csv to json.

import csv
import json
import sys

def csv_to_json(input_file: str, output_file: str):
    """Convert a CSV file to JSON and write to a file or stdout."""

    with open(input_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    json_data = json.dumps(data, indent=4, ensure_ascii=False)

    if output_file == "-":
        print(json_data)
    else:
        with open(output_file, "w", encoding="utf-8") as jsonfile:
            jsonfile.write(json_data)
        print(f"[-] JSON written to: {output_file}")
