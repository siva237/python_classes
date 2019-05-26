#how to call particular parent class method by using super()
#   2 ways
# 1. parentclassname.method name(self)
# 2. super(class name,self).method name()

#by using super() we can able to access the static variables, but unable to access the instance variable


class A:
    x=20
    def m1(self):
        print('A class m1 method')
class B(A):
    def m1(self):
        print('B class m1 method')
class C(B):
    def m1(self):
        print('C class m1 method')
class D(C):
    def m1(self):
        print('D class m1 method')
class E(D):
    def m1(self):
        #B.m1(1)
        super(C,self).m1()
        print(super().x)
        #print('E class m1 method')
e = E()
e.m1()