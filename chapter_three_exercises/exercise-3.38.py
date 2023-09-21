numbers = [9, 11, 22, 34, 17, 22, 34, 22 ,40,34]
length_of_list = len(numbers)

for row in range(length_of_list):
    for column in range(row, length_of_list - 1):
        if numbers[row] > numbers[column + 1]:
            numbers[row], numbers[column + 1] = numbers[column + 1], numbers[row]

length = len(numbers)

# median

list_number = numbers

if length % 2 == 0:
    middle_number = list_number[len(list_number) // 2]
    middle_number2 = list_number[len(list_number) // 2 - 1]
    answer = (middle_number + middle_number2) / 2

middle_number2 = list_number[len(list_number) // 2]
answer = middle_number2

# mean
result = 0
for score in numbers:
    result += score

print(f"sorted numbers = {numbers}\nThe mean of the numbers is {result / length:.1f}\nThe median number is {answer}")

# mode
