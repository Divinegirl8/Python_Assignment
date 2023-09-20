money = int(input("Enter amount (1 dollar = 100 cents): "))

dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

dollar_change = money // quarter
dollar_change2 = (money % quarter) // dime
dollar4 = ((money % quarter) % dime) // nickel
dollar_change3 = ((money % quarter) % nickel) // penny

print(f"The smallest coins for {money} is {dollar_change} quarters , {dollar_change2} dimes , {dollar4} nickels and {dollar_change3} pennies")
