# print([i for i in range(10) if i%2==0])
# print([i**2 for i in range(10)])
#
# l=[2,3,4,5,6,7]
# print([i**3 for i in l])
#
# m=["python","java","web services","ruby-on-rails","Informatica","Devops"]
# print([i for i in m if len(i)>5])
# print([len(i) for i in m if len(i)>5])

# m=["python","java","web services","ruby-on-rails","Informatica","Devops"]
# print({i:len(i) for i in m })

# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# # print([i+j for i in l1 for j in l2])
# res_list = []
# for i in range(0, len(l1)):
#     res_list.append(l1[i] + l2[i])
#
# print(res_list)


l1=[1,2,3,'none',4]
print(len(l1))
print(l1[3])
