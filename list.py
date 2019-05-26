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



def listmethods():
    list = [33, 22, 44, 11, 4, 5]
    list.sort(reverse=True)
    print(list)
    a=[1,2,3,'abc',2,2]
    # a.reverse()
    # print("reversed list",a)
    a.append(4)
    print(a)
    b = a.count(2)
    print("count the no. times repeated the give value:",b)
    a.insert(3,'hai')
    print(a)
    c = a.index('hai')
    print(c)
    d = a[2:5]  #slice operator...[start index : end index -1: step]
    d=a[::-1]
    print(d)
    a[3]="hello"
    print(a)
    for l in a:
        print(l,end=',')



listmethods()