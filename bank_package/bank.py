from decimal import Decimal, getcontext
from bank_package.account import Account
from exceptions.account_number_not_found_error import AccountNumberNotFoundError


class Bank:

    def __init__(self):
        self.accounts = []
        getcontext().prec = 2
        self.count_number_of_customers = 1

    def create_account(self, first_name, last_name, pin):
        generate_customer_name = Bank.create_name(self, first_name, last_name)
        generate_account_number = Bank.account_number(self)
        account = Account(generate_customer_name, pin, generate_account_number)
        self.accounts.append(account)

        self.count_number_of_customers += 1
        return account

    def create_name(self, first_name, last_name):
        return first_name + " " + last_name

    def account_number(self):
        return f"1032{self.count_number_of_customers}"

    def get_number_of_customers(self):
        return len(self.accounts)

    def find_account_number(self, account_number):
        for value in self.accounts:
            if value.get_account_number() == account_number:
                return value
        raise AccountNumberNotFoundError(f"{account_number} not found")

    def deposit(self, account_number, amount):
        account_number = self.find_account_number(account_number)
        account_number.deposit(amount)

    def check_balance(self, account_number, pin):
        account_number = self.find_account_number(account_number)
        return account_number.check_balance(pin)

    def withdraw(self, account_number, amount, pin):
        account_number = self.find_account_number(account_number)
        account_number.withdraw(amount, pin)

    def transfer(self, sender_acct_number, receiver_acct_number, amount, pin):
        sender_acct = self.find_account_number(sender_acct_number)
        receiver_acct = self.find_account_number(receiver_acct_number)

        sender_acct.withdraw(amount, pin)
        receiver_acct.deposit(amount)

    def remove_account(self, account_number, pin):
        account_number = self.find_account_number(account_number)
        Account.validate_pin(account_number, pin)
        self.accounts.remove(account_number)
