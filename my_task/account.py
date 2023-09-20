class Account:
    def __init__(self, name):
        self._name = name
        self._balance = 0

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, money):
        if self._balance >= money and self._balance > 0:
            self._balance -= money
        elif money < 0:
            return self._balance

        print("you have exceeded the balance")
        return self._balance
