number = int(input("enter a number:"))

largest_number = number
smallest_number = number

count = 0

while number != 1:

    count += 1

    if number > largest_number:
        largest_number = number

    if number < smallest_number:
        smallest_number = number

    number = int(input("enter a number:"))

print(f"The largest number is {largest_number}\nThe smallest number is {smallest_number}")