# Write your code here

def odd_keys_dict(dictionary):
    diction2 = {}
    v = dictionary.items()
    for x,y in v:
        if (x % 2) != 0:
            diction2[x] = y
    return diction2

print(odd_keys_dict({1: "a", 2:"b",3:"c"}))
