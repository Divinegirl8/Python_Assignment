first = input("Enter first name: ")
last = input("Enter last name: ")
concatenate = first + last

for user in range(len(concatenate) - 1, -1, -1):
    print(concatenate[user], end=" ")
