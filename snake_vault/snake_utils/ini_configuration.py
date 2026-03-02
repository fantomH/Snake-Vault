# ------------------------------------------------------------------------ INFO
# [/Snake-Vault/snake_vault/snake_utils/ini_configuration.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-03-02 15:27:12 UTC
# updated       : 2026-03-02 15:27:12 UTC
# description   : Utilities for INI configuration.

from configparser import ConfigParser
from pathlib import Path

def load_config(path: str) -> ConfigParser:
    cfg = ConfigParser()
    if not Path(path).exists():
        raise FileNotFoundError(f"[!] Missing config file: {path}")
    cfg.read(path, encoding="utf-8")
    return cfg
