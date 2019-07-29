# reduce() in Python
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the
# list elements mentioned in the sequence passed along.This function is defined in “functools” module.

# Working :

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and
# the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

from functools import reduce

# print(reduce(lambda x: x*2, range(10))) # range function not work in reduce

# print(reduce(lambda x, y: x+y, [2, 3, 4, 5]))

# lis = [1, 3, 5, 6, 2, ]
#
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(reduce(lambda a, b: a + b, lis))
#
# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(reduce(lambda a, b: a if a > b else b, lis))

import operator

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(reduce(operator.add, ["geeks", "for", "geeks"]))