Response = True

while Response:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    print(f'{number1} + {number2} = {number1 + number2}')

    user = input("Do you want to continue: ")

    isResponseNo = user.lower() == "no"
    if isResponseNo:
        Response = False
