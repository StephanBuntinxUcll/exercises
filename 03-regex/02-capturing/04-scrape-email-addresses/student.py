# Write your code here

import re 

def scrape_email_addresses(string):
    return re.findall(r'\w*\.*@\w*\.*\w*', string)

print(scrape_email_addresses('a@c.com fsjdf jfslk fkls fjl dfjalfkj b@d.be fjdlkf jfkljdlkf ...@... *a@b*'))