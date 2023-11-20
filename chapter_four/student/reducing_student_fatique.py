import random
import re


def generate_random_single_digit():
    return random.randint(0, 9)


def generate_computer_response_for_correct_response():
    generate = random.randint(1, 3)
    result = ""

    match generate:
        case 1:
            result = 'Very good!'
        case 2:
            result = 'Nice work!'
        case 3:
            result = 'Keep up the good work!'
    return result


def generate_computer_response_for_incorrect_response():
    generate = random.randint(1, 3)
    result = ""

    match generate:
        case 1:
            result = 'No. Please try again.'
        case 2:
            result = 'Wrong. Try once more.'
        case 3:
            result = 'No. Keep trying.'
    return result


option = True

while option:
    number1 = generate_random_single_digit()
    number2 = generate_random_single_digit()

    user_input = input(f"How much is {number1} * {number2}")

    while not re.match(r'[0-9]', user_input):
        print("Invalid input. Please enter a valid number.")
        user_input = input(f"How much is {number1} * {number2}")

    while int(user_input) != number1 * number2:
        print(generate_computer_response_for_incorrect_response())

        try:
            user_input = int(input(f"How much is {number1} * {number2}"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    if int(user_input) == number1 * number2:
        print(generate_computer_response_for_correct_response())

    user_response = input("Do you want to continue? ").lower()

    while (not re.match(r'[0-9]', user_response)) and "yes" != user_response != "no":
        print("Error")
        user_response = input("Do you want to continue? ").lower()

    if user_response == "no":
        option = False
