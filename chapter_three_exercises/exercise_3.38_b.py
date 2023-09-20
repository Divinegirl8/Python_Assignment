import statistics

number = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]
sorted(number)

# pls no built-in function

print(
    f'The mean of the number is {statistics.mean(number):.1f}\nThe mode of the number is {statistics.mode(number)}\nThe median of the number is {statistics.median(number)}')
