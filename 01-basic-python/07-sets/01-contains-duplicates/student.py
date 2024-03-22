# Write your code here

def contains_duplicates(xs):
    if xs != set(xs):
        print(xs, set(xs))
    return xs != list(set(xs))

print(contains_duplicates([1, 2, 3, 4, 5, 6]))