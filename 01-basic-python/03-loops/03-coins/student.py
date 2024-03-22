# Write your code here

def coins(one, two, five, goal):
    for i in range(one + 1):

        for n in range(two + 1):

            for o in range(five + 1):
                if (i*1)+(n*2)+(o*5) == goal:
                    return True
    return False

print(coins(3,2,2,5))

