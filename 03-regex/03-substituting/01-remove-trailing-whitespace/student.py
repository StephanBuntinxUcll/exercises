# Write your code here

import re

def remove_trailing_whitespace(string, flag=re.MULTILINE):
    return re.sub('\s+$', '', string, flags=flag)

print(remove_trailing_whitespace('\n        fdf qqip saofp k        \t \n        fjdklfj f sfjslkf      \n        fdjfkldjf       '))


