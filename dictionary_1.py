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

# list of tuples ti dict
# listofTuples = [("Riti" , 11), ("Aadi" , 12), ("Sam" , 13),("John" , 22),("Lucy" , 90)]
# studentsDict = dict(listofTuples)
# print(studentsDict)


# listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
# # dictOfWords = { i : 5 for i in listOfStr }
# dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr) ) }
# dictOfWords1 = { listOfStr[i] : len(listOfStr[i]) for i in range(0, len(listOfStr) ) }
# print(dictOfWords)
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


# Sorting the Keys and Values in alphabetical using the value
key_value = {}
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323
print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))


