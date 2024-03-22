# Write your code here

def target_sum(ns, target):
    for i in ns:
        for o in ns:
            if (i+o) == target:
                return True
    return False

