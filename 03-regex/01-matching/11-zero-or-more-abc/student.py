# Write your code here

import re

def zero_or_more_abc(string):
    return re.fullmatch("(abc)*", string)

print(zero_or_more_abc("abcabcabc"))
