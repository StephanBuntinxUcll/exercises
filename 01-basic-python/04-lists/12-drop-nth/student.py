# Write your code here

def drop_nth(xs,n):
    a = xs[:n]
    b = xs[n+1:]
    ys = a + b
    return ys
