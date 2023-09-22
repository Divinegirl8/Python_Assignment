amount = int(input("Enter purchase amount: "))

dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1
purchase_price = 1500

while amount < purchase_price:
    print(f"The price of the item worth {purchase_price}")

    amount = int(input("Enter purchase amount: "))

if amount >= purchase_price:
    amount_deduction = amount - purchase_price
    money = amount_deduction//100

    dollar_change = money // quarter
    dollar_change2 = (money % quarter) // dime
    dollar4 = ((money % quarter) % dime) // nickel
    dollar_change3 = ((money % quarter) % nickel) // penny

print(
    f"The smallest coins for {money} is {dollar_change} quarters , {dollar_change2} dimes , {dollar4} nickels and {dollar_change3} pennies")





