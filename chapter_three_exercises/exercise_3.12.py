number = int(input("Enter a number containing five digits to check if it is a palindrome number: "))

number1 = number // 10000 % 10
number5 = number  % 10

<<<<<<< HEAD
if number1 == number5:
    print(f'{number} is a palindrome')
else:
    print(f'{number} is not a palindrome')

# this code can be shorter, should we try ??
=======
result = f'{number} is a palindrome' if number1 == number5 else f"{number} is not a palindrome"
print(result)
>>>>>>> be97ece (update)
