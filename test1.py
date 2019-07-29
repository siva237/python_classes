# s1 = 'abcde'
# s2 = '1234567'
# s3 = 'ABCDEFGHIJ'
# i = j = k = 0
# out =''
# while i< len(s1) or j < len(s2) or k < len(s3):
#     if i < len(s1):
#         out +=s1[i]
#         i +=1
#     if j < len(s2):
#         out += s2[j]
#         j +=1
#     if k < len(s3):
#         out += s3[k]
#         k +=1
# print(out)   # a1Ab2Bc3Cd4De5E6F7GHIJ


""" i/p : my name is siva sankar
    o/p : sankar siva is name my"""
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


''' i/p : python programming language
    o/p :nohtyp gnimmargorp egaugnal '''
# str1 = 'python programming language'
# s1 = str1.split()
# l1 = []
# for i in s1:
#     l1.append(i[::-1])
# print(l1)
# print(" ".join(l1))

''' i/p : one two three four five six
    o/p : one owt three ruof five xis'''
# str1 = 'one two three four five six'
# word = str1.split()
# l1 = []
# i = 0
# while i < len(word):
#     if i % 2 == 0:
#         l1.append(word[i])
#     else:
#         l1.append(word[i][::-1])
#     i += 1
# out = " ".join(l1)
# print(out)


s = 'b8c96gd4'  # """ o/p : bcdg4689"""
# print(sorted(s))
# alphbets = []
# digits = []
# for ch in s:
#     if ch.isalpha():
#         alphbets.append(ch)
#     else:
#         digits.append(ch)
# l1 = "".join(sorted(alphbets)+sorted(digits))
# print(l1)


# s = 'a1b2c3'    # o/p : abbccc
# out = ''
# for ch in s:
#     if ch.isalpha():
#         x = ch
#     else:
#         out = out + x*int(ch)
# print(out)


# word = "abbcccdddduaa"      # o/p : a1b2c3d4u1a2
# count = 1
# out = ""
# for i in range(len(word)-1):
#     if word[i] == word[i+1]:
#         count += 1
#     else:
#         out += word[i] + str(count)
#         count = 1
# out += word[i+1] + str(count)
# print(out)


# str = 'a5k3x2'      # o/p : afknxz
# out = ''
# for ch in str:
#     if ch.isalpha():
#         out += ch
#         x = ch
#     else:
#         d = int(ch)
#         newch = chr(ord(x) + d)
#         out += newch
# print(out)


#remove the duplicate string
# str = 'aabbddddbfbbfjjfhh'
# l1 = []
# for ch in str:
#     if ch not in l1:
#         l1.append(ch)
# print(''.join(l1))

# str = 'aabbddddbfbbfjjfhh'
# l1 = []
# for ch in str:
#     if ch not in l1:
#         l1.append(ch)
# for ch in l1:
#     print("{} occurs {} times".format(ch,str.count(ch)))


# str = 'hi hi hi how are u'
# l1 = str.split(" ")
# for i in l1:
#     print("{} occurs {} times".format(i, str.count(i)))


# d = {}
# for ch in str:
#     d[ch] = d.get(ch, 0)+1
# print(d)
# for k, v in d.items():
#     print('{} occurs {} times'.format(k, v))


# find the vowels in the given string
# str1 = 'Aabhibusaaa'        # o/p : {'a': 2, 'i': 1, 'u': 1}
# d = {}
# vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
# for ch in str1:
#     if ch in vowels:
#         d[ch] = d.get(ch, 0)+1
# print(d)


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
l=[[1,2,3],[4,5,6],[7,8,9]]
l1=[]
# list = [i for sublist in l for i in sublist]
# print(list)
# for i in l:
#     for j in i:
#         l1.append(j)
# print(l1)


""" finding the missing no. in list"""
# l = [8, 10, 11, 12, 13, 14]
# m_number = sum(range(l[0], l[-1]+1)) - sum(l)
# print((m_number))
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
#     if n % i == 0:
#         sum1 = sum1 + i
# if sum1 == n:
#     print("The number is a Perfect number!")
# else:
#     print("The number is not a Perfect number!")


# Group Anagrams from given list
# Anagrams are the words that are formed by similar elements but the orders in which these
# characters occur differ.

# str1 = input("enter the first string:")
# str2 = input("enter the second string: ")
# if sorted(str1) == sorted(str2):
#     print('both strings are anagrams')
# else:
#     print('not anagrams')

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
