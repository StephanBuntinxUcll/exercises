# Write your code here

import re 

def parse_link(string):
    matchs = re.fullmatch(r"<a href=\"(.+)\">(.+)</a>", string)
    if matchs:
        link , caption = matchs.groups()
        return tuple((caption, link))
    else:
        return None
    
# print(parse_link('<a href="ajflk">iojfgkld</a>'))

    
