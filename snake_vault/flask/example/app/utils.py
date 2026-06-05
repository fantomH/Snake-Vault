# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/example/app/utils.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-03 20:10:31 UTC
# updated       : 2026-06-04 17:04:13 UTC
# description   : Example utils.

from snake_vault.snake_utils.logger import SnakeLogger

log = SnakeLogger(profile="development")

def get_language_dictionary(custom: dict[str, dict] | None = None) -> dict:
    try:
        from snake_vault.flask.linguae import get_display_language
        from snake_vault.flask.linguae import get_language_dictionary

        language = get_display_language()
        
        language_dictionary = get_language_dictionary(prefix="EXAMPLE")

        if custom:
            language_dictionary = {
                **language_dictionary,
                **custom.get(language, {})
            }

        return language_dictionary

    except (ImportError, KeyError):
        return {}
