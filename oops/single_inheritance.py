class A:
    def one(self):
        print("func one from class A")

class B(A):
    def two(self):
        print("func two from class B")

obj = B()
obj.one()
obj.two()
