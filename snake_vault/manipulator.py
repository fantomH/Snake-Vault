# :----------------------------------------------------------------------- INFO
# :[snake_vault/manipulator.py]
# /author        : fantomH
# /created       : 2024-05-30 11:32:04 UTC
# /updated       : 2024-05-30 11:32:04 UTC
# /description   : Data manipulation utils

import re

# :-----/ (function) sanitize_input /-----:
def sanitize_input(data, accepted_characters=" a-zA-Z0-9_\-", replace_characters=None):
    """
    sanitize_input() takes a list, a tuple or a string, and:
        - will replace characters is replace_characters is not None;
        - will remove any characters not in accepted_characters.

    Arguments:
        - accepted_characters => (str)
            By default " a-zA-Z0-9_\-"
        - replace_characters => (list of tuples)
            ex: replace_characters=[(' ', '_'), ('A', 'a')]
    """

    rejected_characters_pattern = re.compile(f'[^{accepted_characters}]')

    if isinstance(data, (list, tuple)):

        if replace_characters:
            for r in replace_characters:
                _original, _replacement = r
                data = [x.replace(_original, _replacement) for x in data]

        # :Removes empty data items.
        sanitized_data = [rejected_characters_pattern.sub('', d) for d in data]

        return [x for x in sanitized_data if x != '']

    elif isinstance(data, str):

        if replace_characters:
            for r in replace_characters:
                _original, _replacement = r
                data = data.replace(_original, _replacement)
                
        # :Removes empty data items.
        return rejected_characters_pattern.sub('', data)

    else:
        raise TypeError("Data must be a list, tuple, or string")
