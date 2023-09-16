largest = 0
second_largest = 0
count = 0

while count < 10:
    count += 1
    number = int(input("Enter number: "))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number
print(f"Largest number is {largest}\nSecond Largest is {second_largest}")