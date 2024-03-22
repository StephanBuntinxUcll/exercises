# Write your code here

import re

def one_or_more_a(string):
    return re.fullmatch( "a+", string)

# print(one_or_more_a("aar"))


