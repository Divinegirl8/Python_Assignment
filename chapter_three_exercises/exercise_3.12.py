number = int(input("Enter a number containing five digits to check if it is a palindrome number: "))

number1 = number // 10000 % 10
number5 = number % 10

result = f'{number} is a palindrome' if number1 == number5 else f"{number} is not a palindrome"
print(result)
