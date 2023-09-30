list_score = []


for numbers in range(1, 11):
    score = int(input("Enter scores: "))
    list_score.append(score)

largest = 0
smallest = score
total = 0
for column in list_score:
    total += column

    if column < smallest:
        smallest = column

    if column > largest:
        largest = column
print(f"""
The minimum number is {smallest}
The maximum number is {largest}
The total of the number is {total}
The average of the number is {total/numbers}
""")
