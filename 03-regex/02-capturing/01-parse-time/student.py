
import re

def parse_time(string):
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})(\.\d{3})?", string)

    if match:
        h, m, s, ms = match.groups(".000")
        ms = ms[1:]
        return tuple((int(h),int(m),int(s),int(ms)))
    else:
        return None
    
print(parse_time("21:51:48.111"))

# def parse_time2(string):
#     match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)

#     if match:
        
#         h, m, s, ms = match.groups()
#         if ms is None:
#             ms= "000"
#         else:
#             ms= ms[1:]
#         for i in match.groups():
#             i=int(i)
#             match.groups().a(int(i))

#         return match.groups()
#     else:
#         return None


# print(parse_time2("12:34:56.051"))

