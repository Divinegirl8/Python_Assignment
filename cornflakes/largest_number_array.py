list = []
largest = 0

for numbers in range(1, 11):
    score = int(input("Enter scores: "))
    list.append(score)

for column in list:
    if column > largest:
        largest = column
print("The largest number is", largest)
