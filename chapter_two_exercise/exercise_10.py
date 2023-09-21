number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))

largest = number_one
smallest = number_one

sum_of_numbers = number_one + number_two + number_three
average_of_numbers = sum_of_numbers / 3
product_of_numbers = number_one * number_two * number_three

if number_two > largest:
    largest = number_two

if number_three > largest:
    largest = number_three

if number_two < smallest:
    smallest = number_two

if number_three < smallest:
    smallest = number_three

print(f"""
The sum of the numbers is {sum_of_numbers}
The average of the numbers is {average_of_numbers}
The product of the numbers is {product_of_numbers}
The largest number is {largest}
The smallest number is  {smallest}
""")
