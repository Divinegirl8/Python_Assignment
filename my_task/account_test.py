from my_task import account
from my_task.account import Account

bank = Account("Ade sua")

user = int(input("deposit an amount: "))

bank.deposit(user)

print(f"Account Name: {bank.get_name()}\nDeposit amount: {bank.get_balance()}\nNew Balance: {bank.get_balance()}")

print()

user2 = int(input("deposit an amount: "))

bank.deposit(user2)

print(f"Account Name: {bank.get_name()}\nNew Balance: {bank.get_balance()}")


print()

user3 = int(input("Enter a withdraw amount: "))

bank.withdraw(user3)

print(bank.get_balance())
