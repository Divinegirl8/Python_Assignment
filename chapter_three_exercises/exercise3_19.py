
hypotenuse = 0
for side1 in range(1, 21):
    for side2 in range(1, 21):
        for hypotenuse in range(1, 21):
            if (side1 ** 2) + (side2 ** 2) == (hypotenuse ** 2):
                print(side1, "+", side2, "=", hypotenuse)
