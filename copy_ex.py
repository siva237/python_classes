import copy
# s={1,2,3,4}
# s1=copy.deepcopy(s)
# print(s1 is s)
# s.add(10)
# print(s)
# print(s1)


# s={1,2,3,4}
# s1=copy.copy(s)
# print(s1 is s)
# s.add(10)
# print(s)
# print(s1)

# l=[1,2,3,4]
# l1=copy.copy(l)
# print(l1 is l)
# l.insert(1,22)
# print(l)
# print(l1)


l=[1,2,3,4]
l1=l
print(l1 is l)
l.insert(1,22)
print(l)
print(l1)