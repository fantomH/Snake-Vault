#!/usr/bin/env python3
# :----------------------------------------------------------------------- INFO
# :[snake_vault/menu.py]
# :author        : fantomH
# :created       : 2024-04-07 02:21:38 UTC
# :updated       : 2024-04-07 02:21:38 UTC
# :description   : Python menu using simple-term-menu

from simple_term_menu import TerminalMenu
from command import doit

def menu(options, title=None, menu_cursor="• ", show_search_hint=True):
    terminal_menu = TerminalMenu(options, title=title, menu_cursor=menu_cursor, show_search_hint=show_search_hint )
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    # options = ["entry 1", "entry 2", "entry 3"]
    options = doit(f"lsblk", capture_output=True).stdout.decode()
    print([x for x in options.split('\n') if ' part ' in x])
    # menu(options, title='THIS IS A MENU')
    

# :------------------------------------------------------------- FIN ¯\_(ツ)_/¯
