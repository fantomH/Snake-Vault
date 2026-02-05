# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_utils/cli.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-02-04 16:14:28 UTC
# updated       : 2026-02-04 16:14:28 UTC
# description   : CLI for snake-utils

import argparse
import sys
from . import ( check_application )

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
        defautl=False,
        action="store_true",
        help="Enable verbose output."
    )

    p.set_defaults(func=check_application_handler)

# --- converter handlers.

def check_application_handler(args):

    check_application(
        application=args.application,
        verbose=args.verbose
        )

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

        args = parser.parse_args()
        args.func(args)
    except ImportError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

# def main():
#     parser = argparse.ArgumentParser(
#         description="Snake utilities."
#     )
#     parser.add_argument("--check-application",
#                         metavar="APP",
#                         help="Check if application is installed on the system.")
#     parser.add_argument("--verbose",
#                         action="store_true",
#                         help="Enable verbose output, if available.")
# 
#     args = parser.parse_args()
# 
#     if args.check_application:
#         check_application(
#             application=args.check_application,
#             verbose=args.verbose
#         )
