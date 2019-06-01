# inner class
# 1.the class which is declared inside ano another class
# 2.without existing one type of object if there is no chance of existing another object then we go for inner class


class Outer:
    def __init__(self):
        print('outer class constructor')

    class Inner:
        def __init__(self):
            print('inner class constructor')

        def m1(self):
            print("inner class method")

#Outer().Inner().m1()


o = Outer()
i = o.Inner()
i.m1()