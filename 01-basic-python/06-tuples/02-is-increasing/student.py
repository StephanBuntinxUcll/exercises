# Write your code here

def is_increasing(ns):
    ms = ns[1:]
    a = list(zip(ns,ms))
    for i in a:
        if i[0] > i[1]:
            return False
    return True


print(is_increasing([1, 2, 3]))