# Write your code here

def contains_duplicates(xs):
    sorted_xs = sorted(xs)
    print(sorted_xs)
    if len(sorted_xs) > 1:
        for i in range(0,len(sorted_xs)):
            if sorted_xs[i] == sorted_xs[i-1]:
                return True
        return False
    else:
        return False

print(contains_duplicates([1]))