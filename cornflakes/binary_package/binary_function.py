def binary_to_decimal(number):
    value = number * -1 if number < 0 else number

    count = 0
    exponential = 0
    sum_number = 0

    while count < len(str(value)):
        result = (value // 10 ** count) % 10
        count += 1
        output = result * 2 ** exponential
        exponential += 1
        sum_number += output
    return sum_number


def decimal_to_binary(number):
    value = number * -1 if number < 0 else number

    join_word = ""

    while value != 0:
        result = value % 2
        join_word += f"{result}"
        value = value // 2
    return int(join_word[::-1])


