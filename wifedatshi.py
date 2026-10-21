class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self_balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, deposit):
        if deposit > 0:
            self.__balance += deposit
        else:
            print("error! brokie")

    def withdraw(self, withdraw):
        if withdraw <= self.__balance:
            self.__balance
        else:
            print("error! brokie")

account = BankAccount("Mapicc", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())