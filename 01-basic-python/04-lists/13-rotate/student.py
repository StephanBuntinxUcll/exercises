# Write your code here

def rotate1(xs, n):
    a = xs[:n]
    b = xs[n:]
    del xs[n:]
    for i in b:
        xs.insert(0,i)
    return xs

print(rotate1(['a', 'b', 'c', 'd', 'e'], 4))

def rotate(xs,n):
    b = xs[n:]



# print(rotate(['a', 'b', 'c', 'd', 'e'], 3))
