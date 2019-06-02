# l=123456
# #output : 1,2,3,4,5,6
# l1=[]
# m=str(l)
# for i in m:
#     l1.append(i)
# print(','.join(l1))

# count=0
# c=str(input('enter the value:'))
# for i in c:
#     if '6' in i:
#         count=count+1
#     elif '8' in i:
#         count=count+2
#     elif '9' in i:
#         count=count+1
# print(count)

# list=[1, 2, 3, 4, 5, 3, 2, 4, 5]


# a = ['a','b','c',4]
# b = [1,2,3,4,5,6]
# c={}
# for i in range(max(len(a),len(b))):
#     if len(a) == len(b):
#         c[i]= [a[i],b[i]]
#     elif len(a) > len(b):
#         b.append(" ")
#         c[i] = [a[i], b[i]]
#     else:
#         a.append(" ")
#         c[i] = [a[i], b[i]]
#     print(c)


# def sumNum(num):
#   previousNum=0
#   for i in range(num):
#     sum = previousNum + i
#     print(sum)
#     previousNum = i
# print("Printing current and previous number sum in a given range")
# sumNum(10)


# s="how are  you"
# print('display only those characters which are present at an even index:',s[::2])
# for i in range(0, len(s), 2):
#     print("index[",i,"]", s[i] )


# remove characters from string starting from zero upto n and return a new string
# def removechars(str,n):
#     return str[n:]
# print(removechars("siva sankar",5))


# return True if first and last number of a list is same
# l=[1,2,3,4,1]
# if l[0]==l[-1]:
#     print("true")
# else:print('false')


# def count_str(statement):
#     count=0
#     for i in range(len(statement)-1):
#         count +=statement[i:i+6]=='python'
#     return count
# c = count_str("python is easy.python is dynamic typed")
# print("python appeared", c,'times')


# Given a two list of ints create a third list such that should contain only odd numbers from the first list and even numbers from the second list
# def mergeList(listOne, listTwo):
#     thirdList = []
#     for num in listOne:
#         if (num % 2 != 0):
#             thirdList.append(num)
#     for num in listTwo:
#         if (num % 2 == 0):
#             thirdList.append(num)
#     return thirdList
# print("Merged List is")
# listOne = [10, 20, 23, 11, 17]
# listTwo = [13, 43, 24, 36, 12]
# print(mergeList(listOne, listTwo))


# def getMiddleThreeChars(str):
#     if len(str)>= 7 & len(str)%2 !=0:
#         middleIndex = int(len(str)/2)  #7/2=3
#         print('middleThreeChars:',str[middleIndex-1:middleIndex+2])   # 3-1:3+2 --> 2:5
#     else:
#         print("false")
# getMiddleThreeChars('dynamic')


# l=[1,2,3,4,3,2,1,2,3,4,5,6,5,7,7]
# dict={i:l.count(i) for i in l}
# print(dict)
# o/p : {1: 2, 2: 3, 3: 3, 4: 2, 5: 2, 6: 1, 7: 2}


# s = "missisipy"
# l = list(s)
# dict = {i:l.count(i) for i in l}
# print(dict)
# o/p : {'m': 1, 'i': 3, 's': 3, 'p': 1, 'y': 1}
# s=set(l)
# d={}
# for i in l:
#     d[i] = l.count(i)
# print(d)
#
#
# l1=[1,2,3]
# l2=['one','two','three']
# l3=[]
# #output :[(1, 'one'), (2, 'two'), (3, 'three')]
#
# # print(list(zip(l1,l2)))
#
# for i in enumerate(l1):
#     for j in enumerate(l2):
#         if i[0]==j[0]:
#             l3.append((i[1],j[1]))
#
# print(l3)


# a='a'
# print(ord(a))


# l1 = [1, 4, 5, 5, 6]
# d = {}
# for i in l1:
#     if (11 - i) in d:
#         print(str(11-i), ',', str(i))
#     else:
#         d[i] = 1


# A=10,20,30,40           # tuple packing
# print(A)
# print(type(A))
# a,b,c,d=A               # tuple unpacking
# print(a,b,c,d)


# a=10
# b=a
# a=20
# print(b)        # 10


# a=0101    #python 3 is not supported.but in python 2 it takes octal..so, a= 65
# b=2
# c=a+b             #c=67
# print(c)


# a = None
# print(type(a)) # NoneType

# for else and while else
# a=[10,20,30]
# for i in a:
#     print('for loop')
# else:
#     print('else block')

# how to find the python version
# import sys
# print(sys.version)
# a='siva'
# b='a'
# print(sys.getrefcount(a))  #  find the reference count


# l1=[1,2,3,4]
# l2=[5,6,7]
# l1.extend(l2)
# print(l1)
# l1.append(l2)
# print(l1)


# l=[55,44,77,66,88]
# # print(sorted(l))
# l.sort()
# print(l)


# l=['siva','sai','ram']
# # print([i for i in l if i.startswith('s')])
# print([i for i in l if i[0] == 'r'])

# find how many different char present in string
# a='hi how are u'
# print(len(set(a)))


# some standard python errors
# TypeError:
# ValueError:
# NameError:
# IndexError:
# IOError
# KeyError


# import random
# print(random.randrange(1000,10000))

# from random import shuffle
# l=[1,2,3,4,5,6,7]
# shuffle(l)
# print(l)


# import datetime
# import time
# time=datetime.datetime.now()
# time= time.asctime()
# print(time)


# how to debug python program in cmd
# python -m pdb (file name) test.py

# from math import sqrt
# nums = {x:int(float(sqrt(x))) for x in range(30)}
# print(nums)


d = {(x, x + 1): x for x in range(10)}
print(d)
