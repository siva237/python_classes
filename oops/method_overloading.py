class A:

    def one(self,*args):
        print("Overlaoding::",args)

obj = A()
obj.one(2,3,4,5,6)