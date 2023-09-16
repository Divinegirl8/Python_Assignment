first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

largest_number = 0
smallest_number = 0
middle_number = 0

if second_number < first_number > third_number:
    largest_number = first_number
if second_number > first_number < third_number:
    smallest_number = first_number
else:
    middle_number = first_number

if first_number < second_number > third_number:
    largest_number = second_number
if first_number > second_number < third_number:
    smallest_number = second_number
else:
    middle_number = second_number

if second_number < third_number > first_number:
    largest_number = third_number
if second_number > third_number < first_number:
    smallest_number = third_number
else:
    middle_number = third_number

print(smallest_number, middle_number, largest_number)