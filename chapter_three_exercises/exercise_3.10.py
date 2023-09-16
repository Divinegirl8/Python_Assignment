from decimal import Decimal


principal = Decimal(1000)
rate  = Decimal(0.07)

for years in range (1,31):
    amount = principal * (1 + rate) ** years
    print(f'Amount in {years} years is ${amount:.1f}')

# years = 0
#
# while years < 30:
#    years +=1
#    amount = principal * (1 + rate) ** years
#    print(f'Amount in {years} years is {amount:.1f}')