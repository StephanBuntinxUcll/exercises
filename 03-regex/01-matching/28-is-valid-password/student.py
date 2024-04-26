# Write your code here

import re

def is_valid_password(string):
    positive_regex = re.fullmatch(r"[A-Z]+[a-z]+[0-9]+[\+\-\*\/\@]+{12,}", string) 
    negative_regex = re.search(r"(.)\1{2}", string)
    negative_regex2 = re.search(r"(.)(.*\1){3}", string)
    if not positive_regex:
        return False
    
    if negative_regex:
        return False
    if negative_regex2:
        return False
    
    return True

print(is_valid_password("ABCabc123@+/"))

