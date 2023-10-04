list_of_numbers = [15, 20, 25, 20, 10, 5]

quotient = 1
count = 0
while count < len(list_of_numbers):
    quotient *= list_of_numbers[count]
    count += 1
print("The quotient of the list of numbers is", quotient)
