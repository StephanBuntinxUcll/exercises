# your code here

       
def remove_duplicates(xs):
    z =0
    ys= []
    a = list(enumerate(xs))
    ns = set(xs)
    for z in xs:
        if z in ns:
            if z not in ys:
                ys.append(z)
    return ys
  


# print(remove_duplicates([1, 5, 2, 3, 6, 4, 2, 6, 1, 4, 7, 9, 0, 4, 4, 4]))    

def test(xs):
    xs.append((zip(9,8)))
    return xs
    

print(test([[1, 5], [2, 3], [6, 4], [2, 6]]))


