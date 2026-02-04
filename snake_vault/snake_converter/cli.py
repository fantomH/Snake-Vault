# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_converter/cli.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2025-10-20 15:43:58 UTC
# updated       : 2026-02-04 15:58:38 UTC
# description   : CLI for snake-converter

import argparse
import sys
from . import (
    csv_to_json,
    xml_to_sqlite
    )

# --- sub argument parsers.

def csv2json_args_parser(subparsers):
    p = subparsers.add_parser(
        "csv2json",
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

def xml2sqlite_args_parser(subparsers):
    p = subparsers.add_parser(
        "xml2sqlite",
        help="Convert XML and create an sqlite table."
    )

    p.add_argument(
        "--input",
        required=True,
        help="Input XML file path."
    )

    p.add_argument(
        "--db",
        required=True,
        help="Output Sqlite database path."
    )

    p.add_argument(
        "--table",
        required=True,
        help="Destination table name."
    )

    p.add_argument(
        "--element-local",
        dest="element_local",
        type=str,
        default=None,
        help="Local XML element to extract (optional)."
    )

    p.add_argument(
        "--batch-size",
        type=int,
        default=1000,
        help="Batch size for processing."
    )

    p.add_argument(
        "--drop-existing",
        action="store_true",
        help="Overwrite existing table."
    )

    p.set_defaults(func=xml2sqlite_handler)

# --- converter handlers.

def csv2json_handler(args):
    print(f"[*] Converting CSV to JSON.")

    csv_to_json(args.input, args.output)    

def xml2sqlite_handler(args):
    print(f"[*] Converting CSV to JSON.")

    xml_to_sqlite(
        xml_path=args.input,
        db_path=args.db,
        table=args.table,
        element_local=args.element_local,
        batch_size=args.batch_size,
        drop_existing=args.drop_existing
    )    

def main():

    try:
        parser = argparse.ArgumentParser(
            prog="snake-converter",
            description="Multi-format data converter."
        )

        subparsers = parser.add_subparsers(
            dest="command",
            required=True
        )

        csv2json_args_parser(subparsers)
        xml2sqlite_args_parser(subparsers)

        args = parser.parse_args()
        args.func(args)
    except ImportError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

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
