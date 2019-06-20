# class based decorators with arguments

class Validate:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self, func, *args):

        def abc(x,y):

            if x>0 and y>0:
                print(func(x,y))

            else:
                print("x and y should be greater than 0")

        return abc


@Validate(10,20)
def add(x,y):
    return x+y


out = add(22,22)