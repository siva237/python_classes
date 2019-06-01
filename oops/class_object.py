class HelloWorld:
    a=10
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name

    def display(self):
        b=20
        print('rollno:',self.rollno, 'name:',self.name)



obj = HelloWorld(101,'jeevan')
obj.display()
