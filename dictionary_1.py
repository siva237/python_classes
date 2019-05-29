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
s={1,2,3,4}
d= dict.fromkeys(s, 1)
print(d)
