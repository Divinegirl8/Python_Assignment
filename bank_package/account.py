from decimal import Decimal, getcontext
from exceptions.deposit_amount_less_than_0_error import DepositAmountLessThanZeroError
from exceptions.validate_pin_error import PinError
from exceptions.withdrawal_amount_greater_than_balance_error import AmountGreaterThanBalanceError


class Account:
    def __init__(self, name, pin, account_number):
        self.__name = name
        self.__pin = pin
        self.__account_number = account_number
        self.__balance = Decimal('0.00').quantize(Decimal('0.01'))
        getcontext().prec = 2

    def deposit(self, amount):
        if amount > 0:
            amount_decimal = Decimal(str(amount))
            self.__balance += amount_decimal
        else:
            raise DepositAmountLessThanZeroError("Amount should be greater than 0")

    def check_balance(self, pin):
        Account.validate_pin(self, pin)
        return self.__balance

    def validate_pin(self, pin):
        if self.__pin != pin:
            raise PinError("Invalid pin")
        return self.__pin == pin

    def get_account_number(self):
        return self.__account_number

    def withdraw(self, amount, pin):
        Account.validate_pin(self, pin)
        if amount <= self.__balance:
            amount_decimal = Decimal(str(amount))
            self.__balance -= amount_decimal
        else:
            raise AmountGreaterThanBalanceError("Amount is greater than your account balance")

    def __str__(self):
        return f"""
==========================================
Account Name: {self.__name}        
Account Number : {self.__account_number}
Pin : Unavailable
Account Balance: {self.__balance}    
==========================================   
        """
