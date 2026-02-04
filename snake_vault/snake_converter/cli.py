# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_converter/cli.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-10-20 15:43:58 UTC
# updated       : 2026-02-04 15:58:38 UTC
# description   : CLI for snake-converter

import argparse
from . import ( csv_to_json )

# --- sub argument parsers.

def csv2json_args_parser(subparsers):
    p = subparsers.add_parser(
        "--csv2json",
        help="Convert CSV to JSON."
    )

    p.add_argument(
        "--input",
        required=True,
        help="Input csv path."
    )

    p.add_argument(
        "--output",
        required=True,
        help="Output JSON path or '-' for stdout."
    )

    p.set_defaults(func=csv2json_handler)

# --- converter handlers.

def csv2json_handler(args):
    print(f"👉 Convertir CSV to JSON.")

    csv_to_json(args.input, args.output)    

def main():
    parser = argparse.ArgumentParser(
        prog="snake-converter",
        description="Multi-format data converter."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    csv2json_args_parser(subparsers)

    args = parser.parse_args()
    args._func(args)

# def main():
#     parser = argparse.ArgumentParser(
#         description="Convert files."
#     )
#     parser.add_argument("--csv2json", action="store_true", help="Convert CSV to JSON")
#     parser.add_argument("--input", required=True, help="Input file path")
#     parser.add_argument("--output", required=True, help="Output file path or '-' for stdout")
# 
#     args = parser.parse_args()
# 
#     if args.csv2json:
#         csv_to_json(args.input, args.output)
#     else:
#         print("❌ Error: No conversion mode specified. Use --csv2json.\n")
#         parser.print_help()
#         sys.exit(1)
