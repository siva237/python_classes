
a=int(input("enter the no.:"))
if (a>1):
    for i in range(2,a):
        if (a&i)==0:
            print(a," is nor prime numberrrr")
            break

        else:
            print(a,"is prime no.")
else:
    print(a, " is nor prime number")

