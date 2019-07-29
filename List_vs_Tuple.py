# from dis import dis
#
# from timeit import timeit
# # print(dis(compile('(1,2,3,4,5,6)','string', 'eval')))
# # print(dis(compile('[1,2,3,4,5,6]','string', 'eval')))
#
#
# # import timeit
# # fun = 'sum(range(1,101))'
# # print(fun)
# # print(timeit.timeit(stmt=fun, number=100000))
#
#
# print(timeit('(1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2)', number=11111111))       #1.5892940676929277  fatser in iteratin
# print(timeit('[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2]', number=11111111))        #8.30956544804592  slower in iteration


import xlwings as xl
import pandas as pa

df = pa.DataFrame([[1, 2], [3, 4]],
                  columns=['c1', 'c2'],
                  index=['r1', 'r2'])
wb = xl.Book()
sheet = wb.sheets['sheet1']
sheet.range('A1').value = df
sheet.range('A1').options(pa.DataFrame, expand = 'table').value


# def world():
#     wb = xw.Book.caller()
#     wb.sheets[0].range('A1').value = 'Hello World!'

