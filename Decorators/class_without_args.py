class Validate:

    def __init__(self,func):
        self.func = func

    def __call__(self, x,y):

        if x>0 and y>0:
            print(self.func(x,y))

        else:
            print("x and y should be greater than 0")


@Validate
def add(a,b):
    return a+b

out = add(22,0)


