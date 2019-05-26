class Test:
    def division(self):

        a = int(input('enter the first value:'))
        b = int(input("enter the second value:"))
        try:
            c = a/b
            print(c)
        except Exception as e:
            print('division by zero is not possible',e)

t = Test()
t.division()