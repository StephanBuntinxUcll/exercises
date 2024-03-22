# Write your code here

def keys_with_value(dictionary, value):
    new_dict = []
    dict_list = dictionary.items()
    for x,y in dict_list:
        if y == value:
            new_dict.append(x)
    return new_dict

print(keys_with_value({'a': 1, 'b': 2, 'c': 3}, 2))
