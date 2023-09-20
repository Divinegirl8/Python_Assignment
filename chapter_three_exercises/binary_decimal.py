number = input("Enter a number in 0's and 1's: ")
length = len(number)

count = 0
exponential = 0
sum = 0

while count < length:
    result = (int(number) // 10 ** count) % 10
    count += 1
    output = result * 2 ** exponential
    exponential += 1

    sum += output
print(sum)
