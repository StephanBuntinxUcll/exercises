
# Write your code 

import re

def contains_three_digits(string):
    return re.fullmatch(".*[0-9]+.*[0-9]+.*[0-9]+", string)


print(contains_three_digits("1 2 3"))