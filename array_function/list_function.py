def largest_number(number):
    largest = 0
    for integer in number:
        if integer > largest:
            largest = integer
    return largest


def reverse_list(number):
    return number[::-1]


def odd_number(number):
    return number[1::2]


def even_number(number):
    return number[::2]


def check_element(numbers: int, integer: int) -> bool:
    for items in numbers:
        if items == integer:
            return True
    return False


def string_palindrome(user_input):
    return user_input == user_input[::-1]


def summation_for_loop(user_input):
    total = 0
    for row in user_input:
        total += row

    return f"{total:.1f}"


def summation_while_loop(user_input):
    total = 0
    row = 0
    while row < len(user_input):
        total += user_input[row]
        row += 1

    return f"{total:.1f}"


def running_total(user_input):
    total = 0
    count = 0
    string_convert = " "

    while count < len(user_input):
        total += user_input[count]
        count += 1
        string_format = f"{total}"
        string_convert += string_format + " "
    return string_convert


def two_list(letter: str, integer: int):
    result = ""
    for row in range(len(letter)):
        result += f"{letter[row]}," + f"{integer[row]}"
        if row < len(letter) - 1:
            result += ","

    return "[" + result + "]"


def seperated_list(letter, integer):
    result1 = ""
    result2 = ""
    for row in range(len(letter)):
        result1 += letter[row] + ","
    for column in range(len(integer)):
        result2 += f"{integer[column]}"
        if column < len(integer) - 1:
            result2 += ","

    return "[" + result1 + result2 + "]"


def list_digits(number):
    cast_number = str(number)
    list_basket = []

    for integer in cast_number:
        list_basket.append(int(integer))
    return list_basket




