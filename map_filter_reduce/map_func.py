# print(list(filter(lambda x:x%2==0,[2,3,4,5,6,7,7,8])))
# print(list(map(lambda i:i**2,[2,3,4,5])))
# # from functools import reduce
# print(reduce(lambda x,y:x+y,[2,3,4,5]))
#
# def squares(x):
#     return x**2
#
# `
# print(list(map(squares,range(10))))

l=["python","java","web services","ruby-on-rails","Informatica","Devops"]
print(list(map(lambda x:len(x)<5,l)))

