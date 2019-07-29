# str() vs repr() in Python
# str() and repr() both are used to get a string representation of object.

import datetime
today = datetime.datetime.now()
# Prints readable format for date-time object
print(str(today))
# prints the official format of date-time object
print(repr(today))

s = 'Hello, Geeks.'
print (str(s))
print (repr(s))
# From above output, we can see if we print string using repr() function then
# it prints with a pair of quotes and if we calculate a value we get more precise value than str() function.
