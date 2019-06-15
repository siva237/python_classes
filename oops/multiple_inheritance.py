# import pdb
# pdb.set_trace()
class A:
    def one(self):
        print("func one from class A")


class B:
    def two(self):
        print("func two from class B")

class C(B,A):
    def three(self):
        print("func three from class C")

obj = C()
obj.one()
obj.two()
obj.three()
print(C.mro())
