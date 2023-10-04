from unittest import TestCase
from my_task.account import Account


class TestAccount(TestCase):
    def test_deposit(self):
        user_name = Account("Adesua")
        user_name.deposit(2000)
        self.assertEqual(2000, user_name.get_balance())

    def test_deposit_two(self):
        user_name = Account("Mr Chibuzor")
        user_name.deposit(0)
        self.assertEqual(0, user_name.get_balance())

    def test_deposit_three(self):
        user_name = Account("Felix")
        user_name.deposit(0.5)
        self.assertEqual(0, user_name.get_balance())

    def test_deposit_three(self):
        user_name = Account("Lisa")
        user_name.deposit(-1000)
        self.assertEqual(0, user_name.get_balance())

    def test_withdrawal(self):
        user_name = Account("Mr Sikiru")
        user_name.deposit(2000)
        user_name.withdraw(3000)
        self.assertEqual(2000, user_name.get_balance())

    def test_withdrawal_two(self):
        user_name = Account("Goodness")
        user_name.deposit(1000)
        user_name.withdraw(1000)
        self.assertEqual(0, user_name.get_balance())

    def test_withdrawal_three(self):
        user_name = Account("Goodness")
        user_name.deposit(2000)
        user_name.withdraw(0.50)
        self.assertEqual(2000, user_name.get_balance())