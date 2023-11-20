# value = ("a","b","c")
# sort = sorted(value)
# print(list(value) == sort)

def is_sorted(value):
    return all(value[i] <= value[i + 1] for i in range(len(value) - 1))




