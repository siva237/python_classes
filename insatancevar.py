# types of variables                         types of methods
# 1.instance variables                      1.instance methods
# 2.static variables                        2.static methods
# 3.local variables                         3.class methods

#  instance variable
# 1.the values varied from object to object is called instance variables
# 2.so, instance variables also called as object level variables

# where we have to declare instance variables:
# 1.inside the constructor by using self
# 2.inside instance method by using self
# 3.from out side of the class by using object reference

# how to access instance variables                           # how to access instance variables
# 1.within the class by using self                              1.del self.variable name
# 2.out side the class by using object reference variable       2.del object reference.variable name


class Student:
    def __init__(self, name, rollno):
        print("constructor")
        self.name1 = name
        self.roono1 = rollno
        #age=25
        self.age=25

        # print("my name is " , self.name1)
        # print("roll no is " , self.roono1)
    def info(self,marks):
        print("my name is ", self.name1)
        print("roll no is ", self.roono1)
        self.marks = marks
s = Student('sai',1)
s.mobile=123
s.info(88)
print(s.__dict__)  # by using "s.__dict__" we can able to find instance variables
del s.mobile
print(s.__dict__)


