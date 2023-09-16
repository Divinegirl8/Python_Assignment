price = int(input("Price of goods: "))
credit_score = input("Credit score(enter true for good credit score and false for bad credit score): ")
name = input("Name of the item: ")
print()


credit_score = credit_score == "true" or credit_score == "True"

if credit_score:
    discount = 10 * price / 100
    down_payment = 10 * price / 100
    print("************************\n\tInvoice\n*************************")

    print(f" Name of items: {name}\n Discount : {discount}%\n Deposit : ${down_payment}")

    print('************************')

else :
    down_payment2 = 25 * price / 100

    print("************************\n\tInvoice\n*************************")

    print(f" Name of items: {name}\n Discount : no discount\n Deposit : ${down_payment2}")

    print('************************')