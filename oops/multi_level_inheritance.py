class A:
    def one(self):
        print("func one from class A")

class B(A):
    def two(self):
        print("func two from class B")

class C(B):
    def three(self):
        print("func three from class c")

obj = C()
obj.one()
obj.two()
obj.three()
print(C.mro())
