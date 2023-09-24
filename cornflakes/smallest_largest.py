user = int(input("Enter number: "))

smallest = user
largest = user

for number in range(1,10):
    user = int(input("Enter number: "))

    if user > largest:
        largest = user

    if user < smallest:
        smallest = user


print(f"The smallest number is {smallest} and the largest is {largest}")


