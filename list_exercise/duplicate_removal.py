list_of_numbers = [15, 20, 25, 20, 10, 5]

maximum = 0
most_occuring_number = 0

for first_number in list_of_numbers:
    count = 0
    for second_number in list_of_numbers:
        if first_number == second_number:
            count += 1

    if count > maximum:
        maximum = count
        most_occuring_number = first_number
list_of_numbers.remove(most_occuring_number)
print(list_of_numbers)
