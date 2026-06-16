# ┌──────────────────────────────────────────────────────────────────── INFO ─┐
# │ Snake-Vault / flask / example / utils                                     │
# ├───────────────────────────────────────────────────────────────────────────┤
# │ [Snake-Vault/snake_vault/flask/example/app/utils.py]                      │
# │ Author      : Pascal Malouin (https://github.com/fantomH)                 │
# │ Created     : 2026-06-03 20:10:31 UTC                                     │
# │ Updated     : 2026-06-11 18:30:38 UTC                                     │
# │ Description : Utils.                                                      │
# └───────────────────────────────────────────────────────────────────────────┘

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
