import re
# with open(r"C:/Users/siva sankar putturu/Desktop/test.txt","r")as file:
#     f1 = file.read()
# print(re.findall(r'[\w]+\@[\w]+\.[\w]+',f1))

with open(r"C:/Users/siva sankar putturu/Desktop/test.txt","r")as file:

    # print(re.findall(r'[\w]+\@[\w]+\.[\w]+', file.read()))
    # print(re.search(r'[\w]+\@[\w]+\.[\w]+', file.read()).group())
    print(re.findall(r'[\w]+\@[gmail]+\.[\w]+', file.read()))
