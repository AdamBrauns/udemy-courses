class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        return 'Withdrawal Accepted'
    
    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            return 'Withdrawal Accepted'
        else:
            return 'Funds Unavailable to withdrawal'

acct1 = Account('John Doe', 100)
print(acct1)
print(acct1.owner)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))