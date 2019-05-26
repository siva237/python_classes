#static variable
# 1.the value is not varied from object to object
# 2.for all objects single copy will be created

#where we have to declare static variables:
#1.within the class directly but from out side of any method
#2.constructor or instance method or static method by using class name
#3.inside class method cls vaariable or by using class name
#4.out side of class by using class name

# class Student:
#     cname="aditya"
#     def __init__(self,name,rollno,age):
#         self.name1=name
#         self.rollno1=rollno
#         self.age1=age
#
# s=Student("sai",111,22)
# print(s.name1,s.rollno1,s.age1,Student.cname)
# print(Student.__dict__)

class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        Test.a=30
t1=Test()
t2=Test()
t2.m1()
t2.b=444
Test.a=555
print(t1.a,t1.b)
print(t2.a,t2.b)