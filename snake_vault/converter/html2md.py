## ----------------------------------------------------------------------- INFO
## [converter/html2md.py]
## author        : "fantomH"
## created       : 2023-09-24 13:01:40 UTC
## updated       : 2023-09-24 13:01:40 UTC
## description   : "Converts HTML to markdown"

from bs4 import (BeautifulSoup)
import markdownify
import re

# Define a function to demote headers by one level
def demote_header(match):
    header_level = int(match.group(2))
    new_level = min(header_level + 1, 6)  # Ensure the new level doesn't go beyond h6
    new_header = f"<{match.group(1)}h{new_level}{match.group(3)}>"
    return new_header

with open('/home/ghost/tmp/marktext', mode='r') as _input:
    md = _input.read()

    ## Fixing HTML
    md = BeautifulSoup(md)
    md = md.prettify()

    ## Demoting HTML headers
    md = re.sub(r'<(/?)[Hh](\d)(.*?>)', demote_header, md)

    md = markdownify.markdownify(md)

    # md = md.replace('\n\n\n', '')

    print(md)
