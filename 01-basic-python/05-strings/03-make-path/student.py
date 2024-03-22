# Write your code here

def make_path(parts):
    a = str(parts)
    b = a.strip("[]")
    return b.replace(",","/").replace("'", "").replace(" ","")


print(make_path(['abc', 'def', 'xyz', 'aaaa', 'foo']))