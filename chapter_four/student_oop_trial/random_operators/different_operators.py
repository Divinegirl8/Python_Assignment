import random
from chapter_four.student_oop_trial.multiplication.student_single_digit_app import main_app
from chapter_four.student_oop_trial.multiplication.student_more_than_one_digit import app
from chapter_four.student_oop_trial.addition.one_digit import addition_main
from chapter_four.student_oop_trial.addition.more_than_one_digit import addition_app
from chapter_four.student_oop_trial.subraction.one_digit_integer import subtraction_one_digit
from chapter_four.student_oop_trial.subraction.two_digit import subtraction_two_digit
from chapter_four.student_oop_trial.division.double_integers import divide_two_digit
from chapter_four.student_oop_trial.division.single_integers import divide_one_digit


def generate_numbers():
    return random.randint(1, 8)


def arithmetic_operators():
    match generate_numbers():
        case 1:
            return main_app()
        case 2:
            return addition_app()
        case 3:
            return app()
        case 4:
            return subtraction_one_digit()
        case 5:
            return addition_main()
        case 6:
            return divide_two_digit()
        case 7:
            return subtraction_two_digit()
        case 8:
            return divide_one_digit()
