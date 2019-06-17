""" i/p : my name is siva sankar
    o/p : sankar siva is name my """
# str="my name is siva sankar"
# # s1=str.split()
# # print(s1)
# # s2=s1[::-1]
# # print(s2)
# # s3=" ".join(s2)
# # print(s3)
#
# print(" ".join(str.split()[::-1]))

""" i/p : my name is siva sankar
    o/p : My Name Is Siva Sankar"""
# str="my name is siva sankar"
# s1=str.split()
# print(s1)
# l=[]
# for i in s1:
#     l.append(i.capitalize())
# print(l)
# s2=" ".join(l)
# print(s2)


# l=[1,2,3,4,5]
# print(l[-1:])

""" I/P = [1,2,3,4]
    O/P : 10"""
# l=[1,2,3,4,5,9]
# k=0
# for i in l:
#     k = k+i
# print(k)


""" I/P :[[1,2,3],[4,5,6],[7,8,9]]
    O/p : [1,2,3,4,5,6,7,8,9]"""
# l=[[1,2,3],[4,5,6],[7,8,9]]
# l1=[]
# # list = [i for sublist in l for i in sublist]
# # print(list)
# for i in l:
#     for j in i:
#         l1.append(j)
#
# print(l1)


""" finding the missing no. in list"""
# l=[1,2,3,4,6,7]
# # m_number= sum(range(l[0],l[-1]+1)) - sum(l)
# # print((m_number))
# k=0
# for i in l:
#     k=k+i
# print(k)
# n=l[-1]
# sum=n*(n+1)/2
# print("sum",sum)
# print("missing no.:",sum-k)


""" i/p : [1,2,3,4,5,6,7]
    o/p : [7, 2, 3, 4, 6, 1]"""
# l=[1,2,3,4,6,7]
# l[-1],l[0] = l[0],l[-1]
# print(l)

"""find the second largest no. in the given list"""
# l=[1,8,6,4,5]
# for i in range(len(l)):
#
#     for j in range(1,len(l)-i):
#         if l[j - 1] > l[j]:
#             (l[j - 1], l[j]) = (l[j], l[j - 1])
# print(l)

# l.sort()
# print(l)
# print(l[-2])


# Write a Python Program to Check Common Letters in Two Input Strings?
# s1=input('Enter first string:')
# s2=input('Enter second string:')
# a=list(set(s1)&set(s2))
# print('The common letters are:',a)
# for i in a:
#     print(i)


# n = int(input("Enter any number: "))
# sum1 = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum1 = sum1 + i
# if(sum1 == n):
#     print("The number is a Perfect number!")
# else:
#     print("The number is not a Perfect number!")


# word = 'aaaannnnn'
# counter=1
# print(range(len(word)))
# for i in range(len(word)-1):
#     if word[i]==word[i+1]:
#         counter +=1
#         # print (word[i], counter, end='')
#     else:
#         counter=1
#         # print (word[i], counter)
#     print(word[i], counter, end='')


word = "abbcccdddduaa"
count = 1
length = ""
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        count += 1
    else:
        length += word[i] + str(count)
        count = 1
length += word[i+1] + str(count)
print(length)


# Group Anagrams from given list
# Anagrams are the words that are formed by similar elements but the orders in which these
# characters occur differ.

# The original list: ['lump', 'eat', 'me', 'tea', 'em', 'plum']
# The grouped Anagrams: [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]

# from collections import defaultdict
#
# test_list = ['lump', 'eat', 'me', 'tea', 'em', 'plum']
# print("The original list : " + str(test_list))
#
# # using defaultdict() + sorted() + values()
# temp = defaultdict(list)
# for ele in test_list:
#     temp[str(sorted(ele))].append(ele)
# res = list(temp.values())
# print(temp)
# print("The grouped Anagrams : " + str(res))


# using list comprehension + sorted() + lambda + groupby()
# from itertools import groupby
# test_list = ['lump', 'eat', 'me', 'tea', 'em', 'plum']
# print("The original list : " + str(test_list))
# temp = lambda test_list: sorted(test_list)
# res = [list(val) for key, val in groupby(sorted(test_list, key=temp), temp)]
# print("The grouped Anagrams : " + str(res))
