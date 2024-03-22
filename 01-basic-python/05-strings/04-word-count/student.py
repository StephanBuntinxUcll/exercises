# Write your code here

def word_count(string):
    a=1
    if len(string) !=0:
        for i in string:
            if i == " ":
                a+=1
        return a
    else:
        return 0
   


