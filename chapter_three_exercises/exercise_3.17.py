for index_a in range(1, 13):
    for index_a2 in range(index_a):
        print("*", end=" ")
    print()

print()

for row in range(13, -1, -1):
    print(" ")
    for column in range(row):
        print("*", end=" ")
    print()

for row in range(1, 13):

    for column in range(row, 13 - 1):
        print(" ", end=" ")
    for column2 in range(row):
        print("*", end=" ")
    print()

print()

for row in range(1, 13):
    print(" ")
    for column in range(row):
        print(" ", end=" ")

    for column2 in range(row,13 - 1):
        print("*", end=" ")

    print()

