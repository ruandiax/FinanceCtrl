class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit (self,dep_amt):
       self.balance = self.balance + dep_amt
       print(f"Added {dep_amt} to the balance")

    def withdraw (self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print ('Withdraw accepted')
        else:
            print('Sorry not enought funds!')

    
    def __str__ (self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"