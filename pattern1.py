# def pattern1():
#     num=1
#     for i in range(1,5):
#         for j in range(1,i+1):
#             print( i*j ,end=' ')
#         print()
# pattern1()


n=int(input('enter the vlaue:'))            #   3
for num in range(n+1):                      # o/p: 1
    for i in range(num):                     #     22
        print(num,end='')                    #     333
    print("\n")