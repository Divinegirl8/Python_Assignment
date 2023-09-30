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


def list_digits(numbers):
    listed_number = [numbers]
    return listed_number


def check_element(numbers: int, integer: int) -> bool:
    for items in numbers:
        if items == integer:
            return True
    return False


def string_palindrome(user_input):
    return user_input == user_input[::-1]


