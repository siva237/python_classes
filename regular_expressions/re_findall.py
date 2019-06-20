import re
email = "ple_ase cont_act us at: jeevanpjr@gmail.com , siva123@gmail.com, sam$@hotmail.com"

# print(re.findall(r'[\W]+\@[\w]+\.[\w]+', email))
# print(re.findall(r'[a-zA-Z0-9_]+\@[a-z]+\.[a-z]+ ', email))
# print(re.findall(r'[a-zA-Z0-9_$]+\@gmail+\.[a-z]+', email))
print(re.findall(r'[\w]+\_[\w]+', email))

ip = "ip address 10.10.10.10"
print(re.search(r'[\d]+\.[\d]+\.[\d]+\.[\d]+', ip).group())


