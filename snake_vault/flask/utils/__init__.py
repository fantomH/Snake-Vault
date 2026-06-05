# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/flask/utils/__init__.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-04 20:28:00 UTC
# updated       : 2026-06-04 20:28:00 UTC
# description   : Flask utils.

from flask import request

def get_client_ip(trust_proxy=True):
    """
    Return the client's IP address.

    Parameters
    ----------
    trust_proxy : bool
        If True, use X-Forwarded-For when present.
        If False, use REMOTE_ADDR only.
    """

    if trust_proxy:
        xff = request.headers.get("X-Forwarded-For")

        if xff:
            return xff.split(",")[0].strip()

    return request.remote_addr
