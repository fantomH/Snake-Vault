# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_converter/cli.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-10-20 15:43:58 UTC
# updated       : 2026-02-04 15:58:38 UTC
# description   : CLI for snake-converter

import argparse
from . import ( csv_to_json )

def main():
    parser = argparse.ArgumentParser(
        description="Convert files."
    )
    parser.add_argument("--csv2json", action="store_true", help="Convert CSV to JSON")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path or '-' for stdout")

    args = parser.parse_args()

    if args.csv2json:
        csv_to_json(args.input, args.output)
    else:
        print("❌ Error: No conversion mode specified. Use --csv2json.\n")
        parser.print_help()
        sys.exit(1)
