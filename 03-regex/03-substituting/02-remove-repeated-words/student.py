# Write your code here

import re 

# def remove_repeated_words(string):
#     return re.sub(r"(\w*\b)\1+", r"\b\1", string)
# print(remove_repeated_words("name name name "))


def remove_repeated_words(string, flag=re.MULTILINE):
    mat = re.sub(r"\b(\w+)(\s+\1*\b)+", r"\1 ", string)
    return re.sub('\s+$', '', mat, flags=flag)
print(remove_repeated_words("aaa aaa bb bb c c"))