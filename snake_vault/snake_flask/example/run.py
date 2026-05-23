# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_flask/run.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-05-19 11:33:46 UTC
# updated       : 2026-05-19 11:33:46 UTC
# description   : Flask example.

from app import create_app

app = create_app({
    "SECRET_KEY": "test-secret"
})

if __name__ == "__main__":
    app.run(debug=True)
