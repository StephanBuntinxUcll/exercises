# Write your code here

import re 

def collect_links2(string):
    return re.findall(r'\"(\w*)\"', string)

def collect_links(string):
    return re.findall(r'<a href="(.*)">', string)

print(collect_links2('<a href="a">fdf</a>fjklfjls<a href="b">qff</a>djqkljl<a href="abc">dfdg</a>fdjflkjdlf<a href="fiop">fdghh</a>fjdlfjlk<a href=""></a>'))

