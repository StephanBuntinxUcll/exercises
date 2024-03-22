# Write your code here

def sum_dict_values(dictionary):
    sum = 0
    list_values = list(dictionary.values())
    for i in list_values:
        sum += i
    return sum
