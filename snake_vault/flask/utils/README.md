<!--
┌────────────────────────────────────────────────────────────────────── INFO ─┐
│ Snake-Vault / Flask Utils                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ [Snake-Vault/snake_vault/flask/utils/README.md]                             │
│ Author      : Pascal Malouin (https://github.com/fantomH)                   │
│ Created     : 2026-06-05 14:30:59 UTC                                       │
│ Updated     : 2026-06-05 14:41:36 UTC                                       │
│ Description : Utility functions for Flask applications.                     │
└─────────────────────────────────────────────────────────────────────────────┘
-->

# snake_vault.flask.utils

Utility functions for Flask applications.

## Overview

The `snake_vault.flask.utils` package contains reusable helper functions that simplify common Flask development tasks.

### Available Functions

| Function          | Description                                    |
| ----------------- | ---------------------------------------------- |
| `get_client_ip()` | Return the IP address of the connected client. |

---

## get_client_ip

```python
get_client_ip(trust_proxy=True)
```

Return the IP address of the connected client.

When `trust_proxy` is enabled, the function checks the `X-Forwarded-For` HTTP header before falling back to Flask's `request.remote_addr`.

This is useful when the application is deployed behind a reverse proxy such as Nginx, Apache, HAProxy, Cloudflare, or a load balancer.

### Parameters

#### trust_proxy

```python
bool
```

Default: `True`

If `True`, use the first IP address found in the `X-Forwarded-For` header when present.

If `False`, ignore proxy headers and use Flask's `request.remote_addr` value only.

### Returns

```python
str | None
```

The client's IP address, or `None` if the address cannot be determined.

### Examples

Using the package import:

```python
from snake_vault.flask.utils import get_client_ip

ip_address = get_client_ip()
print(ip_address)
```

Ignoring proxy headers:

```python
from snake_vault.flask.utils import get_client_ip

ip_address = get_client_ip(trust_proxy=False)
```

Inside a route:

```python
from flask import Flask
from snake_vault.flask.utils import get_client_ip

app = Flask(__name__)

@app.route("/")
def index():
    return f"Your IP address is {get_client_ip()}"
```

### Notes

When running behind a reverse proxy, ensure that the proxy is configured to set the `X-Forwarded-For` header correctly.

Because HTTP headers can be forged by clients, `trust_proxy=True` should only be used when requests are received through a trusted proxy infrastructure.

---

## Importing

The package re-exports public utilities from its submodules.

```python
from snake_vault.flask.utils import get_client_ip
```

instead of

```python
from snake_vault.flask.utils.get_client_ip import get_client_ip
```

