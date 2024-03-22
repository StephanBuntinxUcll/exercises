# Write your code here

def median(ns):
    xs = sorted(ns)
    if len(xs) % 2 != 0 :
        a = len(xs) //2
        return(xs[a])
    else:
        b =len(xs)//2
        return((xs[b]+ xs[b-1])/2)
    
   

