class Customer:
    bank_name = 'SBI'

    def __init__(self, name, balance=0):
        self.cname = name
        self.cbal = balance

    def deposit(self, amount):
        self.cbal = self.cbal+amount
        print("after deposit balance is :", self.cbal)

    def withdraw(self,amount ):
        if amount > self.cbal:
            print("ur withdrawing more than ur bank balance and ur balance is :", self.cbal)
        else:
            self.cbal = self.cbal - amount
            print("after withdraw ur balance is :", self.cbal)

    def balance(self):
        self.balance = self.cbal
        print("available balance is :", self.balance)


print("welcome to ", Customer.bankname)
name = input("enter ue name:")
c = Customer(name)
while True:
    print("d-Deposit \n w-Withdraw \n b-Balance \n e-Exit")
    option = input("choose ur option : ")
    if option == 'd' or option == 'D':
        amount = float(input("enter the amount to deposit:"))
        c.deposit(amount)

    elif option == 'w' or option == 'W':
        amount = float(input("enter thr withdraw amount:"))
        c.withdraw(amount)

    elif option == 'b' or option == 'B':
        c.balance()

    elif option == 'e' or option == 'E':
        print("thanks for banking")
        #sys.exit()

    else:
        print("choose valid option..")

