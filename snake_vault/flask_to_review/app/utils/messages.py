# :----------------------------------------------------------------------- INFO
# [Snake-Vault/snake_vault/flask/app/utils/messages.py]
# /author        : fantomH
# /created       : 2024-04-17 12:25:17 UTC
# /updated       : 2024-04-17 12:25:22 UTC
# /description   : Display messages.

class Colors:

    """Colors - Colors class

    # /module : Snake-Vault/snake_vault/messages.py
    # /version: 2024-04-17 12:13:55 UTC

    Examples:
        blue = Colors.BLUE
    """

    BLUE = '\033[34m'
    BOLD = '\033[1m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    RESET = '\033[m'
    YELLOW = '\033[33m'

def message(category, msg):

    """message() - Formated messages.

    # /module : Snake-Vault/snake_vault/messages.py
    # /version: 2024-04-17 12:14:16 UTC

    Arguments:
        category: (str) Type of message available.
             - action:
               [*] Setting preset for random number.
             - result:
               [-] 33Gb found.
             - question:
               [?] What would you like?
             - alert:
               [!] You might want to install optional dependancies.
             - warning/error:
               [!] Unable to fetch file.
             - title:
               HOSTNAME          IP                PATH
               `title` will not align columns. You will have to do it manually.
    """

    if category == 'action':
        print(f"{Colors.GREEN}[*]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'result':
        print(f"{Colors.BLUE}[-]{Colors.RESET} {msg}")
    elif category == 'question':
        # :The input will be in variable `answer`.
        answer = input(f"{Colors.BLUE}[?]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'alert':
        print(f"{Colors.YELLOW}[!]{Colors.RESET} {msg}")
    elif category == 'warning' or category == 'error':
        print(f"{Colors.RED}[!]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'title':
        print(f"{Colors.BOLD}{msg}{Colors.RESET}")

# :------------------------------------------------------------- FIN ¯\_(ツ)_/¯
