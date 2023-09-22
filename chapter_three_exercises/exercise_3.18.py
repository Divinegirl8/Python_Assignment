for outer in range(1, 13):
    # first
    for column in range(outer):
        print("*", end=" ")

    for column2 in range(outer, 13 - 1):
        print(" ", end=" ")

    for space in range(3):
       print(" ",end=" ")

    # second

    for column2 in range(outer, 13 - 1):
        print("*", end=" ")

    for column in range(outer):
        print(" ", end=" ")

    for space in range(3):
        print(" ", end=" ")

    # third
    for column in range(outer):
        print(" ", end=" ")

    for column2 in range(outer, 13 - 1):
        print("*", end=" ")

    for space in range(3):
        print(" ", end=" ")

    # fourth

    for column in range(outer, 13 - 1):
        print(" ", end=" ")
    for column2 in range(outer):
        print("*", end=" ")

    print()
