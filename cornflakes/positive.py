number = int(input("Enter a number (press 1 to stop):"))

count = 0
positive_number = 0
negative_number = 0
zero_number = 0

while number != 1:

    count += 1

    if number > 0:
        positive_number += 1

    if number < 0:
        negative_number += 1

    if number == 0:
        zero_number += 1

    number = int(input("Enter a number (press 1 to stop):"))

print(f"The positive number is {positive_number}\nThe negative number is {negative_number}\nThe zero number is {zero_number}")
