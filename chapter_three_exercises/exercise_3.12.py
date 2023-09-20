number = int(input("Enter a number containing five digits to check if it is a palindrome number: "))

number1 = number // 10000 % 10
number2 = number // 1000 % 10
number3 = number // 100 % 10
number4 = number // 10 % 10
number5 = number  % 10

if number1 == number5:
    print(f'{number} is a palindrome')
else:
    print(f'{number} is not a palindrome')

# this code can be shorter, should we try ??
