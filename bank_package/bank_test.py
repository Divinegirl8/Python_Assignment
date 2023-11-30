from unittest import TestCase
from bank_package.bank import Bank
from exceptions.account_number_not_found_error import AccountNumberNotFoundError


class BankTest(TestCase):
    def test_bank_can_create_account(self):
        bank = Bank()
        bank.create_account("James", "Divine", "Pin")
        self.assertEqual(1, bank.get_number_of_customers())

    def test_bank_can_create_more_than_one_account(self):
        bank = Bank()
        bank.create_account("James", "Divine", "Pin")
        bank.create_account("Esther", "Junior", "Pin2")
        bank.create_account("Rhoda", "John", "Pin3")

        self.assertEqual(3, bank.get_number_of_customers())

    def test_that_my_bank_can_find_account_number(self):
        bank = Bank()
        bank.create_account("David", "Adeleke", "Pin")
        find_account_number = bank.find_account_number("10321")
        self.assertEqual("10321", find_account_number.get_account_number())

    def test_that_my_bank_cannot_find_account_number(self):
        bank = Bank()
        bank.create_account("David", "Adeleke", "Pin")
        with self.assertRaises(AccountNumberNotFoundError):
            bank.find_account_number("10320")

    def test_that_my_bank_can_deposit_to_an_account(self):
        bank = Bank()
        bank.create_account("James", "Divine", "Pin")
        bank.create_account("Esther", "Junior", "Pin2")
        bank.create_account("Rhoda", "John", "Pin3")
        bank.create_account("James", "Divine", "Pin4")
        bank.create_account("Esther", "Junior", "Pin5")
        bank.create_account("Rhoda", "John", "Pin6")

        bank.deposit("10324", 2500)
        self.assertEqual(2500, bank.check_balance("10324", "Pin4"))

    def test_that_my_bank_can_withdraw_from_an_account(self):
        bank = Bank()
        bank.create_account("James", "Divine", "Pin4")
        bank.create_account("Esther", "Junior", "Pin5")

        bank.deposit("10322", 5000)
        bank.withdraw("10322", 5000, "Pin5")
        self.assertEqual(0, bank.check_balance("10322", "Pin5"))

    def test_that_my_bank_can_transfer_from_an_account_to_another_account(self):
        bank = Bank()
        bank.create_account("James", "Divine", "Pin4")
        bank.create_account("Esther", "Junior", "Pin5")

        bank.deposit("10322", 10_000)
        bank.transfer("10322", "10321", 5_000, "Pin5")
        self.assertEqual(5_000, bank.check_balance("10322", "Pin5"))
        self.assertEqual(5_000, bank.check_balance("10321", "Pin4"))

    def test_that_my_bank_can_remove_an_account(self):
        bank = Bank()
        bank.create_account("James", "Divine", "Pin")
        bank.create_account("Esther", "Junior", "Pin2")
        bank.create_account("Rhoda", "John", "Pin3")
        bank.create_account("James", "Divine", "Pin4")
        bank.create_account("Esther", "Junior", "Pin5")
        bank.create_account("Rhoda", "John", "Pin6")

        self.assertEqual(6, bank.get_number_of_customers())
        self.assertEqual("10323", bank.find_account_number("10323").get_account_number())

        bank.remove_account("10323", "Pin3")
        with self.assertRaises(AccountNumberNotFoundError):
            bank.find_account_number("10323")
        self.assertEqual(5, bank.get_number_of_customers())
