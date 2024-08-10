import uuid

class User:
    def _init_(self, name, initial_balance=0):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.balance = initial_balance

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "balance": self.balance
        }

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        return self.balance