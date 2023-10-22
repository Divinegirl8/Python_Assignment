import random
import re

generate = random.randint(1, 1000)
pattern = r'[0-9]+'
option = True


while option:
    user_input = input("Guess my number between 1 - 1000")

    if not re.match(pattern, user_input):
        print("Invalid, Value must contain a number")
        continue

    convert_to_int = int(user_input)

    if convert_to_int != generate:
        print("Too Low, Try Again!!!")
        continue

    if convert_to_int == generate:
        print("Congratulations")

    user_choice = input("Do you want to continue? ").lower()

    while (not re.match(pattern, user_choice)) and "yes" != user_choice != "no":
        print("Error")
        user_choice = input("Do you want to continue? ").lower()

    if user_choice == "no":
        option = False

