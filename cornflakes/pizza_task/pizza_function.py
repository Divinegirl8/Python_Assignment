import sys

number_of_super_hungry_slices = 4
number_of_hungry_slices = 2
number_of_classic_slices = 1

large_slice = 10
medium_slice = 6
small_slice = 4

large_price = 5000
medium_price = 3000
small_price = 1200

max_value = sys.maxsize


def pizza_box_size(value: str):
    return value


def number_of_hungry_size(number: int):
    return number


def number_of_super_hungry_size(number: int):
    return number


def number_of_classic_size(number: int):
    return number


def super_hungry_size(number: int):
    return number_of_super_hungry_slices * number_of_super_hungry_size(number)


def hungry_size(number: int):
    return number_of_hungry_slices * number_of_hungry_size(number)


def classic_size(number: int):
    return number_of_classic_slices * number_of_classic_size(number)


def total_customer_size(super_hungry: int, hungry: int, classic: int):
    return super_hungry_size(super_hungry) + hungry_size(hungry) + classic_size(classic)


def large_size_index(total: int, large: int):
    result = 0

    if 1 <= total <= large:
        result = 1

    else:
        for index in range(0, max_value):
            if index * large > total:
                result = index
                break

    return result


def medium_size_index(total: int, medium: int):
    result = 0

    if 1 <= total <= medium:
        result = 1

    else:
        for index in range(0, max_value):
            if index * medium > total:
                result = index
                break

    return result


def small_size_index(total: int, small: int):
    result = 0

    if 1 <= total <= small:
        result = 1

    else:
        for index in range(0, max_value):
            if index * small > total:
                result = index
                break

    return result


def calculate_large_total_size(total: int):
    return total * large_slice


def calculate_medium_total_size(total: int):
    return total * medium_slice


def calculate_small_total_size(total: int):
    return total * small_slice


def calculate_large_remaining_size(total: int, large_total: int):
    if total < large_total:
        result = large_total - total

    else:
        result = total - large_total

    return result


def calculate_medium_remaining_size(total: int, medium_total: int):
    if total < medium_total:
        result = medium_total - total

    else:
        result = total - medium_total

    return result


def calculate_small_remaining_size(total: int, small_total: int):
    if total < small_total:
        result = small_total - total

    else:
        result = total - small_total

    return result


def calculate_large_size_price(large_index: int):
    return large_index * large_price


def calculate_medium_size_price(medium_index: int):
    return medium_index * medium_price


def calculate_small_size_price(small_index: int):
    return small_index * small_price


def display_large(total_slices_number: int, box_number: int, left_slices: int, cost: int):
    return f"""
     Number of Slices: {total_slices_number}
     Number of Boxes: {box_number}
     Number of Slices left: {left_slices}
     Total cost to spend: {cost}
    """


def display_medium(total_slices_number: int, box_number: int, left_slices: int, cost: int):
    return f"""
     Number of Slices: {total_slices_number}
     Number of Boxes: {box_number}
     Number of Slices left: {left_slices}
     Total cost to spend: {cost}
    """


def display_small(total_slices_number: int, box_number: int, left_slices: int, cost: int):
    return f"""
     Number of Slices: {total_slices_number}
     Number of Boxes: {box_number}
     Number of Slices left: {left_slices}
     Total cost to spend: {cost}
    """
