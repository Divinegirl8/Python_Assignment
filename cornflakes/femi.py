import re


def check_element(value):
    pattern = r'[0-9]+'
    string_val = ""
    count = 0

    for index in range(len(value)):
        string_val += value[index]

    for valu in string_val:
        if re.match(pattern, valu):
            count += 1

    return count


