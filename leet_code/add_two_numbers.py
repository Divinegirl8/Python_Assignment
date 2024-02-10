def add_two_numbers(l1, l2):
    string_value = ""
    for value in range(len(l1) - 1, -1, -1):
        string_value += str(l1[value])

    string_value2 = ""
    for value2 in range(len(l2) - 1, -1, -1):
        string_value2 += str(l2[value2])

    return change_to_array(str(int(string_value) + int(string_value2))[::-1])


def change_to_array(values):
    new_list = []
    for value in range(len(str(values))):
        new_list.append(values[value])
    return new_list


v = [2, 4, 3]
w = [5, 6, 4]
print(add_two_numbers(v, w))
