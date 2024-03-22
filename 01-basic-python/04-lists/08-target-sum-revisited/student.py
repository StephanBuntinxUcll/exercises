# Write your code here

def target_sum(ns, target):
    for i in range(len(ns)):
        for o in range(len(ns)):
                if (ns[i]+ns[o]) == target and i != o:
                    return True
    return False

print(target_sum([1, 2, 2, 3, 3, 3, 8, 8], 16))