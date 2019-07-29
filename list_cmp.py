# def compare():
#     l1=[1,2,3,4]
#     l2=[2,3,1,4]
#     # l1 = list(input("enter fir'st list:"))
#     # l2 = list(input("enter first list:"))
#     print(l1 is l2)
#     print(l1 + l2)
#     l1.sort()
#     l2.sort()
#     if l1 == l2:
#         print("list are same")
#     else:
#         print("list not equal")
#     d = {}
#     print(d.fromkeys(l1))
#     d1 = zip(l1,l2)
#     print(dict(d1))
#
#
# compare()

# test_list1 = [1, 5, 6, 4, 7]
# test_list2 = [8, 4, 3]
# test_list3 = [9, 10, 3, 5]
#
# # printing original lists
# print("The original list 1 : " + str(test_list1))
# print("The original list 2 : " + str(test_list2))
# print("The original list 3 : " + str(test_list3))
#
# # using map() + set() + list comprehension
# # triple list difference
# temp1, temp2, temp3 = map(set, (test_list1, test_list2, test_list3))
# res1 = [ele for ele in test_list1 if ele not in test_list2 and ele not in test_list3]
# res2 = [ele for ele in test_list2 if ele not in temp1 and ele not in temp3]
# res3 = [ele for ele in test_list3 if ele not in temp2 and ele not in temp1]
#
# # print result
# print("The mutual difference list are : "
#       + str(res1) + " " + str(res2) + " " + str(res3))
# print(temp1)
# print(test_list1)

# list = ['a', 'b', 'c', 'd', 'e']
# print (list[10:])

# x = 'prep'
# print(len(x))
# for i in range(len(x)):
#     print(i)

# def myfunc(a):
#     a = a + 2
#     a = a * 2
#     return a
# print(myfunc(2))

# n = int(2345)
# tot = 0
# while n > 0:
#     dig = n%10
#     tot = tot+dig
#     n = n//10
# print('The total sum of digits is:', tot)


# n=int(2345)
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# print('Reverse of the number:',rev)

# import os
# print(os.getcwd())

# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
#
# names2[0] = 'Alice'
# names3[1] = 'Bob'
#
# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#     if ls[1] == 'Bob':
#         sum += 10
# print(sum)
# # print(ls)
# # print(names3)
# print(list('hello'))
# s='hello'
# print(list([s]))
# print(list(s))


# try:
#     print("a")
#     return
# except:
#     print ('b')
# else:
#     print ("c")
# finally:
#     print ("d")
# SyntaxError: 'return' outside function


# final={}
# def push(x):
#     if x in final:
#         final[x] += 1
#     else:
#         final[x] = 1
# push('Geeky')
# push('Prep')
# push('Geeky')
# print (len(final))
# print(final)


# def calc(i, arr = []):
#     arr.append(i)
#     print (arr)
#     return arr
# calc(1)
# calc(2)
# calc(3)


# def addtolist(listcontainer):
#     listcontainer += [10]
# sd = [10, 20, 30, 40]
# addtolist(sd)
# print(len(sd))    #5


# dictionary = {}
# dictionary[1] = 1
# dictionary['1'] = 2
# dictionary[1] += 1
# calc = 0
# for k in dictionary:
#     calc += dictionary[k]
# print(calc)
# print(dictionary)


# class Geeky:
#     def __init__(self, id):
#         self.id = id
# manager = Geeky(100)
# manager.__dict__['life'] = 498
# x = manager.life + len(manager.__dict__)
# print(x)
# print(manager.life)
# print(manager.__dict__)
# o/p: 500
# 498
# {'id': 100, 'life': 498}


# geeky = [1, 2, 3, 4]
# # geeky.extend([5, 6, 7, 8])
# geeky.append([5, 6, 7, 8])
# print(len(geeky))
# print(geeky)

# class gp:
#     def __init__(x, y):
#         x.y = y
#         y = 555
# s = gp(111)
# print(s.y)

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not x and y:
#     print(3)
# else:
#     print(4)

# a = True
# b = False
# c = False
#
# if a or b and c:
#     print("GEEKYPREP")
# else:
#     print("geekyprep")


# n = int(input("Enter n: "))
# if n < 0:
#     print("negative number")
# elif n == 0:
#     print(1)
# else:
#     fac = 1
#     for i in range(1, n+1):
#         fac = fac * i
#     print(fac)
