# s={}
# print(type(s))
# s.add(1,2,3)
# print(s)
# print(type(s))

# s={1,2,3,4,5,'siva'}
# print(type(s))
# s.add('ravi')
# print(s)
# s.pop()
# print(s)
# s.update('7')
# print(s)
# s1=s.copy()
# print(s1)
# s1.remove('ravi')
# print(s1)
# print(s.difference(s1))
# print(s)
# s.difference_update(s1)
# print(s)

list
s1={1,2,3,4,5}
s2={3,4,8,6,7,1}
print(s1.union(s2))
# print(s2.union(s1))
print("intersection:",s1.intersection(s2))
print("difference based on s1:",s1.difference(s2),"...s1:",s1)
print("difference based on s2:",s2.difference(s1),'...s2:',s2)
# print("difference based on s1:",s1.difference_update(s2),"...s1:",s1)
print("difference based on s2:",s2.difference_update(s1),'...s2:',s2)
# print(s1.isdisjoint(s2))
# s3={1,2,3,4,5}
# s4={1,2,3,4,6}
# print(s3.isdisjoint(s4))
