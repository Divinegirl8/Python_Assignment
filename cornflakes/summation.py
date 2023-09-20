Response = True

while Response:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    print(f'{number1} + {number2} = {number1 + number2}')

    user = input("Do you want to continue: ")

<<<<<<< HEAD
    # refactor the if condition below, it can be shorter
    if user == "no" or user == "No" or user == "NO":
=======
    isResponseNo = user.lower() == "no"
    if isResponseNo:
>>>>>>> be97ece (update)
        Response = False
