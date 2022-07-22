from decimal import Decimal

class Account:

    def __init__(self, name, balance) -> None:

        if balance < Decimal('0.00'):
            raise ValueError("Initial balance must be >= to 0.00")

        self.name = name
        self.balance = balance

    def deposit(self,amount):

        if amount < Decimal("0.00"):
            raise ValueError('Amount must be positive.')

        self.balance += amount




account1 = Account('john Green', Decimal('50.oo'))      