
import random
import re


def remove_non_digit_number(value):
    return re.sub('[^0-9]', '', value)


def generate_number(element):
    result = ""

    for values in element:
        if "2" in values:
            random_upper_letter = chr(random.randint(ord('A'), ord('C')))
            result += random_upper_letter
        if "3" in values:
            random_upper_letter = chr(random.randint(ord('D'), ord('F')))
            result += random_upper_letter
        if "4" in values:
            random_upper_letter = chr(random.randint(ord('G'), ord('I')))
            result += random_upper_letter
        if "5" in values:
            random_upper_letter = chr(random.randint(ord('J'), ord('L')))
            result += random_upper_letter
        if "6" in values:
            random_upper_letter = chr(random.randint(ord('M'), ord('O')))
            result += random_upper_letter
        if "7" in values:
            random_upper_letter = chr(random.randint(ord('P'), ord('S')))
            result += random_upper_letter
        if "8" in values:
            random_upper_letter = chr(random.randint(ord('T'), ord('V')))
            result += random_upper_letter
        if "9" in values:
            random_upper_letter = chr(random.randint(ord('W'), ord('Y')))
            result += random_upper_letter
        if not number.isdigit() or len(number) != 7 or "1" in number or "0" in number:
            result = "Invalid phone number. Please enter a valid seven-digit number."

    return result


number = input("""Enter a number that consist of digit only and 
consist of numbers greater than and equals to 2 or less than and equals to 9 
and must consist of 7 characters
""")


print(generate_number(number))
