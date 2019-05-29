# a=[1,2,3,4,5]
# b=iter(a)
# print(b.__next__())
# print(list(b))


# generators

# def gen():
#     for i in range(10):
#         yield i
#
# out = gen()
# print(out.__next__())
# print(out.__next__())
# print(list(out))
# print(out.__next__())  # stop iteration

#generator expression

# out = (i for i in range(10))
# print(out.__next__())
# print(out.__next__())
# print(out.__next__())
# print(tuple(out))


def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for i in fib():
    if i>600:
        break
    print(i)


