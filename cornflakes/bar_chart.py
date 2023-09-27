list = []
count = 0
while count < 5:
    display = int(input("Enter a number(number between 1 - 30): "))
    if display < 30:
        count += 1
        list.append(display)
    else:
        print("Error,number must not exceed 30")


for rows in list:
    print()
    for column in range(rows):
        print("*",end=" ")