#Tuple
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#tuple is immutable,duplicate values are allowed
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the first position of where it was found

def tuple_methods():
    t=(11,22,33,44,55,'hai',44)
    print(t.count(44))
    print(t.index(44))
    print(t)
tuple_methods()