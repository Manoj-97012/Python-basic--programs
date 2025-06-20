class Bank_Account:
    def __init__(self,account_holder, balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        print(self.account_holder)