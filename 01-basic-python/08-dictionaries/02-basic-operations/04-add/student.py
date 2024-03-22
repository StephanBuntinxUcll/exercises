# Write your code here

def add2(dictionary, key, value):
    dictionary[key] = value
    return dictionary



def add(dictionary, key, value):
    dictionary.update({key : value})


print(add({'a': 1},"b",3))