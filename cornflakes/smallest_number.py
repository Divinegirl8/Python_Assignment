list_score = []

for numbers in range(1, 11):
    score = int(input("Enter scores: "))
    list_score.append(score)

smallest = score
for column in list_score:

    if column < smallest:
        smallest = column
print("The smallest number is", smallest)
