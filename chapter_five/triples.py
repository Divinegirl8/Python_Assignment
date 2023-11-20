list_value = sum(list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, range(1, 10)))))
print(list_value)

values = sum([value ** 3 for value in range(1, 10) if value % 2 == 0])
print(values)

