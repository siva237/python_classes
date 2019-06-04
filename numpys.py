# Numpy is the core library for scientific computing in Python.
# It provides a high-performance multidimensional array object, and tools for working with these arrays.

import numpy
# a=numpy.array([1,2,3])   # rank 1 array
# print(a.shape)          # (3,)
# print(type(a))         # <class 'numpy.ndarray'>

# b=numpy.array([[1,2,3],[4,5,6]])   # rank 2 array
# print(b.shape)          # (2, 3)
# print(type(b))         # <class 'numpy.ndarray'>
#
#              # (0,0) (0,1) (0,2)
# print(b)    # 0 [[1    2    3]
#             #  1 [4    5    6]]
#             #   (1,0) (1,1) (1,2)
#
# print(b[0,0],b[0,2])    # 1  3


# Create an array of all zeros
# a1=numpy.zeros((2,2),int)
# print(a1)

# Create a 2x2 identity matrix
# b1=numpy.eye(2)
# print(b1)

# Create an array of all ones
# c1=numpy.ones((2,2))
# print(c1)

# Create a constant array
# d1=numpy.full((3,3),8)
# print(d1)


# e = numpy.random.randint(200,300,(2,2))  # Create an array filled with random values
# print(e)


