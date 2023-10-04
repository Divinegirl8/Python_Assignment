list_of_numbers = [15, 20, 25, 20, 10, 5]

largest = 0
count = 0

while count < len(list_of_numbers):
    if list_of_numbers[count] > largest:
        largest = list_of_numbers[count]
    count += 1
print("The largest number in the list is", largest)
