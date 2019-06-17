#Counter
from collections import Counter
# l = [3,3,4,5,56,6,7,3,2,4,5]
# # # s="python "
# # # l= list(s)
# # print(Counter(l))

#orderdict
# from collections import OrderedDict
#
# d=OrderedDict()
# d[1] = 'one'
# d[2] = 'two'
# d[3] = 'three'
#
# print(d)

#default dict

from collections import defaultdict

# l = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',5)]
#
# d = defaultdict(list)
#
# for k,v in l:
#     d[k].append(v)
#
#
# print(d)
from collections import Counter,defaultdict
l = "missisipi"
d=defaultdict(int)
# print(Counter(l))
for i in l:
    d[i] +=1

print(d)

s = "jeevan kumar"
#output : {'jeevan':1,'kumar':1}
s1 = s.split(' ')
# print(Counter(s1))
d = defaultdict(int)
for i in s1:
    d[i] +=1

print(d)
