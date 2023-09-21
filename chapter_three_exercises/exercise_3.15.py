factorial = 1
sum_number = 0
for number in range(1,11):
    factorial *= number
    division = 1/factorial
    sum_number += division
print(f"The constant e value is {sum_number + 1:.6f}")