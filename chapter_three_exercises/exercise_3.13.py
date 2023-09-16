number = int(input("Enter a number to find it factorial: "))

count = 0
total = 1

while count < number:
    count += 1
    total *= count
print(total)