# def biggest_odd(letters):
#     biggest_number = 0
#     for letter in letters:
#         number = int(letter)
#         if number % 2 != 0:
#             if number > biggest_number:
#                 biggest_number = number
#     return biggest_number


def biggest_odd(letters):
    return max([num for num in letters if int(num) % 2 != 0])



