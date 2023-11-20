import random
import re


def generate_random_single_digit_number():
    return random.randint(0, 9)


option = True

while option:
    number1 = generate_random_single_digit_number()
    number2 = generate_random_single_digit_number()

    user_input = input(f"How much is {number1} * {number2}")

    while not re.match(r'^[+-]?\d+(\.\d+)?$', user_input):
        print("Invalid input. Please enter a valid number.")
        user_input = input(f"How much is {number1} * {number2}")

    while int(user_input) != number1 * number2:
        print("No. Please try again.")

        try:
            user_input = int(input(f"How much is {number1} * {number2}"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    if int(user_input) == number1 * number2:
        print("Very good!")

    user_choice = input("Do you want to continue? ").lower()

    while (not re.match(r'[0-9]', user_choice)) and "yes" != user_choice != "no":
        print("Error")
        user_choice = input("Do you want to continue? ").lower()

    if user_choice == "no":
        option = False

