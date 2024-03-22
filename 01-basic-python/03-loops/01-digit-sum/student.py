# Write your code here

def last_digit(v):
    return v % 10

def remove_last_digit(c):
    return c // 10

remove_last_digit(1481)

def digit_sum(n):
    v=0
    sum =0
    q = str(n)
    for i in range(0,len(q)):
        v =last_digit(n)
        sum +=v
        n = remove_last_digit(n)

    return sum

print(digit_sum(23892380))



