# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/snake_tables/utils.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-03 20:10:31 UTC
# updated       : 2026-06-04 16:09:27 UTC
# description   : SnakeTables utils.

def get_language_dictionary(custom: dict[str, dict] | None = None) -> dict:
    try:
        from snake_vault.flask.linguae import get_display_language
        from snake_vault.flask.linguae import get_language_dictionary

        language = get_display_language()
        
        language_dictionary = get_language_dictionary(prefix="SNAKETABLE")

        if custom:
            language_dictionary = {
                **language_dictionary,
                **custom.get(language, {})
            }

        return language_dictionary

    except (ImportError, KeyError):
        return {}
