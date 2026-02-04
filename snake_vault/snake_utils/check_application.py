# ------------------------------------------------------------------------ INFO
# [Snake-Vault/snake_vault/snake_utils/check_application.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-02-04 16:30:12 UTC
# updated       : 2026-02-04 16:30:12 UTC
# description   : Check application.

import shutil
import sys

def check_application(application: str, verbose: bool = False) -> bool:
    if shutil.which(application) is None:
        raise SystemExit(
            f"{application} is required.\n"
            f"Install {application} from your OS package manager, then retry.\n"
        )
    if verbose:
        print(f"[✓] {application} found.")
    return True
