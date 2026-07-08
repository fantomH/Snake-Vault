<!--
+---------------------------------------------------------------------- INFO -+
| [Snake-Vault/snake_vault/flask/README.md]                                   |
|                                                                             |
| Author      : Pascal Malouin (https://github.com/fantomH)                   |
| Created     : 2026-06-05 14:30:59 UTC                                       |
| Updated     : 2026-06-20 00:15:58 UTC                                       |
| Description : Utility functions for Flask applications.                     |
+-----------------------------------------------------------------------------+
-->

# snake_vault.flask

Utility functions for Flask applications.

## Overview

The `snake_vault.flask` package contains reusable helper functions that simplify common Flask development tasks.

### Available Functions

| Function          | Description                                    |
| ----------------- | ---------------------------------------------- |
| `get_client_ip()` | Return the IP address of the connected client. |

---

#### get_client_ip(*trust_proxy=True*)

Return the IP address of the connected client.

When `trust_proxy` is enabled, the function checks the `X-Forwarded-For` HTTP header before falling back to Flask's `request.remote_addr`.

This is useful when the application is deployed behind a reverse proxy such as Nginx, Apache, HAProxy, Cloudflare, or a load balancer.

##### Examples

```python
from flask import Flask
from snake_vault.flask import get_client_ip

app = Flask(__name__)

@app.route("/")
def index():
    return f"Your IP address is {get_client_ip()}"
```

##### Notes

When running behind a reverse proxy, ensure that the proxy is configured to set the `X-Forwarded-For` header correctly.

Because HTTP headers can be forged by clients, `trust_proxy=True` should only be used when requests are received through a trusted proxy infrastructure.
