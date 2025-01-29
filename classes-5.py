class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, quantity):
        self.balance+=quantity
        print(f"Deposited: ${quantity}, Current Balance: ${self.balance}")
    def withdraw(self, quantity):
        if  self.balance>=quantity:
           self.balance-=quantity
           print(f"Withdrew: ${quantity}, Current Balance: ${self.balance}")
        else:
           print("Withdrawals may not exceed the available balance")

mybank=Account("Zarina Sakhan", 180)

mybank.deposit(150)

mybank.withdraw(50)

