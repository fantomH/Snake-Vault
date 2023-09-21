## ----------------------------------------------------------------------- INFO
## [messages.py]
## author        : fantomH
## created       : 2023-09-21 00:54:07 UTC
## updated       : 2023-09-21 00:54:07 UTC
## description   : Display messages.

class Colors:
    BLUE = '\033[34m'
    BOLD = '\033[1m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    RESET = '\033[m'
    YELLOW = '\033[33m'

def message(category, msg):

    if category == 'action':
        print(f"{Colors.GREEN}[*]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'result':
        print(f"{Colors.BLUE}[-]{Colors.RESET} {msg}")
    elif category == 'question':
        ## The input will be in variable `answer`.
        answer = input(f"{Colors.BLUE}[?]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'alert':
        print(f"{Colors.YELLOW}[!]{Colors.RESET} {msg}")
    elif category == 'warning' or category == 'error':
        print(f"{Colors.RED}[!]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'title':
        print(f"{Colors.BOLD}{msg}{Colors.RESET}")

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
