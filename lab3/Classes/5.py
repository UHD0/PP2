#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        dep = int(input())
        self.balance += dep
    def withdraw(self):
        wit = int(input())
        if wit <= self.balance:
            self.balance -= wit
        else:
            print('You have no enough money!')

owner = str(input())
balance = int(input())
my = Account(owner, balance)
my.deposit()
print(my.balance)
my.withdraw()
print(my.balance)
