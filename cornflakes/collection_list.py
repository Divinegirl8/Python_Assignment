result = [[25, 50, 75],
          [40, 50, 60],
          [75, 65, 80]]
sum_all = 0
average_all = 0
for row in range(len(result)):
    total = 0
    for column in range(len(result)):
        total += result[row][column]

    sum_all += total / len(result)
    average_all = sum_all / len(result)

    print(f"""The average score of value in {row} index is {total / len(result):.1f}""")
print(f"The average of all is {average_all:.1f}")