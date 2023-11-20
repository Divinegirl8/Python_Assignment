def illuminate_unique_values(values):
    return sorted([value for index_value, value in enumerate(values) if values[value] == index_value])


list_v = [3, 3, 1, 1, 2]
print(illuminate_unique_values(list_v))
