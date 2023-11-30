from unittest import TestCase
from bank_package.account import *


class AccountTest(TestCase):
    def test_that_my_account_can_deposit_and_check_balance(self):
        account = Account("full_name", "pin", "1")
        account.deposit(Decimal(1000))
        self.assertEqual(Decimal(1000), account.check_balance("pin"))

    def test_that_my_account_can_throw_exception_for_invalid_amount(self):
        account = Account("full_name", "pin", "1")
        with self.assertRaises(DepositAmountLessThanZeroError):
            account.deposit(0)

    def test_that_my_account_can_deposit_more_than_once(self):
        account = Account("full_name", "pin", "1")
        account.deposit(Decimal(1000))
        account.deposit(Decimal(2500))
        self.assertEqual(Decimal(3500), account.check_balance("pin"))

    def test_that_my_account_can_throw_exception_for_invalid_pin(self):
        account = Account("full_name", "pin", "1")
        with self.assertRaises(PinError):
            account.check_balance("pin1")

    def test_that_my_account_can_withdraw_money(self):
        account = Account("full_name", "pin", "1")
        account.deposit(1000)
        account.withdraw(999, "pin")
        self.assertEqual(1, account.check_balance("pin"))

    def test_that_my_account_will_throw_an_exception_if_amount_to_withdraw_exceeds_balance(self):
        account = Account("full_name", "pin", "1")
        account.deposit(1000)
        with self.assertRaises(AmountGreaterThanBalanceError):
            account.withdraw(2000, "pin")
