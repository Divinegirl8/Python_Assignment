

list_of_numbers = [15, 20, 25, 20, 10, 5]
new_list = []

for number in list_of_numbers:
    if number not in new_list:
        new_list.append(number)

print(new_list)
