from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("car starts with key")

    def stop(self):
        print("car stops with key")

class Bike(Vehicle):

    def start(self):
        print("Bike starts with key or self")

    def stop(self):
        print("Bike stops with key")


obj = Car()
obj.start()
obj.stop()

obj1 = Bike()
obj1.start()
obj1.stop()




