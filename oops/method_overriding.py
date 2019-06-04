class A:
    def one(self):
        print("func one from class A")

    def two(self):
        print("func two from class A")

class B(A):
    def one(self):
        super(B,self).one()
        print("funct one from class B")


# super(<current_class>,self).method_name()
obj = B()
obj.one()
obj.two()