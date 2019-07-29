# Decorators:
# ----------
# * Functions are first class objects in python.
# * Decorators are Higher order Functions in python
# * The function which accepts 'function' as an arguments and return a function itslef is called Decorator.
# * Functions and classes are callables as the can be called explicitly.


# def hello(a):
# 	return a
# hello(5)
# -----------------------
# def hello(funct):
#
#
# 	return funct
# ----------------------
#
# 1. Function Decorators with arguments
# 2. Function Decorators without arguments
# 3. Class Decorators with arguments
# 4. Class Decorators without arguments.

class Student:
    def __init__(self):
        pass

    def __new__(self):
        pass

    def __call__(self):
        pass


obj = Student()


# def validate(func):
#     def abc(x, y):
#         if x > 0 and y > 0:
#             print(func(x, y))
#         else:
#             print("x and y values should be greater than 0")
#     return abc
# @validate
# def add(a, b):
#     return a + b
# out = add(20, 20)
# @validate
# def sub(a, b):
#     return a - b

# print(out)
# out1 = sub(20, 10)
# print(out1)

def myDecor(func):
    def wrapper(*args, **kwargs):
        print('Modified function')
        func(*args, **kwargs)
    return wrapper

@myDecor
def myfunc(msg):
    print(msg)

# calling myfunc()
myfunc('Hey')