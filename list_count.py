# a=[1,2,3,4,5,6,7,8]
# count = 0
# for i in a:
#     print(i)
#     count=count+1
#
# print("no. of elements in a :",count)

# a=1
# a,b = a+1,a+1
# print(a,b)

# pyList = ['P', 'y', 't', 'h', 'o', 'n']
# pyTuple = ('P', 'y', 't', 'h', 'o', 'n')
# s="python"
# sObject = slice(3)
# print(pyList[sObject])
# sObject = slice(-1, 4, -1)
# print(pyList[sObject])
# print(s[sObject])
# print(s[-1:4:-1])
# print("aaa",s[:-2:1])
# print("bbb",s[ -1: -2:-1])
# print("ccc",s[ 0: -2:-1])


# a=123456
# b='123456'
# c=str(input('enter the value:'))       #i/p:123456
# print(c)
# print(a==b)
# print(c==b)
# print(b is c)
# for i in c:
#     print(i,end=',')             # o/p: 1,2,3,4,5



# l=[1,2,3,4,5]
# for i in enumerate(l):
#     print(i)


# Write a program which prints all duplicated values in a list
# l1 = [1, 2, 3, 4, 5, 4, 3, 5, 4, 6]
# length = len(l1)
# repeated = []
# for i in range(length):
#     k = i+1
#     for j in range(k,length):
#         if l1[i] == l1[j] and l1[i] not in repeated:
#             repeated.append(l1[i])
# print(repeated)


#Ways to remove duplicates from list
l1 = [1, 5, 3, 4, 5, 4, 3, 5, 2, 6]
non_repeated = []
for i in l1:
    if i not in non_repeated:
        non_repeated.append(i)
print(non_repeated)

# by using list comprehensions
# non_repeated=[]
# [non_repeated.append(i) for i in l if i not in non_repeated]
# print(non_repeated)

# s= set(l)
# list = list(s)
# print(list)

# res = [i for n, i in enumerate(l) if i not in l[:n]]
# print(res)
