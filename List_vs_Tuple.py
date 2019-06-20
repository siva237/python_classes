from dis import dis
from timeit import timeit
# print(dis(compile('(1,2,3,4,5,6)','string', 'eval')))
# print(dis(compile('[1,2,3,4,5,6]','string', 'eval')))

print(timeit('(1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2)', number=10000000))       #1.5892940676929277  fatser in iteratin
print(timeit('[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2]', number=10000000))        #  8.30956544804592  slower in iteration

# print(sum(range(1,101)))

