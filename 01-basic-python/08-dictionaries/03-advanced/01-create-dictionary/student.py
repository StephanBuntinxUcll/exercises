# Write your code here

def create_dictionary(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary

print(create_dictionary(['a', 'b', 'c'], ['x', 'y', 'z']))

