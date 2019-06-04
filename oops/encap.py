#Binding up the data into a single unit is nothing but encapsulation.

# class Hello:
#
#     a = 10 # public
#     _b = 20 #protected
#     __c = 30 # private
#
# obj = Hello()
# print(obj.__c)

class Hello:
    def __init__(self):
        self.__version = 10 # private variable

    def get_version(self):
        print(self.__version)

    def set_version(self,a):
        self.__version = a

obj = Hello()
obj.get_version()
obj.set_version(20)
obj.get_version()


