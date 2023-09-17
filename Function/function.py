def commission(rate):
    if rate < 50:
        return rate * 160 + 5000
    elif rate <= 59:
        return rate * 200 + 5000
    elif rate <= 69:
        return rate * 250 + 5000
    else:
        return rate * 500 + 5000


def copies(copy):
    if 0 < copy <= 4:
        return 2000
    elif copy <= 9:
        return 1800
    elif copy <= 29:
        return 1600
    elif copy <= 49:
        return 1500
    elif copy <= 99:
        return 1300
    elif copy <= 199:
        return 1200
    elif copy <= 499:
        return 1100
    else:
        return 1000


def is_even(integer):
    if integer % 2 == 0:
        return True

    return False


def is_prime(integer):
    length_of_numbers = 0
    count = 0

    while count <= integer:
        count += 1
        if integer % count == 0:
            length_of_numbers += 1

    if length_of_numbers == 2:
        return True

    return False


def subtract(first_number, second_number):
    if first_number < second_number:
        return second_number - first_number

    return first_number - second_number


def divide(first_number, second_number):
    if second_number != 0:
        result = first_number / second_number
        approximate = round(result * 100.0) / 100.0
        return approximate

    return 0


def factor_of(number):
    count = 0
    length = 0

    while count <= number:
        count += 1
        if number % count == 0:
            length += 1
    return length


def is_square(number):
    count = 0
    while count < number:
        count += 1
        if count * count == number:
            return True

    return False


def palindrome(number):
    result = number // 10000 % 10
    result2 = number % 10

    if result == result2:
        return True

    return False


def factorial(number):
    count = 1
    result = 1

    while count < number:
        count += 1
        result *= count
    return result
