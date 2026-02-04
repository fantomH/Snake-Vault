# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_utils/cli.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-02-04 16:14:28 UTC
# updated       : 2026-02-04 16:14:28 UTC
# description   : CLI for snake-utils

import argparse
from . import ( check_application )

def main():
    parser = argparse.ArgumentParser(
        description="Snake utilities."
    )
    parser.add_argument("--check-application",
                        metavar="APP",
                        help="Check if application is installed on the system.")
    parser.add_argument("--verbose",
                        action="store_true",
                        help="Enable verbose output, if available.")

    args = parser.parse_args()

    if args.check_application:
        check_application(
            application=args.check_application,
            verbose=args.verbose
        )
