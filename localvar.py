#global variable
# 1.from the clsaa directly we can declare global variable
# 2.within a method we can declare global variables by using global key word

# local variables
# 1.within the method we can declare local variable
# 2.local variables are available within the method only

a=10
class Test:
    #global b  here not possible to declare global variable
    # def __init__(self,b):
    #  self.b=b              #in constructor also not possible to declare global variables
    def m1(self):
        global b,a
        a=333
        b=20
        c=444
        print(a)
        print(c)
    def m2(self):
        print(b)
        print(a)
        #print(c)
t=Test()
t.m1()
t.m2()
