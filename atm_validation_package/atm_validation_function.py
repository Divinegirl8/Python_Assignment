def separate_digit(number: str):
    if "1" <= number <= "9":
        cast = int(number)
        new_list = []

        loop_count = 0

        while loop_count < len(number):
            result = cast // 10 ** loop_count % 10
            loop_count += 1
            new_list.append(result)
        return new_list
    else:
        return f"Invalid Input, It should contain numbers from 1 - 9"


def even_atm_position(number):
    single_digit = 0
    double_digit = 0

    # even position

    for num in range(1, len(number), 2):
        store = int(number[num])
        product = store * 2

        if 10 <= product <= 99:
            two_digit = product

            loop = 0
            while loop < 2:
                out = two_digit // 10 ** loop % 10
                loop += 1
                double_digit += out


        else:
            single_digit += product

    sum_both = single_digit + double_digit
    return sum_both


def odd_atm_position(number):
    odd_sum = 0
    for digit in range(0, len(number), 2):
        cast_number = int(number[digit])
        odd_sum += cast_number
    return odd_sum


def calculate_both_odd_even(number):
    return even_atm_position(number) + odd_atm_position(number)


def check_validity(number):
    remove = ""
    for digit in range(len(number) - 1, -1, -1):
        store = f"{number[digit]}"
        remove += store

    total = calculate_both_odd_even(number)
    last_index = len(number) - 1
    second_to_the_last_index = len(number) - 2
    get_index = number[last_index]
    get_index_two = number[second_to_the_last_index]

    if get_index == 5 and 13 <= len(number) <= 16 and total % 10 == 0:
        card_type = "MasterCard"
        validity_status = "Valid"
    elif get_index == 5 and total % 10 != 0:
        card_type = "MasterCard"
        validity_status = "Invalid"

    if get_index == 6 and 13 <= len(number) <= 16 and total % 10 == 0:
        card_type = "Discover Card"
        validity_status = "Valid"
    elif get_index == 6 and total % 10 != 0:
        card_type = "Discover Card"
        validity_status = "Invalid"

    if get_index == 4 and 13 <= len(number) <= 16 and total % 10 == 0:
        card_type = "Visa Card"
        validity_status = "Valid"
    elif get_index == 4 and total % 10 != 0:
        card_type = "Visa Card"
        validity_status = "Invalid"

    if get_index == 3 and 13 <= len(number) <= 16 and get_index_two == 7 and total % 10 == 0:
        card_type = "America Express Card"
        validity_status = "Valid"
    elif get_index == 3 and get_index_two == 7 and total % 10 != 0:
        card_type = "America Express Card"
        validity_status = "Invalid"

    if get_index < 3 or get_index > 6:
        card_type = "Invalid Card"
        validity_status = "Invalid"
    return f"""
*****************************************
**Credit Card Type: {card_type}
**Credit Card Number: {remove}
**Credit Card Digit Length: {len(number)}
**Credit Card Validity Status: {validity_status}
********************************************
"""


#


# 4388576018402626

user = input("Enter a number: ")

while user != user.isnumeric():
    user = input("Enter a number: ")

if user == user.isnumeric():
    print("ok")
