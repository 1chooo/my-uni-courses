class Banking():
    def __init__(self):
        self.balance = 1000

    def credit(self, amount):
        amount_type = (int, float, complex)

        if isinstance(amount, amount_type):
            self.balance += amount
            return self.balance
        else :
            raise ValueError

    def debit(self, amount):
        amount_type = (int, float, complex)

        if isinstance(amount, amount_type):
            self.balance -= amount
            return self.balance
        else :
            raise ValueError