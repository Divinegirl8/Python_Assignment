list_of_numbers = [15, 20, 25, 20, 10, 5]

smallest = list_of_numbers[0]

for number in list_of_numbers:
    if number < smallest:
        smallest = number

print("The smallest number is", smallest)
