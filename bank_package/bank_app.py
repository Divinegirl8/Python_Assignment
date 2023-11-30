from bank_package.bank import Bank
from bank_package.account import Account
from decimal import Decimal
from exceptions.deposit_amount_less_than_0_error import DepositAmountLessThanZeroError
import sys

my_bank = Bank()


def create_account():
    while True:
        user_first_name = input("First Name: ")

        if not user_first_name.isalpha():
            print("First Name should consist of letters only")
        else:
            break
    while True:
        user_last_name = input("Last Name: ")

        if not user_last_name.isalpha():
            print("Last Name should consist of letters only")
        else:
            break

    while True:
        password = input("Create Password: ")

        if not password.isdigit() or len(password) != 4:
            print("password must consist of numbers and 4 number of characters")
        else:
            break

    account = my_bank.create_account(user_first_name, user_last_name, password)
    print(f"""account created successfully
    {account}
    """)
    bank_menu()


def deposit():
    acct_number = input("Enter your account number: ")

    while True:
        amount_str = input("Enter Amount: ")

        if not amount_str.isdigit():
            print("Amount must contain positive numbers only.")
        else:
            amount = Decimal(amount_str)
            break
    try:
        my_bank.deposit(acct_number, amount)
        print(f"you have deposited {amount} successfully")
        bank_menu()

    except Exception as exception:
        print(exception)
        bank_menu()


def withdraw():
    acct_number = input("Enter your account number: ")
    while True:
        amount_str = input("Enter Amount: ")

        if not amount_str.isdigit():
            print("Amount must contain positive numbers only.")
        else:
            amount = Decimal(amount_str)
            break

    pin = input("Enter pin: ")

    try:
        my_bank.withdraw(acct_number, amount, pin)
        print(f"""
Withdraw Successful
Account Balance: {my_bank.check_balance(acct_number, pin):.0f}
        """)
        bank_menu()
    except Exception as exception:
        print(exception)
        bank_menu()


def check_balance():
    acct_number = input("Enter your account number: ")
    pin = input("Enter your pin: ")

    try:
        print(f"Account Balance: {my_bank.check_balance(acct_number, pin):.0f}")
        bank_menu()
    except Exception as exception:
        print(exception)
        bank_menu()


def transfer():
    sender_account_number = input("Enter Sender Account Number: ")
    receiver_account_number = input("Enter Receiver Account Number: ")

    while True:
        amount_str = input("Enter amount to transfer: ")
        if not amount_str.isdigit():
            print("Amount must contain positive numbers only.")

        else:
            amount = Decimal(amount_str)
            break
    account_pin = input("Enter account pin")

    try:
        my_bank.transfer(sender_account_number, receiver_account_number, amount, account_pin)
        print(f"transfer successful\nAccount Balance {my_bank.check_balance(sender_account_number, account_pin):.0f}")
        bank_menu()
    except Exception as exception:
        print(exception)
        bank_menu()


def bank_menu():
    user_response = input("""
======================================
          Oceanic Bank   
======================================
press 1 -> Create Account
press 2 -> Deposit
press 3 -> Withdraw
press 4 -> Check Balance
press 5 -> Transfer
press 6 -> Exit 
=======================================
    """)
    match user_response:
        case "1":
            create_account()
        case "2":
            deposit()
        case "3":
            withdraw()
        case "4":
            check_balance()
        case "5":
            transfer()
        case "6":
            sys.exit(0)


class BankApp:
    bank_menu()
