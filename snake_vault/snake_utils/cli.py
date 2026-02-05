# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_utils/cli.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-02-04 16:14:28 UTC
# updated       : 2026-02-05 14:33:52 UTC
# description   : CLI for snake-utils

import argparse
import sys
from . import ( check_application,
                sanitize_data )

# --- sub argument parsers.

def check_application_parser(subparsers):
    p = subparsers.add_parser(
        "check-application",
        help="Check if application is installed on the system."
    )

    p.add_argument(
        "application",
        help="Application to verify"
    )

    p.add_argument(
        "--verbose",
        default=False,
        action="store_true",
        help="Enable verbose output."
    )

    p.set_defaults(func=check_application_handler)

def sanitize_data_parser(subparsers):
    p = subparsers.add_parser(
        "sanitize-data",
        help="Data sanitizer."
        )

    p.add_argument(
        "data",
        help="String, list or tuple to sanitize."
        )

    p.add_argument(
        "--accepted-characters",
        default=" a-zA-Z0-9_\\-",
        help="String of allowed characters (Optional. Default: ' a-zA-Z0-9_-')"
        )

    p.add_argument(
        "--replace-characters",
        default=None,
        help="List of tuple."
        )

    p.set_defaults(func=sanitize_data_handler)

# --- converter handlers.

def check_application_handler(args):

    check_application(
        application=args.application,
        verbose=args.verbose
        )

def sanitize_data_handler(args):

    sanitized=sanitize_data(
        data=args.data,
        accepted_characters=args.accepted_characters,
        replace_characters=args.replace_characters
        )
    print(sanitized)

def main():

    try:
        parser = argparse.ArgumentParser(
            prog="snake-utils",
            description="Snake utilities."
            )

        subparsers = parser.add_subparsers(
            dest="command",
            required=True
            )

        check_application_parser(subparsers)
        sanitize_data_parser(subparsers)

        args = parser.parse_args()
        args.func(args)
    except ImportError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
