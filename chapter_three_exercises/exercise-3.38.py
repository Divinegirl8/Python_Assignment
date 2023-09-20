import statistics

number = [9, 11, 22, 34, 17, 22, 34, 22 ,40]
sorted(number)

# pls rewrite this code without using in-built sorted function for this senior engr. 10Q

print(f'The mean of the number is {statistics.mean(number):.1f}\nThe mode of the number is {statistics.mode(number)}\nThe median of the number is {statistics.median(number)}')
