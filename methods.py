#types of methods in python
# 1.instance method-->if one instance variable is there then this method called instance method
# 2.class method-->only static variable  then class method
# 3.static method--> not using static and instance variable

# class Test:
#     def m1(x):
#         print("some method:",x)
# t = Test()
# Test.m1(88)

#how to access members of one class inside another class

class Employee:

    def __init__(self, eno, ename, esal):
        print("Employee class constructor")
        self.eno = eno
        self.e_name = ename
        self.e_sal = esal

    def display(self):
        print("Employee no :", self.eno)
        print('Employee name :', self.e_name)
        print('Employee sal :', self.e_sal)


class Test:
    def update(self,emp):
        print('teat class')
        emp.esal = emp.esal+1000
        #emp.display()


e = Employee(12345, 'siva', 10000)
#Test.update(e)
t = Test()




