import re
from chapter_four.student_oop_trial.multiplication.student_single_digit_app import main_app
from chapter_four.student_oop_trial.multiplication.student_more_than_one_digit import app
from chapter_four.student_oop_trial.addition.one_digit import addition_main
from chapter_four.student_oop_trial.addition.more_than_one_digit import addition_app
from chapter_four.student_oop_trial.subraction.one_digit_integer import subtraction_one_digit
from chapter_four.student_oop_trial.subraction.two_digit import subtraction_two_digit
from chapter_four.student_oop_trial.division.double_integers import divide_two_digit
from chapter_four.student_oop_trial.division.single_integers import divide_one_digit


def multiplication_level():
    user = input("""press 1 -> easy level
press 2 -> hard level
    """)

    while (not re.match(r'[0-9]', user)) or ("1" != user != "2"):
        print("incorrect value, enter either 1 or 2")
        user = input("Enter Again")

    if user == "1":
        print("You chose level 1")
        main_app()

    elif user == "2":
        print("You chose level 2")
        app()


def addition_level():
    user = input("""press 1 -> easy level
press 2 -> hard level
    """)

    while (not re.match(r'[0-9]', user)) or ("1" != user != "2"):
        print("incorrect value, enter either 1 or 2")
        user = input("Enter Again")

    if user == "1":
        print("You chose level 1")
        addition_main()

    elif user == "2":
        print("You chose level 2")
        addition_app()


def subtraction_level():
    user = input("""press 1 -> easy level
press 2 -> hard level
    """)

    while (not re.match(r'[0-9]', user)) or ("1" != user != "2"):
        print("incorrect value, enter either 1 or 2")
        user = input("Enter Again")

    if user == "1":
        print("You chose level 1")
        subtraction_one_digit()

    elif user == "2":
        print("You chose level 2")
        subtraction_two_digit()

def division_level():
    user = input("""press 1 -> easy level
press 2 -> hard level
    """)

    while (not re.match(r'[0-9]', user)) or ("1" != user != "2"):
        print("incorrect value, enter either 1 or 2")
        user = input("Enter Again")

    if user == "1":
        print("You chose level 1")
        divide_one_digit()

    elif user == "2":
        print("You chose level 2")
        divide_two_digit()