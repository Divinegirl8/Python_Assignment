import random
from chapter_four.student_oop_trial.generator_correct_answer import Generator
from chapter_four.student_oop_trial.generate_wrong_answer import Generator2
import re


def generate_single_digit_number():
    return random.randint(1, 9)


def generate_number_for_correct_or_incorrect_response():
    return random.randint(1, 3)


def generate_correct_answer_message():
    generator = Generator()
    response = generator.generate_response(generate_number_for_correct_or_incorrect_response())
    return response


def generate_incorrect_answer_message():
    generator = Generator2()
    response = generator.generate_response(generate_number_for_correct_or_incorrect_response())
    return response


def divide_one_digit():
    option = True

    while option:
        number1 = generate_single_digit_number()
        number2 = generate_single_digit_number()

        user_input = input(f"How much is {number1} / {number2}")

        user_input = wrong_input_validation(number1, number2, user_input)

        user_input = wrong_answer_validation(number1, number2, user_input)

        correct_answer_validation(number1, number2, user_input)

        user_response = input("Do you want to continue? ").lower()

        option = continuation_question(option, user_response)


def wrong_input_validation(number1, number2, user_input):
    while not re.match(r'^[+-]?\d+(\.\d+)?$', user_input):
        print("Invalid input. Please enter a valid number.")
        user_input = input(f"How much is {number1} / {number2}")
    return user_input


def wrong_answer_validation(number1, number2, user_input):
    while float(user_input) != number1 / number2:
        print(generate_incorrect_answer_message())

        try:
            user_input = float(input(f"How much is {number1} / {number2}"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    return user_input


def correct_answer_validation(number1, number2, user_input):
    if float(user_input) == number1 / number2:
        print(generate_correct_answer_message())


def continuation_question(option, user_response):
    while (not re.match(r'[0-9]', user_response)) and "yes" != user_response != "no":
        print("Error")
        user_response = input("Do you want to continue? ").lower()
    if user_response == "no":
        option = False
    return option
