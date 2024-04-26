# Write your code here

import re 

# def hide_email_addresses(string):
#     def replace(match):
#         mat = re.findall("[a-zA-Z0-9\.@]+", string)
#         for i in mat:
#             return "*"*len(i)
#     return re.sub(r"[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-zA-Z]*", replace, string)

def hide_email_addresses(string):
    def replace(match):
       print(match)
       print(match.group())
       return "*"*len(match.group())
      
    return re.sub(r"[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-zA-Z]*", replace, string)

print(hide_email_addresses("a@c.com fsjdf jfslk fkls fjl df\n    jalfkj b@d.be fjdlkf jfkljdlkf\n    qpoiopc fdfqpof ifppopo fkpqo\n    qfjlkl [xyz@ppp.fr] jkfljqlkj"))