# l = 123456
# #output : 1,2,3,4,5,6
# l1 = []
# # m = str(l)
# # for i in m:
# #     l1.append(i)
# # print(','.join(l1))
# [l1.append(i) for i in str(l)]
# print(','.join(l1))

# s = 'abc'
# l = list(s)
# l1 = list([s])
# print(l)
# print(l1)

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


# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# b = [1, 2, 3, 4, 5, 6]
# c = {}
# for i in range(max(len(a), len(b))):
#     if len(a) == len(b):
#         c[a[i]] = b[i]
#     elif len(a) > len(b):
#         b.append(" ")
#         c[a[i]] = b[i]
#     else:
#         a.append(" ")
#         c[a[i]] = b[i]
# print(c)
#
# print({x:y for x, y in zip(a, b)})


# def sumNum(num):
#   previousNum = 0
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
# c = count_str(" is python  easy.python is dynamic typed")
# print("python appeared", c,'times')


# Given a two list of ints create a third list such that should contain only odd number
# from the first list and even numbers from the second list
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
#     if len(str) >= 5 & len(str) % 2 != 0:
#         middleindex = int(len(str)/2)  #7/2=3
#         print('middleThreeChars:',str[middleindex-1:middleindex+2])   # 3-1:3+2 --> 2:5
#     else:
#         print("false")
# getMiddleThreeChars('dynam')


# l=[1,2,3,4,3,2,1,2,3,4,5,6,5,7,7]
# s = 'hi how r u hi u'
# l1 = s.split(' ')
# dicts = {i:l1.count(i) for i in l1}
# dicts1 = {i: len(i) for i in l1}
# print(dicts)
# print(dicts1)
# print(type(l1))

# o/p : {1: 2, 2: 3, 3: 3, 4: 2, 5: 2, 6: 1, 7: 2}


# s = "missisipy"
# l = list(s)
# # dict = {i:l.count(i) for i in l}
# # print(dict)
# # o/p : {'m': 1, 'i': 3, 's': 3, 'p': 1, 'y': 1}
# d={}
# for i in l:
#     d[i] = l.count(i)
# print(d)


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
# print(sorted(l))  # it will create a new list, doesnt modify the priginal list
# print(l)
# l.sort()          # it modify the original list
# print(l)


# l=['siva','sai','ram']
# # print([i for i in l if i.startswith('s')])
# print([i for i in l if i[0] == 'r'])

# find how many different char present in string
# a='hi how are u'
# print(set(a))


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


# d = {(x, x + 1): x for x in range(10)}
# print(d)


# def f(x, l1 = []):
#     for i in range(x):
#         l1.append(i*i)
#     print(l1)
#
# f(2)                # [0, 1]
# f(3,[3, 2, 1])      # [3, 2, 1, 0, 1, 4]
# f(3)                # [0, 1, 0, 1, 4]


# import re
# def camel_to_snake(text):
#     str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
#     return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
# print(camel_to_snake('PythonExercises'))
#
#
# snake_case = "this_is_a_snake_case_string"
# l = snake_case.split("_")
# print(l[0].capitalize() + "".join(map(str.capitalize, l[1:])))


# str = 'green-red-yellow-black-white'
# l1 = str.split('-')
# print(l1)
# l1.sort()
# print(l1)
# print('-'.join(l1))


# import string
# alphabet = set(string.ascii_uppercase)
# print(sorted(alphabet))
# def ispangram(string):
#     return set(string.upper()) >= alphabet
# string = "The quick brown fox jumps over the lazy dog"
# if (ispangram(string) == True):
#     print("Yes")
# else:
#     print("No")

# l = {}
# if not l:
#     print('l is empty')


# words = ['banana', 'pie', 'Washington', 'book']
# print(sorted(words, key=lambda x: x[::-1]))
# print(sorted(words))
# print(sorted(words, reverse=True))



# x = 10
# def a():
#     global x  # without accessing x from global to local you get unboundLocalError
#     print(x)
#     x += 1
#     print(x)
# a()


