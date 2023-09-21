price = int(input("Price of goods: "))
credit_score = input("Credit score(enter true for good credit score and false for bad credit score): ")
name = input("Name of the item: ")
print()


credit_score = credit_score == "true" or credit_score == "True"

if credit_score:
    discount = 10 * price / 100
    down_payment = 10 * price / 100
    print(f"************************\n\tInvoice\n*************************\nName of items: {name}\nDiscount : {discount}%\nDeposit : ${down_payment}\n************************")


else :
    down_payment2 = 25 * price / 100

    print(f"************************\n\tInvoice\n*************************\nName of items: {name}\nDiscount : no discount\nDeposit : ${down_payment2}\n************************")
