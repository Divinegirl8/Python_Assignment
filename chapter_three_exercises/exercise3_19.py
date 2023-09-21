result = 1
for side1 in range(1, 21):
    side1 **= 2
    print(side1)
    for side2 in range(side1):
        side2 **= 2
        for hypotenuse in range(side2):
            hypotenuse **= 2
        print(side1 + side2 == hypotenuse)

#         still working on it
