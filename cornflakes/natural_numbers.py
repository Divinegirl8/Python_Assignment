user = 0
count = 0
sum_number = 0
total = 0

while user != -2:
    user = int(input("Enter a number: "))

    if user > 0:
        count += 1
        total += 1
        sum_number += user

    if total == 10:
        break
print(sum_number)
