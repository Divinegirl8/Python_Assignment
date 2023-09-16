factorial = 1
sum = 0
for number in range(1,11):
    factorial *= number
    division = 1/factorial
    sum += division
print(f"The constant e value is {sum + 1:.6f}")