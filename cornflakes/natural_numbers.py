user = int(input("Enter a number: "))

count = 0
sum = 0
total = 0

while user != 2:

    if user > 0:
        count += 1
        total += 1
        sum += user

    user = int(input("Enter a number: "))

    if total == 10: break
print(sum)
