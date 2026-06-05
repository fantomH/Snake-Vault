# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/quiz/utils.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-03 20:10:31 UTC
# updated       : 2026-06-03 20:10:31 UTC
# description   : SnakeQuiz utils.

def get_language_dictionary():
    try:
        from snake_vault.flask.linguae import get_language_dictionary

        return get_language_dictionary(prefix="SNAKEQUIZ")

    except (ImportError, KeyError):
        return {}
