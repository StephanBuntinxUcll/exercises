# Write your code here

def add_indices(xs):
    ys =  []
    for i in range(len(xs)):
        ys.append(i)
    return list(zip(ys, xs))

# print(add_indices(("a","a","c","c","x")))
