list_of_numbers = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

for row in list_of_numbers:
    for numbers in row:
        result = "0" if numbers == 1 else "X"
        print(result, end=" ")
    print()
