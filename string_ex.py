from builtins import input


def strings():
    # str=input("enter the string:")
    # i=1
    # while i < len(str):
    #     print(str[i],end='')
    #     i=i+2

    str1 = input("enter the first string:")
    str2 = input("enter the first string:")
    output = ''
    i,j=0,0

    while i < len(str1) and j < len(str2):
        output=output+str1[i]+str2[j]
        i = i+1
        j = j+1
    print(output,end='')


strings()