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

# list=[1,2,3,4,5,3,2,4,5]
list="siva sankar siva"
list1=list.split()
count_dict= {}
for i in list1:
    count_dict[i] = count_dict.get(i, 0)+1
print(count_dict)

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