#List
#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
#heterogeneous objects can be allowed,duplicate values are allowed,list is mutable.

# Python List Built-in functions
# Python provides the following built-in functions which can be used with the lists.
#
# SN	Function	Description
# 1	cmp(list1, list2)	It compares the elements of both the lists.
# 2	len(list)	It is used to calculate the length of the list.
# 3	max(list)	It returns the maximum element of the list.
# 4	min(list)	It returns the minimum element of the list.
# 5	list(seq)	It converts any sequence to the list.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# def listmethods():
#     list = [33, 22, 44, 11, 4, 5]
#     list.sort(reverse=True)
#     print(list)
#     a=[1,2,3,'abc',2,2]
#     # a.reverse()
#     # print("reversed list",a)
#     a.append(4)
#     print(a)
#     b = a.count(2)
#     print("count the no. times repeated the give value:",b)
#     a.insert(3,'hai')
#     print(a)
#     c = a.index('hai')
#     print(c)
#     d = a[2:5]  #slice operator...[start index : end index -1: step]
#     d=a[::-1]
#     print(d)
#     a[3]="hello"
#     print(a)
#     for l in a:
#         print(l,end=',')


# from functools import reduce
# l1 = [1, 2, 3, 4, 5]
# # print(reduce(lambda x, y: x + y, l1))
# a = len(l1)
# print(a)
# sum = a*(a+1)/2
# print(sum)


# def getMissingNo(A):
# A = [1, 2, 4, 5, 6]
# n = len(A)
# total = (n + 1) * (n + 2) / 2
# sum_of_A = sum(A)
# retur = total - sum_of_A
# print(retur)


# s = 'hi how are you'
# l1 = list(s)
# print({x: l1.count(x) for x in l1})

# num = 2345
# s = str(num)
# for i in s:
#     print('|'+'*'*int(i))

# l1 = [0,0,1,0,1,1,0,1]   # [0, 0, 0, 0, 1, 1, 1, 1]
# for i in range(len(l1)):
#     for j in range(i+1, len(l1)):
#         if l1[i] > l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
# print(l1)


# d = {'aa': 22, 'vv': 33}
# print(sorted((key, value) for (key, value) in d.items()))
# print(sorted((value, key) for (key, value) in d.items()))

# s = 'hello python programmer hello'
# # l1 = s.split()
# # print(l1)
# print({i:len(i) for i in s.split()})
# # print({i: l1.count(i) for i in l1})
# l2 = ['a', 'f', 'g', 'a', 'A', 'g']
# print({i: l2.count(i) for i in l2})


# l1 = [2,2,2]
# l2 = [3,3,3]
# l3 = []
# for i in range(0, len(l1)):
#     l3.append(l1[i] + l2[i])
#
# print(l3)
# print([l1[i]+l2[i] for i in range(len(l1))])

def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
def mk2():
    print("Ordinary")
p = mk(mk2)
p()