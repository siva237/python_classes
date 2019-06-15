import re

string = """jeevan kumar
siva kumar
krishna reddy"""

print(re.split(r'\n+',string))

a = "hello, welcome ! to python"
print(re.split(r', | !',a))

