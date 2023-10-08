tuple2 = ("Orange", [10, 20, 30], [5, 15, 25])

tuples = ()
for row in tuple2:
    for column in row:
        tuples += tuple2[row][column],
print(tuples)
