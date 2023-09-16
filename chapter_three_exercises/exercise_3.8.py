user = int(input("Enter a number: "))
count = 0
product = 1
result = 0
largest = user
smallest = user


for number in range(4):
    count += 1
    user = int(input("Enter a number: "))
    result += user
    product *= user

    if user > largest:
        largest = user
    if user < smallest:
         smallest = user


print(f'The sum of the four numbers is {result}')
print(f'The average of the numbers is {result/count}')
print(f'The product of the numbers is {product}')
print(f'The largest number is {largest}')
print(f'The smallest number is {smallest}')






