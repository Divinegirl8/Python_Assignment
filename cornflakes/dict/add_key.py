def add_value(values, key, value):
    values[key] = value
    return values


sample_value = {0: 10, 1: 20}
print(add_value(sample_value, 3, 30))
