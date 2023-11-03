def split_list(items: list):
    return f'{items[:(len(items) // 2)]},{items[len(items) // 2:len(items)]}'

# def split_list(items: list):
#     return [items[:len(items) // 2], items[len(items) // 2:]]
#
#
# value = [1, 2, 3, 4]
# print(split_list(value))
