# Write your code here

def double_dict_values(dictionary):
    new_diction = {}
    diction = dictionary.items()
    for x,y in diction:
        new_diction[x]= y*2
    return new_diction