# import getpass
# print(getpass.getuser())

# from functools import wraps
#
# def makebold(fn):
#     @wraps(fn)
#     def wrapped(*args, **kwargs):
#         return "<b>" + fn(*args, **kwargs) + "</b>"
#     return wrapped
#
# def makeitalic(fn):
#     @wraps(fn)
#     def wrapped(*args, **kwargs):
#         return "<i>" + fn(*args, **kwargs) + "</i>"
#     return wrapped
#
# @makebold
# @makeitalic
# def hello():
#     return "hello world"
#
# @makebold
# @makeitalic
# def log(s):
#     return s
#
#
#
# print(hello())       # returns "<b><i>hello world</i></b>"
# print(hello.__name__)  # with functools.wraps() this returns "hello"
# print(log('hello'))


# import keyword
# print(keyword.kwlist)

# L = [("Alice", 25), ("Bob", 20), ("Alex", 5)]
# L.sort(key=lambda x: x[1])
# print(L)


# from operator import attrgetter
# def custom_sort(t):
#     return t[0]
#
# L = [("Alice", 25), ("Bob", 20), ("Alex", 5)]
# L.sort(key=custom_sort)
# l1 = sorted(L, key=custom_sort)
# print(l1)
# print(L)


# cities = ['hyd', 'chennai', 'delhi', 'bangalore', 'mumbai']
# smallest, *rest, highest = cities
# print('smallest: %s' %smallest)
# print(rest)


# def f1():
#     global s1
#     print(s1)
#     s1 = 'hiii'
#     print(s1)
#
#
# s1 = 'how'
# print('before function call : ', s1)
# f1()
# print('after function call: ', s1)


# l1 = [2,2,2]
# l2 = [3,3,3]
# print(list(map(lambda x, y: x+y, l1, l2)))

# for i in range(1):
#     print('hello')
#     print(type(i))


# import json
#
# # Convert JSON string to python dict.
# def python_json_string_to_dict():
#     # Create a JSON string.
#     json_string = '{"name": "Tom", "age" : 25, "score" : 100 }'
#     # Load the JSON string to python dict object.
#     dict_object = json.loads(json_string)
#     # Print dict value by key.
#     print(dict_object)
#     print(dict_object["score"])
#     print(dict_object["age"])
# python_json_string_to_dict()


# l1 = [1, 2, 3, 4, 5]
# str1 = 'siva'
# l2 = []
# for i in l1:
#     l2.append(str1+str(i))
# print(l2)
# # o/p : ['siva1', 'siva2', 'siva3', 'siva4', 'siva5']
#
#
# l1 = [1, 2, 3, 4, 5]
# str1 = 'siva'
# print([str1+str(i) for i in l1])
# # o/p : ['siva1', 'siva2', 'siva3', 'siva4', 'siva5']


# list_a = [1, 2, 3]
# list_b = [10, 20, 30]
#
# print(list(map(lambda x, y: x + y, list_a)))

# add = lambda x, y: x + y
#
# print(add(2, 3))


# dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
#
# l1 = map(lambda x: x['name'], dict_a)  # Output: ['python', 'java']
# print(list(l1))
#
# map(lambda x: x['points'] * 10, dict_a)  # Output: [100, 80]
#
# map(lambda x: x['name'] == "python", dict_a)  # Output: [True, False]


# import pickle
# # emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}
# # pickling_on = open("Emp.pickle","wb")
# # pickle.dump(emp, pickling_on)
# # pickling_on.close()
#
#
# pickle_off = open("Emp.pickle","rb")
# emp = pickle.load(pickle_off)
# print(emp)


# a = 1
# b = 2
#
# print(1 if a > b else -1 )


# from functools import reduce
# print(reduce(lambda x, y:x+y, [1,2,3,4]))

# a = 50
# def f():
#     global a
#     print(a)
#     a = 100
#     print('inside function', a)
# f = f()
# print('outside', a)


l = [1,2,3,8,6,7]
count = 0
for i in l:
    # count +=1
    count =count+1
print(count)

print(len(l))