class Methods:

    def __init__(self):
        print("init method")

    def instance_method(self):
        print("instance method")

    @staticmethod
    def static_method():
        print("static method")

    @classmethod
    def class_methods(cls):
        print("class methods")


# obj = Methods()
# obj.instance_method()
Methods.static_method()
# obj.class_methods()
Methods.class_methods()