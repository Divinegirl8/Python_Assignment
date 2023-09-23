for column in range(1, 5):
    for row in range(column):
        print("*", end=" ")
    print()

for column in range(5, -1, -1):
    for row in range(column):
        print("*", end=" ")
    print()
