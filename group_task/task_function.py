def add_to_list(first, second):
    return [number for number in range(first, second)]


def odd_numbers(numbers):
    return [items for items in numbers if items % 2 != 0]


def double_item(numbers):
    for value in range(len(numbers)):
        numbers[value] **= 2
    return numbers


def change_index(numbers):
    for index, value in enumerate(numbers):
        if 4 >= index <= 7:
            value[index] = 0
        return value


print(change_index(double_item(odd_numbers(add_to_list(1, 21)))))
