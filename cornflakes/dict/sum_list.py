# def sum_list(numbers):
#     total = 0
#     for row in numbers:
#         for num in row:
#             total += num
#     return total


# def sum_list(numbers):
#     total = 0
#     for number in numbers:
#         total += sum(number)
#     return total


def sum_list(numbers):
    first, second = numbers
    return sum(first + second)


number_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(number_list))
