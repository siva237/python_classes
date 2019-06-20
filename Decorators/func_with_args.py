def validate(a,b):
    print("validate decorator:",a,b)

    def one(func):
        print("function one:",func)

        def two(x,y):
            if x>0 and y>0:
                print(func(x,y))

            else:
                print("x and y values should be greater than 0")

        return two
    return one


@validate(2,3)
def add(m,n):
    return m+n

out = add(22,22)


