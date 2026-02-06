# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_enigma/cli.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-02-06 12:34:32 UTC
# updated       : 2026-02-06 12:34:32 UTC
# description   : CLI for snake-enigma

import argparse
import sys
from . import (
    file_md5sum
    )

# --- sub argument parsers.

def file_md5sum__args_parser(subparsers):
    p = subparsers.add_parser(
        "file-md5sum",
        help="Calculate the md5sum of a file."
    )

    p.add_argument(
        "filepath",
        required=True,
        help="Input file path."
    )

    p.set_defaults(func=file_md5sum_handler)

# --- converter handlers.

def file_md5sum_handler(args):

    print(file_md5sum(args.filepath))

def main():

    try:
        parser = argparse.ArgumentParser(
            prog="snake-enigma",
            description="Hash, cipher, encryption..."
        )

        subparsers = parser.add_subparsers(
            dest="command",
            required=True
        )

        file_md5sum__args_parser(subparsers)

        args = parser.parse_args()
        args.func(args)
    except ImportError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
