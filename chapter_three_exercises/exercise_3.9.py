user_number = int(input("Enter a number containing five digits: "))

count = 5

while count > 0:
    count -= 1
    digit = user_number // 10 ** count % 10
    print(digit, end=" ")
