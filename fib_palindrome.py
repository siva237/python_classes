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

# fibonacci series by using generators
def fib(num):
    a,b = 0,1
    for i in range(0,num):
        yield a
        a,b = b, a+b

for item in fib(10):
    print(item)


# Python program to display the Fibonacci sequence up to n-th term using recursive functions


# Recursive function to
#    print Fibonacci sequence
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms = 10
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))





# n = int(input("enter n value:"))
# fact =1
# if n<0:
#     print("no factorials for less than zero")
#
# elif n==0:
#     print("factorial of 0 is 1")
#
# else:
#     for i in range(1,n+1):
#         fact = fact*i
#
# print("factoral of",n,"is:",fact)


# Function to return the factorial
#    of a number using recursion
# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)
# num = 4
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of",num,"is",recur_factorial(num))
