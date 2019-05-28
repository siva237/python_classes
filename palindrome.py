# s = input("enter something:")
# def palindrome(s):
#     print(s)
#     reverse = s[::-1]
#     if s == reverse:
#         print(s, "is palindrome")
#     else:
#         print(s,"not palindrome")
# palindrome(s)


'''fibonacci series '''
# n=int(input("enter the value:"))
# a,b=0,1
# print(a)
# print(b)
# for i in range(0,n):
#     c=a+b
#     a=b
#     b=c
#     print(c)



n = int(input("enter n value:"))
fact =1
if n<0:
    print("no factorials for less than zero")

elif n==0:
    print("factorial of 0 is 1")

else:
    for i in range(1,n+1):
        fact = fact*i

print("factoral of",n,"is:",fact)

