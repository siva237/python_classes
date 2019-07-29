# d={}
# print(type(d))
# d['name']='siva'
# print(d)
# d.update({'name':'ravi','name':'siva','age':25,'loc':'bangl'})
# print("updated dict...",d)
# print(len(d))
# d.setdefault('locc')
# print(d)
# print("get method...",d.get('locc'))
# # print(d.pop('name'))
# # print(d)
# # print(d.popitem())
# print(d.keys())
# print(d.values())
# print(d.items())

# d={'name':'siva','age':25}
# d1=d
# print(d1)
# d.clear()
# print(d1)

# d={'name':'siva','age':25}
# d1=d.copy()
# print(d1)
# d.clear()
# print(d1)
# d={'name':'siva','age':25}
# d1=d
# print(d1)
# d={}
# print(d1)
# print(d)


# how to iterate the dictionary key and values
# Iterate through all keys
# Iterate through all values
# Iterate through all key, value pairs

# Iterate through all keys
# statesAndCapitals = {
#                      'Gujarat' : 'Gandhinagar',
#                      'Maharashtra' : 'Mumbai',
#                      'Rajasthan' : 'Jaipur',
#                      'Bihar' : 'Patna'
#                     }
# for states in statesAndCapitals.keys():
#     print('STATES:',states)
#
# # Iterate through all values
# statesAndCapitals = {
#                      'Gujarat' : 'Gandhinagar',
#                      'Maharashtra' : 'Mumbai',
#                      'Rajasthan' : 'Jaipur',
#                      'Bihar' : 'Patna'
#                     }
# for capitals in statesAndCapitals.values():
#     print("CAPITALS:",capitals)
#
#
# # Iterate through all key, value pairs
# statesAndCapitals = {
#                      'Gujarat' : 'Gandhinagar',
#                      'Maharashtra' : 'Mumbai',
#                      'Rajasthan' : 'Jaipur',
#                      'Bihar' : 'Patna'
#                     }
# for states,Capitals in statesAndCapitals.items():
#     print(states,":",Capitals)


# convert set to dictionary
# s={1,2,3,4}
# d= dict.fromkeys(s, 1)
# print(d)

# list to dictionary
# l=['a','s','d']
# d=dict.fromkeys(l,0)
# print(d)

# list of tuples to dict
# listofTuples = [("Riti" , 11), ("Aadi" , 12), ("Sam" , 13),("John" , 22),("Lucy" , 90)]
# studentsDict = dict(listofTuples)
# print(studentsDict)


# listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" , 'now']
# dictOfWords = { i : 5 for i in listOfStr }
# dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr) ) }
# print(dictOfWords)
# dictOfWords1 = { listOfStr[i] : len(listOfStr[i]) for i in range(0, len(listOfStr) ) }
# print(dictOfWords1)

# Displaying the Keys Alphabetically:
# key_value = {}
# key_value[2] = 56
# key_value[1] = 2
# key_value[5] = 12
# key_value[4] = 24
# key_value[6] = 18
# key_value[3] = 323
# for i in sorted (key_value.keys()) :
#      print(i, end = " ")


# Sorting the Keys and Values in Alphabetical Order using the Key.
# key_value = {}
# key_value[2] = 56
# key_value[1] = 2
# key_value[5] = 12
# key_value[4] = 24
# key_value[6] = 18
# key_value[3] = 323
# for i in sorted (key_value) :
#     print ((i, key_value[i]), end =" ")


# Sorting the Keys and Values in alphabetical using the values and keys
# key_value = {}
# key_value[2] = 56
# key_value[1] = 2
# key_value[5] = 12
# key_value[4] = 24
# key_value[6] = 18
# key_value[3] = 323
# print('keys', sorted(key_value.items(), key = lambda kv:kv[0]))
# print('values', sorted(key_value.items(), key = lambda kv:kv[1]))


# d = {'name': 'siva', 'age': 25}
# del d['age']
# print(d)
# d2 = dict(d.items())

#This does make d2 point to an object equal to d1—but the same object, not a copy.
# The REPL output confirms this: d2 is d1 is True.
# d2 = d

# d2 = {}
# d2.update(d)
# print(d2)
# print(d['name':'age'])  # typeerror

# x = ['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30},'baz': 3}, 'c', 'd']
# print(x[2]['bar']['z'])


# d = {'a': 0, 'b': 1, 'c': 0}
#
# if d['a'] > 0:
#     print('a ok')
# elif d['b'] > 0:
#     print('b ok')
# elif d['c'] > 0:
#     print('c ok')
# elif d['d'] > 0:
#     print('d ok')
# else:
#     print('not ok')

# import pyqrcode
# from pyqrcode import QRCode
#
# # String which represent the QR code
# s = "www.geeksforgeeks.org"
#
# # Generate QR code
# url = pyqrcode.create(s)
#
# # Create and save the png file naming "myqr.png"
# url.svg("myqr.svg", scale=8)


# import operator
# x = {1: 'a', 3: 'f', 4: 'c', 2: 't', 0: 'l'}
# sorted_x = sorted(x.items(), key=operator.itemgetter(0))
# print(sorted_x)
# print(sorted(x.items(), key=lambda x: x[1]))
