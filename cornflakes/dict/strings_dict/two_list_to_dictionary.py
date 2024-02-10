def two_list(item, item2):
    return {value1: value2 for index, (value1, value2) in enumerate(zip(item, item2))}


def two_list_dict(item, item2):
    return list([value1, value2] for index, (value1, value2) in enumerate(zip(item, item2)) if value1 != 0)


v = [1,2,0]
v2 = [1,3]

print(two_list_dict(v,v2))