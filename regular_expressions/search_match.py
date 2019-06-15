import re

# string = "cake and cookies"
# pattern = "cake"
#
# out = re.search(pattern,string)
# print(out.group())

string = "icecream"
pattern = "c"
out = re.match(pattern,string)
print(out)

string1 = "cake and cookie"
pattern1 = "cake"
out1 = re.match(pattern1,string1)
print(out1.group())