import re
from chapter_four.student_oop_trial.difficult_level import multiplication_level
from chapter_four.student_oop_trial.difficult_level import addition_level
from chapter_four.student_oop_trial.difficult_level import subtraction_level
from chapter_four.student_oop_trial.difficult_level import division_level
from chapter_four.student_oop_trial.random_operators.different_operators import arithmetic_operators
users = input("""press 1 -> addition
press 2 -> subtraction
press 3 -> multiplication
press 4 -> division
press 5 -> for all 4 arithmetic operations
""")

list_of_numbers = ["1", "2", "3", "4", "5"]

while (not re.match(r'[0-9]', users)) or (users not in list_of_numbers):
    print("incorrect value, enter either 1 or 2")
    users = input("Enter Again")

if users == "1":
    addition_level()

elif users == "2":
    subtraction_level()

elif users == "3":
    multiplication_level()

elif users == "4":
    division_level()

elif users == "5":
    arithmetic_operators()

