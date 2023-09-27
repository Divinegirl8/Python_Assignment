principal = 1000
pennies = principal * 100
rate = 5 / 100
compounding_frequently = 4

for years in range(1, 11):
    result = pennies * (1 + rate / compounding_frequently) ** (compounding_frequently * years)
    dollar = result // 100
    cents = result % 100

amount = f"The compounded interest is ${dollar:.0f}.{cents:.0f} cents"
print(amount)


