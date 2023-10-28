dict_value = {}


# print(dict(sorted(data_input.items())))

# for value in range(0, len(data_input) + 1):
#     for num in range(0, len(data_input) + 1):
#         if value > num:
#             num, value = value, num
#             print(data_input[num])

def sort_dict(values):
    for key1 in values.keys():
        for key2 in values.keys():
            if values[key1] < values[key2]:
                values[key1], values[key2] = values[key2], values[key1]
    return values


data_input = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}
print(sort_dict(data_input))
