# class Car:
#     def m1(self):
#         print('car')
# class Engine(Car):
#     def m1(self):
#         print('engine')
# e=Engine()
# e.m1()
# print('method resolution order',Engine.__mro__)
# c = Car()
# c.m1()


# python support multiple inheritance
class Maruthi:
    def barnd(self):
        print('maruthi car')

class Audi:
    def brand(self):
        print('audi car')

class Engine(Audi, Maruthi):
    def start(cc):

        print('started',cc)

e = Engine()
e.barnd()
Engine.start('with 1000cc Engine')
print(Engine.__mro__)