# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/utils/get_client_ip.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-04 20:28:00 UTC
# updated       : 2026-06-05 14:20:00 UTC
# description   : Get client IP from a Flask app.

from flask import request

def get_client_ip(trust_proxy: bool = True) -> str | None:
    """
    Return the client's IP address.

    Parameters
    ----------
    trust_proxy : bool
        If True, use X-Forwarded-For when present.
        If False, use REMOTE_ADDR only.
    """

    if trust_proxy:
        xff: str | None = request.headers.get("X-Forwarded-For")

        if xff:
            return xff.split(",")[0].strip()

    return request.remote_addr
